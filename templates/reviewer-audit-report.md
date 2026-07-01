# Reviewer Audit Report

## Source-scope ledger

| Source item | Supplied? | Notes / TODO |
|---|---|---|
| Manuscript text / abstract | | |
| Figures / tables | | |
| Physical setup | | |
| Numerical data generation | | |
| ML method details | | |
| Metrics / diagnostics | | |
| Baselines | | |
| Reproducibility artifacts | | |

## Gate summary

| Gate | Decision | Reason |
|---|---|---|
| Submission readiness | | |
| Fatal issues | | |
| Major issues | | |
| Highest-risk claim | | |
| Minimum rescue path | | |

## Claim-evidence audit

| Claim | Type | Evidence supplied | Status | Reviewer risk | Safer wording |
|---|---|---|---|---|---|

## Reviewer-risk ledger

| Severity | Issue | Missing evidence | Likely reviewer objection | Required fix | Artifact to add |
|---|---|---|---|---|---|

## Evidence-surface checklist

| Surface | Present? | Missing/TODO | Why reviewers care |
|---|---|---|---|
| Physical problem: geometry/domain, BC/IC, regime, nondimensional numbers | | | |
| Numerical data: solver/fidelity, mesh/grid, timestep/CFL, convergence | | | |
| Split/generalization: Re, geometry, BC, mesh, time, OOD/noise | | | |
| ML method: input/output, architecture, normalization, loss, optimizer | | | |
| Physics claim: loss/architecture/constraints/data/evaluation location | | | |
| Metrics: relative error, physical diagnostics, QoIs | | | |
| Baselines: classical and ML, same data/split/metric | | | |
| Figures: GT/input/pred/error, diagnostics, failure cases | | | |
| Deployment: runtime, memory, hardware, fallback, solver-coupled cost | | | |

## Required rescue experiments / artifacts

| Priority | Experiment/table/figure/rewrite | Claim rescued | Minimum acceptable evidence |
|---|---|---|---|

## Loaded-language rewrite table

| Original phrase | Why unsafe | Safer wording |
|---|---|---|

## Final recommendation

- Decision:
- What to fix first:
- What can wait:
- Claims to remove if evidence cannot be added:
