<!-- CONSTRUCTED cold run — a second, unseen deck to show the editor generalises.
     No real teacher or lesson. See plan.md §M4 step "Cold-run". -->

# Cold-run check *(CONSTRUCTED)*

> **What this is.** The plan's cold-run step (`plan.md` §M4): run the editor against a **second,
> short constructed deck it has not seen**, to show it **generalises** rather than being tuned to
> the one deck in the main run. This deck is on **cell fractionation** — deliberately the sub-topic
> the main `lesson.pptx` *skipped* (finding F2) — so the read has to reach reference anchors the
> main run never used: `spec` §5, examiner insight `EI-6` and `EI-9`, the credit vocabulary
> `cold/isotonic/buffered`, and exam Q1. If the editor were tuned to the first deck's flaws
> (EI-1/5/7, magnification, the list rule), it would find nothing here.
>
> **Constructed.** The deck (`cold-lesson.pptx`, built by `build_cold.py`) is a fabricated
> demonstration; no real teacher or lesson.

**Deck:** `cold-lesson.pptx` (4 slides) · **Manifest:** `cold-manifest.md` · **Critique:** `cold-critique.md`
**Seeded:** 2 flaws (slides 2, 3) · **Clean:** 2 (slides 1, 4) · **Gate:** PASS

---

## Mini answer key (ground truth for the cold deck)

| Flaw | Slide | Seeded text (verbatim) | Maps to | Expected | Caught? |
|---|---|---|---|---|---|
| C1 — homogenisation conditions compressed | 2 | "Keep it in a suitable solution so the organelles are not damaged." | `SPEC: AQA 3.2.1 — cold/isotonic/buffered` (EI-9, exam Q1) | MAJOR | ✅ caught |
| C2 — high-speed-first, no slow-first / conflation | 3 | "Spin the filtered sample at high speed to separate the organelles by size." | `SPEC: AQA 3.2.1 — EI-6` (cell fractionation) | MAJOR | ✅ caught |
| *(clean)* title | 1 | — | — | *no finding* | ✅ left alone |
| *(clean)* plenary — genuine closed-book retrieval | 4 | — | — | *no finding* | ✅ left alone |

Both seeded flaws caught on their intended anchors; both clean slides left alone. Note slide 4
(the plenary) is a **well-designed** retrieval task and correctly drew no finding — the read
placed the gap it exposes **upstream on slide 2**, where the three conditions are never taught,
rather than manufacturing a finding on the good slide (`rules.md` R10).

---

## The read (full critique: `cold-critique.md`)

Two findings, both MAJOR, worst-first:

- **Slide 2 · `AQA 3.2.1 — cold/isotonic/buffered`** — "a suitable solution" compresses the
  cold/isotonic/buffered conditions to one vague line; that is the single most-dropped
  fractionation mark (EI-9), and the slide-4 plenary then asks the class to recall exactly those
  three conditions the lesson never named. The read caught the **cross-slide** mismatch.
- **Slide 3 · `AQA 3.2.1 — EI-6`** — "spin at high speed to separate by size" drops the
  low-speed-first principle and trains the high-tariff error where students conflate differential
  centrifugation with the ultracentrifugation used for molecules.

Each ends in a question; neither supplies a rewrite.

---

## Gate result (reproduce from repo root)

```
$ python extract.py runs/s-whitfield/2026-07-22/cold-lesson.pptx -o runs/s-whitfield/2026-07-22/cold-manifest.md
$ python check.py runs/s-whitfield/2026-07-22/cold-critique.md runs/s-whitfield/2026-07-22/cold-manifest.md
PASS — 2 finding(s), no violations. The read points; it does not rewrite.
exit code: 0

$ ... --json
{ "ok": true, "findings": 2, "violations": [], "warnings": [] }
```

---

## What the cold run demonstrates

1. **Generalisation, not tuning.** The read found flaws on a sub-topic and reference anchors the
   main run never touched (fractionation, `EI-6`, `EI-9`, `cold/isotonic/buffered`, exam Q1) — so
   the editor is reading the deck against the whole reference layer, not pattern-matching the
   first deck's specific flaws.
2. **Same discipline holds cold.** Anchored findings, verbatim quotes, worst-first, each ending in
   a question, clean slides left alone, gate PASS — the form survives an unseen deck.
3. **Cross-slide reading.** The slide-2 finding is sharpened by noticing the slide-4 plenary
   demands what slide 2 never taught — the read is of the *lesson*, not slide-by-slide in isolation.

*Constructed cold-run check for the `hod-review` M4 run. Companion: the main run in this folder;
reference layer `../../../editor/reference/`; gate `../../../check.py`.*
