# LaTeX skill A/B sample — CFD-AI/SciML package

## Status

Package validation passed from package root:

```text
ok
skills: 15
references: 25
gold_papers: 15
rubrics: 6
examples: 5
eval_tasks: 5
eval_runs: 3
trigger_tests: 6
schema_tests: 5
trigger_tests: 6
schema_tests: 5
eval_runs: 3
ok
```

LaTeX compile now passes with Tectonic 0.16.9:

```text
no_skill_baseline.pdf   29K
with_skill_cfd_ai.pdf   40K
```

`with_skill_cfd_ai.tex` has minor Underfull hbox warnings in the claim-evidence table only; no fatal errors. Static LaTeX sanity also passed:

```text
no_skill_baseline.tex: static latex sanity ok; chars=3429; sections=4; equations=2
with_skill_cfd_ai.tex: static latex sanity ok; chars=6257; sections=5; equations=3
```

## Files

- `sample_prompt.md` — shared CFD-AI sample task.
- `no_skill_baseline.tex` — generic model/no-skill style output.
- `with_skill_cfd_ai.tex` — output using the CFD-AI/SciML paper skills package principles.
- `comparison_report.md` — this report.

## A/B prompt summary

Topic: convolutional super-resolution for reconstructing high-resolution vorticity fields from downsampled 2D cylinder-wake and decaying-turbulence snapshots.

Evidence supplied:

- cylinder wake at $Re_D=100$;
- 2D homogeneous decaying turbulence;
- downsampling factors $r=4$ and $r=8$;
- baselines: bicubic interpolation and small U-Net;
- metrics: relative $L_2$ error, vorticity spectrum error, vorticity-PDF agreement;
- scoped result: 22% lower relative $L_2$ error than bicubic at $r=4$;
- known limits: unseen $Re_D=300$, sharp shear-layer extrema, no runtime/conservation/3D/PIV evidence.

## Observed difference

### No-skill baseline

Typical generic AI-paper behavior:

- uses broad title: “A Deep Learning Framework for Accurate CFD Super-Resolution”;
- says “novel”, “robust”, “efficient”, “physically consistent”, “real-time” without required evidence;
- treats visual reconstruction as enough for physical validity;
- claims generality across flow regimes despite only scoped 2D cases;
- does not mark missing runtime, conservation residual, 3D, or PIV tests as TODO;
- contribution bullets are method-marketing rather than reviewer-defensible claims.

### Skill-guided version

CFD-AI/SciML package behavior:

- starts from the physical/numerical bottleneck: high-resolution flow-field data unavailable at inference;
- names regimes, variables, and task: vorticity super-resolution for 2D cylinder wake and 2D decaying turbulence;
- keeps ML role scoped to reconstruction, not “CFD replacement”;
- includes baselines and metrics before claims;
- separates pointwise error from physical diagnostics;
- explicitly downgrades unsupported claims:
  - broad generalization: not supported;
  - physical consistency: TODO until residual/conservation audit exists;
  - efficiency/real-time: TODO until runtime/hardware exists;
- adds a claim-evidence table inside the LaTeX document.

## Deployment readiness judgement

**Research-package quality:** close to deployable as an internal skill package.

Evidence:

- package validators pass;
- static evals pass;
- package contains focused skills, gold-paper references, rubrics, examples, templates, and evaluation runs;
- A/B sample shows the intended behavioral gap: the skill reduces overclaiming and produces field-native, reviewer-safer LaTeX.

Remaining blockers before public-ish distribution:

1. Install or provide a LaTeX engine and compile both sample PDFs.
2. Add this A/B sample run to the package README or `evaluation/runs/README.md`.
3. Optional: run an actual external weaker model against `sample_prompt.md` instead of manual A/B samples.
4. Optional: package export script if the goal is sharing outside the local workspace.

## Evaluation verdict

Deployable for internal evaluation use: **yes**.

Public distribution: **not yet**. Needs PDF compile evidence and at least one real weak-model A/B run. Otherwise it smells like “trust me bro, but with YAML.”
