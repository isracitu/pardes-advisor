# 🍊 עוזרת הפרדס - מערכת חישוב קוטר פרי ממוצע רצוי

מערכת מתקדמת לעזור לחקלאי הדרים בישראל בחישוב קוטר פרי ממוצע רצוי בהתאם לתאריך, זן, וסוג קטיף.

## ✨ תכונות

✅ **14 זנים שונים** - כל הזנים הזמינים במערכת משרד החקלאות  
✅ **מדידות מדויקות** - תאריכים וטווחים מ-משרד החקלאות 2026  
✅ **מדידות קרובות** - מציאת שתי המדידות הקרובות ביותר לתאריך הנוכחי  
✅ **הערות מיוחדות** - התמודדות עם ליים (שתי אזוריות) וקלמנטינה מיכל  
✅ **ממשק נוח** - ממשק עברי מתגובב אינטואיטיבי  
✅ **API ברור** - REST API בעברית ללא תלויות חיצוניות

---

## 📂 מבנה הקבצים

```
pardes-server/
├── app.py                    # Flask server ראשי
├── data_fruit_sizes.py      # מבנה נתונים מלא
├── requirements.txt         # Python dependencies
├── test_pardes_advisor.html # ממשק HTML
└── README.md               # קובץ זה
```

---

## 🚀 התקנה

### 1️⃣ דרישות מקדימות
- Python 3.8+
- pip (Python package manager)

### 2️⃣ התקן dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ הרץ את השרת
```bash
python app.py
```

השרת יפעל ב: `http://localhost:5000`

---

## 🎯 שימוש

### דרך ממשק HTML

1. פתח את `test_pardes_advisor.html` בדפדפן
2. בחר זן, סוג קטיף, תאריך, וקוטר פרי
3. לחץ על "חפש"
4. קבל את המדידות הקרובות והמלצות

### דרך API

#### 1. קבל רשימת זנים
```bash
curl http://localhost:5000/api/varieties
```

**תשובה:**
```json
{
  "success": true,
  "varieties": ["אורי", "אשכולית אדומה - קטיף בכיר", ...],
  "count": 14
}
```

#### 2. קבל סוגי קטיף לזן
```bash
curl http://localhost:5000/api/harvests/אורי
```

**תשובה:**
```json
{
  "success": true,
  "variety": "אורי",
  "desired_range": {"min": 22, "max": 82},
  "source": "משרד החקלאות",
  "harvests": ["קטיף פברואר"]
}
```

#### 3. קבל המלצות (POST)
```bash
curl -X POST http://localhost:5000/api/recommendations \
  -H "Content-Type: application/json" \
  -d '{
    "variety": "אורי",
    "harvest_type": "קטיף פברואר",
    "current_date": "2026-06-24",
    "current_diameter": 30
  }'
```

**תשובה:**
```json
{
  "success": true,
  "variety": "אורי",
  "harvest_type": "קטיף פברואר",
  "current_date": "2026-06-24",
  "current_diameter": 30,
  "desired_range": {"min": 22, "max": 82},
  "closest_measurements": {
    "before": {
      "date": "2026-06-15",
      "range": {"min": 21, "max": 41}
    },
    "after": {
      "date": "2026-07-01",
      "range": {"min": 27, "max": 47}
    }
  },
  "diameter_status": {
    "in_range": false,
    "status": "❌ קטן מדי - צריך להגביר השקיה"
  }
}
```

---

## 🌳 הערות מיוחדות

### ליים - שתי אזוריות
- **אזור 1**: כינרת + בית שאן (אמצע יולי)
- **אזור 2**: עמק החולה (סוף יולי + אוגוסט)

כל אזור יש טווח שונה. בחר לפי אזור הגידול שלך.

### קלמנטינה מיכל
נתונים זמינים עד קטיף נובמבר בלבד.  
לתקופות מאוחרות יותר - התייעץ עם מומחה.

---

## 🔧 דפלוימנט ל-Render

### 1. הכן את הקבצים
```bash
# צור תיקייה
mkdir pardes-server
cd pardes-server

# העתק את הקבצים
cp app.py data_fruit_sizes.py requirements.txt .
```

### 2. צור Procfile
```bash
cat > Procfile << EOF
web: gunicorn app:app
EOF
```

### 3. דחוף ל-GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git push origin main
```

### 4. הצע ל-Render

1. התחבר ל- [render.com](https://render.com)
2. New → Web Service
3. חבר את ה-GitHub repo
4. הגדר:
   - **Start Command**: `gunicorn app:app`
   - **Port**: 5000

---

## 📊 13 זנים זמינים

1. אורי
2. אשכולית אדומה - קטיף בכיר
3. אשכולית אדומה - קטיף סלקטיבי
4. טבורי ניוהול
5. טבורי קרה קרה - שוק מקומי
6. טבורי קרה קרה - יצוא
7. קלמנטינה מיכל
8. ליים
9. מינאואלה
10. מנדרינה הדס
11. פומלה אדום
12. פומלית ירוקה
13. פומלית צהובה - שוק מקומי

---

## ⚖️ כתב הצהרת

**⚠️ הערה משפטית חשובה:**

המידע בעוזרת זו הוא המלצה בלבד.  
המשתמש נושא את **האחריות המלאה** לגבי החלטותיו בנוגע להשקיה וקטיף.

יש להתייעץ עם מומחה לאישור הנתונים לתנאים הספציפיים של החלקה שלך.

---

## 📞 תמיכה

נתונים מקור:  
📄 משרד החקלאות ופיתוח הכפר  
🏢 שירות ההדרכה והמקצוע  
📍 אגף הפירות, תחום הדרים

---

## 📝 ניסוח

*עוזרת הפרדס* - מערכת עזר לחקלאים בחישוב קוטר פרי ממוצע רצוי  
גרסה: 5.0 (מלא נתונים)  
תאריך: יוני 2026
