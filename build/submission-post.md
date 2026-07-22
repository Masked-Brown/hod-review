# build/submission-post.md — the community submission draft

Draft copy for the competition comment and the short pitch a judge reads before opening the
repo. Kept in `build/` because it is submission scaffolding, not part of the shipped editor.

---

## The comment (2–3 sentences)

> **hod-review** — an editor that reviews **AQA A-level Biology lesson decks** the way a Head
> of Department reads your slides before Monday: it points at what will fail with your class,
> triple-anchored to the pedagogy, the AQA spec point, and the real exam question — and hands
> the fixing back. It never rewrites your lesson, and that's not a promise in prose: a
> self-tested code gate blocks any output that rewrites a slide, fabricates a quote, or ends in
> a fix instead of a question. For A-level Biology teachers and the HoDs who'd otherwise do the
> read by hand.

*One-line differentiator, if only one line is wanted:* **the no-rewrite rule is enforced in
code, findings are quote-checked against a real `.pptx`, and every finding cites three sources
where the field cites one.**

## The pre-read paragraph (what a judge reads before opening the repo)

> This is a review tool for one narrow, real job: reading an AQA A-level Biology lesson
> PowerPoint and telling the teacher, as a senior colleague would, where it will lose the class
> marks — without ever rewriting it for them. Three things make it worth a look. First,
> enforcement: the no-rewrite invariant lives in a blocking, self-tested Python gate
> (`check.py`), not in prose the model can drift from — `python tests/verify.py` proves it
> clears every clean critique and blocks every broken one on its exact named check. Second, a
> binary input no one else in the field touches: it ingests a real `.pptx` through a
> deterministic extractor and quote-checks every finding against the extracted slide text, so a
> fabricated quote fails mechanically. Third, depth: each finding anchors to the pedagogical
> principle, the AQA spec point, and the exam question the content is assessed by — three
> sources where the bar cites one. A 60-second verify path is in `JUDGE_GUIDE.md`. The
> validation runs are honestly labelled **constructed** — no real teacher run exists yet, and
> `OPEN-DEFECTS.md` says so plainly — but the editor is shipped reading decks it wasn't built
> around, in fresh chats, and the same `editor/` folder reproduces the same structured output
> every time.

---

*Post the comment and the pre-read paragraph together, or the comment alone if length is
capped. Do not mark the entry submitted until AB approves this M5 layer.*
