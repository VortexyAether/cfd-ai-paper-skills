# Abstract-only Fukami reconstruction A/B comparison

## Purpose

Benchmark requested: give only a paper abstract and ask the model to infer what the full paper probably contained: thesis, method, experiments, figures, reviewer risks, and unknowns.

This is intentionally simpler than the earlier review-manuscript benchmark and avoids giving the no-skill arm a long evidence ladder.

## Source scope and contamination controls

| Arm | Source scope |
|---|---|
| `no_skill` | title + abstract only; ran from `/tmp` outside the package with `--ignore-rules`; no package files/rubrics/gold notes named |
| `with_skill` | same title + abstract plus general CFD-AI skills/rubrics/style guides; explicitly instructed not to open `references/gold-papers/fukami-2019-*` or prior run outputs |
| evaluator | after both generations, compared outputs against `references/gold-papers/fukami-2019-super-resolution-jfm.md` |

Both arms used `gpt-5.5` with `xhigh` reasoning.

## Answer-key patterns used for scoring

From the local Fukami 2019 gold note:

- task: low-resolution to high-resolution turbulent flow-field reconstruction;
- models: CNN and hybrid DSC/MS;
- cases: cylinder wake at `Re_D=100`; two-dimensional homogeneous decaying turbulence;
- variables: velocity and/or vorticity;
- data generation: DNS stated, exact solver details TODO;
- downsampling: average and max pooling;
- baseline: bicubic interpolation;
- training/loss: L2 objective, Adam, early stopping in accessible text;
- evidence stack: pipeline/downsampling/model schematics, cylinder wake reconstruction and L2 error, snapshot-count sensitivity, vorticity PDF, homogeneous-turbulence GT/coarse/pred/error, quantitative comparison, likely spectra/statistical diagnostics;
- reviewer defenses: canonical laminar case first, turbulent stress test, classical interpolation baseline, physical variables/regime, bounded reconstruction claim.

## Scorecard

Score 0--3.

| Axis | no_skill | with_skill | Notes |
|---|---:|---:|---|
| Physical problem reconstruction | 3.0 | 3.0 | Both identify under-resolved flow-field super-resolution. |
| ML task transformation | 3.0 | 3.0 | Both infer paired low-res/high-res mapping and downsampling. |
| Model inference | 2.8 | 2.8 | Both infer CNN vs DSC/MS, multiscale/skip role; neither invents layers. |
| Experiment/case inference | 2.6 | 2.7 | Both recover cylinder wake + homogeneous turbulence + 50 snapshots; neither recovers `Re_D=100` or decaying turbulence, correctly left unknown. |
| Baseline/metric inference | 2.0 | 2.3 | Both infer interpolation; neither says bicubic or L2. With-skill frames baselines/metrics more cautiously. |
| Physical diagnostics inference | 2.1 | 2.6 | No-skill speculates spectra/vorticity; with-skill asks for spectra/PDF/statistics and flags visual similarity risk. |
| Figure sequence | 2.5 | 2.7 | Both produce plausible pipeline/architecture/field/error/training sweep sequence; with-skill has clearer confidence labels. |
| Reviewer attack realism | 2.5 | 3.0 | With-skill adds temporal leakage, 2D limitation, 50-snapshot dependence, ablations, and reproducibility risk. |
| Unknown/TODO discipline | 2.8 | 3.0 | Both avoid hard inventions; with-skill unknown list is more field-complete. |
| Gold-paper closeness | 2.4 | 2.8 | With-skill is closer to reconstruction-paper logic and less generic. |
| **Average** | **2.57** | **2.79** | Skill margin exists, but smaller than the flawed-abstract benchmark. |

## Deterministic term coverage

| Term family | no_skill | with_skill |
|---|---|---|
| Core task terms | low/high resolution, CNN, DSC/MS, cylinder wake, homogeneous turbulence, 50 snapshots | same |
| Inferred baselines | interpolation | interpolation |
| Diagnostics | spectra, vorticity, error maps | spectra, PDF/statistics, velocity/vorticity/pressure, error maps |
| Reviewer risks | generalization, physical consistency, baseline strength, data leakage, 2D limits, 50-snapshot dependence | same plus temporal leakage wording, ablations, stationarity/synthetic downsampling, reproducibility |
| Unknowns | solver, grid, timestep, Re, variables, metrics, architecture, downsampling | same plus BC/IC, pressure/variable ambiguity, seed protocol, code/data/citation metadata |

## Main observation

This benchmark is fairer for “abstract -> likely paper contents” than the earlier long review benchmark.

The result is subtle:

- The abstract itself is information-rich, so `no_skill` already reconstructs much of the paper correctly.
- The skill arm does **not** magically recover hidden exact details like bicubic interpolation, L2 loss, Adam, average/max pooling, or `Re_D=100` because it was not allowed to open the exact answer key. Good. That means it did not just leak the answer.
- The skill value shows up in reviewer-risk framing and field-native completeness: temporal leakage, physical/statistical diagnostics, 2D-flow limitation, ablation demand, BC/IC/variable ambiguity, and source-scope discipline.

## Verdict

**with_skill wins, but by a modest margin.**

This is the expected behavior for a clean abstract-only reconstruction task: a strong base model can infer obvious contents from a detailed abstract, while the skill package mainly improves what a CFD reviewer would care to ask next.

## Files

- `prompt-no-skill.md`
- `prompt-with-skill.md`
- `no_skill_output.md`
- `with_skill_output.md`
- `model_settings.md`
