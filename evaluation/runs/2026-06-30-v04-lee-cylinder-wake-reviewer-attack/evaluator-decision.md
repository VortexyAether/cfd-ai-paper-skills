# Evaluator Decision

Decision: patch skills.

Reason: The reviewer skill allowed a weak agent to produce generic review language. Lee-style wake claims require explicit attack surfaces:

- Re/regime split,
- solver/grid/timestep/CFL/BC/IC,
- temporal rollout horizon,
- conservation residuals or physical-loss evidence,
- mechanism analysis when interpretability is claimed.

Patch targets:

- `skills/cfd-ml-paper-reviewer/SKILL.md`
- `skills/cfd-reproducibility-checker/SKILL.md`
- `skills/sciml-experiment-auditor/SKILL.md`

