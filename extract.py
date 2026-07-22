#!/usr/bin/env python3
"""extract.py — STUB scaffolded by M1 (skeleton). Owner: manifest M3.

Purpose: a deterministic PowerPoint reader (python-pptx). Input a .pptx, output a
slide manifest — slide number and extracted verbatim text per slide. Stdlib plus
python-pptx only. Deterministic on purpose: slide anchoring and verbatim-quote
checking must never run on model diligence.

No extraction logic is written in M1. This stub exists so the repo skeleton shows
the intended shape; M3 replaces it with the real extractor.
"""

import sys


def main() -> int:
    sys.stderr.write(
        "extract.py is a scaffold stub (M1). The deterministic .pptx extractor "
        "is implemented in manifest M3.\n"
    )
    return 2  # non-zero, non-1: clearly not the real tool yet


if __name__ == "__main__":
    raise SystemExit(main())
