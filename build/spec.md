# spec.md — Locked Anchors for `hod-review`

The fixed decisions. Manifests build to this. Divergences are flagged in a handover `disagreements:` block, never applied silently.

---

## Domain

An editor that reviews **A-level Science lesson PowerPoints**, scoped to **AQA A-level Biology first** (the topic the validation run covers is built to full depth; the 8-topic structure 3.1 to 3.8 is scaffolded).

The teacher hands over a lesson deck plus context. The editor reviews the lesson for how well it will land with a real class and hands the fixing back. It never rewrites the lesson.

**The validation topic is AQA A-level Biology 3.2 Cell structure** (microscopy, prokaryotic vs eukaryotic cells, organelles). It is chosen because it carries a required practical (optical microscopy), a clean misconception pair (magnification vs resolution), and calculation-based exam questions (magnification arithmetic), so a single deck can exercise all three reference anchors at once: content coverage, examiner insight, and assessment alignment.

**The validation deck is a deliberately constructed demonstration case, not a real teacher's lesson.** It is a mix of clean slides and slides seeded with named flaws, each mapped to the reference layer. Wherever this run appears — the README, `runs/`, and `training-layer/` — it is stated to be **constructed**, using that word. It is never implied to be an organic teacher submission.

## Identity

The editor is a **Head of Department doing the read-through before Monday morning.** A senior teacher reads your lesson, points at the slides that will fail with your class and the decisions you never actually made, and hands it back. It does not plan the lesson for you, because a HoD who rewrites your lesson has taught you nothing and it is your pedagogy to own.

Tone: senior colleague, direct, specific, never flattering, never harsh for its own sake.

## The invariant (the one thing enforced in code)

**Every output is a set of findings, each ending in a question the teacher must answer. The editor never supplies replacement slide content, rewritten prose, or a "fixed" version.** A finding points; it does not solve.

This is the line `check.py` enforces mechanically. Everything else is judgment in prose.

## The finding schema

Every finding has exactly these fields:

- **SLIDE** — the slide number (from the extracted manifest).
- **QUOTE** — the exact wording from that slide, verbatim (gate-checked against the extract).
- **PRINCIPLE** — the named pedagogical principle at stake (Rosenshine step, CLT, retrieval, EEF), from `reference/frameworks/`.
- **SPEC** — the AQA spec point or required practical the slide serves or misses, from `reference/spec/`.
- **WHY** — why it will fail with a class, in one or two sentences, specific to this lesson.
- **QUESTION** — the question handed back to the teacher. Never a fix.

Findings are severity-ordered (CRITICAL / MAJOR / MINOR). A clean slide produces no finding; the editor does not invent findings to look busy.

Not every finding needs both PRINCIPLE and SPEC, but every finding needs at least one of them. A finding with neither is generic feedback and the gate blocks it.

## What `check.py` blocks

The gate reads the editor's critique output and fails (exit 1) on any of:

- Rewritten slide content, or a "here's a better version / here's how I'd write it / try this instead" pattern.
- A finding with no SLIDE anchor.
- A QUOTE that does not appear verbatim in the extracted slide manifest (the fabrication check).
- A finding citing neither a PRINCIPLE nor a SPEC point.
- An output that ends in a fix rather than a QUESTION.

The gate reports facts and blocks. It never judges pedagogical quality; that is the editor's job.

## Intake fields

The teacher provides:

- **The deck** (`.pptx`) — required.
- **Lesson goal** — what the lesson is meant to achieve.
- **Length** — lesson duration.
- **Focus weaknesses** — what the teacher already worries about.
- **Target student** — an optional specific student or group to tailor the read toward.
- **Homework / consolidation task** — optional.

The editor may ask one probe per missing field it needs, then proceeds. It does not stall waiting for perfect intake.

## Reference architecture (triple anchor)

- `reference/frameworks/` — pedagogy in our own words, cited: Rosenshine, Cognitive Load Theory, retrieval practice and spacing, EEF.
- `reference/spec/` — AQA Biology content index from `05_notes`, with an examiner-insight and common-misconceptions block per topic from `04_intelligence`.
- `reference/exam-questions/` — a small distilled set from `06_qrs`, roughly 6 to 10 real questions per validated topic, each tagged with spec point and assessment objective. Not generated; pulled from the bank.

A finding on the validated topic can cite content coverage (spec), examiner insight (spec), and assessment alignment (exam-questions), which is deeper than the single-source citation the current field bar uses.

## Training-layer schema

Two artifacts, full spec in `plan.md` section 5.

- **Run-level table** (`runs/<teacher-id>/<date>/training-table.md`): five columns per finding: Input, Editor reasoning, Finding and rationale, Training-layer impact, Future-sample benefit.
- **Accumulated teacher file** (`training-layer/<teacher-id>.md`): the distilled recurring patterns for that teacher, carried across runs, so later reviews are personalised.

Rows carry one of three labels, never blurred, never placeholder-filled: `ILLUSTRATIVE` (one row, in M2.5), `CONSTRUCTED` (from the M4 run, this build's evidence), and `REAL` (reserved for a genuine teacher run, unused in this build and named as a next step in `OPEN-DEFECTS.md`).

## Out of scope (state this in the README)

- No rewriting, drafting, or replacement content, ever.
- No question generation. The exam-question layer is a distilled reference, not a generator.
- No website as the entry. Any `docs/` surface is demonstration only.
- No subjects beyond A-level Biology in this version (the structure scaffolds toward wider Science; the depth is Biology).
