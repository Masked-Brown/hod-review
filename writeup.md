# writeup.md — the build story and the case for the entry

## The angle, in one line

**An editor that critiques an A-level Biology lesson and hands the fixing back — and never
rewrites it, because the no-rewrite rule is enforced in code, not asked for in prose.**

The competition's highest-weighted criterion is whether the editor *critiques* rather than
rewrites, summarises, or praises. Lesson slides beg to be rewritten — the instant a review
writes "here's a better starter," it has failed the angle. So the rule that carries the whole
entry is not a line in a markdown file we hope the model obeys; it is an invariant a blocking
gate ([`check.py`](check.py)) enforces mechanically. A *must* in a markdown file is a request;
a *must* in code is a constraint.

The persona is what makes that constraint feel correct rather than restrictive. The editor is
a **Head of Department doing the read-through before Monday morning**: a senior colleague reads
your deck, points at the slides that will fail with your class, and hands it back — in time to
fix, then goes home. A HoD who rewrites your lesson has taught you nothing and taken your class
off you; the pedagogy is yours to own. Every UK teacher knows this read, so the boundary is
instantly legible and instantly justified. See [`editor/identity.md`](editor/identity.md).

## The differentiators, with evidence

Three things separate this from a prose-only review tool. Each is shipped, not described.

**1. Enforcement in code.** The one guarantee lives in a self-tested gate, not in hope.
`check.py` reads a critique plus the slide manifest and fails (exit 1) on a rewrite pattern, a
missing slide anchor, a fabricated quote, a finding citing neither principle nor spec, or an
output that ends in a fix instead of a question. It is proven **both directions** — it clears
every clean critique and blocks every broken one on its exact named check — by
[`tests/verify.py`](tests/verify.py) and nine deliberately-broken fixtures in
[`tests/negative/`](tests/negative/), because "a checker that passes everything proves
nothing." CI runs it on every push ([`.github/workflows/verify.yml`](.github/workflows/verify.yml)).
*Evidence:* `python tests/verify.py` → `21/21 assertions passed`; `python check.py --selftest`
→ `1/1 clean cleared, 8/8 bad blocked`.

**2. A binary input nobody else in the field touches.** Every comparable entry reviews pasted
text. This one ingests a real `.pptx` through a **deterministic** extractor
([`extract.py`](extract.py), python-pptx) and then quote-checks every finding against the
extracted slide text. Slide anchoring and verbatim-quote matching are exactly the kind of work
that must never run on model diligence, so they run in code — this is claimline's fabrication
check (every quoted passage must appear in the source), applied to an artifact no one else in
the field works with. *Evidence:* the blind critiques clear the gate against a **freshly
extracted** manifest — `python extract.py runs/blind-02/2026-07-22/blind-lesson.pptx -o m.md &&
python check.py runs/blind-02/2026-07-22/blind02-edit-output-test.md m.md` → `PASS — 10
finding(s)`. Every quote is verified verbatim on the real deck.

**3. Triple-source citations.** The field bar cites one source per finding (a regulation). Each
finding here can anchor to three: the **pedagogical principle** (Rosenshine, cognitive load,
retrieval, EEF — [`editor/reference/frameworks/`](editor/reference/frameworks/)), the **AQA
spec point** the slide serves or misses plus the topic's examiner-insight and misconceptions
([`editor/reference/spec/`](editor/reference/spec/)), and the **real exam question** the content
is assessed by ([`editor/reference/exam-questions/`](editor/reference/exam-questions/)). That is
what turns critique from opinion into something a teacher cannot argue with: not "I think this
starter is weak" but "this skips the worked model Rosenshine calls for, and AQA pays the unit
conversion in exam Q7 as its own mark." *Evidence:* finding on slide 11 of the constructed run,
anchored to `Rosenshine 4 — Provide models` **and** `AQA 3.2.1 — exam Q7`
([`editor/examples.md`](editor/examples.md) §2). The reference layer is deep on the one
validated topic (3.2.1 Cell structure) and scaffolded across the 8-topic structure — depth
shown on a real run over shipped bulk.

**4. A populated accretion layer.** The field's most-punished miss was the empty memory —
everyone designed a learning loop, almost nobody shipped one with real rows. The five-column
training table ([`runs/s-whitfield/2026-07-22/training-table.md`](runs/s-whitfield/2026-07-22/training-table.md))
carries one row per finding, exposing the reasoning chain, and its column 4 is folded into a
cross-run teacher profile ([`training-layer/s-whitfield.md`](training-layer/s-whitfield.md))
that makes the *next* read of that teacher sharper — leading with the credit-vocabulary scan
that fired three times, checking explanation slides for reversed concepts the teacher did not
flag. Every row is labelled `CONSTRUCTED`, never `REAL`.

## The consistency finding

The reproducibility claim is the one that matters most, and it is the one a judge can confirm
by their own hand (Level 3 of [`JUDGE_GUIDE.md`](JUDGE_GUIDE.md)). The evidence for it is
shipped: [`runs/blind-01/2026-07-22/`](runs/blind-01/2026-07-22/) contains **two independent
reads of the same deck**, produced in two separate Claude chats
([`blind-edit-output-test-1.md`](runs/blind-01/2026-07-22/blind-edit-output-test-1.md),
[`blind-edit-output-test-2.md`](runs/blind-01/2026-07-22/blind-edit-output-test-2.md)).

Both reads produced the **same structure**: the finding schema, worst-first severity ordering,
the same three CRITICAL findings on the same slides and the same anchors (the prokaryote
list-rule on slide 6, magnification-for-resolution on slide 8, the two-point uncertainty value
on slide 11), and the same MAJOR core on slides 4 and 7. The exact set of MINOR findings
differs between the two chats — one read flagged the missing diagram, the other flagged the
narrow exam-format coverage.

That difference is not a defect; it is the honest shape of the claim. **The structure is
reproducible because the rules live in the folder, not in a prompt someone has to remember —
the same `editor/` folder gives the same anchored, no-rewrite output across chats. The last
word or two of judgement varies between two careful readers, exactly as it should.** A tool
that claimed byte-identical output would be claiming something a human HoD could not do either.
Both blind reads also clear the code gate against a freshly-extracted manifest, so the
consistency is in genuine, fabrication-checked findings, not in boilerplate.

## The honesty

The strongest thing this entry can do for its own credibility is to state what it has **not**
shown.

- **The main validation run is a constructed self-consistency test, not a blind trial.** The
  same author built the seeded deck and the critique, so the 9/9 answer-key score
  ([`build/handover/MANIFEST-4-COMPLETE.md`](build/handover/MANIFEST-4-COMPLETE.md)) proves the
  *mechanism* and the *discipline* end to end — it does not, by itself, measure blind precision.
  The run's own files say so, in the word "constructed."
- **The blind runs are the harder evidence** — the editor reading decks it was not built around
  — and they are where the reproducibility and fabrication-free claims are actually earned.
- **No genuine teacher run exists yet.** There is no real teacher, deck, or lesson anywhere in
  this build. A `REAL` run — a real teacher on a real lesson — is a reserved next step, named in
  [`OPEN-DEFECTS.md`](OPEN-DEFECTS.md) §3, not implied to be done. The training table has no
  `REAL` rows and will not until that run happens.

The gate's limits are logged with the same candour: it checks form, not pedagogical
correctness, and its rewrite scan is heuristic — a silently pasted re-authoring with no
give-away phrase can slip it, with the verbatim-quote and ends-in-a-question checks as the
structural backstop ([`OPEN-DEFECTS.md`](OPEN-DEFECTS.md) §1–§2). Every headline claim in the
README maps to something a fresh clone can run; the ones that could not were cut (the M5 claims
audit).

## How the repo was built — the methodology is the artifact

The build itself is an interpretable-context-methodology demonstration. Four seed files
([`build/plan.md`](build/plan.md), [`build/spec.md`](build/spec.md),
[`build/brainwave.md`](build/brainwave.md),
[`build/communitycompetitions.md`](build/communitycompetitions.md)) were authored by hand and
carry the decisions and the reasoning. Everything downstream was executed by staged Claude Code
manifests, each with one goal and a handover file the next one waits on:

| Manifest | Job | Handover |
|---|---|---|
| **M1** | Research + scaffold: skeleton, persona, README skeleton | [`MANIFEST-1-COMPLETE.md`](build/handover/MANIFEST-1-COMPLETE.md) |
| **M2** | Substance: `rules.md`, frameworks, finding schema — every rule justified | [`MANIFEST-2-COMPLETE.md`](build/handover/MANIFEST-2-COMPLETE.md) |
| **M2.5** | The bespoke AQA reference layer + training-table schema | [`MANIFEST-2.5-COMPLETE.md`](build/handover/MANIFEST-2.5-COMPLETE.md) |
| **M3** | Enforcement: `extract.py`, `check.py`, tests, CI | [`MANIFEST-3-COMPLETE.md`](build/handover/MANIFEST-3-COMPLETE.md) |
| **M4** | Validation: the constructed run, receipts, populated training table | [`MANIFEST-4-COMPLETE.md`](build/handover/MANIFEST-4-COMPLETE.md) |
| **M5** | Ship: examples, judge guide, claims audit, this writeup | this manifest |

The scored substance (rules, reference, examples) was authored and curated by hand because
loose generation drifts and a drifted example teaches the drift; everything else was handed to
prompts that read the full reasoning first and ran on a manifest loop. There is exactly **one
human gate**, between M4 and M5: M5 hardens the claims the run's substance supports, so the
human reviewed the rules, the reference layer, and the run before the ship layer was released.
Handovers flag disagreements rather than silently overriding the seed files — a logged
divergence is a contribution; a silent override is a defect.

## The intellectual lineage — what this inherits and what it adds

This entry answers a field. It **matches** the favourite's stack (claimline): findings that
quote verbatim and cite the exact rule and never rewrite; a self-tested harness with negative
tests that verify the verifier; CI on every push; a judge guide with a fast no-install verify;
an honest open-defects file; and a rewrite-bait test the editor must refuse three times while
still reviewing. It inherits the wider field's hardest-won lessons: **receipts** over polished
simulation (a run shipped in full as evidence — the single most-rewarded axis), a **populated**
accretion layer over a designed-but-empty one (the most-punished miss), and deterministic work
pinned in code over model diligence.

What it **adds** that no one in the #9 field had done: a **binary PowerPoint input** with the
fabrication check applied to extracted slide text, and **triple-source citations** where the
bar cited one. Both of those are depth axes taken a layer further than the field, on a domain
narrow enough to be a genuine specialism — one exam board, one subject, one topic built to full
depth. That was the opening, and this entry is built to take it.

---

*Full pipeline and rationale: [`build/plan.md`](build/plan.md) and
[`build/brainwave.md`](build/brainwave.md). The bar this was built to beat:
[`build/communitycompetitions.md`](build/communitycompetitions.md). How to verify every claim
above from a fresh clone: [`JUDGE_GUIDE.md`](JUDGE_GUIDE.md).*
