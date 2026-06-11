#!/usr/bin/env python3
"""STUB — export the corpus as backend seed JSON for the app's Kathas section.

This is the one "sync step" of keeping content in its own repo: it turns the canonical
markdown into JSON the Django backend seeder imports. Wire the output shape to the
backend's actual Katha/Festival model when that model is finalized.

Usage:
    python build/to_backend_seed.py            # writes build/output/seed/<slug>.json
"""
from __future__ import annotations

import json

from _corpus import LANGS, OUTPUT_DIR, SECTIONS, load_entries


def entry_to_record(e) -> dict:
    """Map one corpus entry to a backend-shaped record.

    TODO: align field names with the backend Katha/Festival model once defined.
    """
    translations = {}
    for lang in LANGS:
        doc = e.docs.get(lang)
        if not doc:
            continue
        translations[lang] = {
            "title": doc.frontmatter.get("title", ""),
            "subtitle": doc.frontmatter.get("subtitle", ""),
            "summary": doc.frontmatter.get("summary", ""),
            "sections": {sec: doc.sections.get(sec, "") for sec in SECTIONS},
        }
    return {
        "slug": e.slug,
        "type": e.meta.get("type"),
        "order": e.order,
        "deity": e.meta.get("deity", []),
        "panchang": e.meta.get("panchang", {}),
        "tags": e.meta.get("tags", []),
        "status": e.status,
        "translations": translations,
    }


def main() -> None:
    seed_dir = OUTPUT_DIR / "seed"
    seed_dir.mkdir(parents=True, exist_ok=True)
    entries = load_entries("festivals")
    for e in entries:
        rec = entry_to_record(e)
        (seed_dir / f"{e.slug}.json").write_text(
            json.dumps(rec, ensure_ascii=False, indent=2), encoding="utf-8"
        )
    print(f"✓ wrote {len(entries)} seed file(s) to {seed_dir}")
    print("  TODO: align record shape with backend model; add an import management command.")


if __name__ == "__main__":
    main()
