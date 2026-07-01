---
title: CFD-AI Paper Skills Package
created: 2026-06-30
updated: 2026-07-01
source: TARS
status: v0.5
tags:
  - cfd-ai
  - sciml
  - paper-writing
  - hermes-skills
---

# CFD-AI Paper Skills Package

Purpose: build a Hermes/Codex-compatible skill package for people writing, reviewing, auditing, and revising CFD-AI / scientific ML journal papers.

This is not a generic academic-writing prompt pack. It is a reviewer-defense and evaluation system for CFD, turbulence, neural operators, PINNs, surrogate modeling, closure modeling, reconstruction, and physics-aware ML papers.

## Gold-standard authors

VA's answer key:

- Kai Fukami
- Steven L. Brunton
- Romit Maulik
- Sangseung Lee
- Ricardo Vinuesa

Their first-author or senior/corresponding-author-level papers define the target patterns: physical problem clarity, careful positioning, reproducible numerics, fair baselines, meaningful diagnostics, honest limitations, and reviewer-defense structure.

## v0.5 structure

```text
skills/                 focused SKILL.md cockpits
references/gold-papers/ abstract/metadata-grounded answer-key analyses
rubrics/                0-3 evaluator-agent scoring rubrics
examples/               CFD-specific before/after examples
templates/              reusable manuscript/review artifacts
evaluation/             dumb-agent/evaluator protocols, tasks, scorecards, runs, static tests
scripts/                deterministic validators, LaTeX evaluator, export helper
```

## Core skills

| Skill | Job |
|---|---|
| `scientific-journal-writing` | Structure abstracts, introductions, claims, sections, and reviewer-safe prose. |
| `paper-claim-auditor` | Map every claim to evidence, risk, safer wording, or TODO. |
| `cfd-ml-paper-reviewer` | Stress-test manuscripts as a strict CFD/SciML reviewer. |
| `cfd-reproducibility-checker` | Audit equations, BC/IC, mesh, solver, splits, commands, and compute. |
| `sciml-experiment-auditor` | Audit baselines, splits, ablations, diagnostics, UQ, and efficiency. |
| `figure-and-result-storytelling` | Build figure sequences where each figure proves a claim. |
| `related-work-cartographer` / `related-work-synthesis` | Convert citation dumps into field taxonomies and gap paragraphs. |
| `latex-paper-production` | Produce and preflight LaTeX/BibTeX artifacts. |
| `paper-revision-loop-manager` / `response-to-reviewers` | Manage revision evidence and response letters. |

## v0.4 answer-key files

Start with `references/gold-papers/INDEX.md`.

The package now has 15 gold-paper analyses: the original five v0.3 files plus two additional papers per gold-answer author. Each file declares source scope and marks PDF-only details as `unknown/TODO` when not extracted.

Current v0.4 additions include:

- Fukami 2021 spatio-temporal super-resolution and Fukami 2023 SR survey.
- Brunton 2016 SINDy and Brunton 2021 ML workflow tutorial.
- Maulik 2021 neural ROM and Maulik 2023 multiscale GNN autoencoder.
- Lee 2021 CNN wake mechanism analysis and Lee 2022 rough-wall transfer learning.
- Vinuesa 2023 ML for experiments and Vinuesa 2023 DRL drag reduction.

## Evaluation loop

Use:

- `evaluation/dumb-agent.md`
- `evaluation/evaluator-agent.md`
- `evaluation/ab-loop.md`
- `evaluation/tasks/gold-paper-reconstruction-template.md`
- `evaluation/evals.json`
- `evaluation/trigger-tests.yaml`
- `evaluation/schema-tests.yaml`
- `scripts/run_static_evals.py`

Basic loop:

1. Give a weak agent one skill and one benchmark task.
2. Constrain source access.
3. Score output against gold-paper notes and rubrics.
4. Patch the skill only when the failure is benchmark-backed.
5. Save run artifacts under `evaluation/runs/`.

v0.4 includes three simulated dumb-agent runs:

- `evaluation/runs/2026-06-30-v04-fukami-super-resolution-reconstruction/`
- `evaluation/runs/2026-06-30-v04-lee-cylinder-wake-reviewer-attack/`
- `evaluation/runs/2026-06-30-v04-brunton-taxonomy-reconstruction/`

They are labeled simulated runs and do not claim an external model was spawned.

v0.5 adds two LaTeX manuscript benchmark tasks:

- `evaluation/tasks/cfd-ai-full-manuscript-generation-benchmark.md`
- `evaluation/tasks/cfd-ai-trend-review-manuscript-benchmark.md`

The corresponding controlled internal A/B runs are:

- `evaluation/runs/2026-07-01-full-manuscript-ab/`: no-skill failed at 1.2/3.0 average; skill-guided passed at 2.9/3.0 average.
- `evaluation/runs/2026-07-01-trend-review-ab/`: no-skill failed at 1.1/3.0 average; skill-guided passed at 3.0/3.0 average.

The trend-review benchmark is the recommended deployment gate for this package because it stresses workflow-first taxonomy, validation-axis depth, reproducibility discipline, reviewer-trap rewrites, and non-hallucination more strongly than a single-method manuscript seed.

## Rubrics

- `rubrics/claim-evidence-rubric.md`
- `rubrics/cfd-reproducibility-rubric.md`
- `rubrics/sciml-experiment-rubric.md`
- `rubrics/figure-evidence-rubric.md`
- `rubrics/skill-quality-rubric.md`
- `rubrics/vocabulary-style-rubric.md`

All are 0-3 scoreable for evaluator-agent use.

## Field-native style guardrail

AI-assisted manuscript prose must pass the field vocabulary guardrail:

- `references/field-terminology-style-guide.md`
- `rubrics/vocabulary-style-rubric.md`
- `examples/ai-ish-to-field-native-prose.md`

Loaded words such as `robust`, `generalizable`, `physically consistent`, `real-time`, `state-of-the-art`, `novel`, `interpretable`, and `efficient` are allowed only when the manuscript states the required evidence: regime, variable, baseline, metric, physical diagnostic, and limitation boundary. If evidence is missing, the output should mark a TODO rather than polish the overclaim.

## Examples And Templates

Examples:

- `examples/bad-to-good-abstract.md`
- `examples/weak-to-publishable-experiment-plan.md`
- `examples/citation-dump-to-taxonomy.md`
- `examples/generic-review-to-cfd-review.md`
- `examples/ai-ish-to-field-native-prose.md`

Templates:

- `templates/claim-evidence-map.md`
- `templates/experiment-plan.md`
- `templates/reviewer-report.md`
- `templates/response-letter.md`

## Validation

Run from package root:

```bash
python3 scripts/validate_package.py
python3 scripts/summarize_package.py
python3 scripts/run_static_evals.py
python3 scripts/evaluate_latex_output.py --tex evaluation/runs/2026-07-01-trend-review-ab/with_skill/main.tex --benchmark trend-review
python3 scripts/export_package.py --dry-run
PYTHONPYCACHEPREFIX=.tmp_pycache python3 -m py_compile scripts/*.py
rm -rf .tmp_pycache
```

Expected validation result:

```text
ok
```

## Ground rules

- One skill = one focused job.
- `SKILL.md` is the cockpit; references, rubrics, templates, scripts, and evals carry detail.
- Unknown facts are `unknown/TODO`; do not invent solver settings, citations, DOI, or author roles.
- Claim-evidence alignment outranks prose polish.
- Skill changes must be justified by benchmark/eval failures, not taste.
- Full-paper details must stay `unknown/TODO` unless a PDF/arXiv full-text extraction supports them.
