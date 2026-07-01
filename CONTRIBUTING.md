# Contributing

Contributions should improve the package through evidence, not taste.

## Ground Rules

- One skill should do one focused job.
- Every `SKILL.md` must start at byte 0 with YAML frontmatter containing `name` and `description`.
- Skill descriptions must be trigger-oriented.
- Every skill needs an output schema, anti-patterns, and a verification checklist.
- Unknown scientific facts must remain `unknown/TODO`.
- Do not invent solver settings, citations, DOI values, author roles, benchmark numbers, or dataset licenses.
- Claim-evidence alignment outranks prose polish.
- Evaluation artifacts belong under `evaluation/runs/`.
- Skill improvements should be justified by benchmark or evaluation failures.

## Validation

Run from the package root:

```bash
python3 scripts/validate_package.py
python3 scripts/run_static_evals.py
python3 scripts/export_package.py --dry-run
PYTHONPYCACHEPREFIX=.tmp_pycache python3 -m py_compile scripts/*.py
rm -rf .tmp_pycache
```

If you update `scripts/evaluate_latex_output.py`, run it against at least one existing benchmark profile and one new/changed profile.

## Documentation

Public README/docs should be user-centered: what the package is, how to use it, what agent behaviors it provides, tutorials, workflows, limitations, and positioning.

Internal development notes belong in `references/`, `evaluation/`, or ignored local run artifacts.
