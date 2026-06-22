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

DISCLAIMER = """
⚠️ המידע המוצג הוא המלצה בלבד, המבוססת על רשימות רשמיות.
האחריות המלאה על כל יישום תכשיר הדברה חלה על המשתמש בלבד.
לפני כל שימוש — חובה לקרוא את תווית התכשיר ולהתייעץ עם מדריך מוסמך.
המידע אינו מהווה תחליף למוצהר על תווית תכשיר ההדברה.
"""

SYSTEM_GENERAL = f"""אתה עוזר חקלאי מקצועי לפרדסנים ישראלים המגדלים הדרים ליצוא.
אתה שייך לארגון מגדלי ההדרים בישראל.
אתה עונה בעברית פשוטה, ברורה וידידותית — כמו מדריך חקלאי מנוסה שמדבר עם פרדסן בשדה.
השתמש בשפה יומיומית, לא טכנית מדי.

כללים:
1. ענה אך ורק על פי המאגר שלהלן — אל תמציא מידע
2. מיין חומרים מ-PHI נמוך לגבוה (קרוב לקטיף = ראשון)
3. הצג PHI בבירור — "ימי המתנה לקטיף: X ימים"
4. אם שאלה לא קשורה להדברה בהדרים — אמור בנימוס שאתה מתמחה רק בנושא זה
5. כשמבקשים תווית — ספק קישור ישיר: https://pesticides.moag.gov.il/coim/Documents/GetFile?folder=Import&name=XXXX
6. בסוף כל תשובה הוסף הצהרת אחריות

מאגר הנתונים:
{GENERAL_DATA}

הצהרת אחריות:
{DISCLAIMER}
"""

SYSTEM_SHOHAM = f"""אתה עוזר חקלאי מקצועי למגדלי מנדרינה אורי (Orri) של שוהם ליצוא.
אתה שייך לארגון מגדלי ההדרים בישראל.
אתה עונה בעברית פשוטה, ברורה וידידותית.

כללים חשובים:
1. ענה אך ורק על פי מאגר שוהם שלהלן
2. כשיש "התייעץ עם שהם" — הדגש זאת תמיד עם ⚠️
3. כשחומר משאיר שארית — הזכר שהוא נספר במניין הקבוצה המוגבלת
4. הזכר תמיד: אין להשתמש ביותר מ-2 חומרים מהקבוצה: פריגן/מגדילון + טייגר/PYRIPROXYFEN + אנוידור/סורנטו/מובנטו/SPIRODICLOFEN/SPIROTETRAMAT + נקסטר/PYRIDABEN
5. "לא לגרמניה" — הדגש עם ⚠️ והפנה לשהם
6. מיין חומרים מ-PHI נמוך לגבוה
7. בסוף כל תשובה הוסף הצהרת אחריות

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

    # בדיקת בקשות תווית
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
        max_tokens=1500,
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
        'version': '2.0',
        'labels_count': len(LABELS)
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
