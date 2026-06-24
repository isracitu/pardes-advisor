# Product labels mapping to Ministry of Agriculture document IDs
# מיפוי תוויות תרופות ל-מספר מסמך משרד החקלאות

PRODUCT_LABELS = {
    "ORTUS 48% SC": "210",
    "SPINOSAD 48% SC": "205",
    "THIAMETHOXAM 25% WG": "198",
    "DICOFOL 48% EC": "187",
    "PYRETHRINS 3% EC": "201",
    "MALATHION 57% EC": "180",
    "OIL SUPERIOR 82%": "165",
    "EMAMECTIN BENZOATE 1.9% EC": "215",
    "IMIDACLOPRID 20% SL": "225",
    "TRIFLOXYSTROBIN 50% WG": "235",
    "MANCOZEB 80% WG": "240",
    "COPPER SULFATE 50%": "245",
    "SULFUR 80% WG": "250",
    "THIOPHANATE-METHYL 70% WP": "255",
    "DIFENOCONAZOLE 25% EC": "260",
    "TEBUCONAZOLE 25% EC": "265",
    "FENBUCONAZOLE 12% EC": "270",
    "AZOXYSTROBIN 25% SC": "275",
    "CYPROCONAZOLE 10% EC": "280",
    "HEXACONAZOLE 5% SC": "285",
    "DODINE 65% WP": "290",
    "METHOMYL 90% SP": "295",
    "PROFENOFOS 50% EC": "300",
    "PHOSMET 50% WP": "305",
    "PARATHION-METHYL 50% EC": "310",
    "DIMETHOATE 40% EC": "315",
    "ABAMECTIN 1.8% EC": "320",
    "NEEM OIL 3%": "325",
    "KAOLIN 85%": "330",
    "CALCIUM POLYSULFIDE 25%": "335"
}

def get_label_url(product_name):
    """Get official Ministry of Agriculture label URL for a product"""
    doc_id = PRODUCT_LABELS.get(product_name)
    if doc_id:
        return f"https://pesticides.moag.gov.il/LabelView/{doc_id}"
    return None

def get_all_products_with_labels():
    """Return all products with their label URLs"""
    return {
        product: f"https://pesticides.moag.gov.il/LabelView/{doc_id}"
        for product, doc_id in PRODUCT_LABELS.items()
    }
