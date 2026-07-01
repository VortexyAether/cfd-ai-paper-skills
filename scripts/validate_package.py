#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from typing import Final

import run_static_evals


ROOT: Final = Path(__file__).resolve().parents[1]
REQUIRED_DIRS: Final = (
    "skills",
    "references",
    "references/gold-papers",
    "rubrics",
    "examples",
    "templates",
    "evaluation",
    "evaluation/tasks",
    "evaluation/runs",
    "scripts",
)
REQUIRED_GOLD_PAPERS: Final = (
    "references/gold-papers/fukami-2019-super-resolution-jfm.md",
    "references/gold-papers/brunton-2020-machine-learning-fluid-mechanics.md",
    "references/gold-papers/maulik-2020-probabilistic-neural-networks-prf.md",
    "references/gold-papers/lee-2019-cylinder-wake-jfm.md",
    "references/gold-papers/vinuesa-2022-enhancing-cfd-ml.md",
)
REQUIRED_REFERENCE_FILES: Final = (
    "references/gold-papers/INDEX.md",
    "references/gold-standard-bibliography-v0.4.md",
    "references/field-terminology-style-guide.md",
)
REQUIRED_RUBRICS: Final = (
    "rubrics/claim-evidence-rubric.md",
    "rubrics/cfd-reproducibility-rubric.md",
    "rubrics/sciml-experiment-rubric.md",
    "rubrics/figure-evidence-rubric.md",
    "rubrics/skill-quality-rubric.md",
    "rubrics/vocabulary-style-rubric.md",
)
REQUIRED_EXAMPLES: Final = (
    "examples/bad-to-good-abstract.md",
    "examples/weak-to-publishable-experiment-plan.md",
    "examples/citation-dump-to-taxonomy.md",
    "examples/generic-review-to-cfd-review.md",
    "examples/ai-ish-to-field-native-prose.md",
)
REQUIRED_TEMPLATES: Final = (
    "templates/claim-evidence-map.md",
    "templates/experiment-plan.md",
    "templates/response-letter.md",
    "templates/reviewer-report.md",
)
PRIVATE_STATE_DIR: Final = "." + ("ta" + "rs")
LOCAL_USER_PART: Final = "v" + "a"
PUBLIC_SCAN_EXCLUDED_DIRS: Final = frozenset((".git", "." + "omo", PRIVATE_STATE_DIR, "dist", "__pycache__", ".tmp_pycache"))
PUBLIC_SCAN_EXCLUDED_NAMES: Final = frozenset((".gitignore",))
FORBIDDEN_PUBLIC_PATTERNS: Final = (
    "TA" + "RS",
    "Lazy" + "Codex",
    "du" + "mb",
    "du" + "mb-agent",
    "du" + "mb agent",
    "evaluator " + "loop",
    "/Users/" + LOCAL_USER_PART,
    PRIVATE_STATE_DIR,
)
ROOT_SKILL_REQUIRED_STRINGS: Final = (
    "name: cfd-ai-paper-skills",
    "version: v0.6.1",
    "## Trigger Conditions",
    "## Progressive Disclosure",
    "## Routing Table",
    "skills/paper-claim-auditor/SKILL.md",
    "skills/cfd-reproducibility-checker/SKILL.md",
    "skills/experiment-design-for-sciml/SKILL.md",
    "skills/sciml-experiment-auditor/SKILL.md",
    "skills/related-work-cartographer/SKILL.md",
    "skills/related-work-synthesis/SKILL.md",
    "skills/latex-paper-production/SKILL.md",
    "skills/reviewer-simulator/SKILL.md",
    "skills/response-to-reviewers/SKILL.md",
    "skills/paper-revision-loop-manager/SKILL.md",
    "Claim-Evidence Map",
    "Reviewer-Risk Report",
    "Reproducibility Checklist",
    "Experiment Matrix",
    "LaTeX Manuscript Seed",
    "Response Letter",
    "Benchmark Review Output",
)
SKILL_REQUIRED_SECTIONS: Final = (
    ("output schema", "output template"),
    ("anti-pattern",),
    ("verification",),
)
GOLD_PAPER_REQUIRED_SECTION_GROUPS: Final = (
    ("metadata", "bibliographic metadata"),
    ("source scope",),
    ("why answer key", "why this paper is an answer key"),
    ("abstract grammar",),
    ("introduction move",),
    ("method/reproducibility",),
    ("experiment/evidence",),
    ("figure grammar",),
    ("reviewer-defense",),
    ("skill lessons",),
    ("eval task",),
    ("unknowns/todos", "unknowns/todo"),
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def frontmatter_has_key(frontmatter: str, key: str) -> bool:
    prefix = f"{key}:"
    return any(line.startswith(prefix) for line in frontmatter.splitlines())


def has_any_section(text: str, section_names: tuple[str, ...]) -> bool:
    for line in text.lower().splitlines():
        if line.startswith("## ") and any(name in line for name in section_names):
            return True
    return False


def validate_skill(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    require(text.startswith("---\n"), f"{path}: missing YAML frontmatter at byte 0")
    parts = text.split("---", 2)
    require(len(parts) >= 3, f"{path}: malformed YAML frontmatter")
    frontmatter = parts[1]
    require(frontmatter_has_key(frontmatter, "name"), f"{path}: missing name")
    require(frontmatter_has_key(frontmatter, "description"), f"{path}: missing description")
    for section_names in SKILL_REQUIRED_SECTIONS:
        label = " or ".join(section_names)
        require(has_any_section(text, section_names), f"{path}: missing {label} section")


def validate_root_skill(path: Path) -> None:
    validate_skill(path)
    text = path.read_text(encoding="utf-8")
    for required in ROOT_SKILL_REQUIRED_STRINGS:
        require(required in text, f"{path}: missing root entrypoint requirement: {required}")


def validate_gold_paper(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    require(text.startswith("---\n"), f"{path}: missing YAML frontmatter at byte 0")
    for section_names in GOLD_PAPER_REQUIRED_SECTION_GROUPS:
        label = " or ".join(section_names)
        require(has_any_section(text, section_names), f"{path}: missing {label} section")


def validate_gold_papers() -> None:
    papers = sorted(path for path in (ROOT / "references" / "gold-papers").glob("*.md") if path.name != "INDEX.md")
    require(len(papers) >= 15, f"expected at least 15 gold-paper analyses, found {len(papers)}")
    for path in papers:
        validate_gold_paper(path)


def package_path(raw_path: str, label: str, expected_parent: str) -> Path:
    path = Path(raw_path)
    require(not path.is_absolute(), f"{label} path must be relative: {raw_path}")
    require(".." not in path.parts, f"{label} path must not escape package: {raw_path}")
    resolved = (ROOT / path).resolve()
    require(resolved.is_relative_to(ROOT), f"{label} path resolves outside package: {raw_path}")
    parent = (ROOT / expected_parent).resolve()
    require(resolved.is_relative_to(parent), f"{label} path must be under {expected_parent}: {raw_path}")
    return resolved


def validate_eval_tasks(evals_path: Path) -> None:
    data = json.loads(evals_path.read_text(encoding="utf-8"))
    require(isinstance(data.get("evals"), list), "evaluation/evals.json: evals must be a list")
    for item in data["evals"]:
        require(isinstance(item, dict), "evaluation/evals.json: each eval must be an object")
        task = item.get("task")
        require(isinstance(task, str) and bool(task), f"eval item missing task: {item}")
        require(package_path(task, "task", "evaluation/tasks").is_file(), f"referenced eval task missing: {task}")
        scorecard = item.get("scorecard")
        if scorecard is not None:
            require(isinstance(scorecard, str), f"scorecard path must be string: {item}")
            require(
                package_path(scorecard, "scorecard", "evaluation/scorecards").is_file(),
                f"referenced scorecard missing: {scorecard}",
            )


def validate_public_term_separation() -> None:
    for path in sorted(ROOT.rglob("*")):
        relative = path.relative_to(ROOT)
        if not path.is_file():
            continue
        if path.name in PUBLIC_SCAN_EXCLUDED_NAMES:
            continue
        if any(part in PUBLIC_SCAN_EXCLUDED_DIRS for part in relative.parts):
            continue
        if path.suffix.lower() in (".pdf", ".gz"):
            continue
        text = path.read_text(encoding="utf-8").lower()
        for pattern in FORBIDDEN_PUBLIC_PATTERNS:
            require(pattern.lower() not in text, f"{relative}: forbidden public/internal term: {pattern}")


def main() -> int:
    for directory in REQUIRED_DIRS:
        require((ROOT / directory).is_dir(), f"required directory missing: {directory}")

    for path in REQUIRED_GOLD_PAPERS + REQUIRED_REFERENCE_FILES + REQUIRED_RUBRICS + REQUIRED_EXAMPLES + REQUIRED_TEMPLATES:
        require((ROOT / path).is_file(), f"required file missing: {path}")

    validate_root_skill(ROOT / "SKILL.md")

    for skill_path in sorted((ROOT / "skills").glob("*/SKILL.md")):
        validate_skill(skill_path)

    validate_gold_papers()
    validate_eval_tasks(ROOT / "evaluation" / "evals.json")
    validate_public_term_separation()
    run_static_evals.run_all()
    print("ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
