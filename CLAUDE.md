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

### Atma Sanatan app — description (for book front matter and marketing copy)

A companion app for all things devotional. Current features: bhajans, mantras, daily shlokas,
rashifal, panchang, festivals calendar, and wallpapers — with more features coming soon.
Kathas will be live on the app by the time the book reaches buyers — do not say "coming soon" in book copy.
App URL: app.atmasanatan.com · Deep-link for book readers: app.atmasanatan.com/Yu6EECT

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
│   ├── to_full_book.py            # 108-katha KDP book → EPUB3 + PDF (primary build script)
│   ├── to_book_manuscript.py      # full 150-entry manuscript Markdown → build/output/
│   ├── to_sample_book.py          # 4-katha sample → EPUB3 + PDF
│   ├── to_backend_seed.py         # per-entry JSON for the Django seeder (stub)
│   ├── to_reel_script.py          # one-slug reel script in any language (stub)
│   ├── kdp.css                    # base 6×9 stylesheet (used by to_full_book.py)
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

- **No Artifacts.** This is a content repo, not a web app. Never use the Artifact tool to
  publish HTML pages. All output goes into the canonical source files or `build/output/`.

- **No cf-drop / Drop.** Do not upload anything to cf-drop or use the `drop-live-doc` skill
  in this repository. Documents, reports, and research findings stay as files in the repo or
  in the conversation — never pushed to an external hosting service.

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
  **Trusted research domains (in order):** en.wikipedia.org (overview + citation trail) →
  wisdomlib.org (primary Purana translations) → vedabase.io (Bhagavatam) →
  sacred-texts.com → gitapress.org (Hindi) → hinduism.stackexchange.com (tracing obscure refs).
  See WRITING_GUIDE.md §1b for full guidance on using each.
  **Research depth for a single katha improvement:** 4–5 source lookups maximum. Do NOT spawn
  multi-agent research workflows for single-katha edits — a focused sequential lookup is enough.
  Individual research tasks (date verification, new katha writing) can work independently.
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
| F | Remove forced chapter page-breaks (continuous flow) | **Done** — `h1 { page-break-before: auto }` in kdp.css; chapters flow continuously with no forced breaks. |

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

**Full 108-katha book — EPUB3 + PDF (primary build):**
```bash
/usr/bin/python3 build/to_full_book.py            # English (default)
/usr/bin/python3 build/to_full_book.py --lang hi  # Hindi
# → build/output/full-<lang>.epub   (EN ~542 KB, HI ~594 KB)
# → build/output/full-<lang>.pdf    (EN ~465 pp / 1.3 MB, HI ~393 pp / 1.2 MB)
# → build/output/full-<lang>.html   (intermediate HTML; inspect for styling issues)
```

**How `to_full_book.py` works:**

| Detail | Value |
|--------|-------|
| Slug lists | `SLUGS_108_EN` and `SLUGS_108_HI` — 108 curated entries each (different selections per language) |
| Chapter order | Entries with `date_2026 ≥ 2026-07-15` first (chronological), then Jan–Jul entries at the end |
| IAST stripping | All builds drop standalone IAST transliteration lines from Mantras sections |
| Section labels | Auto-localised: English "Significance/Vidhi/Mantras" → Hindi "महत्त्व/विधि/मंत्र" |
| Font | Noto Serif Devanagari embedded in both EPUB and PDF |
| PDF build | Two-pass: Pass 1 = chapters-only PDF (Arabic page numbers); Pass 2 = front-matter + index PDF (Roman); merged with pypdf |
| Page numbers | Index table shows exact page numbers resolved from PDF named destinations |
| Requires | PyYAML (in requirements.txt) + pypdf (`/usr/bin/pip3 install pypdf`) |

To add or remove entries from the book, edit `SLUGS_108_EN` / `SLUGS_108_HI` in the script.
Both lists must remain exactly 108 entries (asserted at load time).

**Sample edition (4 kathas — for quick CSS/layout checks):**
```bash
/usr/bin/python3 build/to_sample_book.py
# → build/output/sample-en.epub, sample-en.pdf, sample-en.html
```
To change which 4 kathas appear, edit `SAMPLE_SLUGS` at the top of the script.

### build/output/ — what each file is

```
build/output/
├── full-en.epub                    ← 108-katha EPUB3, English (to_full_book.py)
├── full-en.pdf                     ← 108-katha PDF, English (~465 pp, KDP-ready)
├── full-en.html                    ← intermediate HTML for chapters (inspect for styling)
├── full-en-chapters.html           ← Pass 1 HTML (chapters only, Arabic page nums)
├── full-en-chapters.pdf            ← Pass 1 PDF (chapters only; merged into full-en.pdf)
├── full-hi.epub / full-hi.pdf      ← same for Hindi (~393 pp)
├── chapters-pdf.css                ← auto-generated CSS for chapters pass; do NOT hand-edit
├── festival-vrat-companion-en.md   ← full 150-entry English manuscript (to_book_manuscript.py)
├── festival-vrat-companion-hi.md   ← full Hindi manuscript
├── sample-en.epub                  ← 4-katha EPUB3 sample (to_sample_book.py)
├── sample-en.pdf                   ← 4-katha PDF sample
├── sample-en.html                  ← intermediate HTML for sample PDF
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

All platforms are non-exclusive for paperbacks — publish everywhere in parallel.

### Channel split (decided June 2026)

**KDP does not distribute print books to Amazon.in** — Amazon.in is not a supported KDP print
marketplace. This means there is no conflict: each platform covers completely non-overlapping
channels for print.

| Format | Platform | Marketplaces |
|--------|----------|--------------|
| Kindle ebook | KDP (worldwide) | Amazon.com, Amazon.co.uk, Amazon.in Kindle store — one global Kindle listing |
| Paperback + Hardcover | KDP | Amazon.com, Amazon.co.uk, Amazon.de, Amazon.ca, Amazon.com.au — global Amazon **except** India |
| Paperback + Hardcover | Notion Press | Amazon.in + Flipkart + local Indian bookstores — India print exclusively |

No territory exclusion needed in KDP settings — KDP simply won't appear on Amazon.in for print.
Use different ISBNs per platform per format (two separate Amazon.in vs Amazon.com product pages,
exactly like every traditionally published book with separate Indian and US editions).

### Notion Press international pricing note
Notion Press requires a **minimum $22 USD** for international sales, yielding only ~$2–3 royalty —
worse than KDP at $12.99. Do **not** enable Notion Press international distribution; India-only
channels only (Amazon.in + Flipkart + local retail). All global print sales go through KDP.

### KDP pricing (US, 477 pages, 6×9, B&W — June 2026)
- Paperback print cost: $1.00 + (477 × $0.012) = **$6.72**
- Hardcover print cost: $6.80 + (477 × $0.012) = **$12.52**
- At $12.99 paperback: royalty = 0.60 × ($12.99 − $6.72) = **$3.76/copy**
- At $14.99 paperback: royalty = 0.60 × ($14.99 − $6.72) = **$4.96/copy**
- At $24.99 hardcover: royalty = 0.60 × ($24.99 − $12.52) = **$7.48/copy**
- Shipping: paid by buyer (free for Prime); does not affect author royalty calculation.

---

## date_2027 verification — monthly calendar approach

DrikPanchang publishes a "Hindu Festivals and Vrats" page for each calendar month, listing every
festival with its exact date. This is far more efficient than one-by-one lookups — fetch one month
page and verify every festival in that month simultaneously.

**URL pattern:**
```
https://www.drikpanchang.com/hindu-calendar/hindu-calendar-detail.html?year=2027&month=<N>
```
Replace `<N>` with the 1-based month number (1=January … 12=December).

**Process (per month batch):**
1. Open the URL for that month in DrikPanchang.
2. Scan the page for all festivals matching our entries.
3. Note the exact Gregorian dates shown.
4. Update each matching `meta.yaml` `date_2027` field; replace `TODO-VERIFY` with `YYYY-MM-DD`.
5. Add a `# verified DrikPanchang 2027` comment on the same line.

**Progress (as of June 2026):** ALL 150 entries complete.

| Month | Status | Notes |
|-------|--------|-------|
| Jan 2027 | ✅ done | lohri, makar-sankranti, shakambhari-purnima, sakat-chauth, magha-sankashti |
| Feb 2027 | ✅ done | mauni-amavasya, vasant-panchami, ratha-saptami, bhishma-ashtami, jaya-ekadashi, magha-purnima |
| Mar–Jun 2027 | ✅ done | All entries verified from DrikPanchang monthly festival pages |
| Jul 2027 | ✅ done | jaya-parvati-vrat, kokila-vrat, shravan-sankashti, shravan-somvar-vrat, solah-somvar-vrat, somvar-vrat, mangala-gauri-vrat |
| Aug–Dec 2027 | ✅ done | All entries verified from DrikPanchang + ProKerala panchang |

**Weekday vrats — special handling:**
Entries like `ravivar-vrat`, `mangalvar-vrat`, `budhvar-vrat`, `brihaspativar-vrat`, `shanivar-vrat`,
`shukravar-lakshmi`, `shukravar-santoshi`, `vaibhav-lakshmi-vrat` have `tithi: <Weekday>` in their
panchang block (not a lunar tithi — just the day of week). DrikPanchang does not publish annual date
lists for these generic weekday vratas. The canonical approach:
1. Fetch the ProKerala Hindu Calendar for the relevant Gregorian month:
   `https://www.prokerala.com/general/calendar/hinducalendar.php?year=<YYYY>&mon=<month-name>&sb=1`
2. Identify all occurrences of that weekday within the specified paksha (Shukla/Krishna).
3. Record the **first occurrence** as the `date_YYYY` field, verified from the ProKerala panchang.
4. Comment: `# verified ProKerala panchang YYYY — <Month> <Paksha> <tithi> — first <Weekday>`

Note: `date_2026` is fully verified for all 150 entries. `date_2027` is now also complete for all 150.

---

## First deliverable

The **Festival & Vrat Companion** book (KDP paperback-first) — each festival folder is one
chapter. All 150 entries are `ready_to_publish`. Next step: verify remaining `TODO-VERIFY` date
fields against DrikPanchang and flip entries to `published`.
