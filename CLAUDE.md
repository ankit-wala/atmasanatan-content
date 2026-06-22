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
 book / EPUB / PDF  backend seed JSON    reel / video scripts
 (KDP paperback)    (app Kathas section) (Instagram / YouTube)
```

Edit content here once — the book, the app, and the videos all build from the same source, so
nothing drifts.

### Sibling repos (context, not edited from here)
- `hindu_saar_mobile/` — the Atma Sanatan KMP app (consumes katha content via the backend API).
- `hindusaar-web-backend/` — Django backend + DB + seeders (imports the seed JSON this repo emits).
- `atmasanatan-assets/` — reel/carousel production tooling and marketing assets.

---

## Repository layout

```
atmasanatan-content/
├── kathas/
│   ├── festivals/<slug>/
│   │   ├── meta.yaml        # language-neutral facts (data layer)
│   │   ├── en.md            # English prose
│   │   ├── hi.md            # Hindi prose (primary / source language)
│   │   ├── mr.md            # Marathi prose
│   │   └── gu.md            # Gujarati prose
│   └── _template/festival-slug/   # copy this to start a new entry
├── build/
│   ├── _corpus.py           # shared loader — ALL builds read corpus through this
│   ├── to_book_manuscript.py      # full 150-entry manuscript → build/output/
│   ├── to_sample_book.py          # 4-katha sample → EPUB3 + PDF (working, preferred)
│   ├── to_backend_seed.py         # per-entry JSON for the Django seeder (stub)
│   ├── to_reel_script.py          # one-slug reel script in any language (stub)
│   ├── kdp.css                    # basic 6×9 stylesheet for full manuscript PDF
│   ├── sample/
│   │   ├── metadata.yaml          # EPUB title/author/rights metadata
│   │   └── epub.css               # EPUB3 stylesheet (separate from PDF CSS)
│   ├── fonts/
│   │   └── NotoSerifDevanagari/   # embedded in EPUB + PDF for Devanagari rendering
│   ├── fill_dates_2026.py         # utility: bulk-fill date_2026 fields
│   ├── upgrade_status.py          # utility: bulk-promote entry statuses
│   ├── seed_extras.py / seed_stubs.py   # one-off seed helpers
│   └── requirements.txt           # PyYAML only
├── build/output/            # GENERATED — gitignored, never hand-edit
│   ├── festival-vrat-companion-en.md   # full English manuscript (150 entries)
│   ├── festival-vrat-companion-hi.md   # full Hindi manuscript
│   ├── festival-vrat-companion-mr.md   # full Marathi manuscript
│   ├── festival-vrat-companion-gu.md   # full Gujarati manuscript
│   ├── sample-en.epub               # 4-katha EPUB3 sample (with font + ToC)
│   ├── sample-en.pdf                # 4-katha PDF sample (6×9, Noto font)
│   ├── sample-en.html               # intermediate HTML for the PDF (keep for inspection)
│   ├── sample-pdf.css               # generated PDF stylesheet (saffron/crimson KDP theme)
│   ├── seed/<slug>.json             # per-entry seed JSON for the backend
│   └── reels/<slug>-<lang>.md       # reel scripts
├── CONTENT_FORMAT.md        # authoritative schema spec — read before adding content
├── WRITING_GUIDE.md         # 5-phase write procedure with quality checklist
├── KATHA_CALENDAR.md        # entries ordered by the Hindu calendar year
├── README.md
└── CLAUDE.md                # this file
```

---

## Corpus state (as of June 2026)

- **150 entries**, all `status: ready_to_publish`
- **4 languages complete**: `en` · `hi` · `mr` · `gu` — 150 files each, 600 content files total
- **Sections per entry**: `## Katha` · `## Significance` · `## Vidhi` · `## Mantras`
  - `## Observance` was merged into `## Vidhi` (June 2026) as a compact bullet list to reduce
    book length. The corpus parser still supports `Observance` as a section key, but no current
    files use it — everything is in `Vidhi`.
- **Page stats** (English, 6×9 KDP, 11pt Palatino): median ~4 pages/katha · min ~2.5 · max ~6.5
  · total ~620 pages

---

## The two layers of an entry

1. **`meta.yaml` — data layer (language-neutral).** slug, `type` (festival|vrat|ekadashi),
   `order`, `deity`, `panchang` (month/paksha/tithi/`date_2026`/`date_2027`), `region`, `tags`,
   `sources`, `status`. Facts live here once, never duplicated across languages.
2. **`<lang>.md` — prose layer.** YAML front-matter (`title`, `subtitle`, `summary`, `reel_hook`)
   + standard section headings. The builds slice prose on these exact `##` headings, in order:
   **`## Katha` · `## Significance` · `## Vidhi` · `## Mantras`**.
   Do not rename or reorder them. `Katha`/`Significance`/`Vidhi` are required; `Mantras` always
   present. `Observance` is retired — merge any observance content into `Vidhi` as bullet points.

Full schema is in `CONTENT_FORMAT.md` — read it before creating or editing entries.

---

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
- **Mantras stay in Devanagari** plus IAST transliteration — keep them intact across all languages.
- **Gujarati files: scan for Bengali script.** After any bulk generation or editing of `gu.md`
  files, run `grep -rl $'[ঀ-৿]' kathas/festivals --include="gu.md"` before committing.
  Bengali (U+0980–U+09FF) and Gujarati (U+0A80–U+0AFF) characters are visually similar but
  completely different — LLMs sometimes emit Bengali when writing Gujarati.
- **Religious-content care.** This is devotional material. Be accurate and respectful; do not
  invent scripture, attribute fabricated quotes, or embellish doctrine. When unsure of a fact,
  mark it `TODO-VERIFY` rather than guessing.

---

## Common tasks

### Write a katha entry (stub → reviewed)
**Read `WRITING_GUIDE.md` first** — it is the complete 5-phase procedure with checklist.
Short version:
1. Read `scripture_ref` in `meta.yaml`. Find the source at wisdomlib.org or Gita Press.
2. Verify `date_2026` + `date_2027` on DrikPanchang. Fill both fields in `meta.yaml`.
3. Write `hi.md` first (Gita Press Hindi source; Katha 300–700w · Significance · Vidhi · Mantras).
   English (`en.md`) is translated from Hindi, not written independently.
4. Pass the quality checklist in `WRITING_GUIDE.md`.
5. `/usr/bin/python3 build/to_book_manuscript.py --lang hi --include-drafts` — confirm it renders.
6. Set `status: reviewed`. Translate hi.md → en.md → mr.md → gu.md.
7. Verify `date_2026` + `date_2027` on DrikPanchang → set `status: ready_to_publish`.
8. Owner final check → set `status: published`.

### Vidhi section format (current standard)
All Vidhi sections use a compact bullet list — no separate Observance section:
```markdown
## Vidhi

- **उपवास:** पूर्ण निर्जल; असमर्थ हों तो फल संभव
- **सायंकाल पूजन:** मूर्ति स्थापित करें; फूल, दूर्वा, दीप अर्पण; नैवेद्य; मंत्रजप; आरती
- **रात्रि:** चंद्रोदय के बाद व्रत तोड़ें — चंद्रदर्शन अनिवार्य; प्रसाद ग्रहण करें
- **2026 तिथि:** TODO-VERIFY (पौष कृष्ण चतुर्थी)
```
5–10 bullets; **bold labels** for stages; semicolons to chain related items; date always last.

### Page-reduction decisions (June 2026)

Options from the publishing analysis artifact — status of each:

| Option | Description | Decision |
|--------|-------------|----------|
| A | Compress Vidhi + Observance into bullet list | **Done** — all 600 files (hi/en/mr/gu), −50 pages |
| B | Cut Significance to a 2-line pull quote | **Rejected** — sampled 5 entries; most Significance sections are genuinely additive (symbolism, etymology, theological framing). Only ~half have any restatement, and those restate just 1–2 sentences. Not worth gutting sections that add real depth. |
| F | Remove forced chapter page-breaks (continuous flow) | **Parked** — saves ~30–40 pages, pure CSS change. Revisit when finalising layout. |

### Add a brand-new entry (not already stubbed)
1. `cp -r kathas/_template/festival-slug kathas/festivals/<slug>` (rename to the real slug).
2. Fill `meta.yaml` completely including `scripture_ref`.
3. Add the entry to `KATHA_CALENDAR.md` in the correct month block.
4. Follow the write procedure above.

---

## Build system

### Python note (macOS)
Use `/usr/bin/python3` (system Python 3.9.6) — it has PyYAML pre-installed and the build scripts
work reliably with it. Do NOT use Homebrew Python (`/opt/homebrew/bin/python3`, currently 3.14)
— it lacks PyYAML and has a libexpat ABI mismatch that breaks the XML parser.
**Subagents must use `/usr/bin/python3` explicitly.**

### Tool stack (confirmed working)
| Tool | Path | Version | Used for |
|------|------|---------|----------|
| Python | `/usr/bin/python3` | 3.9.6 | all build scripts |
| pandoc | `/opt/homebrew/bin/pandoc` | 3.10 | Markdown → HTML → EPUB3 |
| weasyprint | `/opt/homebrew/bin/weasyprint` | — | HTML → PDF |
| Noto Serif Devanagari | `build/fonts/` | — | embedded in EPUB/PDF for Sanskrit |

### Build commands

```bash
# Reinstall PyYAML if needed
/usr/bin/pip3 install -r build/requirements.txt

# Full manuscripts (all 150 entries)
/usr/bin/python3 build/to_book_manuscript.py --lang en              # published/reviewed only
/usr/bin/python3 build/to_book_manuscript.py --lang hi --include-drafts   # preview incl. drafts
# → build/output/festival-vrat-companion-<lang>.md

# Backend seed JSON
/usr/bin/python3 build/to_backend_seed.py
# → build/output/seed/<slug>.json  (one file per entry)

# Reel script (one slug at a time)
/usr/bin/python3 build/to_reel_script.py --slug diwali --lang hi
# → build/output/reels/diwali-hi.md
```

### Produce the KDP book

**Sample edition (4 kathas — EPUB3 + PDF, recommended for KDP preview):**
```bash
/usr/bin/python3 build/to_sample_book.py
# → build/output/sample-en.epub   (188 KB, with Noto font + ToC)
# → build/output/sample-en.pdf    (114 KB, 6×9in, saffron/crimson theme)
# → build/output/sample-en.html   (intermediate HTML, keep for inspection)
# → build/output/sample-pdf.css   (generated stylesheet, do not hand-edit)
```
`to_sample_book.py` self-contains: front matter (invocation + intro), back matter (2026 calendar
+ about page), Noto Serif Devanagari font embedding, full PDF stylesheet (generated by
`make_pdf_css()` inline), and EPUB3 metadata from `build/sample/metadata.yaml`.
To change which 4 kathas appear, edit `SAMPLE_SLUGS` at the top of the script.

**Full manuscript → PDF (all 150 entries):**
```bash
# 1. Build Markdown manuscript
/usr/bin/python3 build/to_book_manuscript.py --lang en
# → build/output/festival-vrat-companion-en.md

# 2. Markdown → HTML
pandoc build/output/festival-vrat-companion-en.md \
  --from markdown --to html5 --standalone \
  --metadata title="Festival & Vrat Companion" \
  --css build/kdp.css \
  -o build/output/festival-vrat-companion-en.html

# 3. HTML → PDF
weasyprint build/output/festival-vrat-companion-en.html \
           build/output/festival-vrat-companion-en.pdf
```
`build/kdp.css` — basic 6×9 stylesheet (less polished than the sample theme; improve as needed).
Replace `en` with `hi` / `mr` / `gu` for other languages.

### build/output/ — what each file is

```
build/output/
├── festival-vrat-companion-en.md   ← full English manuscript, all 150 entries
├── festival-vrat-companion-hi.md   ← full Hindi manuscript
├── festival-vrat-companion-mr.md   ← full Marathi manuscript (~15,275 lines)
├── festival-vrat-companion-gu.md   ← full Gujarati manuscript (~15,174 lines)
├── sample-en.epub                  ← 4-katha EPUB3 for ebook stores / KDP preview
├── sample-en.pdf                   ← 4-katha PDF for KDP interior upload / review
├── sample-en.html                  ← intermediate HTML (weasyprint source); inspect styling here
├── sample-pdf.css                  ← auto-generated by to_sample_book.py; do NOT hand-edit
├── seed/
│   └── <slug>.json                 ← per-entry seed record for Django backend importer
└── reels/
    └── <slug>-<lang>.md            ← reel scripts
```

All of `build/output/` is gitignored — regenerate from source, never commit these files.

---

## Languages

`en` · `hi` · `mr` · `gu`. Each is its own `.md` with identical structure so any single language
can be built independently.

**Primary language is Hindi** (`hi.md`) — Gita Press Hindi editions are the working source text.
Translation order: `hi.md` → `en.md` → `mr.md` → `gu.md`.
Translate `mr.md` and `gu.md` directly from `hi.md`, not from `en.md`.

---

## Publishing targets

- **KDP (Kindle Direct Publishing)** — ebook (global) + print-on-demand paperback (US/global).
  Use KDP Select for 70% royalty on Amazon.in (India); without Select, India ebooks earn 35%.
- **Notion Press / Pothi.com** — Indian POD for local printing + Flipkart/physical retail.
  Both are non-exclusive for paperbacks, so the same book can be on KDP + Notion Press/Pothi
  simultaneously without conflict.
- All three platforms are non-exclusive for paperbacks — publish everywhere in parallel.

---

## First deliverable

The **Festival & Vrat Companion** book (KDP paperback-first) — each festival folder is one
chapter. All 150 entries are `ready_to_publish`. Next step: verify remaining `TODO-VERIFY` date
fields against DrikPanchang and flip entries to `published`.
