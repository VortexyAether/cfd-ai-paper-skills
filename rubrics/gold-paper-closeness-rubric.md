# Gold-Paper Closeness Rubric

Use this rubric when comparing generated CFD-AI/SciML manuscript text to the writing, argument, and evidence patterns in the gold-paper notes. It is not a grammar rubric. It checks whether the output sounds and behaves like a real fluid-mechanics/SciML paper rather than generic AI academic prose.

Score each axis 0–3.

| Axis | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Physical problem anchoring | Opens with generic AI/CFD importance | Names broad field but not flow/regime/quantity | Names flow/task and key variable | Names flow case, regime, variables, governing bottleneck, and why the task matters physically |
| Rhetorical move fidelity | Paragraphs are interchangeable boilerplate | Has context/method/results but weak order | Mostly follows context → gap → method → evidence → scope | Each section uses gold-paper moves: physical context, narrow gap, method role, evidence stack, limitation boundary |
| Field-native collocations | Uses phrases like novel framework, powerful model, complex dynamics | Some field terms mixed with generic AI wording | Mostly uses task/variable/baseline language | Uses natural CFD/SciML collocations: low-resolution snapshot, high-resolution field, vorticity PDF, spectra, Reynolds-number holdout, conservation residual |
| Evidence sequence | Claims precede or replace evidence | Evidence is mentioned but not ordered | Quantitative and visual evidence are present | Evidence follows a journal-like sequence: setup validation, baseline, field/error plot, physical diagnostic, ablation/generalization, limitation |
| Claim calibration | Loaded adjectives without proof | Some adjectives scoped | Most claims tied to evidence/TODO | Every claim word is either evidence-backed, narrowed to tested conditions, or converted to a required experiment |
| Gold-author pattern match | No visible relation to gold papers | Superficial citation or author name | Uses one or two domain patterns | Matches relevant author pattern: Fukami reconstruction grammar, Brunton taxonomy, Maulik uncertainty/ROM, Lee mechanism/wake, Vinuesa opportunity+caveat |
| Figure/caption grammar | Decorative figures/captions | Figure list lacks claim role | Captions include condition/metric | Captions read as mini-arguments with condition, diagnostic, comparator, and claim supported |
| Limitation/reviewer defense | Limitations are generic future work | Names broad missing pieces | Names several untested axes | Names reviewer-relevant missing evidence: BC/IC, grid, solver, split, seeds, baselines, physical diagnostics, OOD axis, code/data |
| Source-scope discipline | Invents details | Hedges but still implies unknown facts | Most unknowns marked | Unknown solver/metric/figure/citation details are explicitly marked TODO without weakening the supported contribution |
| Normal-paper texture | Overly symmetrical AI prose or marketing rhythm | Some unnatural AI phrasing remains | Mostly natural with occasional stiffness | Reads like journal prose: specific nouns, measured verbs, local transitions, no decorative hype, no generic promise paragraphs |

## Scoring interpretation

- **0–1 average**: generic AI academic output; do not use as manuscript seed.
- **1–2 average**: usable outline but too far from field paper texture.
- **2–2.6 average**: acceptable draft seed with targeted rewrite required.
- **2.6+ average**: close enough to gold-paper style for package benchmark pass.

## Hard fails

Any of these cap the overall verdict at weak-pass or fail:

- unsupported `robust`, `generalizable`, `physically consistent`, `state-of-the-art`, or `real-time` in abstract/conclusion;
- method-first opening that never names flow case, variable, regime, or reference data;
- a result section with field images but no metric, baseline, or physical diagnostic;
- invented solver/mesh/BC/IC/DOI/citation details;
- a limitation paragraph that says only “future work will extend the method.”

## Evaluator table

Use this table in benchmark reports:

| Axis | Score 0–3 | Evidence from output | Gold-paper target | Required rewrite |
|---|---:|---|---|---|

## Practical target

The goal is not to mimic author style cosmetically. The goal is to reproduce the scientific contract that makes the gold papers credible: precise physical setting, limited ML role, ordered evidence, visible uncertainty, and reviewer-aware boundaries.
