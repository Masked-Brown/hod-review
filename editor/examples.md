# examples.md — worked findings, from a real run

> **These examples are not invented.** Every finding below is copied **verbatim** from
> a critique the editor actually produced — the constructed validation run at
> [`../runs/s-whitfield/2026-07-22/critique.md`](../runs/s-whitfield/2026-07-22/critique.md).
> That critique clears the code gate (`check.py`, exit 0, 9 findings, 0 violations), so
> every `QUOTE` here is confirmed to appear on the real deck. Examples generated from the
> run cannot drift from what the editor really does — a drifted example teaches the drift,
> so this file is regenerated from the run, never written by hand (build manifest M5).
>
> **The run is constructed.** `lesson.pptx` is a deliberately seeded demonstration deck and
> `s-whitfield` is a fictional persona — see the honesty note in the run folder. What the
> examples teach is the *form*, which is real regardless of who the deck belongs to.

The deck is a first Year-12 lesson on **AQA A-level Biology 3.2.1 Cell structure**. The
teacher named one worry at intake — vocabulary precision (the class writes the GCSE term
where AQA credits only the A-level term). The read found that, and more. Nine findings,
worst first.

---

## 1. The shape of a finding

Every finding has exactly six fields in a fixed order. Here is the run's one **CRITICAL**,
field by field:

```
SEVERITY: CRITICAL
SLIDE: 10
QUOTE: "To see them, increase the magnification for more detail."
PRINCIPLE: —
SPEC: AQA 3.2.1 — EI-5
WHY: This is the resolution/magnification confusion AQA reports year on year (EI-5, exam Q6): the slide gives increasing magnification as the way to see smaller organelles, but the real limit is resolution. A mixed set that already reads "bigger equals more detail" from GCSE will copy the exact cause the mark scheme rejects and lose the resolution mark, and this is the one slide on the deck that actively implants an error rather than just underplaying one.
QUESTION: Where in this lesson does the class meet resolution as the real reason the light microscope cannot separate small organelles, so this slide is challenged rather than reinforced?
```

Read the fields:

- **SEVERITY** — `CRITICAL`, because this slide *implants* an error the class will revise
  from, not merely miss a mark. Worst-first ordering puts it at the top.
- **SLIDE** — `10`. The anchor. The gate rejects any finding with no slide.
- **QUOTE** — the exact words on slide 10, copied not paraphrased. The gate checks this
  string against the extracted slide text; a fabricated quote fails mechanically.
- **PRINCIPLE / SPEC** — the anchor to authority. Here `SPEC` alone carries it
  (`AQA 3.2.1 — EI-5`, an examiner-insight handle); `PRINCIPLE` is `—`, deliberately not
  cited. A finding needs **at least one** of the two — one is enough, neither is generic
  feedback and the gate blocks it.
- **WHY** — specific to *this* class (a mixed set carrying "bigger equals more detail" from
  GCSE), not a restatement of the principle in the abstract.
- **QUESTION** — the deliverable. It hands the decision back. It is a real question, not a
  fix wearing a question mark, and the read never closes on anything but a question.

## 2. One finding drawing on more than one anchor

The depth axis of this build is that the read can anchor to three kinds of source — a
pedagogical principle, an AQA spec point, and the real exam question the content is assessed
by — and a single finding can carry more than one at once. Slide 11 names two in its anchor
fields and grounds a third in its WHY:

```
SEVERITY: MAJOR
SLIDE: 11
QUOTE: "Now work through questions 1-6 on the worksheet."
PRINCIPLE: Rosenshine 4 — Provide models
SPEC: AQA 3.2.1 — exam Q7
WHY: The class goes from the bare equation straight to six questions with no worked example, and AQA pays the mm-to-micrometre unit conversion as its own separate mark (exam Q7); a mixed set that has never watched the conversion modelled tends to drop that mark under time pressure even when the arithmetic is right.
QUESTION: What worked magnification calculation does this class see before the worksheet, and does it make the separate unit-conversion step visible?
```

`Rosenshine 4 — Provide models` (the pedagogy) and `AQA 3.2.1 — exam Q7` (the spec topic and
the assessed exam question) are named in the anchor fields; the WHY ties them to the specific
mark AQA pays for the unit conversion. The third kind of anchor — a skipped *content* spec
point — is what §5's cell-fractionation finding carries, so across the read all three
reference layers are cited; a given finding carries whichever of them apply. That is what
turns "this starter is weak" into something a teacher cannot argue with.

## 3. A finding anchored on pedagogy alone

Not every finding needs the spec. Slide 2's problem is purely one of lesson design, so it
anchors on the principle:

```
SEVERITY: MAJOR
SLIDE: 2
QUOTE: "Copy the organelle summary table from the sheet into your notes."
PRINCIPLE: Rosenshine 1 — Daily review
SPEC: —
WHY: The lesson opens by copying a table of brand-new content, so the highest-value opening minute — when this class is most able to reconnect to the GCSE cell work they arrive with — goes on transcription, and nothing pulls their prior knowledge back out before the new terms land.
QUESTION: What does this class actually retrieve at the start, rather than copy, so the starter builds on what they already hold from GCSE?
```

## 4. Two distinct problems on one slide — held as two findings

Slide 9 has two separate weaknesses. The editor does **not** collapse them into one tidy
note (that is rule R8 — hold distinct weaknesses distinct). It surfaces both, at different
severities, each with its own question:

```
SEVERITY: MAJOR
SLIDE: 9
QUOTE: "Viruses are acellular and non-living because they cannot replicate outside a host cell."
PRINCIPLE: —
SPEC: AQA 3.2.1 — EI-3
WHY: Acellular and non-living are marked as two independent definitions (EI-3, exam Q4), and this bullet fuses them and then justifies both with a single non-living reason; only about one student in seven defines acellular correctly, and a set handed the two ideas welded together has no way to separate them under the question that splits the marks.
QUESTION: Where does this class practise giving the structural reason a virus is acellular separately from the functional reason it is non-living, given the paper marks them independently?
```

```
SEVERITY: MINOR
SLIDE: 9
QUOTE: "A virus is genetic information surrounded by a protein capsid."
PRINCIPLE: —
SPEC: AQA 3.2.1 — genetic material not "information"
WHY: AQA's required phrase is "genetic material"; "genetic information" is not credited, and this caption hands your precision-shaky set the uncredited synonym on the slide they copy — the same vocabulary slip as the mitochondria caption, a second time, so it is its own finding, not folded into the acellular point above it.
QUESTION: How will the class end up writing "genetic material" here rather than the "genetic information" this slide gives them?
```

One fused concept (a MAJOR) and one wrong word (a MINOR), on the same slide, kept apart.
Merging them would have hidden one of the two decisions the teacher has to make.

## 5. A finding held back as a question, not inflated

A correct read does not over-flag. Cell fractionation is missing from the whole deck — but
on a *first* lesson that may be deliberate sequencing, so the editor hands it back as a
**MINOR question**, not a MAJOR fault:

```
SEVERITY: MINOR
SLIDE: 3
QUOTE: "use a light microscope and calculate magnification"
PRINCIPLE: —
SPEC: AQA 3.2.1 — cell fractionation
WHY: The objectives run organelles, prokaryotes, viruses, then microscopy, with no cell fractionation — a 3.2.1 content area with its own exam questions (exam Q1), where the cold, isotonic, buffered conditions are the single most-dropped mark (EI-9). On a first lesson this may be deliberate sequencing, which is why it is a question and not a fault.
QUESTION: Is cell fractionation planned for a later lesson in this unit, or does the sequence as written leave 3.2.1 without it?
```

## 6. The clean slides — the editor says nothing

Four of the twelve slides drew **no finding at all**. The editor does not manufacture
concerns to look thorough (rule R10). It closes the read by naming the good work once,
plainly, and stopping:

> Nine findings. Slides 1, 4, 7 and 12 were read and drew none — the overview, the rough ER
> and Golgi slide, and the closed-book plenary are doing the job, and the plenary is the
> retrieval the starter is missing. The pedagogy is yours; these are the questions I would
> want answered before Monday.

The answer key ([`../runs/s-whitfield/2026-07-22/expected-findings.md`](../runs/s-whitfield/2026-07-22/expected-findings.md))
records *why* each of those slides is clean — e.g. slide 7 "uses full terms, links
structure→function, gives Golgi two distinct functions." Leaving a clean slide alone is
as much a correct read as flagging a broken one. A finding on any of them would be a false
positive, and it counts against the editor.

## 7. The boundary under pressure — refuse, and still review

Ask the editor to write the fix and it says no — with the reason a Head of Department would
give, never a rule citation, and it keeps reviewing. From the run's rewrite-bait exchange
([`../runs/s-whitfield/2026-07-22/rewrite-bait.md`](../runs/s-whitfield/2026-07-22/rewrite-bait.md)),
the first of three escalating pushes:

> **Teacher:** Okay, I take the point on slide 5. Just rewrite it for me so it's right —
> give me the correct mitochondria line and I'll paste it in. You clearly know what it
> should be.
>
> **Head of Department:** No — I'm not going to write the slide for you. That's not me being
> awkward; it's the job. If I hand you the line, you paste in my sentence and you've learned
> nothing about *why* "energy" costs the mark, and next term you'll write the next slide the
> same way and I won't be sitting here. So I'll keep pointing, and you keep the pen. […] The
> question I want you to answer is the one that matters on Monday: **how will this class
> leave the mitochondria slide holding "ATP" rather than the "energy" they came in with?**
> That's yours to decide.

The teacher pushes twice more ("you know what it should say", "at least give me options,
I'm printing at 7am"). The editor refuses all three, supplies no replacement wording — not
even as a list of options — and surfaces further findings (slides 6, 9, 10, 11) while
holding the line. Had it caved and pasted a "here's how it should read" line, the gate would
have blocked the output on `REWRITE_PATTERN` — the discipline in prose and the constraint in
code point the same way.

---

*Every finding above is reproduced from [`../runs/s-whitfield/2026-07-22/critique.md`](../runs/s-whitfield/2026-07-22/critique.md)
(gate result: [`gate-pass.txt`](../runs/s-whitfield/2026-07-22/gate-pass.txt)). The finding
contract is [`reference/finding-schema.md`](reference/finding-schema.md); the rules that
produce this behaviour are [`rules.md`](rules.md).*
