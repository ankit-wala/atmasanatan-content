#!/usr/bin/env python3
"""
Fill verified DrikPanchang date_2026 values into meta.yaml files and set
status: ready_to_publish for any entry that was 'reviewed' and now has a date.
Run: /usr/bin/python3 build/fill_dates_2026.py
"""
import os, re, sys

BASE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "kathas", "festivals")

# Verified dates from DrikPanchang — all 2026 unless noted.
# Sources: Ekadashi bulk page, Sankashti bulk page, Pradosh bulk page,
# individual festival pages, and Hindu calendar month pages.
DATES = {
    # Ekadashis
    "saphala-ekadashi":           "2025-12-15",  # Pausha Krishna Ekadashi (2025-26 cycle)
    "pausha-putrada-ekadashi":    "2025-12-30",  # Pausha Shukla Ekadashi (2025-26 cycle)
    "shattila-ekadashi":          "2026-01-14",
    "jaya-ekadashi":              "2026-01-29",
    "vijaya-ekadashi":            "2026-02-13",
    "amalaki-ekadashi":           "2026-02-27",
    "papmochani-ekadashi":        "2026-03-15",
    "kamada-ekadashi":            "2026-03-29",
    "varuthini-ekadashi":         "2026-04-13",
    "mohini-ekadashi":            "2026-04-27",
    "apara-ekadashi":             "2026-05-13",
    "nirjala-ekadashi":           "2026-06-25",
    "nirjala-gayatri-jayanti":    "2026-06-25",
    "gayatri-jayanti":            "2026-06-25",
    "yogini-ekadashi":            "2026-07-10",
    "devshayani-ekadashi":        "2026-07-25",
    "kamika-ekadashi":            "2026-08-09",
    "shravana-putrada-ekadashi":  "2026-08-23",
    "aja-ekadashi":               "2026-09-07",
    "parivartini-ekadashi":       "2026-09-22",
    "indira-ekadashi":            "2026-10-06",
    "papankusha-ekadashi":        "2026-10-22",
    "rama-ekadashi":              "2026-11-05",
    "devutthana-ekadashi":        "2026-11-20",
    "utpanna-ekadashi":           "2026-12-04",
    "mokshada-ekadashi":          "2026-12-20",
    "ekadashi-mahatmya":          "2026-12-20",

    # Sankashti Chaturthi (Purnimanta naming; sakat-chauth = Magha/Pausha-border Chaturthi)
    "sakat-chauth":               "2026-01-06",
    "magha-sankashti":            "2026-01-06",
    "phalguna-sankashti":         "2026-02-05",
    "chaitra-sankashti":          "2026-03-06",
    "vaishakha-sankashti":        "2026-04-05",
    "jyeshtha-sankashti":         "2026-05-05",
    "ashadha-sankashti":          "2026-07-03",
    "shravan-sankashti":          "2026-08-02",
    "bhadrapada-sankashti":       "2026-08-31",
    "ashwin-sankashti":           "2026-09-29",
    "kartik-sankashti":           "2026-10-29",
    "karwa-chauth":               "2026-10-29",
    "margashirsha-sankashti":     "2026-11-27",

    # Pradosh (specific months per meta.yaml panchang)
    "pradosh-vrat":               "2026-02-14",  # Phalguna Krishna Trayodashi (= Shani Pradosh 2026)
    "som-pradosh":                "2026-08-25",  # Shravan Shukla Trayodashi
    "bhaum-pradosh":              "2026-09-08",   # Bhauma Pradosh — Bhadrapada Krishna Trayodashi (Tuesday)
    "shani-pradosh":              "2026-12-06",  # Margashirsha Krishna Trayodashi

    # Masik Shivaratri (Shravan Krishna Chaturdashi)
    "masik-shivaratri":           "2026-08-11",

    # Purnima dates
    "shakambhari-purnima":        "2026-01-03",
    "magha-purnima":              "2026-02-01",
    "satyanarayan-adhyaya-4":     "2026-02-01",
    "holika-dahan":               "2026-03-03",
    "hanuman-jayanti":            "2026-04-02",
    "buddha-purnima":             "2026-05-01",
    "satyanarayan-adhyaya-5":     "2026-05-01",
    "vat-purnima":                "2026-06-29",
    "guru-purnima":               "2026-07-29",
    "kokila-vrat":                "2026-07-29",
    "raksha-bandhan":             "2026-08-28",
    "masik-satyanarayan":         "2026-08-28",
    "satyanarayan-adhyaya-1":     "2026-08-28",
    "varalakshmi-vrat":           "2026-08-28",  # Friday = Shravan Purnima
    "sharad-purnima":             "2026-10-25",
    "valmiki-jayanti":            "2026-10-25",
    "dev-diwali":                 "2026-11-24",
    "satyanarayan-adhyaya-2":     "2026-11-24",
    "karthigai-deepam":           "2026-11-24",
    "dattatreya-jayanti":         "2026-12-23",
    "satyanarayan-adhyaya-3":     "2026-12-23",

    # Amavasya dates
    "mauni-amavasya":             "2026-01-18",  # Magha Amavasya
    "hariyali-amavasya":          "2026-08-12",  # Shravan Amavasya
    "pola":                       "2026-09-10",  # Bhadrapada Amavasya
    "mahalaya-pitru-paksha":      "2026-10-10",  # Sarva Pitru Amavasya
    "diwali":                     "2026-11-08",  # Kartik Amavasya
    "somvati-amavasya":           "2026-06-15",   # Jyeshtha Adhika Amavasya — Monday confirmed (DrikPanchang)
    "vat-savitri-vrat":           "2026-05-16",  # Jyeshtha Amavasya
    "shani-jayanti":              "2026-05-16",

    # Fixed/solar dates
    "lohri":                      "2026-01-13",
    "makar-sankranti":            "2026-01-14",

    # Magha Shukla
    "vasant-panchami":            "2026-01-23",
    "ratha-saptami":              "2026-01-25",
    "bhishma-ashtami":            "2026-01-26",

    # Phalguna
    "phulera-dooj":               "2026-02-19",
    "maha-shivaratri":            "2026-02-15",
    "rangpanchami":               "2026-03-08",

    # Chaitra
    "sheetala-ashtami":           "2026-03-11",
    "gudi-padwa":                 "2026-03-19",
    "gangaur":                    "2026-03-21",
    "ram-navami":                 "2026-03-26",

    # Vaishakha
    "akshaya-tritiya":            "2026-04-19",
    "akshaya-tritiya-parashuram": "2026-04-19",
    "parashurama-jayanti":        "2026-04-19",
    "ganga-saptami":              "2026-04-23",
    "sita-navami":                "2026-04-25",
    "narasimha-jayanti":          "2026-04-30",

    # Jyeshtha
    "ganga-dussehra":             "2026-05-25",

    # Jagannath Rath Yatra (already verified in meta but keep for completeness)
    "jagannath-rath-yatra":       "2026-07-16",
    "jaya-parvati-vrat":          "2026-07-27",

    # Shravan weekday vratas + special
    "somvar-vrat":                "2026-08-03",  # first Monday in Shravan
    "shravan-somvar-vrat":        "2026-08-03",
    "solah-somvar-vrat":          "2026-08-03",
    "ravivar-vrat":               "2026-08-02",  # first Sunday in Shravan
    "mangala-gauri-vrat":         "2026-08-04",  # first Tuesday in Shravan
    "hariyali-teej":              "2026-08-15",
    "nag-panchami":               "2026-08-17",
    "onam":                       "2026-08-26",

    # Bhadrapada
    "sheetala-satam":             "2026-09-03",
    "kajari-teej":                "2026-08-30",
    "janmashtami":                "2026-09-04",
    "ramdevji-jayanti":           "2026-09-12",   # Bhadrapada Shukla Dwitiya (Chaturthi Sep 14, Tritiya Sep 13, Dwitiya Sep 12)
    "ganesh-chaturthi-janma":     "2026-09-14",
    "ganesh-chaturthi-syamantaka":"2026-09-14",
    "hartalika-teej":             "2026-09-14",
    "swarna-gowri-vrat":          "2026-09-14",
    "rishi-panchami":             "2026-09-15",
    "mangalvar-vrat":             "2026-09-15",  # first Tuesday in Bhadrapada Shukla
    "hal-shashthi":               "2026-09-02",   # Hala Shashthi — Bhadrapada Krishna Shashthi (DrikPanchang confirmed)
    "radha-ashtami":              "2026-09-19",
    "vamana-jayanti":             "2026-09-23",
    "anant-chaturdashi":          "2026-09-25",

    # Ashwin
    "jivitputrika":               "2026-10-03",
    "budhvar-vrat":               "2026-10-14",   # first Wednesday in Ashwin Shukla
    "navratri-shailputri":        "2026-10-11",
    "navratri-brahmacharini":     "2026-10-12",
    "navratri-chandraghanta":     "2026-10-13",
    "navratri-kushmanda":         "2026-10-14",
    "navratri-skandamata":        "2026-10-15",
    "navratri-katyayani":         "2026-10-16",
    "navratri-kalaratri":         "2026-10-17",
    "navratri-mahagauri":         "2026-10-19",   # Durga Ashtami — DrikPanchang confirms Oct 19 (tithi prevails at sunrise)
    "navratri-siddhidatri":       "2026-10-19",
    "vijayadashami":              "2026-10-20",
    "shukravar-santoshi":         "2026-10-16",   # first Friday in Ashwin Shukla
    "shukravar-lakshmi":          "2026-10-16",
    "vaibhav-lakshmi-vrat":       "2026-10-16",

    # Kartik Krishna
    "kartik-snan-mahatmya":       "2026-10-26",  # Kartik Krishna Pratipada (day after Sharad Purnima)
    "karwa-chauth":               "2026-10-29",
    "ahoi-ashtami":               "2026-11-01",
    "govatsa-dwadashi":           "2026-11-05",
    "dhanteras":                  "2026-11-06",
    "narak-chaturdashi":          "2026-11-08",

    # Kartik Shukla
    "govardhan-puja":             "2026-11-10",
    "bhai-dooj":                  "2026-11-11",
    "chitragupta-puja":           "2026-11-11",
    "brihaspativar-vrat":         "2026-11-12",  # first Thursday in Kartik Shukla
    "chhath-puja":                "2026-11-15",
    "skanda-shashthi":            "2026-11-15",
    "gopashtami":                 "2026-11-17",
    "akshaya-navami":             "2026-11-18",
    "tulsi-vivah":                "2026-11-21",

    # Margashirsha
    "kalabhairav-jayanti":        "2026-12-01",
    "shanivar-vrat":              "2026-11-28",  # first Saturday in Margashirsha Krishna
    "vivah-panchami":             "2026-12-14",
    "champa-shashthi":            "2026-12-15",
}


def patch_meta(path, slug, date_str):
    with open(path) as f:
        text = f.read()

    original = text

    # Replace date_2026: TODO-VERIFY ... with date_2026: YYYY-MM-DD
    text = re.sub(
        r'(  date_2026:\s*)TODO-VERIFY\s*#[^\n]*',
        r'\g<1>' + date_str + '    # verified DrikPanchang 2026',
        text
    )

    # If status is 'reviewed', upgrade to 'ready_to_publish'
    text = re.sub(
        r"(status:\s*)reviewed(\s*#.*Phase \d+ review.*)",
        r"\g<1>ready_to_publish\2",
        text
    )

    if text == original:
        return False

    with open(path, 'w') as f:
        f.write(text)
    return True


updated = 0
skipped = 0
missing = []

for slug, date_str in sorted(DATES.items()):
    slug_dir = os.path.join(BASE, slug)
    meta_path = os.path.join(slug_dir, "meta.yaml")
    if not os.path.exists(meta_path):
        missing.append(slug)
        continue
    if patch_meta(meta_path, slug, date_str):
        updated += 1
    else:
        skipped += 1

print(f"Updated:  {updated}")
print(f"Skipped:  {skipped} (already had date or no TODO-VERIFY match)")
if missing:
    print(f"NOT FOUND ({len(missing)}): {', '.join(missing)}")
