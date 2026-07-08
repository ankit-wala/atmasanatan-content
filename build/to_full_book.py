#!/usr/bin/env python3
"""Build the full 108-katha book as EPUB3 and PDF.

Order: entries starting from July 15, 2026 (chronological), then pre-July entries
at the end (they recur in 2027 for the reader). South-dominant, lesser-known
ekadashis, and duplicate/regional entries are excluded — see BOOK_TODO.md.

Usage:
    /usr/bin/python3 build/to_full_book.py [--lang en|hi]

Outputs (in build/output/):
    full-<lang>.epub
    full-<lang>.pdf
    full-<lang>.html   (intermediate, keep for inspection)
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
import textwrap
from datetime import datetime

import re

sys.path.insert(0, os.path.dirname(__file__))
from _corpus import SECTIONS, OUTPUT_DIR, load_entries

# IAST diacritics that never appear in Devanagari/Hindi/Marathi/Gujarati text
_IAST_RE = re.compile(r'[āīūṃṁṅñṭḍṇśṣḥṛḷĀĪŪṂṁṄÑṬḌṆŚṢḤṚ]')


def strip_iast_lines(text: str) -> str:
    """Remove standalone IAST transliteration lines (all builds)."""
    out = []
    for line in text.splitlines():
        s = line.strip()
        # Always keep: empty lines, blockquotes, headings, bold labels, list items
        if not s or s.startswith('>') or s.startswith('#') or s.startswith('**') or s.startswith('-'):
            out.append(line)
        elif _IAST_RE.search(s):
            pass  # IAST transliteration line — drop it
        else:
            out.append(line)
    return '\n'.join(out)

# ── Curated 108 slugs — audience-tuned per language ──────────────────────────
# Order is derived at runtime from date_2026: entries >= July 15 first
# (chronological), then Jan–Jul wrap-around entries at the end.
# See BOOK_TODO.md §1 for the audience logic behind each list.

SLUGS_108_EN = {
    "ahoi-ashtami", "akshaya-navami", "akshaya-tritiya", "amalaki-ekadashi",
    "anant-chaturdashi", "ashadha-sankashti", "ashwin-sankashti",
    "bhadrapada-sankashti", "bhai-dooj", "brihaspativar-vrat", "buddha-purnima",
    "chaitra-sankashti", "chhath-puja", "dattatreya-jayanti", "dev-diwali",
    "devshayani-ekadashi", "devutthana-ekadashi", "dhanteras", "diwali",
    "ekadashi-mahatmya", "ganesh-chaturthi-janma", "ganesh-chaturthi-syamantaka",
    "ganga-dussehra", "ganga-saptami", "gayatri-jayanti", "gopashtami",
    "govardhan-puja", "gudi-padwa", "guru-purnima", "hal-shashthi",
    "hanuman-jayanti", "hartalika-teej", "holika-dahan", "indira-ekadashi",
    "jagannath-rath-yatra", "janmashtami", "jaya-ekadashi", "jaya-parvati-vrat",
    "jyeshtha-sankashti", "kalabhairav-jayanti", "kamada-ekadashi",
    "kartik-sankashti", "kartik-snan-mahatmya", "karwa-chauth", "kokila-vrat",
    "lohri", "magha-purnima", "magha-sankashti", "maha-shivaratri",
    "mahalaya-pitru-paksha", "makar-sankranti", "mangala-gauri-vrat",
    "margashirsha-sankashti", "masik-satyanarayan", "masik-shivaratri",
    "mauni-amavasya", "mokshada-ekadashi", "nag-panchami", "narak-chaturdashi",
    "narasimha-jayanti", "navratri-brahmacharini", "navratri-chandraghanta",
    "navratri-kalaratri", "navratri-katyayani", "navratri-kushmanda",
    "navratri-mahagauri", "navratri-shailputri", "navratri-siddhidatri",
    "navratri-skandamata", "nirjala-ekadashi", "onam", "papmochani-ekadashi",
    "parashurama-jayanti", "parivartini-ekadashi", "phalguna-sankashti",
    "pradosh-vrat", "radha-ashtami", "raksha-bandhan", "ram-navami",
    "rangpanchami", "ratha-saptami", "rishi-panchami", "sakat-chauth",
    "satyanarayan-adhyaya-1", "satyanarayan-adhyaya-2", "shani-jayanti",
    "shani-pradosh", "shanivar-vrat", "sharad-purnima", "sheetala-ashtami",
    "shravan-sankashti", "shravan-somvar-vrat", "shukravar-lakshmi",
    "sita-navami", "skanda-shashthi", "solah-somvar-vrat", "somvar-vrat",
    "somvati-amavasya", "swarna-gowri-vrat", "tulsi-vivah", "utpanna-ekadashi",
    "vaishakha-sankashti", "valmiki-jayanti", "vamana-jayanti", "varalakshmi-vrat",
    "vasant-panchami", "vat-savitri-vrat", "vijayadashami",
}

SLUGS_108_HI = [
    "ahoi-ashtami", "akshaya-tritiya", "anant-chaturdashi", "ashadha-sankashti",
    "ashwin-sankashti", "bhadrapada-sankashti", "bhai-dooj", "bhishma-ashtami",
    "brihaspativar-vrat", "buddha-purnima", "chaitra-durgashtami", "chaitra-sankashti", "chhath-puja",
    "chitragupta-puja", "dattatreya-jayanti", "dev-diwali", "devshayani-ekadashi",
    "devutthana-ekadashi", "dhanteras", "diwali", "ekadashi-mahatmya",
    "ganesh-chaturthi-janma", "ganesh-chaturthi-syamantaka", "ganga-dussehra",
    "gangaur", "gayatri-jayanti", "gopashtami", "govardhan-puja", "gudi-padwa",
    "guru-purnima", "hal-shashthi", "hanuman-jayanti", "hartalika-teej",
    "holika-dahan", "indira-ekadashi", "jagannath-rath-yatra", "janmashtami",
    "jaya-ekadashi", "jaya-parvati-vrat", "jivitputrika", "jyeshtha-sankashti",
    "kalabhairav-jayanti", "kamada-ekadashi",
    "kartik-snan-mahatmya", "karwa-chauth", "lohri", "magha-purnima",
    "magha-sankashti", "maha-shivaratri", "mahalaya-pitru-paksha",
    "makar-sankranti", "mangala-gauri-vrat", "mangalvar-vrat",
    "margashirsha-sankashti", "onam", "masik-shivaratri",
    "mauni-amavasya", "mokshada-ekadashi", "nag-panchami", "narak-chaturdashi",
    "narasimha-jayanti", "navratri-brahmacharini", "navratri-chandraghanta",
    "navratri-kalaratri", "navratri-katyayani", "navratri-kushmanda",
    "navratri-mahagauri", "navratri-shailputri", "navratri-siddhidatri",
    "navratri-skandamata", "nirjala-ekadashi", "papmochani-ekadashi",
    "parashurama-jayanti", "phalguna-sankashti", "phulera-dooj", "pradosh-vrat",
    "radha-ashtami", "raksha-bandhan", "ram-navami", "shukravar-santoshi",
    "ravivar-vrat", "rishi-panchami", "sakat-chauth", "satyanarayan-adhyaya-1",
    "satyanarayan-adhyaya-2", "shakambhari-purnima", "shani-jayanti",
    "shani-pradosh", "shanivar-vrat", "sharad-purnima", "sheetala-ashtami",
    "sheetala-satam", "shravan-sankashti", "shravan-somvar-vrat",
    "shukravar-lakshmi", "sita-navami", "kokila-vrat", "somvar-vrat",
    "somvati-amavasya", "tulsi-vivah", "utpanna-ekadashi", "vaishakha-sankashti",
    "valmiki-jayanti", "vamana-jayanti", "vasant-panchami", "vat-savitri-vrat",
    "vijayadashami", "vivah-panchami",
]

assert len(SLUGS_108_EN) == 108, f"EN list has {len(SLUGS_108_EN)} slugs"
assert len(SLUGS_108_HI) == 108, f"HI list has {len(SLUGS_108_HI)} slugs"

SLUG_SETS = {"en": SLUGS_108_EN, "hi": SLUGS_108_HI,
             "mr": SLUGS_108_EN, "gu": SLUGS_108_EN}


def add_mantra_linebreaks(body: str) -> str:
    """Add pandoc hard line breaks (trailing backslash) between consecutive
    blockquote lines so each half-verse renders on its own line in the PDF."""
    lines = body.split('\n')
    out = []
    for i, line in enumerate(lines):
        stripped = line.rstrip()
        next_is_bq = (i + 1 < len(lines) and lines[i + 1].lstrip().startswith('>'))
        if stripped.lstrip().startswith('>') and next_is_bq and not stripped.endswith('\\'):
            out.append(stripped + '\\')
        else:
            out.append(line)
    return '\n'.join(out)


def order_by_date(entries: list, cutoff: str = "2026-07-15") -> list:
    """Sort entries: date_2026 >= cutoff first (chronological), then the rest."""
    def sort_key(e):
        d = str(e.meta.get("panchang", {}).get("date_2026", "") or "")
        if not d or d.startswith("TODO"):
            d = "9999-99-99"
        return d

    on_or_after = sorted([e for e in entries if sort_key(e) >= cutoff], key=sort_key)
    before = sorted([e for e in entries if sort_key(e) < cutoff], key=sort_key)
    return on_or_after + before

SECTION_LABELS = {
    "en": {"Significance": "Significance", "Vidhi": "Vidhi", "Observance": "Vidhi", "Mantras": "Mantras"},
    "hi": {"Significance": "महत्त्व",      "Vidhi": "विधि",  "Observance": "विधि",  "Mantras": "मंत्र"},
    "mr": {"Significance": "महत्त्व",      "Vidhi": "विधी",  "Observance": "विधी",  "Mantras": "मंत्र"},
    "gu": {"Significance": "મહત્ત્વ",      "Vidhi": "વિધિ",  "Observance": "વિધિ",  "Mantras": "મંત્ર"},
}

BUILD_DIR  = os.path.dirname(os.path.abspath(__file__))
SAMPLE_DIR = os.path.join(BUILD_DIR, "sample")
_NOTO_DIR = os.path.join(BUILD_DIR, "fonts", "NotoSerifDevanagari", "unhinted", "ttf")

FONT_REGISTRY = {
    "noto": {
        "name":    "NotoSerifDevanagari",
        "regular": os.path.join(_NOTO_DIR, "NotoSerifDevanagari-Regular.ttf"),
        "bold":    os.path.join(_NOTO_DIR, "NotoSerifDevanagari-Bold.ttf"),
    },
    "mangal": {
        "name":    "Mangal",
        "regular": os.path.join(BUILD_DIR, "fonts", "Mangal", "mangal.ttf"),
        "bold":    os.path.join(BUILD_DIR, "fonts", "Mangal", "mangalb.ttf"),
    },
    "nirmala": {
        "name":    "NirmalaUI",
        "regular": os.path.join(BUILD_DIR, "fonts", "Nirmala", "NirmalaUI.ttf"),
        "bold":    os.path.join(BUILD_DIR, "fonts", "Nirmala", "NirmalaUIB.ttf"),
    },
}

# Resolved at runtime by --font; defaults to noto
FONT_REGULAR = FONT_REGISTRY["noto"]["regular"]
FONT_BOLD    = FONT_REGISTRY["noto"]["bold"]
FONT_NAME    = FONT_REGISTRY["noto"]["name"]

# EPUB always embeds Noto Serif Devanagari regardless of --font
EPUB_FONT_REGULAR = FONT_REGISTRY["noto"]["regular"]
EPUB_FONT_BOLD    = FONT_REGISTRY["noto"]["bold"]


# ── Content helpers ────────────────────────────────────────────────────────────

def front_matter(lang: str) -> str:
    _qr = f"file://{os.path.join(BUILD_DIR, 'app-qr.svg')}"
    if lang == "hi":
        return textwrap.dedent("""\
            ::: {.title-page}

            # 108 व्रत कथा

            [108 पवित्र अनुष्ठान — कथा, महत्त्व, विधि और मंत्र]{.subtitle}

            [आत्म सनातन]{.publisher}

            [2026]{.year}

            :::

            ::: {.copyright-page}

            *108 व्रत कथा*

            © 2026 आत्म सनातन। सर्वाधिकार सुरक्षित।

            इस पुस्तक का कोई भी भाग — चाहे मुद्रित, इलेक्ट्रॉनिक, या किसी अन्य माध्यम से — प्रकाशक की लिखित अनुमति के बिना पुनः प्रकाशित, संग्रहीत या प्रसारित नहीं किया जा सकता।

            **शास्त्र-स्रोत:** इस पुस्तक की कथाएँ वाल्मीकि रामायण, श्रीमद्भागवतम्, स्कंद पुराण, पद्म पुराण, ब्रह्म वैवर्त पुराण एवं अन्य पौराणिक ग्रंथों पर आधारित हैं।

            **तिथियाँ:** सभी तिथियाँ सत्यापित हैं। तिथि का प्रारंभ एवं समापन स्थान के अनुसार भिन्न हो सकता है — व्रत से पूर्व Atma Sanatan ऐप के पंचांग से पुष्टि अवश्य करें।

            प्रकाशक: आत्म सनातन · प्रथम संस्करण, 2026

            :::

            ::: {.invocation}

            **श्री गणेशाय नमः**

            ---

            > वक्रतुण्ड महाकाय सूर्यकोटिसमप्रभ ।<br />निर्विघ्नं कुरु मे देव सर्वकार्येषु सर्वदा ॥

            :::

            # प्रस्तावना

            भारत ने सदा काल को उत्सवों से मापा है। हिन्दू पंचांग केवल तारीखों का संग्रह नहीं — यह पवित्र वर्ष का मानचित्र है। यह बताता है कि किस दिन कौन-सा देवता सर्वाधिक सन्निकट है, किस तिथि पर कौन-सी उपासना सर्वाधिक फलदायी है, और किन दिनों में प्राचीन कथाएँ सबसे जीवंत हो उठती हैं।

            यहाँ संकलित उत्सव और व्रत सहस्राब्दियों से मनाए जाते आए हैं। इनकी जड़ें पुराणों में हैं — हिन्दू परंपरा के महान आख्यान-ग्रंथों में — और इनकी विधियाँ पीढ़ी-दर-पीढ़ी, मंदिरों और घरों में, देश के हर कोने में और अब विश्वभर में प्रवाहित होती चली आई हैं।

            यह पुस्तक एक सहयात्री है — किसी पुजारी या पंडित का विकल्प नहीं, बल्कि उनके लिए एक मार्गदर्शक जो दीपक के पीछे की कथा, मंत्र के भीतर का अर्थ और इन पवित्र दिनों में की जाने वाली क्रियाओं का कारण जानना चाहते हैं। प्रत्येक प्रविष्टि में कथा, महत्त्व, विधि और मंत्र हैं।

            पहले कथा पढ़िए। कहानी को हृदय में उतरने दीजिए। उसके बाद पूजा का अनुभव ही बदल जाएगा।

            — *आत्म सनातन*

            ## इस पुस्तक का उपयोग कैसे करें

            यह पुस्तक **15 जुलाई** से आरंभ होती है और हिन्दू पंचांग के अनुसार अगले जुलाई तक चलती है — ताकि आप प्रत्येक उत्सव से पहले उसे पढ़ सकें। प्रत्येक अध्याय में **महत्त्व** उत्सव को धार्मिक परंपरा में स्थापित करता है, **विधि** पूजन एवं व्रत की क्रमिक विधि देती है, और **मंत्र** देवनागरी एवं अर्थ सहित प्रमुख स्तोत्र प्रस्तुत करते हैं।

            प्रत्येक अध्याय के शीर्षक के नीचे 2026 और 2027 की तिथियाँ दी गई हैं — ताकि आप अगला उत्सव कब है, यह तुरंत देख सकें। पुस्तक के आरंभ में अनुक्रमणिका (Index) दी गई है जिसमें सभी 108 प्रविष्टियों के पृष्ठ क्रमांक हैं।

            ::: {.app-page}

            ## आत्म सनातन ऐप

            इस पुस्तक की कथाएँ सुनने के लिए **आत्म सनातन** ऐप डाउनलोड करें।

            भजन · मंत्र · दैनिक श्लोक · राशिफल · पंचांग · त्योहार · वॉलपेपर और बहुत कुछ

            ![](APP_QR_PATH){.app-qr}

            **app.atmasanatan.com**

            :::

        """).replace("APP_QR_PATH", _qr)
    return textwrap.dedent("""\
        ::: {.title-page}

        # 108 Vrat Katha

        [108 Sacred Observances — Katha, Significance, Vidhi and Mantras]{.subtitle}

        [Atma Sanatan]{.publisher}

        [2026]{.year}

        :::

        ::: {.copyright-page}

        *108 Vrat Katha*

        Copyright © 2026 Atma Sanatan. All rights reserved.

        No part of this publication may be reproduced, stored in a retrieval system, or transmitted in any form or by any means — electronic, mechanical, photocopying, recording, or otherwise — without the prior written permission of the publisher.

        **Scripture sources:** The kathas in this book draw on primary Hindu scriptural sources, including the Valmiki Ramayana, the Shrimad Bhagavatam, the Skanda Purana, the Padma Purana, the Brahma Vaivarta Purana, and other Puranic texts.

        **Festival dates:** All dates in this book are verified. Tithi timings vary by location — always confirm the exact timing on the Atma Sanatan app before observing.

        Published by Atma Sanatan · First edition, 2026

        :::

        ::: {.invocation}

        **श्री गणेशाय नमः**

        *Śrī Gaṇeśāya Namaḥ*

        ---

        > वक्रतुण्ड महाकाय सूर्यकोटिसमप्रभ ।<br />निर्विघ्नं कुरु मे देव सर्वकार्येषु सर्वदा ॥

        *Vakratuṇḍa Mahākāya Sūryakoṭisamaprabha |*
        *Nirvighnaṃ Kuru Me Deva Sarvakāryeṣu Sarvadā ||*

        O Lord with the curved trunk and the mighty form,
        radiant as ten million suns —
        grant me freedom from all obstacles, always, in every endeavour.

        :::

        # Introduction

        India has always measured time by festivals. The Hindu Panchang is not simply a calendar — it is a map of the sacred year, marking the days when a particular deity is closest, when the cosmos is aligned for a specific kind of worship, when the ancient stories are most alive.

        The festivals collected here have been observed for thousands of years. Their roots lie in the Puranas — the great narrative scriptures of the Hindu tradition — and their vidhi has been carried forward across generations, in temples and homes, across every corner of the subcontinent and now across the world.

        This book is a companion — not a substitute for a priest or pandita, but a guide for those who want to know the story behind the flame, the meaning inside the mantra, the reason we do what we do on these sacred days. Each chapter has a Katha (the founding story), a Significance section, a Vidhi (how to observe), and Mantras.

        Read the katha first. Let the story land. The puja will feel different after that.

        May your observance of each festival carry the full weight of its tradition.

        — *Atma Sanatan*

        ## How to Use This Book

        This book opens on **July 15** and follows the Hindu calendar year through to the following July — so you can read ahead of each festival as it approaches. Each chapter covers one festival or vrat. **Significance** places it in the wider dharmic picture. **Vidhi** gives the step-by-step puja and fast. **Mantras** gives the key prayers with Devanagari script and English meaning.

        Each chapter shows the 2026 and 2027 dates directly below its title — so you always know when the next occurrence falls. The index at the front lists all 108 festivals with page numbers.

        Dates in this book are verified. Tithi timings vary by location — always confirm on the Atma Sanatan app before observing.

        ::: {.app-page}

        ## Atma Sanatan App

        To listen to the kathas in this book, download the **Atma Sanatan** app.

        Bhajans · mantras · daily shlokas · rashifal · panchang · festivals · wallpapers and more

        ![](APP_QR_PATH){.app-qr}

        **app.atmasanatan.com**

        :::

    """).replace("APP_QR_PATH", _qr)


def format_chapter(entry, lang: str) -> str:
    doc = entry.docs.get(lang)
    if not doc:
        return ""

    # {#slug} anchor lets the index resolve page numbers via target-counter
    lines = [f"# {doc.title} {{#{entry.slug}}}\n"]

    if doc.frontmatter.get("subtitle"):
        lines.append(f"*{doc.frontmatter['subtitle']}*\n")

    # Dates below the subtitle — replaces the back-matter calendar table
    p_meta = entry.meta.get("panchang", {})
    d26 = fmt_date(p_meta.get("date_2026"))
    d27 = fmt_date(p_meta.get("date_2027"))
    lines.append(f'<p class="chapter-dates">2026: {d26}&nbsp;&nbsp;·&nbsp;&nbsp;2027: {d27}</p>\n')

    for sec in SECTIONS:
        body = doc.sections.get(sec, "")
        if body and not body.strip().startswith("TODO"):
            if sec == "Katha":
                lines.append(f"\n{body}\n")
            else:
                if sec == "Mantras":
                    body = strip_iast_lines(body)
                    body = add_mantra_linebreaks(body)
                labels = SECTION_LABELS.get(lang, SECTION_LABELS["en"])
                label = labels.get(sec, sec)
                lines.append(f"\n## {label}\n\n{body}\n")

    lines.append('\n<div class="chapter-end">✦ ✦ ✦</div>\n')
    text = "\n".join(lines)
    if lang != "en":
        text = text.replace("—", "–")  # em dash → en dash
    return text


def fmt_date(date_val) -> str:
    if not date_val:
        return "—"
    s = str(date_val)
    if s.startswith("TODO") or not s:
        return "—"
    try:
        dt = datetime.strptime(s, "%Y-%m-%d")
        return dt.strftime("%b %-d")
    except ValueError:
        return s


def _fmt_date(val) -> str:
    """Format a meta.yaml date value (datetime.date or 'YYYY-MM-DD' string) → 'Jul 16'."""
    if val is None:
        return "—"
    s = str(val).split()[0]  # strip any trailing YAML comment fragments
    if s.startswith("TODO") or not s:
        return "—"
    try:
        import datetime
        d = datetime.date.fromisoformat(s)
        return d.strftime("%b %-d")  # e.g. "Jul 16"
    except Exception:
        return s


def make_index(entries, lang: str, page_nums: dict = None) -> str:
    """Single-column index table: Festival | 2026 | 2027 | Page.
    page_nums maps slug → Arabic page number from the chapters PDF."""
    if page_nums is None:
        page_nums = {}

    if lang == "hi":
        heading = "# अनुक्रमणिका"
        hdr_fest, hdr_2026, hdr_2027, hdr_page = "उत्सव", "2026", "2027", "पृष्ठ"
    else:
        heading = "# Index"
        hdr_fest, hdr_2026, hdr_2027, hdr_page = "Festival", "2026", "2027", "Page"

    rows = [
        f'<thead><tr>'
        f'<th class="idx-hdr-title">{hdr_fest}</th>'
        f'<th class="idx-hdr-date">{hdr_2026}</th>'
        f'<th class="idx-hdr-date">{hdr_2027}</th>'
        f'<th class="idx-hdr-page">{hdr_page}</th>'
        f'</tr></thead><tbody>'
    ]
    for entry in entries:
        doc = entry.docs.get(lang)
        title = doc.title if doc else entry.slug
        panchang = entry.meta.get("panchang", {}) or {}
        d26 = _fmt_date(panchang.get("date_2026"))
        d27 = _fmt_date(panchang.get("date_2027"))
        num = page_nums.get(entry.slug, "")
        num_str = str(num) if num else "—"
        rows.append(
            f'<tr>'
            f'<td class="idx-title">{title}</td>'
            f'<td class="idx-date">{d26}</td>'
            f'<td class="idx-date">{d27}</td>'
            f'<td class="idx-page">{num_str}</td>'
            f'</tr>'
        )
    rows.append('</tbody>')
    index_html = (
        '<div class="festival-index">\n'
        '<table>\n' +
        '\n'.join(rows) +
        '\n</table>\n</div>'
    )
    return f'::: {{.index-section}}\n\n{heading}\n\n{index_html}\n\n:::'


def back_matter(lang: str) -> str:
    if lang == "hi":
        heading = "# आत्म सनातन के बारे में"
        body = "आत्म सनातन एक भक्तिपूर्ण प्रकाशन परियोजना है।"
    else:
        heading = "# About Atma Sanatan"
        body = textwrap.dedent("""\
            Atma Sanatan is a devotional publishing project dedicated to making the stories,
            meanings, and practices of the Hindu festival year accessible to practitioners
            across the world. All kathas draw on primary scriptural sources — the Skanda Purana,
            the Brahma Vaivarta Purana, the Valmiki Ramayana, the Shrimad Bhagavatam — and
            all dates are verified against DrikPanchang.

            **Get the App** — scan the QR code below to install the Atma Sanatan app for
            daily reminders, puja guides, and the full festival library on your phone.

            *(QR code — coming soon)*
        """)
    return f"{heading}\n\n{body}\n"


# ── Assembly ───────────────────────────────────────────────────────────────────

def assemble(entries, lang: str) -> str:
    """Single-document assembly for EPUB."""
    parts = [front_matter(lang), make_index(entries, lang)]
    for entry in entries:
        chapter = format_chapter(entry, lang)
        if chapter:
            parts.append(chapter)
    return "\n\n".join(parts)


def assemble_chapters_md(entries: list, lang: str) -> str:
    """Chapters + back matter only — used as Pass 1 of the two-pass PDF build.
    WeasyPrint numbers these from page 1 so target page numbers are correct."""
    parts = []
    for entry in entries:
        chapter = format_chapter(entry, lang)
        if chapter:
            parts.append(chapter)
    return "\n\n".join(parts)


def assemble_front_md(entries: list, lang: str, page_nums: dict) -> str:
    """Front matter + index with hardcoded page numbers — used as Pass 2."""
    front = front_matter(lang)
    idx = make_index(entries, lang, page_nums)
    text = f'::: {{.front-matter}}\n\n{front}\n\n{idx}\n\n:::'
    if lang != "en":
        text = text.replace("—", "–")
    return text


# ── CSS ────────────────────────────────────────────────────────────────────────

def build_css(roman: bool = False, lang: str = "en") -> str:
    """Generate PDF CSS.  roman=True for the front-matter PDF (Roman page numbers,
    title page suppressed); roman=False for the chapters PDF (Arabic from 1)."""
    kdp_css_path = os.path.join(BUILD_DIR, "kdp.css")
    with open(kdp_css_path) as f:
        base_css = f.read()
    font_faces = ""
    if os.path.exists(FONT_REGULAR):
        font_faces += (
            f"@font-face {{\n"
            f"    font-family: '{FONT_NAME}';\n"
            f"    src: url('file://{FONT_REGULAR}');\n"
            f"    font-weight: normal;\n}}\n"
        )
    if os.path.exists(FONT_BOLD):
        font_faces += (
            f"@font-face {{\n"
            f"    font-family: '{FONT_NAME}';\n"
            f"    src: url('file://{FONT_BOLD}');\n"
            f"    font-weight: bold;\n}}\n"
        )
    # Mirror margins + page numbering — appended last so they win over kdp.css @page.
    # Odd pages (recto, :right): inside=left 0.80", outside=right 0.65"
    # Even pages (verso, :left):  inside=right 0.80", outside=left 0.65"
    counter_val = "counter(page, lower-roman)" if roman else "counter(page)"
    num_css = f"""content: {counter_val};
                font-size: 8.5pt;
                color: #999;
                font-family: Georgia, serif;"""
    page_override = textwrap.dedent(f"""\
        @page :right {{
            margin: 0.75in 0.65in 0.75in 0.80in;
            @bottom-center {{ {num_css} }}
        }}
        @page :left {{
            margin: 0.75in 0.80in 0.75in 0.65in;
            @bottom-center {{ {num_css} }}
        }}
    """)
    if roman:
        page_override += "@page:first { @bottom-center { content: none; } }\n"

    # Devanagari glyphs render visually smaller than Latin at the same pt size.
    # Scale body + blockquote up by 1pt while pinning line-height as an absolute
    # value (11pt × 1.4 = 15.4pt) so the line pitch — and therefore page count —
    # stays identical to the English build.
    lang_override = ""
    if lang != "en":
        lang_override = textwrap.dedent(f"""\
            body       {{ font-size: 11pt; line-height: 16pt; font-family: '{FONT_NAME}', Georgia, serif; }}
            blockquote {{ font-size: 11pt; line-height: 19pt; }}
            .festival-index table {{ line-height: 1.45; }}
            h2         {{ font-size: 9.5pt; letter-spacing: 0.5pt; }}
        """)

    return font_faces + "\n" + base_css + "\n" + page_override + "\n" + lang_override


# ── Build steps ────────────────────────────────────────────────────────────────

def _build_html(md: str, html_path: str, css_path: str) -> None:
    meta_yaml = os.path.join(SAMPLE_DIR, "metadata.yaml")
    cmd = [
        "pandoc", "-",
        "--metadata-file", meta_yaml,
        "-t", "html5", "--standalone",
        "--css", css_path,
        "-o", html_path,
    ]
    subprocess.run(cmd, input=md.encode(), check=True)


def _run_weasyprint(html_path: str, pdf_path: str) -> None:
    result = subprocess.run(["weasyprint", html_path, pdf_path],
                            capture_output=True, text=True)
    if result.returncode != 0:
        print("WeasyPrint stderr:", result.stderr[-2000:], file=sys.stderr)
        result.check_returncode()


def _extract_anchor_pages(pdf_path: str) -> dict:
    """Return slug → page number (1-indexed) from named destinations in a PDF.
    WeasyPrint generates a named destination for every HTML element with an id."""
    try:
        from pypdf import PdfReader
        reader = PdfReader(pdf_path)
        dests = reader.named_destinations or {}
        # Build indirect-ref → 1-indexed page number map
        ref_to_num = {}
        for i, page in enumerate(reader.pages):
            ref = getattr(page, 'indirect_reference', None)
            if ref is not None:
                ref_to_num[ref] = i + 1
        result = {}
        for name, dest in dests.items():
            try:
                pg = dest.page
                ref = getattr(pg, 'indirect_reference', None)
                if ref is not None and ref in ref_to_num:
                    result[name] = ref_to_num[ref]
            except Exception:
                pass
        return result
    except Exception as e:
        print(f"  Warning: anchor extraction failed ({e})", file=sys.stderr)
        return {}


def _pad_to_even_pages(pdf_path: str) -> int:
    """If pdf_path has an odd page count, append a blank page so chapters always
    land on an odd physical position (recto) in the merged PDF.
    Returns the final page count."""
    from pypdf import PdfWriter, PdfReader
    reader = PdfReader(pdf_path)
    count = len(reader.pages)
    if count % 2 == 0:
        return count
    # 6×9 in points (1 pt = 1/72 in)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    writer.add_blank_page(width=6 * 72, height=9 * 72)
    with open(pdf_path, "wb") as f:
        writer.write(f)
    print(f"  Front matter was {count} pages (odd) — blank page added → {count + 1} pages.")
    return count + 1


def _merge_pdfs(inputs: list, output: str) -> None:
    from pypdf import PdfWriter, PdfReader
    writer = PdfWriter()
    for path in inputs:
        for page in PdfReader(path).pages:
            writer.add_page(page)
    with open(output, "wb") as f:
        writer.write(f)


def build_epub(combined_md: str, out_path: str, lang: str) -> None:
    epub_css  = os.path.join(SAMPLE_DIR, "epub.css")
    meta_yaml = os.path.join(SAMPLE_DIR, "metadata.yaml")
    cmd = [
        "pandoc", "-",
        "--metadata-file", meta_yaml,
        "-t", "epub3",
        "--toc", "--toc-depth=1", "--split-level=1",
        "--css", epub_css,
        "-o", out_path,
    ]
    if os.path.exists(EPUB_FONT_REGULAR):
        cmd += ["--epub-embed-font", EPUB_FONT_REGULAR]
    if os.path.exists(EPUB_FONT_BOLD):
        cmd += ["--epub-embed-font", EPUB_FONT_BOLD]
    subprocess.run(cmd, input=combined_md.encode(), check=True)


def build_pdf(entries: list, lang: str, html_path: str, pdf_path: str) -> None:
    """Two-pass PDF build:
      Pass 1 — chapters-only PDF (page 1 = first chapter, Arabic)
      Pass 2 — front-matter PDF with hardcoded page numbers (Roman, title suppressed)
      Merge   — front-matter PDF + chapters PDF → final PDF
    """
    out = str(OUTPUT_DIR)

    # Pass 1: chapters + back matter
    chap_md  = assemble_chapters_md(entries, lang)
    chap_css_path = os.path.join(out, "chapters-pdf.css")
    chap_html     = html_path.replace(".html", "-chapters.html")
    chap_pdf      = pdf_path.replace(".pdf",  "-chapters.pdf")
    with open(chap_css_path, "w") as f:
        f.write(build_css(roman=False, lang=lang))
    _build_html(chap_md, chap_html, chap_css_path)
    print("  Rendering chapters PDF …")
    _run_weasyprint(chap_html, chap_pdf)

    # Extract anchor → page from chapters PDF
    page_nums = _extract_anchor_pages(chap_pdf)
    print(f"  {len(page_nums)} chapter page anchors resolved.")

    # Pass 2: front matter with computed page numbers
    front_md  = assemble_front_md(entries, lang, page_nums)
    front_css_path = os.path.join(out, "front-pdf.css")
    front_html     = html_path.replace(".html", "-front.html")
    front_pdf      = pdf_path.replace(".pdf",  "-front.pdf")
    with open(front_css_path, "w") as f:
        f.write(build_css(roman=True, lang=lang))
    _build_html(front_md, front_html, front_css_path)
    print("  Rendering front-matter PDF …")
    _run_weasyprint(front_html, front_pdf)

    # Ensure front matter ends on an even physical page so that:
    #   - chapter 1 lands on position (front_pages + 1) = odd = recto
    #   - every chapter page's recto/verso assignment is preserved in the merged PDF
    front_pages = _pad_to_even_pages(front_pdf)
    print(f"  Front matter: {front_pages} pages (even — chapter 1 will be recto in merged PDF).")

    # Merge: front matter (Roman, even pages) + chapters (Arabic from 1)
    print("  Merging PDFs …")
    _merge_pdfs([front_pdf, chap_pdf], pdf_path)

    # Keep the chapters HTML as the main inspection file
    import shutil
    shutil.copy2(chap_html, html_path)


# ── Main ───────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lang", default="en", choices=["en", "hi", "mr", "gu"])
    parser.add_argument("--font", default=None, choices=list(FONT_REGISTRY),
                        help="PDF body font (noto|mangal|nirmala). EPUB always uses noto. Defaults to nirmala for hi, noto otherwise.")
    args = parser.parse_args()
    lang = args.lang

    global FONT_REGULAR, FONT_BOLD, FONT_NAME
    font_key = args.font or ("nirmala" if lang == "hi" else "noto")
    _f = FONT_REGISTRY[font_key]
    FONT_REGULAR = _f["regular"]
    FONT_BOLD    = _f["bold"]
    FONT_NAME    = _f["name"]

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    all_entries = {e.slug: e for e in load_entries("festivals")}
    slug_set = SLUG_SETS[lang]
    missing = [s for s in slug_set if s not in all_entries]
    if missing:
        print(f"Warning: slugs not found: {missing}", file=sys.stderr)

    curated = [all_entries[s] for s in slug_set if s in all_entries]
    entries = order_by_date(curated)

    print(f"Building {len(entries)}-chapter {lang.upper()} book …")
    combined_md = assemble(entries, lang)

    epub_out = str(OUTPUT_DIR / f"full-{lang}.epub")
    html_out = str(OUTPUT_DIR / f"full-{lang}.html")
    pdf_out  = str(OUTPUT_DIR / f"full-{lang}.pdf")

    print("Building EPUB3 …")
    build_epub(combined_md, epub_out, lang)
    print(f"  ✓ {epub_out}  ({os.path.getsize(epub_out)//1024} KB)")

    print("Building PDF …")
    build_pdf(entries, lang, html_out, pdf_out)
    print(f"  ✓ {pdf_out}  ({os.path.getsize(pdf_out)//1024} KB)")
    print(f"  (inspect chapters HTML: {html_out})")


if __name__ == "__main__":
    main()
