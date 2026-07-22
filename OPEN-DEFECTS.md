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

## 3. No real teacher run exists — every run is constructed

There is **no genuine teacher, deck, or lesson** in this build. Every run shipped under
`runs/` is a **deliberately constructed demonstration case**, labelled `CONSTRUCTED` (never
`REAL`) in every artifact, as the README honesty note states.

Two gradations, both honest:

- The `s-whitfield` run is a **self-consistency test** — the same author built the seeded deck
  and the answer key, so its 9/9 score proves the *mechanism* end to end, not blind precision.
- The `blind-01` / `blind-02` runs are **blind to the editor** (read in fresh chats with no
  answer key in view) but the decks are still **author-built**. They test the editor on
  material it was not tuned to, but not on the messiness of a real teacher's real deck.

A `REAL` training run — a genuine teacher on a genuine lesson — is a **reserved next step**,
named here, not implied to be done. The training table has no `REAL` rows and will not until
that run happens.

## 4. Only one topic is built to full depth

The bespoke reference layer scaffolds the full AQA A-level Biology topic map (3.1–3.8), but only
**3.2.1 Cell structure** is populated to full depth (content index, examiner-insight block,
distilled exam questions). A lesson on any other topic gets the scaffold — the topic code and
scope — but not the deep anchors, so a finding on it can name the spec area yet cannot cite a
specific misconception or exam question the way a 3.2.1 finding can. Each `3.x` topic is built to
depth only when a lesson on it is reviewed (`editor/reference/spec/aqa-biology-index.md`).
Extending depth to more topics — and, further out, to wider A-level Science — is a next step,
not something this build ships.
