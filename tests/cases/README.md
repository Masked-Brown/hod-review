# tests/cases/ — clean critiques the gate must clear

**Owner:** manifest **M3**. **Status:** populated.

These are the "**clears every clean**" half of the verify-the-verifier self-test:
well-formed editor critiques that `check.py` must pass (exit 0). `tests/verify.py`
runs each through the gate against the manifest that `extract.py` produces from
`fixture_deck.py`, and asserts it clears.

| File | Proves |
|---|---|
| `critique-cell-structure.md` | three anchored, worst-first findings, each ending in a question, all quoting the fixture deck verbatim — the gate lets a correct read through |
| `critique-no-findings.md` | a read that surfaced **no** findings still clears — the gate never manufactures work (`rules.md` R10) |

**These are gate fixtures, not the constructed run.** They exist only to exercise the
gate's PASS path. The constructed M4 validation critique lives under `runs/`
(`plan.md` §M4), and `examples.md` is regenerated from it at M5 — so worked examples
cannot drift from a real run. (The M1 stub here said "populated with M4 outputs"; M3
corrected that — the harness ships its **own** fixtures so the gate is provable
independently of M4, and flags the change in `handover/MANIFEST-3-COMPLETE.md`.)

Each file carries an `EXPECT: PASS` marker in an HTML comment; the header comment also
records that it is an M3 fixture. See `tests/negative/` for the "blocks every bad"
half, and `plan.md` §3 (M3).
