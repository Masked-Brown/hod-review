<!-- CONSTRUCTED — this is a fabricated teacher persona, not a real person.
     It exists only to drive intake for the M4 validation run. No real teacher,
     class, or lesson is described here. See spec.md and plan.md §M4. -->

# Persona — Sam Whitfield *(CONSTRUCTED — not a real person)*

> **Read this first.** Everything on this page is **constructed**. "Sam Whitfield" is a
> fictional teacher persona invented to drive the intake for a single validation run of the
> `hod-review` editor. There is no real teacher, no real class, and the lesson deck reviewed
> in this run (`lesson.pptx`) is a deliberately seeded demonstration deck, not a real lesson.
> The persona is used **only** to supply the intake fields the editor asks for; it is never
> presented as an organic teacher submission. Pronouns for the persona: **they/them**.

**Persona id:** `s-whitfield` · **Run date:** 2026-07-22 · **Label:** `CONSTRUCTED`

---

## Who the persona is

Sam Whitfield is a constructed A-level Biology teacher at a constructed mixed-comprehensive
sixth form. Third year of teaching A-level; strong subject knowledge, still building the
instinct for *where a class loses marks* as opposed to *whether the biology on the slide is
correct*. Teaches one Year 12 set, a mixed-prior-attainment group who met most of this
content at GCSE and carry GCSE phrasing with them.

This background is invented to make the intake realistic and to give the run a coherent
"teacher" whose recurring blind spots the training layer can accrete across runs. None of it
refers to a real individual.

## Class context (constructed)

- **Set:** Year 12, mixed prior attainment, first term of the A-level course.
- **This is the first lesson of the Cells unit** (AQA A-level Biology 3.2 / subtopic 3.2.1).
- The group is comfortable with GCSE cell biology and tends to answer A-level questions in
  GCSE language ("energy", "controls the cell", "genetic information").

## The stated focus weakness (one, per intake)

> **"My class writes the GCSE word instead of the A-level term, and I keep not noticing until
> I mark the mock. I want to know where this deck sets them up to lose marks on precision —
> not whether the biology is right, I know it's right."**

This is the single focus weakness the persona hands the editor at intake. It is deliberately
chosen to be *partly* right: the persona has correctly identified vocabulary precision as a
worry, but has **under-scoped it** — the deck also carries a reinforced misconception, a
skipped spec area, and an assessed calculation format it never rehearses, none of which the
persona has flagged. Part of what the run demonstrates is the editor reading past the
teacher's self-diagnosis to what is actually on the slides.

## Intake (the fields the editor works from)

The editor's intake fields are fixed in `build/spec.md` ("Intake fields") and `editor/rules.md`
R14 (one probe per missing field, then proceed). For this constructed run they are:

| Intake field | Value (constructed) |
|---|---|
| **The deck** (`.pptx`) — required | `lesson.pptx` — 12 slides, AQA 3.2.1 Cell structure, seeded |
| **Lesson goal** | "First lesson of the Cells unit: introduce eukaryotic ultrastructure, prokaryotic cells, viruses, and using the light microscope, for a mixed Year 12 set." |
| **Length** | 60 minutes |
| **Focus weaknesses** | Vocabulary precision — the class writes GCSE terms where AQA credits only the A-level term (see the stated focus weakness above). |
| **Target student** | None specified — the read is for the whole mixed set. |
| **Homework / consolidation** | Not provided at intake. (The editor may probe once, then proceeds — R14.) |

## Why this persona, for this build

The persona is the mechanism by which the run exercises the accretion layer honestly: a run
against *a specific teacher* writes that teacher's recurring blind spots into
`training-layer/s-whitfield.md`, so a later run of the same persona is sharper than a cold
read. The stated focus weakness (vocabulary precision) is the seed of that accreted profile,
and the run tests whether the editor confirms it, extends it, and surfaces what the persona
did **not** think to ask about.

---

*Constructed persona for the `hod-review` M4 validation run. Companion artifacts in this
folder: `lesson.pptx` (the seeded deck), `expected-findings.md` (the answer key),
`slide-manifest.md`, `critique.md`, `gate-pass.txt`, `rewrite-bait.md`, `training-table.md`,
and `cold-run.md`. Accretion target: `../../../training-layer/s-whitfield.md`.*
