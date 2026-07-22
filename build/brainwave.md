# brainwave.md — The Reasoning Behind the Build

Why each decision was made, so a build prompt inherits the thinking, not just the instructions. When a manifest hits a judgment call the seed files did not foresee, it should resolve it in the spirit of this file.

---

## Why this domain

A lesson-plan editor for teachers is a real problem with an edtech payoff (it is an add-on feature for an existing product, so the competition doubles as product validation). Scoped to AQA A-level Biology, it is specific enough to be a genuine specialism, and it sits on ground where the builder has real materials and real credibility. Broad "lesson editor" would lose on the specificity criterion; the narrowing to one board and one subject is what makes it a winner.

## Why no-rewrite is the whole game

The competition's highest-weighted criterion is whether the editor critiques rather than rewrites. Lesson slides beg to be rewritten, which makes the trap sharper here than in most domains. The instant the editor writes "here is a better starter", the entry has failed the angle. So the no-rewrite rule is not a line in `rules.md` we hope holds; it is the invariant we enforce in code. This mirrors the enforcement exemplar (Gabriel's no-diagnosis gate) and the field favourite's rewrite-bait test.

The in-domain justification carries it: a Head of Department reading your lesson before Monday points at what will fail and hands it back. One who rewrites it for you has taught you nothing, and the pedagogy is yours to own. The constraint makes the tool better, it does not limit it.

## Why a binary input is the wedge

Every other entry in the field reviews pasted text. Ingesting a real PowerPoint through a deterministic extractor is a differentiator no one else has, and it lets the same fabrication-proof mechanism the favourite uses (every quote must appear verbatim in the source) apply to an artifact nobody else touches. The extractor is deterministic on purpose: slide anchoring and quote-checking are the kind of matching that must never run on model diligence.

## Why triple-source citation beats single-source

The field bar cites one source per finding (a regulation). Anchoring each finding to three (the pedagogical principle, the AQA spec point, and a real exam question the content is assessed by) is a depth axis taken further than anyone else has taken it. It is also what turns critique from opinion into something a teacher cannot argue with: not "I think this starter is weak" but "this violates spaced retrieval, skips spec point 3.x, and never rehearses the question format it is assessed in." The three-part reference layer is built from the builder's own distilled corpus, which is why it can go this deep.

## Why the training layer must be populated, not designed

The field's most-punished miss was the empty memory: everyone designed a learning loop, almost nobody shipped one with real rows. So the layer is only ever shipped populated, from a real run, and the discipline of marking rows illustrative versus real is strict. The five-column table does double duty: it satisfies the accretion axis honestly, and it exposes the reasoning chain, which is the integrative-complexity demonstration the builder wants to show. An empty table would be worse than no table.

## Why we ship the distilled layer, and why size is disciplined

The reference layer is the builder's own IP, distilled by hand from research, so copyright is not a constraint and contributing it is a deliberate choice. The size discipline (deep on the validated topic, scaffold the rest, reformat as citable reference rather than raw dump) is about two things the judges score: methodology cleanliness (each file does one job) and provenance (a finding must be able to point at a specific entry). Raw bulk that no finding could ever cite lowers the score; it does not raise it. Depth shown on a real run beats depth shipped and never exercised.

## Why the Head of Department identity

The persona is the load-bearing part of the no-rewrite discipline. Every UK teacher knows the HoD pre-observation read-through, so the boundary ("points at what fails, hands it back, never plans it for you") is instantly legible and instantly justified. Identity is where the enforcement rule stops feeling like a restriction and starts feeling like the correct behaviour of a specific expert.

## Why 20 / 80 and manifests

The scored substance (rules, reference, examples) is authored and curated by hand because loose generation drifts, and a drifted example teaches the model the drift. Everything else is handed to Claude Code prompts that read the full reasoning here and run unattended on a manifest loop. The build process is itself an ICM artifact: staged jobs, each with one goal and a handover summary, the next waiting on the last. It demonstrates the methodology while producing the entry.

## The bar we are targeting

Beat claimline. That means matching its stack (gate, verify-the-verifier negative tests, CI, judge guide, honest open-defects) and adding the two things it does not have: a binary PowerPoint input and triple-source citations. Nobody in the field has done both of those. That is the opening.

The M4 run is a constructed demonstration, honestly labelled, not a real user on a real lesson. The absence of a genuine teacher run is logged as a next step in `OPEN-DEFECTS.md`, not claimed as done.
