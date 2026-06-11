#!/usr/bin/env python3
"""STUB — turn a katha into a short reel / video script (Instagram + YouTube).

Pulls the hook + story + a closing question, the format that performed best on
@atma.sanatan. Output is a per-slide script you can feed into the reel pipeline in
the atmasanatan-assets repo (or Veo/Flow for animation).

Usage:
    python build/to_reel_script.py --slug diwali --lang hi
"""
from __future__ import annotations

import argparse

from _corpus import OUTPUT_DIR, load_entries


def build_script(slug: str, lang: str) -> str:
    entry = next((e for e in load_entries("festivals") if e.slug == slug), None)
    if entry is None:
        raise SystemExit(f"No entry with slug '{slug}'")
    doc = entry.docs.get(lang)
    if doc is None:
        raise SystemExit(f"No {lang}.md for '{slug}'")

    hook = doc.frontmatter.get("reel_hook", "")
    katha = doc.sections.get("Katha", "")
    # First two sentences of the katha as the body beat.
    body = " ".join(katha.replace("\n", " ").split(". ")[:2]).strip()

    return "\n".join([
        f"# Reel script — {doc.title} ({lang})",
        "",
        "## Slide 1 — HOOK",
        hook,
        "",
        "## Slide 2 — STORY",
        body,
        "",
        "## Slide 3 — CLOSING QUESTION (drives comments — the proven format)",
        "TODO: pose a debate/reflection question, e.g. 'What does this festival mean to you?'",
        "",
        "## CTA",
        "Follow @atma.sanatan for daily kathas.",
        "",
        "<!-- TODO: split body into beats sized to video duration; see atmasanatan-assets CLAUDE.md TTS rule -->",
    ])


def main() -> None:
    ap = argparse.ArgumentParser(description="Build a reel/video script from a katha.")
    ap.add_argument("--slug", required=True)
    ap.add_argument("--lang", default="hi")
    args = ap.parse_args()

    script = build_script(args.slug, args.lang)
    reels_dir = OUTPUT_DIR / "reels"
    reels_dir.mkdir(parents=True, exist_ok=True)
    out_path = reels_dir / f"{args.slug}-{args.lang}.md"
    out_path.write_text(script, encoding="utf-8")
    print(f"✓ {out_path}")


if __name__ == "__main__":
    main()
