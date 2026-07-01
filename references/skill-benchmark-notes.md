---
title: Skill benchmark notes
created: 2026-06-30
updated: 2026-06-30
source: skill-benchmark notes and documentation review
status: v0.3-updated
tags:
  - skills
  - benchmark
  - agent-design
---

# Skill benchmark notes

## Public skill-format benchmark

Observed from Claude custom-skill documentation and common Agent Skills conventions:

- Skill is a folder with `SKILL.md`.
- `SKILL.md` starts at byte 0 with YAML frontmatter.
- Required fields are usually `name` and `description`.
- Optional support folders: `references/`, `scripts/`, `assets/`.
- Best practice: keep each skill focused. Multiple focused skills compose better than one giant skill.
- Good descriptions are trigger-oriented: they tell the agent when to load the skill.
- Testing/validation is part of mature skill development.

## What famous skills do well

Patterns to copy:

1. Narrow trigger condition.
2. Concrete workflow, not philosophy.
3. Bundled references/templates/scripts when the workflow needs them.
4. Verification steps at the end.
5. Examples that anchor output shape.
6. Anti-patterns that prevent common failure modes.

## What to avoid

Bad skill behavior:

- Too broad: “write better papers.” Useless. Human-level fog.
- No verification: produces fluent nonsense.
- No output schema: every run looks different.
- No domain constraints: generic academic writing ignores CFD reviewer risks.
- No evaluation loop: cannot tell if the skill improves anything.

## Benchmark criteria for this package

Each skill should be scored from 0–3 on:

1. Trigger precision
2. Domain specificity
3. Workflow concreteness
4. Output template clarity
5. Verification rigor
6. Gold-paper alignment
7. Baseline-agent usability
8. Failure-mode coverage

Minimum acceptable average: 2.5/3.

## Package-level standard

A strong skill package should include:

```text
cfd-ai-paper-skills/
├── README.md
├── skills/
│   ├── scientific-journal-writing/SKILL.md
│   ├── cfd-ml-paper-reviewer/SKILL.md
│   └── ...
├── references/
│   ├── gold-standard-paper-map.md
│   ├── figure-archetypes.md
│   ├── experiment-matrices.md
│   └── journal-expectations.md
├── templates/
│   ├── claim-evidence-map.md
│   ├── reviewer-report.md
│   ├── response-letter.md
│   └── experiment-plan.md
└── evaluation/
    ├── baseline-agent-evaluator-protocol.md
    ├── tasks/
    └── scorecards/
```

v0.3 implements the advertised reference layer with:

- `references/figure-archetypes.md`
- `references/experiment-matrices.md`
- `references/journal-expectations.md`
- `references/gold-papers/*.md`
- `rubrics/*.md`
- `examples/*.md`

## Why this matters

The package must be usable by a weak agent. If only a strong model can use it, the skill is not encoding procedure; it is just decorating an already competent model. Unacceptable. Shiny nonsense with YAML.
