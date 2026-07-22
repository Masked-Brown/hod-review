# MANIFEST 3 — COMPLETE

status: complete-with-questions

summary: Built the enforcement stack that makes the no-rewrite invariant a property,
not a promise. `extract.py` reads a `.pptx` into a deterministic, verbatim slide
manifest; `check.py` is the blocking gate that fails (exit 1) on any of eight named
violations of the invariant, and reports facts without ever judging pedagogy;
`tests/verify.py` proves the gate **both directions** over the real pipeline
(fixture deck → extract → check) — 2/2 clean critiques cleared, 9/9 deliberately
broken critiques blocked each on its named check, 21/21 assertions — and
`.github/workflows/verify.yml` runs that plus `check.py --selftest` on every push.
The three open questions M2/M2.5 handed to M3 (typographic-quote normalisation, the
rewrite/fix pattern set, whether to validate handles) are resolved and documented in
code. `python tests/verify.py` and `python check.py --selftest` both pass locally on
Python 3.14 / python-pptx 1.0.2. M4 (the constructed deck and validation run) was
**not** started — it needs the human review gate before M5.

files-created:
- `extract.py` — deterministic `.pptx` → slide manifest (overwrote the M1 stub). Reads
  text boxes, placeholders, tables (cell by cell), and text inside grouped shapes,
  verbatim, in document order; emits `## Slide N` blocks; every slide keeps its number
  even when empty so anchoring never drifts. Stdlib + python-pptx only. CLI: `python
  extract.py deck.pptx [-o out.md]`.
- `check.py` — the blocking gate (overwrote the M1 stub). Enforces `spec.md`'s "What
  check.py blocks" / `finding-schema.md` §7 as eight codes (below). Library
  (`check_critique`, `parse_manifest`) + CLI (`python check.py critique.md manifest.md`,
  `--json`, `--selftest`, `--no-handle-check`). Reports facts and blocks; never judges
  pedagogy (`rules.md` R16, `finding-schema.md` §8).
- `tests/verify.py` — verify-the-verifier harness (overwrote the M1 stub). Builds the
  fixture deck, round-trips it through `extract.py`, then runs the gate over every
  `cases/` and `negative/` fixture and asserts each clears / is blocked on its named
  check, that **every** code in `check.ALL_CODES` has a negative, and that the CLIs and
  `--selftest` behave.
- `tests/fixture_deck.py` — **new**; the canonical 6-slide gate-test deck (built at test
  time, not committed as a binary). Flagged below as a structural addition.
- `tests/cases/critique-cell-structure.md` — clean 3-finding read (worst-first, each
  ending in a question, all quotes verbatim); must PASS.
- `tests/cases/critique-no-findings.md` — a read that surfaced no findings; must PASS
  (the gate never manufactures work).
- `tests/negative/01-quote-not-on-slide.md` … `09-slide-not-in-manifest.md` — nine
  known-bad critiques, one per named check, each broken in exactly one way.
- `.gitignore` — **new**; ignores Python bytecode/caches only (scoped narrowly; see
  decision 13).
- `handover/MANIFEST-3-COMPLETE.md` — this file.

files-changed:
- `.github/workflows/verify.yml` — replaced the M1 manual-dispatch placeholder with the
  real workflow: on push + PR, install python-pptx and run `tests/verify.py` and
  `check.py --selftest`.
- `tests/cases/README.md`, `tests/negative/README.md` — overwrote the M1 stubs with the
  populated contract (what each fixture proves, the EXPECT→code table).
- The four seed files were **not** modified.

## The eight named checks `check.py` enforces

| Code | Blocks (spec.md / finding-schema.md) |
|---|---|
| `REWRITE_PATTERN` | rewrite / "better version" phrasing in the editor's prose or a field |
| `ENDS_IN_FIX` | the output continues past the last question with a fix |
| `NO_SLIDE` | a finding with no usable SLIDE anchor |
| `SLIDE_NOT_IN_MANIFEST` | a SLIDE number the deck does not contain |
| `QUOTE_NOT_VERBATIM` | a QUOTE not found verbatim on the **cited** slide (the fabrication check) |
| `NO_ANCHOR` | a finding citing neither a PRINCIPLE nor a SPEC point |
| `NO_QUESTION` | a finding not ending in a QUESTION that ends in `?` |
| `MALFORMED_BLOCK` | a finding block with a missing field, wrong order, or empty required field |

`spec.md` names five block conditions; these are those five plus the well-formedness
and slide-in-manifest checks `finding-schema.md` §2/§7.6 imply, made explicit and each
given a negative fixture (decision 2).

decisions-made:
1. **Manifest format: a human-readable, machine-parseable Markdown file** — a `# Slide
   manifest` preamble then one `## Slide N` block per slide, verbatim text beneath.
   Justification: `plan.md` §6 calls the artifact `slide-manifest.md`; a line-scan
   parser (`^## Slide (\d+)$`) keeps `check.py` a scan, not a Markdown parse, and a
   judge can read the manifest directly. Negligible edge (a slide whose text literally
   contains a line `## Slide 7` would mis-split) is documented in code and open-question
   3; real decks do not do this, and the `verify.py` round-trip proves extract↔check
   agreement on realistic content.
2. **Eight violation codes, one negative fixture each; the gate self-asserts full
   coverage.** Justification: "a checker that passes everything proves nothing" — and a
   checker whose *checks* are untested proves little more. `spec.md`'s five bullets plus
   the two structural checks `finding-schema.md` implies gives eight; `verify.py`
   asserts `set(EXPECT codes) == set(check.ALL_CODES)`, so a future edit that drops a
   check without a fixture fails CI.
3. **Verbatim match = whitespace-normalised substring against the *cited* slide only.**
   Collapse runs of whitespace to one space on both sides; match is otherwise exact.
   Scoping to the cited slide (not "any slide") also catches right-quote/wrong-slide.
   Per `finding-schema.md` §3.
4. **Typographic quotes/apostrophes folded to ASCII in the verbatim match — quotes and
   apostrophes only, not dashes** (resolves M2 open-question #1). Justification:
   PowerPoint autocorrects `'`→`’` and `"`→`”`, so a real quote would fail a naive
   match; folding them keeps the fabrication check true without letting paraphrase
   through. Dashes are left alone deliberately — an en/em-dash difference can be a real
   fabrication signal, and the flagged edge was about quotes, not dashes. Verified: a
   critique quoting with a curly apostrophe matches the straight apostrophe on the
   slide.
5. **Rewrite/fix detection is a documented phrase list, scanned over the editor's prose
   and every field *except the verbatim QUOTE span*** (resolves M2 open-question #3).
   Justification: the QUOTE is the *slide's* words, not the editor's; a slide that
   itself says "try this instead" must not trip the gate, so the QUOTE span is excluded
   from the scan. The list catches "here's a better version", "it should read", "replace
   X with Y", "let me reword", and kin. Its limit (phrase-based, cannot see unmarked
   supplied content) is stated in open-question 1.
6. **`ENDS_IN_FIX` vs `REWRITE_PATTERN` split by position.** A rewrite phrase *after* the
   last finding's QUESTION → `ENDS_IN_FIX` (spec.md "ends in a fix rather than a
   QUESTION"); anywhere else → `REWRITE_PATTERN` (spec.md "rewritten content / better
   version"). Justification: `spec.md` lists these as two separate block conditions, so
   the gate reports them as two distinct named checks.
7. **The PRINCIPLE/SPEC handle check is an advisory soft-warning, never a block**
   (resolves M2.5 open-question #2). It is **structural**: it recognises a handle by
   *shape* (a `reference/frameworks/` prefix, or `AQA <code> — …`) and warns only on a
   value that is not a handle at all — a vague gesture (`rules.md` R15) like "good
   practice". Justification: M2.5 itself cautioned that hard membership validation would
   break the gate as the reference layer grows; a structural advisory enforces "cite a
   handle, not a gesture" while staying robust to new topics, `EI-n`, and `exam Q-n`.
   Disable with `--no-handle-check`.
8. **A critique with zero findings PASSES.** Justification: a genuinely clean deck draws
   no findings (`rules.md` R10, `finding-schema.md` §5); the gate blocks *violations*, it
   never forces findings or judges whether the read *should* have found more — that is
   pedagogy, and the gate is forbidden it (R16, §8). `critique-no-findings.md` fixes this
   as a tested PASS.
9. **`check.py --selftest` is self-contained; `tests/verify.py` is the comprehensive
   on-disk harness. Both prove both directions and both pass.** Justification: `check.py`
   is the artifact a judge is most likely to run in isolation, so its `--selftest` uses
   inline fixtures and needs no `tests/` directory; the small duplication buys standalone
   integrity. The reviewable, file-based verify-the-verifier is `tests/verify.py`.
10. **The fixture deck is built at test time, not committed as a binary.** Justification:
    deterministic, no binary-diff noise, and it keeps the fixture unmistakably *a gate
    test*, not the M4 constructed run. `verify.py` builds it, extracts it, and runs every
    critique against the resulting manifest, so the whole pipeline is exercised.
11. **Nine negatives = the four named in `plan.md` §3 plus five extending coverage** to
    every gate check (missing slide, out-of-manifest slide, non-question terminal,
    malformed block, ends-in-fix). Justification: the plan names four as examples; a
    genuine verify-the-verifier covers every check.
12. **CI pins Python 3.12 and `python-pptx==1.0.2`.** Justification: reproducibility —
    1.0.2 is the version the passing local run used; 3.12 is a stable Actions runtime and
    the code is 3.9+ compatible (`from __future__ import annotations`).
13. **Added `.gitignore`, scoped to Python bytecode/caches only.** Justification: keeps
    `__pycache__` out of history. It deliberately does **not** ignore `*.pptx`, so it
    cannot surprise M4 if M4 chooses to commit its constructed deck as evidence.
14. **CLIs reconfigure stdout/stderr to UTF-8 (`errors="replace"`).** Justification: the
    output and handles contain em dashes; this prevents a `UnicodeEncodeError` on a
    strict Windows console without affecting Linux/CI output.

disagreements:
1. **`tests/cases/` ownership — divergence from the M1 stub note, flagged not silent.**
   The M1 `tests/cases/README.md` stub read "Owner: M3 (populated with **M4 outputs**)".
   M3 diverges: the harness ships its **own** gate fixtures (a fixture deck and
   hand-written clean/broken critiques), so the gate is provable *independently of M4*.
   This is the honest reading of the split — the gate must be self-tested at M3, before
   any run exists (`plan.md` §3 "Done when: `verify.py` and `--selftest` both pass"),
   which cannot depend on M4. The constructed M4 critique still lands under `runs/`, and
   `examples.md` is regenerated from it at M5, so worked examples cannot drift. I updated
   the README to say so rather than editing the plan.
2. **`tests/fixture_deck.py` is a structural addition not named in `plan.md` §6's tree**
   (mirrors M1's flag that `tests/cases/` was scaffolded though not in M3's bullet list).
   Justification: `verify.py` needs a real `.pptx` to round-trip `extract.py`; a
   deterministic build-at-test-time module is cleaner than a committed binary. Minor;
   noted so M4/M5 expect it.
3. **Made the gate's named checks eight, not five.** Not a divergence from intent —
   `finding-schema.md` §7.6 already lists "malformed finding block" as an implied check,
   and a SLIDE not in the manifest is `finding-schema.md` §2 — but `spec.md` enumerates
   five bullets, so I note that the gate reports **eight** codes (the five plus the two
   structural checks split out and named) so nothing reads as scope creep.

open-questions:
1. **Rewrite detection is phrase-based and cannot catch *unmarked* supplied content.** If
   an output appended raw rewritten slide text with no tell-tale phrase ("here's a
   better…") *and* still ended on a valid question earlier, a rewrite hidden as benign
   trailing prose could slip. The structural `NO_QUESTION` / `ENDS_IN_FIX` checks are the
   backstop (the read must close on a question, and a *phrased* fix after it is caught),
   and editor discipline (`rules.md` R1) is the first line — but the gap is real.
   **Recommend `OPEN-DEFECTS.md` (M4 creates it, M5 finalises) record this**, alongside
   the already-documented "gate cannot catch a well-formed but unwarranted finding"
   (`finding-schema.md` §8).
2. **Manifest parse edge:** a slide whose text literally contains a line `## Slide <n>`
   would be mis-split. Negligible for real A-level decks; harden only if a real deck ever
   trips it. **M4/M5.**
3. **Handle validation is structural, not membership.** If AB prefers the gate to warn
   when a handle is well-shaped but not in the published set, that is a small opt-in
   (`--strict-anchors`) a later pass can add; kept advisory-and-structural per M2.5
   open-question #2's own caution against breaking the gate on reference growth. **AB/M5
   decides.**
4. **Inherited (M1 open-question #1):** the residual "real run" wording in the seed files
   is untouched; M3's new artifacts use "constructed" / "fixture" and never call any run
   real. Still a human decision for M5's claims audit.

next-manifest-needs:
- **M4 is next, but the one human gate sits between M4 and M5** (`plan.md` §4). M3 did
  **not** start M4. M4 constructs the validation deck and persona (honestly labelled
  constructed), ships `runs/<teacher-id>/<date>/` with the answer key, runs the editor,
  and — the M3 hook — runs `extract.py` on the deck to produce `slide-manifest.md` and
  `check.py` against the produced critique, committing the PASS.
- **The finding format the gate enforces is fixed by `finding-schema.md` §1** (a
  `SEVERITY:` line then SLIDE/QUOTE/PRINCIPLE/SPEC/WHY/QUESTION, in order, one per line).
  M4's `critique.md` must conform verbatim or the gate blocks it. Invoke:
  `python check.py runs/<id>/<date>/critique.md runs/<id>/<date>/slide-manifest.md`;
  PASS = exit 0. Use `--json` for a machine-readable receipt if the run wants one.
- **The gate is not the answer key.** It proves the critique is well-formed, anchored,
  fabrication-free and rewrite-free; it cannot prove the findings are *right*. That is
  `runs/.../expected-findings.md` (M4), which measures precision/recall against ground
  truth — the deliberate limit in `finding-schema.md` §8.
- **`OPEN-DEFECTS.md`:** M4 should create-if-absent and record (a) the phrase-based
  rewrite-detection limit (open-question 1), (b) the unwarranted-finding limit (§8), and
  (c) the missing genuine-teacher run (M4's own guardrail). M5 finalises.
- **Advisory handle warnings** print to stderr and never block; M4's real critique should
  cite published handles (from `reference/spec/3.2-cell-structure.md` and
  `reference/exam-questions/cell-structure.md`) so none fire.
- **Reproduce M3 green from a fresh clone:** `pip install python-pptx==1.0.2` then
  `python tests/verify.py` and `python check.py --selftest`. CI does exactly this on
  every push.
