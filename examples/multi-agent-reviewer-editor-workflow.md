# Multi-Agent Reviewer-Editor Workflow Example

## Input draft

> We introduce a novel AI framework that predicts turbulent wake dynamics with state-of-the-art accuracy. The model is robust across Reynolds numbers and geometries, physically consistent, and faster than CFD. These results reveal hidden flow physics and enable engineering design.

## Reviewer output

| Severity | Issue | Reviewer objection | Required fix |
|---|---|---|---|
| Fatal | `state-of-the-art accuracy` | no named baselines or metrics | same-data/split/metric baseline table |
| Fatal | `robust across Reynolds numbers and geometries` | no held-out Re/geometry split | validation matrix with interpolation/extrapolation and failure boundary |
| Fatal | `faster than CFD` / design use | no hardware, latency, memory, end-to-end workflow | runtime table and task-limited deployment scope |
| Major | `physically consistent` | no residuals, divergence, forces, spectra, or conservation checks | physical diagnostic figure/table |
| Major | `reveals hidden flow physics` | no mechanism analysis or validated physical interpretation | remove or replace with observable diagnostic claim |

## Evidence Auditor output

| Claim | Type | Supplied evidence | Missing/TODO | Safe status |
|---|---|---|---|---|
| predicts wake dynamics | accuracy | unspecified results | metrics, baselines, rollout horizon | weak |
| robust across Re/geometries | generalization | none | held-out split axes | unsupported |
| physically consistent | physical validity | none | residuals/QoIs | unsupported |
| faster than CFD | efficiency | none | hardware/runtime | unsupported |

## Experiment Planner output

| Claim rescued | Experiment / validation | Baseline | Metric / diagnostic | Failure mode tested |
|---|---|---|---|---|
| accuracy | same-split comparison | CFD reference, ROM/CNN/FNO if relevant | relative L2, RMSE, QoIs | weak baseline |
| generalization | held-out Re and geometry matrix | same model families | error by split axis | interpolation mistaken for extrapolation |
| physical consistency | diagnostic suite | CFD reference | divergence, residuals, Strouhal/force spectra | pretty but unphysical fields |
| efficiency | runtime test | CFD and surrogate workflow | latency, memory, hardware, speed-error curve | inference-only speed claim |

## Figure/Table Editor output

| Figure/table | Claim supported | Required panels/columns | Caption claim | Missing data |
|---|---|---|---|---|
| GT/pred/error wake fields | prediction quality | same color scale, error map | model reproduces tested wake structures | reference fields |
| Validation matrix table | generalization | train/test Re, geometry, BC, mesh | scope of tested transfer | split protocol |
| Physical diagnostic plot | physical fidelity | residual/divergence/force/frequency | fields preserve selected diagnostics | diagnostics |
| Runtime table | efficiency | hardware, latency, memory, CFD comparator | task-limited speed | timing data |

## Prose Editor output

> Accurate prediction of unsteady wake fields remains challenging when fast estimates are needed for repeated design or control studies. We evaluate a neural surrogate for wake-field prediction under the supplied flow configuration. The current evidence is insufficient to claim state-of-the-art accuracy, Reynolds-number or geometry generalization, physical consistency, or CFD replacement. To support those claims, the study must report the numerical setup, leakage-safe validation splits, same-scope baselines, quantitative errors, physical diagnostics, and end-to-end runtime on stated hardware.

## Gatekeeper output

| Original risk | After edit | Residual blocker | Next action |
|---|---|---|---|
| SOTA | removed | accuracy still unproven | baseline/metric table |
| generalization | removed | transfer untested | held-out split matrix |
| physical consistency | removed | physics fidelity unknown | diagnostic figure |
| faster than CFD | narrowed to fast estimates motivation | efficiency unknown | runtime table |

## Lesson

The multi-agent gain is not that seven agents write seven paragraphs. The gain is that no editor can smooth over a reviewer blocker without the gatekeeper seeing it.
