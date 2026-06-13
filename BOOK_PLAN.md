# Book Plan — Festival & Vrat Companion (Book 1: 108 Kathas)

> Planning doc for the first ebook + paperback. Researched 2026-06-11/12 (calendar verified
> against DrikPanchang; publishing economics verified against KDP help pages). Re-verify the
> KDP figures at publish time — royalty rules changed June 2025 and Jan 2026.

## 1. Concept

**108 kathas, in calendar order, from Ashadha / Chaturmas (July 2026) to Diwali 2027**
(Oct 29, 2027) — the close of Vikram Samvat 2083. One katha per chapter; each chapter =
Katha + Significance + Vidhi (+ Observance/Mantras where relevant), built straight from
`kathas/` via `build/to_book_manuscript.py`.

The natural opener is **Devshayani Ekadashi / Chaturmas beginning (Jul 25, 2026)** — the
traditional start of the vrat season — preceded by Yogini Ekadashi (Jul 10), Rath Yatra
(Jul 16) and Guru Purnima (Jul 29) in the same opening month.

The window is ~16 months, so it contains **two** Shravans, two Navratris (plus Chaitra
Navratri), two Diwalis, and the full 24-ekadashi cycle. Repeated festivals share one katha —
see §3 for how repeats are handled.

> **Why not June 2026:** planning started June 12, 2026 — too late to cover June. Dropping
> June only loses the Adhik Maas trio (Purushottam Mahatmya, Parama Ekadashi, Vibhuvana
> Sankashti; next Adhik Maas is 2029). Everything else from June 2026 — Nirjala Ekadashi,
> Vat Savitri/Vat Purnima, Ganga Dussehra, Shani Jayanti — recurs in June 2027, inside the
> window, so those kathas are still covered.

## 2. Is 108 achievable? — Yes, comfortably

Verified inventory of **distinct, traditionally-sourced kathas in the window: ~132 firm,
~141 ceiling, ~109 conservative floor.** We pick the best 108 and hold the rest as reserves
(or mini-book exclusives). The floor is tighter than before (June's Adhik kathas dropped
out), which means a few popular folk-tier kathas (Santoshi Mata, Saptavar) likely stay in —
keep them with honest sourcing notes.

### Katha inventory by block (distinct kathas)

| Block | Count | Notes |
|---|---|---|
| Ekadashi cycle | 24 | All 24 named ekadashis occur in-window (both Putradas are different stories — King Suketuman vs King Mahijit). Padma/Brahma Vaivarta Purana — strongest block. |
| Sankashti Chaturthi | 12 | One per lunar month incl. Sakat Chauth (Magha). Vibhuvana (the 13th, Adhik-only) is out of window. Ganesha Purana tradition. |
| Navratri + Vijayadashami | 10 | 9 Durga forms (or Devi Mahatmya episodes — Markandeya Purana) + Shami/Aparajita. |
| Shravan block | 10 | 4 Shravan Somvar + Solah Somvar + Mangala Gauri + Hariyali Teej + Nag Panchami + Varalakshmi + Raksha Bandhan. |
| Bhadrapada block | 10 | Kajari Teej, Hal Shashthi, Janmashtami (Krishna janma — Bhagavata Sk. 10), Hartalika, Ganesh Chaturthi ×2 (janma + Syamantaka), Rishi Panchami, Radha Ashtami, Vamana, Anant Chaturdashi. |
| Saptavar + Santoshi Mata | 8 | Weekday vrat kathas; folk-tier sourcing — label honestly. |
| Pradosh | 7 | Core katha (Skanda Purana) + weekday variants (variants are thin — may collapse to 2–3). |
| Kartik block | 7 | Chhath, Skanda Shashthi, Gopashtami, Akshaya Navami, Tulsi Vivah, Dev Diwali, Kartik Mahatmya (expandable reserve). |
| Diwali cluster | 6 | Dhanteras, Narak Chaturdashi, Lakshmi Puja, Govardhan, Bhai Dooj, Govatsa Dwadashi. |
| Satyanarayan | 5 | Five adhyayas, tied to Purnimas. |
| Ashwin/Pitru block | 5 | Mahalaya/Karna, Jivitputrika, Kojagari Purnima, Karwa Chauth, Ahoi Ashtami. |
| Pausha–Magha | 5 | Makar Sankranti, Shakambhari, Vasant Panchami, Ratha Saptami, Bhishma Ashtami. |
| Vaishakha | 5 | Akshaya Tritiya, Parashurama, Sita Navami, Narasimha, Kurma Jayanti. |
| Margashirsha | 4 (+2 regional) | Kalabhairav, Vivah Panchami, Gita Jayanti, Dattatreya (+ Champa Shashthi MH, Karthigai Deepam TN). |
| Phalguna | 4 | Shivaratri ×2 (hunter katha + Lingodbhava), Holika/Prahlada, Sheetala Ashtami. |
| Jyeshtha (Jun 2027) | 3 | Shani Jayanti, Vat Savitri, Ganga Dussehra. |
| Chaitra | 3 | Gangaur, Ram Navami, Hanuman Jayanti. |
| Ashadha | 3 | Rath Yatra (Indradyumna), Guru Purnima (Vyasa), Jaya Parvati. |
| Misc | 1 | Somvati Amavasya. |

**Deprioritize / honest-label (folk, non-Puranic):** Santoshi Mata, Vaibhav Lakshmi, Saptavar
weekday kathas, Pradosh weekday variants, Kokila Vrat, Gudi Padwa. Keep popular ones with a
sourcing note; cut the rest first when trimming to 108.

## 3. Handling repeated festivals (the >1-year span)

The window contains two occurrences of many observances: both Shravans (with their Somvar
sets), Hariyali/Kajari/Hartalika Teej, Raksha Bandhan, Janmashtami, Ganesh Chaturthi, Sharad
Navratri, Karwa Chauth, Ahoi Ashtami, the Diwali cluster, and ~10 ekadashis (Yogini through
Rama). The katha itself never changes year to year, so:

1. **One katha = one chapter, placed at its first occurrence.** A katha is never printed
   twice — that would pad the book and break the "108 distinct kathas" promise.
2. **The second occurrence still appears in the calendar flow** as a short *observance
   entry*: date, tithi, a 2–4 line reminder of the vrat, and a cross-reference ("Katha: see
   Chapter 12, Shravan 2026"). The reader following the book week-by-week through VS 2083
   never hits a gap, but pays no page cost for duplication (~¼ page each, ~25–30 entries,
   ~8–10 pages total).
3. **Year-specific differences go in the observance entry, not the katha.** E.g. Shravan
   2027 has **5 Somvars** vs 4 in 2026; muhurat/tithi timings differ. These are panchang
   facts, not story changes.
4. **In the repo:** the canonical entry keeps a single katha in `<lang>.md`; `meta.yaml`
   carries *both* verified dates (today's schema has `date_2026` — extend the panchang block
   with `date_2027`, both DrikPanchang-verified). The book builder emits the full chapter at
   the first date and auto-generates the cross-reference entry at the second — repeats are a
   build concern, never hand-duplicated content. *(Requires a small builder + schema update —
   see TODOs.)*
5. **Bonus:** dual dates make the book usable across both years and give the app/reels two
   publishing moments per festival from the same source entry.

## 4. Publishing reality (this reshapes the pricing question)

Verified on official KDP help pages (fetched 2026-06-12):

1. **KDP cannot sell paperbacks on Amazon.in at all** — print-on-demand does not serve the
   India marketplace ([G201834340](https://kdp.amazon.com/en_US/help/topic/G201834340)).
2. **KDP does not print Hindi/Marathi/Gujarati paperbacks anywhere** — Indian languages are
   **ebook-only** on KDP ([G202124400](https://kdp.amazon.com/en_US/help/topic/G202124400)).
3. **Kindle ebooks on Amazon.in are fully supported** in en/hi/mr/gu. 70% royalty requires
   **KDP Select (90-day exclusivity) + list price ₹99–₹449**; otherwise 35%.
4. KDP English paperback works only on Amazon.com/.co.uk/EU — the **diaspora** channel.

So the channel mix is:

| Channel | Product | Price | Royalty/copy (est.) |
|---|---|---|---|
| KDP Kindle, Amazon.in | hi + en ebook, KDP Select | **₹249** (launch ₹199) | ~₹160–165 @70% |
| Indian POD (Pothi.com / Notion Press) → lists on Amazon.in + Flipkart | hi + en paperback, ~380 pp | **₹399–₹501** | TODO — run Pothi calculator |
| KDP paperback, Amazon.com | en, 6×9, ~360 pp | **$14.99** | ~$3.60 @60% (print ≈ $1 + $0.012/pp) |

### ₹251 vs ₹501 — answered

- **Ebook at ₹501 makes no sense:** above ₹449 you fall out of the 70% band and earn ₹175
  at 35% — barely more than ₹166 at ₹251 in the 70% band, while killing volume. Ebook ceiling
  is effectively **₹449**; sweet spot ₹199–₹299.
- **₹251 paperback is likely loss-making** for a ~380-page POD book in India; **₹501 is the
  paperback price**, positioned as a premium/gift edition. (Gita Press anchors the category at
  ₹70 for 416 pp — subsidized; we don't compete on price, we compete on structure: calendar-
  ordered, dated for VS 2083, vidhi + mantras + sourcing, multi-language brand.)
- Auspicious framing works: **ebook ₹251, paperback ₹501**.

### Page count estimate

~3 pp per katha at 6×9 (katha 1.5–2 + significance 0.5 + vidhi 0.5 + mantras 0.25) →
108 × 3 ≈ 324 pp + front matter, month intros, panchang tables ≈ **350–400 pp**
(Hindi runs ~10% longer). Well under KDP's 828-pp B&W cap.

## 5. Product ladder (small books vs full book)

Sell **both**: the 108 flagship at premium, plus themed minis as funnel/gifting products.
Club minis **by deity/theme**, not by calendar — the flagship already owns the calendar angle,
and deity-themed books match how devotees actually buy (Shiv-bhakt buys the Shiv book).

| Mini | Kathas | Contents | Ebook price |
|---|---|---|---|
| Ekadashi Mahatmya | 24 | Full named-ekadashi cycle (+ Adhik pair later, from reserves, for a 26 edition) | ₹149 |
| Shiv Vrat Kathayein | ~21 | Shivaratri ×2, Pradosh, Shravan Somvar, Solah Somvar, Mangala Gauri, Som. Amavasya | ₹99–129 |
| Devi Kathayein | ~21 | Navratri 9, Teej set, Vat Savitri, Karwa Chauth, Ahoi, Santoshi, Vasant Panchami | ₹99–129 |
| Shri Ganesh Sankashti | 12 | All 12 monthly Sankashti kathas (Vibhuvana joins in an Adhik-year update) | ₹99 |
| Diwali & Kartik Maas | ~13 | Diwali cluster 6 + Kartik block 7 — seasonal, time the launch to Oct | ₹99 |

Minis are pure remixes of the same `kathas/` corpus — zero extra content cost once the build
script can filter by tag/deity (add a `--tags`/`--slugs` flag to `to_book_manuscript.py`).
21 / 26 / 13 are naturally auspicious-adjacent counts; flagship keeps 108.

## 6. Production plan

1. **Locale priority:** `en` (canonical draft) + `hi` (primary market) for Book 1.
   mr/gu follow after launch.
2. **Sequencing target:** the real deadline is **Navratri–Diwali 2026 (Oct–Nov), the gifting
   peak.** Working backwards: manuscript freeze ~Sep 2026 → **~7 entries/week** from
   mid-June.
3. **Write in calendar order** (Yogini Ekadashi → Rath Yatra → Devshayani/Chaturmas opener →
   Guru Purnima → Shravan block → …) so partial progress is always publishable as a
   "Part 1" if needed.
4. Every entry: `meta.yaml` with sources + DrikPanchang-verified `date_2026`/`date_2027`
   (dates marked ~ in research = `TODO-VERIFY`), then `status: reviewed`.
5. Final manuscript → `docx`/`pdf` skill for KDP/Pothi interior formatting (6×9 trim).

### Open TODOs
- [ ] Run Pothi.com / Notion Press price calculators for a 380-pp B&W paperback → confirm
      ₹399 vs ₹501 royalty per copy; pick the India POD partner.
- [ ] Decide KDP Select (90-day Amazon exclusivity) — required for 70% on Amazon.in.
- [ ] Finalize the 108 list (cut ~24 from the ~132 inventory; cut thin folk-tier first).
- [ ] Extend `meta.yaml` panchang schema with `date_2027` (and update `CONTENT_FORMAT.md`)
      so repeated festivals carry both verified dates in one canonical entry.
- [ ] Teach `to_book_manuscript.py` to emit cross-reference *observance entries* at second
      occurrences (per §3) instead of duplicating chapters.
- [ ] Add tag/slug filtering to `to_book_manuscript.py` for the mini-book builds.
- [ ] Verify all ~ dates on DrikPanchang as entries are written (repo date rule).
