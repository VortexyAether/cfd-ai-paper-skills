# Task: Lee cylinder wake reviewer attack

## Skill under test

- `cfd-ml-paper-reviewer`
- `experiment-design-for-sciml`

## Gold reference

Sangseung Lee and Donghyun You, *Data-driven prediction of unsteady flow fields over a circular cylinder using deep learning*, JFM 879:217–254 / arXiv:1804.06076.

## Baseline-agent prompt

A manuscript claims: “Our deep learning model accurately predicts unsteady cylinder wake flow and generalizes to new flow conditions.” Critique it as a CFD reviewer.

## Expected answer-key patterns

- Requires Re/regime, domain, BC/IC, solver, grid, timestep/CFL.
- Needs temporal rollout stability, not just one-step error.
- Needs train/test split clarity and unseen condition tests.
- Needs GT/pred/error fields and quantitative metrics.
- Generalization claim must be bounded unless unseen Re/geometry/BC are tested.
