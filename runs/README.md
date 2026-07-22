<!-- STUB · scaffolded by M1 (skeleton). Owner: M4. -->

# runs/

**Status:** stub directory — no runs yet.
**Owner:** manifest **M4** (validation and receipts).
**Purpose:** the shipped evidence of a review. Each run lives at
`runs/<teacher-id>/<date>/` and contains:

- `slide-manifest.md` — output of `extract.py` on the deck;
- `critique.md` — the editor's findings;
- `rewrite-bait-exchange.md` — the three escalating rewrite requests, all refused;
- `expected-findings.md` — the answer key: every seeded flaw and its reference anchor;
- `training-table.md` — the five-column table, rows labelled `CONSTRUCTED`.

**Honesty invariant (from `spec.md` and `plan.md` §3/§7):** the M4 run is a
deliberately **constructed** demonstration case — no real teacher, deck, or lesson.
Every artifact here states so, using the word "constructed". The `<teacher-id>`
names a fictional persona used only to drive intake.
