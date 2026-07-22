#!/usr/bin/env python3
"""check.py — STUB scaffolded by M1 (skeleton). Owner: manifest M3.

Purpose: the blocking gate. Reads the editor's critique output and fails (exit 1) if
any finding contains rewritten slide content or a "here's a better version" pattern;
any finding has no slide anchor; any QUOTE does not appear verbatim in the extracted
slide manifest (the fabrication check); any finding cites neither a PRINCIPLE nor a
SPEC point; or the output ends in a fix rather than a QUESTION. The gate reports facts
and blocks — it never judges pedagogical quality (that is the editor's job).

No gate logic is written in M1. This stub exits 2 (not 0, not 1) so it can never be
mistaken for a passing or blocking gate. M3 replaces it with the real checker.
"""

import sys


def main() -> int:
    sys.stderr.write(
        "check.py is a scaffold stub (M1). The blocking gate is implemented in "
        "manifest M3. Exit 2 = not yet the gate (not a PASS, not a BLOCK).\n"
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
