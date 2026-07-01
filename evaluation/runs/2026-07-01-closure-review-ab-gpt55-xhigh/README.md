# Closure review A/B benchmark: gpt-5.5 xhigh

Run date: 2026-07-01

Benchmark task:

- `evaluation/tasks/cfd-ai-closure-review-benchmark.md`

Topic:

- **Machine-learning turbulence closures: why a priori accuracy is not enough for RANS and LES deployment**

## Arms

| Arm | Source scope | Output |
|---|---|---|
| `no_skill` | task packet only; isolated run directory; `--ignore-rules` | `no_skill/main.tex`, `no_skill/main.pdf` |
| `with_skill` | same task plus package skills/rubrics/gold notes | `with_skill/main.tex`, `with_skill/main.pdf` |

## Compile

Both compiled with Tectonic. Logs contain layout warnings only.

```text
no_skill/main.pdf   60,609 bytes
with_skill/main.pdf 68,901 bytes
```

## Score summary

```text
no_skill average:   2.57 / 3.00
with_skill average: 3.00 / 3.00
```

## Main finding

The no-skill arm is already strong because the task prompt is well constrained. The with-skill arm still wins by making the review more audit-ready: workflow-first taxonomy, stronger a priori/a posteriori evidence ladder, stricter solver-coupled validation, better UQ/calibration/fallback logic, and clearer source-scope discipline.

See `comparison_report.md` for the full scorecard.
