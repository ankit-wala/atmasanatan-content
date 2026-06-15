# Content Format — schema for every katha entry

Every entry is a folder under `kathas/<group>/<slug>/` containing one `meta.yaml` plus one
markdown file per language. **Keep structure identical across all entries** — the build
scripts extract content by these exact keys and headings.

---

## 1. `meta.yaml` — language-neutral facts

```yaml
slug: diwali              # unique, lowercase, hyphenated — matches the folder name
type: festival            # festival | vrat | ekadashi
order: 100                # sort order within the book and app list (ascending)
category: major           # major | minor
deity:                    # primary deities, English canonical spelling
  - Lakshmi
  - Ganesha
  - Rama
panchang:
  month: Kartik           # Hindu lunar month
  paksha: Krishna         # Shukla | Krishna
  tithi: Amavasya
  date_2026: TODO-VERIFY  # YYYY-MM-DD — VERIFY against DrikPanchang before publishing
  date_2027: TODO-VERIFY  # second-year occurrence; same katha, different calendar date
region: pan-india         # pan-india | north-india | south-india | east-india | west-india | <state>
related_shlokas: []       # ids into a future verses corpus (leave [] for now)
related_bhajans: []       # ids into a future bhajans corpus
tags:
  - diwali
  - deepavali
  - lakshmi-puja
sources:                  # every factual/scriptural claim must trace to one of these
  - "DrikPanchang — Diwali"
  - "Valmiki Ramayana — return of Rama to Ayodhya"
scripture_ref: "Valmiki Ramayana, Yuddha Kanda"   # primary source: Purana/text + khanda + chapter
status: draft             # draft | reviewed | ready_to_publish | published
```

Rules:
- `date_2026` (and any tithi time) **must** be verified against DrikPanchang before `status:
  published`. Until then use `TODO-VERIFY`.
- `ready_to_publish` means content is fully reviewed and all `TODO-VERIFY` date fields have been
  confirmed against DrikPanchang — ready to flip to `published` once the final check is done.
- `slug` is the join key across the book, the backend seed, and reel outputs. Never reuse.

---

## 2. `<lang>.md` — per-language prose

YAML front-matter + standard section headings. **Do not rename or reorder the `##` headings** —
builds slice on them.

```markdown
---
slug: diwali
lang: en
title: "Diwali — The Festival of Lights"
subtitle: "When Ayodhya lit a million lamps"
summary: "Diwali marks the return of Lord Rama to Ayodhya and the worship of Lakshmi for prosperity."
reel_hook: "Why did an entire kingdom light a million lamps in one night?"
---

## Katha
The story, in narrative prose. This is the heart of the entry — the part that carries the book
and the reel. Write it as a story, not a summary.

## Significance
Why this festival matters; what it represents spiritually and culturally.

## Vidhi
How it is observed — puja steps, sequence, what to prepare. For a `type: vrat` entry this is the
vrat vidhi; for a festival it is the puja vidhi.

## Observance
Fasting rules, timing, do's and don'ts, parana (fast-breaking) where relevant.

## Mantras
Key shlokas / mantras with transliteration and one-line meaning. Keep Devanagari + transliteration.
```

Section presence:
- `## Katha`, `## Significance`, `## Vidhi` — **required** in every entry.
- `## Observance`, `## Mantras` — include when relevant (always for vrats).

---

## 3. Adding a new entry

1. Copy `kathas/_template/festival-slug/` → `kathas/festivals/<your-slug>/`.
2. Fill `meta.yaml`. Mark unverified dates `TODO-VERIFY`.
3. Write `en.md` first (canonical), then translate into `hi.md`, `mr.md`, `gu.md`.
4. Build & preview: `python build/to_book_manuscript.py --lang en`.
5. Verify dates against DrikPanchang → set `status: reviewed` → `published`.

---

## 4. Why content is decoupled from the app

The backend serves kathas from its DB, so a build step exports `meta.yaml` + the markdown into
seed JSON the backend imports (`to_backend_seed.py`). This is the one sync cost of keeping content
in its own repo — paid back by being able to edit a story without touching app or backend code,
and by one source feeding the book, the app, and the videos without drift.
