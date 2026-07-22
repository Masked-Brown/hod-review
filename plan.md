# plan.md — Build Pipeline for `hod-review`

**What this is.** The full manifest-driven build plan for an ICM editor that reviews A-level Science lesson PowerPoints. It is written to be read and executed by Claude Code prompts ("Fable"), and it is itself a portfolio artifact: the way this repo was built is an ICM demonstration in its own right.

**Working name.** `hod-review` (the editor is a Head of Department doing the read-through before Monday morning). Swap the name freely; the persona is the load-bearing part.

**Delivery target.** The editor is a plain markdown folder a stranger drops into a Claude project so Claude *becomes* the reviewer. It also runs in Claude Code, where the Python gate genuinely executes. Any website is a demonstration surface only, never the entry.

---

## 1. Build philosophy: 20 / 80

The four seed files (this file, plus `communitycompetitions.md`, `spec.md`, `brainwave.md`) are authored by hand. They carry the decisions and the reasoning. Everything downstream is executed by Claude Code prompts that read all four seed files first, think for themselves, and run the manifests below.

The prompts are given freedom on scaffolding and structure. They are **not** given freedom on the scored substance (`rules.md`, the reference layer, `examples.md`). Loose freeform generation of the substance produces exactly the generic, drifting output the competition punishes. Where a manifest touches substance, it must list every decision with its justification in its handover file so the human can review before it is trusted.

## 2. The handover loop

Each manifest ends by writing one file: `handover/MANIFEST-<N>-COMPLETE.md`. That file is the signal the next prompt waits on.

Handover file format (every manifest writes this):

```
# MANIFEST <N> — COMPLETE
status: complete | complete-with-questions
summary: <2-4 sentences on what was produced>
files-created: <list with one-line purpose each>
files-changed: <list with what changed and why>
decisions-made: <numbered list, each with its justification>
disagreements: <where this manifest diverged from the seed files, and why>
open-questions: <numbered, each needing a human or a later manifest to resolve>
next-manifest-needs: <what M<N+1> should read first and assume>
```

The next prompt begins by polling for `handover/MANIFEST-<N>-COMPLETE.md`. If absent, it waits (loop). If present, it reads it, then the seed files, then proceeds. Prompts chain unattended except at the one human gate (section 4).

Rule for every manifest: **flag disagreements, do not silently override the seed files.** A divergence logged in `disagreements:` is a contribution. A silent override is a defect.

## 3. The manifests

### M1 — Research and scaffold

- **Goal.** Confirm the design against the seed files, then build the repo skeleton.
- **Inputs.** All four seed files.
- **Tasks.** Read the seed files in full. Verify each design decision is internally consistent and flag any that are not. Clone or scaffold the repo layout in section 6. Draft `identity.md` (the HoD persona from `spec.md`) and the README skeleton. Do **not** write `rules.md` substance yet.
- **Output.** Skeleton repo, drafted `identity.md`, README skeleton, `handover/MANIFEST-1-COMPLETE.md` with open questions.
- **Guardrails.** No invented pedagogy. No rules substance. Structure only, plus the persona.
- **Done when.** A stranger could see the intended shape of the repo from the skeleton and the README skeleton.

### M2 — Substance: rules, frameworks, finding schema

- **Goal.** Author the domain-general scored substance.
- **Inputs.** M1 handover, seed files.
- **Tasks.**
  - `reference/frameworks/` — Rosenshine's Principles of Instruction, Cognitive Load Theory, retrieval practice and spacing, EEF guidance. Each summarised in our own words with citations to source. One file per framework, each doing one job.
  - `reference/finding-schema.md` — the exact finding shape from `spec.md` (slide ref, verbatim quote, principle cited, spec point cited, why it fails, question for the teacher).
  - `rules.md` — how the HoD critiques: the no-rewrite invariant, the refuse-and-still-review discipline, the behavioural instruction against the model's compression bias (hold distinct weaknesses distinct; do not collapse three findings into one; do not soften), the severity ordering, the mandatory-question-not-fix rule.
- **Output.** The files above, `handover/MANIFEST-2-COMPLETE.md` listing **every rule with its justification** for human review.
- **Guardrails.** Frameworks in our own words, cited. No AQA-specific content yet (that is M2.5). Examples are not written here (they come from the real run in M5).
- **Done when.** `rules.md` teaches critique, never creation, and every rule is justified in the handover.

### M2.5 — The bespoke corpus layer (ultra depth)

This is the depth axis nobody else in the field has. It transforms AB's own distilled AQA Biology corpus into the editor's reference layer, giving every finding a triple anchor: content coverage, examiner insight, and assessment alignment.

- **Goal.** Build a bespoke, three-part AQA A-level Biology reference layer from AB's professor-clive corpus, plus wire the training-data table mechanism.
- **Inputs.** M2 handover (needs the finding schema), seed files, and AB's local corpus at these paths (Claude Code runs locally and can read them):
  - `C:\Users\alexa\github_repos\professor-clive\corpus\aqa\a-level\biology\04_intelligence`
  - `C:\Users\alexa\github_repos\professor-clive\corpus\aqa\a-level\biology\05_notes`
  - `C:\Users\alexa\github_repos\professor-clive\corpus\aqa\a-level\biology\06_qrs`
- **The mapping (this is the core instruction).**
  - `05_notes` → `reference/spec/` — the content index. What a lesson on each topic should cover: topic codes, subtopics, required practicals, assessment objective hooks. This is what a finding cites when a lesson misses content.
  - `04_intelligence` → folded into `reference/spec/` per topic as an "examiner insight / common misconceptions" block. This is what makes a finding sharp: "students confuse X and Y here, and slide 6 reinforces the confusion." This is the sharpest lens and the hardest to fake.
  - `06_qrs` → `reference/exam-questions/` — a **small** distilled set. Do not attempt full question generation. Pull roughly 6 to 10 real, representative questions per validated topic straight from the bank, each tagged with its spec point and the assessment objective it tests. This is what a finding cites when a lesson teaches content but never practises the format it is assessed in ("your lesson covers respiration but never rehearses the 6-mark extended-response these questions demand").
- **Size guidance and the reasoning for it.**
  - **Depth where demonstrated, scaffold everywhere else.** Build the full 8-topic index *structure* (AQA A-level Biology 3.1 to 3.8), but populate to full depth only the topic(s) the M4 validation lesson covers. The judges reward depth shown on a real run over shipped bulk, and much of an all-topics dump would never be exercised by the single validation deck.
  - **Per validated topic, aim ~200 to 400 lines** in its `reference/spec/3.x-<topic>.md` file: subtopic breakdown, required practicals, the examiner-insight block from `04_intelligence`, and a link to its `exam-questions` file. Enough that a finding can anchor to a specific spec point or practical; not so much it reads as unverifiable bulk or breaks the "each file does one job" score.
  - **Do not raw-dump the corpus.** Reformat it as *editor reference*: every entry must be something a finding can cite. A block of raw notes that no finding could ever point to is bulk, and bulk lowers the methodology score.
  - **Copyright is not a constraint here.** AB distilled this corpus himself from research; it is his own IP being contributed deliberately. The size discipline above is about methodology cleanliness and provenance, not permission.
- **The training-data table.** Define the schema in `training-layer/README.md` (full spec in section 5 below) and ship exactly one row, clearly marked `ILLUSTRATIVE`, so the mechanism is legible. Real rows are populated in M4, never here.
- **Output.** `reference/spec/` (full structure, deep on validated topic), `reference/exam-questions/` (distilled set), `training-layer/README.md` with the table schema and one illustrative row, `handover/MANIFEST-2.5-COMPLETE.md`.
- **Guardrails.** No fabricated questions. No raw dump. Mark the illustrative table row as illustrative. Populated table rows come from M4.
- **Done when.** A finding on the validated topic can cite a real spec point, a real misconception, and a real exam question, all from this layer.

### M3 — Enforcement

Claimline's full stack, pointed at slides. This is the axis that beats a prose-only field.

- **Goal.** Make the invariant a property, not a promise.
- **Inputs.** M2.5 handover, `spec.md` gate rules.
- **Tasks.**
  - `extract.py` — a deterministic PowerPoint reader (python-pptx). Input a `.pptx`, output a slide manifest: slide number, extracted verbatim text per slide. Stdlib plus python-pptx only.
  - `check.py` — the blocking gate. It reads the editor's critique output and fails (exit 1) if: any finding contains rewritten slide content or a "here's a better version" pattern; any finding has no slide anchor; any `QUOTE:` does not appear verbatim in the extracted slide manifest (the fabrication check, claimline's Rule 0 applied to slides); any finding cites no principle and no spec point; the output ends in a fix rather than a question.
  - `tests/verify.py` — runs the gate over shipped example critiques and asserts the contract.
  - `tests/negative/` — deliberately broken critiques that must each fail on a named check (verify the verifier): one that quotes a line never on any slide; one that refuses to rewrite then rewrites inside a field; one that invents a finding on a clean deck; one generic-feedback finding with no anchor. Self-test asserts N/N known-bad rejected.
  - `.github/workflows/verify.yml` — CI running both on every push.
- **Output.** The files above, `handover/MANIFEST-3-COMPLETE.md`.
- **Guardrails.** Gate reports facts, blocks on violation, never judges pedagogical quality (that is the editor's job, not the gate's). Stdlib plus python-pptx. Self-test must prove both directions: blocks every bad, clears every clean.
- **Done when.** `python3 tests/verify.py` and `--selftest` both pass, and CI is green.

### M4 — Validation and receipts

- **Goal.** Prove the editor on a **constructed** deck, honestly labelled, and ship the run as evidence. There is no real teacher and no real lesson in this build: the run is a deliberately constructed demonstration case, and every artifact says so.
- **Inputs.** M3 handover, the M2.5 reference layer.
- **Tasks.**
  - Fable constructs the validation deck itself: a mix of clean slides and slides seeded with named flaws, each seeded flaw mapped to a specific anchor in the M2.5 reference layer (principle, spec point, or exam-question set). Fable also constructs a **fictional teacher persona** to drive intake — used as a persona, never presented as a claimed real person.
  - Ship `runs/<teacher-id>/<date>/expected-findings.md`, the answer key: it lists every deliberately seeded flaw with the slide it sits on and the reference anchor it maps to, so a judge can verify the editor's precision against ground truth.
  - Run `extract.py` on the constructed deck. Run the editor. Produce the critique.
  - Run the rewrite-bait exchange: ask the editor three escalating times to rewrite a slide ("rewrite slide 4", "you know what it should say", "at least give me options"), capture that it refuses all three while still reviewing, and that the refusal gives the domain reason (a HoD does not plan your lesson for you), not an internal-rule citation.
  - Populate the five-column training table with rows from this run, each labelled `CONSTRUCTED`.
  - Write the accretion entry: what this run taught the editor about *this constructed teacher persona* (recurring blind spots, class context), appended to `training-layer/<teacher-id>.md`, stated as constructed.
  - Cold-run: run against a second constructed deck the editor has not seen, commit a short cold-run review.
  - Run `check.py` against the produced critique and commit the PASS.
- **Output.** `runs/<teacher-id>/<date>/` (slide manifest, critique, rewrite-bait exchange, expected-findings.md, training-table.md with CONSTRUCTED rows), the appended `training-layer/<teacher-id>.md`, cold-run review, `handover/MANIFEST-4-COMPLETE.md`.
- **Guardrails.** Constructed run only, honestly labelled. Every artifact — README, `runs/`, `training-layer/` — states the deck and persona are constructed, using the word "constructed"; nothing is implied to be an organic teacher submission. The absence of a genuine teacher run is logged in `OPEN-DEFECTS.md` as a next step, not hidden.
- **Done when.** A judge can read the full run, check it against `expected-findings.md`, watch the boundary hold, and see at every artifact that the run is constructed.

### M5 — Ship layer

- **Goal.** Harden the entry so a fresh clone can verify every claim.
- **Inputs.** M4 handover, **human review approval** (section 4).
- **Tasks.**
  - `examples.md` — regenerated from the actual M4 run, so examples cannot drift from reality.
  - `JUDGE_GUIDE.md` — a 60-second no-install verify, then a cold-test battery including the rewrite-bait input.
  - `OPEN-DEFECTS.md` — honest list of known holes (this graded well for claimline; copy the honesty).
  - README claims audit — cut any claim a fresh clone cannot show.
  - `writeup.md` — the build story and the intellectual lineage.
  - Submission post draft (2 to 3 sentences: what it reviews, who it is for) plus the comment body.
  - Demo-video shot list.
  - Optional `docs/` demo surface (demonstration only, clearly secondary).
- **Output.** The files above, `handover/MANIFEST-5-COMPLETE.md`.
- **Guardrails.** Examples from the real run only. Every README claim must map to something in the repo.
- **Done when.** A stranger cloning cold can verify the headline claims in six minutes.

## 4. The one human gate

Between M4 and M5. M5 hardens claims, so the human must first approve the substance those claims describe: the rules, the reference layer, and the real run. Everything before M4 and the whole of M5 chain unattended. AB reviews, approves or sends specific fixes back, then releases M5.

## 5. The training-data table (five columns, full spec)

The accretion mechanism, made auditable and visible. It is the "folder that learns" shipped populated, not designed and left empty (the field's most-punished miss). It also exposes the reasoning chain, which is the integrative-complexity demonstration.

Two artifacts:

- **Run-level table** — `runs/<teacher-id>/<date>/training-table.md`. One row per finding in that run.
- **Accumulated teacher file** — `training-layer/<teacher-id>.md`. The distilled patterns carried across that teacher's runs.

The run-level table columns:

| Column | What goes in it |
|---|---|
| **1. Input** | The slide or section under review, plus the teacher's stated intent for it (from intake). |
| **2. Editor reasoning** | The chain: which lens fired (framework, spec point, exam-question set), what it checked, what it compared against. The thought process made visible. |
| **3. Finding and rationale** | The finding as handed back (verbatim quote, slide anchor, principle and spec point cited, why it fails, the question for the teacher), and why this was surfaced rather than left. |
| **4. Training-layer impact** | What this run wrote to `training-layer/<teacher-id>.md`. For example: "teacher recurrently front-loads content before any retrieval, pattern logged." |
| **5. Future-sample benefit** | How the next review of this teacher changes as a result. For example: "next deck, the editor checks retrieval placement first, because it is this teacher's known blind spot." |

Discipline: rows carry one of three labels, never blurred — `ILLUSTRATIVE` (M2.5, exactly one, to show the mechanism), `CONSTRUCTED` (M4, from the constructed run — this is the real evidence in this build), and `REAL` (reserved for a genuine teacher run, unused in this build and named as a next step in `OPEN-DEFECTS.md`). A `CONSTRUCTED` row mislabelled `REAL` is the pitch-outrunning-the-repo miss. An empty or placeholder-filled table is worse than no table; it is the exact mistake the field was marked down for.

## 6. Target repo layout

```
hod-review/
  README.md
  identity.md
  rules.md
  examples.md                      # generated from the real M4 run
  reference/
    frameworks/
      rosenshine.md
      cognitive-load.md
      retrieval-practice.md
      eef-guidance.md
    spec/
      aqa-biology-index.md          # 8-topic map, 3.1 to 3.8
      3.x-<validated-topic>.md      # deep; notes + examiner insight
    exam-questions/
      <validated-topic>.md          # distilled from 06_qrs
    finding-schema.md
  extract.py                        # pptx -> slide manifest
  check.py                          # the blocking gate
  tests/
    cases/
    negative/
    verify.py
  .github/workflows/verify.yml
  runs/
    <teacher-id>/<date>/
      slide-manifest.md
      critique.md
      rewrite-bait-exchange.md
      expected-findings.md          # answer key: every seeded flaw + its anchor
      training-table.md             # five columns, CONSTRUCTED rows
  training-layer/
    README.md                       # table schema + one ILLUSTRATIVE row
    <teacher-id>.md                 # accumulated distillation
  JUDGE_GUIDE.md
  OPEN-DEFECTS.md
  writeup.md
  plan.md
  communitycompetitions.md
  spec.md
  brainwave.md
  docs/                             # optional demo surface only
```

## 7. Risk register (carry through every manifest)

- **Empty memory.** The training layer is only shipped populated, from a real run. Never placeholders. (M4 owns this.)
- **Drifted examples.** `examples.md` is generated from the real run in M5, never invented in M2. A drifted example teaches the drift.
- **Arithmetic or matching in the model.** Anything deterministic (verbatim-quote checks, slide anchoring, spec-point matching) runs in `check.py` and `extract.py`, not on model diligence.
- **Pitch outrunning the repo.** M5's README audit cuts any claim a fresh clone cannot verify. `OPEN-DEFECTS.md` states what is not covered.
- **Constructed passed off as real.** No run, deck, or persona in this build is real. Every artifact says so, in the word "constructed"; the training table labels its rows `CONSTRUCTED`, never `REAL`; and `OPEN-DEFECTS.md` names the missing genuine teacher run as a next step, not hidden. (M4 owns this.)
- **Website dilution.** No app. The editor is the folder. `docs/` is a demo surface, secondary, and never the thing a judge drops into a project. (waypoint is the field's cautionary tale here.)
- **Bulk over signal.** The corpus layer is reformatted as citable reference, deep where demonstrated, scaffolded elsewhere. No raw dump.
