# Fruit size guidelines - Ministry of Agriculture 2026
# מדריך גודל פרי - משרד החקלאות 2026
# Source: "השקיית הדרים על פי גודל הפרי - 2026"

FRUIT_SIZE_DATA = {
    "אשכולית אדומה": {
        "min_mm": 92,
        "max_mm": 162,
        "description": "קטיף בכיר (ספטמבר-אוקטובר)",
        "harvest_months": ["ספטמבר", "אוקטובר"],
        "market": "יצוא"
    },
    "אשכולית אדומה - שוק מקומי": {
        "min_mm": 92,
        "max_mm": 125,
        "description": "קטיף סלקטיבי בסתיו וקטיף משלים בסוף העונה (פברואר-מרס)",
        "harvest_months": ["פברואר", "מרס"],
        "market": "שוק מקומי"
    },
    "פומלית ירוקה": {
        "min_mm": 122,
        "max_mm": 162,
        "description": "קטיף (ספטמבר-אוקטובר)",
        "harvest_months": ["ספטמבר", "אוקטובר"],
        "market": "יצוא"
    },
    "פומלית צהובה": {
        "min_mm": 112,
        "max_mm": None,  # ללא הגבלה עליונה בשוק מקומי
        "description": "שוק מקומי (ינואר)",
        "harvest_months": ["ינואר"],
        "market": "שוק מקומי"
    },
    "פומלו אדום": {
        "min_mm": 122,
        "max_mm": 162,
        "description": "קטיף (ספטמבר-אוקטובר)",
        "harvest_months": ["ספטמבר", "אוקטובר"],
        "market": "יצוא"
    },
    "מינאולה": {
        "min_mm": 25,
        "max_mm": 85,
        "description": "קטיף (דצמבר)",
        "harvest_months": ["דצמבר"],
        "market": "יצוא"
    },
    "אורי": {
        "min_mm": 22,
        "max_mm": 82,
        "description": "קטיף (פברואר)",
        "harvest_months": ["פברואר"],
        "market": "יצוא"
    },
    "ניוהול": {
        "min_mm": 82,
        "max_mm": 122,
        "description": "קטיף סלקטיבי ומשלים (נובמבר-פברואר)",
        "harvest_months": ["נובמבר", "דצמבר", "ינואר", "פברואר"],
        "market": "יצוא"
    },
    "קלמנטינה": {
        "min_mm": 22,
        "max_mm": 82,
        "description": "קטיף סלקטיבי ומשלים (נובמבר-דצמבר)",
        "harvest_months": ["נובמבר", "דצמבר"],
        "market": "יצוא"
    },
    "מנדרינה הדס": {
        "min_mm": 22,
        "max_mm": 82,
        "description": "קטיף (ינואר-אפריל)",
        "harvest_months": ["ינואר", "פברואר", "מרס", "אפריל"],
        "market": "יצוא"
    },
    "ליים": {
        "min_mm": 52,
        "max_mm": 72,
        "description": "קטיף (יולי-אוגוסט) — עמק החולה וכינרת",
        "harvest_months": ["יולי", "אוגוסט"],
        "market": "יצוא"
    },
    "קרה קרה - שוק מקומי": {
        "min_mm": 85,
        "max_mm": 122,
        "description": "קטיף סלקטיבי (נובמבר-פברואר)",
        "harvest_months": ["נובמבר", "דצמבר", "ינואר", "פברואר"],
        "market": "שוק מקומי"
    },
    "קרה קרה": {
        "min_mm": 72,
        "max_mm": 92,
        "description": "יצוא (ינואר-פברואר)",
        "harvest_months": ["ינואר", "פברואר"],
        "market": "יצוא"
    }
}

def get_fruit_size_range(variety):
    """
    חזור טווח גודל פרי לזן מסוים
    
    Args:
        variety (str): שם הזן (כפי שהוא מופיע בטבלה)
    
    Returns:
        dict: {"min_mm": int, "max_mm": int, "description": str}
              או None אם הזן לא קיים
    """
    if variety in FRUIT_SIZE_DATA:
        data = FRUIT_SIZE_DATA[variety]
        return {
            "min_mm": data["min_mm"],
            "max_mm": data["max_mm"],
            "description": data["description"],
            "harvest_months": data["harvest_months"],
            "market": data["market"]
        }
    return None

def get_all_varieties():
    """חזור רשימה של כל הזנים הזמינים"""
    return list(FRUIT_SIZE_DATA.keys())

def format_size_recommendation(variety, current_size_mm=None):
    """
    פורמט המלצה על גודל פרי
    
    Args:
        variety (str): שם הזן
        current_size_mm (int, optional): גודל פרי נוכחי (אם ידוע)
    
    Returns:
        str: טקסט המלצה יפה
    """
    data = get_fruit_size_range(variety)
    
    if not data:
        return f"לא מצאתי מידע על זן '{variety}'"
    
    min_mm = data["min_mm"]
    max_mm = data["max_mm"]
    description = data["description"]
    harvest_months = ", ".join(data["harvest_months"])
    market = data["market"]
    
    result = f"""
🍊 **{variety}**
   טווח רצוי: {min_mm}-{max_mm if max_mm else '∞'} מ״מ
   קטיפים: {harvest_months}
   שוק: {market}
   הערה: {description}
"""
    
    if current_size_mm:
        if current_size_mm < min_mm:
            result += f"   ⚠️ הפרי שלך ({current_size_mm} מ״מ) **קטן מדי** — צריך להעלות השקיה\n"
        elif max_mm and current_size_mm > max_mm:
            result += f"   ⚠️ הפרי שלך ({current_size_mm} מ״מ) **גדול מדי** — צריך להפחית השקיה\n"
        else:
            result += f"   ✅ הפרי שלך ({current_size_mm} מ״מ) **בטווח הנכון**\n"
    
    return result
