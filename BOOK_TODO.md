# Book Go-Live TODO

Target: English first, then Hindi. 108 kathas, ordered from July 15, 2026.

---

## ✅ 1. Curate 108 kathas — DONE

Current corpus: 150 entries. Each language edition selects its own 108, tuned to its audience.
The corpus stays at 150 — curation is a config/constant in the build script, not file deletions.

### Audience logic

| Edition | Primary reader | Region focus |
|---------|---------------|--------------|
| Hindi | Hindi-speaking devotee, all ages | UP, Rajasthan, MP, Bihar, Delhi, Uttarakhand |
| English | Young, pan-India / diaspora reader | Pan-India + global; South Indian diaspora significant |
| Gujarati (future) | Gujarati reader | Gujarat; keep sheetala-satam, vat-purnima, varalakshmi-vrat |

### Hindi 108 (finalised)

```
ahoi-ashtami          akshaya-tritiya        anant-chaturdashi
ashadha-sankashti     ashwin-sankashti       bhadrapada-sankashti
bhai-dooj             bhishma-ashtami        brihaspativar-vrat
buddha-purnima        chaitra-sankashti      chhath-puja
chitragupta-puja      dattatreya-jayanti     dev-diwali
devshayani-ekadashi   devutthana-ekadashi    dhanteras
diwali                ekadashi-mahatmya      ganesh-chaturthi-janma
ganesh-chaturthi-syamantaka  ganga-dussehra gangaur
gayatri-jayanti       gopashtami             govardhan-puja
gudi-padwa            guru-purnima           hal-shashthi
hanuman-jayanti       hartalika-teej         holika-dahan
indira-ekadashi       jagannath-rath-yatra   janmashtami
jaya-ekadashi         jaya-parvati-vrat      jivitputrika
jyeshtha-sankashti    kalabhairav-jayanti    kamada-ekadashi
kartik-sankashti      kartik-snan-mahatmya   karwa-chauth
lohri                 magha-purnima          magha-sankashti
maha-shivaratri       mahalaya-pitru-paksha  makar-sankranti
mangala-gauri-vrat    mangalvar-vrat         margashirsha-sankashti
masik-satyanarayan    masik-shivaratri       mauni-amavasya
mokshada-ekadashi     nag-panchami           narak-chaturdashi
narasimha-jayanti     navratri-brahmacharini navratri-chandraghanta
navratri-kalaratri    navratri-katyayani     navratri-kushmanda
navratri-mahagauri    navratri-shailputri    navratri-siddhidatri
navratri-skandamata   nirjala-ekadashi       papmochani-ekadashi
parashurama-jayanti   phalguna-sankashti     phulera-dooj
pradosh-vrat          radha-ashtami          raksha-bandhan
ram-navami            ramdevji-jayanti       ravivar-vrat
rishi-panchami        sakat-chauth           satyanarayan-adhyaya-1
satyanarayan-adhyaya-2  shakambhari-purnima  shani-jayanti
shani-pradosh         shanivar-vrat          sharad-purnima
sheetala-ashtami      sheetala-satam         shravan-sankashti
shravan-somvar-vrat   shukravar-lakshmi      sita-navami
solah-somvar-vrat     somvar-vrat            somvati-amavasya
tulsi-vivah           utpanna-ekadashi       vaishakha-sankashti
valmiki-jayanti       vamana-jayanti         vasant-panchami
vat-savitri-vrat      vijayadashami          vivah-panchami
```

**Hindi-only** (not in English): bhishma-ashtami, chitragupta-puja, gangaur, hal-shashthi, jivitputrika,
mangalvar-vrat, phulera-dooj, ramdevji-jayanti, ravivar-vrat, shakambhari-purnima,
sheetala-satam, vivah-panchami

**Hindi drops (42):** aja-ekadashi, akshaya-navami, akshaya-tritiya-parashuram, amalaki-ekadashi,
apara-ekadashi, bhaum-pradosh, budhvar-vrat, champa-shashthi, ganga-saptami, govatsa-dwadashi,
hariyali-amavasya, hariyali-teej, kajari-teej, kamika-ekadashi, karthigai-deepam, kokila-vrat,
mohini-ekadashi, nirjala-gayatri-jayanti, onam, papankusha-ekadashi, parivartini-ekadashi,
pausha-putrada-ekadashi, pola, rama-ekadashi, rangpanchami, ratha-saptami, saphala-ekadashi,
satyanarayan-adhyaya-3, satyanarayan-adhyaya-4, satyanarayan-adhyaya-5, shattila-ekadashi,
shravana-putrada-ekadashi, shukravar-santoshi, skanda-shashthi, som-pradosh, swarna-gowri-vrat,
vaibhav-lakshmi-vrat, varalakshmi-vrat, varuthini-ekadashi, vat-purnima, vijaya-ekadashi, yogini-ekadashi

---

### English 108 (finalised)

```
ahoi-ashtami          akshaya-navami         akshaya-tritiya
amalaki-ekadashi      anant-chaturdashi      ashadha-sankashti
ashwin-sankashti      bhadrapada-sankashti   bhai-dooj
brihaspativar-vrat    buddha-purnima         chaitra-sankashti
chhath-puja           dattatreya-jayanti     dev-diwali
devshayani-ekadashi   devutthana-ekadashi    dhanteras
diwali                ekadashi-mahatmya      ganesh-chaturthi-janma
ganesh-chaturthi-syamantaka  ganga-dussehra ganga-saptami
gayatri-jayanti       gopashtami             govardhan-puja
gudi-padwa            guru-purnima           hal-shashthi
hanuman-jayanti       hartalika-teej         holika-dahan
indira-ekadashi       jagannath-rath-yatra   janmashtami
jaya-ekadashi         jaya-parvati-vrat      jyeshtha-sankashti
kalabhairav-jayanti   kamada-ekadashi        kartik-sankashti
kartik-snan-mahatmya  karwa-chauth           kokila-vrat
lohri                 magha-purnima          magha-sankashti
maha-shivaratri       mahalaya-pitru-paksha  makar-sankranti
mangala-gauri-vrat    margashirsha-sankashti masik-satyanarayan
masik-shivaratri      mauni-amavasya         mokshada-ekadashi
nag-panchami          narak-chaturdashi      narasimha-jayanti
navratri-brahmacharini navratri-chandraghanta navratri-kalaratri
navratri-katyayani    navratri-kushmanda     navratri-mahagauri
navratri-shailputri   navratri-siddhidatri   navratri-skandamata
nirjala-ekadashi      onam                   papmochani-ekadashi
parashurama-jayanti   parivartini-ekadashi   phalguna-sankashti
pradosh-vrat          radha-ashtami          raksha-bandhan
ram-navami            rangpanchami           ratha-saptami
rishi-panchami        sakat-chauth           satyanarayan-adhyaya-1
satyanarayan-adhyaya-2  shani-jayanti        shani-pradosh
shanivar-vrat         sharad-purnima         sheetala-ashtami
shravan-sankashti     shravan-somvar-vrat    shukravar-lakshmi
sita-navami           skanda-shashthi        solah-somvar-vrat
somvar-vrat           somvati-amavasya       swarna-gowri-vrat
tulsi-vivah           utpanna-ekadashi       vaishakha-sankashti
valmiki-jayanti       vamana-jayanti         varalakshmi-vrat
vasant-panchami       vat-savitri-vrat       vijayadashami
```

**English-only** (not in Hindi): akshaya-navami, amalaki-ekadashi, ganga-saptami, kokila-vrat,
onam, parivartini-ekadashi, rangpanchami, ratha-saptami, skanda-shashthi, swarna-gowri-vrat,
varalakshmi-vrat

**English drops (42):** aja-ekadashi, akshaya-tritiya-parashuram, apara-ekadashi, bhaum-pradosh,
bhishma-ashtami, budhvar-vrat, champa-shashthi, chitragupta-puja, gangaur, govatsa-dwadashi,
hariyali-amavasya, hariyali-teej, jivitputrika, kajari-teej, kamika-ekadashi, karthigai-deepam,
mangalvar-vrat, mohini-ekadashi, nirjala-gayatri-jayanti, papankusha-ekadashi,
pausha-putrada-ekadashi, phulera-dooj, pola, rama-ekadashi, ramdevji-jayanti, ravivar-vrat,
saphala-ekadashi, satyanarayan-adhyaya-3, satyanarayan-adhyaya-4, satyanarayan-adhyaya-5,
shakambhari-purnima, shattila-ekadashi, sheetala-satam, shravana-putrada-ekadashi,
shukravar-santoshi, som-pradosh, vaibhav-lakshmi-vrat, varuthini-ekadashi, vat-purnima,
vijaya-ekadashi, vivah-panchami, yogini-ekadashi

---

### Common core (in both editions — 97 entries)

Everything not listed as Hindi-only or English-only above.

**Lists confirmed. Implement as `SLUGS_108_HI` / `SLUGS_108_EN` constants in `to_full_book.py`.**

---

## 2. Dates

- [x] Remove `date_2026` bullet from Vidhi sections — done for all 4 languages (559 files)
- [ ] Add `date_2028` field to all meta.yaml files (verify each against DrikPanchang — significant effort)
- [x] Verify all remaining `TODO-VERIFY` date fields (2026 + 2027) against DrikPanchang — complete for all 150 entries

---

## ✅ 3. Ordering (start from July 15, 2026) — DONE

- [x] `order_by_date()` in `to_full_book.py` reads `date_2026` from meta.yaml — entries ≥ Jul 15 first (chronological), then Jan–Jul wrap-around entries at end
- [x] Data-driven; no manual slug ordering hardcoded in the script
- [x] All 2025-dated entries excluded from both slug sets; last entry is `ashadha-sankashti` (Jul 3)

---

## ✅ 4. Build system — `to_full_book.py` — DONE

- [x] `build/to_full_book.py` exists — single command produces EPUB3 + PDF for all 108 entries
- [x] `--lang en|hi|mr|gu` selects `SLUGS_108_EN` or `SLUGS_108_HI`
- [x] Ordering driven by `order_by_date()` at build time
- [x] Index generated in back matter (§5)

---

## 5. Index with multi-year dates

Design: back-matter table with columns — **Festival | Page | 2026 | 2027 | 2028**

- [x] Confirm `date_2027` is filled for all 108 entries — complete for all 150 entries
- [ ] Add `date_2028` to meta.yaml for all 108 entries
- [x] Build index generator in `to_full_book.py` — single-column table: Festival | 2026 | 2027 | Page
- [x] Page numbers: two-pass build — chapters PDF first, pypdf extracts anchor→page, hardcoded into index HTML

---

## 6. Book structure — front matter & back matter

### Finalised decisions
- **Title:** 108 Vrat Katha (EN + HI editions — audience is young Hindi-speaking Indians, name works)
- **Subtitle:** "108 Sacred Observances — Katha, Significance, Vidhi and Mantras"
- **Section label for Vidhi:** Vidhi (kept as-is; not translated)
- **Half-title page:** removed — wasted page, not needed
- **Dedication:** skipped

### Front matter (write these)
- [x] Title page — "108 Vrat Katha" / subtitle / Atma Sanatan / 2026
- [x] Copyright page — rights, scripture attribution, DrikPanchang credit
- [x] Invocation — in `front_matter()`, reviewed
- [x] Introduction — all section references use correct terms (Katha, Significance, Vidhi, Mantras)
- [x] How to Use This Book — updated to say "Vidhi" throughout

### Back matter
- [ ] Full index table: Festival | Page | 2026 | 2027 | 2028 (see §5)
- [ ] About Atma Sanatan page
- [ ] App page: "Continue Your Practice" — QR code + App Store / Play Store links (QR URL TBD — user to provide)

---

## 7. QR code

- [ ] Get app URL from user (ideally a short redirect link, e.g. `atmasanatan.in/app`, so the QR never goes stale)
- [ ] Generate high-res QR code image (300 DPI, PNG) — `pip install qrcode[pil]`
- [ ] Embed in "Get the App" back matter page
- [ ] Test scan on printed/previewed PDF

---

## 8. Cover design

### Hindi wraparound cover — Notion Press ✅ DONE

- [x] **Front cover** — `build/build_cover.py` → `cover/front-cover-300dpi-maroon.png`
  - 1800×2700px, 300 DPI, near-black → deep maroon gradient (3-stop)
  - AI scene (Varaha) + gold ornate frame + NotoSerifDevanagari Black title (१०८ / व्रत कथाएँ)
  - Dynamic text sizing fills frame-bottom → 75px safe zone
- [x] **Back cover** — `build/build_full_cover.py --back` → `cover/back-cover-300dpi.png`
  - Same maroon gradient; Atma Sanatan logo (white-bg removed), Hindi description, 5 bullets
  - Atharva Veda verse + attribution + Hindi meaning; publisher block (आत्म सनातन + website)
  - Barcode zone reserved (bottom-right, x 1100–1725, y 2185–2625)
- [x] **Spine** — 280×2700px (0.934" for 420pp cream paper)
  - १०८ व्रत कथाएँ, NotoSerifDevanagari Black gold, CCW rotation; आत्म सनातन at bottom
- [x] **Full wraparound assembled** — `build/build_full_cover.py` → `cover/full-cover-300dpi.png` + `.pdf`
  - 3964×2784px (13.212"×9.278"), 42px bleed each side — matches Notion Press template exactly
- [x] Cover spec: 6×9, 300 DPI, PDF — Notion Press compliant

### Remaining cover tasks

- [ ] **Install img2pdf** (`/usr/bin/pip3 install img2pdf`) and rebuild PDF for lossless output before submission
- [ ] **Upload to Notion Press** and pass the online cover checker
- [ ] **KDP cover** — KDP uses a slightly different bleed template; rebuild or crop from full cover PNG for KDP submission (KDP accepts 300 DPI PNG/JPG as well as PDF)
- [ ] **English cover** — front cover title needs "108 Vrat Katha" in English; back cover in English — design separately when ready to publish English edition

### Trim size decision — 6×9 confirmed ✅

Tested 5×8 vs 6×9 on Notion Press (June 2026). **6×9 is cheaper for both editions.**

| Edition | 6×9 pages | 5×8 pages | Page increase |
|---------|-----------|-----------|---------------|
| English | ~478 pp   | ~654 pp   | +37%          |
| Hindi   | ~387 pp   | ~497 pp   | +28%          |

5×8 saves ~₹100 on the trim-size base price at Notion Press, but the 28–37% page increase
adds ~₹110–180 in extra per-page printing cost (at ~₹0.25/page rate differential), making
5×8 more expensive overall. Additionally, 5×8 at 500–650 pages requires a larger minimum
gutter (0.75") than 6×9 at under 500 pages (0.625") — the thicker spine costs more to bind.

---

## 9. Publishing setup

- [ ] KDP: account ready, ISBN decision (KDP free ISBN vs own), categories, keywords, pricing (70% royalty needs KDP Select for India)
- [ ] Notion Press: account, upload English interior PDF
- [ ] Pothi.com: account, upload English interior PDF
- [ ] Hindi build: run `to_full_book.py --lang hi`, review, upload separately

---

## 10. QA before upload

- [ ] Proof-read 10 random entries in final English PDF
- [ ] Verify no mantra is split across a page break
- [ ] Verify all section headings are never isolated from content
- [ ] Verify index dates are accurate for a sample of 5 entries
- [ ] Verify Gujarati files: `grep -rl $'[ঀ-৿]' kathas/festivals --include="gu.md"` (already clean, re-check after any bulk edits)
- [ ] Verify all mantras have Devanagari + IAST

---

## 11. Katha elaboration — all 150 entries ← CURRENT PRIORITY

**Scope:** All 150 hi.md Katha sections. Hindi first (feeds the book), then re-translate to en/mr/gu.

**Goal:** Expand each `## Katha` section from ~400–500 words to ~600–650 where content
genuinely supports it. Rules are in WRITING_GUIDE.md (elaboration rules section).

**What elaboration means:**
- Full emotional texture — the devotee's state of mind, the stakes, the turning moment
- Natural dialogue where the source supports it (no invented speech)
- Atmospheric setting details consistent with tradition
- The journey, not just the miracle — show the devotion that earned the grace
- No padding: if a story is fully told in 550 words, stop there; don't invent to reach a target

**Workflow — phases of 5 entries:**
- Each phase: elaborate 5 `hi.md` Katha sections → user reviews → approve/fix → next phase
- After every 20 entries (4 phases): rebuild Hindi PDF, spot-check, confirm page count
- All 108 Hindi-book kathas done → Hindi PDF finalised → **publish Hindi book**
- Remaining 42 kathas (English-only etc.) elaborated for EN translation pass
- Then re-translate all elaborated hi.md → en.md → mr.md → gu.md

**Phase tracker (30 phases × 5 = 150 total):**

| Phase | Slugs | Status |
|-------|-------|--------|
| 1  | jagannath-rath-yatra · guru-purnima · shravan-somvar-vrat · somvar-vrat · nag-panchami | ✅ done |
| 2  | devshayani-ekadashi · jaya-parvati-vrat · kokila-vrat · shravan-sankashti · ravivar-vrat | ✅ done |
| 3  | solah-somvar-vrat · mangala-gauri-vrat · shravana-putrada-ekadashi · som-pradosh · onam | ✅ done |
| 4  | varalakshmi-vrat · raksha-bandhan · satyanarayan-adhyaya-1 · masik-satyanarayan · kajari-teej | ✅ done |
| 5  | bhadrapada-sankashti · hal-shashthi · sheetala-satam · janmashtami · aja-ekadashi | ✅ done |
| 6  | bhaum-pradosh · pola · ramdevji-jayanti · hartalika-teej · ganesh-chaturthi-janma | ✅ done |
| 7  | ganesh-chaturthi-syamantaka · swarna-gowri-vrat · rishi-panchami · mangalvar-vrat · radha-ashtami | ✅ done |
| 8  | parivartini-ekadashi · vamana-jayanti · anant-chaturdashi · ashwin-sankashti · jivitputrika | ✅ done |
| 9  | indira-ekadashi · mahalaya-pitru-paksha · navratri-shailputri · navratri-brahmacharini · navratri-chandraghanta | ✅ done |
| 10 | navratri-kushmanda · budhvar-vrat · navratri-skandamata · navratri-katyayani · shukravar-santoshi | ✅ done |
| 11 | shukravar-lakshmi · vaibhav-lakshmi-vrat · navratri-kalaratri · navratri-mahagauri · navratri-siddhidatri | ✅ done |
| 12 | vijayadashami · papankusha-ekadashi · sharad-purnima · valmiki-jayanti · kartik-snan-mahatmya | ✅ done |
| 13 | karwa-chauth · kartik-sankashti · ahoi-ashtami · rama-ekadashi · govatsa-dwadashi | ✅ done |
| 14 | dhanteras · narak-chaturdashi · diwali · govardhan-puja · bhai-dooj | ✅ done |
| 15 | chitragupta-puja · brihaspativar-vrat · chhath-puja · skanda-shashthi · gopashtami | ✅ done |
| 16 | akshaya-navami · devutthana-ekadashi · tulsi-vivah · dev-diwali · satyanarayan-adhyaya-2 | ✅ done |
| 17 | karthigai-deepam · margashirsha-sankashti · shanivar-vrat · kalabhairav-jayanti · utpanna-ekadashi | ✅ done |
| 18 | shani-pradosh · vivah-panchami · champa-shashthi · mokshada-ekadashi · ekadashi-mahatmya | ✅ done |
| 19 | dattatreya-jayanti · satyanarayan-adhyaya-3 · saphala-ekadashi · pausha-putrada-ekadashi · shakambhari-purnima | ✅ done |
| 20 | sakat-chauth · magha-sankashti · lohri · makar-sankranti · shattila-ekadashi | ✅ done |
| 21 | mauni-amavasya · vasant-panchami · ratha-saptami · bhishma-ashtami · jaya-ekadashi | ✅ done |
| 22 | magha-purnima · satyanarayan-adhyaya-4 · phalguna-sankashti · vijaya-ekadashi · pradosh-vrat | ✅ done |
| 23 | maha-shivaratri · phulera-dooj · amalaki-ekadashi · holika-dahan · chaitra-sankashti | ✅ done |
| 24 | rangpanchami · sheetala-ashtami · papmochani-ekadashi · gudi-padwa · gangaur | ✅ done |
| 25 | ram-navami · kamada-ekadashi · hanuman-jayanti · vaishakha-sankashti · varuthini-ekadashi | ✅ done |
| 26 | akshaya-tritiya · parashurama-jayanti · akshaya-tritiya-parashuram · ganga-saptami · sita-navami | ✅ done |
| 27 | mohini-ekadashi · narasimha-jayanti · buddha-purnima · satyanarayan-adhyaya-5 · jyeshtha-sankashti | ✅ done |
| 28 | apara-ekadashi · vat-savitri-vrat · shani-jayanti · ganga-dussehra · somvati-amavasya | ✅ done |
| 29 | nirjala-ekadashi · gayatri-jayanti · nirjala-gayatri-jayanti · vat-purnima · ashadha-sankashti | ✅ done |
| 30 | yogini-ekadashi · kamika-ekadashi · masik-shivaratri · hariyali-amavasya · hariyali-teej | ✅ done |

**Page budget:** Hindi 390pp → target ≤ 500pp after all 150 elaborated.

---

## 12. English book length reduction (parked)

- [ ] Try **10.5pt body font, line-height 1.35** (currently 11pt / 1.4)
- [ ] Estimated saving: ~20–25 pages (454pp → ~430pp)
- [ ] Decision: revisit after Hindi elaboration is done and EN is re-translated from elaborated HI

---

---

## 13. Final upload checklist — Hindi edition

Complete these in order before submitting to Notion Press or KDP.

### A. Interior PDF — curation & review

- [ ] **Rebuild interior PDF** — `to_full_book.py --lang hi` — confirm no build errors
- [ ] **Page count check** — expect 390–430pp; if over 450, revisit font/spacing
- [ ] **Front matter review** (open PDF, check each page visually):
  - [ ] Title page: correct title, subtitle, publisher ("Atma Sanatan"), year (2026)
  - [ ] Copyright page: rights statement, scripture attribution, DrikPanchang credit
  - [ ] Invocation page: Devanagari renders cleanly, no font fallback boxes
  - [ ] Introduction: no broken references ("Observance" should not appear — should say "Vidhi")
  - [ ] How to Use: references match actual section names (Katha / Significance / Vidhi / Mantras)
- [ ] **Random sample — 10 kathas** (open PDF, spot-check):
  - [ ] No mantra split across a page break
  - [ ] No section heading isolated at bottom of page (widow heading)
  - [ ] Bold labels in Vidhi section render correctly
  - [ ] Devanagari conjuncts render without fallback boxes (especially ज्ञ, क्ष, त्र, श्र)
  - [ ] IAST lines have been stripped (should not appear in any chapter)
- [ ] **Index check:**
  - [ ] Back-matter index table present with Festival | 2026 | 2027 | Page columns
  - [ ] Spot-check 5 entries: page numbers match actual chapter pages
  - [ ] Spot-check 5 dates: 2026 and 2027 dates are correct vs DrikPanchang
- [ ] **Back matter:**
  - [ ] About Atma Sanatan page present
  - [ ] App page ("Continue Your Practice") present — QR code embedded (§7 must be done first)

### B. Cover PDF — production quality

- [ ] **Install img2pdf** (one-time):
  ```bash
  /usr/bin/pip3 install img2pdf
  ```
- [ ] **Rebuild full cover** — `build/build_full_cover.py` — confirm "img2pdf — lossless" in output (not "PIL fallback")
- [ ] **Verify cover PDF dimensions**: 13.212" × 9.278" at 300 DPI — open in Preview → Tools → Show Inspector → confirm
- [ ] **Visual check on cover PDF**: back cover text legible, no clipping at bleed edges, spine text readable

### C. Notion Press upload (India print — Amazon.in + Flipkart)

- [ ] Log in / create Notion Press account
- [ ] Start new book → select "Black & White, Cream paper, 6×9"
- [ ] Upload interior PDF → wait for processing → confirm page count matches
- [ ] Upload full wraparound cover PDF (`full-cover-300dpi.pdf`)
- [ ] Pass Notion Press cover checker (flag any safe-zone violations)
- [ ] Set title, author, description (use Hindi back cover description)
- [ ] Set price (INR) — research competitive pricing for devotional books (~₹299–399)
- [ ] Distribution: Amazon.in + Flipkart + local retail only (do NOT enable international — see CLAUDE.md)
- [ ] Order a physical proof copy before wide release

### D. KDP upload (global print + Kindle ebook)

- [ ] **Paperback cover** — KDP uses its own bleed template; regenerate or use `full-cover-300dpi.png` and let KDP's cover uploader crop; verify in KDP previewer
- [ ] Upload interior PDF → KDP online previewer → confirm rendering
- [ ] Set publisher name: **"Atma Sanatan"** (text field, no registration required)
- [ ] Set categories: Religion & Spirituality → Hinduism
- [ ] Set keywords (7): व्रत कथा, festival vrat, Hindu fasting, puja vidhi, vrat katha hindi, festival stories, Hindu observances
- [ ] Pricing: $12.99 paperback (royalty ~$3.76 at 477pp) — or $14.99 for ~$4.96
- [ ] **Kindle ebook**: upload `full-hi.epub` → set price (₹199–299 INR / $4.99 USD)
- [ ] Preview ebook on KDP Kindle previewer — verify Devanagari, images, ToC
- [ ] Submit; allow 24–72 hrs for review

---

## Order of work

1. ~~Confirm 108 katha list~~ ✅
2. ~~Remove date bullets from Vidhi~~ ✅
3. ~~Build `to_full_book.py` with July 15 ordering~~ ✅
4. ~~Hindi katha elaboration — all 30 phases of 5 (§11)~~ ✅
5. ~~Hindi cover design — front + spine + back + full PDF (§8)~~ ✅
6. **Finalise Hindi front + back matter (§6)** ← NOW
   - About Atma Sanatan page
   - App page ("Continue Your Practice") with QR code
7. QR code for Hindi (§7) — get app URL, generate PNG, embed in §6 app page
8. Install img2pdf + upload cover PDF to Notion Press; pass cover checker
9. **Publish Hindi book** → KDP (ebook) + Notion Press (India print) + KDP global print
10. — (pause English until Hindi is live) —
11. Re-translate elaborated hi.md → en.md → mr.md → gu.md
12. English font reduction to 10.5pt (§12)
13. Finalise English front + back matter
14. English cover design (§8 — English edition)
15. Publish English book
16. Add `date_2028` to all entries (lower priority — next year)
