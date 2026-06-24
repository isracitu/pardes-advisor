from flask import Flask, request, jsonify
from flask_cors import CORS
from anthropic import Anthropic
import json
from datetime import datetime

# Import data modules
from data_general import PESTS_GENERAL, PRODUCTS_GENERAL
from data_shoham import PESTS_SHOHAM, PRODUCTS_SHOHAM, SHOHAM_RULES
from data_labels import PRODUCT_LABELS

app = Flask(__name__)
CORS(app)

# Initialize Anthropic client
client = Anthropic()

# Store conversation history per session
conversations = {}

def get_or_create_conversation(session_id):
    """Get or create a conversation for a session"""
    if session_id not in conversations:
        conversations[session_id] = []
    return conversations[session_id]

def format_pesticide_recommendation(products, mode="general"):
    """Format pesticide products with PHI sorting"""
    if not products:
        return "לא נמצאו חומרים מתאימים."
    
    # Sort by PHI (pre-harvest interval)
    sorted_products = sorted(
        products,
        key=lambda x: x.get("phi_days", float('inf'))
    )
    
    result = "🍊 **חומרים מאושרים:**\n\n"
    
    for product in sorted_products[:5]:  # Top 5
        name = product.get("name", "?")
        pest = product.get("pest", "?")
        phi = product.get("phi_days", "?")
        rate = product.get("rate", "?")
        notes = product.get("notes", "")
        doc_id = product.get("doc_id", None)
        
        result += f"**{name}**\n"
        result += f"  🐛 מזיק: {pest}\n"
        result += f"  ⏰ PHI: {phi} ימים\n"
        result += f"  📊 קצב: {rate}\n"
        
        if doc_id:
            label_url = f"https://pesticides.moag.gov.il/LabelView/{doc_id}"
            result += f"  📄 [תווית רשמית]({label_url})\n"
        
        if notes:
            result += f"  ⚠️ הערות: {notes}\n"
        
        result += "\n"
    
    return result

def format_shoham_warning(products):
    """Format special Shoham warnings if needed"""
    warning = ""
    
    has_compound_limits = any(
        p.get("compound_category") for p in products
    )
    
    if has_compound_limits:
        warning += "⚠️ **הערה חשובה לשוהם:**\n"
        warning += "יש הגבלות מיוחדות על ספירת חומרים בתרופות מתקבוצות מסוימות.\n"
        warning += "**חובה להתייעץ עם מדריך משק מוסמך לפני שימוש.**\n\n"
    
    return warning

@app.route("/api/chat", methods=["POST"])
def chat():
    """Main chat endpoint"""
    try:
        data = request.json
        user_message = data.get("message", "").strip()
        session_id = data.get("session_id", "default")
        is_shoham = data.get("is_shoham", False)
        
        if not user_message:
            return jsonify({"error": "Message is required"}), 400
        
        # Get conversation history
        conversation = get_or_create_conversation(session_id)
        
        # Build system prompt based on track
        if is_shoham:
            system_prompt = """אתה עוזר חכם לחקלאים בישראל שמגדלים הדרים.
            
מצב שוהם: אתה עוזר בתוכנית שוהם (מנדרינה אורי).

כללים:
1. תן המלצות על כימיקלים לחסל מזיקים מהרשימה המאושרת בלבד.
2. השתמש בהמלצות מהטבלה שלהלן לכל מזיק.
3. ממיין את התוצאות לפי PHI (ימי המתנה לקטיף) — קטן ל-גדול.
4. כלול תמיד הצהרת אחריות: "המידע הוא המלצה בלבד. האחריות חלה על המשתמש."
5. לשוהם יש הגבלות מיוחדות על ספירת חומרים — הזהר!

השב בעברית פשוטה וברורה."""
        else:
            system_prompt = """אתה עוזר חכם לחקלאים בישראל שמגדלים הדרים.

כללים:
1. תן המלצות על כימיקלים לחסל מזיקים מהרשימה המאושרת בלבד.
2. ממיין את התוצאות לפי PHI (ימי המתנה לקטיף) — קטן ל-גדול.
3. כלול תמיד הצהרת אחריות: "המידע הוא המלצה בלבד. האחריות חלה על המשתמש."

השב בעברית פשוטה וברורה."""
        
        # Check for fruit size question
        fruit_size_keywords = ["גודל פרי", "קוטר", "מ״מ", "מילימטר", "גודל"]
        is_fruit_size_question = any(keyword in user_message for keyword in fruit_size_keywords)
        
        # Add user message to history
        conversation.append({"role": "user", "content": user_message})
        
        # Get AI response
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=2000,
            system=system_prompt,
            messages=conversation
        )
        
        assistant_message = response.content[0].text
        
        # Add assistant response to history
        conversation.append({"role": "assistant", "content": assistant_message})
        
        # Add liability disclaimer
        disclaimer = "\n\n⚖️ **הצהרת אחריות משפטית:**\nהמידע הוא המלצה בלבד ובמטרה להנחיה כללית בלבד. האחריות המלאה על היישום חלה על המשתמש. לפני שימוש בכל חומר — קרא בעיון את התווית הרשמית ותייעץ עם מדריך משק מוסמך."
        
        return jsonify({
            "response": assistant_message + disclaimer,
            "session_id": session_id,
            "is_shoham": is_shoham,
            "timestamp": datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/fruit-size", methods=["POST"])
def get_fruit_size():
    """Get fruit size recommendation with monthly tables"""
    try:
        from data_fruit_size import get_fruit_size_recommendation, get_all_varieties
        
        data = request.json
        variety = data.get("variety", "").strip()
        current_size = data.get("current_size_mm")
        
        if not variety:
            # Return list of all varieties
            varieties = get_all_varieties()
            return jsonify({"varieties": varieties})
        
        # Get smart recommendation with today's date
        result = get_fruit_size_recommendation(variety, current_size)
        
        return jsonify({
            "variety": variety,
            "recommendation": result.get("recommendation", ""),
            "timestamp": datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/varieties", methods=["GET"])
def get_varieties():
    """Get list of all fruit varieties"""
    try:
        varieties = list(FRUIT_SIZE_DATA.keys())
        return jsonify({"varieties": varieties})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/health", methods=["GET"])
def health():
    """Health check"""
    return jsonify({"status": "healthy", "timestamp": datetime.now().isoformat()})

@app.route("/", methods=["GET"])
def root():
    """Root endpoint"""
    return jsonify({
        "name": "עוזרת הפרדס",
        "version": "4.0",
        "endpoints": {
            "chat": "/api/chat (POST)",
            "fruit-size": "/api/fruit-size (POST)",
            "varieties": "/api/varieties (GET)",
            "health": "/api/health (GET)"
        }
    })

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
