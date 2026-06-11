# atmasanatan-content

Canonical, single-source-of-truth content corpus for **Atma Sanatan** — kathas, festivals,
vrat guides, and (later) verses and bhajans.

This repo holds **content, not code**. One canonical source per item; build scripts transform
it into every consumer:

```
                     ┌─────────────────────────┐
                     │  kathas/  (canonical MD) │
                     └────────────┬────────────┘
                                  │  build/
          ┌───────────────────────┼───────────────────────┐
          ▼                       ▼                        ▼
  to_book_manuscript.py    to_backend_seed.py       to_reel_script.py
   KDP book manuscript      backend seed JSON         reel / video scripts
  (festival-vrat book)     (app Kathas section)      (Instagram / YouTube)
```

Edit content here once. The book, the app, and the videos all build from the same source —
no drift.

## Layout

```
atmasanatan-content/
├── kathas/
│   ├── festivals/
│   │   └── <slug>/
│   │       ├── meta.yaml        # language-neutral facts (type, deity, panchang, sources)
│   │       ├── en.md            # English prose (front-matter + standard sections)
│   │       ├── hi.md            # Hindi
│   │       ├── mr.md            # Marathi
│   │       └── gu.md            # Gujarati
│   └── _template/
│       └── festival-slug/       # copy this folder to start a new entry
├── build/
│   ├── to_book_manuscript.py    # → build/output/festival-vrat-companion-<lang>.md
│   ├── to_backend_seed.py       # → build/output/seed/<slug>.json   (stub)
│   ├── to_reel_script.py        # → build/output/reels/<slug>-<lang>.md (stub)
│   └── requirements.txt
├── CONTENT_FORMAT.md            # the schema every entry must follow
└── README.md
```

## First deliverable

The **Festival & Vrat Companion** book (KDP paperback-first). Each festival folder becomes one
chapter. Run:

```bash
pip install -r build/requirements.txt
python build/to_book_manuscript.py --lang en
# → build/output/festival-vrat-companion-en.md  (hand off to the docx/pdf skill for KDP)
```

## Languages

`en` · `hi` · `mr` · `gu`. Each language is its own `.md` file with identical structure so a
build can target any single language.

## Status / accuracy

Every `meta.yaml` carries a `status:` field (`draft` → `reviewed` → `published`) and a
`sources:` list. **Dates and tithis must be verified against DrikPanchang before an entry is
marked `published`** (see CONTENT_FORMAT.md). Placeholders are marked `TODO-VERIFY`.
