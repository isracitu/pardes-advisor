# עוזרת הפרדס — Pardes Advisor

## סקירה כללית
עוזרת חכמה בעברית לחקלאים בישראל המגדלים הדרים (citrus) ליצוא. השרת מספק המלצות בזמן אמת על חומרים לחסל מזיקים, ממוינות לפי PHI (ימי המתנה לקטיף).

## תכונות
- 🤖 ממשק שיחה טבעי בעברית עם Claude AI
- 🍊 תמיכה בשני מצבים: **רשימה כללית** (משרד החקלאות) ו-**שוהם אורי** (רשימה מיוחדת)
- 📋 מיון אוטומטי לפי PHI
- 🔗 קישורים לתוויות רשמיות (pesticides.moag.gov.il)
- 📏 חישובי גודל פרי לפי זן ותאריך (11 זנים מטופלים)
- ⚖️ הצהרות אחריות משפטיות מובנות

## Architecture

```
frontend (Wix HTML widget)
         ↓
Flask server (Render free tier)
  ├── app.py (main server)
  ├── data_general.py (רשימת משרד החקלאות)
  ├── data_shoham.py (רשימת שוהם)
  ├── data_labels.py (מיפוי תוויות)
  └── data_fruit_size.py (גדלים לפי זן)
         ↓
    Claude API (Anthropic)
```

## API Endpoints

### POST /api/chat
שאלה ותשובה בסיסית על חומרים.

**Request:**
```json
{
  "message": "יש לי זבוב בפרי שלי, מה עושים?",
  "session_id": "user_123",
  "is_shoham": false
}
```

**Response:**
```json
{
  "response": "המלצות על חומרים...",
  "session_id": "user_123",
  "is_shoham": false
}
```

### POST /api/fruit-size
חישוב גודל פרי רצוי.

**Request:**
```json
{
  "variety": "ניוהול",
  "current_size_mm": 30
}
```

**Response:**
```json
{
  "variety": "ניוהול",
  "recommendation": "טווח רצוי: 82-122 מ״מ. הפרי שלך קטן מדי..."
}
```

### GET /api/varieties
קבל רשימת כל הזנים הזמינים.

### GET /api/health
בדוק אם השרת כן בחיים.

## Development

### Local Setup
```bash
git clone https://github.com/isracitu/pardes-advisor.git
cd pardes-advisor
python -m venv venv
source venv/bin/activate  # Unix/Mac
pip install -r requirements.txt
export ANTHROPIC_API_KEY="your-key-here"
python app.py
```

### Testing
```bash
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"שלום","is_shoham":false}'
```

## Deployment

### Render (Recommended)
1. קישר את GitHub repository ל-Render
2. בחר `render.yaml` כמו build config
3. הוסף `ANTHROPIC_API_KEY` ב-Environment Variables
4. Deploy!

שרת יהיה זמין ב-`https://pardes-advisor.onrender.com`

## Data Structure

### Fruit Sizes (data_fruit_size.py)
```python
FRUIT_SIZE_DATA = {
    "ניוהול": {
        "min_mm": 82,
        "max_mm": 122,
        "harvest_months": ["נובמבר", "דצמבר", "ינואר", "פברואר"],
        "market": "יצוא"
    },
    ...
}
```

זנים כלולים:
- אשכולית אדומה
- פומלית ירוקה / צהובה
- פומלו
- מינאולה
- אורי
- ניוהול
- קלמנטינה
- מנדרינה הדס
- ליים
- קרה קרה

## שוהם (Shoham) Mode

רשימה מיוחדת למנדרינה אורי עם:
- הגבלות על ספירת חומרים
- תאריכים מוגבלים
- דרישות התייעצות עם מדריך משק
- שוהם קיבלה אישור בעל פה + במייל לשימוש בנתוני הרשימה

## License
רק לשימוש על ידי ארגון מגדלי ההדרים בישראל ובעלים מורשים.

## Contact
Daniel Klusky
Israeli Citrus Growers Organization
קישור: www.hapardes.com
