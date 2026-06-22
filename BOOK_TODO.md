# Book Go-Live TODO

Target: English first, then Hindi. 108 kathas, ordered from July 15, 2026.

---

## 1. Curate 108 kathas

Current corpus: 150 entries. Need to drop 42.

### Proposed drops (42 entries) — confirm before actioning

**Ekadashis — keep 10, drop 15** (too many; most readers observe 2–3 at most)
- [ ] Drop: `saphala-ekadashi`, `pausha-putrada-ekadashi`, `shattila-ekadashi`, `vijaya-ekadashi`, `amalaki-ekadashi`
- [ ] Drop: `varuthini-ekadashi`, `mohini-ekadashi`, `apara-ekadashi`, `yogini-ekadashi`, `kamika-ekadashi`
- [ ] Drop: `shravana-putrada-ekadashi`, `aja-ekadashi`, `parivartini-ekadashi`, `papankusha-ekadashi`, `rama-ekadashi`
- Keep: `nirjala`, `devshayani`, `devutthana`, `mokshada`, `papmochani`, `kamada`, `ekadashi-mahatmya`, `utpanna`, `jaya`, `indira`

**South-dominant festivals — drop 6**
- [ ] Drop: `onam`, `karthigai-deepam`, `varalakshmi-vrat`, `swarna-gowri-vrat`, `skanda-shashthi`, `vat-purnima`

**Weekday vratas — keep major 6, drop 6**
- [ ] Drop: `ravivar-vrat`, `mangalvar-vrat`, `budhvar-vrat`, `shanivar-vrat`, `shukravar-santoshi`, `vaibhav-lakshmi-vrat`
- Keep: `somvar-vrat`, `solah-somvar-vrat`, `shravan-somvar-vrat`, `mangala-gauri-vrat`, `brihaspativar-vrat`, `shukravar-lakshmi`

**Satyanarayan adhyayas — keep 2, drop 3**
- [ ] Drop: `satyanarayan-adhyaya-3`, `satyanarayan-adhyaya-4`, `satyanarayan-adhyaya-5`
- Keep: `masik-satyanarayan`, `satyanarayan-adhyaya-1`, `satyanarayan-adhyaya-2`

**Lesser-known / regional (North/West/East focus) — drop 12**
- [ ] Drop: `akshaya-navami`, `champa-shashthi`, `bhishma-ashtami`, `phulera-dooj`, `ratha-saptami`
- [ ] Drop: `shakambhari-purnima`, `pola`, `ramdevji-jayanti`, `hal-shashthi`, `sheetala-satam`
- [ ] Drop: `nirjala-gayatri-jayanti` (duplicate context with `nirjala-ekadashi` + `gayatri-jayanti`)
- [ ] Drop: `akshaya-tritiya-parashuram` (duplicate context with `akshaya-tritiya` + `parashurama-jayanti`)

**Confirm list with user before any file changes.**

---

## 2. Dates

- [ ] Remove `date_2026` bullet from Vidhi sections in all en.md files (currently last bullet: "**2026 Date:** ...")
- [ ] Remove same from hi.md, mr.md, gu.md
- [ ] Add `date_2028` field to all meta.yaml files (verify each against DrikPanchang — significant effort)
- [ ] Verify all remaining `TODO-VERIFY` date fields (2026 + 2027) against DrikPanchang → flip to `ready_to_publish` / `published`

---

## 3. Ordering (start from July 15, 2026)

- [ ] Build a sorted entry list: entries with `date_2026 >= 2026-07-15` first (chronological), then entries with `date_2026 < 2026-07-15` at the end (they recur in 2027)
- [ ] Update `to_full_book.py` ordering logic accordingly
- [ ] Confirm entries with 2025 dates (e.g. `saphala-ekadashi`) are either dropped (see curation) or placed at the end

---

## 4. Build system — create `to_full_book.py`

- [ ] Create `build/to_full_book.py` modelled on `to_sample_book.py` — self-contained, single command produces EPUB3 + PDF for all 108 entries
- [ ] Accepts `--lang` flag (default: `en`)
- [ ] Applies the July 15 ordering
- [ ] Generates the index (see §5)

---

## 5. Index with multi-year dates

Design: back-matter table with columns — **Festival | Page | 2026 | 2027 | 2028**

- [ ] Confirm `date_2027` is filled for all 108 entries (check for TODO-VERIFY)
- [ ] Add `date_2028` to meta.yaml for all 108 entries
- [ ] Build index generator in `to_full_book.py` — reads slug order, pulls dates from meta.yaml, outputs a table in back matter
- [ ] Page numbers: WeasyPrint does not support auto page-number injection in body tables; approach TBD (generate index after PDF, or use a two-pass build)

---

## 6. Book structure — front matter & back matter

### Front matter (write these)
- [ ] Half-title page
- [ ] Title page (title, subtitle, author/publisher)
- [ ] Copyright page (year, rights, scripture attribution, DrikPanchang credit)
- [ ] Dedication (optional — confirm with user)
- [ ] Invocation — already in sample, review
- [ ] Introduction — already in sample, expand if needed
- [ ] How to Use This Book — already in sample, review

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
