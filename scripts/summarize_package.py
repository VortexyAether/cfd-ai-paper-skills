#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from typing import Final

import run_static_evals


ROOT: Final = Path(__file__).resolve().parents[1]


def count_files(pattern: str) -> int:
    return sum(1 for path in ROOT.glob(pattern) if path.is_file())


def count_dirs(pattern: str) -> int:
    return sum(1 for path in ROOT.glob(pattern) if path.is_dir())


def main() -> int:
    evals = json.loads((ROOT / "evaluation" / "evals.json").read_text(encoding="utf-8"))
    trigger_count, schema_count, _run_count = run_static_evals.run_all()
    counts = {
        "skills": count_files("skills/*/SKILL.md"),
        "references": count_files("references/**/*.md"),
        "gold_papers": count_files("references/gold-papers/*.md") - count_files("references/gold-papers/INDEX.md"),
        "rubrics": count_files("rubrics/*.md"),
        "examples": count_files("examples/*.md"),
        "eval_tasks": len(evals.get("evals", [])),
        "eval_runs": count_dirs("evaluation/runs/2026-06-30-v04-*"),
        "trigger_tests": trigger_count,
        "schema_tests": schema_count,
    }
    for key, value in counts.items():
        print(f"{key}: {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
