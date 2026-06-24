# Shoham Orri Mandarin - Approved Pesticides List v13, May 2026
# שוהם - מנדרינה אורי - רשימת תרופות מאושרות גרסה 13, מאי 2026
# Authorization: Verbal + Email approval from Shoham management

PESTS_SHOHAM = [
    "זבוב הפירות המצרי",
    "זבוב הפירות החרוב",
    "מינר עלה",
    "סיגיל הדרים",
    "קוקציד מגן",
    "אקארינים",
    "חלודה שחורה",
    "גומוזיס"
]

PRODUCTS_SHOHAM = [
    {
        "name": "ORTUS 48% SC",
        "pest": "זבוב הפירות המצרי",
        "phi_days": 21,  # שונה לשוהם
        "rate": "75 מ״ל / 100 ל׳ מים",
        "doc_id": "210",
        "compound_category": "Class A",
        "notes": "עד 3 התזות בעונה בשוהם"
    },
    {
        "name": "SPINOSAD 48% SC",
        "pest": "עש משעמם",
        "phi_days": 14,  # שונה לשוהם
        "rate": "50 מ״ל / 100 ל׳ מים",
        "doc_id": "205",
        "compound_category": "Organic",
        "notes": "מאושר בשוהם"
    },
    {
        "name": "DICOFOL 48% EC",
        "pest": "אקארינים",
        "phi_days": 21,
        "rate": "100 מ״ל / 100 ל׳ מים",
        "doc_id": "187",
        "compound_category": "Class B",
        "notes": "בקתם תוך 10-14 ימים בשוהם"
    },
    {
        "name": "PYRETHRINS 3% EC",
        "pest": "זבוב הפירות החרוב",
        "phi_days": 7,
        "rate": "25 מ״ל / 100 ל׳ מים",
        "doc_id": "201",
        "compound_category": "Organic",
        "notes": "טבעי, מאושר בשוהם"
    },
    {
        "name": "OIL SUPERIOR 82%",
        "pest": "קוקציד מגן",
        "phi_days": 21,
        "rate": "150 מ״ל / 100 ל׳ מים",
        "doc_id": "165",
        "compound_category": "Oil",
        "notes": "סוף חורף בלבד"
    }
]

SHOHAM_RULES = {
    "max_applications": {
        "ORTUS 48% SC": 3,
        "SPINOSAD 48% SC": 4,
        "DICOFOL 48% EC": 2
    },
    "germany_restrictions": [
        "DICOFOL 48% EC",
        "Some neonicotinoids"
    ],
    "consultation_required_for": [
        "Multiple products from same compound category in short period",
        "More than 2 systemic applications",
        "Products intended for Germany export"
    ],
    "notes": "שוהם קיבלה אישור ממשרד החקלאות להפצת מידע זה. יש הגבלות על ספירת חומרים ודרישות התייעצות."
}
