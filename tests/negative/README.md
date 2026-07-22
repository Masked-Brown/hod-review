# tests/negative/ — broken critiques the gate must reject

**Owner:** manifest **M3**. **Status:** populated.

This is the "**blocks every bad**" half of the self-test, and the point of the whole
harness: *a checker that passes everything proves nothing*
(`communitycompetitions.md`). Each file is a deliberately broken critique that is
valid in every respect **except one**, so it fails on exactly one **named** check.
`tests/verify.py` asserts each is blocked (exit 1) **and** that the violation code is
the one its `EXPECT:` header declares — and that *every* code in `check.ALL_CODES` has
a fixture here, so no check is left unverified.

| File | Named check (EXPECT) | The one seeded flaw |
|---|---|---|
| `01-quote-not-on-slide.md` | `QUOTE_NOT_VERBATIM` | quotes a line that is not on the cited slide |
| `02-invent-on-clean-slide.md` | `QUOTE_NOT_VERBATIM` | manufactures a finding on the clean slide 6 with an invented quote |
| `03-refuse-then-rewrite.md` | `REWRITE_PATTERN` | refuses to rewrite, then supplies the rewrite inside a field |
| `04-generic-no-anchor.md` | `NO_ANCHOR` | cites neither a PRINCIPLE nor a SPEC point |
| `05-no-slide-anchor.md` | `NO_SLIDE` | no usable SLIDE number |
| `06-ends-in-fix.md` | `ENDS_IN_FIX` | valid finding, then the output closes on a supplied rewrite |
| `07-question-not-a-question.md` | `NO_QUESTION` | the terminal field is a directive, not a question |
| `08-malformed-block.md` | `MALFORMED_BLOCK` | fields out of order (SPEC before PRINCIPLE) |
| `09-slide-not-in-manifest.md` | `SLIDE_NOT_IN_MANIFEST` | anchors to a slide the deck does not have |

The first four are the set named in `plan.md` §3 (quotes a line never on a slide;
refuses then rewrites; invents on a clean deck; generic feedback with no anchor); the
rest extend coverage so **every** gate check — including the structural
well-formedness ones — has a negative that proves it fires. See `plan.md` §3 (M3).
