# communitycompetitions.md — What Wins, What Loses

Read this before writing anything. It is the accumulated judgment from the community's competitions, distilled so a build prompt knows what to reach for and what to avoid. This is guidance, not a rubric to game; the point is to build the strongest honest entry.

---

## The four judging criteria (Comp #9: The Editor)

1. Does the editor actually **critique**, or does it rewrite, summarise, or praise? This is the highest-weighted criterion.
2. Is the **domain specific** enough to be useful? Broad loses. "Writing editor" fails; "op-ed editor for tech-policy publications" passes.
3. Is the **methodology clean**? Each file does one job well.
4. **README quality.** Can a stranger clone it cold and use it?

## The three axes that split the field

- **Enforcement.** Your one guarantee lives in code (a blocking gate, a self-tested checker, a schema check) or it lives in prose you hope the model obeys. A *must* in a markdown file is a request. A *must* in code is a constraint.
- **Receipts.** A real run shipped as evidence (transcript, dated log, before-and-after fix) reads differently from a polished simulation. Every time. This was the single most-rewarded axis.
- **Accretion.** Almost everyone designs a memory (a corrections log, a run archive). Almost nobody ships one with real rows in it. Most common promise, rarest delivery.

## The three misses to never repeat

- **The empty memory.** A designed loop that never ran is a diagram. Ship it populated, from a real run, or cut it.
- **Arithmetic in the model.** Anything deterministic (counting, summing, date maths, verbatim-quote matching) belongs in a script, not on model diligence. Worked examples whose numbers do not survive their own rules teach the model the drift.
- **The pitch outrunning the repo.** Tighten every claim to what a stranger can verify from a fresh clone. The builds that did this were a pleasure to grade, and that correlated with placing.

## What the named winners actually did

- **Mira Bradshaw (chalky-prd)** — the intended user, a real person, ran it async on real work; the whole run shipped as evidence: transcript, red-team, fix log. Receipts, in the oldest sense.
- **Gabriel Azoulay (Visit Ready)** — the rule everyone writes as prose ("no diagnosis"), enforced by a blocking, self-tested gate in code, plus a shipped `blocked-draft.md` showing the gate reject a leak.
- **Nicolás Patrón (structure-call-ar)** — the same arithmetic pinned in Python, TypeScript, and the worked examples, reconciling to the last unit.
- **Will Vessels (content-engine)** — end-to-end samples with provenance sidecars that actually match each lane's declared rules. The differentiator shipped, not described.
- **Sunny Singh (Context Re-Entry)** — every fact wears a source tag; when memory and the repo disagree, the repo wins. Demonstrated on a real false memory.
- **Jordan Shaw (Quartermaster)** — confidence derived at read time and never stored, so stale cannot hide behind a cached badge.
- **Roc Lee (Daily Sonar)** — column-level ownership of a shared sheet: what the machine may write, propose, or never touch.
- **Craig Howard (Voice Engine)** — "a folder cannot learn on its own; you are the training loop." The correction mechanism written down.

## The Comp #9 field, and the bar to beat

**claimline (Gabriel again) is the favourite.** It fuses everything and goes a layer deeper. Match or beat this stack:

- Findings quote the copy verbatim, cite the exact rule, state what the writer must resolve. Never rewrites.
- A test harness: shipped cases with hundreds of checks. The load-bearing one, **Rule 0: every quoted passage must appear verbatim in the input**, so a fabricated finding fails mechanically regardless of how competent it reads.
- **Negative tests that verify the verifier**: deliberately broken reviews that must each fail on a named check. "A checker that passes everything proves nothing."
- **CI** running both on every push. A `JUDGE_GUIDE.md` with a 60-second no-install protocol. An `OPEN-DEFECTS.md` listing known holes honestly.
- A **rewrite-bait test**: the input escalates three times and adds time pressure; the editor must refuse all three while still doing the review, and the refusal must give the domain reason, not cite an internal rule.

Others in the field: **vera-plan-editor** (demo video, flawed-sample-plus-answer-key, receipts, and one original mechanism: every finding gets an explicit disposition so nothing disappears silently; no code gate). **WHETSTONE** (deterministic `verify.py` facts-floor, defects-vs-decisions split, real reviews including one of itself). **cafe-pitch-editor** (a `check.py` that only verifies its own shipped examples, honestly scoped, narrow domain).

**waypoint is the cautionary tale.** A full Next.js app: dashboard, resume studio, Playwright tests. The actual editor is buried in a sub-folder. "Is the methodology clean, each file one job" becomes hard to answer, and the folder a stranger drops into a project is not the repo root. Enormous effort, diluted entry. **If we build a site, it is a demonstration surface for the editor only, never the entry.**

## Hard fail conditions (do not do)

- Rewriting, drafting, or supplying replacement content instead of handing the fix back.
- Generic feedback ("consider strengthening your intro") with no anchor and no named principle.
- A domain too broad to be a specialism.
- A designed memory shipped empty or with placeholder rows.
- Claims in the README a fresh clone cannot demonstrate.
- Deterministic work left to model diligence.
- A private repo, or one that goes private during judging.

## The winning shape (do)

- One tight domain: A-level Science lesson editor, AQA, Biology-first.
- The no-rewrite invariant enforced in code, not just in prose.
- Findings triple-anchored and fabrication-checked against the source.
- One real run shipped in full, including a refused rewrite-bait exchange.
- A populated accretion layer, from that real run.
- A judge guide with a 60-second verify and an honest open-defects file.
- Examples generated from the real run, so they cannot drift.

## Our differentiators (what no one in the #9 field has)

1. **A binary input.** Every entry reviews pasted text. Ours ingests a real PowerPoint via a deterministic extractor, and every finding is quote-checked against the extracted slide text (claimline's Rule 0, applied to an artifact nobody else touches).
2. **Triple-source citations.** claimline cites one source (a regulation). Ours cites three: the pedagogical principle (Rosenshine, CLT, EEF), the AQA spec point the slide serves, and a real exam question the content is assessed by. Deeper anchoring than the current bar.
3. **An in-domain justification for no-rewrite.** The Head of Department read-through: someone senior reads your lesson, points at what will fail with your class, and hands it back. It never plans the lesson for you.
