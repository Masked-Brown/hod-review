# Training layer — the folder that learns

**The accretion mechanism for `hod-review`, made auditable.** A folder cannot learn on its own; the review loop is the training loop. This layer records what each review taught the editor about a specific teacher, so the *next* review of that teacher is sharper than a cold read. It is shipped **populated from a run**, never as an empty diagram — the field's most-punished miss (see `communitycompetitions.md`).

> **State of this layer right now.** This README defines the schema and ships **exactly one `ILLUSTRATIVE` row** to make the mechanism legible. The evidence rows — labelled `CONSTRUCTED` — are populated by the M4 constructed validation run, not here. An empty or placeholder-filled table would be worse than no table; this file avoids that by shipping one honest, clearly-marked demonstration row and nothing more.

---

## Two artifacts

1. **Run-level table** — `runs/<teacher-id>/<date>/training-table.md`. One row per finding in that run. The reasoning chain for a single review, made visible.
2. **Accumulated teacher file** — `training-layer/<teacher-id>.md`. The distilled recurring patterns for that teacher, carried across their runs, so later reviews are personalised. Built by folding column 4 of each run-level table into a running profile.

The run-level table is the raw ledger; the teacher file is the distillation. Column 4 of the table is literally what gets written into the teacher file; column 5 is the payoff on the next run.

---

## The five columns

| Column | What goes in it |
|---|---|
| **1. Input** | The slide or section under review, plus the teacher's stated intent for it (from intake — lesson goal, focus weaknesses, target student). |
| **2. Editor reasoning** | The chain: which lens fired (a `reference/frameworks/` principle, a `reference/spec/` point, an `exam-questions` set), what it checked, what it compared against. The thought process made visible — this is the integrative-complexity demonstration. |
| **3. Finding and rationale** | The finding as handed back, in the `../reference/finding-schema.md` block shape (SEVERITY, SLIDE, verbatim QUOTE, PRINCIPLE and/or SPEC, WHY it fails with a class, the QUESTION handed back) — plus why this was surfaced rather than left. Never a fix. |
| **4. Training-layer impact** | What this run wrote to `training-layer/<teacher-id>.md`. E.g. "teacher recurrently front-loads content before any retrieval — pattern logged." |
| **5. Future-sample benefit** | How the next review of this teacher changes as a result. E.g. "next deck, the editor checks retrieval placement first, because it is this teacher's known blind spot." |

---

## The three labels — never blurred

Every row carries exactly one:

- **`ILLUSTRATIVE`** — a single row, here in this README, to show the mechanism. Not evidence of a run.
- **`CONSTRUCTED`** — from the M4 validation run. The deck and teacher persona are deliberately constructed and honestly labelled as such (`spec.md`, `plan.md` §M4). **This is the real evidence in this build.**
- **`REAL`** — reserved for a genuine teacher run on a genuine lesson. **Unused in this build** and named as a next step in `OPEN-DEFECTS.md`. A `CONSTRUCTED` row mislabelled `REAL` would be the pitch-outrunning-the-repo miss; the labels stay strict.

---

## ILLUSTRATIVE row (mechanism demonstration only)

> The slide, quote, teacher, and intent below are **invented to show how a row is filled** — no review has occurred. Marked `ILLUSTRATIVE`. Real rows arrive in M4 labelled `CONSTRUCTED`.

**Label:** `ILLUSTRATIVE` · **Topic:** 3.2.1 Cell structure · **Teacher:** *(illustrative)*

**1. Input** — Slide 6, an organelle recap: *"Mitochondria — the powerhouse of the cell. They make energy for everything the cell does."* Teacher's stated intent (intake): a fast recap of organelle functions before an exam-style plenary; focus weakness flagged as "class rushes the recall questions".

**2. Editor reasoning** — Three lenses fired. **Spec-vocabulary lens** (`../reference/spec/3.2-cell-structure.md` §1, `AQA 3.2.1 — ATP not "energy"`): AQA credits *ATP*; *"energy"* for mitochondrial function is an **explicit reject**. **Examiner-insight lens** (`EI-1`): vocabulary substitution is single-mark testable and reliably lost — "energy" is the archetype. **Exam-question lens** (`../reference/exam-questions/cell-structure.md`): this topic is 66% KNOWLEDGE marks, where precise organelle vocabulary is the mark. Checked the slide caption against the credit-vocabulary list; the model the class will copy uses the rejected term. **Principle lens** (`Rosenshine 4 — Provide models`): a model that embeds GCSE phrasing teaches the class the exact answer the mark scheme rejects. Severity judged **MAJOR** not CRITICAL — it will measurably lose a mark and undercuts the slide's own purpose, but it does not reverse a concept (mitochondria *are* central to energy supply); the editor does not inflate.

**3. Finding and rationale** — surfaced (not left) because it sits on the exact slide the teacher built to fix recall, so the flaw undercuts the teacher's own stated goal. Handed back as:

```
SEVERITY: MAJOR
SLIDE: 6
QUOTE: "Mitochondria — the powerhouse of the cell. They make energy for everything the cell does."
PRINCIPLE: Rosenshine 4 — Provide models
SPEC: AQA 3.2.1 — ATP not "energy" (EI-1)
WHY: This recap is the last organelle model the class sees before the plenary it is meant to prepare them for; if the model says "energy", they will write "energy" in the KNOWLEDGE questions, where "energy" is an explicit reject and "ATP" is the only credited term.
QUESTION: This slide is the final model the class copies before they answer — how will you make sure they leave with "ATP" rather than the "energy" phrasing most of them arrive with from GCSE?
```

**4. Training-layer impact** — Written to `training-layer/<teacher-id>.md`: *"Recap slides carry GCSE-carryover vocabulary ('energy' for ATP; 'controls the cell' for the nucleus). Vocabulary precision on organelle function is a recurring blind spot — check function captions against the credit-vocabulary list."*

**5. Future-sample benefit** — Next deck from this teacher, the editor checks organelle-function captions against the credit-vocabulary list **first**, because rejected-term carryover is this teacher's known pattern — so the same class-level mark loss is caught on slide one, not re-derived from scratch.

---

## How rows are added (not here — in M4)

1. A review runs against a deck. `extract.py` produces the slide manifest; the editor produces the critique; `check.py` clears it.
2. Each finding becomes one run-level row (`runs/<teacher-id>/<date>/training-table.md`), labelled `CONSTRUCTED`.
3. Column 4 of each row is folded into `training-layer/<teacher-id>.md` — the accretion step.
4. The next run reads the teacher file first, so column 5's promised benefit is realised.

*Rows come from the run, so they cannot drift from it. Schema per `plan.md` §5; finding shape per `../reference/finding-schema.md`; labels per `spec.md`.*
