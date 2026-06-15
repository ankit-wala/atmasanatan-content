# CLAUDE.md — atmasanatan-content

Guidance for Claude when working in this repository.

## What this repo is

The **canonical, single-source-of-truth content corpus** for Atma Sanatan — kathas, festivals,
and vrat guides (verses and bhajans may move here later). It holds **content, not application
code.** One canonical source per item; small build scripts transform it into every consumer.

```
        kathas/  (canonical Markdown + YAML)
                      │  build/
   ┌──────────────────┼──────────────────┐
   ▼                  ▼                   ▼
 book manuscript   backend seed JSON    reel / video scripts
 (KDP paperback)   (app Kathas section) (Instagram / YouTube)
```

Edit content here once — the book, the app, and the videos all build from the same source, so
nothing drifts.

### Sibling repos (context, not edited from here)
- `hindu_saar_mobile/` — the Atma Sanatan KMP app (consumes katha content via the backend API).
- `hindusaar-web-backend/` — Django backend + DB + seeders (imports the seed JSON this repo emits).
- `atmasanatan-assets/` — reel/carousel production tooling and marketing assets.

## Repository layout

```
atmasanatan-content/
├── kathas/
│   ├── festivals/<slug>/
│   │   ├── meta.yaml      # language-neutral facts (data layer)
│   │   ├── en.md  hi.md  mr.md  gu.md   # prose layer, one file per language
│   └── _template/festival-slug/         # copy to start a new entry
├── build/
│   ├── _corpus.py             # shared loader — all builds read the corpus through this
│   ├── to_book_manuscript.py  # → build/output/festival-vrat-companion-<lang>.md  (working)
│   ├── to_backend_seed.py     # → build/output/seed/<slug>.json   (stub: align to backend model)
│   ├── to_reel_script.py      # → build/output/reels/<slug>-<lang>.md   (stub)
│   └── requirements.txt       # PyYAML
├── CONTENT_FORMAT.md          # the authoritative schema spec — read before adding content
├── README.md
└── CLAUDE.md                  # this file
```

## The two layers of an entry

1. **`meta.yaml` — data layer (language-neutral).** slug, `type` (festival|vrat|ekadashi),
   `order`, `deity`, `panchang` (month/paksha/tithi/`date_2026`), `region`, `tags`, `sources`,
   `status`. Facts live here once, never duplicated across languages.
2. **`<lang>.md` — prose layer.** YAML front-matter (`title`, `subtitle`, `summary`, `reel_hook`)
   + standard section headings. The builds slice prose on these exact `##` headings, in order:
   **`## Katha` · `## Significance` · `## Vidhi` · `## Observance` · `## Mantras`**. Do not
   rename or reorder them. `Katha`/`Significance`/`Vidhi` are required; `Observance`/`Mantras`
   when relevant (always for vrats).

Full schema is in `CONTENT_FORMAT.md` — read it before creating or editing entries.

## Rules (do not break these)

- **DrikPanchang date rule.** Every date/tithi must be verified against
  [DrikPanchang](https://www.drikpanchang.com/) before an entry's `status` becomes `published`.
  Unverified dates are written literally as `TODO-VERIFY`. The book builder injects a warning
  comment whenever it sees an unverified date — never silence that warning by faking a date.
- **Status lifecycle:** `draft` → `reviewed` → `ready_to_publish` → `published`. The book
  builder ships `reviewed`/`ready_to_publish`/`published` entries by default (`--include-drafts`
  is preview-only). `ready_to_publish` means content is fully reviewed AND all `TODO-VERIFY`
  date fields have been confirmed against DrikPanchang — it is the final holding state before
  flipping to `published`. Do not mark an entry `published` until its facts are sourced and its
  date verified.
- **Sources required.** Every factual/scriptural claim should trace to an entry in `meta.yaml`
  `sources:`. Prefer primary scripture (Valmiki Ramayana, Padma Purana, etc.) + DrikPanchang.
- **Never hand-edit `build/output/`.** It is generated and gitignored. Change the canonical
  source, then rebuild.
- **`slug` is the join key** across book, seed, and reels. Unique, lowercase-hyphenated, matches
  the folder name, and never reused.
- **Mantras stay in Devanagari** plus transliteration — keep them intact across all languages.
- **Religious-content care.** This is devotional material. Be accurate and respectful; do not
  invent scripture, attribute fabricated quotes, or embellish doctrine. When unsure of a fact,
  mark it `TODO-VERIFY` rather than guessing.

## Common tasks

### Write a katha entry (stub → reviewed)
**Read `WRITING_GUIDE.md` first** — it is the complete 5-phase procedure with checklist.
Short version:
1. Read `scripture_ref` in `meta.yaml`. Find the source at wisdomlib.org or Gita Press.
2. Verify `date_2026` + `date_2027` on DrikPanchang. Fill both fields in `meta.yaml`.
3. Write `hi.md` first (Gita Press Hindi source; Katha 300–700w · Significance · Vidhi · Observance · Mantras). English (`en.md`) is translated from Hindi, not written independently.
4. Pass the quality checklist in `WRITING_GUIDE.md`.
5. `python3 build/to_book_manuscript.py --lang hi --include-drafts` — confirm it renders.
6. Set `status: reviewed`. Translate hi.md → en.md → mr.md → gu.md.
7. Verify `date_2026` + `date_2027` on DrikPanchang → set `status: ready_to_publish`.
8. Owner final check → set `status: published`.

### Add a brand-new entry (not already stubbed)
1. `cp -r kathas/_template/festival-slug kathas/festivals/<slug>` (rename to the real slug).
2. Fill `meta.yaml` completely including `scripture_ref`.
3. Add the entry to `KATHA_CALENDAR.md` in the correct month block.
4. Then follow the write procedure above.

### Build commands

> **Python note (macOS):** Use `/usr/bin/python3` (system Python 3.9.6) — it has PyYAML
> pre-installed and the build scripts work reliably with it. Do NOT use Homebrew Python
> (`/opt/homebrew/bin/python3`, currently 3.14) — it lacks PyYAML and has a libexpat ABI
> mismatch that breaks the XML parser. Subagents should use `/usr/bin/python3` explicitly.

```bash
/usr/bin/pip3 install -r build/requirements.txt     # if PyYAML ever needs reinstalling

/usr/bin/python3 build/to_book_manuscript.py --lang en        # KDP manuscript (published/reviewed only)
/usr/bin/python3 build/to_book_manuscript.py --lang hi --include-drafts   # preview incl. drafts
/usr/bin/python3 build/to_backend_seed.py                      # app seed JSON for every entry
python build/to_reel_script.py --slug diwali --lang hi          # one reel script
```

### Produce the actual KDP book
The book builder emits Markdown. To make the paperback/ebook file, hand the generated
`build/output/festival-vrat-companion-<lang>.md` to the `docx` or `pdf` skill for KDP formatting
(trim size, headings, page numbers, front matter). Do the content research/verification first,
then invoke the format skill.

## Languages
`en` · `hi` · `mr` · `gu`. Each is its own `.md` with identical structure so any single language
can be built independently.

**Primary language is Hindi** (`hi.md`) for almost all entries — Gita Press Hindi editions are
the working source text. Translation order: `hi.md` → `en.md` → `mr.md` → `gu.md`. Translate
`mr.md` and `gu.md` from `hi.md`, not from `en.md`.

## First deliverable
The **Festival & Vrat Companion** book (KDP paperback-first) — each festival folder is one
chapter. Prioritize entries whose dates can be verified against DrikPanchang.
