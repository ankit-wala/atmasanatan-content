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

- [ ] Determine final page count (needed for KDP spine width calculation)
- [ ] Design front cover, spine, back cover — in `atmasanatan-assets/` repo
- [ ] KDP cover spec: 6×9, 300 DPI, PDF or high-res JPG, spine width = page count × paper thickness

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

## Order of work (suggested)

1. Confirm 108 katha list (user review)
2. Remove date bullets from Vidhi (bulk script)
3. Add `date_2028` + verify dates (manual DrikPanchang work)
4. Build `to_full_book.py` with July 15 ordering
5. Write/finalise front + back matter
6. QR code (once URL received)
7. Generate final English PDF, proof-read
8. Cover design
9. Upload English → KDP + Notion Press + Pothi
10. Hindi build + upload
