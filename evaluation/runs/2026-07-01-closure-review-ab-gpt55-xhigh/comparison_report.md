# Comparison report: closure review benchmark, gpt-5.5 xhigh

## Model setting

Both arms used `gpt-5.5` with `xhigh` reasoning through `codex exec`.

## Task and source scope

Target task: `evaluation/tasks/cfd-ai-closure-review-benchmark.md`.

Review topic: **Machine-learning turbulence closures: why a priori accuracy is not enough for RANS and LES deployment**.

Source scope:

- `no_skill`: benchmark task packet copied to `no_skill/task.md`; no package guidance; Codex run used `--ignore-rules` from the isolated no-skill run directory.
- `with_skill`: same task packet plus package router, review/writing/reproducibility/figure/LaTeX skills, local gold-paper notes, terminology guide, and rubrics.

Unknown paper-specific bibliography, DOI values, author lists, benchmark numbers, solver settings, datasets, and code repositories were required to remain `TODO`.

## Build status

Both artifacts compiled with Tectonic. Warnings were layout-only underfull/overfull boxes.

| Arm | TeX size | PDF size | Compile result |
|---|---:|---:|---|
| `no_skill` | 23,487 bytes | 60,609 bytes | compiled; warnings only |
| `with_skill` | 29,833 bytes | 68,901 bytes | compiled; warnings only |

## Deterministic artifact counts

| Arm | Lines | Sections | Tables | Figures | Bibitems | TODO hits |
|---|---:|---:|---:|---:|---:|---:|
| `no_skill` | 221 | 8 | 2 | 3 | 5 | 21 |
| `with_skill` | 336 | 9 | 3 | 3 | 7 | 27 |

## Scorecard

Score: 0--3. These are evaluator judgments backed by the compiled artifacts and content checks.

| Axis | no_skill | with_skill | Main difference |
|---|---:|---:|---|
| LaTeX compilability | 3.0 | 3.0 | Both compiled with Tectonic. |
| Review-paper structure | 2.3 | 3.0 | No-skill is coherent; with-skill has stronger review scaffold, limitations, conclusion, and agenda. |
| RANS/LES distinction | 2.8 | 3.0 | Both separate RANS and LES; with-skill ties each to different evidence contracts more systematically. |
| A priori vs a posteriori evidence | 2.6 | 3.0 | No-skill has the ladder; with-skill makes it the central review logic and repeats it through tables/figures. |
| Coupled-solver validation | 2.5 | 3.0 | With-skill is stricter about solver time step, residuals, wall-clock, fallback, and same-solver baselines. |
| Invariance/realizability/stability | 2.6 | 3.0 | With-skill separates representation evidence from admissibility/stability more cleanly. |
| UQ/verifiability | 2.3 | 3.0 | With-skill explicitly demands calibration, coverage, decision policy, abstention/fallback. |
| Reproducibility discipline | 2.2 | 3.0 | With-skill includes solver-coupling capsules and source-scope discipline. |
| Figure/table evidence logic | 2.4 | 3.0 | No-skill meets minimum; with-skill adds a third table and clearer claim-linked captions. |
| Field-native vocabulary | 2.6 | 3.0 | Both are cautious; with-skill is more naturally CFD-review-like and less generic. |
| Non-hallucination / TODO marking | 3.0 | 3.0 | Neither invents exact numbers/DOIs/solver settings. |
| **Average** | **2.57** | **3.00** | Skill margin remains visible under strong model. |

## No-skill strengths

- Surprisingly strong because the task prompt itself is well designed.
- Correctly separates RANS and LES and names distinct diagnostics: mean velocity, Reynolds stresses, pressure coefficient, skin friction, separation/reattachment for RANS; spectra, SGS dissipation, resolved kinetic energy, drift for LES.
- Includes a priori/a posteriori evidence ladder, three boxed figure placeholders, reviewer-trap rewrites, and TODO placeholder bibliography.
- Avoids unsupported claims about solved turbulence, universal deployment, exact numbers, DOI values, and code repositories.

## No-skill failures / weaker points

- Has only the two required tables; the source-boundary/reproducibility surface is less inspectable than the with-skill arm.
- More narrative and less ledger-like: it explains evidence requirements but does not force as many reviewer-audit columns.
- UQ is described correctly, but calibration/decision/fallback evidence is less operational than in the with-skill artifact.
- Reproducibility is present, but not as strong as a solver-coupling capsule with time step, residuals, stability controls, wall-clock, hardware, memory, fallback, and same-solver baseline.
- Field-native vocabulary is good, but mostly inherited from the prompt; the output has less gold-paper/review-style scaffolding.

## With-skill strengths

- Starts from closure as a numerical-model component rather than generic ML promise.
- Organizes the review by closure role before method family, matching the package's workflow-first taxonomy rule.
- Makes a priori vs a posteriori the central evidence ladder instead of a one-off warning.
- Distinguishes representation evidence from realizability, boundedness, energy-transfer behavior, and coupled numerical stability.
- Includes a stronger reviewer-trap table with required validation/TODO column.
- Adds explicit source-scope discipline in limitations: exact metadata and paper-specific evidence stay TODO.
- Gives a more concrete research agenda: paired a priori/a posteriori benchmarks, closure-role-specific validation matrices, solver-coupling capsules, calibrated UQ tied to action, negative/boundary cases.

## Risky phrase audit

Both arms only use risky phrases inside reviewer-trap/overclaim tables, not as claims made by the manuscript.

| Phrase | no_skill handling | with_skill handling |
|---|---|---|
| `physically consistent` | Flagged as overclaim: invariant inputs do not prove it. | Same, with explicit realizability/stability TODO. |
| `generalizable` | Rewritten to held-out geometry/Re/pressure-gradient/regime tests. | Same, plus leakage-safe split wording. |
| `state-of-the-art` | Requires same-data/same-solver/same-metric baselines. | Same. |
| `real-time` | Rewritten to solver wall-clock/hardware/runtime evidence. | Same, with full coupled runtime and fallback overhead. |
| `robust` | Not present. | Present only as overclaim needing condition/range/failure boundary. |

## Verdict

The review benchmark is harder than the Fukami reconstruction task because the no-skill prompt already contains a strong evidence packet. Still, the skill-guided arm wins clearly.

The margin is not fluency. Both are fluent. The skill margin is:

1. stronger workflow-first review structure;
2. more inspectable evidence ladders and tables;
3. stricter solver-coupled deployment boundaries;
4. better UQ/calibration/fallback operationalization;
5. more explicit source-scope and reviewer-risk discipline.

Conclusion: **with-skill passes as a stronger review-manuscript seed; no-skill is usable but less audit-ready.**

## Files

- `model_settings.md`
- `task.md`
- `no_skill/prompt.md`
- `no_skill/main.tex`
- `no_skill/main.pdf`
- `no_skill/compile.log`
- `with_skill/main.tex`
- `with_skill/main.pdf`
- `with_skill/compile.log`
