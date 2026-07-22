# hod-review

**An editor that reviews A-level Science lesson PowerPoints — scoped to AQA A-level
Biology — the way a Head of Department reads your deck before Monday morning. It
points at what will fail with your class and hands it back. It never rewrites your
lesson.**

> **Build status: COMPLETE (manifests M1–M5).** The editor, the code gate, the bespoke
> AQA reference layer, a constructed validation run with an answer key, blind runs in
> fresh chats, the populated accretion layer, and the ship layer (judge guide, examples,
> claims audit) are all in place. Built by a manifest-driven pipeline
> (see [`build/plan.md`](build/plan.md)); the [manifest status](#build-status) table below
> says exactly what shipped. Every headline claim here maps to something a fresh clone can
> run — see [`JUDGE_GUIDE.md`](JUDGE_GUIDE.md).

---

## What it is

You hand over a lesson deck (`.pptx`) and a little context. The editor reads it as a
senior colleague would — against how learning works, against what the AQA
specification asks, and against the questions the content is actually examined by —
and hands back a set of **findings**. Each finding points at one slide, quotes it,
names what is wrong and why, and ends in a **question you have to answer**. It does
not write the fix. The fix is your teaching, and your teaching is yours to own.

See [`editor/identity.md`](editor/identity.md) for who the editor is and why it reads this way.

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

Where the single-source citation is the field bar (per the competitor review in
[`build/communitycompetitions.md`](build/communitycompetitions.md)), every finding here can
anchor to three, which is what turns critique from opinion into something a teacher cannot
argue with:

1. **The pedagogical principle** — Rosenshine, cognitive load, retrieval and spacing,
   EEF (`editor/reference/frameworks/`).
2. **The AQA spec point** the slide serves or misses, plus the examiner insight and
   common misconceptions for that topic (`editor/reference/spec/`).
3. **The real exam question** the content is assessed by (`editor/reference/exam-questions/`).

A finding needs at least one of principle or spec; on the validated topic it can carry
all three.

## The finding shape

Each finding has exactly these fields (full definition in
[`editor/reference/finding-schema.md`](editor/reference/finding-schema.md), manifest M2):

- **SLIDE** — the slide number, from the extracted manifest.
- **QUOTE** — the exact wording from that slide, verbatim (gate-checked against the extract).
- **PRINCIPLE** — the pedagogical principle at stake.
- **SPEC** — the AQA spec point or required practical.
- **WHY** — why it will fail with a class, specific to this lesson.
- **QUESTION** — the question handed back to the teacher. Never a fix.

Findings are severity-ordered. A clean slide produces no finding; the editor does not
invent findings to look busy.

## The binary-input wedge

Where comparable editors in the field review reviewed pasted text
([`build/communitycompetitions.md`](build/communitycompetitions.md)), this one ingests a real
`.pptx` through a **deterministic** extractor (`extract.py`, python-pptx, manifest M3) and then
quote-checks every finding against the extracted slide text. Slide anchoring and
verbatim-quote matching are exactly the kind of work that must never run on model
diligence, so they run in code — which you can watch: the shipped blind critiques clear the
gate against a freshly extracted manifest, so every quote is verified verbatim on the real
deck.

## A reproducible system, not a clever prompt

The rules live in the `editor/` folder, not in a prompt you have to remember, so the same
folder gives the same structured output across chats. The repo ships the proof:
[`runs/blind-01/`](runs/blind-01/2026-07-22/) contains **two independent reads of the same
deck from two separate chats** — same schema, same worst-first ordering, and **every
high-severity finding identical**: the same three CRITICAL findings and the same MAJOR core,
on the same slides and anchors. The two reads differ only at the margins — which lower-priority
points each surfaced, and one extra finding one read made. That is the honest shape of the
claim: the structure is reproducible; the last word of judgement is not identical, and should
not be. You can reproduce it yourself — see [`JUDGE_GUIDE.md`](JUDGE_GUIDE.md) Level 3.

## How you use it

**Drop the [`editor/`](editor/) folder into a Claude project, give it a lesson deck, and
ask for a review.** The editor is a self-contained markdown folder (`identity.md`,
`rules.md`, `examples.md`, and everything under `reference/` — all inside `editor/`,
pointing at nothing outside it). A stranger drops it in and Claude *becomes* the Head of
Department. This is the entry — not a website, not an app.

The editor reads **slide text**. You give it that text one of two ways:

- **Attach the `.pptx`** to the Claude project and let Claude read the slides directly — the
  quickest path.
- **Run [`extract.py`](extract.py)** on the deck for a reproducible slide manifest (slide
  number + verbatim text per slide) and paste or attach that. This is deterministic, so the
  same deck always yields the same manifest — and it is what the code gate quote-checks
  findings against.

**Run it in Claude Code** and the Python gate genuinely executes: `extract.py` turns a deck
into a manifest, and [`check.py`](check.py) blocks any output that rewrites a slide,
fabricates a quote, drops an anchor, or ends in a fix instead of a question. Any `docs/`
surface is a demonstration only, never the entry.

## Honesty note — the runs are constructed

Every run in `runs/` is a **deliberately constructed demonstration case**, not a real
teacher's lesson. There is no real teacher, deck, or lesson in this build. Every artifact
says so, in that word. The training table labels its rows `CONSTRUCTED`, never `REAL`; a
genuine teacher run is named as a next step in [`OPEN-DEFECTS.md`](OPEN-DEFECTS.md), not
implied to be done.

Two honest gradations within that. The `s-whitfield` run is a **self-consistency test** —
the same author built the seeded deck and wrote the answer key, so its 9/9 score proves the
*mechanism*, not blind precision. The **blind runs** (`blind-01`, `blind-02`) are the harder
evidence: the editor reading decks it was not built around, in fresh chats, still producing
anchored, fabrication-checked, no-rewrite findings that clear the gate. See
[`writeup.md`](writeup.md) for the full framing.

## Repo layout

```
hod-review/
  README.md                          # this file
  editor/                            # THE EDITOR — self-contained; drops into a Claude project alone
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
  extract.py                         # pptx -> slide manifest (M3)
  check.py                           # the blocking gate (M3)
  tests/
    cases/  negative/  verify.py     # the self-tested harness (M3)
  .github/workflows/verify.yml       # CI (M3)
  runs/                              # shipped evidence (M4)
    s-whitfield/<date>/              #   the constructed run: seeded deck + answer key + 9/9 score
    blind-01/<date>/                 #   a blind deck read TWICE in separate chats (consistency check)
    blind-02/<date>/                 #   a second blind deck, read cold
  training-layer/                    # the populated accretion layer (M2.5 + M4)
  JUDGE_GUIDE.md  OPEN-DEFECTS.md  writeup.md   # ship layer (M5): verify path, honest holes, build story
  docs/                              # optional demo surface only
  build/                             # the build record — not part of the shipped editor
    plan.md  spec.md  brainwave.md  communitycompetitions.md   # the seed files
    handover/                        # per-manifest completion records
    reviews/                         # manifest-review evidence (REVIEW-M3.md)
```

## How this repo is built

The four seed files — [`build/plan.md`](build/plan.md),
[`build/communitycompetitions.md`](build/communitycompetitions.md), [`build/spec.md`](build/spec.md),
[`build/brainwave.md`](build/brainwave.md) — are authored by hand and carry the decisions and the
reasoning. Everything downstream is executed by Claude Code prompts that read all four
first and run the manifests in `build/plan.md`, each ending in a `build/handover/` file the next
one waits on. The build process is itself an ICM demonstration.

### Build status

| Manifest | Scope | State |
|---|---|---|
| **M1** | Research + scaffold: skeleton, `identity.md`, README skeleton | ✅ complete |
| **M2** | Substance: `rules.md`, frameworks, finding schema | ✅ complete |
| **M2.5** | Bespoke AQA corpus layer + training-table schema | ✅ complete |
| **M3** | Enforcement: `extract.py`, `check.py`, tests, CI | ✅ complete |
| **M4** | Validation: the constructed run, receipts, populated training table | ✅ complete |
| **M5** | Ship: examples, judge guide, claims audit, writeup | ✅ complete |

Each manifest ended by writing a handover file in [`build/handover/`](build/handover/) that
the next one read first. See [`build/plan.md`](build/plan.md) for the full pipeline and
[`build/communitycompetitions.md`](build/communitycompetitions.md) for the bar this is built to
beat. The build itself — staged jobs, each with one goal and a handover — is an
interpretable-context-methodology demonstration; the full story is in
[`writeup.md`](writeup.md).

## Out of scope

- No rewriting, drafting, or replacement content, ever.
- No question generation — the exam-question layer is distilled reference, not a generator.
- No website as the entry — any `docs/` surface is demonstration only.
- No subjects beyond A-level Biology in this version. The reference layer scaffolds the
  full AQA A-level Biology topic map (3.1–3.8) with one topic (3.2.1 Cell structure) built
  to full depth; every other topic is scope-only until a lesson on it is reviewed. Wider
  Science is a possible future direction, not something this build ships.
