# Writing Guide — How to Write a Katha Entry

This is the step-by-step procedure for taking any stub in `kathas/festivals/<slug>/`
from `status: draft` to `status: reviewed`. Follow every phase in order.
One person or one AI session can complete a single entry in ~30–45 minutes once familiar.

---

## Overview: the five phases

```
1. RESEARCH     Find the source text. Understand the story fully.
2. VERIFY       Confirm the date on DrikPanchang. Fill meta.yaml.
3. WRITE        Draft en.md — prose, vidhi, mantras.
4. CHECK        Self-review against the quality checklist.
5. PREVIEW      Build the manuscript. Confirm it renders correctly.
```

Set `status: reviewed` only after all five phases pass.

---

## Phase 1 — Research

### 1a. Read the stub first
Open `kathas/festivals/<slug>/meta.yaml`. The `scripture_ref` field tells you exactly
where to go:
```yaml
scripture_ref: "Padma Purana, Uttara Khanda — Sridhara katha"
```
That is your primary source. Go there before writing a single word.

### 1b. Find the source text

**Free online (English):**
- [wisdomlib.org](https://www.wisdomlib.org/) — the best single resource. Has nearly all 18
  Maha Puranas translated. Search by Purana name + chapter.
- [sacred-texts.com](https://sacred-texts.com/hin/) — older translations, good for Ramayana
  and Mahabharata.
- [valmiki.iitk.ac.in](https://valmiki.iitk.ac.in/) — Valmiki Ramayana, Sanskrit + English,
  searchable by kanda and sarga.
- [mbh.iitk.ac.in](https://www.sacred-texts.com/hin/maha/index.htm) — Mahabharata.

**Hindi reference (cross-check):**
- Gita Press editions: [gitapress.org](https://www.gitapress.org/) — most authoritative for
  vrat kathas. If a Gita Press edition says it differently, note the difference; their
  editorial tradition is 80+ years old and widely trusted by devotees.
- Their *Vrat Parichay* (code 610) covers most vrat kathas. Specific festival booklets
  (Satyanarayan, Ekadashi sets etc.) are available individually.

**Sanskrit (for shloka verification):**
- [GRETIL](https://gretil.sub.uni-goettingen.de/) — Göttingen Register of Electronic Texts
  in Indian Languages. Sanskrit originals, useful for mantra accuracy.

### 1c. What to extract from the source

Before opening `en.md`, note down:
1. **The full story arc** — characters, conflict, resolution, miracle/boon.
2. **Phala-shruti** — the promised benefit stated at the end of the katha. Every traditional
   katha ends with one. Include it faithfully; do not invent or suppress it.
3. **Vidhi steps** — what the text actually prescribes for the puja/vrat. If the source is
   thin on vidhi, cross-check a Gita Press booklet.
4. **Key mantras** — what shloka is recited, which deity, in what context.
5. **Any variant versions** — some festivals have regional variations. Note the primary
   (Puranic) version; you can mention variants briefly in Significance.

### 1d. Folk-tier kathas — special handling

If `sources:` in meta.yaml says "folk tradition" or "oral tradition" (Santoshi Mata,
weekday vrats, Ahoi Ashtami, etc.), this means no single classical Puranic source exists.
You MUST include the following note at the start of the **Significance** section:

> *This vrat katha belongs to the living oral tradition of Hindu devotion. It does not trace
> to a specific Purana verse but has been observed by countless devotees across generations.
> Its spiritual value rests in the faith and intention of the devotee.*

Do not skip this note for folk-tier kathas. It is honest and it protects the corpus.

---

## Phase 2 — Verify dates and fill meta.yaml

### 2a. DrikPanchang verification (mandatory before reviewed)

Go to [drikpanchang.com](https://www.drikpanchang.com/) and find the exact date for
**both 2026 and 2027**:

| Festival type | Where to look on DrikPanchang |
|---|---|
| Named festival (Diwali, Janmashtami…) | Search the festival name directly |
| Ekadashi | drikpanchang.com/vrats/ekadashidates.html?year=2026 |
| Sankashti Chaturthi | drikpanchang.com/chaturthi/sankashti-chaturthi-dates.html |
| Purnima, Amavasya | drikpanchang.com/purnima / amavasya pages |
| Solar dates (Makar Sankranti) | drikpanchang.com/makar-sankranti |

Note the date in **YYYY-MM-DD** format and any important muhurat/timing.

### 2b. Update meta.yaml

Fill in every `TODO-VERIFY` field:
```yaml
panchang:
  month: Kartik
  paksha: Krishna
  tithi: Amavasya
  date_2026: 2026-11-08    # ← verified against DrikPanchang
  date_2027: 2027-10-29    # ← verified against DrikPanchang
```

Also confirm or correct:
- `deity:` list — matches the actual story you found
- `sources:` — add/correct the specific Purana + khanda + chapter
- `scripture_ref:` — most precise reference: `"Bhagavata Purana, Skandha 10, Ch. 1-3"`
- `region:` — correct if the festival is regional, not pan-india

Do **not** set `status: reviewed` yet — that happens after the prose passes Phase 4.

---

## Phase 3 — Write the primary language file

**Source determines which language you write first:**

- **Hindi source (Gita Press, Sanskrit primary + Hindi edition):** Write `hi.md` first. This covers almost all entries — vrat kathas, Ekadashi kathas, and festival kathas where a Gita Press Hindi edition exists.
- **Sanskrit-only source with no Hindi edition:** Write `en.md` first from the Sanskrit/English translation, then translate to `hi.md`.

In practice, Gita Press Hindi editions exist for nearly every entry in this corpus, so **the default is: write `hi.md` first.**

**Translation order after the primary language is locked:**
`hi.md` (primary) → `en.md` → `mr.md` → `gu.md`

For `mr.md` and `gu.md`, translate from `hi.md`, not from `en.md`. For `en.md`, translate from `hi.md` when a Hindi source exists — do not work from an intermediate translation.

### 3a. Front matter

```yaml
---
slug: janmashtami
lang: en
title: "Janmashtami — The Birth of Shri Krishna"
subtitle: "The night Devaki's eighth child changed the world"
summary: "Janmashtami celebrates the birth of Lord Krishna in Kansa's prison — the divine child who would redeem the world."
reel_hook: "Why did a tyrant king fear his own nephew before the child was even born?"
---
```

- **title**: `"[Festival Name] — [one clear tagline]"`. Not clever; clear.
- **subtitle**: one evocative line. Poetic, not informational.
- **summary**: 1–2 sentences, present tense. Used in the book blurb and app listing.
- **reel_hook**: a question that creates suspense or curiosity. This is the opening of a
  30-second Instagram reel. Make it scroll-stopping.

### 3b. `## Katha` — the story (300–700 words)

This is the most important section. Write it as **narrative prose** — not bullet points,
not a summary, not a Wikipedia article. Tell the story.

**Tone:** Devotional but not sycophantic. Respectful. Present-tense for dramatic moments,
past-tense for framing. Active voice throughout.

**Language — the single most important rule for this project:**
Write in the simplest, most everyday words possible. This corpus is for everyone —
a farmer in Bihar, a housewife in Surat, a software engineer in Bengaluru. If a simpler
word exists, always use it. Never use a complex or literary word to sound elevated.

Examples of what to do and what to avoid:

| Avoid | Use instead |
|---|---|
| The deity manifested in resplendent form | The god appeared before them, radiant |
| Immersed in deep penance and austerity | He prayed and fasted without stopping |
| Bestowed bountiful blessings | Blessed him with everything he asked for |
| The celestial realms were illuminated | The heavens glowed with light |
| Propitiate the deity | Please the god / worship the god |
| Commenced the ritualistic observance | Began the puja |

This applies equally in **Hindi, Marathi, and Gujarati** — use the common spoken form of
each language, not the Sanskritised literary register. In Hindi: prefer the word a person
would use in daily conversation over a tatsama (pure Sanskrit-origin) equivalent.

**Structure that works:**
1. Open with the context — who is the central figure, what world do they live in?
2. The problem / conflict / test — what is at stake?
3. The turning point — the divine intervention, the devotion, the miracle.
4. The resolution — what changed? What was granted?
5. The phala-shruti — end with the promised fruit of observing this vrat/festival,
   woven naturally into the closing: *"Whoever observes this vrat with sincerity…"*

**Original composition rule — this is non-negotiable:**
The source text (Gita Press Hindi edition, Bhagavata Purana, etc.) is used for **facts only** —
the story arc, character names, sequence of events, numbers, the phala-shruti. Every sentence of
prose you write must be composed fresh in your own words. Do not translate sentences from the
source; do not copy phrases from any modern publication. Modern Gita Press editions are copyrighted.

You may add small atmospheric details that serve the narrative and are consistent with the
tradition — the darkness of the prison, the sound of rain, a character's expression. These are
a storyteller's craft, not invention. What you must never add is new plot, new characters, or
facts not found in any traditional version.

Think of it like this: you have read the story from the source. Now put the book aside and tell
it in your own voice. A kathakaar at a temple doesn't read from Gita Press line by line — they
know the story and they tell it. That is what we are doing.

**Hard rules:**
- Do NOT invent dialogue, characters, or events not in the source.
- Do NOT blend two different source versions into one without noting it.
- Do NOT add modern framing, psychology, or social commentary.
- Do NOT add the word "auspicious" more than once per entry (it is overused in this genre).
- Sanskrit deity names use the familiar popular spelling (Krishna, not Kṛṣṇa) throughout
  the Katha prose. IAST is reserved for the Mantras section only.

### 3c. `## Significance` (100–200 words)

Answer: *why does this matter?*
- The spiritual/theological meaning of the festival.
- Astronomical or panchang significance if relevant (e.g., Makar Sankranti = Uttarayan).
- Cultural/regional significance — who observes it, how widely.
- If this is a multi-regional festival with variations, note the primary tradition.
- For folk-tier kathas: add the sourcing note here (see Phase 1d).

### 3d. `## Vidhi` (100–250 words)

Step-by-step puja or vrat procedure. Use a numbered list.

```markdown
## Vidhi

1. Wake before sunrise. Take a bath and wear clean clothes.
2. Set up the puja thali with…
3. Light a diya with ghee…
4. Offer flowers, akshat (unbroken rice), and roli…
5. Recite the katha (this chapter).
6. Perform aarti.
7. Distribute prasad.
```

Source this from the text or from a Gita Press vidhi guide for the festival.
If the source provides no specific vidhi, write the general tradition for that deity/festival
and note it as "traditional practice."

### 3e. `## Observance` (vrats only, 80–150 words)

Required for any entry with `type: vrat`. Cover:
- Fasting rules (nirjal / water only / fruit / single meal — specify exactly)
- Who observes it (married women, men, all devotees)
- Timing (from sunrise to moonrise, from sunrise to sunset, etc.)
- Parana — how and when to break the fast
- What to avoid (grains, certain foods, specific actions)

If it is a festival (`type: festival`) with no fasting element, this section can be omitted.

### 3f. `## Mantras` (1–3 mantras)

Format for each mantra:

```markdown
### [Mantra name or deity]

**Sanskrit (Devanagari):**
ॐ नमः शिवाय

**Transliteration:**
Oṃ Namaḥ Śivāya

**Meaning:** I bow to Shiva — the auspicious one within all beings.
```

Rules for mantras:
- **Always include Devanagari.** Never transliteration-only.
- Use IAST transliteration (ā, ī, ū, ṃ, ś, ṣ, ṭ, ḍ, ṇ) — not phonetic approximations.
- Verify shloka accuracy against at least two sources before publishing.
- Keep the meaning to one line — devotees know the prayer; they need a quick anchor, not a commentary.
- For complex ekadashi/festival shlokas, 1 mantra is sufficient. Satyanarayan, Navratri devis,
  Shivaratri can have 2–3.

### Sanskrit shlokas inside the Katha prose — very strict rule

Sanskrit shlokas may appear **inside the Katha narrative only in very rare cases** — when
a specific verse is so central to the story that quoting it directly would genuinely move the
reader in a way plain prose cannot. The test is: *would omitting this verse make the story feel
incomplete?* If the answer is "no" or "probably not," do not include it.

**When you do include a verse inside the Katha:**
- Use it as a brief pause, not a performance of scholarship.
- Give the Devanagari in italics, immediately followed by a plain-English (or plain-Hindi)
  translation in parentheses or the next sentence.
- Maximum one such verse per katha. Two is already too many.
- Never leave a shloka without explanation — a reader who does not know Sanskrit must be
  able to continue reading without confusion.

**Example of the right way:**

> Devaki held her newborn and whispered the only words that came:
> *ॐ नमो भगवते वासुदेवाय* — "I bow to you, Lord Vasudeva."
> In that moment, the prison cell felt like the holiest place on earth.

**Example of the wrong way:**

> As described in the Bhagavata Purana:
> *नमः पङ्कजनाभाय नमः पङ्कजमालिने।*
> *नमः पङ्कजनेत्राय नमस्ते पङ्कजाङ्घ्रये॥*
> This shloka shows the glory of the Lord.

The wrong example uses Sanskrit to show off the source, not to serve the story. Avoid it.
The Mantras section already handles shlokas formally — the Katha section is for storytelling.

---

## Phase 4 — Quality checklist

Go through this checklist before setting `status: reviewed`. Every item must pass.

### Content accuracy
- [ ] Every event and character in the Katha traces to the `sources:` list
- [ ] All numbers and sequences are verified against the source text — children born/killed, days fasted, years of exile, order of events, names of siblings. These are the easiest facts to get wrong from memory and the easiest for a reader to spot.
- [ ] No invented dialogue, characters, or miracles
- [ ] Phala-shruti is included faithfully
- [ ] Folk-tier kathas have the sourcing note in Significance

### Dates and facts
- [ ] `date_2026` in meta.yaml is a real YYYY-MM-DD, verified on DrikPanchang
- [ ] `date_2027` same
- [ ] `deity:` list in meta.yaml matches the story
- [ ] `scripture_ref:` is specific (Purana + khanda + chapter, not just "Purana name")

### Prose quality
- [ ] Katha reads as a story, not a summary or bullet list
- [ ] Active voice, present-tense for dramatic moments
- [ ] No Wikipedia-style hedging ("it is believed that", "according to legend")
  — write as a devotional author, not a journalist. The source is cited in meta.yaml.
- [ ] No fabricated Sanskrit quotes or invented shloka references
- [ ] Devanagari in Mantras section is correct (verify against GRETIL or wisdomlib)
- [ ] IAST transliteration is used, not casual phonetic spelling
- [ ] Vocabulary is simple and everyday — no literary or archaic words anywhere
- [ ] Any Sanskrit shloka inside the Katha prose is immediately followed by its plain meaning

### For translated files (hi.md, mr.md, gu.md) — additional checks
- [ ] Deities, Rishis, and Elders use respectful pronoun forms (वे/उन्होंने in Hindi;
  त्यांनी in Marathi; તેઓ in Gujarati)
- [ ] Ordinary characters and villains use non-respectful forms (वह/उसने; त्याने; તેણે)
- [ ] No character's respect level changes inconsistently within one paragraph
- [ ] Translation was done from the correct source language (Hindi from Gita Press / Sanskrit,
  not from en.md where a primary Hindi source exists)
- [ ] Translation was done block by block, not sentence by sentence
- [ ] Translated text reads naturally when read aloud — not like a literal translation

### Structure
- [ ] All three required sections present: `## Katha`, `## Significance`, `## Vidhi`
- [ ] `## Observance` present for vrats (`type: vrat`)
- [ ] `## Mantras` present (at minimum one mantra for any entry)
- [ ] Section headings are exactly as specified — no renaming

### meta.yaml
- [ ] `status:` is still `draft` (you'll change it to `reviewed` at the end)
- [ ] No `TODO` strings remaining anywhere in the file

---

## Phase 5 — Build preview

Run the manuscript builder and visually check the output:

```bash
# Single entry preview (add --include-drafts to see draft-status entries)
python3 build/to_book_manuscript.py --lang en --include-drafts

# Check the output
open build/output/festival-vrat-companion-en.md
```

Verify:
- The entry appears in the correct calendar position (sorted by `order`)
- All five sections render cleanly with correct headings
- The Devanagari text is not garbled
- No raw `TODO` strings appear in the output

If the build shows warnings about unverified dates, those entries will not appear in the
default (non-draft) build — that is expected and correct.

---

## Phase 5 — Set status: reviewed

Once the checklist passes and the build looks clean:

```yaml
# in meta.yaml
status: reviewed
```

**Do not set `status: published` yet.** Published means all four language files (en, hi, mr, gu)
are complete. Reviewed means the primary language draft is done and verified.

---

## Phase 6 — Independent Review Agent

After the primary language file (hi.md) passes the Phase 4 checklist and status is set to
`reviewed`, run an independent review agent before moving to translations.

**Why this exists:** The writing agent has full context of the research session — it can
unconsciously fill in gaps with plausible-sounding details, miss pronoun-hierarchy errors it
introduced, or let a sequence mistake slip through because it "knows" what comes next. An
independent agent reads the entry cold, with no memory of the writing session, and is far more
likely to catch errors.

**How to run it:**

Spawn a fresh agent (via the Agent tool, or a new Claude session) with this prompt:

```
You are a quality-reviewer for a devotional Hindu katha corpus. Read the following entry cold
and check for every item in the list below. Report each issue with the section name and a
one-sentence description of the problem. If everything passes, say "PASS — no issues found."

Entry to review:
  meta.yaml:  [paste full meta.yaml]
  hi.md:      [paste full hi.md]
  en.md:      [paste full en.md, if written]

Checklist — flag any of the following:

FACTS
□ Are the number of children born and killed internally consistent?
□ Are all named characters (parents, siblings, disciples, kings) consistent within the story?
□ Does the sequence of events match standard Puranic accounts?
□ Are no miracles, dialogues, or plot points invented beyond what the source supports?
□ Is the scripture_ref in meta.yaml specific enough (skandha / chapter, not just "Purana")?
□ Are date_2026 and date_2027 plausible for the stated tithi and month?

LANGUAGE — HINDI
□ Are Deities, Rishis, and revered elders using वे/उन्होंने/उनके throughout?
□ Are villains and ordinary mortals using वह/उसने/उसके/था throughout?
□ Does any villain accidentally receive respectful verb forms (आए, चले गए, बोले)?
□ Does any deity accidentally receive disrespectful verb forms (आया, था)?

STRUCTURE
□ Are all required sections present: Katha, Significance, Vidhi, Observance (if vrat), Mantras (if applicable)?
□ Does the Katha section end with a phala-shruti (merit statement)?
□ Are Devanagari mantras intact and not paraphrased?
□ Does the Observance section cover paran timing and special rules for this vrat?

TONE
□ Is the prose original composition (not copied from Gita Press or any published source)?
□ Is the register devotional but not artificially ornate — a kathakaar's voice, not a textbook?
```

**Pass criteria:** The review agent must report `PASS — no issues found` (or only trivial
wording suggestions) before the entry proceeds to translation. Any factual, pronoun-hierarchy,
or structural issue must be fixed and re-reviewed.

**Record the outcome:** Add a one-line note to the entry's meta.yaml comment or PROGRESS.md:
```
# Phase 6 review: PASS — <date>
```

---

## Phase 7 — Translation Review Agent

After `en.md`, `mr.md`, and `gu.md` are written, run an independent review agent that reads
all three translations against `hi.md` and **fixes issues inline** (not just reports them).

**Why this exists:** A translation agent works entry-by-entry in a single pass. It can silently
drop a paragraph, introduce complex vocabulary, apply pronoun register incorrectly, or produce
prose that sounds like translated Hindi rather than natural target-language prose. An independent
agent reads all three translations cold against the Hindi source and catches what the translation
agent missed.

**How to run it:**

Spawn a fresh agent (via the Agent tool) with the following prompt for each entry:

```
You are a translation quality reviewer for a devotional Hindu katha corpus.
Your job is to read hi.md (source) and then check en.md, mr.md, and gu.md against it.
Find issues AND fix them by editing the files directly.

Entry: kathas/festivals/<slug>/
Read all four files: hi.md, en.md, mr.md, gu.md.

For EACH translated file (en, mr, gu), check every item below. Fix all issues found.

──────────────────────────────────────────────
FAITHFULNESS (compare against hi.md paragraph by paragraph)
──────────────────────────────────────────────
□ Every paragraph in hi.md has a corresponding paragraph in the translation.
  No paragraph is missing. No paragraph is combined with another.
□ No content is added that is not in hi.md.
□ All named characters, places, numbers, and sequence of events match hi.md exactly.
□ The phala-shruti (closing merit statement) is present and faithful.
□ The panchang date note in Observance (if present) is translated, not omitted.

──────────────────────────────────────────────
VOCABULARY SIMPLICITY
──────────────────────────────────────────────
□ No literary or archaic words — every word should be one a non-literary reader
  uses in daily speech.
  - English: no "bestowed", "propitiated", "manifested", "celestial realm",
    "auspicious grace", "commenced", "verily", "thus did he speak"
  - Marathi: no overly Sanskritised forms; prefer common spoken Marathi
  - Gujarati: prefer everyday Gujarati a grandmother would use, not textbook Gujarati
□ If a simpler equivalent exists, use it. Flag and fix any complex word found.

──────────────────────────────────────────────
PRONOUN REGISTER
──────────────────────────────────────────────
Marathi:
□ ALL named characters (deities, sages, kings, named devotees, named women,
  named brahmins — even if they sin or err) must use ते/त्यांनी/त्यांना/त्यांचा throughout.
□ Only truly unnamed background figures ("एक व्यापारी", unnamed guards) use तो/त्याने.
□ Named demons (Kansa, Hiranyakashipu, Ravana) use तो/त्याने — they are not revered.

Gujarati:
□ ALL named characters must use તેઓ/તેઓએ/તેઓના/તેઓને throughout.
□ Only truly unnamed figures use તેણે/તેને.
□ Named demons use તેણે — they are not revered.

English:
□ Deities addressed with "Lord", "Devi", "Shri" or equivalent.
□ Sages addressed as "Sage", "Maharshi", or by full name with title.
□ No colloquial informality for deities or revered figures.

──────────────────────────────────────────────
STRUCTURE
──────────────────────────────────────────────
□ All section headings are in English exactly: ## Katha, ## Significance, ## Vidhi,
  ## Observance (if present), ## Mantras (if present). No translated headings.
□ All sections present in the translation that are present in hi.md.
□ `---` separators appear in the same positions as in hi.md.
□ Devanagari mantra text is verbatim (not paraphrased or abbreviated).
□ IAST transliteration lines are verbatim.
□ Only the meaning lines (अर्थ / meaning) are translated.

──────────────────────────────────────────────
LANGUAGE NATURALNESS
──────────────────────────────────────────────
□ Marathi prose reads like natural Marathi — not Hindi sentence structure
  written in Marathi script.
□ Gujarati prose reads like natural Gujarati — same test.
□ English prose reads as devotional narrative, not a literal gloss of the Hindi.

──────────────────────────────────────────────
AFTER FIXING:
Report a one-line summary per language: what was fixed (or "PASS — no issues").
```

**Pass criteria:** All three translations pass all checklist items. Any issue must be fixed
before the entry proceeds to `status: published`.

**Record the outcome:** Add a comment to meta.yaml:
```yaml
# Phase 7 review: en/mr/gu PASS — <date>
```

---

## Translation workflow (hi, mr, gu)

After `en.md` is `reviewed`:

1. Copy `en.md` → `hi.md` (same front matter structure, `lang: hi`).
2. Translate the prose sections. **Section headings MUST stay in English in every language file** — do not translate them. The corpus parser (`_corpus.py`) reads sections by their English heading names; translated headings will break the build silently.
   - `## Katha` — keep as-is in hi, mr, gu
   - `## Significance` — keep as-is in hi, mr, gu
   - `## Vidhi` — keep as-is in hi, mr, gu
   - `## Observance` — keep as-is in hi, mr, gu
   - `## Mantras` — keep as-is in hi, mr, gu
3. The Devanagari in Mantras stays exactly the same across all languages.
   Translate only the one-line meaning.
4. Translate `title`, `subtitle`, `summary`, `reel_hook` naturally — not word-for-word.

**Language register for each translation:**
- **Hindi (hi):** Use the everyday Khariboli Hindi a person speaks at home or in a bazaar.
  Avoid tatsama (Sanskrit-heavy) vocabulary. Prefer: *उसने पूजा की* over *उन्होंने पूजन-अर्चन संपन्न किया*.
- **Marathi (mr):** Use standard spoken Marathi, not the formal written register.
  Avoid Sanskritised Marathi used in academic texts.
- **Gujarati (gu):** Use everyday Gujarati. The tone should feel like a grandmother
  telling this story, not a textbook.

**The simplicity rule applies equally in all four languages.** The vocabulary test:
*would a person who reads this language but has not studied it formally understand every sentence?*
If not, simplify.

### Respect hierarchy for pronouns and verbs

Every character in the katha must be addressed at the correct level of respect. This is not
optional — getting it wrong feels immediately wrong to any native reader and breaks trust.

**Hindi:**

| Character type | Pronoun | Verb form | Example |
|---|---|---|---|
| Deity (Vishnu, Shiva, Devi, Krishna…) | वे | उन्होंने / उनसे / उन्हें | वे वहाँ प्रकट हुए। उन्होंने कहा… |
| Divine beings (Garuda, Nandi, Narada, Hanuman) | वे | उन्होंने | नारद जी वहाँ पहुँचे। उन्होंने पूछा… |
| Rishis, Sadhus, Gurus | वे | उन्होंने | महर्षि ने कहा… / वे बोले… |
| **Any named character** — kings, queens, brahmins, devotees, pativrata women, even sinning/repenting named characters | वे | उन्होंने | Named king राजा हरिश्चन्द्र: वे बोले। Named devotee सत्राजित: उन्होंने कहा। |
| Truly unnamed background figures ("एक व्यापारी", "एक स्त्री", unnamed guards) | वह | उसने / उसे | वह घबरा गया। उसने द्वार खोला। |
| Demons / villains (Kansa, Hiranyakashipu, Ravana…) | वह | उसने | उसने सैनिकों को आदेश दिया। |

> **The key rule:** The pronoun tier is decided by whether the character has a **name**, not by
> whether they are good or bad. Named brahmin, named king, named devotee, named queen — all get
> वे/उन्होंने. Only truly anonymous figures ("a merchant", "a woman", "the guards") get वह/उसने.
> Demons who are named and prominent (Kansa, Ravana) stay at वह/उसने — they are not revered.

**The specific test for Hindi:** whenever you write a sentence about a deity or a sage,
ask — would you say *"Krishna ne kaha"* or *"Krishna ji ne kaha"* in conversation?
In devotional writing, use the **-जी** suffix when naming deities/sages inline:
*श्रीकृष्ण जी ने कहा…*, *नारद मुनि ने कहा…* — then continue with **उन्होंने** for that
character through the paragraph.

**Marathi equivalents:**

| Character type | Pronoun/verb |
|---|---|
| Deity / Sage / Any named character (king, devotee, brahmin, woman) | ते/त्यांनी/त्यांना/त्यांचा/त्यांच्या |
| Truly unnamed background figure / demon | तो/त्याने/त्याला (m) or ती/तिने/तिला (f) |

**Gujarati equivalents:**

| Character type | Pronoun/verb |
|---|---|
| Deity / Sage / Any named character (king, devotee, brahmin, woman) | તેઓ/તેઓએ/તેઓના/તેઓને |
| Truly unnamed background figure / demon | તેણે/તેને (m/f) |

### Translate in blocks, not sentence by sentence

**Why:** Translating one sentence at a time loses the rhythm of the paragraph, causes
pronoun inconsistency between sentences, and introduces meaning errors at sentence
boundaries. A block of 3–5 sentences is the right unit.

**Procedure:**
1. Read the entire Katha section in the source language first. Understand the full arc.
2. Identify natural paragraph / scene boundaries (setup, conflict, turning point, resolution,
   phala-shruti). Each boundary is a block boundary.
3. Translate one block at a time. After each block:
   - Re-read the translated block aloud (mentally). Does it flow naturally?
   - Check: are all pronouns at the correct respect level?
   - Check: are all character names spelled consistently with the rest of the entry?
4. Only move to the next block after the current one reads cleanly.
5. After all blocks are done, read the full translated section from top to bottom once more.

**Block example (Hindi):**

Source block (English):
> Devaki's eighth child was born at midnight. The prison cell was flooded with light. Kansa's
> guards fell asleep. Vasudeva lifted the child and walked through the open doors.

Translate this whole unit together, not line by line:
> मध्यरात्रि को देवकी के आठवें पुत्र का जन्म हुआ। पूरी कोठरी रोशनी से भर गई। कंस के
> पहरेदार गहरी नींद में सो गए। वसुदेव जी ने बालक को उठाया और खुले दरवाज़ों से बाहर निकल गए।

Notice: Vasudeva gets **जी** (respected adult), Kansa gets plain **कंस के** (no ji, no
respectful verb), and the sentence rhythm mirrors the original's pace.

### Source language for translations — read from the original

Many kathas exist in Hindi in their primary Gita Press source. When that is the case:

- **Hindi (hi.md):** Do NOT translate from `en.md`. Go directly to the Hindi Gita Press
  source and adapt/simplify from it. Double translation (Sanskrit → English → Hindi) always
  introduces errors and the Hindi ends up sounding unnatural.
- **English (en.md):** Translate from the Sanskrit source (via wisdomlib.org) or the best
  available scholarly English translation. Where a good English translation already exists,
  adapt it rather than retranslating from scratch.
- **Marathi / Gujarati:** These can be translated from the verified Hindi (hi.md), not from
  English — the vocabulary and phrasing will be more natural. But if a Marathi or Gujarati
  primary source exists (e.g., a regional vrat tradition with its own text), always prefer
  the primary source.

The chain of trust: **Sanskrit/regional primary source → Hindi → Marathi/Gujarati → English**,
not the reverse. English is canonical for the *schema and structure* of this repo; it is not
necessarily the best base for Indic-language translations.

5. Repeat for `mr.md` (Marathi) and `gu.md` (Gujarati).
6. After all four language files are done → set `status: published` in meta.yaml.

---

## Batch workflow — doing multiple entries at once

Batching by Hindu month is the most efficient approach because:
- DrikPanchang month pages show all dates for a month together — verify a whole month at once.
- One Purana section (e.g. Skanda Purana, Kartik Mahatmya) often covers multiple entries
  in the same month — read it once, write several kathas.
- The calendar order of writing matches the book's chapter order, so you always have a
  contiguous "Part 1" to preview.

**Suggested batch size: one Hindu month at a time (~8–14 entries per month).**

Batch procedure:
1. Open KATHA_CALENDAR.md. Pick the next unwritten month.
2. Go to DrikPanchang's month page. Verify and fill all `date_2026`/`date_2027` for
   every entry in that month block.
3. Identify which Puranas cover that month's entries. Read/skim the relevant chapters.
4. Write kathas in calendar order within the month.
5. Run build preview once at the end of the batch.
6. Set all verified + written entries to `status: reviewed`.

---

## Quick reference: word counts

| Section | Minimum | Target | Maximum |
|---|---|---|---|
| Katha | 250 | 400–550 | 700 |
| Significance | 80 | 120–180 | 250 |
| Vidhi | 60 | 100–150 | 200 |
| Observance (vrats) | 60 | 80–120 | 150 |
| Mantras | 1 mantra | 1–2 mantras | 3 mantras |
| **Total per entry** | ~500 | ~700–900 | ~1200 |

At 800 words/entry × 108 entries = ~86,000 words = ~350–380 pages at 6×9.

---

## Source hierarchy (when sources conflict)

1. **Primary Sanskrit text** (Valmiki Ramayana, Mahabharata, named Purana chapter) — highest authority
2. **Gita Press Hindi edition** — most trusted popular interpretation, 80+ years of editorial consistency
3. **Other traditional commentaries** (Shankaracharya lineage, regional acharya traditions)
4. **DrikPanchang** — for dates, tithis, and muhurat only (not for story content)
5. **Folk/oral tradition** — valid source for folk-tier kathas; must be labelled as such

When sources give different versions: follow the primary Sanskrit source. Note the variation
in one sentence in Significance if it is significant: *"In the South Indian tradition, this
katha is told differently…"*

---

## What NOT to write

- **No invented scripture.** If you cannot find the source, write "Source: TODO-VERIFY" and
  leave the Katha section as a stub rather than fabricating a story.
- **No complex vocabulary.** Every word must be one a non-literary reader uses in daily life.
  If you write a sentence and think "a scholar would appreciate this phrasing," simplify it.
- **No unexplained Sanskrit in the Katha prose.** Any Sanskrit shloka inside the narrative
  must be immediately followed by its plain-language meaning. No exceptions.
- **No Sanskrit showing-off.** Quoting a shloka to demonstrate that you found the source is
  wrong. The Mantras section handles shlokas formally; the Katha section is for storytelling.
- **No comparative religion framing.** Do not say "similar to Christian X" or draw parallels
  to other traditions. This is a devotional text.
- **No doctrinal debates.** Do not engage with questions like "was Krishna historical?" — state
  the tradition simply and faithfully.
- **No modern social commentary** embedded in the katha ("this teaches us gender equality"
  etc.). Let the story carry its own meaning.
- **No sycophantic openers.** Do not begin the Katha with "This beautiful and sacred story..."
  Begin with the story itself.
- **No Sanskritised register in Hindi/Marathi/Gujarati.** Translations must feel spoken, not
  written-for-scholars. If the Hindi reads like a government circular or a Purana critical
  edition, it is wrong.
