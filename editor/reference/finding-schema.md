# finding-schema.md — the finding contract

> **What this is.** The exact shape of a finding: the fields the editor emits and the
> fields the gate (manifest M3) parses and enforces. This is the single contract shared
> by the editor and the gate — one file, one job. If the editor and the gate ever disagree
> about what a finding is, this file is the source of truth and both are wrong until they
> match it.

The six fields of the contract are **SLIDE, QUOTE, PRINCIPLE, SPEC, WHY, QUESTION**. This
file makes them machine-parseable and states, field by field, what is *enforced in code*
versus what is *editor discipline*.

---

## 1. The block format

A finding is a block of exactly seven lines — a `SEVERITY` line followed by the six schema
fields — each on its own line, keyed by an uppercase label and a colon, **in this fixed
order**:

```
SEVERITY: CRITICAL
SLIDE: 6
QUOTE: "the exact wording copied from slide 6, verbatim"
PRINCIPLE: CLT — redundancy effect
SPEC: —
WHY: One or two sentences on why this fails with this class, given the intake context.
QUESTION: The question handed back to the teacher, ending in a question mark?
```

Rules of the format, so a parser is unambiguous:

- **One field per line.** The key is the text before the first colon; the value is
  everything after the first colon and one space, trimmed. `WHY` and `QUESTION` may be long
  but are a single logical line (no hard line breaks inside a field).
- **Fixed order**, every field present. A field the editor cannot fill for `PRINCIPLE` or
  `SPEC` is written as an em dash `—` (see §4). `SLIDE`, `QUOTE`, `WHY`, `QUESTION` are never
  empty.
- **Blocks are separated by one blank line.** A new `SEVERITY:` line begins the next finding.
- Findings live under a top-level `# Findings` heading in the critique, emitted in severity
  order (§5). Prose outside that section (intake echo, a one-line closing) is allowed but is
  **not** part of any finding and must itself contain no rewrite (§6).

### How the gate locates a finding

The gate scans for lines matching `^SEVERITY:\s*(CRITICAL|MAJOR|MINOR)\s*$`. Each match
opens a finding; the next six non-blank lines are read as the fields by their key prefixes
(`SLIDE:`, `QUOTE:`, `PRINCIPLE:`, `SPEC:`, `WHY:`, `QUESTION:`). A finding missing a field,
or with fields out of order, is malformed and the gate blocks it. This keeps parsing a line
scan, not a Markdown parse.

## 2. `SLIDE`

- An integer: the slide number from the extracted manifest (the extractor's output).
- **Enforced:** the value must be a positive integer, and that slide number must exist in the
  extracted manifest for the deck under review. A finding with no `SLIDE`, or a `SLIDE` not in
  the manifest, is blocked. *(gate check: "A finding with no SLIDE anchor.")*

## 3. `QUOTE`

- The exact wording from that slide, wrapped in straight double quotes: `QUOTE: "..."`.
- The gate takes the text between the first and last double quote on the line as the quoted
  span.
- **Enforced — the fabrication check (the load-bearing one).** The quoted span must appear
  **verbatim** in the extracted text of the cited `SLIDE`. This is claimline's Rule 0 applied
  to slides: a finding that quotes a line not on the slide fails mechanically, however
  competent it reads. *(gate check: "A QUOTE that does not appear verbatim in the extracted
  slide manifest.")*

### The verbatim-match rule (defined once, here)

To be deterministic across PowerPoint's line-wrapping and spacing quirks while staying a
true fabrication check, the comparison is:

1. Take the quoted span and the extracted text of the cited slide.
2. **Normalise whitespace** on both: collapse every run of whitespace (spaces, tabs,
   newlines) to a single space, then trim ends.
3. **No case folding, no punctuation stripping.** The match is otherwise exact.
4. The `QUOTE` passes if its normalised form is a **substring** of the normalised slide text.

The editor must therefore quote real words in real order — paraphrase fails. Whitespace and
line-wrap differences do not. (Known edge for M3: typographic vs straight quotes/apostrophes
inside the quoted text — M3 decides whether to also normalise `’“”` to ASCII; flagged in the
M2 handover, not fixed here.)

## 4. `PRINCIPLE` and `SPEC` — the anchor

- **`PRINCIPLE`** — a citable handle from `reference/frameworks/` (e.g. `Rosenshine 1 — Daily
  review`, `CLT — split-attention effect`), or `—` if not used.
- **`SPEC`** — an AQA spec point or required practical from `reference/spec/` (authored in
  M2.5), or `—` if not used.
- **Enforced:** at least one of `PRINCIPLE` / `SPEC` must be a real citation (not `—`). A
  finding with neither is generic feedback, and the gate blocks it. *(gate check: "A finding
  citing neither a PRINCIPLE nor a SPEC point.")*
- **Discipline (not code):** that the cited handle is the *right* one, and that it names a
  real entry in `reference/`, is editor judgement. M3 *may* optionally validate the handle
  against the known set from `reference/frameworks/` and `reference/spec/`; this file defines
  the handles so that option exists, but does not require it, so M2.5 can extend the spec
  handles without breaking the gate.

On the validated topic a finding can carry **all three** anchors — principle, spec, and (via
the `WHY`/`QUESTION`) the assessment alignment from `reference/exam-questions/` — which is
the triple-source depth the field bar does not reach.

## 5. `SEVERITY` and ordering

Every finding carries exactly one severity, and findings are emitted **worst-first**:

- **CRITICAL** — the slide will actively mislead or lose the class: it teaches a
  misconception, reverses a key distinction, or omits something the lesson's own stated goal
  depends on. Left unfixed, students leave with the wrong model.
- **MAJOR** — the slide will underperform: a principle is violated or a spec point skipped in
  a way that measurably weakens learning, but it does not implant an error.
- **MINOR** — a real but low-cost issue: friction, a smaller clarity or sequencing problem, a
  missed opportunity. Worth a question, not worth derailing the lesson.

Ties within a tier are broken by slide order. A clean slide produces **no** finding.
*(Severity is editor judgement; the gate checks only that the label is one of the three and
that the block is well-formed — the gate never grades pedagogy.)*

## 6. `WHY` and `QUESTION`, and the no-fix rule

- **`WHY`** — one or two sentences on why this fails *with this class*, specific to this
  lesson and the intake context. Not a restatement of the principle. *(Discipline; the
  specificity criterion.)*
- **`QUESTION`** — the decision handed back to the teacher, phrased as a genuine question and
  ending in `?`. Never a fix, and never a leading question with a single intended answer (a
  fix in disguise). *(rules.md R7.)*
- **Enforced:** every finding ends in `QUESTION`, and the critique as a whole ends on
  findings — never on supplied replacement content. The gate blocks:
  - any finding whose terminal field is not `QUESTION`, or whose `QUESTION` does not end in
    `?`;
  - any `QUESTION` (or any text in the document) matching a **rewrite / fix pattern** — e.g.
    "here's a better…", "here's how I'd write it", "try this instead", "change it to…", "it
    should say…", "replace … with …", "rewritten:". *(gate checks: "Rewritten slide content, or a
    'here's a better version' pattern," and "An output that ends in a fix rather than a
    QUESTION." The exact pattern list is operationalised in the gate.)*

## 7. What the gate blocks — the checklist

The gate reads the critique and the extracted manifest and fails (exit 1) on any of:

1. A rewrite / "better version" pattern anywhere in the output.
2. A finding with no `SLIDE` anchor (or a `SLIDE` not in the manifest).
3. A `QUOTE` that is not verbatim in the cited slide's extracted text (fabrication check, §3).
4. A finding citing neither `PRINCIPLE` nor `SPEC`.
5. An output that ends in a fix rather than a `QUESTION`.
6. *(Well-formedness, implied by the above)* a malformed finding block — missing field, wrong
   order, empty required field, unknown severity.

The gate **reports facts and blocks**. It never judges whether a finding is pedagogically
right — that is the editor's job (`rules.md` R16).

## 8. What the gate cannot do — stated honestly

The verbatim and anchor checks make *fabricated* and *unanchored* findings fail mechanically.
They **cannot** catch a finding that is well-formed but *unwarranted* — a real quote plus a
real principle attached to a slide that was actually fine. Nothing in code can, because that
is a pedagogical judgement and the gate is forbidden from making it. That gap is covered two
other ways: by editor discipline (`rules.md` R10 — do not manufacture findings) and, in the
constructed run, by its answer key (M4) — the record that measures the
editor's precision and recall against known ground truth. This limit is deliberate and is
recorded, not hidden.

---

*This file is the schema's source of truth; it makes the schema parseable and assigns each rule
to code or to discipline. The gate implements §1–§7. M2.5 extends the `SPEC`
handle set without changing this format.*
