#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from typing import Final


ROOT: Final = Path(__file__).resolve().parents[1]
TRIGGER_TESTS: Final = ROOT / "evaluation" / "trigger-tests.yaml"
SCHEMA_TESTS: Final = ROOT / "evaluation" / "schema-tests.yaml"
REQUIRED_RUN_FILES: Final = (
    "prompt.md",
    "skill-version.md",
    "dumb-output.md",
    "evaluator-scorecard.md",
    "tars-decision.md",
)
EXPECTED_RUN_DIRS: Final = (
    "2026-06-30-v04-brunton-taxonomy-reconstruction",
    "2026-06-30-v04-fukami-super-resolution-reconstruction",
    "2026-06-30-v04-lee-cylinder-wake-reviewer-attack",
)
RUN_TASKS: Final = {
    "2026-06-30-v04-brunton-taxonomy-reconstruction": "evaluation/tasks/brunton-taxonomy-reconstruction.md",
    "2026-06-30-v04-fukami-super-resolution-reconstruction": "evaluation/tasks/fukami-super-resolution-reconstruction.md",
    "2026-06-30-v04-lee-cylinder-wake-reviewer-attack": "evaluation/tasks/lee-cylinder-wake-reviewer-attack.md",
}
TRIGGER_KEYS: Final = frozenset(("id", "prompt", "expected_skill", "eval_task"))
SCHEMA_KEYS: Final = frozenset(("id", "skill", "template", "rubric", "eval_task", "gold_paper"))


class StaticEvalError(AssertionError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise StaticEvalError(message)


def parse_simple_yaml_list(path: Path, allowed_keys: frozenset[str]) -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    for line_number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        stripped = raw_line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("- "):
            if current is not None:
                records.append(current)
            current = {}
            key, value = parse_key_value(stripped[2:], path, line_number)
            require(key in allowed_keys, f"{path}:{line_number}: unexpected key {key}")
            current[key] = value
            continue
        require(current is not None, f"{path}:{line_number}: key before list item")
        key, value = parse_key_value(stripped, path, line_number)
        require(key in allowed_keys, f"{path}:{line_number}: unexpected key {key}")
        require(key not in current, f"{path}:{line_number}: duplicate key {key}")
        current[key] = value
    if current is not None:
        records.append(current)
    require(records, f"{path}: no records found")
    return records


def parse_key_value(raw: str, path: Path, line_number: int) -> tuple[str, str]:
    require(":" in raw, f"{path}:{line_number}: expected key: value")
    key, value = raw.split(":", 1)
    key = key.strip()
    value = value.strip().strip('"')
    require(bool(key), f"{path}:{line_number}: empty key")
    require(bool(value), f"{path}:{line_number}: empty value for {key}")
    return key, value


def relative_file(raw_path: str, label: str, expected_parent: str) -> Path:
    path = Path(raw_path)
    require(not path.is_absolute(), f"{label} path must be relative: {raw_path}")
    require(".." not in path.parts, f"{label} path must not escape package: {raw_path}")
    resolved = (ROOT / path).resolve()
    require(resolved.is_relative_to(ROOT), f"{label} path resolves outside package: {raw_path}")
    parent = (ROOT / expected_parent).resolve()
    require(resolved.is_relative_to(parent), f"{label} path must be under {expected_parent}: {raw_path}")
    require(resolved.is_file(), f"{label} path missing: {raw_path}")
    return resolved


def skill_path(skill_name: str) -> Path:
    path_fragment = Path(skill_name)
    require(not path_fragment.is_absolute(), f"skill name must be relative: {skill_name}")
    require(".." not in path_fragment.parts, f"skill name must not escape skills/: {skill_name}")
    path = (ROOT / "skills" / path_fragment / "SKILL.md").resolve()
    skills_root = (ROOT / "skills").resolve()
    require(path.is_relative_to(skills_root), f"skill path resolves outside skills/: {skill_name}")
    require(path.is_file(), f"skill missing: {skill_name}")
    return path


def validate_trigger_tests() -> int:
    count = 0
    for record in parse_simple_yaml_list(TRIGGER_TESTS, TRIGGER_KEYS):
        require("id" in record, "trigger test missing id")
        require("prompt" in record, f"trigger {record.get('id', '<unknown>')} missing prompt")
        require("expected_skill" in record, f"trigger {record['id']} missing expected_skill")
        require("eval_task" in record, f"trigger {record['id']} missing eval_task")
        skill_path(record["expected_skill"])
        relative_file(record["eval_task"], "eval_task", "evaluation/tasks")
        count += 1
    return count


def validate_schema_tests() -> int:
    count = 0
    for record in parse_simple_yaml_list(SCHEMA_TESTS, SCHEMA_KEYS):
        require("id" in record, "schema test missing id")
        require("skill" in record, f"schema {record['id']} missing skill")
        skill_path(record["skill"])
        expected_parents = {
            "template": "templates",
            "rubric": "rubrics",
            "eval_task": "evaluation/tasks",
            "gold_paper": "references/gold-papers",
        }
        for key, expected_parent in expected_parents.items():
            require(key in record, f"schema {record['id']} missing {key}")
            relative_file(record[key], key, expected_parent)
        count += 1
    return count


def validate_eval_runs() -> int:
    count = 0
    for dirname in EXPECTED_RUN_DIRS:
        run_dir = ROOT / "evaluation" / "runs" / dirname
        require(run_dir.is_dir(), f"expected run directory missing: {dirname}")
        for filename in REQUIRED_RUN_FILES:
            artifact = run_dir / filename
            require(artifact.is_file(), f"{run_dir}: missing {filename}")
            require(artifact.stat().st_size > 0, f"{artifact}: empty artifact")
        patch_artifacts = (run_dir / "patched-skill-diff.md", run_dir / "recommended-patch.md")
        existing_patch_artifacts = [path for path in patch_artifacts if path.is_file()]
        require(bool(existing_patch_artifacts), f"{run_dir}: missing patched-skill-diff.md or recommended-patch.md")
        require(
            any(path.stat().st_size > 0 for path in existing_patch_artifacts),
            f"{run_dir}: patch artifact is empty",
        )
        prompt_text = (run_dir / "prompt.md").read_text(encoding="utf-8").lower()
        require("simulated dumb-agent run" in prompt_text, f"{run_dir}: prompt must label simulated dumb-agent run")
        skill_text = (run_dir / "skill-version.md").read_text(encoding="utf-8")
        for skill in task_skills(relative_file(RUN_TASKS[dirname], "run_task", "evaluation/tasks")):
            skill_path(skill)
            require(f"skills/{skill}/SKILL.md" in skill_text, f"{run_dir}: missing task skill in skill-version.md: {skill}")
        count += 1
    require(count >= 3, "expected at least 3 v0.4 eval run directories")
    return count


def task_skills(task_path: Path) -> list[str]:
    skills: list[str] = []
    in_section = False
    for line in task_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("## "):
            in_section = stripped.lower() == "## skill under test"
            continue
        if in_section and stripped.startswith("- `") and stripped.endswith("`"):
            skills.append(stripped.removeprefix("- `").removesuffix("`"))
        if in_section and stripped and not stripped.startswith("- `"):
            break
    require(skills, f"{task_path}: no skills under test found")
    return skills


def run_all() -> tuple[int, int, int]:
    return validate_trigger_tests(), validate_schema_tests(), validate_eval_runs()


def main() -> int:
    trigger_count, schema_count, run_count = run_all()
    print(f"trigger_tests: {trigger_count}")
    print(f"schema_tests: {schema_count}")
    print(f"eval_runs: {run_count}")
    print("ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
