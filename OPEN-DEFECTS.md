# OPEN-DEFECTS.md

**Purpose:** an honest register of what this build does *not* cover, so no README claim
outruns the repo. The list is stated plainly; nothing here is hidden behind optimism.
Manifest **M4** logs the constructed-run entry (defect 3); manifest **M5** finalises the
list. What is already known is written down now.

---

## 1. The gate cannot catch a rewrite pasted in with no give-away phrase

The gate's rewrite detection (`check.py`) is a **heuristic phrase list** — "here's a
better version", "it should read", "replace X with Y", and kin. It catches a rewrite
that *announces itself*. It **cannot** catch rewritten slide content pasted in with no
tell-tale phrasing: prose that quietly re-authors the slide but never trips a pattern
passes the rewrite scan. The verbatim-`QUOTE` and end-in-a-`QUESTION` checks are the
structural backstop — a fabricated quote or an output that closes on a fix still fails
— but a well-disguised rewrite between them is a real hole, not a solved problem. This
limit is stated in `check.py` itself.

## 2. The gate cannot catch a well-formed finding that is simply wrong on the pedagogy

The gate checks *form*, never *correctness*. A finding can be perfectly well-formed —
a real slide, a verbatim quote, a real principle or spec handle, a genuine question —
and still be **pedagogically wrong**: the wrong lens cited, a misread of the slide, a
concern that does not apply to this class. Nothing in code can judge that, and the gate
is forbidden from trying (`check.py`: it reports facts and blocks; it never grades
pedagogy). This gap rests on editor discipline, and — in the constructed run — on the
answer key that measures the editor's findings against known ground truth. It is not
closed by the gate.

## 3. No real teacher run exists — the M4 run is a constructed demonstration

There is **no genuine teacher, deck, or lesson** in this build. The validation run
shipped under `runs/` is a **deliberately constructed demonstration case**, labelled
`CONSTRUCTED` (never `REAL`) in every artifact, as the README honesty note states. A
`REAL` training run — a genuine teacher on a genuine lesson — is a **reserved next
step**, named here, not implied to be done.
