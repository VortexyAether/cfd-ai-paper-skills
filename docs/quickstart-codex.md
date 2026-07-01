# Quickstart: Codex

Use this guide when Codex can read the package directory.

## 1. Point Codex at the package

Give Codex the repository path and the skill files to follow:

```text
Use /path/to/cfd-ai-paper-skills as a local skill package.
Follow skills/paper-claim-auditor/SKILL.md and skills/cfd-reproducibility-checker/SKILL.md.
```

## 2. Provide evidence

Attach or point to the material the agent is allowed to use:

- manuscript draft;
- abstract/introduction;
- experiment notes;
- solver logs;
- result tables;
- figure drafts;
- BibTeX;
- reviewer comments.

Tell Codex that missing scientific facts must remain `TODO`.

## 3. Ask for an artifact

Good first tasks:

```text
Audit manuscript/main.tex. Return a claim-evidence table with columns: claim, evidence, missing evidence, reviewer risk, safer wording, and manuscript location.
```

```text
Review experiments.md for CFD/SciML reproducibility. Check solver, mesh, BC/IC, splits, baselines, diagnostics, uncertainty, hardware, runtime, and code/data availability.
```

```text
Use skills/latex-paper-production/SKILL.md to create a standalone LaTeX mini-review seed from evidence_packet.md. Include TODO bibliography entries only.
```

## 4. Run checks when editing this package

If Codex changes the package itself, ask it to run:

```bash
python3 scripts/validate_package.py
python3 scripts/run_static_evals.py
python3 scripts/export_package.py --dry-run
PYTHONPYCACHEPREFIX=.tmp_pycache python3 -m py_compile scripts/*.py
rm -rf .tmp_pycache
```

For LaTeX benchmark outputs, use:

```bash
python3 scripts/evaluate_latex_output.py --tex path/to/main.tex --benchmark trend-review
```

## Practical tips

- Name the skills explicitly for focused work.
- Give the agent permission to weaken unsafe claims.
- Ask for tables/checklists when auditing.
- Keep public claims separate from internal TODOs.
- Require source-scope notes for any related-work or benchmark landscape task.
