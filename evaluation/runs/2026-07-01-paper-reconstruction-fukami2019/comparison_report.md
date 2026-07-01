# Paper reconstruction from dense summary — Fukami 2019 A/B

Run root:

`evaluation/runs/2026-07-01-paper-reconstruction-fukami2019/`

## Task

Original target paper:

Fukami, Fukagata, and Taira, *Super-resolution reconstruction of turbulent flows with machine learning*, Journal of Fluid Mechanics, 2019.

Protocol:

1. Compress the original paper note into `source_summary_dense.md`.
2. Ask for a LaTeX manuscript seed reconstructed only from that summary.
3. Compare generic/no-skill behavior with skill-guided behavior.

## Compile result

Both outputs compile with Tectonic:

```text
no_skill/main.pdf    35K
with_skill/main.pdf  43K
```

## Qualitative result

### no-skill

The no-skill output is fluent and paper-like, but it fills summary gaps with claims that were not supplied:

- says the model is `robust`;
- says it is `generalizable`;
- invokes `real-time` reconstruction / CFD acceleration;
- says it `outperforms` interpolation without keeping exact values as TODO;
- treats spectral recovery as established rather than PDF-level TODO;
- gives a normal citation instead of TODO-verified bibliography.

This is the expected failure mode: it reconstructs a plausible paper, not a source-bounded one.

### with-skill

The skill-guided output is less flashy and more defensible:

- states the source scope;
- preserves the allowed claim: low-resolution to high-resolution flow-field reconstruction;
- keeps missing numerical values, solver settings, split seeds, architecture details, and figure captions as TODO;
- distinguishes cylinder wake `Re_D=100` and 2D homogeneous decaying turbulence;
- includes claim-evidence and reviewer-risk tables;
- uses figure placeholders with explicit claim boundaries;
- avoids claiming 3D generalization, real-time deployment, solver acceleration, or universal turbulence recovery.

Risky terms appear mostly inside explicit blocked-claim contexts, not as paper claims.

## Files

- `source_summary_dense.md`
- `prompt.md`
- `no_skill/main.tex`
- `no_skill/main.pdf`
- `with_skill/main.tex`
- `with_skill/main.pdf`

## Verdict

This benchmark is better than the earlier hand-designed evidence-packet tasks because it tests whether the agent can reconstruct a paper without inventing missing paper details. The gap is visible: no-skill writes a plausible manuscript; with-skill writes a source-bounded reconstruction.
