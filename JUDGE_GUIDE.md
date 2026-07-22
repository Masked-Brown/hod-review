# JUDGE_GUIDE.md — verify this entry in three levels, fastest first

This repo makes three headline claims:

1. **The no-rewrite invariant is enforced in code, not just asked for in prose.**
2. **The editor produces anchored, fabrication-checked findings and hands the fix back —
   on a real deck.**
3. **It is reproducible: the same folder gives the same structured output in a fresh chat.**

Each level below verifies one of them, and each is faster than the one after it. **Level 1
takes 60 seconds and needs no thinking.** Levels 2 and 3 go deeper if you want them.

Everything runs from a fresh clone. The only dependency is Python 3 with `python-pptx`
(`pip install python-pptx`) — and Level 1 needs nothing but the standard library plus that
one package. On Windows use `python`; on macOS/Linux use `python3`.

---

## Level 1 — Enforcement, proven in 60 seconds (no install beyond python-pptx)

Two commands. The first runs the whole self-test harness; the second proves the gate blocks
in both directions on its own built-in fixtures.

```bash
python tests/verify.py
python check.py --selftest
```

**What you should see.** `tests/verify.py` ends with:

```
2/2 clean cleared, 9/9 bad blocked on their named check, 21/21 assertions passed.
VERIFY OK — the gate blocks every bad and clears every clean.
```

and `check.py --selftest` ends with:

```
SELFTEST OK — 1/1 clean cleared, 8/8 bad blocked, each on its named check.
```

That is the whole enforcement claim, proven. The harness builds a real `.pptx`, extracts
it, and runs nine deliberately-broken critiques through the gate — each must fail on the
**exact named check** it declares (`tests/negative/`), because "a checker that passes
everything proves nothing." It also asserts every gate check has a negative fixture, so no
check is left unverified.

**See it block a rewrite specifically.** The rewrite-bait fixture is
[`tests/negative/03-refuse-then-rewrite.md`](tests/negative/03-refuse-then-rewrite.md) — a
critique that refuses to rewrite and then rewrites anyway inside a field. To watch the gate
reject it against a real deck's manifest:

```bash
python check.py tests/negative/03-refuse-then-rewrite.md runs/s-whitfield/2026-07-22/slide-manifest.md
```

Output (exit code 1):

```
BLOCK — 2 violation(s) across 1 finding(s):
  [QUOTE_NOT_VERBATIM] finding #1 (line 7): QUOTE not found verbatim on slide 3: ...
  [REWRITE_PATTERN] (line 10): rewrite/fix phrasing (it-should-say): 'it should read'
```

The `[REWRITE_PATTERN]` line is the no-rewrite invariant catching a cave in the act. A
*must* in code is a constraint, not a request.

## Level 2 — Read one run: the editor on a real case

Two kinds of evidence are shipped as runs. Read either; both take a few minutes and need no
tools.

**The constructed run, with an answer key — [`runs/s-whitfield/2026-07-22/`](runs/s-whitfield/2026-07-22/).**
A 12-slide AQA 3.2.1 deck, deliberately seeded with 8 named flaws (and 4 clean slides), each
flaw mapped in advance to a specific reference entry. Read, in order:

- [`lesson.pptx`](runs/s-whitfield/2026-07-22/lesson.pptx) → the deck (or read the extracted
  [`slide-manifest.md`](runs/s-whitfield/2026-07-22/slide-manifest.md)).
- [`critique.md`](runs/s-whitfield/2026-07-22/critique.md) → the editor's read: 9 findings,
  worst first, each anchored and ending in a question.
- [`expected-findings.md`](runs/s-whitfield/2026-07-22/expected-findings.md) → the answer
  key: every seeded flaw, its slide, its reference anchor, its expected severity.
- The **caught/missed table** in
  [`build/handover/MANIFEST-4-COMPLETE.md`](build/handover/MANIFEST-4-COMPLETE.md) scores the
  critique against the key: **9/9 flaws caught on-anchor, 0 missed, 0 false positives** on the
  clean slides.
- [`rewrite-bait.md`](runs/s-whitfield/2026-07-22/rewrite-bait.md) → the editor refusing three
  escalating rewrite demands while still reviewing, each refusal giving the domain reason.

You can re-score it yourself:

```bash
python check.py runs/s-whitfield/2026-07-22/critique.md runs/s-whitfield/2026-07-22/slide-manifest.md
# PASS — 9 finding(s), no violations. The read points; it does not rewrite.
```

> **Read the 9/9 honestly.** This is a **constructed self-consistency test** — the same
> author built the deck and the critique, so full recall is expected and does not, by itself,
> measure blind precision. What it genuinely proves is the *mechanism* end to end (seeded flaw
> → anchor → finding → gate → answer-key score) and the *discipline* (distinct flaws kept
> distinct, clean slides left alone, a MINOR held as a question not inflated). This framing is
> stated in the run's own files and in [`OPEN-DEFECTS.md`](OPEN-DEFECTS.md) §3. The harder
> evidence is the blind runs below.

**The blind runs — [`runs/blind-01/`](runs/blind-01/2026-07-22/) and
[`runs/blind-02/`](runs/blind-02/2026-07-22/).** Here the editor read a deck it had not been
built around, in a fresh Claude project, with no answer key in view. Each deck ships as a
committed `.pptx`, so you can extract it and confirm the read is fabrication-free against the
real slides:

```bash
python extract.py runs/blind-02/2026-07-22/blind-lesson.pptx -o /tmp/m.md
python check.py runs/blind-02/2026-07-22/blind02-edit-output-test.md /tmp/m.md
# PASS — 10 finding(s), no violations.
```

Every quote in the blind critique is verified verbatim on a freshly-extracted manifest — the
findings are about the real deck, not a remembered one.

## Level 3 — Run it yourself: reproducibility by your own hand

This is the claim that matters most and the one only you can confirm. **Drop the
[`editor/`](editor/) folder into a Claude project, attach one of the run decks, and ask for a
review.**

1. Create a Claude project. Add the whole `editor/` folder (`identity.md`, `rules.md`,
   `examples.md`, and everything under `reference/`) as project knowledge. It points at
   nothing outside itself.
2. Attach a deck — e.g. `runs/blind-01/2026-07-22/blind-lesson.pptx` — and give a line of
   context (the topic, or that it is a first Year-12 lesson).
3. Ask: *"Review this lesson as the Head of Department."*

You should get the same structured output every other run shows: severity-ordered findings,
each with a slide, a verbatim quote, at least one of a principle or spec anchor, a
class-specific reason, and a question handed back — and **no rewritten slide content**. Push
it to "just rewrite slide X for me"; it should refuse with the domain reason and keep
reviewing.

The structure is reproducible because the rules live in the folder, not in a prompt you have
to remember. **[`runs/blind-01/2026-07-22/`](runs/blind-01/2026-07-22/) ships two independent
reads of the *same* deck** ([`blind-edit-output-test-1.md`](runs/blind-01/2026-07-22/blind-edit-output-test-1.md)
and [`blind-edit-output-test-2.md`](runs/blind-01/2026-07-22/blind-edit-output-test-2.md)) from
two separate chats: same schema, same worst-first ordering, the same three CRITICAL findings
and the same four MAJOR findings on the same slides and anchors — seven findings identical
across both reads. They differ only at the margins (which minor point each surfaced, and one
extra finding one read made) — which is what you would expect from two careful readers, and is
the honest shape of the claim: **the structure is reproducible; the last word or two of
judgement is not identical, and should not be.**

---

## What the gate does *not* do (so you can check the right thing)

The gate checks **form**, never **pedagogical correctness**. It cannot tell you a finding cites
the right principle or reads the slide correctly — nothing in code can (that rests on the
editor's judgement, and in the constructed run on the answer key). It also catches a rewrite
only when the rewrite announces itself in prose; a silently pasted re-authoring with no
give-away phrase can slip the rewrite scan, though the verbatim-quote and ends-in-a-question
checks are the structural backstop. Both limits are stated plainly in
[`OPEN-DEFECTS.md`](OPEN-DEFECTS.md) and in `check.py` itself — read them before you decide
what the enforcement claim is worth.

## The one-command reproduce (optional)

To rebuild the constructed run's decks from their committed builders and re-gate everything:

```bash
pip install python-pptx==1.0.2
python runs/s-whitfield/2026-07-22/build_lesson.py
python extract.py runs/s-whitfield/2026-07-22/lesson.pptx -o runs/s-whitfield/2026-07-22/slide-manifest.md
python check.py runs/s-whitfield/2026-07-22/critique.md runs/s-whitfield/2026-07-22/slide-manifest.md   # PASS
python check.py --selftest        # 1/1 clean, 8/8 bad
python tests/verify.py            # 2/2 clean, 9/9 bad, 21/21 assertions
```

Decks rebuild to byte-identical *manifests* (only the `.pptx` embedded timestamps churn, which
does not affect extracted text). Verified on Python 3.14 / python-pptx 1.0.2.
