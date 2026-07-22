# MANIFEST 5 — COMPLETE

status: complete-with-questions

summary: Built the ship layer — the whole entry is now legible to a stranger and verifiable
from a fresh clone. Regenerated `editor/examples.md` verbatim from the gate-passed
`s-whitfield` critique (real findings only, no invented examples); wrote `JUDGE_GUIDE.md` as a
three-level verify path (60-second enforcement / read one run / reproduce it yourself), with
every command confirmed to pass from this clone; wrote `writeup.md` (angle, four differentiators
with evidence pointers, the blind-01 two-chat consistency finding, the honesty section, the
manifest methodology, the field lineage); refreshed `README.md` as a 90-second front door and
fixed the stale build-status table (M3–M5 now shown complete, top banner updated). Ran a claims
audit reading the finished README/JUDGE_GUIDE/writeup as a hostile stranger with only a fresh
clone, and softened or attributed every claim the clone cannot demonstrate. Wrote
`build/submission-post.md` (community comment + pre-read paragraph). Finalised `OPEN-DEFECTS.md`.
**Did not touch** the editor's rules, the reference layer, or `check.py`/`extract.py` logic — M5
is documentation, examples, and claims only. Verified green throughout: `tests/verify.py`
(21/21 assertions), `check.py --selftest` (1/1 clean, 8/8 bad), the `s-whitfield` main + cold
gate (PASS), and all three blind critiques clearing the gate against **freshly extracted**
manifests (blind-01 test-1 8 findings, test-2 9 findings, blind-02 10 findings). The entry is
**not** marked submitted — that is AB's call after reviewing M5.

files-created:
- `JUDGE_GUIDE.md` — was an M1 stub; now the full three-level verify path. Level 1: the two
  commands (`tests/verify.py`, `check.py --selftest`) plus the live rewrite-block command, with
  exact expected output. Level 2: the `s-whitfield` run (deck, critique, answer key, 9/9
  caught/missed table) with its honest self-consistency framing, and the blind runs as the
  harder evidence. Level 3: drop `editor/` into a Claude project and reproduce the structured
  output by hand, with the blind-01 two-chat consistency as the shipped proof. Plus a "what the
  gate does not do" section and an optional one-command reproduce.
- `writeup.md` — was an M1 stub; now the build story and the case for the entry.
- `build/submission-post.md` — new. The 2–3 sentence community comment (what it reviews, who
  it's for, the one-line differentiator) plus a pre-read paragraph a judge reads before opening
  the repo.

files-changed:
- `editor/examples.md` — was an M1 stub reserved for M5; regenerated **verbatim** from
  `runs/s-whitfield/2026-07-22/critique.md` (which clears the gate). Shows the finding form
  field-by-field (the one CRITICAL), a multi-anchor finding, a pedagogy-only finding, two
  distinct findings held apart on one slide (R8), a held-back MINOR (R10), the clean slides
  drawing nothing, and the refuse-to-rewrite exchange. Examples generated from the run cannot
  drift from real output.
- `README.md` — fixed the stale build-status table (M3/M4/M5 were shown pending; now all six
  manifests ✅ complete) and the top banner (was "SUBSTANCE … pending"; now "COMPLETE M1–M5").
  Added a "reproducible system" differentiator with the blind-01 evidence pointer; made "the
  editor reads slide text — attach the `.pptx`, or run `extract.py` for a reproducible manifest"
  explicit; expanded the honesty note to distinguish the constructed self-consistency run from
  the harder blind runs; updated the folder map's `runs/` to the actual runs. Applied the claims
  audit (see below).
- `OPEN-DEFECTS.md` — finalised. §3 reworded so it is clear **every** run is constructed, with
  the two honest gradations (self-consistency vs blind-to-editor-but-author-built). Added §4:
  only 3.2.1 Cell structure is built to full depth; other topics are scaffold-only and wider
  Science is a future direction, not shipped. §1 and §2 (the two gate limits) were already
  present from M3 and are unchanged.

files-not-touched (guardrail):
- The editor's rules (`editor/rules.md`, `editor/identity.md`, `editor/reference/finding-schema.md`),
  the entire reference layer (`editor/reference/frameworks/`, `spec/`, `exam-questions/`),
  `check.py`, `extract.py`, `tests/`, and all `runs/` critiques/decks/answer-keys were **not
  modified**. M5 is documentation, examples, and claims — not a rebuild.

## What the claims audit cut or softened

Read the finished README, JUDGE_GUIDE, and writeup as a hostile stranger with only a fresh
clone. Nothing was found that was outright false; the following were softened, attributed, or
corrected so no claim outruns what the clone can show:

1. **Field-comparison absolutes attributed, not asserted.** "Every comparable editor reviews
   pasted text", "no one in the #9 field had done", "the favourite" — a fresh clone cannot
   verify claims about other people's entries. All such comparisons are now explicitly sourced
   to the committed competitor review (`build/communitycompetitions.md`), which the clone *can*
   read, with a note in the writeup that these are claims about the field, not clone-verifiable
   facts — and a pointer to what the clone *can* verify (JUDGE_GUIDE Levels 1–3).
2. **The "triple-anchored" example corrected.** `examples.md` §2 originally implied the slide-11
   finding carried three distinct anchor *fields*; it carries two (PRINCIPLE + a SPEC field that
   names both the spec topic and the exam question). Reworded to be honest: the read can draw on
   three source layers and a finding carries whichever apply, with the third layer (a skipped
   *content* spec point) shown by the §5 cell-fractionation finding. README's triple-anchor claim
   already hedged with "can" and was left.
3. **The consistency claim tightened to the truth.** The two blind-01 reads share **seven**
   findings (all three CRITICAL + the four MAJOR on slides 4 and 7); they differ only at the
   margins (which MINOR each surfaced, and one extra MAJOR one read made). The earlier "the minor
   findings vary" understated that one MAJOR also differs. Corrected in README, JUDGE_GUIDE, and
   writeup.
4. **"Scaffolds toward wider Science" moved to a next step.** The reference layer scaffolds AQA
   Biology 3.1–3.8 with one topic deep — it does not scaffold other sciences. README out-of-scope
   reworded to what ships; the wider-Science ambition is now named in `OPEN-DEFECTS.md` §4.
5. **No specific "CI is green right now" claim was made.** `.github/workflows/verify.yml` exists
   and runs `verify.py` + `--selftest` on push/PR (verified by reading it); the docs claim only
   that CI runs the checks on every push (a config fact), not a live GitHub Actions status this
   clone cannot see.

decisions-made:
1. **`examples.md` regenerated from the `s-whitfield` critique, not a blind critique.**
   Justification: the plan (§M5) and the M4 handover both name `critique.md` as the source, and
   it is the only critique paired with a committed answer key, so the examples map to scoreable
   ground truth. It clears the gate, so every reproduced QUOTE is verified verbatim. The blind
   critiques are cited as evidence in the judge guide/writeup instead.
2. **JUDGE_GUIDE Level 1 uses `verify.py` + `--selftest` as the two commands, with the live
   rewrite-block as a third demonstrator.** Justification: the plan asks for a no-install
   60-second verify and "see check.py block a rewrite". `--selftest` is self-contained and
   deterministically reports the rewrite fixture blocking; the fixture-03 one-liner shows a live
   block against a real manifest for anyone who wants it. Both were run and their exact output is
   quoted.
3. **Every command in the ship docs was executed before being documented.** Justification: the
   entry's whole pitch is "verifiable from a fresh clone", so a command that does not run would be
   the exact pitch-outrunning-the-repo miss. Confirmed: verify.py, selftest, both s-whitfield
   gates, and all three blind critiques against freshly-extracted manifests.
4. **Blind critiques quoted as clearing the gate against freshly-extracted manifests.**
   Justification: this is the strongest honestly-available evidence that the blind reads are
   fabrication-free on the real decks (not remembered), and it is reproducible by the judge. Ran
   `extract.py` on each committed blind deck and re-gated — all PASS.
5. **Commits made straight to `main`.** Justification: the entire build history (M1–M4 handovers)
   is committed to `main`, and the prompt directs "commit and push via shell git … Commit, push,
   stop." Branching would break the established manifest-on-main workflow. No seed file, editor
   rule, or gate code was changed, so there is nothing on `main` to protect behind a branch here.

disagreements:
1. **None on substance with the seed files.** M5 built exactly the ship layer `plan.md` §M5
   describes, with the honesty discipline `plan.md` §7 requires.
2. **`plan.md` §M5 lists two optional items not built: a demo-video shot list and a `docs/` demo
   surface.** Both are explicitly optional in the plan ("Optional `docs/` demo surface";
   "Demo-video shot list"). Not built, on purpose: `communitycompetitions.md` warns that a demo
   surface dilutes the entry (the `waypoint` cautionary tale), and `docs/README.md` already
   states the editor is the folder, not a site. A shot list with no video is scaffolding for work
   this build does not do. Flagged here rather than silently dropped. If AB wants either, it is a
   small M5-follow-up.
3. **Run-folder filename note carried from M4:** the rewrite-bait artifact is
   `runs/s-whitfield/2026-07-22/rewrite-bait.md` (the `plan.md` §6 tree names it
   `rewrite-bait-exchange.md`). The ship docs reference the real path. Same artifact, shorter
   name; noted, not changed.

open-questions:
1. **AB's review and the submit decision.** The entry is complete and verifiable but **not marked
   submitted** — that is AB's call after reviewing M5, per the prompt. `build/submission-post.md`
   holds the draft comment; nothing is posted.
2. **The residual open items are the four in `OPEN-DEFECTS.md`,** all honestly logged: (§1) the
   rewrite scan is heuristic and can miss a disguised rewrite; (§2) the gate checks form, not
   pedagogical correctness; (§3) no genuine teacher run exists — every run is constructed; (§4)
   only 3.2.1 is built to full depth. None is a defect in what ships; each is a named boundary or
   next step. The highest-value next step remains a `REAL` run: a genuine teacher on a genuine
   lesson (§3).
3. **Optional deliverables (disagreement 2)** — demo video and `docs/` surface — are open only if
   AB wants them; the build's position is that they add dilution risk, not score.

next-manifest-needs:
- **There is no M6.** M5 is the final manifest in `plan.md`. The only remaining action is AB's
  human review of the shipped entry and the decision to submit (using
  `build/submission-post.md`). If AB sends fixes back, they are scoped M5 follow-ups (claims
  wording, optional demo surface), not a new manifest.
- Anyone verifying cold should start at `JUDGE_GUIDE.md` (60-second Level 1), then `README.md`
  for the whole shape, then `writeup.md` for the case and `OPEN-DEFECTS.md` for the honest holes.

---

## Verified green at M5 close (from this clone)

```
python tests/verify.py            # 2/2 clean, 9/9 bad on named check, 21/21 assertions — VERIFY OK
python check.py --selftest        # 1/1 clean, 8/8 bad — SELFTEST OK
python check.py runs/s-whitfield/2026-07-22/critique.md      runs/s-whitfield/2026-07-22/slide-manifest.md   # PASS, 9 findings
python check.py runs/s-whitfield/2026-07-22/cold-critique.md runs/s-whitfield/2026-07-22/cold-manifest.md    # PASS, 2 findings
# blind reads clear the gate against FRESHLY extracted manifests (quotes verbatim on the real decks):
python extract.py runs/blind-01/2026-07-22/blind-lesson.pptx -o m.md && python check.py runs/blind-01/2026-07-22/blind-edit-output-test-1.md m.md  # PASS, 8
python extract.py runs/blind-01/2026-07-22/blind-lesson.pptx -o m.md && python check.py runs/blind-01/2026-07-22/blind-edit-output-test-2.md m.md  # PASS, 9
python extract.py runs/blind-02/2026-07-22/blind-lesson.pptx -o m.md && python check.py runs/blind-02/2026-07-22/blind02-edit-output-test.md  m.md  # PASS, 10
```

All relative links in the ship docs (README, JUDGE_GUIDE, writeup, OPEN-DEFECTS, examples,
submission-post) resolve to real files. Verified on Python 3.14 / python-pptx 1.0.2.
