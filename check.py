#!/usr/bin/env python3
"""check.py — the blocking gate (manifest M3).

Reads an editor critique plus the slide manifest that `extract.py` produced, and
**fails (exit 1)** if the critique violates the one invariant this build enforces in
code: *the editor points, it never rewrites.* On a clean critique it exits 0.

The gate is the line, not the editor (`rules.md` R16). It reports facts and blocks;
it never judges whether a finding is pedagogically *right* — that is the editor's
job, and nothing in code can do it (`reference/finding-schema.md` §8). What it does
enforce is exactly the checklist in `spec.md` ("What check.py blocks") and
`reference/finding-schema.md` §7:

    REWRITE_PATTERN        rewrite / "better version" phrasing in the editor's prose
    ENDS_IN_FIX            the output ends in a fix instead of a question
    NO_SLIDE               a finding with no usable SLIDE anchor
    SLIDE_NOT_IN_MANIFEST  a SLIDE number that does not exist in the deck
    QUOTE_NOT_VERBATIM     a QUOTE not found verbatim on the cited slide (fabrication)
    NO_ANCHOR              a finding citing neither a PRINCIPLE nor a SPEC
    NO_QUESTION            a finding not ending in a QUESTION that ends in "?"
    MALFORMED_BLOCK        a finding block missing a field or out of order

Finding format (fixed by `reference/finding-schema.md` §1) — a SEVERITY line then
the six fields, each on its own line, in this order:

    SEVERITY: CRITICAL | MAJOR | MINOR
    SLIDE: <int>
    QUOTE: "<verbatim wording from that slide>"
    PRINCIPLE: <framework handle, or — >
    SPEC: <AQA handle, or — >
    WHY: <why it fails with this class>
    QUESTION: <the question handed back, ending in ?>

Usage:
    python check.py critique.md manifest.md      # gate a critique (exit 0 pass / 1 block)
    python check.py critique.md manifest.md --json
    python check.py --selftest                   # prove both directions, standalone

Design notes for the two matching rules the gate turns on:

* Verbatim (§3). The QUOTE must appear on the *cited* slide. To be deterministic
  across PowerPoint's line-wrapping and smart-quote autocorrect while staying a true
  fabrication check, both sides are normalised: runs of whitespace collapse to one
  space, and typographic quotes/apostrophes fold to ASCII (M2 open-question #1, owned
  here). No case folding, no punctuation stripping. The QUOTE passes iff its
  normalised form is a substring of the normalised slide text.

* Rewrite detection. A phrase list (M2 open-question #3, owned here) — "here's a
  better version", "it should read", "replace X with Y", and kin. It is scanned over
  the editor's prose and every field *except the verbatim QUOTE span*, because the
  QUOTE is the slide's words, not the editor's, and a slide may itself say "try
  this". This is heuristic and cannot catch supplied content with no tell-tale
  phrasing; that limit is stated in OPEN-DEFECTS, and the structural NO_QUESTION /
  ENDS_IN_FIX checks are the backstop that the read closes on a question.

The optional PRINCIPLE/SPEC handle check is an **advisory soft-warning, never a
block** (M2.5 open-question #2, owned here): it flags a citation that is not a
recognised handle *shape* (a vague gesture like "good practice" — `rules.md` R15),
printed to stderr, with no effect on the exit code, so the reference layer can grow
without breaking the gate.
"""

from __future__ import annotations

import argparse
import json
import re
import sys

# --------------------------------------------------------------------------- #
# Violation codes
# --------------------------------------------------------------------------- #

REWRITE_PATTERN = "REWRITE_PATTERN"
ENDS_IN_FIX = "ENDS_IN_FIX"
NO_SLIDE = "NO_SLIDE"
SLIDE_NOT_IN_MANIFEST = "SLIDE_NOT_IN_MANIFEST"
QUOTE_NOT_VERBATIM = "QUOTE_NOT_VERBATIM"
NO_ANCHOR = "NO_ANCHOR"
NO_QUESTION = "NO_QUESTION"
MALFORMED_BLOCK = "MALFORMED_BLOCK"

# Every check the gate can fail on. tests/verify.py asserts each has a negative
# fixture — "a checker that passes everything proves nothing."
ALL_CODES = (
    REWRITE_PATTERN, ENDS_IN_FIX, NO_SLIDE, SLIDE_NOT_IN_MANIFEST,
    QUOTE_NOT_VERBATIM, NO_ANCHOR, NO_QUESTION, MALFORMED_BLOCK,
)

FIELD_ORDER = ("SLIDE", "QUOTE", "PRINCIPLE", "SPEC", "WHY", "QUESTION")
_SEVERITY_RE = re.compile(r"^SEVERITY:\s*(CRITICAL|MAJOR|MINOR)\s*$")
_SLIDE_HEADER_RE = re.compile(r"^##\s+Slide\s+(\d+)\s*$")


# --------------------------------------------------------------------------- #
# Normalisation (verbatim-match rule, finding-schema §3)
# --------------------------------------------------------------------------- #

_QUOTE_MAP = {
    "‘": "'", "’": "'", "‚": "'", "‛": "'", "′": "'",
    "“": '"', "”": '"', "„": '"', "‟": '"', "″": '"',
}


def _fold_quotes(text: str) -> str:
    for src, dst in _QUOTE_MAP.items():
        text = text.replace(src, dst)
    return text


def _normalise(text: str) -> str:
    """Fold typographic quotes to ASCII and collapse whitespace to single spaces."""
    return " ".join(_fold_quotes(text).split())


def _quoted_span(quote_value: str) -> str | None:
    """The text between the first and last double-quote of a QUOTE field value.

    Curly quotes are folded first, so a QUOTE delimited with typographic quotes is
    handled the same as one delimited with straight quotes.
    """
    folded = _fold_quotes(quote_value)
    first = folded.find('"')
    last = folded.rfind('"')
    if first == -1 or last <= first:
        return None
    return folded[first + 1:last]


# --------------------------------------------------------------------------- #
# Rewrite / fix phrase list (M2 open-question #3)
# --------------------------------------------------------------------------- #

_REWRITE_PATTERNS = [
    ("better-version", r"here'?s\s+(?:a|an|the|my)?\s*(?:better|stronger|clearer|improved|corrected|revised|rewritten|fixed|cleaner)\b"),
    ("a-better-version", r"\b(?:a|the)\s+better\s+version\b"),
    ("heres-how-id", r"here'?s\s+how\s+(?:i'?d|i\s+would)\b"),
    ("heres-a-rewrite", r"here'?s\s+(?:a|an|the|my)?\s*(?:rewrite|revision|rephrase|wording|fix|version)\b"),
    ("id-rewrite", r"\b(?:i'?d|i\s+would)\s+(?:rewrite|reword|redraft|rephrase|change\s+it|write\s+it|put\s+it|phrase\s+it|say)\b"),
    ("let-me-rewrite", r"\blet\s+me\s+(?:rewrite|reword|redraft|rephrase|fix|draft|write)\b"),
    ("try-this-instead", r"\btry\s+(?:this|the\s+following)\s+instead\b"),
    ("instead-write", r"\binstead,?\s+(?:write|say|use|put|try|make\s+it)\b"),
    ("change-x-to", r"\bchange\s+(?:it|this|the\s+\w+)\s+to\b"),
    ("replace-with", r"\breplace\b.{1,80}?\bwith\b"),
    ("it-should-say", r"\b(?:it|this|the\s+(?:slide|caption|line|title|text|wording|bullet))\s+should\s+(?:say|read|instead\s+say|instead\s+read)\b"),
    ("should-say-quote", r"\bshould\s+(?:say|read)\b\s*[:\-–—]?\s*[\"'“‘]"),
    ("rewritten-colon", r"\b(?:rewritten|rewrite|revised|suggested\s+(?:rewrite|wording|version|edit|text))\s*:"),
    ("you-could-say", r"\byou\s+could\s+(?:say|write|put|phrase|use)\b"),
    ("how-id-write", r"\bhow\s+i'?d\s+(?:write|phrase|word|put)\s+it\b"),
]

_REWRITE_COMPILED = [(name, re.compile(rx, re.IGNORECASE)) for name, rx in _REWRITE_PATTERNS]


def _first_rewrite_hit(text: str):
    for name, rx in _REWRITE_COMPILED:
        match = rx.search(text)
        if match:
            return name, match.group(0)
    return None


# --------------------------------------------------------------------------- #
# Handle recognition (advisory only, R15 / M2.5 open-question #2)
# --------------------------------------------------------------------------- #

_PRINCIPLE_PREFIXES = (
    "Rosenshine ", "CLT", "Retrieval", "Spacing", "Interleaving",
    "Desirable difficulties", "Dual coding", "EEF",
)
_SPEC_HANDLE_RE = re.compile(r"^AQA\s+\d+(?:\.\d+)*\s+[—–-]")


def _principle_recognised(value: str) -> bool:
    return any(value.startswith(prefix) for prefix in _PRINCIPLE_PREFIXES)


def _spec_recognised(value: str) -> bool:
    return bool(_SPEC_HANDLE_RE.match(value))


def _is_absent(value: str) -> bool:
    """A PRINCIPLE/SPEC field written as '—' (or blank) — i.e. deliberately not cited."""
    stripped = value.strip()
    return stripped == "" or set(stripped) <= {"-", "–", "—"}


# --------------------------------------------------------------------------- #
# Data structures
# --------------------------------------------------------------------------- #

class Violation:
    __slots__ = ("code", "detail", "finding", "line")

    def __init__(self, code, detail, finding=None, line=None):
        self.code = code
        self.detail = detail
        self.finding = finding  # 1-based finding index, or None for document-level
        self.line = line        # 1-based line number in the critique, or None

    def as_dict(self):
        return {"code": self.code, "detail": self.detail,
                "finding": self.finding, "line": self.line}

    def __repr__(self):
        where = f" finding #{self.finding}" if self.finding else ""
        at = f" (line {self.line})" if self.line else ""
        return f"[{self.code}]{where}{at}: {self.detail}"


class Result:
    def __init__(self, violations, warnings, finding_count):
        self.violations = violations
        self.warnings = warnings
        self.finding_count = finding_count

    @property
    def ok(self):
        return not self.violations


class _Finding:
    __slots__ = ("index", "severity", "fields", "field_lines", "start_line", "malformed")

    def __init__(self, index, severity, fields, field_lines, start_line, malformed):
        self.index = index
        self.severity = severity
        self.fields = fields              # key -> value string
        self.field_lines = field_lines    # key -> 0-based line index
        self.start_line = start_line      # 0-based index of the SEVERITY line
        self.malformed = malformed        # str reason, or None


# --------------------------------------------------------------------------- #
# Parsing
# --------------------------------------------------------------------------- #

def parse_manifest(text: str) -> dict[int, str]:
    """Parse an extract.py manifest into {slide_number: slide_text}."""
    slides: dict[int, list[str]] = {}
    current: int | None = None
    for line in text.splitlines():
        header = _SLIDE_HEADER_RE.match(line)
        if header:
            current = int(header.group(1))
            slides[current] = []
        elif current is not None:
            slides[current].append(line)
    return {num: "\n".join(body).strip() for num, body in slides.items()}


def _parse_findings(lines: list[str]) -> list[_Finding]:
    findings: list[_Finding] = []
    i = 0
    n = len(lines)
    while i < n:
        sev_match = _SEVERITY_RE.match(lines[i].rstrip())
        if not sev_match:
            i += 1
            continue
        severity = sev_match.group(1)
        start_line = i
        fields: dict[str, str] = {}
        field_lines: dict[str, int] = {}
        malformed = None
        j = i + 1
        for key in FIELD_ORDER:
            while j < n and lines[j].strip() == "":
                j += 1
            if j >= n:
                malformed = f"reached end of critique while expecting {key}"
                break
            line = lines[j].rstrip()
            if _SEVERITY_RE.match(line):
                malformed = f"next finding began before {key} was given"
                break
            prefix = key + ":"
            if not line.startswith(prefix):
                shown = line[:48] + ("…" if len(line) > 48 else "")
                malformed = f"expected {key} but found: {shown!r}"
                break
            fields[key] = line[len(prefix):].strip()
            field_lines[key] = j
            j += 1
        findings.append(
            _Finding(len(findings) + 1, severity, fields, field_lines, start_line, malformed)
        )
        i = j
    return findings


# --------------------------------------------------------------------------- #
# The gate
# --------------------------------------------------------------------------- #

def check_critique(critique_text: str, manifest: dict[int, str],
                   *, handle_check: bool = True) -> Result:
    """Run the gate. Returns a Result; never raises on ordinary bad input."""
    lines = critique_text.splitlines()
    findings = _parse_findings(lines)
    violations: list[Violation] = []
    warnings: list[str] = []

    # Track QUOTE spans so the rewrite scan can skip the slide's own words, and the
    # last QUESTION line so a rewrite after it reads as "ends in a fix".
    quote_line_indices: set[int] = set()
    last_question_line = -1

    for finding in findings:
        fidx = finding.index
        human_line = finding.start_line + 1

        if finding.malformed:
            violations.append(Violation(MALFORMED_BLOCK, finding.malformed, fidx, human_line))
            # Still register any QUOTE line we managed to read, to keep the rewrite
            # scan honest about the slide's own words.
            if "QUOTE" in finding.field_lines:
                quote_line_indices.add(finding.field_lines["QUOTE"])
            continue

        quote_line_indices.add(finding.field_lines["QUOTE"])
        last_question_line = max(last_question_line, finding.field_lines["QUESTION"])

        # SLIDE ----------------------------------------------------------------
        slide_raw = finding.fields["SLIDE"].strip()
        slide_num = None
        if not re.fullmatch(r"\d+", slide_raw) or int(slide_raw) < 1:
            violations.append(Violation(
                NO_SLIDE, f"SLIDE must be a positive integer, got {slide_raw!r}",
                fidx, finding.field_lines["SLIDE"] + 1))
        else:
            slide_num = int(slide_raw)
            if slide_num not in manifest:
                violations.append(Violation(
                    SLIDE_NOT_IN_MANIFEST,
                    f"SLIDE {slide_num} is not in the manifest "
                    f"(deck has slides {_slide_range(manifest)})",
                    fidx, finding.field_lines["SLIDE"] + 1))
                slide_num = None  # cannot verbatim-check a slide that is not there

        # QUOTE ----------------------------------------------------------------
        span = _quoted_span(finding.fields["QUOTE"])
        if span is None or span.strip() == "":
            violations.append(Violation(
                MALFORMED_BLOCK, "QUOTE has no double-quoted verbatim span",
                fidx, finding.field_lines["QUOTE"] + 1))
        elif slide_num is not None:
            if _normalise(span) not in _normalise(manifest[slide_num]):
                violations.append(Violation(
                    QUOTE_NOT_VERBATIM,
                    f"QUOTE not found verbatim on slide {slide_num}: {span!r}",
                    fidx, finding.field_lines["QUOTE"] + 1))

        # PRINCIPLE / SPEC anchor ---------------------------------------------
        principle = finding.fields["PRINCIPLE"]
        spec = finding.fields["SPEC"]
        principle_cited = not _is_absent(principle)
        spec_cited = not _is_absent(spec)
        if not principle_cited and not spec_cited:
            violations.append(Violation(
                NO_ANCHOR, "finding cites neither a PRINCIPLE nor a SPEC point",
                fidx, finding.field_lines["PRINCIPLE"] + 1))
        if handle_check:
            if principle_cited and not _principle_recognised(principle):
                warnings.append(
                    f"finding #{fidx}: PRINCIPLE {principle!r} is not a recognised "
                    f"framework handle (advisory; see reference/frameworks/).")
            if spec_cited and not _spec_recognised(spec):
                warnings.append(
                    f"finding #{fidx}: SPEC {spec!r} is not a recognised "
                    f"'AQA <code> — …' handle (advisory; see reference/spec/).")

        # WHY ------------------------------------------------------------------
        if finding.fields["WHY"].strip() == "":
            violations.append(Violation(
                MALFORMED_BLOCK, "WHY is empty", fidx, finding.field_lines["WHY"] + 1))

        # QUESTION -------------------------------------------------------------
        question = finding.fields["QUESTION"].strip()
        if question == "":
            violations.append(Violation(
                NO_QUESTION, "QUESTION is empty",
                fidx, finding.field_lines["QUESTION"] + 1))
        elif not question.endswith("?"):
            violations.append(Violation(
                NO_QUESTION, f"QUESTION must end in '?': {question!r}",
                fidx, finding.field_lines["QUESTION"] + 1))

    # Rewrite / fix scan — over the whole document minus the verbatim QUOTE spans.
    for idx, line in enumerate(lines):
        if idx in quote_line_indices:
            continue
        hit = _first_rewrite_hit(line)
        if not hit:
            continue
        name, snippet = hit
        if last_question_line != -1 and idx > last_question_line:
            violations.append(Violation(
                ENDS_IN_FIX,
                f"output continues past the last question with a fix ({name}): {snippet!r}",
                None, idx + 1))
        else:
            violations.append(Violation(
                REWRITE_PATTERN,
                f"rewrite/fix phrasing ({name}): {snippet!r}",
                None, idx + 1))

    return Result(violations, warnings, len(findings))


def _slide_range(manifest: dict[int, str]) -> str:
    if not manifest:
        return "(none)"
    nums = sorted(manifest)
    return f"1–{nums[-1]}" if nums == list(range(1, nums[-1] + 1)) else ", ".join(map(str, nums))


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #

def _read(path: str) -> str:
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read()


def _report(result: Result, as_json: bool) -> None:
    if as_json:
        print(json.dumps({
            "ok": result.ok,
            "findings": result.finding_count,
            "violations": [v.as_dict() for v in result.violations],
            "warnings": result.warnings,
        }, indent=2))
        return
    for warning in result.warnings:
        sys.stderr.write(f"warning: {warning}\n")
    if result.ok:
        print(f"PASS — {result.finding_count} finding(s), no violations. "
              f"The read points; it does not rewrite.")
    else:
        print(f"BLOCK — {len(result.violations)} violation(s) "
              f"across {result.finding_count} finding(s):")
        for v in result.violations:
            print(f"  {v}")


def _utf8_streams() -> None:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):  # pragma: no cover - non-reconfigurable stream
            pass


def main(argv: list[str]) -> int:
    _utf8_streams()
    parser = argparse.ArgumentParser(
        prog="check.py",
        description="The blocking gate: point, never rewrite. Exit 0 pass, 1 block.",
    )
    parser.add_argument("critique", nargs="?", help="the editor critique to gate")
    parser.add_argument("manifest", nargs="?", help="the extract.py slide manifest")
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    parser.add_argument("--no-handle-check", action="store_true",
                        help="disable the advisory PRINCIPLE/SPEC handle warnings")
    parser.add_argument("--selftest", action="store_true",
                        help="prove the gate both directions on built-in fixtures")
    args = parser.parse_args(argv)

    if args.selftest:
        return run_selftest(verbose=not args.json)

    if not args.critique or not args.manifest:
        parser.error("need CRITIQUE and MANIFEST (or --selftest)")

    critique_text = _read(args.critique)
    manifest = parse_manifest(_read(args.manifest))
    result = check_critique(critique_text, manifest, handle_check=not args.no_handle_check)
    _report(result, args.json)
    return 0 if result.ok else 1


# --------------------------------------------------------------------------- #
# Standalone self-test — proves both directions with no external files.
# The reviewable, file-based verify-the-verifier is tests/verify.py.
# --------------------------------------------------------------------------- #

_SELFTEST_MANIFEST = {
    1: "Mitochondria are the powerhouse of the cell and produce energy for respiration.",
    2: "Plenary\nAny questions before we finish?",
}

_SELFTEST_CLEAN = '''\
# Findings

SEVERITY: MAJOR
SLIDE: 1
QUOTE: "produce energy for respiration"
PRINCIPLE: —
SPEC: AQA 3.2.1 — ATP not "energy"
WHY: AQA rejects "energy" for mitochondria and credits only ATP, so this caption is the exact word the mark scheme throws out.
QUESTION: How will you make sure the class writes "ATP" rather than "energy" when this is the slide they copy down?
'''

# One deliberately-broken critique per code, each broken in exactly one way.
_SELFTEST_BAD = {
    QUOTE_NOT_VERBATIM: '''\
SEVERITY: MAJOR
SLIDE: 1
QUOTE: "mitochondria make ATP from glucose directly"
PRINCIPLE: —
SPEC: AQA 3.2.1 — ATP not "energy"
WHY: The caption is imprecise for this class.
QUESTION: What will the class write down here?
''',
    NO_ANCHOR: '''\
SEVERITY: MINOR
SLIDE: 1
QUOTE: "produce energy for respiration"
PRINCIPLE: —
SPEC: —
WHY: This feels a little generic for the group.
QUESTION: Could this be sharper?
''',
    NO_SLIDE: '''\
SEVERITY: MINOR
SLIDE: —
QUOTE: "produce energy for respiration"
PRINCIPLE: —
SPEC: AQA 3.2.1 — ATP not "energy"
WHY: The anchor is missing its slide number.
QUESTION: Which slide is this on?
''',
    SLIDE_NOT_IN_MANIFEST: '''\
SEVERITY: MINOR
SLIDE: 99
QUOTE: "Any questions before we finish?"
PRINCIPLE: —
SPEC: AQA 3.2.1 — microscopy
WHY: This points at a slide the deck does not have.
QUESTION: Did you mean a different slide?
''',
    NO_QUESTION: '''\
SEVERITY: MINOR
SLIDE: 1
QUOTE: "produce energy for respiration"
PRINCIPLE: —
SPEC: AQA 3.2.1 — ATP not "energy"
WHY: The finding does not end in a question.
QUESTION: The class should be told the correct term.
''',
    MALFORMED_BLOCK: '''\
SEVERITY: MINOR
SLIDE: 1
QUOTE: "produce energy for respiration"
SPEC: AQA 3.2.1 — ATP not "energy"
PRINCIPLE: —
WHY: PRINCIPLE and SPEC are out of order here.
QUESTION: Is the block well formed?
''',
    REWRITE_PATTERN: '''\
SEVERITY: MAJOR
SLIDE: 1
QUOTE: "produce energy for respiration"
PRINCIPLE: —
SPEC: AQA 3.2.1 — ATP not "energy"
WHY: I won't rewrite your slide, but here's how it should read: "Mitochondria are the site of aerobic respiration and produce ATP."
QUESTION: What term will the class leave with?
''',
    ENDS_IN_FIX: '''\
SEVERITY: MAJOR
SLIDE: 1
QUOTE: "produce energy for respiration"
PRINCIPLE: —
SPEC: AQA 3.2.1 — ATP not "energy"
WHY: The caption uses a rejected term.
QUESTION: What term will the class leave with?

If it helps, here's a better version of the slide: Mitochondria are the site of aerobic respiration, releasing ATP.
''',
}


def run_selftest(verbose: bool = True) -> int:
    failures: list[str] = []

    clean = check_critique(_SELFTEST_CLEAN, _SELFTEST_MANIFEST)
    if not clean.ok:
        failures.append(f"clean critique was blocked: {[str(v) for v in clean.violations]}")

    for code, critique in _SELFTEST_BAD.items():
        result = check_critique(critique, _SELFTEST_MANIFEST)
        got = [v.code for v in result.violations]
        if result.ok:
            failures.append(f"{code}: expected a block, got PASS")
        elif got != [code]:
            failures.append(f"{code}: expected exactly [{code}], got {got}")

    if verbose:
        if failures:
            sys.stderr.write("SELFTEST FAILED:\n")
            for line in failures:
                sys.stderr.write(f"  - {line}\n")
        else:
            print(f"SELFTEST OK — 1/1 clean cleared, "
                  f"{len(_SELFTEST_BAD)}/{len(_SELFTEST_BAD)} bad blocked, "
                  f"each on its named check.")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
