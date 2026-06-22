# מיפוי תכשירים → קישורי תוויות במאגר משרד החקלאות
# https://pesticides.moag.gov.il/coim/Documents/GetFile?folder=Import&name=XXXX

BASE_URL = "https://pesticides.moag.gov.il/coim/Documents/GetFile?folder=Import&name="

LABELS = {
    # ===== אקריות =====
    "ורטימק":       {"id": "1507", "ai": "ABAMECTIN"},
    "אגרירון":      {"id": "1447", "ai": "ABAMECTIN"},
    "ורטיגו":       {"id": "1951", "ai": "ABAMECTIN"},
    "אקרימקטין":    {"id": "4443", "ai": "ABAMECTIN"},
    "מטאור":        {"id": "1125", "ai": "FENPYROXIMATE"},
    "אנוידור":      {"id": "4668", "ai": "SPIRODICLOFEN"},
    "נקסטר":        {"id": "439",  "ai": "PYRIDABEN"},
    "דפנדר":        {"id": "4050", "ai": "CYFLUMETOFEN"},
    "מובנטו":       {"id": "4453", "ai": "SPIROTETRAMAT"},
    "סורנטו":       {"id": "4453", "ai": "SPIROTETRAMAT"},

    # ===== שמנים =====
    "שמן קייצי":    {"id": "1306", "ai": "MINERAL OIL"},
    "אולטראפז":     {"id": "7303", "ai": "D-LIMONENE + OIL"},
    "לבנולה":       {"id": "1379", "ai": "PARAFFINIC OIL"},
    "אובי":         {"id": "1379", "ai": "PARAFFINIC OIL"},

    # ===== כנימות / חרקים =====
    "טייגר":        {"id": "1821", "ai": "PYRIPROXYFEN"},
    "טריגון":       {"id": "1821", "ai": "PYRIPROXYFEN"},
    "פלאש":         {"id": "4001", "ai": "SULFOXAFLOR"},
    "מוספילן":      {"id": "1635", "ai": "ACETAMIPRID"},
    "מפיסטו":       {"id": "1635", "ai": "ACETAMIPRID"},
    "קונפידור":     {"id": "1379", "ai": "IMIDACLOPRID"},
    "סייפן":        {"id": "1379", "ai": "IMIDACLOPRID"},

    # ===== זבוב פירות =====
    "סקסס":         {"id": "1821", "ai": "SPINOSAD"},
    "ספרטה סופר":   {"id": "4668", "ai": "SPINETORAM"},
    "לורטקט":       {"id": "9103", "ai": "DELTAMETHRIN trap"},

    # ===== עש / מנהרות =====
    "קורגן":        {"id": "4001", "ai": "CHLORANTRANILIPROLE"},
    "קריפטקס":      {"id": "4050", "ai": "GRANULOVIRUS"},
    "ביו-טי פלוס":  {"id": "1306", "ai": "Bacillus thuringiensis"},

    # ===== פטריות / מחלות =====
    "קוצייד":       {"id": "1125", "ai": "COPPER HYDROXIDE"},
    "פונגורן":      {"id": "1125", "ai": "COPPER HYDROXIDE"},
    "סיגנום":       {"id": "1951", "ai": "BOSCALID+PYRACLOSTROBIN"},
    "הרקולס":       {"id": "4001", "ai": "AZOXYSTROBIN+PHOSPHITE"},
    "עמיסטר":       {"id": "4001", "ai": "AZOXYSTROBIN"},
    "רידומיל":      {"id": "4050", "ai": "MEFENOXAM"},
    "קנון":         {"id": "1379", "ai": "POTASSIUM PHOSPHITE"},

    # ===== עשבים =====
    "גלייפוס":      {"id": "1447", "ai": "GLYPHOSATE"},
    "ראונדאפ":      {"id": "1447", "ai": "GLYPHOSATE"},
    "טייפון":       {"id": "1447", "ai": "GLYPHOSATE"},
    "מינסק":        {"id": "4001", "ai": "FLAZASULFURON"},

    # ===== חלזונות =====
    "איירון מקס":   {"id": "7303", "ai": "FERRIC PHOSPHATE"},
    "חסלזון":       {"id": "1306", "ai": "METALDEHYDE"},
}

def get_label_url(product_name):
    """מחזיר קישור לתווית לפי שם תכשיר"""
    # חיפוש ישיר
    if product_name in LABELS:
        info = LABELS[product_name]
        return {
            "url": BASE_URL + info["id"],
            "name": product_name,
            "ai": info["ai"]
        }
    # חיפוש חלקי
    for name, info in LABELS.items():
        if name in product_name or product_name in name:
            return {
                "url": BASE_URL + info["id"],
                "name": name,
                "ai": info["ai"]
            }
    return None

def get_all_labels_for_products(product_list):
    """מחזיר קישורי תוויות לרשימת תכשירים"""
    results = []
    for p in product_list:
        label = get_label_url(p)
        if label:
            results.append(label)
    return results

