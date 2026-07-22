# MANIFEST 1 — COMPLETE

status: complete-with-questions

summary: Read all four seed files in full and checked the design for internal
consistency. Scaffolded the complete repo layout from `plan.md` §6 as
purpose-and-owner stub files (no scored substance), drafted `identity.md` (the Head
of Department persona) and an honest README skeleton, and committed/pushed the work in
four pieces. The build is internally consistent bar one wording inconsistency in the
seed files (several places call the constructed M4 run "the real run"), flagged below
rather than silently edited.

files-created:
- `README.md` — repo README **skeleton**: intended shape (invariant, triple anchor, binary-input wedge, two surfaces, layout tree) plus a build-status banner and per-manifest state table so no claim outruns the repo.
- `identity.md` — the Head of Department **persona** (who reads, why this way, the no-rewrite boundary as character, tone, what to expect). M1 substance deliverable.
- `rules.md` — stub, owner M2 (critique discipline).
- `examples.md` — stub, owner M5 (worked findings generated from the M4 run).
- `reference/frameworks/rosenshine.md` — stub, owner M2.
- `reference/frameworks/cognitive-load.md` — stub, owner M2.
- `reference/frameworks/retrieval-practice.md` — stub, owner M2.
- `reference/frameworks/eef-guidance.md` — stub, owner M2.
- `reference/finding-schema.md` — stub, owner M2 (the SLIDE/QUOTE/PRINCIPLE/SPEC/WHY/QUESTION contract).
- `reference/spec/aqa-biology-index.md` — stub, owner M2.5 (8-topic map 3.1–3.8).
- `reference/spec/3.2-cell-structure.md` — stub, owner M2.5 (deep validated topic).
- `reference/exam-questions/cell-structure.md` — stub, owner M2.5 (distilled real questions).
- `extract.py` — stub, owner M3 (deterministic pptx→manifest); exits 2.
- `check.py` — stub, owner M3 (the blocking gate); exits 2.
- `tests/verify.py` — stub, owner M3 (verify-the-verifier harness); exits 2.
- `tests/cases/README.md` — stub dir marker, owner M3 (shipped clean critiques).
- `tests/negative/README.md` — stub dir marker, owner M3 (deliberately broken critiques).
- `.github/workflows/verify.yml` — CI **placeholder**, owner M3; manual-dispatch-only echo so it cannot run or fail on push before M3.
- `runs/README.md` — stub dir marker, owner M4 (constructed-run artifacts + the constructed-not-real invariant).
- `training-layer/README.md` — stub, owner M2.5 (five-column schema + one ILLUSTRATIVE row).
- `JUDGE_GUIDE.md` — stub, owner M5.
- `OPEN-DEFECTS.md` — stub, owner M4 (first entry) + M5 (finalised).
- `writeup.md` — stub, owner M5.
- `docs/README.md` — stub, owner M5 (optional demo surface, never the entry).
- `handover/MANIFEST-1-COMPLETE.md` — this file.

files-changed:
- None. M1 only added files. The four seed files (`plan.md`, `communitycompetitions.md`, `spec.md`, `brainwave.md`) were **not** modified — M1's standing rule is to flag divergences, not edit the seeds.

decisions-made:
1. **Scaffolded with purpose-and-owner stub files, not empty/`.gitkeep` placeholders.** Justification: the "done when" bar is that a stranger can see the intended shape from the skeleton; a stub that names its purpose and its owning manifest makes the shape legible and prevents scope bleed, while carrying no scored substance (no pedagogy, rules, corpus, or gate logic).
2. **Named the validated-topic files concretely** — `reference/spec/3.2-cell-structure.md` and `reference/exam-questions/cell-structure.md` — instead of the layout's placeholder `3.x-<validated-topic>`. Justification: `spec.md` locks the validation topic as AQA 3.2 Cell structure, so the filename is a structural consequence of an already-locked decision, not invented pedagogy.
3. **Made the `.py` stubs exit code 2.** Justification: 2 is neither the gate's PASS (0) nor its BLOCK (1), so a stub can never be mistaken for a working extractor or gate — the enforcement axis stays honest even in the skeleton.
4. **Made CI a manual-dispatch-only placeholder echo.** Justification: shows the CI shape in the tree while guaranteeing no failing Actions run on push before the gate exists; M3 replaces it with the on-every-push gate.
5. **Wrote `identity.md` to persona/character/boundary/tone only,** explicitly deferring the finding schema, severity ordering, and gate mechanics to `rules.md`/`finding-schema.md` (M2). Justification: honours the M1/M2 split ("structure only, plus the persona; no rules substance") while still making the no-rewrite boundary read as character, per `brainwave.md`.
6. **Wrote the README as an honest skeleton** with a build-status banner and a per-manifest state table, deferring exact usage steps and hard claims to M5. Justification: README quality is a scored criterion and shape must be visible, but M5 owns the claims audit; marking shipped-vs-pending pre-empts any claim outrunning the repo.
7. **Committed and pushed in four pieces** (skeleton → identity → README → handover). Justification: the instruction to commit/push as pieces complete, and it keeps the handover loop legible in history.

disagreements:
1. **"real run" wording — flagged, and not propagated.** Six places in `plan.md` (lines 59, 132, 137, 167, 209, 210) and one in `communitycompetitions.md` (line 67) call the M4 validation run "the real run" / "the real M4 run". This is in tension with the emphatic, repeated decision — `spec.md:15`, `plan.md:103` (M4 goal), `plan.md:115` (M4 guardrail), `plan.md:213` (risk register: "Constructed passed off as real"), `brainwave.md:45`, `communitycompetitions.md:66/69` — that no run in this build is real; it is **constructed**. The intended meaning in those seven places is "the actually-executed run (not a mock-up)", but because honest labelling is a load-bearing scored axis, the residual "real run" wording risks leaking a false claim into downstream artifacts (`examples.md`, README, the training table). **My divergence:** in the new artifacts (README, `identity.md`, the stub headers) I used "constructed" / "the executed run" and did **not** propagate the "real run" phrasing. I did not edit the seed files (that would be a silent override, which the seeds forbid). Legitimate uses of "real" were preserved and are *not* part of this flag: a real `.pptx` (binary input), a real/non-fabricated spec point or exam question, a real class context, and other entrants' genuinely real runs.
2. **`tests/cases/` scaffolded though not named in M3's task list.** It appears in the `plan.md` §6 layout but M3's task bullets name only `tests/verify.py` and `tests/negative/`. I followed the layout (authoritative for structure) and added `tests/cases/README.md` as the home for the shipped clean critiques the harness runs against. Minor; noted so M3 expects it.

open-questions:
1. **Should the "real run" wording be normalised in the seed files?** (disagreement #1.) Resolving it means editing `plan.md`/`communitycompetitions.md` — a human decision. Recommended home if approved: M5's README/claims audit, or a dedicated wording pass, rewriting the ~7 residual mentions to "constructed run" / "the executed run" while preserving the legitimate uses of "real". Needs AB.
2. **`<teacher-id>` slug and `<date>` format** for `runs/<teacher-id>/<date>/` and `training-layer/<teacher-id>.md` are undecided. M1 created the `runs/` and `training-layer/` README markers but not the id'd subdirs/files. M4 must fix the fictional-persona id and the date format.
3. **`OPEN-DEFECTS.md` ownership/sequencing.** M5's task list "creates" it, but M4's guardrail requires the missing genuine-teacher run to be logged there. I marked the stub owner "M4 (first entry) + M5 (finalised)" — M4 should create-if-absent and append, M5 finalises. Confirm this is the intended sequencing.
4. **`training-layer/README.md` is M2.5's to author** (schema + one ILLUSTRATIVE row), but M1 placed a stub there. M2.5 must **overwrite** the stub, not treat it as pre-existing schema.
5. **`examples.md` authorship.** The §6 comment, the risk register, and M5's task all put authorship in M5 (from the M4 run); M4's output list does not include `examples.md`. Read as consistent (M4 produces the run, M5 writes the file) — flagged only to prevent double-authorship. Confirm M4 does not write `examples.md`.
6. **M2.5 corpus paths not yet verified.** M2.5's inputs are three `professor-clive` corpus paths on AB's machine; M1 did not read them (out of M1 scope). M2.5 should verify they exist and are readable before starting, and flag if not.

next-manifest-needs:
- **M2 is next** (Substance: `rules.md`, `reference/frameworks/`, `reference/finding-schema.md`). It should read, in order: this handover, then all four seed files in full — especially `spec.md` ("The finding schema" and "What `check.py` blocks"), `brainwave.md`, and `communitycompetitions.md` (the claimline bar) — then `identity.md`.
- **Assume the skeleton exists.** M2 **overwrites** (does not append to) the stub headers at `rules.md`, `reference/frameworks/*.md`, and `reference/finding-schema.md`.
- **Keep the M1/M2 boundary.** `identity.md` is *who* the editor is; `rules.md` is *how* it works. `rules.md` should express the persona's discipline, not restate the persona.
- **`finding-schema.md` is the contract shared by the editor and `check.py` (M3).** Define exactly the fields SLIDE / QUOTE / PRINCIPLE / SPEC / WHY / QUESTION in a shape M3 can parse mechanically (the gate keys off it).
- **`rules.md` must teach critique, never creation:** the no-rewrite invariant, refuse-and-still-review, the anti-compression behavioural instruction (hold distinct weaknesses distinct; do not collapse three findings into one; do not soften), severity ordering (CRITICAL/MAJOR/MINOR), and the mandatory-question-not-fix rule. M2's handover must list **every rule with its justification**.
- **Guardrails carried forward:** frameworks in our own words with citations; **no AQA-specific content** (that is M2.5); **no examples** (they come from the M4 run). And do not propagate the "real run" wording — use "constructed" for the M4 run (open-question #1).
