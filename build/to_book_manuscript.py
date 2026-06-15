#!/usr/bin/env python3
"""Build the Festival & Vrat Companion book manuscript from the canonical corpus.

Each festival folder becomes one chapter. Output is a single Markdown manuscript per
language — hand that to the `docx` or `pdf` skill to produce the KDP-ready file.

Usage:
    python build/to_book_manuscript.py --lang en
    python build/to_book_manuscript.py --lang hi --include-drafts

By default only entries with status `reviewed` or `published` are included (drafts are
skipped so an unfinished entry never ships in a book). Pass --include-drafts to preview.
"""
from __future__ import annotations

import argparse
import sys

from _corpus import OUTPUT_DIR, SECTIONS, load_entries

# Friendly section titles in each language (heading key -> display label).
SECTION_LABELS = {
    "en": {"Katha": "The Story", "Significance": "Significance", "Vidhi": "How to Observe",
           "Observance": "Fasting & Observance", "Mantras": "Mantras"},
    "hi": {"Katha": "कथा", "Significance": "महत्त्व", "Vidhi": "विधि",
           "Observance": "व्रत एवं नियम", "Mantras": "मंत्र"},
    "mr": {"Katha": "कथा", "Significance": "महत्त्व", "Vidhi": "विधी",
           "Observance": "व्रत व नियम", "Mantras": "मंत्र"},
    "gu": {"Katha": "કથા", "Significance": "મહત્ત્વ", "Vidhi": "વિધિ",
           "Observance": "વ્રત અને નિયમ", "Mantras": "મંત્ર"},
}

BOOK_TITLE = {
    "en": "The Hindu Festival & Vrat Companion",
    "hi": "हिंदू त्योहार एवं व्रत संगिनी",
    "mr": "हिंदू सण व व्रत संगिनी",
    "gu": "હિંદુ તહેવાર અને વ્રત સંગિની",
}


def build(lang: str, include_drafts: bool) -> str:
    entries = load_entries("festivals")
    if not include_drafts:
        entries = [e for e in entries if e.status in ("reviewed", "ready_to_publish", "published")]

    labels = SECTION_LABELS.get(lang, SECTION_LABELS["en"])
    out: list[str] = []

    # Title page
    out.append(f"# {BOOK_TITLE.get(lang, BOOK_TITLE['en'])}\n")
    out.append("> Atma Sanatan\n\n---\n")

    # Table of contents
    out.append("## Contents\n")
    for e in entries:
        doc = e.docs.get(lang)
        if doc:
            out.append(f"- {doc.title}")
    out.append("\n---\n")

    # Chapters
    skipped: list[str] = []
    for e in entries:
        doc = e.docs.get(lang)
        if not doc:
            skipped.append(f"{e.slug} (no {lang}.md)")
            continue
        out.append(f"\n# {doc.title}\n")
        if doc.frontmatter.get("subtitle"):
            out.append(f"*{doc.frontmatter['subtitle']}*\n")
        # Unverified-date guard for the book.
        if str(e.meta.get("panchang", {}).get("date_2026", "")).startswith("TODO"):
            out.append("<!-- WARNING: date_2026 not yet verified against DrikPanchang -->\n")
        for sec in SECTIONS:
            body = doc.sections.get(sec)
            if body and "TODO" not in body[:8]:
                out.append(f"\n## {labels.get(sec, sec)}\n\n{body}\n")
        out.append("\n---\n")

    if skipped:
        sys.stderr.write("Skipped (missing translation):\n  " + "\n  ".join(skipped) + "\n")

    return "\n".join(out)


def main() -> None:
    ap = argparse.ArgumentParser(description="Build the festival-vrat book manuscript.")
    ap.add_argument("--lang", default="en", help="en | hi | mr | gu")
    ap.add_argument("--include-drafts", action="store_true",
                    help="include status: draft entries (preview only)")
    args = ap.parse_args()

    manuscript = build(args.lang, args.include_drafts)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUTPUT_DIR / f"festival-vrat-companion-{args.lang}.md"
    out_path.write_text(manuscript, encoding="utf-8")
    print(f"✓ {out_path}  ({len(manuscript.splitlines())} lines)")
    print("  Next: hand this to the docx/pdf skill to produce the KDP-ready file.")


if __name__ == "__main__":
    main()
