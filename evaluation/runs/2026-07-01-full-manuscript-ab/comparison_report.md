# Full manuscript A/B benchmark run

Run root:

`evaluation/runs/2026-07-01-full-manuscript-ab/`

Benchmark prompt:

`evaluation/tasks/cfd-ai-full-manuscript-generation-benchmark.md`

## Run type

Controlled baseline ablation:

- `no_skill/main.tex`: same evidence packet, no CFD-AI/SciML skill behavior applied; intentionally reflects generic AI manuscript failure modes.
- `with_skill/main.tex`: same evidence packet, generated with the CFD-AI/SciML paper-writing skill package principles.

This is not yet an external weak-model benchmark. It is a controlled internal A/B sanity test.

## Compile verification

Both outputs compile with Tectonic.

```text
no_skill/main.pdf    36K
with_skill/main.pdf  50K
```

Compile warnings are non-fatal layout warnings only:

- no-skill: Underfull hbox warnings in claim table.
- with-skill: Underfull hbox warnings in TODO/evidence tables.

No fatal LaTeX errors.

## Risky phrase scan

### No-skill baseline

The no-skill output uses unsupported or weakly supported language:

- `robust`
- `generalizable`
- `physically consistent`
- `real-time`
- broad `CFD acceleration`
- broad extension to three-dimensional turbulence and experimental data

It also claims:

- physical consistency from spectra/PDF only,
- generalization from two provided cases,
- real-time acceleration without runtime/hardware evidence.

### Skill-guided output

The skill-guided output mentions risky concepts only as scoped limitations or TODOs:

- conservation/residual: explicitly not claimed;
- runtime/deployment: TODO;
- three-dimensional/PIV: TODO;
- $Re_D=300$: stress-test failure boundary, not success.

## Scorecard

Scores are manual manual evaluator scores using the benchmark scorecard.

| Axis | No skill | With skill | Notes |
|---|---:|---:|---|
| LaTeX compilability | 3 | 3 | Both compile. |
| Physics/regime specificity | 1 | 3 | No-skill names cases but stays generic; with-skill anchors Re, vorticity, 2D regimes. |
| Claim-evidence alignment | 0 | 3 | No-skill overclaims; with-skill maps each claim to evidence/TODO. |
| Baseline fairness | 2 | 3 | Both mention bicubic/U-Net; with-skill states scope and missing U-Net details. |
| Physical diagnostics | 1 | 2 | No-skill treats diagnostics as proof; with-skill uses spectrum/PDF but marks residual gap. |
| Reproducibility/TODO discipline | 1 | 3 | No-skill omits missing solver/grid/seed details; with-skill lists them. |
| Limitation honesty | 1 | 3 | No-skill softens $Re_D=300$ failure; with-skill makes it the boundary. |
| Figure/story logic | 1 | 3 | No-skill figure captions are decorative; with-skill captions state evidence role. |
| Field-native vocabulary | 1 | 3 | No-skill marketing language; with-skill uses reconstruction/regime/diagnostic vocabulary. |
| Non-hallucination | 1 | 3 | No-skill implies unsupported deployment/generalization; with-skill avoids invented details. |

Average:

- No skill: **1.2 / 3.0**
- With skill: **2.9 / 3.0**

Benchmark internal pass threshold:

- average score >= 2.2;
- no score below 1 on claim-evidence, non-hallucination, or LaTeX compilability.

Result:

- No skill: **fail**.
- With skill: **pass**.

## Main behavioral difference

The no-skill output behaves like a plausible AI paper draft: fluent, compiled, and superficially complete, but it turns missing evidence into optimistic prose.

The skill-guided output behaves like a reviewer-defensible seed: it narrows the claim, preserves evidence boundaries, marks TODOs, and makes the $Re_D=300$ result a limitation rather than a victory lap.

## Next benchmark improvement

For a stronger deployment gate, run the same benchmark with an actual external weaker model:

1. give it only the benchmark prompt;
2. record raw output without manual cleanup;
3. compile or log compile failure;
4. score with the same rubric;
5. compare against skill-guided output.

That would turn this from an internal sanity check into a real weak-agent A/B benchmark.
