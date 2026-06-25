from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from datetime import datetime
from data_fruit_sizes import FRUIT_SIZES_DATA, find_closest_measurements
from data_pesticides import PESTS_AND_TREATMENTS, list_all_pests, search_treatment, get_pest_treatments, build_pests_context
import json
import os

app = Flask(__name__, static_folder='templates', static_url_path='')
CORS(app)

# ===== דפים =====

@app.route('/')
def index():
    return send_from_directory('templates', 'index.html')

@app.route('/widget')
def widget():
    return send_from_directory('templates', 'index.html')

# ===== API גודל פרי =====

@app.route('/api/varieties', methods=['GET'])
def get_varieties():
    varieties = sorted(list(FRUIT_SIZES_DATA.keys()))
    return jsonify({"success": True, "varieties": varieties, "count": len(varieties)})

@app.route('/api/harvests/<variety>', methods=['GET'])
def get_harvests(variety):
    if variety not in FRUIT_SIZES_DATA:
        return jsonify({"success": False, "error": "זן לא נמצא"}), 404
    data = FRUIT_SIZES_DATA[variety]
    return jsonify({
        "success": True, "variety": variety,
        "desired_range": data["desired_range"],
        "source": data["source"],
        "harvests": list(data["harvests"].keys())
    })

@app.route('/api/recommendations', methods=['POST'])
def get_recommendations():
    try:
        data = request.json
        variety = data.get("variety")
        harvest_type = data.get("harvest_type")
        current_date_str = data.get("current_date")
        current_diameter = data.get("current_diameter")

        if not all([variety, current_date_str, current_diameter is not None]):
            return jsonify({"success": False, "error": "חסרים פרמטרים"}), 400

        if variety not in FRUIT_SIZES_DATA:
            return jsonify({"success": False, "error": f"זן '{variety}' לא נמצא"}), 404

        variety_data = FRUIT_SIZES_DATA[variety]

        if harvest_type and harvest_type not in variety_data["harvests"]:
            return jsonify({"success": False, "error": f"סוג קטיף '{harvest_type}' לא נמצא"}), 404

        try:
            current_date = datetime.strptime(current_date_str, "%Y-%m-%d").date()
        except ValueError:
            return jsonify({"success": False, "error": "פורמט תאריך שגוי. YYYY-MM-DD"}), 400

        current_diameter = float(current_diameter)

        if not harvest_type:
            harvest_type = list(variety_data["harvests"].keys())[0]

        measurements = find_closest_measurements(variety, harvest_type, current_date.isoformat())
        if not measurements:
            return jsonify({"success": False, "error": "לא נמצאו מדידות לתאריך זה"}), 404

        desired_range = variety_data["desired_range"]
        response = {
            "success": True, "variety": variety, "harvest_type": harvest_type,
            "current_date": current_date_str, "current_diameter": current_diameter,
            "desired_range": desired_range, "source": variety_data["source"],
        }

        measurements_response = {}
        if measurements["before"]:
            measurements_response["before"] = {"date": measurements["before"]["date"], "range": measurements["before"]["range"]}
        if measurements["after"]:
            measurements_response["after"] = {"date": measurements["after"]["date"], "range": measurements["after"]["range"]}
        response["closest_measurements"] = measurements_response

        min_r = desired_range.get("min")
        max_r = desired_range.get("max")
        in_range = True
        status = "בטווח רצוי"
        if min_r and current_diameter < min_r:
            in_range = False
            status = "קטן מדי - צריך להגביר השקיה"
        elif max_r and current_diameter > max_r:
            in_range = False
            status = "גדול מדי - צריך להפחית השקיה"
        response["diameter_status"] = {"in_range": in_range, "status": status}

        notes = []
        if "ליים" in variety.lower():
            if harvest_type and "אזור 1" in harvest_type:
                notes.append("זן זה מגדל בשתי אזוריות שונות. אתה צופה בנתונים עבור אזור: כינרת / בית שאן")
            elif harvest_type and "אזור 2" in harvest_type:
                notes.append("זן זה מגדל בשתי אזוריות שונות. אתה צופה בנתונים עבור אזור: עמק החולה")
        if "קלמנטינה מיכל" in variety.lower():
            notes.append("נתונים זמינים עד קטיף נובמבר בלבד.")
        if notes:
            response["notes"] = notes

        return jsonify(response)
    except Exception as e:
        return jsonify({"success": False, "error": f"שגיאה: {str(e)}"}), 500

# ===== API תכשירי הדברה =====

@app.route('/api/pests', methods=['GET'])
def get_pests_list():
    return jsonify({"success": True, "pests": list_all_pests(), "count": len(list_all_pests())})

@app.route('/api/pest/<pest_name>', methods=['GET'])
def get_pest_info(pest_name):
    pest_data = get_pest_treatments(pest_name)
    if not pest_data:
        return jsonify({"success": False, "error": f"מזיק '{pest_name}' לא נמצא"}), 404
    return jsonify({
        "success": True,
        "pest_hebrew": pest_data["שם_עברי"],
        "pest_scientific": pest_data["שם_מדעי"],
        "treatments": pest_data["תכשירים"],
        "count": len(pest_data["תכשירים"])
    })

@app.route('/api/search-treatment', methods=['GET'])
def search_treatments():
    q = request.args.get('q', '').strip()
    if not q:
        return jsonify({"success": False, "error": "צריך מילת חיפוש"}), 400
    results = search_treatment(q)
    return jsonify({"success": True, "search_term": q, "results": results, "count": len(results)})

# ===== API צ'אט =====

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        import anthropic

        data = request.json
        question = data.get('question', '').strip()
        if not question:
            return jsonify({"success": False, "error": "אנא שלח שאלה"}), 400

        # בנה context מלא - כל הנתונים, לא חתוכים
        pests_ctx = build_pests_context()

        varieties_list = sorted(FRUIT_SIZES_DATA.keys())
        fruit_lines = []
        for v in varieties_list:
            vd = FRUIT_SIZES_DATA[v]
            dr = vd.get("desired_range", {})
            fruit_lines.append(f"- {v}: טווח רצוי {dr.get('min','?')}-{dr.get('max','?')} מ\"מ, סוגי קטיף: {', '.join(vd['harvests'].keys())}")
        fruit_ctx = "\n".join(fruit_lines)

        system_prompt = f"""אתה "עוזרת הפרדס" - יועצת מקצועית לחקלאי הדרים בישראל.

כללים חשובים:
1. ענה רק על סמך הנתונים שלהלן. אם אין לך מידע - אמור בבירור "אין לי מידע על כך".
2. אל תמציא שום נתון, תכשיר, או המלצה.
3. ענה בעברית ברורה ופשוטה.
4. תשובות קצרות וישירות.

=== נתוני גודל פרי (13 זנים) ===
{fruit_ctx}

=== תכשירי הדברה מורשים ===
{pests_ctx}

מקור הנתונים: משרד החקלאות, מהדורה 2026."""

        client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))
        message = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=600,
            system=system_prompt,
            messages=[{"role": "user", "content": question}]
        )

        return jsonify({"success": True, "question": question, "answer": message.content[0].text})

    except Exception as e:
        return jsonify({"success": False, "error": f"שגיאה: {str(e)}"}), 500

# ===== Health =====

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({
        "success": True, "status": "healthy",
        "total_varieties": len(FRUIT_SIZES_DATA),
        "total_pests": len(PESTS_AND_TREATMENTS),
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
