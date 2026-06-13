#!/usr/bin/env python3
"""
Seed the RESERVE POOL — all kathas NOT in the initial 108 selection.
Orders 201+ so they sort after the 108 and are clearly marked as reserve.
Idempotent: skips any folder that already exists.
Run: python3 build/seed_extras.py
"""

import os

BASE = os.path.join(os.path.dirname(__file__), "..", "kathas", "festivals")

# Same tuple format as seed_stubs.py:
# slug, type, order, category, deity[], month, paksha, tithi,
# region, tags[], sources[], title, scripture_ref
EXTRAS = [

    # ═══════════════════════════════════════════════════════════════════════
    # SANKASHTI CHATURTHI — 11 remaining (Sakat Chauth / Pausha is #69)
    # One distinct Ganesha-swaroop katha per lunar month.
    # ═══════════════════════════════════════════════════════════════════════

    ("bhadrapada-sankashti",
     "vrat", 201, "major",
     ["Ganesha"],
     "Bhadrapada", "Krishna", "Chaturthi",
     "pan-india",
     ["sankashti","ganesha","bhadrapada","chaturthi","angarika"],
     ["Ganesha Purana — Dhumravarna swaroop katha",
      "DrikPanchang — Bhadrapada Sankashti Chaturthi"],
     "Bhadrapada Sankashti — Dhumravarna Ganesh Katha",
     "Ganesha Purana"),

    ("ashwin-sankashti",
     "vrat", 202, "major",
     ["Ganesha"],
     "Ashwin", "Krishna", "Chaturthi",
     "pan-india",
     ["sankashti","ganesha","ashwin","chaturthi"],
     ["Ganesha Purana — Ekadanta swaroop katha",
      "DrikPanchang — Ashwin Sankashti Chaturthi"],
     "Ashwin Sankashti — Ekadanta Ganesh Katha",
     "Ganesha Purana"),

    ("kartik-sankashti",
     "vrat", 203, "major",
     ["Ganesha"],
     "Kartik", "Krishna", "Chaturthi",
     "pan-india",
     ["sankashti","ganesha","kartik","chaturthi"],
     ["Ganesha Purana — Saumya/Trimurti swaroop katha",
      "DrikPanchang — Kartik Sankashti Chaturthi"],
     "Kartik Sankashti — Saumya Ganesh Katha",
     "Ganesha Purana"),

    ("margashirsha-sankashti",
     "vrat", 204, "major",
     ["Ganesha"],
     "Margashirsha", "Krishna", "Chaturthi",
     "pan-india",
     ["sankashti","ganesha","margashirsha","chaturthi"],
     ["Ganesha Purana — Bhanu/Dhruva swaroop katha",
      "DrikPanchang — Margashirsha Sankashti Chaturthi"],
     "Margashirsha Sankashti — Bhanu Ganesh Katha",
     "Ganesha Purana"),

    ("magha-sankashti",
     "vrat", 205, "major",
     ["Ganesha"],
     "Magha", "Krishna", "Chaturthi",
     "pan-india",
     ["sankashti","ganesha","magha","chaturthi","maha-sankashti"],
     ["Ganesha Purana — Maha / Dwidala swaroop katha",
      "DrikPanchang — Magha Sankashti Chaturthi (Maha Sankashti)"],
     "Magha Sankashti (Maha Sankashti) — Dwidala Ganesh Katha",
     "Ganesha Purana"),

    ("phalguna-sankashti",
     "vrat", 206, "major",
     ["Ganesha"],
     "Phalguna", "Krishna", "Chaturthi",
     "pan-india",
     ["sankashti","ganesha","phalguna","chaturthi"],
     ["Ganesha Purana — Trinetra / Vikata swaroop katha",
      "DrikPanchang — Phalguna Sankashti Chaturthi"],
     "Phalguna Sankashti — Trinetra Ganesh Katha",
     "Ganesha Purana"),

    ("chaitra-sankashti",
     "vrat", 207, "major",
     ["Ganesha"],
     "Chaitra", "Krishna", "Chaturthi",
     "pan-india",
     ["sankashti","ganesha","chaitra","chaturthi"],
     ["Ganesha Purana — Vakratunda / Bhalchandra swaroop katha",
      "DrikPanchang — Chaitra Sankashti Chaturthi"],
     "Chaitra Sankashti — Vakratunda Ganesh Katha",
     "Ganesha Purana"),

    ("vaishakha-sankashti",
     "vrat", 208, "major",
     ["Ganesha"],
     "Vaishakha", "Krishna", "Chaturthi",
     "pan-india",
     ["sankashti","ganesha","vaishakha","chaturthi"],
     ["Ganesha Purana — Ekadanta / Vakratunda swaroop katha",
      "DrikPanchang — Vaishakha Sankashti Chaturthi"],
     "Vaishakha Sankashti — Ekadanta Ganesh Katha",
     "Ganesha Purana"),

    ("jyeshtha-sankashti",
     "vrat", 209, "major",
     ["Ganesha"],
     "Jyeshtha", "Krishna", "Chaturthi",
     "pan-india",
     ["sankashti","ganesha","jyeshtha","chaturthi"],
     ["Ganesha Purana — Kriti / Kulpati swaroop katha",
      "DrikPanchang — Jyeshtha Sankashti Chaturthi"],
     "Jyeshtha Sankashti — Kriti Ganesh Katha",
     "Ganesha Purana"),

    ("ashadha-sankashti",
     "vrat", 210, "major",
     ["Ganesha"],
     "Ashadha", "Krishna", "Chaturthi",
     "pan-india",
     ["sankashti","ganesha","ashadha","chaturthi"],
     ["Ganesha Purana — Vikata swaroop katha",
      "DrikPanchang — Ashadha Sankashti Chaturthi"],
     "Ashadha Sankashti — Vikata Ganesh Katha",
     "Ganesha Purana"),

    ("shravan-sankashti",
     "vrat", 211, "major",
     ["Ganesha"],
     "Shravan", "Krishna", "Chaturthi",
     "pan-india",
     ["sankashti","ganesha","shravan","chaturthi"],
     ["Ganesha Purana — Lambodara swaroop katha",
      "DrikPanchang — Shravan Sankashti Chaturthi"],
     "Shravan Sankashti — Lambodara Ganesh Katha",
     "Ganesha Purana"),

    # ═══════════════════════════════════════════════════════════════════════
    # PRADOSH VRAT — core + 3 weekday variants
    # ═══════════════════════════════════════════════════════════════════════

    ("pradosh-vrat",
     "vrat", 212, "major",
     ["Shiva","Parvati"],
     "Phalguna", "Krishna", "Trayodashi",
     "pan-india",
     ["pradosh","shiva","trayodashi","vrat"],
     ["Skanda Purana, Siva Rahasya Khanda — core Pradosh vrat katha",
      "DrikPanchang — Pradosh Vrat"],
     "Pradosh Vrat — Trayodashi ki Shiv Aradhana",
     "Skanda Purana, Siva Rahasya Khanda"),

    ("som-pradosh",
     "vrat", 213, "minor",
     ["Shiva","Parvati"],
     "Shravan", "Shukla", "Trayodashi",
     "pan-india",
     ["pradosh","som-pradosh","shiva","monday","trayodashi"],
     ["Skanda Purana — Som Pradosh vrat katha (Monday Pradosh)",
      "DrikPanchang — Som Pradosh"],
     "Som Pradosh — Somvar ke Pradosh ki Mahima",
     "Skanda Purana"),

    ("bhaum-pradosh",
     "vrat", 214, "major",
     ["Shiva","Mangal"],
     "Bhadrapada", "Shukla", "Trayodashi",
     "pan-india",
     ["pradosh","bhaum-pradosh","angaraki-pradosh","shiva","tuesday","trayodashi"],
     ["Skanda Purana — Bhaum / Angaraki Pradosh katha (Tuesday Pradosh — very auspicious)",
      "DrikPanchang — Bhaum Pradosh / Angaraki Pradosh"],
     "Bhaum Pradosh (Angaraki) — Mangalvar Pradosh ki Mahima",
     "Skanda Purana"),

    ("shani-pradosh",
     "vrat", 215, "major",
     ["Shiva","Shani"],
     "Margashirsha", "Krishna", "Trayodashi",
     "pan-india",
     ["pradosh","shani-pradosh","shiva","shani","saturday","trayodashi"],
     ["Skanda Purana — Shani Pradosh vrat katha (Saturday Pradosh)",
      "DrikPanchang — Shani Pradosh"],
     "Shani Pradosh — Shanivaar Pradosh ki Mahima",
     "Skanda Purana"),

    # ═══════════════════════════════════════════════════════════════════════
    # REMAINING WEEKDAY VRATS
    # (somvar #105, mangalvar #106, shukravar-santoshi #107, shanivar #108
    #  already seeded)
    # ═══════════════════════════════════════════════════════════════════════

    ("ravivar-vrat",
     "vrat", 216, "minor",
     ["Surya"],
     "Shravan", "Shukla", "Ravivar",
     "pan-india",
     ["ravivar","sunday","surya","vrat","weekday"],
     ["Folk tradition / Bhavishya Purana — Ravivar vrat katha",
      "DrikPanchang — Ravivar Vrat"],
     "Ravivar Vrat — Surya Dev ki Aradhana",
     "Bhavishya Purana (folk tradition)"),

    ("budhvar-vrat",
     "vrat", 217, "minor",
     ["Budha","Ganesha"],
     "Ashwin", "Shukla", "Budhvar",
     "pan-india",
     ["budhvar","wednesday","budha","ganesha","vrat","weekday"],
     ["Folk tradition — Budhvar vrat katha",
      "DrikPanchang — Budhvar Vrat"],
     "Budhvar Vrat — Budha Dev ki Aradhana",
     "Folk tradition (oral)"),

    ("brihaspativar-vrat",
     "vrat", 218, "major",
     ["Vishnu","Brihaspati"],
     "Kartik", "Shukla", "Brihaspativar",
     "pan-india",
     ["brihaspativar","thursday","vishnu","brihaspati","vrat","weekday","guruvar"],
     ["Skanda Purana — Brihaspativar vrat katha (yellow clothing, banana puja)",
      "DrikPanchang — Brihaspativar / Guruvar Vrat"],
     "Brihaspativar Vrat — Vishnu aur Brihaspati ki Aradhana",
     "Skanda Purana (folk tradition)"),

    ("shukravar-lakshmi",
     "vrat", 219, "minor",
     ["Lakshmi"],
     "Ashwin", "Shukla", "Shukravar",
     "pan-india",
     ["shukravar","friday","lakshmi","vrat","weekday"],
     ["Folk tradition — Shukravar Lakshmi vrat katha (distinct from Santoshi Mata)",
      "DrikPanchang — Shukravar Vrat"],
     "Shukravar Vrat — Maa Lakshmi ki Aradhana",
     "Folk tradition (oral)"),

    # ═══════════════════════════════════════════════════════════════════════
    # MISSING FESTIVALS & VRATS
    # ═══════════════════════════════════════════════════════════════════════

    ("somvati-amavasya",
     "festival", 220, "major",
     ["Shiva","Peepal"],
     "Shravan", "Krishna", "Amavasya",
     "pan-india",
     ["somvati-amavasya","monday","amavasya","shiva","peepal","pitru"],
     ["Skanda Purana — Somvati Amavasya katha (Amavasya falling on Monday)",
      "DrikPanchang — Somvati Amavasya"],
     "Somvati Amavasya — Peepal aur Pitra Tarpan",
     "Skanda Purana"),

    ("gudi-padwa",
     "festival", 221, "minor",
     ["Brahma","Rama"],
     "Chaitra", "Shukla", "Pratipada",
     "maharashtra",
     ["gudi-padwa","ugadi","hindu-new-year","chaitra","maharashtra"],
     ["Brahma Purana — creation of the world on Chaitra Shukla Pratipada",
      "Valmiki Ramayana — Rama's return to Ayodhya (one tradition)",
      "DrikPanchang — Gudi Padwa / Ugadi"],
     "Gudi Padwa — Hindu Nava Varsha",
     "Brahma Purana"),

    ("lohri",
     "festival", 222, "minor",
     ["Agni","Surya"],
     "Pausha", "Shukla", "Sankranti",
     "north-india",
     ["lohri","agni","surya","punjab","harvest","january"],
     ["Folk tradition — Dulla Bhatti katha (Punjab oral tradition)",
      "DrikPanchang — Lohri"],
     "Lohri — Dulla Bhatti aur Agni Puja",
     "Folk tradition (oral, Punjab)"),

    ("vaibhav-lakshmi-vrat",
     "vrat", 223, "minor",
     ["Lakshmi"],
     "Ashwin", "Shukla", "Shukravar",
     "pan-india",
     ["vaibhav-lakshmi","lakshmi","vrat","friday","modern"],
     ["Modern pamphlet tradition — Vaibhav Lakshmi vrat katha (no classical Puranic source; 20th c. popular vrat)",
      "DrikPanchang — Vaibhav Lakshmi Vrat"],
     "Vaibhav Lakshmi Vrat",
     "Modern devotional tradition (no classical Puranic source)"),

    ("kartik-snan-mahatmya",
     "festival", 224, "minor",
     ["Vishnu","Kartik"],
     "Kartik", "Krishna", "Pratipada",
     "pan-india",
     ["kartik-snan","vishnu","kartik","mahatmya","snan"],
     ["Padma Purana — Kartik snan Mahatmya (month-long bathing significance)",
      "DrikPanchang — Kartik Maas"],
     "Kartik Snan Mahatmya — Kartik Maas ki礼ima",
     "Padma Purana"),

    ("kokila-vrat",
     "vrat", 225, "minor",
     ["Shiva","Parvati"],
     "Ashadha", "Shukla", "Purnima",
     "north-india",
     ["kokila-vrat","shiva","parvati","ashadha","cuckoo","women"],
     ["Folk tradition — Kokila (cuckoo) vrat katha for married women",
      "DrikPanchang — Kokila Vrat"],
     "Kokila Vrat", "Folk tradition (oral)"),

    ("hariyali-amavasya",
     "festival", 226, "minor",
     ["Shiva","Pitru"],
     "Shravan", "Krishna", "Amavasya",
     "pan-india",
     ["hariyali-amavasya","shravan","amavasya","pitru","tree-planting"],
     ["Padma Purana — Shravan Amavasya significance",
      "DrikPanchang — Hariyali Amavasya (Shravan Amavasya)"],
     "Hariyali Amavasya — Shravan ki Amavasya",
     "Padma Purana"),

    ("ganga-saptami",
     "festival", 227, "minor",
     ["Ganga","Surya"],
     "Vaishakha", "Shukla", "Saptami",
     "pan-india",
     ["ganga-saptami","ganga","surya","vaishakha","river"],
     ["Brahma Purana — Ganga Saptami katha (Ganga's second sacred day after Dussehra)",
      "DrikPanchang — Ganga Saptami"],
     "Ganga Saptami — Ganga ka Prakatya",
     "Brahma Purana"),

    ("vat-purnima",
     "festival", 228, "major",
     ["Savitri","Satyavan","Yama"],
     "Jyeshtha", "Shukla", "Purnima",
     "maharashtra",
     ["vat-purnima","savitri","satyavan","jyeshtha","purnima","maharashtra","gujarat"],
     ["Mahabharata, Vana Parva — Savitri-Satyavan katha (same story as Vat Savitri Amavasya; Maharashtra/Gujarat observe on Purnima)",
      "DrikPanchang — Vat Purnima"],
     "Vat Purnima — Savitri ki Prem aur Tapasya (Maharashtra / Gujarat)",
     "Mahabharata, Vana Parva"),

    ("rangpanchami",
     "festival", 229, "minor",
     ["Krishna","Radha"],
     "Phalguna", "Krishna", "Panchami",
     "north-india",
     ["rangpanchami","holi","krishna","phalguna","braj","colors"],
     ["Folk tradition — Rang Panchami katha (5 days after Holi, Braj tradition)",
      "DrikPanchang — Rang Panchami"],
     "Rang Panchami — Holi ke Panchve Din",
     "Folk tradition (Braj oral tradition)"),

    ("phulera-dooj",
     "festival", 230, "minor",
     ["Krishna","Radha"],
     "Phalguna", "Shukla", "Dwitiya",
     "north-india",
     ["phulera-dooj","krishna","radha","phalguna","braj","flowers"],
     ["Bhagavata Purana / Braj tradition — Phulera Dooj katha (Krishna plays with flowers)",
      "DrikPanchang — Phulera Dooj"],
     "Phulera Dooj — Phoolon ki Holi",
     "Braj folk tradition"),

    ("gayatri-jayanti",
     "festival", 231, "minor",
     ["Gayatri","Brahma"],
     "Jyeshtha", "Shukla", "Ekadashi",
     "pan-india",
     ["gayatri-jayanti","gayatri","brahma","jyeshtha","mantra"],
     ["Devi Bhagavata Purana — Gayatri Devi's manifestation katha",
      "DrikPanchang — Gayatri Jayanti"],
     "Gayatri Jayanti — Maa Gayatri ka Prakatya",
     "Devi Bhagavata Purana"),

    ("karthigai-deepam",
     "festival", 232, "minor",
     ["Shiva","Murugan"],
     "Margashirsha", "Shukla", "Purnima",
     "south-india",
     ["karthigai-deepam","shiva","murugan","margashirsha","tamil-nadu","deepam"],
     ["Skanda Purana — Karthigai Deepam katha (Shiva's pillar of light)",
      "DrikPanchang — Karthigai Deepam"],
     "Karthigai Deepam — Shiva ki Jyoti ka Prakash",
     "Skanda Purana"),

    ("valmiki-jayanti",
     "festival", 233, "minor",
     ["Valmiki"],
     "Ashwin", "Shukla", "Purnima",
     "pan-india",
     ["valmiki-jayanti","valmiki","ashwin","purnima","ramayana"],
     ["Valmiki Ramayana — Valmiki's life and transformation from Ratnakar to Maharishi Valmiki",
      "DrikPanchang — Valmiki Jayanti"],
     "Valmiki Jayanti — Ratnakar se Maharishi Valmiki",
     "Valmiki Ramayana, Bala Kanda"),

    ("masik-shivaratri",
     "vrat", 234, "minor",
     ["Shiva"],
     "Shravan", "Krishna", "Chaturdashi",
     "pan-india",
     ["masik-shivaratri","shiva","chaturdashi","monthly","krishna-paksha"],
     ["Skanda Purana — Masik Shivaratri vrat katha (monthly, every Krishna Chaturdashi)",
      "DrikPanchang — Masik Shivaratri"],
     "Masik Shivaratri — Har Maah ki Shivratri",
     "Skanda Purana"),

    ("pola",
     "festival", 235, "minor",
     ["Shiva","Bull","Nandi"],
     "Bhadrapada", "Krishna", "Amavasya",
     "maharashtra",
     ["pola","nandi","bull","bhadrapada","amavasya","maharashtra"],
     ["Folk tradition — Pola festival katha (Maharashtra, Chhattisgarh bull-worship)",
      "DrikPanchang — Pola"],
     "Pola — Bail Pola (Maharashtra)",
     "Folk tradition (Maharashtra oral tradition)"),

    ("ramdevji-jayanti",
     "festival", 236, "minor",
     ["Ramdevji","Vishnu"],
     "Bhadrapada", "Shukla", "Dwitiya",
     "rajasthan",
     ["ramdevji","ramdev-baba","bhadrapada","rajasthan","folk-deity"],
     ["Ramdev Purana (regional) — Ramdevji's life and miracles (Rajasthan folk tradition)",
      "DrikPanchang — Ramdevji Jayanti"],
     "Ramdevji Jayanti — Ramdev Baba ki Katha",
     "Ramdev Purana (Rajasthan regional tradition)"),

    ("swarna-gowri-vrat",
     "vrat", 237, "minor",
     ["Gauri","Parvati"],
     "Bhadrapada", "Shukla", "Tritiya",
     "karnataka",
     ["swarna-gowri","gauri","parvati","bhadrapada","karnataka","south-india"],
     ["Skanda Purana — Swarna Gowri / Gowri Habba vrat katha (Karnataka, day before Ganesh Chaturthi)",
      "DrikPanchang — Swarna Gowri Vrat"],
     "Swarna Gowri Vrat — Gowri Habba (Karnataka)",
     "Skanda Purana"),

    ("onam",
     "festival", 238, "major",
     ["Vamana","Vishnu","Bali"],
     "Bhadrapada", "Shukla", "Shravan-Nakshatra",
     "kerala",
     ["onam","vamana","bali","vishnu","kerala","harvest"],
     ["Bhagavata Purana, Skandha 8 — Bali-Vamana katha (Kerala Onam tradition)",
      "DrikPanchang — Onam / Thiruvonam"],
     "Onam — Maaveli aur Vamana Avatar (Kerala)",
     "Bhagavata Purana, Skandha 8"),

    ("masik-satyanarayan",
     "vrat", 239, "minor",
     ["Vishnu","Satyanarayan"],
     "Shravan", "Shukla", "Purnima",
     "pan-india",
     ["satyanarayan","vishnu","purnima","masik","monthly"],
     ["Skanda Purana, Reva Khanda — Satyanarayan Puja significance on any Purnima",
      "DrikPanchang — Purnima"],
     "Masik Satyanarayan Puja — Har Purnima ka Vrat",
     "Skanda Purana, Reva Khanda"),

    ("ekadashi-mahatmya",
     "festival", 240, "major",
     ["Vishnu","Ekadashi Devi"],
     "Margashirsha", "Krishna", "Ekadashi",
     "pan-india",
     ["ekadashi","vishnu","mahatmya","overview","importance"],
     ["Padma Purana — Ekadashi Mahatmya (general importance of all Ekadashis)",
      "Brahma Vaivarta Purana — Ekadashi cycle significance"],
     "Ekadashi Mahatmya — Sabhi Ekadashiyon ka Parichay",
     "Padma Purana, Uttara Khanda"),

    ("akshaya-tritiya-parashuram",
     "festival", 241, "minor",
     ["Parashurama","Vishnu","Lakshmi"],
     "Vaishakha", "Shukla", "Tritiya",
     "pan-india",
     ["akshaya-tritiya","parashurama","vishnu","vaishakha","combined"],
     ["Bhagavata Purana — Parashurama avatar katha (Vaishakha Shukla Tritiya is his janma AND Akshaya Tritiya)",
      "DrikPanchang — Akshaya Tritiya / Parashurama Jayanti"],
     "Akshaya Tritiya aur Parashurama Jayanti — Ek Din, Do Kathayen",
     "Bhagavata Purana"),

    ("nirjala-gayatri-jayanti",
     "festival", 242, "minor",
     ["Gayatri","Vishnu"],
     "Jyeshtha", "Shukla", "Ekadashi",
     "pan-india",
     ["nirjala-ekadashi","gayatri-jayanti","jyeshtha","confluence","vishnu"],
     ["Brahma Vaivarta Purana — when Nirjala Ekadashi and Gayatri Jayanti fall on same tithi",
      "DrikPanchang — Nirjala Ekadashi / Gayatri Jayanti"],
     "Nirjala Ekadashi aur Gayatri Jayanti — Sanyog",
     "Brahma Vaivarta Purana"),

]


META_TEMPLATE = """\
slug: {slug}
type: {type}
order: {order}
category: {category}
deity:
{deity_lines}
panchang:
  month: {month}
  paksha: {paksha}
  tithi: {tithi}
  date_2026: TODO-VERIFY   # YYYY-MM-DD — verify against DrikPanchang before publishing
  date_2027: TODO-VERIFY   # second occurrence; same katha, different date
region: {region}
related_shlokas: []
related_bhajans: []
tags:
{tag_lines}
sources:
{source_lines}
scripture_ref: "{scripture_ref}"
status: draft
"""

EN_TEMPLATE = """\
---
slug: {slug}
lang: en
title: "{title}"
subtitle: "TODO"
summary: "TODO — one to two sentences."
reel_hook: "TODO — scroll-stopping question."
---

## Katha

TODO — tell the story. Source: {scripture_ref}

## Significance

TODO — spiritual and cultural meaning.

## Vidhi

TODO — puja / vrat steps in order.

## Observance

TODO — fasting rules, timing, parana. (Required for vrats; optional for festivals.)

## Mantras

TODO — key shloka in Devanagari + transliteration + one-line meaning.
"""


def write_stub(entry):
    (slug, etype, order, category, deity, month, paksha, tithi,
     region, tags, sources, title, scripture_ref) = entry

    folder = os.path.join(BASE, slug)
    if os.path.exists(folder):
        print(f"  SKIP  {slug}  (already exists)")
        return

    os.makedirs(folder)

    deity_lines  = "\n".join(f"  - {d}" for d in deity)
    tag_lines    = "\n".join(f"  - {t}" for t in tags)
    source_lines = "\n".join(f'  - "{s}"' for s in sources)

    meta = META_TEMPLATE.format(
        slug=slug, type=etype, order=order, category=category,
        deity_lines=deity_lines, month=month, paksha=paksha, tithi=tithi,
        region=region, tag_lines=tag_lines, source_lines=source_lines,
        scripture_ref=scripture_ref,
    )
    en = EN_TEMPLATE.format(slug=slug, title=title, scripture_ref=scripture_ref)

    with open(os.path.join(folder, "meta.yaml"), "w") as f:
        f.write(meta)
    with open(os.path.join(folder, "en.md"), "w") as f:
        f.write(en)

    print(f"  CREATE {order:>3}  {slug}")


if __name__ == "__main__":
    print(f"Seeding reserve-pool extras into {BASE}\n")
    for entry in EXTRAS:
        write_stub(entry)
    total = len(EXTRAS)
    print(f"\nDone. {total} entries processed.")
