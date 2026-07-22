# MANIFEST 4 — COMPLETE

status: complete-with-questions

summary: Proved the editor on a deliberately **constructed**, honestly-labelled validation
run and shipped the whole run as evidence under `runs/s-whitfield/2026-07-22/`. Built a
fictional teacher persona and a 12-slide seeded AQA 3.2.1 Cell-structure deck (a real `.pptx`
via python-pptx) mixing clean slides with 8 named flaws that map to specific `editor/reference/`
entries; wrote the answer key; ran `extract.py` → manifest, produced the editor's 9-finding
critique, and cleared `check.py` (exit 0, 0 violations, 0 advisory warnings) **on the first
run**. Captured the rewrite-bait exchange (three escalating pushes, all refused with the domain
reason while the review continued), populated the five-column training table with 9 `CONSTRUCTED`
rows, appended the accreted persona profile, and ran a **cold** second deck (cell fractionation —
the area the main lesson skipped) that the editor read correctly on unseen anchors. Every seeded
flaw was caught on its intended anchor; every clean slide was left alone; no finding was
manufactured. M5 was **not** started — it waits on the human review gate (`plan.md` §4).

files-created:
- `runs/s-whitfield/2026-07-22/persona.md` — the fictional teacher persona (labelled
  `CONSTRUCTED`), with class context, one stated focus weakness (vocabulary precision), and the
  intake fields the editor works from.
- `runs/s-whitfield/2026-07-22/build_lesson.py` — deterministic python-pptx builder for the main
  deck; committed so the deck's exact wording (the fabrication-check ground truth) is auditable
  and reproducible.
- `runs/s-whitfield/2026-07-22/lesson.pptx` — the 12-slide seeded demonstration deck (4 clean, 8
  seeded flaws across 7 slides).
- `runs/s-whitfield/2026-07-22/slide-manifest.md` — `extract.py` output over `lesson.pptx`.
- `runs/s-whitfield/2026-07-22/expected-findings.md` — the answer key: every seeded flaw, its
  slide, verbatim text, reference anchor, expected severity; plus the 4 clean slides as
  expected-negatives so false positives are scoreable.
- `runs/s-whitfield/2026-07-22/critique.md` — the editor's read: 9 findings, worst-first
  (1 CRITICAL, 6 MAJOR, 2 MINOR), each anchored and ending in a question.
- `runs/s-whitfield/2026-07-22/gate-pass.txt` — the `check.py` PASS receipt (human + `--json` +
  exit code + the "no fix was needed" note).
- `runs/s-whitfield/2026-07-22/rewrite-bait.md` — the three-escalation refusal exchange.
- `runs/s-whitfield/2026-07-22/training-table.md` — the five-column run-level table, 9
  `CONSTRUCTED` rows.
- `runs/s-whitfield/2026-07-22/build_cold.py`, `cold-lesson.pptx`, `cold-manifest.md`,
  `cold-critique.md`, `cold-run.md` — the cold-run deck, its manifest, its 2-finding critique
  (gate PASS), and the consolidated cold-run deliverable + mini answer key.
- `training-layer/s-whitfield.md` — the accreted persona profile (4 recurring blind spots folded
  from column 4 of the training table), labelled `CONSTRUCTED`.
- `build/handover/MANIFEST-4-COMPLETE.md` — this file.

files-changed:
- **None of the seed files, the editor (`editor/`), the gate (`check.py`, `extract.py`), the
  tests, or the README were modified.** M4 is additive: it consumes the M2/M2.5 reference layer
  and the M3 gate and produces run evidence under `runs/` and `training-layer/`.
- `OPEN-DEFECTS.md` was **not** changed — its defect 3 ("No real teacher run exists — the M4 run
  is a constructed demonstration") was already created by M3 and already discharges M4's guardrail
  that the missing genuine-teacher run be logged as a next step. Verified present; no edit needed.
- The `README.md` build-status table still shows M3/M4 as pending. **Left untouched on purpose:**
  the README claims audit is M5's job (`plan.md` §M5), and M4 does not pre-empt it. Flagged in
  open-questions.

## The seeded-flaw → outcome map (the required table)

Scored `critique.md` against `expected-findings.md`. **Caught** = the editor produced a finding on
the seeded flaw's slide, on its intended reference anchor, at the expected severity. **Missed** =
no such finding. **Added** = a finding not in the answer key (a false positive if on a clean slide).

| # | Seeded flaw | Slide | Anchor (expected) | Expected sev | Editor's result | Caught / Missed / Added |
|---|---|---|---|---|---|---|
| F1 | Starter copies new content, no retrieval | 2 | `Rosenshine 1 — Daily review` | MAJOR | MAJOR, `Rosenshine 1 — Daily review` | **CAUGHT** |
| F2 | Cell fractionation skipped | 3 | `SPEC AQA 3.2.1 — cell fractionation` | MINOR | MINOR, `AQA 3.2.1 — cell fractionation` | **CAUGHT** |
| F3 | "Mitochondria produce energy" | 5 | `SPEC AQA 3.2.1 — ATP not "energy"` (EI-1) | MAJOR | MAJOR, `AQA 3.2.1 — ATP not "energy"` | **CAUGHT** |
| F4 | Nucleus "controls all activities" | 6 | `SPEC AQA 3.2.1 — EI-7` | MAJOR | MAJOR, `AQA 3.2.1 — EI-7` | **CAUGHT** |
| F5 | Prokaryote list, universal+non-universal mixed | 8 | `SPEC AQA 3.2.1 — EI-2` | MAJOR | MAJOR, `AQA 3.2.1 — EI-2` | **CAUGHT** |
| F6a | Acellular/non-living fused | 9 | `SPEC AQA 3.2.1 — EI-3` | MAJOR | MAJOR, `AQA 3.2.1 — EI-3` | **CAUGHT** |
| F6b | "genetic information" (reject term) | 9 | `SPEC AQA 3.2.1 — genetic material not "information"` | MINOR | MINOR, `AQA 3.2.1 — genetic material not "information"` | **CAUGHT** |
| F7 | Magnification written for resolution | 10 | `SPEC AQA 3.2.1 — EI-5` | CRITICAL | CRITICAL, `AQA 3.2.1 — EI-5` | **CAUGHT** |
| F8 | Calculation, no worked model | 11 | `Rosenshine 4 — Provide models` + `exam Q7` | MAJOR | MAJOR, both anchors | **CAUGHT** |
| — | Clean slides 1, 4, 7, 12 | — | *no finding* | — | no finding on any | **no false positive** |

**Score: 9/9 seeded flaws caught, on-anchor, at expected severity. 0 missed. 0 findings added
(0 false positives on the 4 clean slides).** The two-flaws-on-one-slide case (F6a + F6b, slide 9)
was held as **two distinct findings**, not collapsed (`rules.md` R8).

**Cold run (`cold-run.md`):** 2/2 seeded flaws caught (C1 slide 2 `cold/isotonic/buffered`; C2
slide 3 `EI-6`), 0 false positives on its 2 clean slides — on reference anchors the main run never
used, so the read generalises rather than being tuned to one deck.

**Honest reading of the perfect score.** This is a **constructed self-consistency test**: the same
author built the deck and the critique, so full recall is expected and does not, on its own,
measure blind precision. What the 9/9 (+2/2 cold) genuinely demonstrates is the **mechanism** end
to end (seeded flaw → reference anchor → finding → gate → answer-key score → accreted pattern), the
finding **form** (gate-verified: anchored, fabrication-free, rewrite-free, ends in a question), the
**discipline** (distinct weaknesses kept distinct; clean slides left alone; a MINOR left as a
question, not inflated), and **generalisation** to an unseen deck. The blind trial — a real teacher
on a real deck — is the reserved `REAL` run named in `OPEN-DEFECTS.md` §3, and is deliberately not
claimed here.

decisions-made:
1. **Persona id `s-whitfield`, run date `2026-07-22`, pronouns they/them, declared constructed on
   every artifact.** Justification: `plan.md` §M4 and `spec.md` require a fictional persona used
   only to drive intake, honestly labelled with the word "constructed". A neutral, clearly-invented
   persona with stated pronouns avoids implying a real individual and avoids a pronoun guess.
2. **One stated focus weakness = vocabulary precision (GCSE carryover), deliberately
   under-scoped.** Justification: the plan asks for "one stated focus weakness"; making it *partly*
   right (real, but narrower than the deck's actual problems) lets the run show the editor reading
   *past* the teacher's self-diagnosis (the CRITICAL misconception F7 and the skipped spec F2 were
   never flagged by the persona), and gives the accretion layer a genuine "wider than self-diagnosis"
   pattern to log.
3. **12-slide deck, 4 clean / 8 seeded, spanning the three required flaw types.** Justification:
   `plan.md` §M4 requires a misconception reinforced (F7, EI-5, the CRITICAL), a spec point skipped
   (F2, cell fractionation), and an assessed format never rehearsed (F8, exam Q7 unit conversion),
   plus "some slides genuinely clean so the editor is seen NOT flagging good work" (slides 1/4/7/12).
   The extra EI-coded/vocabulary flaws (F3/F4/F5/F6a/F6b) exercise the content, examiner-insight and
   assessment anchors together and make the vocabulary pattern recur three times so it can accrete.
4. **Deck built in ASCII (straight quotes, hyphens), from a committed builder script.**
   Justification: `check.py`'s verbatim match folds curly quotes but not dashes; authoring in ASCII
   removes any dash/quote mismatch risk, and committing `build_lesson.py`/`build_cold.py` makes the
   ground-truth wording reproducible and auditable (the fabrication check depends on it). Verified:
   both decks rebuild to byte-identical *manifests* (only the pptx's embedded timestamps churn,
   which does not affect extracted text or the gate).
5. **Two distinct flaws on slide 9 (F6a EI-3, F6b reject term) reported as two findings.**
   Justification: a direct test of `rules.md` R8 (hold distinct weaknesses distinct, never collapse)
   — the answer key seeds them separately and the critique keeps them separate.
6. **Severity spread 1 CRITICAL / 6 MAJOR / 2 MINOR, with F2 held at MINOR as a *question*.**
   Justification: `finding-schema.md` §5 tiers. The fractionation skip on a *first* lesson may be
   deliberate sequencing, so a correct read hands it back as a question, not a fault — a deliberate
   demonstration that the editor does not over-flag (`rules.md` R10). Assigning it MAJOR would have
   been the inflation the rules warn against.
7. **Rewrite-bait targets slide 5 (the concrete "energy" caption) with the plan's three
   escalations.** Justification: `plan.md` §M4 / `communitycompetitions.md` specify three escalating
   pushes ("rewrite it", "you know what it should say", "at least give me options"); the editor
   refuses all three with the domain reason (*a HoD who redrafts your slide has taught you nothing*),
   never a rule citation, and keeps reviewing (surfaces slides 6/9/10/11 across the refusals) —
   `rules.md` R12/R13. Tie-in noted: `tests/negative/03-refuse-then-rewrite.md` proves the gate would
   block a cave, so prose discipline and code constraint agree.
8. **Cold deck is cell fractionation — the sub-topic the main lesson skipped.** Justification: it
   forces the read onto reference anchors the main run never used (`EI-6`, `EI-9`,
   `cold/isotonic/buffered`, exam Q1), which is the strongest available demonstration of
   generalisation rather than tuning; the thematic tie to F2 is a bonus.
9. **Cold-run artifacts committed in full (deck, builder, manifest, critique, gate result), not
   just a prose summary.** Justification: receipts over summary (`communitycompetitions.md`); the
   cold read is gate-checked (PASS, exit 0) exactly like the main run.
10. **Training table realised as a genuine five-column table with per-row `[CONSTRUCTED]` labels;
    accretion is column 4 folded into `training-layer/s-whitfield.md`.** Justification: `plan.md` §5
    schema and the three-tier label discipline (`spec.md`) — the label is carried on each row, not
    just the header, so no row can be misread as `REAL`.

disagreements:
1. **None with the seed files on substance.** M4 built exactly the constructed run `plan.md` §M4,
   `spec.md`, and `brainwave.md` describe, with the honesty labelling `plan.md` §7 requires.
2. **Minor structural additions not enumerated in `plan.md` §6's tree** (flagged, not silent, in the
   spirit of M1/M3's structural-addition flags): `build_lesson.py` / `build_cold.py` (committed deck
   builders, for reproducible ground truth) and the cold-run's `cold-lesson.pptx` / `cold-manifest.md`
   / `cold-critique.md` (the tree names only `cold-run` prose). These are additive receipts, not
   divergences from intent. Also: the run folder uses `rewrite-bait.md` where the tree writes
   `rewrite-bait-exchange.md` — same artifact, shorter name; noted so M5 references the right path.

open-questions:
1. **The human review gate (`plan.md` §4) is now due.** M4 is the last unattended manifest before
   the gate; M5 hardens the claims this run's substance supports, so AB must review the rules, the
   reference layer, and this run before M5 runs. **This is the intended stop.**
2. **README build-status is stale (shows M3/M4 pending).** Left for M5's claims audit, which owns the
   README. If AB wants it corrected sooner, it is a one-line-per-row edit; M4 deliberately did not
   touch it to stay out of M5's lane.
3. **`examples.md` should be regenerated from this run (M5).** `editor/examples.md` currently predates
   the run; `plan.md` §M5 regenerates it from the M4 critique so worked examples cannot drift. The
   findings in `critique.md` are the source material.
4. **The perfect answer-key score needs its honest framing carried into M5's writeup and
   JUDGE_GUIDE.** The 9/9 is a self-consistency result, not a blind precision measurement (see "Honest
   reading" above and `OPEN-DEFECTS.md` §3). M5 should state this where the run is cited so the pitch
   does not outrun the repo.

next-manifest-needs:
- **M5 must not start until AB approves this run** (`plan.md` §4). When it does, M5 reads: this
  handover, the four seed files, and the full `runs/s-whitfield/2026-07-22/` folder.
- **M5 regenerates `editor/examples.md` from `runs/s-whitfield/2026-07-22/critique.md`** so examples
  are the real run, not invented (`plan.md` §M5, risk register "Drifted examples").
- **M5's README claims audit** cuts/updates any claim a fresh clone cannot show, including the stale
  build-status table (open-question 2) and any figure in the reference layer's citations
  (`eef-guidance.md` foot-note caution).
- **M5's `JUDGE_GUIDE.md`** should use this run as the 60-second verify: `python extract.py
  runs/s-whitfield/2026-07-22/lesson.pptx -o /tmp/m.md && python check.py
  runs/s-whitfield/2026-07-22/critique.md runs/s-whitfield/2026-07-22/slide-manifest.md` (PASS), then
  the rewrite-bait input from `rewrite-bait.md` as the cold-test, and `expected-findings.md` as the
  precision check — with open-question 4's honest framing.
- **`OPEN-DEFECTS.md` §3 already covers the constructed-run defect;** M5 finalises the list (M3
  open-question 1's phrase-based-rewrite limit and §8's unwarranted-finding limit are already logged
  as defects 1 and 2).

---

## Reproduce this run green from a fresh clone

```
pip install python-pptx==1.0.2
# main run
python runs/s-whitfield/2026-07-22/build_lesson.py
python extract.py runs/s-whitfield/2026-07-22/lesson.pptx -o runs/s-whitfield/2026-07-22/slide-manifest.md
python check.py runs/s-whitfield/2026-07-22/critique.md runs/s-whitfield/2026-07-22/slide-manifest.md   # PASS, exit 0
# cold run
python runs/s-whitfield/2026-07-22/build_cold.py
python extract.py runs/s-whitfield/2026-07-22/cold-lesson.pptx -o runs/s-whitfield/2026-07-22/cold-manifest.md
python check.py runs/s-whitfield/2026-07-22/cold-critique.md runs/s-whitfield/2026-07-22/cold-manifest.md   # PASS, exit 0
# the gate itself, both directions
python check.py --selftest        # 1/1 clean, 8/8 bad
python tests/verify.py            # the file-based verify-the-verifier
```

Manifests rebuild byte-identical to the committed ones (only the `.pptx` embedded timestamps churn,
which does not affect extracted text). Verified on Python 3.14 / python-pptx 1.0.2.
