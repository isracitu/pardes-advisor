from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import anthropic
import os
from datetime import datetime
from data_general import GENERAL_DATA
from data_shoham import SHOHAM_DATA
from data_granot import GRANOT_DATA
from data_labels import get_label_url, LABELS
from data_fruit_size import (
    FRUIT_SIZE_DB, VARIETY_KW,
    get_variety_options, get_harvest_months, find_closest_dates
)

app = Flask(__name__)
CORS(app)

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

DISCLAIMER = """
⚠️ **המידע הוא המלצה בלבד.**
האחריות המלאה על כל יישום חלה על המשתמש.
לפני שימוש — קרא את התווית והתייעץ עם מדריך מוסמך.
"""

FORMAT_RULES = """
**פורמט תשובה לחומרי הדברה:**
- אל תשתמש בטבלאות Markdown עם |
- לכל חומר:
🌿 **שם התכשיר**
חומר פעיל: XXX
⏱️ ימי המתנה: X ימים
⚗️ מינון: X
ℹ️ הערה: X
⚠️ אזהרה: X
---
- מיין מ-PHI נמוך לגבוה
- בהתחלה: "מצאתי X חומרים נגד [מזיק], ממוינים מהקרוב לקטיף:"
- בסוף: הצהרת אחריות
"""

SYSTEM_GENERAL = f"""אתה עוזר חקלאי מקצועי לפרדסנים ישראלים.
שייך לארגון מגדלי ההדרים בישראל.
ענה בעברית פשוטה כמו מדריך חקלאי בשדה.

התאריך היום: {datetime.now().strftime('%d/%m/%Y')}

{FORMAT_RULES}

ענה לפי המאגר הזה בלבד:
{GENERAL_DATA}

{DISCLAIMER}
"""

SYSTEM_SHOHAM = f"""אתה עוזר חקלאי למגדלי שוהם (מנדרינה אורי) ליצוא.
שייך לארגון מגדלי ההדרים בישראל.

התאריך היום: {datetime.now().strftime('%d/%m/%Y')}

{FORMAT_RULES}

כללי שוהם - חובה:
1. בראש כל תשובה הצג:
"🟡 **כללי שוהם — חובה לקרוא!**
• אין יותר מ-2 חומרים מהקבוצה: פריגן/מגדילון + PYRIPROXYFEN + SPIRODICLOFEN/SPIROTETRAMAT + PYRIDABEN + IMIDACLOPRID
• חומרים עם שארית נספרים במניין
• בכל ספק — התייעץ עם שהם"
2. חומר עם שארית — ציין "⚠️ נספר בקבוצה המוגבלת"
3. "לא לגרמניה" — ציין "⚠️ לא לגרמניה — התייעץ עם שהם!"

ענה לפי מאגר שוהם בלבד:
{SHOHAM_DATA}

{DISCLAIMER}
"""

SYSTEM_GRANOT = f"""אתה עוזר חקלאי למגדלי גרנות פרש ליצוא.
שייך לארגון מגדלי ההדרים בישראל.

התאריך היום: {datetime.now().strftime('%d/%m/%Y')}

{FORMAT_RULES}

כללי גרנות פרש - חובה:
1. בראש כל תשובה הצג:
"🟢 **כללי גרנות פרש — חובה לקרוא!**
• 🟨 תכשירים מסומנים צהוב = סיכון לשאריות — עד 2 שימושים. חובה לדווח לצוות גרנות-פרש!
• 🟪 תכשירים מסומנים סגול = נאסרו ע"י חלק מהלקוחות — חובה לדווח לצוות גרנות-פרש!
• בכל ספק — התייעץ עם צוות גרנות-פרש"
2. כל חומר מסומן 🟨 בתשובה — ציין במפורש "🟨 דווח לגרנות-פרש!"
3. כל חומר מסומן 🟪 בתשובה — ציין במפורש "🟪 אסור לחלק מהלקוחות — דווח לגרנות-פרש!"

ענה לפי מאגר גרנות פרש בלבד:
{GRANOT_DATA}

{DISCLAIMER}
"""

def detect_variety_in_text(text):
    text_lower = text.lower()
    if 'פומלית ירוקה' in text_lower:
        return 'פומלית ירוקה', False
    if 'פומלית צהובה' in text_lower:
        return 'פומלית צהובה', False
    for kw, variety in VARIETY_KW.items():
        if kw.lower() in text_lower:
            if variety.startswith('_ASK_'):
                return variety, True
            return variety, False
    return None, False

def extract_size_from_text(text):
    import re
    matches = re.findall(r'\b(\d{2,3})\b', text)
    for m in matches:
        n = int(m)
        if 10 <= n <= 200:
            return n
    return None

def format_date_he(month, day):
    months = ['', 'ינואר', 'פברואר', 'מרץ', 'אפריל', 'מאי', 'יוני',
              'יולי', 'אוגוסט', 'ספטמבר', 'אוקטובר', 'נובמבר', 'דצמבר']
    return f"{day} ב{months[month]}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    grower_type = data.get('grower_type', 'general')
    fruit_context = data.get('fruit_context', {})
    history = data.get('history', [])
    mode = data.get('mode', 'pesticide')  # pesticide / fruit

    if not user_message and not fruit_context.get('active'):
        return jsonify({'error': 'No message'}), 400

    # מצב גודל פרי
    if mode == 'fruit' or fruit_context.get('active'):
        return handle_fruit_size(user_message, fruit_context, history)

    # מצב חומרי הדברה
    if grower_type == 'shoham':
        system = SYSTEM_SHOHAM
    elif grower_type == 'granot':
        system = SYSTEM_GRANOT
    else:
        system = SYSTEM_GENERAL

    label_links = []
    if 'תווית' in user_message.lower():
        for name in LABELS:
            if name in user_message:
                info = get_label_url(name)
                if info:
                    label_links.append(info)

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
        'type': 'pesticide'
    })

def handle_fruit_size(user_message, ctx, history):
    """לוגיקת גודל פרי"""
    if not ctx.get('variety'):
        variety, needs_ask = detect_variety_in_text(user_message)
        if not variety:
            return jsonify({
                'reply': 'אנא בחר זן או כתוב את שמו (לדוגמה: ניוהול, אורי, פומלית, אשכולית).',
                'type': 'fruit_size',
                'fruit_context': {'active': True},
                'options': {
                    'question': 'variety_type',
                    'choices': [
                        {'label': '🍊 ניוהול', 'value': 'ניוהול'},
                        {'label': '🟡 אורי', 'value': 'אורי'},
                        {'label': '🍋 פומלית ירוקה', 'value': 'פומלית ירוקה'},
                        {'label': '🟢 פומלית צהובה', 'value': 'פומלית צהובה'},
                        {'label': '🔴 אשכולית אדומה', 'value': 'אשכולית אדומה'},
                        {'label': '🟠 פומלו אדום', 'value': 'פומלו אדום'},
                        {'label': '🍊 מינאולה', 'value': 'מינאולה'},
                        {'label': '🟠 קלמנטינה מיכל', 'value': 'קלמנטינה מיכל'},
                        {'label': '🟡 הדס', 'value': 'הדס'},
                        {'label': '🟢 ליים', 'value': 'ליים'},
                        {'label': '🟠 קרה קרה', 'value': 'קרה קרה'},
                    ]
                }
            })

        if variety == '_ASK_פומלית':
            return jsonify({
                'reply': 'איזו פומלית? 🍋',
                'type': 'fruit_size',
                'fruit_context': {'active': True},
                'options': {
                    'question': 'variety_type',
                    'choices': [
                        {'label': '🟢 פומלית ירוקה', 'value': 'פומלית ירוקה'},
                        {'label': '🟡 פומלית צהובה', 'value': 'פומלית צהובה'},
                    ]
                }
            })

        ctx['variety'] = variety
        size = extract_size_from_text(user_message)
        if size:
            ctx['fruit_size'] = size

    variety = ctx.get('variety')

    sub_options = get_variety_options(variety)
    if sub_options and not ctx.get('sub_variety'):
        return jsonify({
            'reply': f'איזה סוג של {variety}?',
            'type': 'fruit_size',
            'fruit_context': ctx,
            'options': {
                'question': 'sub_variety',
                'choices': [{'label': f'📋 {s}', 'value': s} for s in sub_options]
            }
        })

    sub_variety = ctx.get('sub_variety')

    if not ctx.get('harvest_month'):
        months = get_harvest_months(variety, sub_variety)
        if not months:
            return jsonify({
                'reply': f'אין לי מידע על {variety}.',
                'type': 'fruit_size',
                'fruit_context': {}
            })
        if len(months) == 1:
            ctx['harvest_month'] = months[0]
        else:
            return jsonify({
                'reply': f'באיזה חודש אתה מתכנן לקטוף?',
                'type': 'fruit_size',
                'fruit_context': ctx,
                'options': {
                    'question': 'harvest_month',
                    'choices': [{'label': f'📅 {m}', 'value': m} for m in months]
                }
            })

    harvest_month = ctx['harvest_month']

    if not ctx.get('fruit_size'):
        size = extract_size_from_text(user_message)
        if size:
            ctx['fruit_size'] = size
        else:
            return jsonify({
                'reply': f'מה הגודל של הפרי שלך כרגע (במ"מ)?',
                'type': 'fruit_size',
                'fruit_context': ctx
            })

    fruit_size = ctx['fruit_size']

    today = datetime.now()
    result = find_closest_dates(variety, sub_variety, harvest_month, today.month, today.day)

    if not result or (not result['before'] and not result['after']):
        return jsonify({
            'reply': f'אין נתונים בטבלה לתאריך הנוכחי עבור {variety} - {harvest_month}.',
            'type': 'fruit_size',
            'fruit_context': {},
            'show_followup': True
        })

    today_str = today.strftime('%d/%m/%Y')
    variety_full = f"{variety} ({sub_variety})" if sub_variety else variety

    reply = f"📊 **{variety_full} — קטיף {harvest_month}**\n"
    reply += f"תאריך היום: {today_str}\n"
    reply += f"הפרי שלך: **{fruit_size} מ\"מ**\n\n"

    if result['before']:
        (m, d), mn, mx = result['before']
        reply += f"📅 לפי ה-{format_date_he(m, d)}: הטווח הרצוי **{mn}-{mx} מ\"מ**\n"
    if result['after']:
        (m, d), mn, mx = result['after']
        if result['before'] != result['after']:
            reply += f"📅 לפי ה-{format_date_he(m, d)}: הטווח הרצוי **{mn}-{mx} מ\"מ**\n"

    reply += "\n"

    relevant = result['before'] if result['before'] else result['after']
    _, mn, mx = relevant

    if fruit_size < mn:
        status = f"🔴 **הפרי שלך מתחת לטווח המומלץ**"
    elif fruit_size > mx:
        status = f"🟠 **הפרי שלך מעל הטווח המומלץ**"
    else:
        status = f"🟢 **הפרי שלך בטווח המומלץ**"

    reply += f"{status}\n\n"
    reply += DISCLAIMER

    return jsonify({
        'reply': reply,
        'type': 'fruit_size',
        'fruit_context': {},
        'show_followup': True
    })

@app.route('/fruit_select', methods=['POST'])
def fruit_select():
    data = request.json
    question = data.get('question')
    value = data.get('value')
    ctx = data.get('fruit_context', {})

    if question == 'variety_type':
        ctx['variety'] = value
    elif question == 'sub_variety':
        ctx['sub_variety'] = value
    elif question == 'harvest_month':
        ctx['harvest_month'] = value

    ctx['active'] = True
    return handle_fruit_size("", ctx, [])

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'ok',
        'message': 'עוזרת הפרדס פעילה',
        'version': '4.1',
        'features': ['general', 'shoham', 'granot', 'fruit_size'],
        'varieties': len(FRUIT_SIZE_DB),
        'labels_count': len(LABELS)
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
