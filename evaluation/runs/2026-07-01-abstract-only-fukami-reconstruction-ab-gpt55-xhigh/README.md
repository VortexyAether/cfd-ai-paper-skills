# Abstract-only Fukami reconstruction A/B benchmark

Run date: 2026-07-01

## Task

Given only the title and abstract of Fukami et al., *Super-resolution reconstruction of turbulent flows with machine learning*, infer what the full paper probably contains.

## Controls

| Arm | Scope | Output |
|---|---|---|
| `no_skill` | title + abstract only; temporary directory outside package; `--ignore-rules` | `no_skill_output.md` |
| `with_skill` | same title + abstract plus general skills/rubrics/style guides; exact Fukami answer-key note banned during generation | `with_skill_output.md` |

## Score summary

```text
no_skill average:   2.57 / 3.00
with_skill average: 2.79 / 3.00
```

## Main finding

This is a cleaner benchmark. The skill margin is modest, not huge, because the abstract is already detailed and the exact answer key was intentionally withheld from the skill arm. The skill output is still better at CFD-reviewer concerns: temporal leakage, physical/statistical diagnostics, 2D limitation, ablations, BC/IC/variable ambiguity, and reproducibility/source-scope discipline.

See `comparison_report.md`.
