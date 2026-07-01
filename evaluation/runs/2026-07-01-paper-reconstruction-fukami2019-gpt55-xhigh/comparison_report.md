# Comparison report: Fukami 2019 reconstruction, gpt-5.5 xhigh

## Model setting

Model setting for both benchmark arms: `gpt-5.5`, `xhigh reasoning`, Codex exec.

## Task and source scope

Target task: `evaluation/tasks/fukami-super-resolution-reconstruction.md`.

Target paper: Fukami, Fukagata, and Taira, *Super-resolution reconstruction of turbulent flows with machine learning*, Journal of Fluid Mechanics, 2019.

Source scope:

- no_skill: task prompt plus dense source summary only;
- with_skill: task prompt, dense source summary, relevant package guidance, and the local Fukami 2019 gold-paper note;
- full PDF figure-caption verification remains TODO;
- unknown solver details, exact numerical values, architecture layer counts, split seeds, code status, and panel order remain TODO/unknown.

## No-skill strengths

- Much stronger than the prior baseline: it obeys the explicit TODO instruction and does not assert real-time deployment, universal generalization, or exact numerical performance.
- Correctly identifies the low-resolution to high-resolution flow-field mapping, CNN/hybrid model family, bicubic baseline, cylinder wake at `Re_D=100`, and two-dimensional homogeneous decaying turbulence.
- Includes practical reviewer concerns and follow-on experiment needs.
- Marks missing solver, architecture, split, and spectral/statistical details as TODO.

## No-skill failures

- The manuscript is mainly narrative; it does not force every claim into a claim-evidence table.
- It mentions physical/statistical diagnostics and spectra as likely evidence, but the boundary between supplied evidence and PDF-level TODO is less visible than in the with-skill arm.
- Reproducibility gaps are listed in prose, not prioritized by rejection risk.
- Vocabulary control is mostly prompt-driven. Suspicious phrases are avoided, but there is no explicit phrase gate for robust/generalizable/physically consistent/real-time claims.
- The bibliography remains TODO-bounded in the arm, which is fair under the no-skill source scope but less useful as a reconstruction artifact.

## With-skill strengths

- Starts with source scope and a one-sentence bounded claim.
- Converts the paper reconstruction into a claim-evidence map, so unsupported claims become explicit TODOs.
- Adds a CFD reproducibility ledger that separates partial evidence from missing BC/IC, mesh, solver, split, and compute details.
- Uses field-native reconstruction vocabulary: low-resolution input, high-resolution target, velocity/vorticity fields, bicubic interpolation, vorticity PDF, spectra/statistical diagnostics, and named flow cases.
- Explicitly blocks overclaims about robustness, generalization, real-time deployment, solver acceleration, and universal turbulence recovery.
- Uses the Fukami gold note to add verified bibliographic metadata and DOI while still marking PDF caption verification TODO.

## With-skill failures

- It is more audit-like than manuscript-like; tables dominate the artifact.
- Some TODOs are repetitive across the claim map, reproducibility ledger, and figure placeholders.
- The skill-guided arm still cannot verify exact figure captions, panel order, spectra, quantitative values, or code repository status from the available source scope.
- The package guidance did not include a compile-safe minimal LaTeX profile; optional formatting packages had to be removed because the available cached Tectonic bundle was limited.

## Claim-evidence comparison

| Axis | no_skill | with_skill |
|---|---|---|
| Claim boundary | Mostly bounded by prose TODOs | Explicit one-sentence claim plus unsupported-claim table |
| Accuracy claims | Avoids exact values; could still imply better reconstruction from likely evidence | States comparison structure and requires exact values before superiority claims |
| Physical consistency | Names vorticity PDFs and spectra, with spectra marked TODO | Separates supported PDF evidence from spectral/statistical TODOs |
| Generalization | Warns against broad claims | Explicitly blocks generalization unless a named holdout axis exists |
| Efficiency/deployment | Does not claim real-time deployment | Explicitly marks runtime, hardware, and deployment evidence TODO |
| Limitation honesty | Good for a general model | Stronger and more systematic |

## Hallucination and unsupported-claim audit

| Risk | no_skill | with_skill |
|---|---|---|
| Exact numerical errors | Not invented | Not invented |
| Exact architecture layer counts | Not invented | Not invented |
| Solver, mesh, BC/IC | Marked TODO in prose | Marked TODO in a reproducibility ledger |
| Code/data repository status | Not claimed | Unknown/TODO despite gold-note mention of an availability statement |
| Figure captions and panel order | Marked TODO | Marked TODO |
| Broad 3D/general turbulence claim | Avoided | Explicitly rejected |

## Reproducibility audit

The with-skill arm is better here. The no-skill arm names missing items, but the with-skill arm scores them implicitly by category: governing equations partial, regime numbers partial, geometry partial, BC/IC missing, grid/time integration missing, data splits partial, ML training partial, baselines partial, compute/code status missing or unknown.

The strongest remaining reproducibility blockers are unchanged across both arms:

- exact DNS solver implementation;
- boundary and initial conditions;
- grid/resolution and time integration;
- train/validation/test split definition and seeds;
- pooling factors and low-resolution dimensions;
- full architecture and optimizer settings;
- verified code/data URL and commands.

## Vocabulary/style audit

The no-skill arm is substantially safer than the previous generic baseline because the stronger model followed the prompt. It avoids most marketing language and marks unknowns. The with-skill arm is still cleaner: it gates the exact suspicious terms (`robust`, `generalizable`, `physically consistent`, `real-time`, `efficient`) and rewrites them into evidence requirements.

## Verdict

Yes, the skill package still helps with a stronger base model, but the margin is smaller than in the earlier run. Under `gpt-5.5` with `xhigh reasoning`, the no-skill arm already respects many source-scope constraints. The skill-guided arm adds value by making the constraints inspectable: claim-evidence mapping, reproducibility triage, vocabulary gating, and explicit reviewer-defense boundaries.

The result is not that the with-skill prose is prettier. It is safer, more CFD-native, and easier to audit.

## Recommended package improvements from observed failures

- Add a benchmark-run template that records model, reasoning effort, source scope, compiler status, and validation status consistently.
- Add a minimal compile-safe LaTeX template that avoids optional packages and font styles when Tectonic cache access is limited.
- Add a strong-model comparison rubric so future reports distinguish "skill helped a weak model" from "skill still adds audit structure to a strong model."
- Add a no-skill contamination note to evaluation protocols: generate the no-skill arm before loading package rubrics when possible, or record the source separation explicitly.
- Add a compact manuscript-vs-audit balance checklist for with-skill outputs, so the skill arm remains readable as a manuscript seed while preserving evidence ledgers.
