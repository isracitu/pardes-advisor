# קוטר פרי ממוצע רצוי לכל זן - נתונים מ-משרד החקלאות 2026

FRUIT_SIZES_DATA = {
    # 1. אשכולית אדומה - קטיף בכיר (92-162 מ"מ)
    "אשכולית אדומה - קטיף בכיר": {
        "desired_range": {"min": 92, "max": 162},
        "source": "משרד החקלאות - קטיף בכיר",
        "harvests": {
            "קטיף ספטמבר": {
                "dates": [
                    {"date": "2026-06-01", "range": {"min": 42, "max": 72}},
                    {"date": "2026-06-15", "range": {"min": 57, "max": 87}},
                    {"date": "2026-07-01", "range": {"min": 67, "max": 97}},
                    {"date": "2026-07-15", "range": {"min": 74, "max": 104}},
                    {"date": "2026-08-01", "range": {"min": 79, "max": 109}},
                    {"date": "2026-08-15", "range": {"min": 83, "max": 113}},
                    {"date": "2026-09-01", "range": {"min": 87, "max": 117}},
                    {"date": "2026-09-15", "range": {"min": 90, "max": 120}},
                ]
            },
            "קטיף אוקטובר": {
                "dates": [
                    {"date": "2026-06-01", "range": {"min": 36, "max": 66}},
                    {"date": "2026-06-15", "range": {"min": 51, "max": 81}},
                    {"date": "2026-07-01", "range": {"min": 61, "max": 91}},
                    {"date": "2026-07-15", "range": {"min": 68, "max": 98}},
                    {"date": "2026-08-01", "range": {"min": 73, "max": 103}},
                    {"date": "2026-08-15", "range": {"min": 77, "max": 107}},
                    {"date": "2026-09-01", "range": {"min": 81, "max": 111}},
                    {"date": "2026-09-15", "range": {"min": 84, "max": 114}},
                    {"date": "2026-10-01", "range": {"min": 87, "max": 117}},
                    {"date": "2026-10-15", "range": {"min": 90, "max": 120}},
                ]
            }
        }
    },

    # 2. אשכולית אדומה - קטיף סלקטיבי (92-125 מ"מ)
    "אשכולית אדומה - קטיף סלקטיבי": {
        "desired_range": {"min": 92, "max": 125},
        "source": "משרד החקלאות - קטיף סלקטיבי",
        "harvests": {
            "קטיף פברואר-מרס": {
                "dates": [
                    {"date": "2026-06-01", "range": {"min": 20, "max": 50}},
                    {"date": "2026-06-15", "range": {"min": 35, "max": 65}},
                    {"date": "2026-07-01", "range": {"min": 45, "max": 75}},
                    {"date": "2026-07-15", "range": {"min": 52, "max": 82}},
                    {"date": "2026-08-01", "range": {"min": 57, "max": 87}},
                    {"date": "2026-08-15", "range": {"min": 61, "max": 91}},
                    {"date": "2026-09-01", "range": {"min": 65, "max": 95}},
                    {"date": "2026-09-15", "range": {"min": 68, "max": 98}},
                    {"date": "2026-10-01", "range": {"min": 71, "max": 101}},
                    {"date": "2026-10-15", "range": {"min": 74, "max": 104}},
                    {"date": "2026-11-01", "range": {"min": 76, "max": 106}},
                    {"date": "2026-11-15", "range": {"min": 78, "max": 108}},
                ]
            },
            "לאחר קטיף סלקטיבי": {
                "dates": [
                    {"date": "2026-12-01", "range": {"min": 80, "max": 97}},
                    {"date": "2027-01-01", "range": {"min": 83, "max": 100}},
                    {"date": "2027-02-01", "range": {"min": 86, "max": 103}},
                    {"date": "2027-03-01", "range": {"min": 88, "max": 105}},
                    {"date": "2027-04-01", "range": {"min": 90, "max": 107}},
                ]
            }
        }
    },

    # 3. טבורי ניוהול (82-122 מ"מ)
    "טבורי ניוהול": {
        "desired_range": {"min": 82, "max": 122},
        "source": "משרד החקלאות",
        "harvests": {
            "קטיף נובמבר": {
                "dates": [
                    {"date": "2026-06-01", "range": {"min": 21, "max": 51}},
                    {"date": "2026-06-15", "range": {"min": 29, "max": 59}},
                    {"date": "2026-07-01", "range": {"min": 36, "max": 66}},
                    {"date": "2026-07-15", "range": {"min": 43, "max": 73}},
                    {"date": "2026-08-01", "range": {"min": 48, "max": 78}},
                    {"date": "2026-08-15", "range": {"min": 53, "max": 83}},
                    {"date": "2026-09-01", "range": {"min": 57, "max": 87}},
                    {"date": "2026-09-15", "range": {"min": 61, "max": 91}},
                    {"date": "2026-10-01", "range": {"min": 65, "max": 95}},
                    {"date": "2026-10-15", "range": {"min": 69, "max": 99}},
                ]
            },
            "לאחר קטיף סלקטיבי - קטיף ינואר": {
                "dates": [
                    {"date": "2026-11-01", "range": {"min": 72, "max": 82}},
                    {"date": "2026-11-15", "range": {"min": 74, "max": 84}},
                    {"date": "2026-12-01", "range": {"min": 76, "max": 86}},
                    {"date": "2026-12-15", "range": {"min": 78, "max": 88}},
                    {"date": "2027-01-01", "range": {"min": 80, "max": 90}},
                ]
            },
            "קטיף פברואר": {
                "dates": [
                    {"date": "2026-11-15", "range": {"min": 56, "max": 76}},
                    {"date": "2026-12-01", "range": {"min": 57, "max": 77}},
                    {"date": "2026-12-15", "range": {"min": 58, "max": 78}},
                    {"date": "2027-01-01", "range": {"min": 59, "max": 79}},
                    {"date": "2027-02-01", "range": {"min": 60, "max": 80}},
                ]
            }
        }
    },

    # 4. פומלית ירוקה (122-162 מ"מ)
    "פומלית ירוקה": {
        "desired_range": {"min": 122, "max": 162},
        "source": "משרד החקלאות",
        "harvests": {
            "קטיף ספטמבר": {
                "dates": [
                    {"date": "2026-06-01", "range": {"min": 44, "max": 69}},
                    {"date": "2026-06-15", "range": {"min": 59, "max": 84}},
                    {"date": "2026-07-01", "range": {"min": 69, "max": 94}},
                    {"date": "2026-07-15", "range": {"min": 76, "max": 101}},
                    {"date": "2026-08-01", "range": {"min": 81, "max": 106}},
                    {"date": "2026-08-15", "range": {"min": 85, "max": 110}},
                    {"date": "2026-09-01", "range": {"min": 89, "max": 114}},
                    {"date": "2026-09-15", "range": {"min": 92, "max": 117}},
                    {"date": "2026-10-01", "range": {"min": 95, "max": 120}},
                ]
            },
            "קטיף אוקטובר": {
                "dates": [
                    {"date": "2026-06-01", "range": {"min": 40, "max": 60}},
                    {"date": "2026-06-15", "range": {"min": 55, "max": 75}},
                    {"date": "2026-07-01", "range": {"min": 65, "max": 85}},
                    {"date": "2026-07-15", "range": {"min": 72, "max": 92}},
                    {"date": "2026-08-01", "range": {"min": 77, "max": 97}},
                    {"date": "2026-08-15", "range": {"min": 81, "max": 101}},
                    {"date": "2026-09-01", "range": {"min": 85, "max": 105}},
                    {"date": "2026-09-15", "range": {"min": 88, "max": 108}},
                    {"date": "2026-10-01", "range": {"min": 91, "max": 111}},
                    {"date": "2026-10-15", "range": {"min": 94, "max": 114}},
                    {"date": "2026-11-01", "range": {"min": 96, "max": 116}},
                ]
            }
        }
    },

    # 5. פומלית צהובה - שוק מקומי (112+ מ"מ)
    "פומלית צהובה - שוק מקומי": {
        "desired_range": {"min": 112, "max": None},
        "source": "משרד החקלאות - שוק מקומי",
        "harvests": {
            "קטיף ינואר": {
                "dates": [
                    {"date": "2026-06-01", "range": {"min": 49, "max": 70}},
                    {"date": "2026-06-15", "range": {"min": 64, "max": 85}},
                    {"date": "2026-07-01", "range": {"min": 74, "max": 95}},
                    {"date": "2026-07-15", "range": {"min": 81, "max": 102}},
                    {"date": "2026-08-01", "range": {"min": 86, "max": 107}},
                    {"date": "2026-08-15", "range": {"min": 90, "max": 111}},
                    {"date": "2026-09-01", "range": {"min": 94, "max": 115}},
                    {"date": "2026-09-15", "range": {"min": 97, "max": 118}},
                    {"date": "2026-10-01", "range": {"min": 100, "max": 121}},
                    {"date": "2026-10-15", "range": {"min": 103, "max": 124}},
                    {"date": "2026-11-01", "range": {"min": 105, "max": 126}},
                    {"date": "2026-11-15", "range": {"min": 107, "max": 128}},
                    {"date": "2026-12-01", "range": {"min": 109, "max": 130}},
                    {"date": "2026-12-15", "range": {"min": 111, "max": 132}},
                    {"date": "2027-01-01", "range": {"min": 112, "max": 133}},
                    {"date": "2027-01-15", "range": {"min": 113, "max": 134}},
                ]
            }
        }
    },

    # 6. פומלו אדום (122-162 מ"מ)
    "פומלו אדום": {
        "desired_range": {"min": 122, "max": 162},
        "source": "משרד החקלאות",
        "harvests": {
            "קטיף ספטמבר": {
                "dates": [
                    {"date": "2026-06-01", "range": {"min": 80, "max": 112}},
                    {"date": "2026-06-15", "range": {"min": 95, "max": 127}},
                    {"date": "2026-07-01", "range": {"min": 105, "max": 137}},
                    {"date": "2026-07-15", "range": {"min": 112, "max": 144}},
                    {"date": "2026-08-01", "range": {"min": 117, "max": 149}},
                    {"date": "2026-08-15", "range": {"min": 121, "max": 153}},
                    {"date": "2026-09-01", "range": {"min": 125, "max": 157}},
                    {"date": "2026-09-15", "range": {"min": 128, "max": 160}},
                    {"date": "2026-10-01", "range": {"min": 131, "max": 163}},
                ]
            },
            "קטיף אוקטובר": {
                "dates": [
                    {"date": "2026-06-01", "range": {"min": 77, "max": 109}},
                    {"date": "2026-06-15", "range": {"min": 92, "max": 124}},
                    {"date": "2026-07-01", "range": {"min": 102, "max": 134}},
                    {"date": "2026-07-15", "range": {"min": 109, "max": 141}},
                    {"date": "2026-08-01", "range": {"min": 114, "max": 146}},
                    {"date": "2026-08-15", "range": {"min": 118, "max": 150}},
                    {"date": "2026-09-01", "range": {"min": 122, "max": 154}},
                    {"date": "2026-09-15", "range": {"min": 125, "max": 157}},
                    {"date": "2026-10-01", "range": {"min": 128, "max": 160}},
                ]
            }
        }
    },

    # 7. מינאואלה (25-85 מ"מ)
    "מינאואלה": {
        "desired_range": {"min": 25, "max": 85},
        "source": "משרד החקלאות",
        "harvests": {
            "קטיף דצמבר": {
                "dates": [
                    {"date": "2026-06-01", "range": {"min": 18, "max": 38}},
                    {"date": "2026-06-15", "range": {"min": 23, "max": 43}},
                    {"date": "2026-07-01", "range": {"min": 28, "max": 48}},
                    {"date": "2026-07-15", "range": {"min": 33, "max": 53}},
                    {"date": "2026-08-01", "range": {"min": 37, "max": 57}},
                    {"date": "2026-08-15", "range": {"min": 41, "max": 61}},
                    {"date": "2026-09-01", "range": {"min": 45, "max": 65}},
                    {"date": "2026-09-15", "range": {"min": 49, "max": 69}},
                    {"date": "2026-10-01", "range": {"min": 52, "max": 72}},
                    {"date": "2026-10-15", "range": {"min": 55, "max": 75}},
                    {"date": "2026-11-01", "range": {"min": 58, "max": 78}},
                    {"date": "2026-11-15", "range": {"min": 61, "max": 81}},
                    {"date": "2026-12-01", "range": {"min": 63, "max": 83}},
                    {"date": "2026-12-15", "range": {"min": 65, "max": 85}},
                    {"date": "2027-01-01", "range": {"min": 67, "max": 87}},
                ]
            }
        }
    },

    # 8. אורי (22-82 מ"מ)
    "אורי": {
        "desired_range": {"min": 22, "max": 82},
        "source": "משרד החקלאות",
        "harvests": {
            "קטיף פברואר": {
                "dates": [
                    {"date": "2026-07-01", "range": {"min": 14, "max": 34}},
                    {"date": "2026-07-15", "range": {"min": 21, "max": 41}},
                    {"date": "2026-08-01", "range": {"min": 27, "max": 47}},
                    {"date": "2026-08-15", "range": {"min": 32, "max": 52}},
                    {"date": "2026-09-01", "range": {"min": 37, "max": 57}},
                    {"date": "2026-09-15", "range": {"min": 41, "max": 61}},
                    {"date": "2026-10-01", "range": {"min": 45, "max": 65}},
                    {"date": "2026-10-15", "range": {"min": 49, "max": 69}},
                    {"date": "2026-11-01", "range": {"min": 53, "max": 73}},
                ]
            }
        }
    },

    # 9. קלמנטינה מיכל (22-82 מ"מ)
    "קלמנטינה מיכל": {
        "desired_range": {"min": 22, "max": 82},
        "source": "משרד החקלאות - נתונים זמינים עד קטיף נובמבר בלבד",
        "harvests": {
            "קטיף נובמבר": {
                "dates": [
                    {"date": "2026-06-01", "range": {"min": 16, "max": 36}},
                    {"date": "2026-06-15", "range": {"min": 21, "max": 41}},
                    {"date": "2026-07-01", "range": {"min": 26, "max": 46}},
                    {"date": "2026-07-15", "range": {"min": 30, "max": 50}},
                    {"date": "2026-08-01", "range": {"min": 34, "max": 54}},
                    {"date": "2026-08-15", "range": {"min": 38, "max": 58}},
                    {"date": "2026-09-01", "range": {"min": 41, "max": 61}},
                    {"date": "2026-09-15", "range": {"min": 44, "max": 64}},
                    {"date": "2026-10-01", "range": {"min": 47, "max": 67}},
                    {"date": "2026-10-15", "range": {"min": 50, "max": 70}},
                ]
            }
        }
    },

    # 10. מנדרינה הדס (22-82 מ"מ)
    "מנדרינה הדס": {
        "desired_range": {"min": 22, "max": 82},
        "source": "משרד החקלאות",
        "harvests": {
            "קטיף מרס-אפריל": {
                "dates": [
                    {"date": "2026-07-01", "range": {"min": 19, "max": 39}},
                    {"date": "2026-07-15", "range": {"min": 24, "max": 44}},
                    {"date": "2026-08-01", "range": {"min": 29, "max": 49}},
                    {"date": "2026-08-15", "range": {"min": 33, "max": 53}},
                    {"date": "2026-09-01", "range": {"min": 37, "max": 57}},
                    {"date": "2026-09-15", "range": {"min": 40, "max": 60}},
                    {"date": "2026-10-01", "range": {"min": 43, "max": 63}},
                    {"date": "2026-10-15", "range": {"min": 46, "max": 66}},
                    {"date": "2026-11-01", "range": {"min": 49, "max": 69}},
                    {"date": "2026-11-15", "range": {"min": 52, "max": 72}},
                    {"date": "2026-12-01", "range": {"min": 53, "max": 63}},
                    {"date": "2026-12-15", "range": {"min": 56, "max": 66}},
                    {"date": "2027-01-01", "range": {"min": 58, "max": 68}},
                    {"date": "2027-01-15", "range": {"min": 60, "max": 70}},
                    {"date": "2027-02-01", "range": {"min": 61, "max": 71}},
                ]
            },
            "קטיף ינואר": {
                "dates": [
                    {"date": "2026-11-01", "range": {"min": 53, "max": 63}},
                    {"date": "2026-11-15", "range": {"min": 56, "max": 66}},
                    {"date": "2026-12-01", "range": {"min": 58, "max": 68}},
                    {"date": "2026-12-15", "range": {"min": 60, "max": 70}},
                    {"date": "2027-01-01", "range": {"min": 61, "max": 71}},
                ]
            },
            "קטיף מרס-אפריל נוסף": {
                "dates": [
                    {"date": "2026-12-01", "range": {"min": 54, "max": 74}},
                    {"date": "2027-01-01", "range": {"min": 56, "max": 76}},
                    {"date": "2027-02-01", "range": {"min": 58, "max": 78}},
                    {"date": "2027-03-01", "range": {"min": 59, "max": 79}},
                    {"date": "2027-04-01", "range": {"min": 60, "max": 80}},
                ]
            }
        }
    },

    # 11. ליים (52-72 מ"מ) - שתי אזוריות
    "ליים": {
        "desired_range": {"min": 52, "max": 72},
        "source": "משרד החקלאות - שתי אזוריות גידול",
        "harvests": {
            "אזור 1: אמצע יולי (כינרת + בית שאן)": {
                "dates": [
                    {"date": "2026-06-15", "range": {"min": 36, "max": 56}},
                    {"date": "2026-07-01", "range": {"min": 41, "max": 61}},
                    {"date": "2026-07-15", "range": {"min": 46, "max": 66}},
                    {"date": "2026-08-01", "range": {"min": 50, "max": 70}},
                ]
            },
            "אזור 2: סוף יולי + אוגוסט (עמק החולה)": {
                "dates": [
                    {"date": "2026-06-15", "range": {"min": 33, "max": 53}},
                    {"date": "2026-07-01", "range": {"min": 38, "max": 58}},
                    {"date": "2026-07-15", "range": {"min": 43, "max": 63}},
                    {"date": "2026-08-01", "range": {"min": 47, "max": 67}},
                    {"date": "2026-08-15", "range": {"min": 50, "max": 70}},
                ]
            }
        }
    },

    # 12. טבורי קרה קרה - שוק מקומי (85-122 מ"מ)
    "טבורי קרה קרה - שוק מקומי": {
        "desired_range": {"min": 85, "max": 122},
        "source": "משרד החקלאות - שוק מקומי",
        "harvests": {
            "קטיף נובמבר-דצמבר": {
                "dates": [
                    {"date": "2026-06-01", "range": {"min": 41, "max": 56}},
                    {"date": "2026-06-15", "range": {"min": 46, "max": 61}},
                    {"date": "2026-07-01", "range": {"min": 51, "max": 66}},
                    {"date": "2026-07-15", "range": {"min": 56, "max": 71}},
                    {"date": "2026-08-01", "range": {"min": 61, "max": 76}},
                    {"date": "2026-08-15", "range": {"min": 65, "max": 80}},
                    {"date": "2026-09-01", "range": {"min": 69, "max": 84}},
                    {"date": "2026-09-15", "range": {"min": 73, "max": 84}},
                    {"date": "2026-10-01", "range": {"min": 76, "max": 91}},
                    {"date": "2026-10-15", "range": {"min": 79, "max": 94}},
                    {"date": "2026-11-01", "range": {"min": 81, "max": 96}},
                    {"date": "2026-11-15", "range": {"min": 83, "max": 98}},
                    {"date": "2026-12-01", "range": {"min": 85, "max": 100}},
                ]
            },
            "קטיף ינואר-פברואר": {
                "dates": [
                    {"date": "2026-06-01", "range": {"min": 39, "max": 54}},
                    {"date": "2026-06-15", "range": {"min": 44, "max": 59}},
                    {"date": "2026-07-01", "range": {"min": 49, "max": 64}},
                    {"date": "2026-07-15", "range": {"min": 54, "max": 69}},
                    {"date": "2026-08-01", "range": {"min": 59, "max": 74}},
                    {"date": "2026-08-15", "range": {"min": 63, "max": 78}},
                    {"date": "2026-09-01", "range": {"min": 67, "max": 82}},
                    {"date": "2026-09-15", "range": {"min": 71, "max": 86}},
                    {"date": "2026-10-01", "range": {"min": 74, "max": 89}},
                    {"date": "2026-10-15", "range": {"min": 77, "max": 92}},
                    {"date": "2026-11-01", "range": {"min": 79, "max": 94}},
                    {"date": "2026-11-15", "range": {"min": 81, "max": 96}},
                    {"date": "2026-12-01", "range": {"min": 83, "max": 98}},
                    {"date": "2026-12-15", "range": {"min": 84, "max": 99}},
                    {"date": "2027-02-01", "range": {"min": 85, "max": 100}},
                ]
            }
        }
    },

    # 13. טבורי קרה קרה - יצוא (72-92 מ"מ)
    "טבורי קרה קרה - יצוא": {
        "desired_range": {"min": 72, "max": 92},
        "source": "משרד החקלאות - יצוא",
        "harvests": {
            "קטיף ינואר-פברואר": {
                "dates": [
                    {"date": "2026-06-01", "range": {"min": 24, "max": 44}},
                    {"date": "2026-06-15", "range": {"min": 29, "max": 49}},
                    {"date": "2026-07-01", "range": {"min": 34, "max": 54}},
                    {"date": "2026-07-15", "range": {"min": 39, "max": 59}},
                    {"date": "2026-08-01", "range": {"min": 44, "max": 64}},
                    {"date": "2026-08-15", "range": {"min": 48, "max": 68}},
                    {"date": "2026-09-01", "range": {"min": 52, "max": 72}},
                    {"date": "2026-09-15", "range": {"min": 56, "max": 76}},
                    {"date": "2026-10-01", "range": {"min": 59, "max": 79}},
                    {"date": "2026-10-15", "range": {"min": 62, "max": 82}},
                    {"date": "2026-11-01", "range": {"min": 64, "max": 84}},
                    {"date": "2026-11-15", "range": {"min": 66, "max": 86}},
                    {"date": "2026-12-01", "range": {"min": 68, "max": 88}},
                    {"date": "2026-12-15", "range": {"min": 69, "max": 89}},
                    {"date": "2027-02-01", "range": {"min": 70, "max": 90}},
                ]
            }
        }
    }
}

def get_variety_names():
    """החזר רשימת כל השנים הזמינים"""
    return sorted(list(FRUIT_SIZES_DATA.keys()))

def get_harvest_types(variety):
    """החזר סוגי קטיף זמינים לזן מסוים"""
    if variety not in FRUIT_SIZES_DATA:
        return []
    return list(FRUIT_SIZES_DATA[variety]["harvests"].keys())

def find_closest_measurements(variety, harvest_type, current_date):
    """
    מצא את שתי המדידות הקרובות ביותר לתאריך נתון
    מחזיר: (date_before, range_before, date_after, range_after)
    """
    if variety not in FRUIT_SIZES_DATA:
        return None
    
    if harvest_type not in FRUIT_SIZES_DATA[variety]["harvests"]:
        return None
    
    dates = FRUIT_SIZES_DATA[variety]["harvests"][harvest_type]["dates"]
    
    # מיין את התאריכים
    sorted_dates = sorted(dates, key=lambda x: x["date"])
    
    for i in range(len(sorted_dates) - 1):
        if sorted_dates[i]["date"] <= current_date < sorted_dates[i+1]["date"]:
            return {
                "before": sorted_dates[i],
                "after": sorted_dates[i+1]
            }
    
    # אם לפני כל תאריך
    if current_date < sorted_dates[0]["date"]:
        return {"before": None, "after": sorted_dates[0]}
    
    # אם אחרי כל תאריך
    return {"before": sorted_dates[-1], "after": None}
