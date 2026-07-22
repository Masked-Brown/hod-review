# MANIFEST 2.5 — COMPLETE

status: complete-with-questions

summary: Built the bespoke three-part AQA A-level Biology reference layer from AB's
`professor-clive` corpus and wired the training-data table mechanism. Populated the validated
topic (AQA Biology 3.2.1 Cell structure) to full depth — content coverage, examiner insight,
and a distilled set of real exam questions — and scaffolded the other seven topics as
structure only, per the size guidance. Defined and published the `SPEC` handle convention
(the open question M2 handed to M2.5), completing the triple anchor: a finding on cell
structure can now cite a real pedagogical principle (M2 frameworks), a real spec point +
misconception (this layer), and a real exam question (this layer). Shipped the training-table
schema with exactly one `ILLUSTRATIVE` row. Corpus paths verified readable before starting.

files-changed (all were M1 stubs; M2.5 overwrote each with authored substance, as the M1 and
M2 handovers instructed):

- `reference/spec/3.2-cell-structure.md` — the deep validated topic (187 lines). Published
  `SPEC` handle convention + handle table; six sub-concept sections each with AQA credit
  vocabulary and structure→function links; a 10-entry examiner-insight/misconception block
  (EI-1…EI-10) with cohort mastery data and a "slide risk" per entry; a mark-scheme
  credit-terms tier table (always/context/reject) with the context-dependent "DNA" trap; an
  assessment-shape + marking-mechanics note; cross-topic co-occurrence links; provenance.
- `reference/spec/aqa-biology-index.md` — the 8-topic scaffold (3.1–3.8, all 38 subtopics)
  with one-line scope each, depth-status markers (● validated / ○ scaffold), the `SPEC` handle
  convention pointer, and required-practical notes only where certain.
- `reference/exam-questions/cell-structure.md` — 8 real AQA past-paper questions distilled
  from `06_qrs` (six verbatim + two calculation), each tagged to spec point and assessment
  objective (AO1/AO2), cross-linked to a misconception anchor, with a coverage table and
  honest provenance. No generated questions.
- `training-layer/README.md` — the accretion mechanism: two artifacts, the five columns, the
  three strict labels, and exactly one `ILLUSTRATIVE` row rendered as the full 7-field finding
  block (SEVERITY…QUESTION) showing the triple-anchor reasoning chain.
- `README.md` — corrected the build-status table (M2 and M2.5 → complete) and the status
  banner to reflect the shipped substance. Housekeeping for the honesty axis; flagged for M5's
  claims audit (M5 owns the README).

files-created:
- `handover/MANIFEST-2.5-COMPLETE.md` — this file.

decisions-made:
1. **Verified the three corpus paths readable before starting** (M1 open-question #6 / M2
   next-needs). All three exist and are readable: `04_intelligence`, `05_notes`, `06_qrs` under
   `professor-clive/corpus/aqa/a-level/biology`. The validated topic maps to the `3.2.1_*`
   subtrees in each. No path failure to flag.
2. **Kept the M1 filename `3.2-cell-structure.md` but cite the precise AQA code `AQA 3.2.1`
   inside SPEC handles.** Justification: the seed files call the topic "3.2 Cell structure" and
   M1 locked that filename (M1 decision #2, M2 next-needs); the precise AQA *subtopic* code is
   3.2.1 (3.2 is the parent topic "Cells"). Findings must anchor to a real spec point, so the
   handles use `AQA 3.2.1`. The file's header states this explicitly. A reconciliation for
   citability, not a change to the locked topic — logged so it is not silent.
3. **Defined and published the `SPEC` handle convention** `AQA <code> — <handle>` (resolves M2
   open-question #4). Justification: R15 requires a finding to cite a *specific* handle, not
   gesture; M2 defined `PRINCIPLE` handles and explicitly handed `SPEC` to M2.5. The convention
   mirrors the `PRINCIPLE` format so the two compose into the triple anchor, and the deep file
   publishes the full handle set as the known list M3's optional check may validate against
   (M2 open-question #2).
4. **Full depth on 3.2.1 only; scaffolded 3.1–3.8.** Justification: the plan's size guidance —
   depth where demonstrated (the M4 validation deck exercises only this topic), scaffold
   everywhere else; an all-topics dump is bulk that lowers the methodology score.
5. **Distilled 8 real questions, including 2 calculation questions.** Justification: `spec.md`
   chose this topic partly for its magnification/percentage-error calculations, so the
   assessment leg must exercise that anchor. Six carry verbatim stems from the corpus
   `06_sample_questions.md`; the two calculation questions (2024 P1 Q03.4/03.5) are distilled
   from their documented mark scheme and shared question context (their verbatim stems are
   parked in the corpus V2). Flagged as provenance on each rather than fabricating a stem — the
   questions are real AQA items, honoring "distil real questions, do not generate."
6. **AO mapping stated and applied:** KNOWLEDGE→AO1, APPLICATION→AO2, CALCULATION→AO2
   (quantitative application). Justification: AQA's assessment-objective definitions; the set's
   AO spread mirrors the topic's real 66/19/14 mark profile.
7. **Attribution/copyright framing for the exam questions.** Justification: AB's distilled
   notes/intelligence/mark-scheme analysis are his own IP (plan §M2.5: "copyright is not a
   constraint here"), but the past-paper *question text* is AQA's. Handled by concise quotation
   with year/paper/question attribution for educational criticism/review, and by framing the
   mark schemes as AB's *distilled credit points*, not verbatim AQA mark-scheme documents. See
   open-question #1 for the residual human decision.
8. **Examiner-insight block as 10 numbered, citable handles (EI-1…EI-10),** each with the
   cohort data where recorded and a "slide risk" line. Justification: this is the sharpest and
   hardest-to-fake lens; numbering makes each a checkable `SPEC` handle and the "slide risk"
   lets a finding say what a bad slide *looks like*, not just that content is thin. Added EI-10
   (causal-chain APPLICATION) to cover the ~19% APPLICATION mark share, a genuine gap.
9. **Illustrative training row rendered as the exact 7-field finding block, severity calibrated
   MAJOR not CRITICAL.** Justification: fidelity to `finding-schema.md` §1 (M2 added `SEVERITY`
   as a parseable line beyond the six `spec.md` fields; the row honours it). MAJOR because the
   "energy"/ATP slip loses a mark and undercuts the slide's own purpose but does not reverse a
   concept — modelling non-inflated severity (R10) rather than dramatising the demonstration.
   PRINCIPLE handle `Rosenshine 4 — Provide models`; SPEC handle `AQA 3.2.1 — ATP not "energy"
   (EI-1)`.
10. **Added a mark-scheme credit-terms tier table.** Justification: vocabulary precision carries
    most of this topic's marks; the mark scheme's own always/context/reject tiers are a
    high-value citable lookup for the dominant finding type, and the context-dependent "DNA"
    term is called out as the trap. Real corpus data, not padding.
11. **Kept required-practical claims minimal and only where certain.** Justification: avoid
    fabricated pedagogy. 3.2.1 has no single numbered RP (its microscopy/drawing skill spans
    several), so it is framed as "the required-practical skill of optical microscopy +
    scientific drawing"; scaffolded topics name an RP only where confidently known.
12. **Updated the README build-status table + banner.** Justification: M2 left its own row as
    "pending" though complete; leaving M2.5 as pending after shipping would understate the repo,
    a mild honesty miss. The status table exists precisely to keep the repo and its claims in
    step. Minimal, accurate edits; flagged here because M5 owns the README claims audit.
13. **Used "constructed"/"run" wording; did not propagate "real run."** Justification: honours
    M1 open-question #1 and M2 decision #12 — the load-bearing honesty axis.
14. **The deep file landed at 187 lines** (the ~200–400 guidance is an "aim"). Justification:
    deliberately at the lean end to honour the anti-bulk discipline — every line is a finding
    anchor (a handle, a credit term, a numbered misconception, a marking rule), which is denser
    citable value than a longer raw-dump would carry. Judged this a better methodology-score
    trade than padding to the midpoint.

disagreements:
1. **No substantive divergence from the seed files.** M2.5 built to `plan.md` §M2.5 (the
   05_notes/04_intelligence/06_qrs mapping), §5 (the five-column table), and `spec.md`
   ("Reference architecture", "Training-layer schema") as written. Two items are flagged as
   *reconciliations*, not overrides, so they are not silent: (a) the seed files call the topic
   "3.2 Cell structure" while the precise AQA subtopic code is 3.2.1 — kept the M1 filename,
   used `AQA 3.2.1` in handles for citability (decision #2); (b) two of the eight questions are
   distilled from the corpus mark scheme + context rather than verbatim stems, to cover the
   calculation assessment anchor the topic was chosen for (decision #5). Both within the M2.5
   instruction; flagged only because they are worth a human eye.

open-questions:
1. **AQA past-paper question copyright — human decision for M5's claims audit.** M2.5 reproduces
   six short verbatim AQA question stems (with year/paper/question attribution) plus distilled
   credit points. AB's corpus itself keeps `06_sample_questions.md` gitignored ("real AQA exam
   questions … never commits"), so the verbatim stems are the one part of this layer that is
   AQA's IP rather than AB's own distillation. I judged concise attributed quotation for
   educational criticism/review defensible and consistent with the explicit M2.5 instruction to
   pull real questions. **AB/M5 decides:** confirm this is acceptable for a public repo, or
   reduce Q1–Q6 to question *specifications* (command word + marks + distilled mark scheme)
   without the verbatim stem, as Q7–Q8 already are.
2. **Should `check.py` validate `SPEC` handles against the published set?** The deep file now
   publishes the known handle set, so the option M2 anticipated (open-question #2) exists.
   Recommend a **soft warning, not a hard block**, so M2.5's/later reference-layer growth does
   not break the gate. **M3 decides.**
3. **Q7–Q8 verbatim stems.** If a later pass un-parks the calculation stems from corpus V2, Q7–Q8
   could carry verbatim question text like Q1–Q6; for now they stay as distilled specifications.
   **M4/M5.**
4. **Inherited (M1 open-question #1):** normalising the residual "real run" wording in the seed
   files remains a human decision. M2.5 added no such wording.

next-manifest-needs:
- **M3 is next** (enforcement: `extract.py`, `check.py`, `tests/`, CI). It should read, in
  order: this handover; `reference/finding-schema.md` (the parse contract, §1–§7, and §7's block
  checklist); `spec.md` ("What `check.py` blocks"); and the **published `SPEC` handle set** in
  `reference/spec/3.2-cell-structure.md` (for the optional `PRINCIPLE`/`SPEC` handle check —
  recommend soft-warning per open-question #2).
- **The triple anchor is now complete.** `PRINCIPLE` (frameworks, M2) + `SPEC` (content +
  examiner insight, M2.5) + `exam-questions` (assessment, M2.5). A finding on 3.2 cell structure
  can cite all three; the `SPEC` field resolves to a real published handle `AQA 3.2.1 — …`.
- **`SEVERITY` is a parseable finding line** (M2 finding-schema §1). The `ILLUSTRATIVE` training
  row and any critique the gate parses carry it; `check.py` keys findings off `^SEVERITY:`.
- **The training-table schema is fixed** (`training-layer/README.md`): M4 populates
  `runs/<teacher-id>/<date>/training-table.md` with `CONSTRUCTED` rows against it, and folds
  column 4 into `training-layer/<teacher-id>.md`. The `ILLUSTRATIVE` row is the target shape.
- **Guardrails carried forward:** the gate reports facts and blocks, never judges pedagogy
  (finding-schema §7–§8, rules R16); the verbatim `QUOTE` check is the load-bearing one;
  typographic-quote normalisation (M2 open-question #1) and the rewrite/fix-pattern regex set
  (M2 open-question #3) are M3's to own; no fabricated questions; keep "constructed" wording.
