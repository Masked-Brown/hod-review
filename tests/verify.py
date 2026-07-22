#!/usr/bin/env python3
"""tests/verify.py — verify the verifier (manifest M3).

Proves the gate **both directions** over the real pipeline, on shipped fixtures:

    fixture_deck.build()  ->  extract.py  ->  slide manifest  ->  check.py

1. Round-trips the fixture deck through `extract.py` and confirms the verbatim slide
   text survives, so the fabrication check has real ground truth.
2. Runs every critique in `cases/` through the gate and asserts it **clears** — the
   "clears every clean" half.
3. Runs every critique in `negative/` through the gate and asserts it is **blocked on
   the exact named check** its `EXPECT:` header declares — the "blocks every bad"
   half. "A checker that passes everything proves nothing" (`communitycompetitions.md`).
4. Asserts every gate check in `check.ALL_CODES` has at least one negative fixture, so
   no check is left unverified.
5. Exercises the `extract.py` and `check.py` CLIs (exit 0 pass / 1 block) and
   `check.py --selftest`.

Exit 0 iff every assertion holds. Stdlib + python-pptx only. Run: `python tests/verify.py`.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
for path in (ROOT, HERE):
    if path not in sys.path:
        sys.path.insert(0, path)

import check          # noqa: E402  (repo-root module)
import extract        # noqa: E402  (repo-root module; imported to prove it loads)
import fixture_deck   # noqa: E402  (tests/ module)

CASES_DIR = os.path.join(HERE, "cases")
NEG_DIR = os.path.join(HERE, "negative")
PY = sys.executable
_EXPECT_RE = re.compile(r"EXPECT:\s*([A-Z_]+)")


class Reporter:
    def __init__(self):
        self.failures: list[str] = []
        self.count = 0

    def check(self, name: str, ok: bool, detail: str = "") -> None:
        self.count += 1
        mark = "ok  " if ok else "FAIL"
        line = f"  [{mark}] {name}"
        if not ok and detail:
            line += f"\n         -> {detail}"
        print(line)
        if not ok:
            self.failures.append(name)


def _read(path: str) -> str:
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read()


def _expect_code(text: str) -> str | None:
    match = _EXPECT_RE.search(text)
    return match.group(1) if match else None


def _md_files(directory: str) -> list[str]:
    return [
        f for f in sorted(os.listdir(directory))
        if f.endswith(".md") and f.lower() != "readme.md"
    ]


def main() -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass

    report = Reporter()
    tmpdir = tempfile.mkdtemp(prefix="hod-verify-")

    # --- 1. Build the fixture deck and round-trip it through extract.py (CLI) -----
    print("Pipeline: fixture_deck -> extract.py -> manifest")
    pptx_path = os.path.join(tmpdir, fixture_deck.FIXTURE_BASENAME)
    fixture_deck.build(pptx_path)
    manifest_path = os.path.join(tmpdir, "manifest.md")
    proc = subprocess.run(
        [PY, os.path.join(ROOT, "extract.py"), pptx_path, "-o", manifest_path],
        capture_output=True, text=True,
    )
    report.check("extract.py CLI exits 0", proc.returncode == 0, proc.stderr.strip())

    manifest = check.parse_manifest(_read(manifest_path))
    report.check("manifest has all 6 slides", len(manifest) == 6, f"got {sorted(manifest)}")
    report.check(
        "slide 3 text preserved verbatim",
        "produce energy for respiration" in manifest.get(3, ""),
        repr(manifest.get(3, "")),
    )
    report.check(
        "slide 6 text preserved verbatim",
        "Any questions before we finish?" in manifest.get(6, ""),
        repr(manifest.get(6, "")),
    )

    # --- 2. Clean cases must clear ------------------------------------------------
    print("\nClears every clean (cases/):")
    case_files = _md_files(CASES_DIR)
    report.check("at least one clean case exists", len(case_files) >= 1)
    cleared = 0
    for name in case_files:
        result = check.check_critique(_read(os.path.join(CASES_DIR, name)), manifest)
        ok = result.ok
        report.check(f"cases/{name} clears the gate", ok,
                     "; ".join(str(v) for v in result.violations))
        cleared += ok
        for warning in result.warnings:
            print(f"         (advisory) {warning}")

    # --- 3. Negatives must block on their named check -----------------------------
    print("\nBlocks every bad, each on its named check (negative/):")
    neg_files = _md_files(NEG_DIR)
    report.check("at least one negative case exists", len(neg_files) >= 1)
    blocked = 0
    seen_codes: set[str] = set()
    for name in neg_files:
        text = _read(os.path.join(NEG_DIR, name))
        expected = _expect_code(text)
        result = check.check_critique(text, manifest)
        codes = [v.code for v in result.violations]
        if expected is not None:
            seen_codes.add(expected)
        ok = (not result.ok) and codes == [expected]
        report.check(f"negative/{name} blocked on [{expected}]", ok, f"got {codes}")
        blocked += ok

    # --- 4. Every gate check is verified by a negative ----------------------------
    print("\nCoverage: every gate check has a negative fixture:")
    missing = sorted(set(check.ALL_CODES) - seen_codes)
    report.check("all gate checks covered by a negative", not missing,
                 f"uncovered: {missing}")

    # --- 5. CLIs and --selftest ---------------------------------------------------
    print("\nCLI contract:")
    clean_cli = subprocess.run(
        [PY, os.path.join(ROOT, "check.py"),
         os.path.join(CASES_DIR, "critique-cell-structure.md"), manifest_path],
        capture_output=True, text=True,
    )
    report.check("check.py exits 0 on a clean critique", clean_cli.returncode == 0,
                 clean_cli.stdout.strip() + clean_cli.stderr.strip())
    bad_cli = subprocess.run(
        [PY, os.path.join(ROOT, "check.py"),
         os.path.join(NEG_DIR, neg_files[0]), manifest_path],
        capture_output=True, text=True,
    )
    report.check("check.py exits 1 on a broken critique", bad_cli.returncode == 1,
                 bad_cli.stdout.strip())
    selftest = subprocess.run(
        [PY, os.path.join(ROOT, "check.py"), "--selftest"],
        capture_output=True, text=True,
    )
    report.check("check.py --selftest exits 0", selftest.returncode == 0,
                 selftest.stdout.strip() + selftest.stderr.strip())

    # --- Summary ------------------------------------------------------------------
    print(
        f"\n{cleared}/{len(case_files)} clean cleared, "
        f"{blocked}/{len(neg_files)} bad blocked on their named check, "
        f"{report.count - len(report.failures)}/{report.count} assertions passed."
    )
    if report.failures:
        print("VERIFY FAILED:")
        for name in report.failures:
            print(f"  - {name}")
        return 1
    print("VERIFY OK — the gate blocks every bad and clears every clean.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
