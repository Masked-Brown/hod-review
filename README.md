# hod-review

**An editor that reviews A-level Science lesson PowerPoints — scoped to AQA A-level
Biology — the way a Head of Department reads your deck before Monday morning. It
points at what will fail with your class and hands it back. It never rewrites your
lesson.**

> **Build status: SKELETON (manifest M1 complete).**
> This repo is being built by a manifest-driven pipeline (see [`plan.md`](plan.md)).
> The structure and the persona are in place; the scored substance and the code gate
> are authored by later manifests. The [manifest status](#build-status) table below
> says exactly what is shipped and what is pending — nothing here claims to work that
> does not yet exist.

---

## What it is

You hand over a lesson deck (`.pptx`) and a little context. The editor reads it as a
senior colleague would — against how learning works, against what the AQA
specification asks, and against the questions the content is actually examined by —
and hands back a set of **findings**. Each finding points at one slide, quotes it,
names what is wrong and why, and ends in a **question you have to answer**. It does
not write the fix. The fix is your teaching, and your teaching is yours to own.

See [`identity.md`](identity.md) for who the editor is and why it reads this way.

## Who it is for

A-level Biology teachers preparing lessons, and the Heads of Department who would
otherwise do this read by hand. The domain is deliberately narrow — one exam board,
one subject — because a review that is specific is a review that is useful.

## The one invariant

**Every output is a set of findings, each ending in a question. The editor never
supplies replacement slide content, rewritten prose, or a "fixed" version.**

This is the whole angle, so it is not left to prose the model might drift from — it
is enforced mechanically by a code gate (`check.py`, manifest M3). A *must* in a
markdown file is a request; a *must* in code is a constraint.

## How it works — the triple anchor

Where most review tools cite one thing (or nothing), every finding here can anchor to
three, which is what turns critique from opinion into something a teacher cannot
argue with:

1. **The pedagogical principle** — Rosenshine, cognitive load, retrieval and spacing,
   EEF (`reference/frameworks/`).
2. **The AQA spec point** the slide serves or misses, plus the examiner insight and
   common misconceptions for that topic (`reference/spec/`).
3. **The real exam question** the content is assessed by (`reference/exam-questions/`).

A finding needs at least one of principle or spec; on the validated topic it can carry
all three.

## The finding shape

Each finding has exactly these fields (full definition in
[`reference/finding-schema.md`](reference/finding-schema.md), manifest M2):

- **SLIDE** — the slide number, from the extracted manifest.
- **QUOTE** — the exact wording from that slide, verbatim (gate-checked against the extract).
- **PRINCIPLE** — the pedagogical principle at stake.
- **SPEC** — the AQA spec point or required practical.
- **WHY** — why it will fail with a class, specific to this lesson.
- **QUESTION** — the question handed back to the teacher. Never a fix.

Findings are severity-ordered. A clean slide produces no finding; the editor does not
invent findings to look busy.

## The binary-input wedge

Every comparable editor reviews pasted text. This one ingests a real `.pptx` through a
**deterministic** extractor (`extract.py`, python-pptx, manifest M3) and then
quote-checks every finding against the extracted slide text. Slide anchoring and
verbatim-quote matching are exactly the kind of work that must never run on model
diligence, so they run in code.

## How you use it

Two surfaces, one editor:

- **Drop the folder into a Claude project.** The editor is a plain markdown folder
  (`identity.md`, `rules.md`, `reference/`). A stranger drops it in and Claude
  *becomes* the Head of Department. This is the entry.
- **Run it in Claude Code.** Here the Python gate genuinely executes: `extract.py`
  turns a deck into a slide manifest, and `check.py` blocks any output that rewrites,
  fabricates a quote, or drops its anchor.

Any `docs/` surface is a demonstration only, never the entry. The editor is the
folder.

_Exact steps land with the ship layer (`JUDGE_GUIDE.md`, manifest M5)._

## Honesty note — the validation run is constructed

The validation run shipped in `runs/` is a **deliberately constructed demonstration
case**, not a real teacher's lesson. There is no real teacher, deck, or lesson in this
build. Every artifact says so, in that word. The training table labels its rows
`CONSTRUCTED`, never `REAL`; a genuine teacher run is named as a next step in
`OPEN-DEFECTS.md`, not implied to be done.

## Repo layout

```
hod-review/
  README.md                        # this file
  identity.md                      # who the editor is (the HoD persona)
  rules.md                         # how it critiques (M2)
  examples.md                      # worked findings, generated from the M4 run (M5)
  reference/
    frameworks/                    # pedagogy, our words + citations (M2)
      rosenshine.md  cognitive-load.md  retrieval-practice.md  eef-guidance.md
    spec/                          # AQA content index, deep on the validated topic (M2.5)
      aqa-biology-index.md  3.2-cell-structure.md
    exam-questions/                # distilled real questions (M2.5)
      cell-structure.md
    finding-schema.md              # the finding contract (M2)
  extract.py                       # pptx -> slide manifest (M3)
  check.py                         # the blocking gate (M3)
  tests/
    cases/  negative/  verify.py   # the self-tested harness (M3)
  .github/workflows/verify.yml     # CI (M3)
  runs/<teacher-id>/<date>/        # the constructed run, shipped as evidence (M4)
  training-layer/                  # the populated accretion layer (M2.5 + M4)
  JUDGE_GUIDE.md  OPEN-DEFECTS.md  writeup.md   # ship layer (M5)
  docs/                            # optional demo surface only
  plan.md  communitycompetitions.md  spec.md  brainwave.md   # the seed files
```

## How this repo is built

The four seed files — [`plan.md`](plan.md),
[`communitycompetitions.md`](communitycompetitions.md), [`spec.md`](spec.md),
[`brainwave.md`](brainwave.md) — are authored by hand and carry the decisions and the
reasoning. Everything downstream is executed by Claude Code prompts that read all four
first and run the manifests in `plan.md`, each ending in a `handover/` file the next
one waits on. The build process is itself an ICM demonstration.

### Build status

| Manifest | Scope | State |
|---|---|---|
| **M1** | Research + scaffold: skeleton, `identity.md`, README skeleton | ✅ complete |
| **M2** | Substance: `rules.md`, frameworks, finding schema | ⬜ pending |
| **M2.5** | Bespoke AQA corpus layer + training-table schema | ⬜ pending |
| **M3** | Enforcement: `extract.py`, `check.py`, tests, CI | ⬜ pending |
| **M4** | Validation: the constructed run, receipts, populated training table | ⬜ pending |
| **M5** | Ship: examples, judge guide, open-defects, claims audit | ⬜ pending |

Files marked with a manifest above are stubs until that manifest runs; each stub names
its owner. See [`plan.md`](plan.md) for the full pipeline and
[`communitycompetitions.md`](communitycompetitions.md) for the bar this is built to
beat.

## Out of scope

- No rewriting, drafting, or replacement content, ever.
- No question generation — the exam-question layer is distilled reference, not a generator.
- No website as the entry — any `docs/` surface is demonstration only.
- No subjects beyond A-level Biology in this version (the structure scaffolds toward
  wider Science; the depth is Biology).
