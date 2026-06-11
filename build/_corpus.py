"""Shared corpus loader for all build scripts.

One place that knows how to read the canonical content so the book / seed / reel
builders all see the same parsed structure. No external deps beyond PyYAML.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
KATHAS_DIR = REPO_ROOT / "kathas"
OUTPUT_DIR = REPO_ROOT / "build" / "output"

LANGS = ["en", "hi", "mr", "gu"]
# Standard section headings, in book order. Builds slice prose on these.
SECTIONS = ["Katha", "Significance", "Vidhi", "Observance", "Mantras"]

_FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)$", re.DOTALL)


@dataclass
class LangDoc:
    lang: str
    frontmatter: dict
    sections: dict          # heading -> body text (str)

    @property
    def title(self) -> str:
        return self.frontmatter.get("title", "")


@dataclass
class Entry:
    slug: str
    path: Path
    meta: dict
    docs: dict = field(default_factory=dict)   # lang -> LangDoc

    @property
    def order(self) -> int:
        return int(self.meta.get("order", 0))

    @property
    def status(self) -> str:
        return self.meta.get("status", "draft")


def _parse_markdown(text: str) -> tuple[dict, dict]:
    """Return (frontmatter dict, {heading: body})."""
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return {}, {}
    fm = yaml.safe_load(m.group(1)) or {}
    body = m.group(2)

    sections: dict[str, str] = {}
    current = None
    buf: list[str] = []
    for line in body.splitlines():
        h = re.match(r"^##\s+(.*?)\s*$", line)
        if h:
            if current is not None:
                sections[current] = "\n".join(buf).strip()
            current = h.group(1).strip()
            buf = []
        elif current is not None:
            buf.append(line)
    if current is not None:
        sections[current] = "\n".join(buf).strip()
    return fm, sections


def load_entries(group: str = "festivals") -> list[Entry]:
    """Load all entries under kathas/<group>/, sorted by `order`."""
    base = KATHAS_DIR / group
    entries: list[Entry] = []
    for entry_dir in sorted(base.iterdir()):
        if not entry_dir.is_dir() or entry_dir.name.startswith("_"):
            continue
        meta_path = entry_dir / "meta.yaml"
        if not meta_path.exists():
            continue
        meta = yaml.safe_load(meta_path.read_text(encoding="utf-8")) or {}
        entry = Entry(slug=meta.get("slug", entry_dir.name), path=entry_dir, meta=meta)
        for lang in LANGS:
            md = entry_dir / f"{lang}.md"
            if md.exists():
                fm, sections = _parse_markdown(md.read_text(encoding="utf-8"))
                entry.docs[lang] = LangDoc(lang=lang, frontmatter=fm, sections=sections)
        entries.append(entry)
    entries.sort(key=lambda e: e.order)
    return entries
