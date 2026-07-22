<!-- CONSTRUCTED — this is the answer key for a deliberately seeded demonstration deck.
     No real teacher or lesson. Every flaw below was placed on purpose by build_lesson.py
     and mapped to a specific entry in editor/reference/. See plan.md §M4. -->

# Expected findings — the answer key *(CONSTRUCTED)*

> **What this is.** The ground truth for the `s-whitfield / 2026-07-22` validation run. Every
> flaw in `lesson.pptx` was **seeded on purpose** and is listed here with the slide it sits
> on, the verbatim seeded text, the `editor/reference/` entry it maps to, and the severity a
> correct read should assign. A judge scores `critique.md` against this file: each seeded flaw
> the editor should **catch**, each clean slide it should **leave alone**.
>
> **This is a constructed self-consistency test, not a blind trial.** The same author built the
> deck and the critique, so full recall is expected — what this run demonstrates is the
> *mechanism* (seeded flaw → reference anchor → finding → gate → answer-key score → accreted
> pattern), the finding **form** (fabrication-checked, anchored, rewrite-free, ends in a
> question), and that the editor **leaves clean slides alone**. A genuine blind trial — a real
> teacher on a real deck — is the reserved `REAL` run named in `OPEN-DEFECTS.md`, not this.

**Deck:** `lesson.pptx` (12 slides) · **Topic:** AQA A-level Biology 3.2.1 Cell structure
**Seeded flaws:** 8 (one slide carries two) → **9 expected findings** · **Clean slides:** 4

---

## The three flaw types the run was built to exercise (plan.md §M4)

| Required flaw type | Seeded as | Where |
|---|---|---|
| A **misconception the slide reinforces** (EI-coded) | F7 — magnification written for resolution (EI-5) | Slide 10 |
| A **spec point the lesson skips** | F2 — cell fractionation absent from the whole deck | Slide 3 (objectives) |
| An **assessed question-format never rehearsed** | F8 — magnification calculation, no worked model, unit-conversion mark unrehearsed (exam Q7) | Slide 11 |

Four more EI-coded / vocabulary misconceptions (F3, F4, F5, F6a, F6b) and one further pedagogy
flaw (F1) are seeded around them so the read is exercised across content, examiner-insight, and
assessment-alignment anchors at once, and so the vocabulary-precision pattern the persona
flagged recurs often enough to accrete (see `training-table.md`).

---

## The seeded flaws (ground truth)

### F1 — Starter opens on new content, no retrieval · Slide 2 · expect **MAJOR**
- **Seeded text (verbatim):** "Copy the organelle summary table from the sheet into your notes."
- **Maps to:** `PRINCIPLE: Rosenshine 1 — Daily review` (also `Retrieval — review vs re-reading`, `../../../editor/reference/frameworks/`).
- **Flaw type:** pedagogy / lesson sequencing. The highest-value opening minute is spent copying brand-new content instead of retrieving prior (GCSE) knowledge.
- **Not seeded here:** slide is otherwise fine; the one finding is the missing retrieval.

### F2 — Lesson skips cell fractionation · Slide 3 · expect **MINOR**
- **Seeded text (verbatim, the anchor line):** "use a light microscope and calculate magnification"
- **Maps to:** `SPEC: AQA 3.2.1 — cell fractionation` (`../../../editor/reference/spec/3.2-cell-structure.md` §5).
- **Flaw type:** skipped spec area. The objectives run organelles → prokaryotes → viruses → microscopy with **no** cell fractionation, a 3.2.1 content area with its own exam questions (exam Q1; the cold/isotonic/buffered step is the single most-dropped fractionation mark, EI-9).
- **Why MINOR, not MAJOR:** on a *first* lesson the omission may be deliberate sequencing. A correct read hands this back as a **question** (is it coming later?), not an assertion of error — a deliberate test that the editor does not over-flag (R10).

### F3 — "Mitochondria produce energy" · Slide 5 · expect **MAJOR**
- **Seeded text (verbatim):** "Mitochondria produce energy for the cell's reactions."
- **Maps to:** `SPEC: AQA 3.2.1 — ATP not "energy"` (§1 credit vocabulary; examiner insight **EI-1**; credit-terms tier: "energy" is **never-credit**).
- **Flaw type:** reinforced misconception / vocabulary. "Produce energy" is an explicit AQA reject; ATP is the only credited term. Directly on the persona's stated focus weakness.

### F4 — Nucleus "controls all the cell's activities" · Slide 6 · expect **MAJOR**
- **Seeded text (verbatim):** "The nucleus controls all the cell's activities."
- **Maps to:** `SPEC: AQA 3.2.1 — EI-7` (§1; "controls cell activities" is GCSE-level, **zero credit**; credit is coding for polypeptides).
- **Flaw type:** reinforced misconception / GCSE-carryover vocabulary. Second data point on the vocabulary-precision pattern.

### F5 — Prokaryote features: universal and non-universal mixed · Slide 8 · expect **MAJOR**
- **Seeded text (verbatim):** "murein cell wall, cell-surface membrane, 70S ribosomes, circular DNA, capsule, plasmids, flagella"
- **Maps to:** `SPEC: AQA 3.2.1 — EI-2` (the list rule; §2 prokaryotic structure; assessed by exam **Q3**).
- **Flaw type:** reinforced misconception / list discipline. Murein wall, membrane, 70S, circular DNA are universal; capsule, plasmids, flagella are not — presented undifferentiated, the list trains the exact answer the "features of all prokaryotes" question zeroes.

### F6a — Acellular and non-living fused · Slide 9 · expect **MAJOR**
- **Seeded text (verbatim):** "Viruses are acellular and non-living because they cannot replicate outside a host cell."
- **Maps to:** `SPEC: AQA 3.2.1 — EI-3` (§3; the two definitions are marked **independently**; assessed by exam **Q4**).
- **Flaw type:** reinforced misconception. The bullet welds two independently-marked definitions and justifies both with one non-living reason; only ~15% of the cohort defines *acellular* correctly.

### F6b — "genetic information" (a reject term) · Slide 9 · expect **MINOR**
- **Seeded text (verbatim):** "A virus is genetic information surrounded by a protein capsid."
- **Maps to:** `SPEC: AQA 3.2.1 — genetic material not "information"` (§3 credit vocabulary; credit-terms tier: "genetic information" is **never-credit**).
- **Flaw type:** vocabulary. **This is the second distinct flaw on slide 9** — it must be held as its own finding, not merged with F6a (tests `rules.md` R8: hold distinct weaknesses distinct, never collapse).

### F7 — "Increase the magnification" to see smaller organelles · Slide 10 · expect **CRITICAL**
- **Seeded text (verbatim):** "To see them, increase the magnification for more detail."
- **Maps to:** `SPEC: AQA 3.2.1 — EI-5` (§4 microscopy; resolution ≠ magnification; assessed by exam **Q6**).
- **Flaw type:** reinforced misconception — **the CRITICAL**. The slide gives magnification as the cause of the optical microscope's limit; the real cause is resolution. It reverses the key distinction and sends the class to revise the wrong causal model.

### F8 — Calculation: no worked model, straight to independent work · Slide 11 · expect **MAJOR**
- **Seeded text (verbatim):** "Now work through questions 1-6 on the worksheet."
- **Maps to:** `PRINCIPLE: Rosenshine 4 — Provide models` + `SPEC: AQA 3.2.1 — exam Q7` (also `CLT — worked-example effect`).
- **Flaw type:** assessed-format not rehearsed. The equation is stated then the class works alone with no worked example; AQA pays the mm→µm unit conversion as its **own** mark (exam Q7), reliably dropped when never modelled.

---

## The clean slides (expected: NO finding)

A correct read leaves these alone. A finding on any of them is a **false positive** (manufactured
finding, `rules.md` R10) and counts against the editor.

| Slide | Content | Why it is clean |
|---|---|---|
| **1** | Title / lesson overview | No pedagogical claim to fault. |
| **4** | "The eukaryotic cell" — membrane-bound organelles, compartmentalisation | Correct, precise, appropriately pitched. |
| **7** | "Rough ER and Golgi apparatus" | Uses full terms, links structure→function, gives Golgi two distinct functions — the vocabulary discipline the mark scheme wants. |
| **12** | "Plenary" — closed-book, name three organelles + precise function, check vs mark scheme | Genuine retrieval (`Retrieval — testing effect`) and a precision check — the good version of what slide 2 fails to do. |

---

## Scoring grid (what the judge fills in against `critique.md`)

| Flaw | Slide | Expected severity | Anchor | Caught? |
|---|---|---|---|---|
| F1 starter no retrieval | 2 | MAJOR | Rosenshine 1 | — |
| F2 fractionation skipped | 3 | MINOR | SPEC cell fractionation | — |
| F3 "produce energy" | 5 | MAJOR | SPEC ATP not "energy" / EI-1 | — |
| F4 nucleus "controls activities" | 6 | MAJOR | SPEC EI-7 | — |
| F5 prokaryote list rule | 8 | MAJOR | SPEC EI-2 | — |
| F6a acellular/non-living fused | 9 | MAJOR | SPEC EI-3 | — |
| F6b "genetic information" | 9 | MINOR | SPEC genetic material not "information" | — |
| F7 magnification for resolution | 10 | CRITICAL | SPEC EI-5 | — |
| F8 calc, no worked model | 11 | MAJOR | Rosenshine 4 + exam Q7 | — |
| *(clean)* slides 1, 4, 7, 12 | — | *no finding* | — | *false positive if flagged* |

The filled-in version of this grid — caught / missed / added — is in
`../../../build/handover/MANIFEST-4-COMPLETE.md`.

---

*Answer key for the CONSTRUCTED `hod-review` M4 run. Finding shape: `../../../editor/reference/finding-schema.md`.
Reference anchors: `../../../editor/reference/`. The produced read: `critique.md`; the gate result: `gate-pass.txt`.*
