#!/usr/bin/env python3
"""Build a 4-katha sample book as EPUB3 and PDF.

Selected entries (in calendar order):
  maha-shivaratri, nirjala-ekadashi, janmashtami, diwali

Usage:
    /usr/bin/python3 build/to_sample_book.py

Outputs:
    build/output/sample-en.epub
    build/output/sample-en.pdf
    build/output/sample-en.html   (intermediate, keep for inspection)
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
import textwrap
from datetime import datetime

sys.path.insert(0, os.path.dirname(__file__))
from _corpus import SECTIONS, OUTPUT_DIR, load_entries

SAMPLE_SLUGS = ["maha-shivaratri", "nirjala-ekadashi", "janmashtami", "diwali"]
LANG = "en"

SECTION_LABELS = {
    "Katha":       "The Story",
    "Significance":"Significance",
    "Vidhi":       "How to Observe",
    "Observance":  "Fasting & Observance",
    "Mantras":     "Mantras",
}

BUILD_DIR   = os.path.dirname(os.path.abspath(__file__))
SAMPLE_DIR  = os.path.join(BUILD_DIR, "sample")
FONTS_DIR   = os.path.join(BUILD_DIR, "fonts", "NotoSerifDevanagari", "unhinted", "ttf")

FONT_REGULAR = os.path.join(FONTS_DIR, "NotoSerifDevanagari-Regular.ttf")
FONT_BOLD    = os.path.join(FONTS_DIR, "NotoSerifDevanagari-Bold.ttf")


def strip_date_bullet(body: str) -> str:
    """Remove the trailing date bullet from Vidhi sections (e.g. '- **2026 date:** ...')."""
    return re.sub(r'\n- \*\*20\d\d[^\n]*', '', body)


# ── Content helpers ────────────────────────────────────────────────────────────

def front_matter() -> str:
    return textwrap.dedent("""\
        # Invocation

        ::: {.invocation}

        **श्री गणेशाय नमः**

        *Śrī Gaṇeśāya Namaḥ*

        ---

        > वक्रतुण्ड महाकाय सूर्यकोटिसमप्रभ ।
        > निर्विघ्नं कुरु मे देव सर्वकार्येषु सर्वदा ॥

        *Vakratuṇḍa Mahākāya Sūryakoṭisamaprabha |*
        *Nirvighnaṃ Kuru Me Deva Sarvakāryeṣu Sarvadā ||*

        O Lord with the curved trunk and the mighty form,
        radiant as ten million suns —
        grant me freedom from all obstacles, always, in every endeavour.

        :::

        # Introduction

        India has always measured time by festivals. The Hindu Panchang is not simply a calendar — it is a map of the sacred year, marking the days when a particular deity is closest, when the cosmos is aligned for a specific kind of worship, when the ancient stories are most alive.

        The festivals collected here have been observed for thousands of years. Their roots lie in the Puranas — the great narrative scriptures of the Hindu tradition — and their observances have been carried forward across generations, in temples and homes, across every corner of the subcontinent and now across the world. A Shivaratri fast observed in Varanasi and one observed in New Jersey draw on the same story, the same mantra, the same promise.

        This book is a companion — not a substitute for a priest or pandita, but a guide for those who want to know the story behind the flame, the meaning inside the mantra, the reason we do what we do on these sacred nights. Each entry has a *Katha* (the founding story), a *Significance* section, a *Vidhi* (how to perform the puja), and *Mantras* to recite. Vrat entries also include an *Observance* section covering the fast and its rules.

        Read the katha first. Let the story land. The puja will feel different after that.

        May your observance of each festival carry the full weight of its tradition.

        — *Atma Sanatan*

        ## How to Use This Book

        Each chapter covers one festival or vrat. **The Story** tells you why this day exists — the scripture narrative that gave this festival its meaning. **Significance** places it in the wider dharmic picture. **How to Observe** (Vidhi) gives the step-by-step puja. **Fasting & Observance** covers vrat rules where applicable. **Mantras** gives the key prayers with Devanagari script, IAST transliteration, and English meaning.

        Dates in this book are verified against the DrikPanchang for 2026. Dates change each year — always confirm tithi timings on DrikPanchang before observing.

    """)


def format_chapter(entry) -> str:
    doc = entry.docs.get(LANG)
    if not doc:
        return ""

    panchang  = entry.meta.get("panchang", {})
    date_str  = str(panchang.get("date_2026", ""))

    lines = [f"# {doc.title}\n"]

    if doc.frontmatter.get("subtitle"):
        lines.append(f"*{doc.frontmatter['subtitle']}*\n")

    if date_str and not date_str.startswith("TODO"):
        try:
            dt = datetime.strptime(date_str, "%Y-%m-%d")
            formatted = dt.strftime("%B %-d, %Y")
            lines.append(f'<p class="panchang-date">2026 — {formatted}</p>\n')
        except ValueError:
            pass

    for sec in SECTIONS:
        body = doc.sections.get(sec, "")
        if body and not body.strip().startswith("TODO"):
            if sec == "Katha":
                lines.append(f"\n{body}\n")
            else:
                if sec == "Vidhi":
                    body = strip_date_bullet(body)
                label = SECTION_LABELS.get(sec, sec)
                lines.append(f"\n## {label}\n\n{body}\n")

    lines.append('\n<div class="chapter-end">✦ ✦ ✦</div>\n')
    return "\n".join(lines)


def back_matter() -> str:
    return textwrap.dedent("""\
        # Festival Calendar — 2026

        The four festivals in this sample edition fall on the following dates in 2026.
        All dates are verified against DrikPanchang.

        | Festival | Date | Panchang |
        |:---------|:-----|:---------|
        | Maha Shivaratri | February 15, 2026 | Phalguna Krishna Chaturdashi |
        | Nirjala Ekadashi | June 25, 2026 | Jyeshtha Shukla Ekadashi |
        | Janmashtami | September 4, 2026 | Bhadrapada Krishna Ashtami |
        | Diwali | November 8, 2026 | Kartik Krishna Amavasya |

        *Dates vary by year and location. Verify tithi timings on DrikPanchang
        before observing.*

        # About Atma Sanatan

        Atma Sanatan is a devotional publishing project dedicated to making the stories,
        meanings, and practices of the Hindu festival year accessible to practitioners
        across the world. All kathas draw on primary scriptural sources — the Skanda Purana,
        the Brahma Vaivarta Purana, the Valmiki Ramayana, the Shrimad Bhagavatam — and
        all dates are verified against DrikPanchang.

        This is a sample of *The Hindu Festival & Vrat Companion*, which covers over
        150 festivals and vratas of the Hindu year.

    """)


# ── Assembly ───────────────────────────────────────────────────────────────────

def assemble(entries) -> str:
    parts = [front_matter()]
    for entry in entries:
        chapter = format_chapter(entry)
        if chapter:
            parts.append(chapter)
    parts.append(back_matter())
    return "\n\n".join(parts)


# ── PDF CSS (font-face injected at build time; rules live in build/kdp.css) ────

def build_css() -> str:
    """Read kdp.css and prepend @font-face declarations with absolute file:// paths."""
    kdp_css_path = os.path.join(BUILD_DIR, "kdp.css")
    with open(kdp_css_path) as f:
        base_css = f.read()

    font_faces = ""
    if os.path.exists(FONT_REGULAR):
        font_faces += (
            f"@font-face {{\n"
            f"    font-family: 'NotoSerifDevanagari';\n"
            f"    src: url('file://{FONT_REGULAR}');\n"
            f"    font-weight: normal;\n}}\n"
        )
    if os.path.exists(FONT_BOLD):
        font_faces += (
            f"@font-face {{\n"
            f"    font-family: 'NotoSerifDevanagari';\n"
            f"    src: url('file://{FONT_BOLD}');\n"
            f"    font-weight: bold;\n}}\n"
        )
    return font_faces + "\n" + base_css

# ── Build steps ────────────────────────────────────────────────────────────────

def build_epub(combined_md: str, out_path: str) -> None:
    epub_css   = os.path.join(SAMPLE_DIR, "epub.css")
    meta_yaml  = os.path.join(SAMPLE_DIR, "metadata.yaml")

    cmd = [
        "pandoc", "-",
        "--metadata-file", meta_yaml,
        "-t", "epub3",
        "--toc",
        "--toc-depth=1",
        "--split-level=1",
        "--css", epub_css,
        "-o", out_path,
    ]
    if os.path.exists(FONT_REGULAR):
        cmd += ["--epub-embed-font", FONT_REGULAR]
    if os.path.exists(FONT_BOLD):
        cmd += ["--epub-embed-font", FONT_BOLD]

    subprocess.run(cmd, input=combined_md.encode(), check=True)


def build_pdf(combined_md: str, html_path: str, pdf_path: str) -> None:
    meta_yaml = os.path.join(SAMPLE_DIR, "metadata.yaml")

    pdf_css_content = build_css()
    pdf_css_path = os.path.join(str(OUTPUT_DIR), "sample-pdf.css")
    with open(pdf_css_path, "w") as f:
        f.write(pdf_css_content)

    cmd1 = [
        "pandoc", "-",
        "--metadata-file", meta_yaml,
        "-t", "html5",
        "--standalone",
        "--toc",
        "--toc-depth=1",
        "--css", pdf_css_path,
        "-o", html_path,
    ]
    subprocess.run(cmd1, input=combined_md.encode(), check=True)

    cmd2 = ["weasyprint", html_path, pdf_path]
    result = subprocess.run(cmd2, capture_output=True, text=True)
    if result.returncode != 0:
        print("WeasyPrint stderr:", result.stderr[-2000:], file=sys.stderr)
        result.check_returncode()


# ── Main ───────────────────────────────────────────────────────────────────────

def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    all_entries = {e.slug: e for e in load_entries("festivals")}
    entries = [all_entries[s] for s in SAMPLE_SLUGS if s in all_entries]
    missing = [s for s in SAMPLE_SLUGS if s not in all_entries]
    if missing:
        print(f"Warning: slugs not found: {missing}", file=sys.stderr)

    print(f"Assembling {len(entries)} chapters: {[e.slug for e in entries]}")
    combined_md = assemble(entries)

    epub_out = str(OUTPUT_DIR / "sample-en.epub")
    html_out = str(OUTPUT_DIR / "sample-en.html")
    pdf_out  = str(OUTPUT_DIR / "sample-en.pdf")

    print("Building EPUB3 …")
    build_epub(combined_md, epub_out)
    epub_mb = os.path.getsize(epub_out) / 1024
    print(f"  ✓ {epub_out}  ({epub_mb:.0f} KB)")

    print("Building PDF …")
    build_pdf(combined_md, html_out, pdf_out)
    pdf_mb = os.path.getsize(pdf_out) / 1024
    print(f"  ✓ {pdf_out}  ({pdf_mb:.0f} KB)")
    print(f"  (inspect HTML: {html_out})")


if __name__ == "__main__":
    main()
