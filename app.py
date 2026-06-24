from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
from data_fruit_sizes import FRUIT_SIZES_DATA, find_closest_measurements
import json

app = Flask(__name__)
CORS(app)

@app.route('/api/varieties', methods=['GET'])
def get_varieties():
    """החזר רשימת כל הזנים הזמינים"""
    varieties = sorted(list(FRUIT_SIZES_DATA.keys()))
    return jsonify({
        "success": True,
        "varieties": varieties,
        "count": len(varieties)
    })

@app.route('/api/harvests/<variety>', methods=['GET'])
def get_harvests(variety):
    """החזר סוגי קטיף לזן מסוים"""
    if variety not in FRUIT_SIZES_DATA:
        return jsonify({"success": False, "error": "זן לא נמצא"}), 404
    
    data = FRUIT_SIZES_DATA[variety]
    harvest_types = list(data["harvests"].keys())
    
    return jsonify({
        "success": True,
        "variety": variety,
        "desired_range": data["desired_range"],
        "source": data["source"],
        "harvests": harvest_types
    })

@app.route('/api/recommendations', methods=['POST'])
def get_recommendations():
    """
    מקבל:
    - variety: שם הזן
    - harvest_type: סוג קטיף
    - current_date: תאריך היום (YYYY-MM-DD)
    - current_diameter: קוטר פרי במ"מ
    
    מחזיר:
    - שתי המדידות הקרובות ביותר
    - טווח רצוי
    - הערות מיוחדות אם יש
    """
    try:
        data = request.json
        variety = data.get("variety")
        harvest_type = data.get("harvest_type")
        current_date_str = data.get("current_date")
        current_diameter = data.get("current_diameter")
        
        # בדיקות קלט
        if not all([variety, current_date_str, current_diameter is not None]):
            return jsonify({
                "success": False,
                "error": "חסרים פרמטרים: variety, current_date, current_diameter"
            }), 400
        
        if variety not in FRUIT_SIZES_DATA:
            return jsonify({"success": False, "error": f"זן '{variety}' לא נמצא"}), 404
        
        variety_data = FRUIT_SIZES_DATA[variety]
        
        # אם יש harvest_type, בדוק אותו
        if harvest_type and harvest_type not in variety_data["harvests"]:
            return jsonify({
                "success": False,
                "error": f"סוג קטיף '{harvest_type}' לא נמצא לזן זה"
            }), 404
        
        # המר תאריך
        try:
            current_date = datetime.strptime(current_date_str, "%Y-%m-%d").date()
        except ValueError:
            return jsonify({
                "success": False,
                "error": "פורמט תאריך שגוי. השתמש ב-YYYY-MM-DD"
            }), 400
        
        current_diameter = float(current_diameter)
        
        # אם לא צוין סוג קטיף, השתמש בראשון
        if not harvest_type:
            harvest_type = list(variety_data["harvests"].keys())[0]
        
        # מצא את המדידות הקרובות
        measurements = find_closest_measurements(variety, harvest_type, current_date.isoformat())
        
        if not measurements:
            return jsonify({
                "success": False,
                "error": "לא נמצאו מדידות לתאריך זה"
            }), 404
        
        desired_range = variety_data["desired_range"]
        
        # בנה את התשובה
        response = {
            "success": True,
            "variety": variety,
            "harvest_type": harvest_type,
            "current_date": current_date_str,
            "current_diameter": current_diameter,
            "desired_range": desired_range,
            "source": variety_data["source"],
        }
        
        # הוסף מדידות קרובות
        measurements_response = {}
        
        if measurements["before"]:
            before = measurements["before"]
            measurements_response["before"] = {
                "date": before["date"],
                "range": before["range"]
            }
        
        if measurements["after"]:
            after = measurements["after"]
            measurements_response["after"] = {
                "date": after["date"],
                "range": after["range"]
            }
        
        response["closest_measurements"] = measurements_response
        
        # בדוק אם הקוטר הנוכחי בתוך הטווח הרצוי
        min_range = desired_range.get("min")
        max_range = desired_range.get("max")
        
        in_range = True
        status = "✅ בטווח רצוי"
        
        if min_range and current_diameter < min_range:
            in_range = False
            status = "❌ קטן מדי - צריך להגביר השקיה"
        elif max_range and current_diameter > max_range:
            in_range = False
            status = "❌ גדול מדי - צריך להפחית השקיה"
        
        response["diameter_status"] = {
            "in_range": in_range,
            "status": status
        }
        
        # הוסף הערות מיוחדות
        notes = []
        
        # הערה לליים
        if "ליים" in variety.lower():
            region = None
            if harvest_type and "אזור 1" in harvest_type:
                region = "כינרת / בית שאן"
            elif harvest_type and "אזור 2" in harvest_type:
                region = "עמק החולה"
            
            if region:
                notes.append(f"⚠️ זן זה מגדל בשתי אזוריות שונות. אתה צופה בנתונים עבור אזור: {region}")
        
        # הערה לקלמנטינה מיכל
        if "קלמנטינה מיכל" in variety.lower():
            notes.append("⚠️ הערה: נתונים זמינים עד קטיף נובמבר בלבד. לתקופות מאוחרות יותר, יש להתייעץ עם מומחה.")
        
        if notes:
            response["notes"] = notes
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"שגיאה בעיבוד הבקשה: {str(e)}"
        }), 500

@app.route('/api/all-data/<variety>', methods=['GET'])
def get_all_data(variety):
    """החזר את כל הנתונים לזן מסוים"""
    if variety not in FRUIT_SIZES_DATA:
        return jsonify({"success": False, "error": "זן לא נמצא"}), 404
    
    data = FRUIT_SIZES_DATA[variety]
    return jsonify({
        "success": True,
        "variety": variety,
        "data": data
    })

@app.route('/api/health', methods=['GET'])
def health():
    """בדיקת בריאות השרת"""
    return jsonify({
        "success": True,
        "status": "healthy",
        "total_varieties": len(FRUIT_SIZES_DATA),
        "varieties_list": sorted(list(FRUIT_SIZES_DATA.keys()))
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
