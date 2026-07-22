#!/usr/bin/env python3
"""tests/verify.py — STUB scaffolded by M1 (skeleton). Owner: manifest M3.

Purpose: run the gate (check.py) over the shipped example critiques in tests/cases/
and assert the contract. With --selftest, prove both directions — every clean
critique clears, every deliberately broken critique in tests/negative/ is rejected
on its named check ("a checker that passes everything proves nothing").

No test logic is written in M1. M3 replaces this stub with the real harness.
"""

import sys


def main() -> int:
    sys.stderr.write(
        "tests/verify.py is a scaffold stub (M1). The verify-the-verifier harness "
        "is implemented in manifest M3.\n"
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
