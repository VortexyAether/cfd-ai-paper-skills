# Task: Reviewer-editor loop abstract rescue

## Skill under test

- `paper-revision-loop-manager`
- `reviewer-audit-toolkit`
- `scientific-journal-writing`
- `paper-claim-auditor`

## Prompt

Given only the abstract below, run a reviewer-to-editor loop:

1. reviewer audit;
2. editorial rewrite;
3. re-audit of the rewritten abstract;
4. next experiments/tables/figures needed to make stronger claims.

Do not invent solver, data, metric, citation, architecture, or runtime details.

Draft abstract:

> We introduce a novel AI framework that accurately predicts turbulent wake dynamics and reveals hidden flow physics. The method is robust across Reynolds numbers and geometries, physically consistent, and faster than CFD. Our results show excellent agreement with simulation data and demonstrate state-of-the-art performance for engineering design.

## Expected answer-key patterns

Reviewer pass:

- Gate should be reject-risk or major-revision risk.
- Fatal/Major issues should include: unsupported novelty, accuracy, hidden-physics discovery, robustness, generalization, physical consistency, faster-than-CFD, state-of-the-art, engineering-design use.
- Missing evidence should include: flow setup, solver/data generation, Re/geometry split, architecture/input-output/loss, metrics, baselines, physical diagnostics, runtime/hardware, failure cases.

Editor pass:

- Should not preserve `novel`, `robust`, `physically consistent`, `faster than CFD`, `state-of-the-art`, or `engineering design` unless turned into TODO/scoped evidence.
- Should start from wake-flow prediction or sparse/low-cost surrogate motivation, not AI capability.
- Should explicitly state preliminary / tested-scope / evidence-limited status.
- Should keep contribution meaningful while reducing claims.

Re-audit pass:

- Should list which original claims were removed/downgraded.
- Should list residual blockers.
- Should propose concrete rescue artifacts: validation matrix, baseline table, diagnostic figure, reproducibility table, runtime table.
