#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
# --- How to run ---
# python3 scripts/evaluate_latex_output.py --tex path/to/main.tex --benchmark full-manuscript
# python3 scripts/evaluate_latex_output.py --tex path/to/main.tex --benchmark trend-review --out report.md
# python3 scripts/evaluate_latex_output.py --tex path/to/main.tex --benchmark trend-review --compile
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Final


ROOT: Final = Path(__file__).resolve().parents[1]
RISKY_PHRASES: Final = (
    "robust", "generalizable", "generalise", "generalize", "physically consistent",
    "physical consistency", "real-time", "state-of-the-art", "deployment-ready",
    "deployable", "general CFD acceleration", "3D turbulence", "three-dimensional",
    "PIV", "conservation", "Navier--Stokes residual", "Navier-Stokes residual",
    "solve turbulence", "solves turbulence", "solved turbulence", "solved CFD",
)
SAFE_CONTEXT_MARKERS: Final = (
    "TODO", "unsupported", "not claim", "not claimed", "do not claim", "limitation",
    "absent", "missing", "requires", "needs", "future work", "no evidence", "remain", "without",
    "not presented", "not sufficient", "therefore no", "no conservation", "no residual",
)
FULL_REQUIRED_SECTIONS: Final = ("Introduction", "Methods", "Results", "Conclusion")
TREND_REQUIRED_SECTIONS: Final = (
    "Introduction", "Taxonomy", "Validation", "Reproducibility", "Reviewer",
    "Research agenda", "Conclusion",
)
BENCHMARK_LANDSCAPE_REQUIRED_SECTIONS: Final = (
    "Introduction", "Benchmark", "Validation", "Reproducibility", "Failure", "Research agenda", "Conclusion",
)
BENCHMARK_CHOICES: Final = ("full-manuscript", "trend-review", "closure-review", "benchmark-landscape-review")
FULL_TERMS: Final = (
    "vorticity", "Re_D", "downsampling", "bicubic", "U-Net", "spectrum", "PDF",
    "shear-layer", "relative $L_2$",
)
TREND_TERMS: Final = (
    "geometry", "mesh", "neural operator", "graph", "workflow", "validation",
    "boundary", "uncertainty", "reproducibility",
)
CLOSURE_TERMS: Final = (
    "closure", "RANS", "LES", "a priori", "a posteriori", "invariance",
    "coupled", "uncertainty", "verifiability",
)
BENCHMARK_LANDSCAPE_TERMS: Final = (
    "dataset", "benchmark", "split", "validation", "reproducibility", "failure", "surrogate", "PDEBench", "DeepXDE",
)
BenchmarkProfile = tuple[tuple[str, ...], tuple[str, ...], int, int, str]
BENCHMARK_PROFILES: Final[dict[str, BenchmarkProfile]] = {
    "full-manuscript": (FULL_REQUIRED_SECTIONS, FULL_TERMS, 2, 1, "claim-evidence markers"),
    "trend-review": (TREND_REQUIRED_SECTIONS, TREND_TERMS, 3, 2, "reviewer-trap markers"),
    "closure-review": (TREND_REQUIRED_SECTIONS, CLOSURE_TERMS, 3, 2, "reviewer-trap markers"),
    "benchmark-landscape-review": (BENCHMARK_LANDSCAPE_REQUIRED_SECTIONS, BENCHMARK_LANDSCAPE_TERMS, 3, 2, "reviewer-trap markers"),
}


@dataclass(frozen=True)
class Finding:
    __slots__ = ("label", "passed", "detail")

    label: str
    passed: bool
    detail: str


@dataclass(frozen=True)
class RiskHit:
    __slots__ = ("phrase", "line_number", "context", "bounded")

    phrase: str
    line_number: int
    context: str
    bounded: bool


@dataclass(frozen=True)
class CompileResult:
    __slots__ = ("status", "detail")

    status: str
    detail: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Deterministic LaTeX surface evaluator for CFD-AI benchmark outputs.",
    )
    parser.add_argument("--tex", required=True, type=Path, help="Path to LaTeX source file.")
    parser.add_argument(
        "--benchmark",
        required=True,
        choices=BENCHMARK_CHOICES,
        help="Benchmark profile to evaluate.",
    )
    parser.add_argument("--out", type=Path, help="Optional markdown report path.")
    parser.add_argument(
        "--compile",
        action="store_true",
        help="If tectonic is available, run a non-semantic compile check.",
    )
    return parser.parse_args()


def read_tex(path: Path) -> str:
    if not path.is_file():
        raise FileNotFoundError(f"LaTeX file does not exist: {path}")
    return path.read_text(encoding="utf-8")


def command_present(text: str, command: str) -> bool:
    return re.search(rf"\\{re.escape(command)}(?:\[[^\]]*\])?\{{", text) is not None


def environment_count(text: str, name: str) -> int:
    return len(re.findall(rf"\\begin\{{{re.escape(name)}\}}", text))


def has_section_like(text: str, name: str) -> bool:
    pattern = rf"\\(?:section|subsection)\*?\{{[^}}]*{re.escape(name)}[^}}]*\}}"
    return re.search(pattern, text, flags=re.IGNORECASE) is not None


def contains_term(text: str, term: str) -> bool:
    normalized = text.lower().replace("--", "-")
    return term.lower().replace("--", "-") in normalized


def line_context(lines: list[str], index: int) -> str:
    start = max(0, index - 1)
    end = min(len(lines), index + 2)
    context = " ".join(line.strip() for line in lines[start:end])
    return re.sub(r"\s+", " ", context)


def find_risky_phrases(text: str) -> list[RiskHit]:
    hits: list[RiskHit] = []
    lines = text.splitlines()
    for index, line in enumerate(lines):
        for phrase in RISKY_PHRASES:
            if phrase.lower() not in line.lower():
                continue
            context = line_context(lines, index)
            bounded = any(marker.lower() in context.lower() for marker in SAFE_CONTEXT_MARKERS)
            hits.append(RiskHit(phrase=phrase, line_number=index + 1, context=context, bounded=bounded))
    return hits


def compile_with_tectonic(path: Path, enabled: bool) -> CompileResult:
    if not enabled:
        return CompileResult(status="not-run", detail="Compile check skipped; use --compile to enable.")
    executable = shutil.which("tectonic")
    if executable is None:
        return CompileResult(status="not-run", detail="tectonic is not available on PATH.")
    command = (executable, "--keep-logs", "--outdir", str(path.parent), str(path))
    completed = subprocess.run(command, capture_output=True, text=True, check=False)
    if completed.returncode == 0:
        return CompileResult(status="pass", detail="tectonic exited 0.")
    tail = (completed.stderr or completed.stdout).splitlines()[-8:]
    return CompileResult(status="fail", detail="tectonic failed: " + " | ".join(tail))


def benchmark_profile(benchmark: str) -> BenchmarkProfile:
    try:
        return BENCHMARK_PROFILES[benchmark]
    except KeyError as error:
        raise ValueError(f"unknown benchmark profile: {benchmark}") from error


def build_findings(text: str, benchmark: str, tex_path: Path) -> list[Finding]:
    figure_count = environment_count(text, "figure")
    table_count = max(environment_count(text, "table"), environment_count(text, "tabular"))
    sections, terms, minimum_figures, minimum_tables, marker_detail = benchmark_profile(benchmark)
    required_section_hits = [name for name in sections if has_section_like(text, name)]
    term_hits = [term for term in terms if contains_term(text, term)]
    risks = find_risky_phrases(text)
    unbounded = [hit for hit in risks if not hit.bounded]
    marker = "claim" if benchmark == "full-manuscript" else "reviewer"
    return [
        Finding("Input file", tex_path.is_file(), str(tex_path)),
        Finding("Document class", command_present(text, "documentclass"), "Expected \\documentclass{...}."),
        Finding("Title", command_present(text, "title") or "\\maketitle" in text, "Expected title/maketitle."),
        Finding("Abstract", "\\begin{abstract}" in text, "Expected abstract environment."),
        Finding(
            "Required sections",
            len(required_section_hits) == len(sections),
            f"{len(required_section_hits)}/{len(sections)}: {', '.join(required_section_hits)}",
        ),
        Finding(
            "Figure count",
            figure_count >= minimum_figures,
            f"{figure_count} found; benchmark minimum is {minimum_figures}.",
        ),
        Finding(
            "Table count",
            table_count >= minimum_tables,
            f"{table_count} table-like environments found; benchmark minimum is {minimum_tables}.",
        ),
        Finding(
            "Bibliography/TODO",
            ("\\begin{thebibliography}" in text or "\\bibliography{" in text) and "TODO" in text,
            "Expected bibliography marker and TODO discipline for missing evidence.",
        ),
        Finding(
            "Required CFD terms",
            len(term_hits) >= max(1, len(terms) - 1),
            f"{len(term_hits)}/{len(terms)}: {', '.join(term_hits)}",
        ),
        Finding(
            marker_detail,
            marker in text.lower() and "evidence" in text.lower(),
            f"Expected {marker_detail} with evidence language.",
        ),
        Finding(
            "Risky phrase discipline",
            not unbounded,
            f"{len(risks)} risky hits; {len(unbounded)} appear unbounded by TODO/limitation context.",
        ),
    ]


def score(findings: list[Finding]) -> tuple[int, int]:
    passed = sum(1 for finding in findings if finding.passed)
    return passed, len(findings)


def render_report(tex_path: Path, benchmark: str, text: str, compile_result: CompileResult) -> str:
    findings = build_findings(text, benchmark, tex_path)
    passed, total = score(findings)
    risks = find_risky_phrases(text)
    lines = [
        f"# Deterministic LaTeX evaluator report: {tex_path.name}",
        "",
        f"- Benchmark: `{benchmark}`",
        f"- Source: `{tex_path}`",
        "- Judge type: deterministic surface checks only; this is not a semantic LLM review.",
        f"- Compile check: **{compile_result.status}** - {compile_result.detail}",
        f"- Simple score: **{passed}/{total}** checks passed.",
        "",
        "## Scorecard",
        "",
        "| Check | Result | Detail |",
        "|---|---:|---|",
    ]
    for finding in findings:
        result = "pass" if finding.passed else "fail"
        lines.append(f"| {finding.label} | {result} | {finding.detail} |")
    lines.extend(["", "## Risky Phrase Scan", ""])
    if risks:
        lines.extend(["| Phrase | Line | Bounded? | Context |", "|---|---:|---:|---|"])
        for hit in risks:
            bounded = "yes" if hit.bounded else "no"
            context = hit.context.replace("|", "\\|")
            lines.append(f"| `{hit.phrase}` | {hit.line_number} | {bounded} | {context} |")
    else:
        lines.append("No configured risky phrases found.")
    lines.extend(
        [
            "",
            "## Interpretation Limits",
            "",
            "This script checks visible LaTeX structure, benchmark-specific markers, risky phrases, and term coverage.",
            "It cannot verify factual correctness, novelty, citation accuracy, solver settings, or whether a claim is scientifically true.",
            "Use manual rubric review for semantic quality and keep unknown facts marked as TODO.",
            "",
        ],
    )
    return "\n".join(lines)


def main() -> int:
    args = parse_args()
    tex_path = args.tex.resolve()
    text = read_tex(tex_path)
    compile_result = compile_with_tectonic(tex_path, bool(args.compile))
    report = render_report(tex_path, str(args.benchmark), text, compile_result)
    if args.out is not None:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(report, encoding="utf-8")
    else:
        print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
