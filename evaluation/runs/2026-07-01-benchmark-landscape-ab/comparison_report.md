# Benchmark landscape A/B run

Run root:

`evaluation/runs/2026-07-01-benchmark-landscape-ab/`

Benchmark task:

`evaluation/tasks/cfd-ai-benchmark-landscape-review.md`

## Setup

Controlled A/B sample for the v0.6.1 benchmark-landscape review task.

- `no_skill/`: generic baseline behavior from the task prompt only.
- `with_skill/`: skill-guided behavior using the root `SKILL.md` router and CFD-AI benchmark landscape discipline.

## Compile

Both files compile with Tectonic:

```text
no_skill/main.pdf    30K
with_skill/main.pdf  40K
```

## Deterministic evaluator

```text
no_skill:   6/11 checks passed
with_skill: 11/11 checks passed
```

Risky phrase discipline:

```text
no_skill:   fail — 12 risky hits, 11 unbounded
with_skill: pass — 1 risky hit, 0 unbounded
```

## Main difference

The no-skill sample turns the topic into a resource overview and makes unsupported claims about robustness, generalization, real-time deployment, state-of-the-art methods, broad CFD coverage, and physically consistent models.

The skill-guided sample separates datasets, tools, benchmark suites, curated lists, and review claims. It forces validation axes apart: time, regime, geometry, mesh, BC/IC, cross-solver/fidelity, coupled-solver deployment, physical diagnostics, reproducibility, and license/data logistics. Missing facts stay as TODO.

## Files

- `prompt.md`
- `no_skill/main.tex`
- `no_skill/main.pdf`
- `with_skill/main.tex`
- `with_skill/main.pdf`
- `evaluator-no-skill.md`
- `evaluator-with-skill.md`
