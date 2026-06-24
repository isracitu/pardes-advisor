from flask import Flask, request, jsonify
from flask_cors import CORS
import anthropic
import os
from data_general import GENERAL_DATA
from data_shoham import SHOHAM_DATA
from data_labels import get_label_url, LABELS

app = Flask(__name__)
CORS(app)

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

FORMAT_RULES = """
**חשוב מאוד — פורמט תשובה:**
- אל תשתמש בטבלאות Markdown עם | בכלל!
- השב בפורמט הבא לכל חומר:

🌿 **שם התכשיר**
חומר פעיל: XXX
⏱️ ימי המתנה לקטיף: X ימים
⚗️ מינון: X
ℹ️ הערה: X (אם יש)
⚠️ אזהרה: X (אם יש)
📋 [קישור לתווית]

---

- הפרד בין חומרים עם קו: ---
- מיין מהקרוב לקטיף לרחוק ביותר
- בהתחלה — הוסף שורה אחת: "מצאתי X חומרים נגד [שם המזיק], ממוינים מהקרוב לקטיף:"
- בסוף — הוסף הצהרת אחריות
"""

DISCLAIMER = """
⚠️ **המידע הוא המלצה בלבד.**
האחריות המלאה על כל יישום חלה על המשתמש.
לפני שימוש — קרא את התווית והתייעץ עם מדריך מוסמך.
"""

SYSTEM_GENERAL = f"""אתה עוזר חקלאי מקצועי לפרדסנים ישראלים המגדלים הדרים ליצוא.
שייך לארגון מגדלי ההדרים בישראל.
ענה בעברית פשוטה, ברורה וידידותית — כמו מדריך חקלאי מנוסה שמדבר עם פרדסן בשדה.

{FORMAT_RULES}

כללים:
1. ענה אך ורק על פי המאגר שלהלן
2. מיין חומרים מ-PHI נמוך לגבוה
3. אם שאלה לא קשורה להדברה בהדרים — אמור שאתה מתמחה רק בנושא זה
4. כשמבקשים תווית — ספק קישור: https://pesticides.moag.gov.il/coim/Documents/GetFile?folder=Import&name=XXXX

מאגר הנתונים:
{GENERAL_DATA}

הצהרת אחריות:
{DISCLAIMER}
"""

SYSTEM_SHOHAM = f"""אתה עוזר חקלאי מקצועי למגדלי מנדרינה אורי (Orri) של שוהם ליצוא.
שייך לארגון מגדלי ההדרים בישראל.
ענה בעברית פשוטה וידידותית.

{FORMAT_RULES}

כללים חשובים:
1. ענה אך ורק על פי מאגר שוהם
2. בתחילת כל תשובה — הוסף תיבת אזהרה של שוהם:
   "🟡 **כללי שוהם — חובה לקרוא!**
   • אין להשתמש ביותר מ-2 חומרים מהקבוצה: פריגן/מגדילון + PYRIPROXYFEN + SPIRODICLOFEN/SPIROTETRAMAT + PYRIDABEN + IMIDACLOPRID
   • חומרים עם שארית נספרים במניין
   • בכל ספק — התייעץ עם שהם"
3. כשחומר משאיר שארית — ציין במפורש "⚠️ נספר בקבוצה המוגבלת"
4. "לא לגרמניה" — ציין "⚠️ לא לגרמניה — התייעץ עם שהם!"
5. מיין מ-PHI נמוך לגבוה

מאגר שוהם — מנדרינה אורי 2026-2027:
{SHOHAM_DATA}

הצהרת אחריות:
{DISCLAIMER}
"""

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    is_shoham = data.get('is_shoham', False)
    history = data.get('history', [])

    if not user_message:
        return jsonify({'error': 'No message'}), 400

    label_links = []
    msg_lower = user_message.lower()
    if 'תווית' in msg_lower:
        for name in LABELS:
            if name in user_message:
                info = get_label_url(name)
                if info:
                    label_links.append(info)

    system = SYSTEM_SHOHAM if is_shoham else SYSTEM_GENERAL
    messages = history[-10:] + [{"role": "user", "content": user_message}]

    if label_links:
        extra = "\n\nקישורי תוויות:\n"
        for l in label_links:
            extra += f"- {l['name']}: {l['url']}\n"
        messages[-1]["content"] += extra

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2000,
        system=system,
        messages=messages
    )

    return jsonify({
        'reply': response.content[0].text,
        'label_links': label_links,
        'is_shoham': is_shoham
    })

@app.route('/label', methods=['GET'])
def get_label():
    name = request.args.get('name', '')
    if not name:
        return jsonify({'error': 'נדרש שם תכשיר'}), 400
    result = get_label_url(name)
    if result:
        return jsonify(result)
    return jsonify({'error': f'לא נמצאה תווית עבור {name}',
                    'fallback': 'https://pesticides.moag.gov.il'}), 404

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'ok',
        'message': 'עוזרת הפרדס פעילה',
        'version': '2.1',
        'labels_count': len(LABELS)
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
