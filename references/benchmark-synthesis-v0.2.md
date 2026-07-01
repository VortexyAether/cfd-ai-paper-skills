---
title: Benchmark synthesis v0.2
created: 2026-06-30
updated: 2026-06-30
source: TARS + delegated benchmark agent
status: archived-v0.2-input-superseded-by-v0.3
tags:
  - cfd-ai
  - skills
  - benchmark
  - agent-evals
---

# Benchmark synthesis v0.2

> v0.3 note: this file is retained as historical benchmark input. Current v0.3 package structure is summarized in `README.md`, operational rubrics live in `rubrics/`, and evaluator workflow lives in `evaluation/evaluator-agent.md`, `evaluation/dumb-agent.md`, and `evaluation/ab-loop.md`.

Benchmarked sources:

- Anthropic/Claude Skills documentation: `SKILL.md`, YAML frontmatter, `references/`, `scripts/`, `assets/`, `skills-ref validate`.
- Claude Code subagents: `name`, `description`, optional `tools`, `model`; description as trigger; context/tool isolation.
- OpenAI/Codex Skills: versioned bundle, `SKILL.md` manifest, model sees name/description/path first; references/scripts/assets; one job per skill.
- AGENTS.md convention: agent-facing repo instructions, tests, style, PR instructions.
- OpenAI agent evals: traces → graders → datasets/eval runs → iterative improvement.
- NeurIPS checklist: claims, limitations, reproducibility, code/data, ethics, LLM usage.
- ML Reproducibility Checklist: math setting, assumptions, complexity, datasets/splits/preprocessing, dependencies, commands, hyperparameters, metrics, variance, compute.
- ICLR Reviewer Guide: objective, motivation/literature placement, claim support, significance, constructive review.
- CFD reproducibility literature: mesh generation, BCs, solver choices, averaging windows, code differences, nondeterminism.

---

## Design conclusions

### 1. One skill = one job

Do not create one giant “paper helper.” It will trigger too broadly and produce fog.

Use focused skills:

- claim auditing
- CFD reproducibility
- SciML experiment auditing
- related-work cartography
- reviewer simulation
- limitations/ethics/LLM disclosure
- revision loop management
- LaTeX production

### 2. Description is the trigger

The description must say when to use the skill, not advertise it.

Bad:

> Helps write better papers.

Good:

> Use when a CFD/SciML manuscript reports numerical experiments and needs audit of mesh, boundary conditions, solver settings, data splits, baselines, hyperparameters, and reproduction commands.

### 3. Progressive disclosure

Keep `SKILL.md` short enough to load. Put heavy material in:

- `references/`
- `templates/`
- `rubrics/`
- `tests/`
- `scripts/` if deterministic checks exist

### 4. Output schema is mandatory

Every skill must emit:

- evidence location,
- severity/risk,
- recommended fix,
- unknown/TODO marker,
- verification status.

No schema = no evaluation. No evaluation = skill theater.

### 5. Evaluation is part of the package

A release-quality skill package needs:

- trigger tests,
- rubric regression tests,
- adversarial tests,
- scorecards,
- trace/run artifacts,
- pass thresholds.

---

# Archived v0.2 package skill map

## MVP from current package

Existing v0.1 names are usable:

- `scientific-journal-writing`
- `cfd-ml-paper-reviewer`
- `related-work-synthesis`
- `experiment-design-for-sciml`
- `figure-and-result-storytelling`
- `latex-paper-production`
- `journal-submission-checklist`
- `response-to-reviewers`

## Benchmark-aligned additions / aliases

Add these as sharper skills or aliases:

1. `paper-claim-auditor`
2. `cfd-reproducibility-checker`
3. `sciml-experiment-auditor`
4. `related-work-cartographer`
5. `reviewer-simulator`
6. `limitations-ethics-llm-disclosure`
7. `paper-revision-loop-manager`

Mapping:

| Benchmark skill | Existing overlap | Recommendation |
|---|---|---|
| paper-claim-auditor | scientific-journal-writing | create separate skill; claim audit is core and testable |
| cfd-reproducibility-checker | cfd-ml-paper-reviewer | create separate skill; CFD details deserve own checklist |
| sciml-experiment-auditor | experiment-design-for-sciml | rename/alias or keep both; auditor is stricter |
| related-work-cartographer | related-work-synthesis | create alias or v0.2 rewrite |
| reviewer-simulator | cfd-ml-paper-reviewer | create generic journal-review simulator; keep CFD reviewer separate |
| limitations-ethics-llm-disclosure | journal-submission-checklist | create separate; checklist is too late-stage |
| paper-revision-loop-manager | response-to-reviewers | create separate; response letter is one artifact, revision loop is process |

---

# Required package structure

```text
CFD-AI_Paper_Skills_Package/
├── README.md
├── AGENTS.md
├── skills/
│   ├── paper-claim-auditor/SKILL.md
│   ├── cfd-reproducibility-checker/SKILL.md
│   ├── sciml-experiment-auditor/SKILL.md
│   ├── related-work-cartographer/SKILL.md
│   ├── reviewer-simulator/SKILL.md
│   ├── limitations-ethics-llm-disclosure/SKILL.md
│   ├── paper-revision-loop-manager/SKILL.md
│   └── ...
├── references/
├── templates/
├── evaluation/
│   ├── evals.json
│   ├── tasks/
│   ├── scorecards/
│   └── runs/
└── scripts/  # optional deterministic validators later
```

---

# Rubric standards

## Claim rubric

| Score | Meaning |
|---|---|
| 0 | unsupported or contradicted |
| 1 | weak/partial evidence |
| 2 | supported under narrow assumptions |
| 3 | strongly supported with clear scope |

Axes:

- novelty
- technical correctness
- empirical support
- reproducibility
- clarity
- significance
- limitation honesty

## CFD reproducibility rubric

| Axis | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| governing equations | missing | partial | stated | complete with assumptions |
| BC/IC | missing | vague | mostly specified | complete/reproducible |
| mesh/time convergence | none | informal | partial | systematic |
| solver details | absent | software only | key settings | full config/commands |
| ML splits | absent | random only | partial | leakage-safe regime split |
| metrics | vague | generic | relevant | physics-aware + reproducible |
| compute/runtime | absent | rough | partial | exact hardware/runtime |

---

# Required tests

## Trigger tests

```yaml
- prompt: "Check whether my PINN paper is reproducible."
  expected_skill: sciml-experiment-auditor

- prompt: "Rewrite the abstract to avoid overclaiming."
  expected_skill: paper-claim-auditor

- prompt: "Audit mesh convergence and boundary conditions."
  expected_skill: cfd-reproducibility-checker
```

## Regression tests

Example:

```yaml
case: missing_boundary_conditions
input: "We simulate flow over an airfoil using OpenFOAM..."
expected_flags:
  - boundary_conditions_missing
  - solver_settings_missing
  - mesh_convergence_missing
```

## Adversarial tests

- “all details are in supplementary” but no supplement.
- “SOTA” claim without baselines.
- “generalizes to turbulent flows” but laminar-only tests.
- code URL placeholder.
- LLM used in analysis/code but no disclosure.

---

# CI-like release thresholds

- trigger accuracy ≥ 90%
- critical issue recall ≥ 85%
- hallucinated critique ≤ 5%
- output schema compliance = 100%

These are aspirational until we build an automated runner. Still better than vibes. Barely a contest.
