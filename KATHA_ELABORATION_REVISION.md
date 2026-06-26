# Katha Elaboration — Revision Pass

## What this document is

A fresh-context brief for the next Claude session to **review and correct** the katha
elaborations that were already added to all 150 `hi.md` files in a prior session.

**One elaboration pass has already been done.** Every `hi.md` has been expanded and carries a
`katha_elaborated: "2026-06-25"` marker in its YAML front matter. All changes are uncommitted
(in `git diff HEAD`). This pass is NOT about adding new elaborations — it is about checking
whether what was already added is genuinely sourced and valuable, fixing what isn't, and
removing hollow additions.

---

## Context

The repo `atmasanatan-content` holds 150 festival/vrat entries. Each has:
- `kathas/festivals/<slug>/meta.yaml` — facts, sources, panchang
- `kathas/festivals/<slug>/hi.md` — Hindi prose (Katha · Significance · Vidhi · Mantras)

In a previous session, the `## Katha` section of every `hi.md` was expanded. All 150 are
**uncommitted** (in `git diff HEAD`). The file `katha_word_counts.txt` has before/after word
counts for every entry by phase.

### What was done — and the problem

The elaborations fall into two categories:

**Good (Phases 1–~10):** Entries that were genuinely thin (280–450 words) received real story
content drawn from the source scripture. Example — `jagannath-rath-yatra` went from 468 → 614
words by adding King Indradyumna's backstory, Vidyapati's journey, the divine craftsman episode,
and Brahma's explanation — all from Skanda Purana. These additions embedded new narrative facts.

**Problem (Phases ~15–30, especially 26–30):** Entries received ~70–90 words of invented
atmospheric content — character interiority ("Bhima sat with his eyes closed and wondered..."),
frozen moments ("Parvati did not step back. Her eyes were still..."), scene texture. None of this
came from any source. It adds mood but not substance.

The entries in Phases 26–30 that received manufactured paragraphs need to be replaced with
genuine sourced content.

---

## The cardinal rule: add only if there is genuine value

**Word count is never the goal.** The goal is a complete, satisfying katha that a reader finds
worth reading. Some stories are naturally 500–550 words and complete. Some go to 700+ words
because the source material is rich. Both are fine. The only failure states are:
- A story so thin it feels rushed or incomplete
- A story padded with content that adds nothing real

### Target and skip threshold

- **Target range: ~650 words.** This is a sweet spot, not a hard minimum or maximum. Stories that
  reach 600–700 words with every sentence earning its place are ideal. Shorter (500–550) is fine
  if the story is genuinely complete. Longer (700–800+) is fine if the source material is rich.
  Do not pad to reach 650, and do not cut a good addition just because the story already hits 650.
- **Skip threshold: 750+ words.** If the katha is already at or above 750 words, skip it entirely —
  do not add anything, regardless of what else could be said.

### Decision tree for each entry

```
Is the current katha section already 750+ words?
  → SKIP entirely. Story is at or above the skip threshold — do not add anything.

Is the current katha between 650–750 words?
  → The story is already at or near target. Only add if there is a standout story beat
    from the source that is genuinely missing and clearly improves the narrative.
    The bar here is high — if in doubt, leave it as-is.

Is the current katha under 650 words?
  → Check the source. Is there a story beat, fact, or detail the existing text skipped?
     YES, from a verifiable source → Add it.
     NO real omission found       → Leave it as-is. Do not add anything.
```

**Atmospheric sentences that help the story are acceptable** — if they make a transition
smoother, hold a dramatic moment, or improve the reading experience, they can stay. The
problem is when atmosphere is the *only* thing added and there is no story content at all.
The test: does this sentence make the katha better to read, or is it filler?

For the **existing additions** (already in the diff):
- Read what was added. Ask: does this make the story better?
  - It contains story facts from the source, or it improves narrative flow → **Keep it.**
  - It is atmosphere that genuinely helps (transition, pacing, a moment that needed weight) → **Keep it.**
  - It is invented interiority or mood with no story content and no obvious narrative function → **Replace with sourced content, or remove.**
  - Nothing sourced can be found to replace it → **Remove it.** Return the story to its pre-addition state.

A story at 480 words with every sentence earning its place is better than 570 words where 90
are hollow.

---

## What "good" elaboration looks like

**The standard to hit:**

1. Read `meta.yaml` → `scripture_ref` field. This names the source (e.g. "Skanda Purana,
   Reva Khanda" or "Mahabharata, Adi Parva, Astika section").
2. Fetch the source text from **wisdomlib.org** (search: `site:wisdomlib.org <scripture_ref>`),
   **sacred-texts.com**, or **Gita Press Hindi PDFs**.
3. Read what the existing katha says. Find a story beat, character detail, dialogue, or factual
   element present in the source that the existing prose omits or condenses.
4. Write 3–6 sentences that embed this sourced content naturally into the existing prose — at the
   most logical insertion point (usually before or after an existing paragraph break).
5. The addition should answer: "What actually happened here that the current text skips?"

**What NOT to add:**
- Invented interior monologue ("she must have felt...")
- Atmospheric filler ("the forest was quiet, the birds had stopped...")
- Theological commentary that belongs in Significance, not Katha
- Any sentence that cannot be traced to the source text
- Anything added only to push the word count up

---

## Priority order for revision

### Tier 1 — Definitely replace (phases 26–30, this session's work)

All 25 entries received manufactured paragraphs. Check `git diff HEAD -- kathas/festivals/<slug>/hi.md`
to see exactly what was added. For each, fetch the source and write a replacement.

| Phase | Slugs |
|-------|-------|
| 26 | akshaya-tritiya · parashurama-jayanti · akshaya-tritiya-parashuram · ganga-saptami · sita-navami |
| 27 | mohini-ekadashi · narasimha-jayanti · buddha-purnima · satyanarayan-adhyaya-5 · jyeshtha-sankashti |
| 28 | apara-ekadashi · vat-savitri-vrat · shani-jayanti · ganga-dussehra · somvati-amavasya |
| 29 | nirjala-ekadashi · gayatri-jayanti · nirjala-gayatri-jayanti · vat-purnima · ashadha-sankashti |
| 30 | yogini-ekadashi · kamika-ekadashi · masik-shivaratri · hariyali-amavasya · hariyali-teej |

### Tier 2 — Spot-check (phases 11–25)

Many of these also received thin additions (20–60 words). Use the word count file
(`katha_word_counts.txt`) to find entries where "Added" was small AND the "After" total is still
below 500 words — those likely need real sourced content.

### Tier 3 — Probably fine (phases 1–10)

These received the largest additions and were sourced from scripture. Spot-check 2–3 per phase
to confirm quality; only revise if something is clearly fabricated.

---

## Agent instructions (one agent per slug)

Each agent should:

```
Task: Revise the katha elaboration for slug: <slug>

1. Read kathas/festivals/<slug>/hi.md — note the current ## Katha word count.
   Check katha_word_counts.txt for the before/after numbers.

2. SKIP entirely if the current katha is already 750+ words.
   → Leave the file exactly as it is. Move to the next slug.

3. Run: git diff HEAD -- kathas/festivals/<slug>/hi.md
   This shows exactly what was added. Evaluate the addition:

   KEEP as-is if any of these are true:
   - It contains specific story facts (names, events, dialogue) traceable to the source.
   - It is atmospheric/transitional but genuinely improves narrative flow or pacing.
   Test: does this make the katha better to read? If yes, keep it.

   Mark for revision if:
   - It is invented interiority or mood with no story content and no narrative function.
   - It reads like padding — you could remove it and not miss it.

4. Read kathas/festivals/<slug>/meta.yaml — note the `scripture_ref` field.

5. Fetch the source text (wisdomlib.org, sacred-texts.com, or Gita Press):
   - Search: wisdomlib.org + <scripture name from scripture_ref>
   - Find the relevant chapter/section for this specific story

6. Compare source vs existing katha:
   - Is there a real story beat, character detail, or dialogue the katha omits?
     YES → Write a sourced replacement (60–120 words) and insert it.
     NO  → Remove the manufactured addition entirely. No replacement needed.
           A complete story at 470 words beats a padded one at 560 words.

7. Edit the file accordingly:
   - KEEP: existing addition passes the quality test (sourced or helpful atmosphere)
   - REPLACE: swap hollow addition with sourced content
   - REMOVE: hollow addition + nothing sourced to add → restore to pre-addition text

8. Do NOT change the katha_elaborated: "2026-06-25" YAML marker.
9. Do NOT change any other section (Significance, Vidhi, Mantras).
10. Report: slug | action (KEPT/REPLACED/REMOVED) | word count before → after | source used
```

---

## Technical notes

- **System Python:** `/usr/bin/python3` (3.9.6) — use this, not Homebrew Python
- **Build check after revision:** `/usr/bin/python3 build/to_book_manuscript.py --lang hi --include-drafts`
- **All 150 files are currently uncommitted** — safe to edit
- **katha_word_counts.txt** — reference for before/after word counts by phase
- **KATHA_CALENDAR.md** — ordered entry list by Hindu calendar
- **CLAUDE.md** — full repo instructions, read before starting

---

## Source lookup guide by entry type

| Entry type | Primary source | Where to find |
|------------|---------------|---------------|
| Vishnu Purana stories | Vishnu Purana | wisdomlib.org/hinduism/book/vishnu-purana |
| Skanda Purana stories | Skanda Purana | wisdomlib.org (search by kanda) |
| Mahabharata episodes | Mahabharata | wisdomlib.org or sacred-texts.com/hin/maha |
| Valmiki Ramayana | Valmiki Ramayana | wisdomlib.org/hinduism/book/valmiki-ramayana |
| Shiva Purana stories | Shiva Purana | wisdomlib.org/hinduism/book/shiva-purana |
| Ekadashi kathas | Padma Purana / Brahma Vaivarta Purana | wisdomlib.org |
| Satyanarayan katha | Skanda Purana, Reva Khanda | wisdomlib.org |
| Ganesha stories | Ganesha Purana / Mudgala Purana | wisdomlib.org |
| Navaratri (Devi) | Devi Bhagavata Purana | wisdomlib.org |

---

## Workflow orchestration (parallel agents per phase)

This revision should be run using the **Workflow tool** with parallel agents — five agents per
phase, one per slug, all running simultaneously. This is faster and avoids context contamination
between slugs.

### Setup (before any phase)

1. Read this document fully.
2. Read `CLAUDE.md` (repo conventions, build commands, tool paths).
3. Read `katha_word_counts.txt` to have the before/after numbers available.

### Run in the original phase order (1 → 30)

Process slugs in the same order they were originally elaborated — Phase 1 through Phase 30.
The priority tiers above are guidance on where problems are most likely; they are **not** the
execution order. Running in original order keeps things predictable and avoids confusion.

All 150 slugs can be run in one `parallel()` call — each is fully independent. The workflow
tool caps concurrency automatically, so there is no risk in passing all 150 at once.

```javascript
// Slugs in original phase order (Phase 1 → 30), read from BOOK_TODO.md
// Each agent revises one slug independently
const results = await parallel(ALL_SLUGS_IN_PHASE_ORDER.map(slug => () =>
  agent(
    `Revise the katha elaboration for slug: ${slug}. ` +
    `Follow the per-agent instructions in KATHA_ELABORATION_REVISION.md exactly.`,
    { label: `revise:${slug}`, phase: 'Revision' }
  )
))
```

To get the slug list in phase order, read `BOOK_TODO.md` — it has all 30 phases with their
5 slugs each, in the original sequence.

### After the batch: report then proceed

Once all agents complete, collect their reports (slug | KEPT/REPLACED/REMOVED | word count
before → after | source used) and print a summary to the user. If any slug couldn't find a source
or had an ambiguous situation, flag it for human review before proceeding.

### Tier 2 spot-check (phases 11–25)

After phases 26–30 are done, consult `katha_word_counts.txt` and identify entries in phases 11–25
where "Added" ≤ 40 words AND "After" < 500 words — these likely received thin additions worth
reviewing. Run a parallel() pass on those slugs only.

### Build check (after all revision phases)

```bash
/usr/bin/python3 build/to_book_manuscript.py --lang hi --include-drafts
```

Confirm no rendering errors before proceeding to the review phase.

### Final review (separate workflow, adversarial agent)

After all revision phases pass the build check, spawn a **separate review workflow** — do NOT
reuse the same agents that did the revision work.

```javascript
// Review workflow
const TIER1_SLUGS = [
  // 25 entries from phases 26–30 (list them explicitly)
  'akshaya-tritiya', 'parashurama-jayanti', /* ... all 25 ... */
]
// Plus 10 random slugs from phases 11–25 for spot-checking
const REVIEW_SLUGS = [...TIER1_SLUGS, ...TIER2_SAMPLE_10]

const reviews = await parallel(REVIEW_SLUGS.map(slug => () =>
  agent(
    `Adversarial review for slug: ${slug}. ` +
    `Follow the review agent instructions in KATHA_ELABORATION_REVISION.md. ` +
    `Be skeptical. Try to find padding, manufactured content, or misplaced theology.`,
    { label: `review:${slug}`, phase: 'Review' }
  )
))
```

All ~35 review agents run simultaneously. Collect results; any FLAG goes back to revision.

### Commit

Only after all Tier 1 entries are PASS in review: commit all 150 files together in a single commit.

```bash
git add kathas/festivals/*/hi.md
git commit -m "feat(hi): source-verified katha elaboration across all 150 entries"
```

---

## Quality check questions for each entry

Before committing a revised elaboration, verify:
- [ ] Can every sentence in the addition be traced to a named source?
- [ ] Does the addition tell us something the existing prose didn't already say?
- [ ] Is it in Hindi prose that matches the existing voice?
- [ ] Does it avoid theological commentary (that belongs in Significance)?
- [ ] Is it 60–120 words (not shorter padding, not a full retelling)?
- [ ] Does it embed naturally — the reader shouldn't notice the seam?

---

## Final review phase (separate agent, after all revisions done)

After all Tier 1 (and any Tier 2) revisions are complete, spawn a **separate review agent**
that has NOT seen the revision work. Its job is adversarial: assume the revisions may still
contain manufactured content and try to find it.

### Review agent instructions

```
Task: Review the katha elaboration quality across revised entries.

You are a reviewer who did NOT write these elaborations. Be skeptical.
Your job is to find content that was added for padding rather than value.

For each slug in the list provided:
1. Read kathas/festivals/<slug>/hi.md
2. Read kathas/festivals/<slug>/meta.yaml — note scripture_ref
3. Run: git diff HEAD -- kathas/festivals/<slug>/hi.md
   (If nothing was added, it was left as-is — check it still reads complete.)

4. For each added paragraph:
   a. Does it contain at least one specific, verifiable story fact
      (name, event, location, dialogue, sequence)?
      Spot-check 1 claim against wisdomlib.org or sacred-texts.com.
        Confirmed: PASS.  Not found: FLAG as UNVERIFIED.
   b. Is it purely character interiority, mood, or scene texture with no facts?
      FLAG as MANUFACTURED.
   c. Is it theological explanation or symbolism analysis?
      FLAG as MISPLACED (belongs in Significance, not Katha).
   d. Was it added to an entry that was already 750+ words before the addition?
      FLAG as UNNECESSARY-LENGTH (story was already long enough to skip).

5. Report for each slug:
   status: PASS | FLAG
   action_taken: KEPT | REPLACED | REMOVED
   current_word_count: <n>
   issues (if flagged):
     - sentence: "..."
       type: MANUFACTURED | MISPLACED | UNVERIFIED | UNNECESSARY-LENGTH
       suggested_fix: "..."
```

### Review scope

Run the review agent on all 25 Tier 1 entries (phases 26–30) plus a random sample of 10 entries
from phases 11–25. Total: ~35 entries per review run.

### Review output format

```
slug: <slug>
status: PASS | FLAG
action_taken: KEPT | REPLACED | REMOVED
current_word_count: <n>
issues (if flagged):
  - sentence: "..."
    type: MANUFACTURED | MISPLACED | UNVERIFIED | UNNECESSARY-LENGTH
    suggested_fix: "..."
```

### After review

- PASS entries: commit as-is
- FLAG entries: send back to revision agent with the reviewer's specific note
- If flagged as UNNECESSARY-LENGTH (story was already 750+ words): strip the addition, no replacement needed
- If flagged as MANUFACTURED or UNVERIFIED with no sourced replacement available: remove entirely, do not re-invent
- Repeat until all 25 Tier 1 entries are PASS
