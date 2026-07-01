# Evaluation runs

Run artifacts live under `evaluation/runs/`. Do not delete prior runs; new hardening evidence should add files beside the run it evaluates.

## Run Index

| Run | Type | Task | Result | Interpretation |
|---|---|---|---|---|
| `2026-06-30-v04-fukami-super-resolution-reconstruction/` | simulated baseline-agent | Fukami SR reconstruction | benchmark-backed patch recommended | v0.4 gold-paper reconstruction sanity run. |
| `2026-06-30-v04-lee-cylinder-wake-reviewer-attack/` | simulated baseline-agent | Lee wake reviewer attack | benchmark-backed patch recommended | v0.4 reviewer-defense sanity run. |
| `2026-06-30-v04-brunton-taxonomy-reconstruction/` | simulated baseline-agent | Brunton taxonomy reconstruction | benchmark-backed patch recommended | v0.4 related-work taxonomy sanity run. |
| `2026-07-01-full-manuscript-ab/` | controlled internal A/B | full manuscript LaTeX seed | no-skill fail 1.2/3.0; with-skill pass 2.9/3.0 | Skill guidance improves claim-evidence discipline and limitation honesty. |
| `2026-07-01-trend-review-ab/` | controlled internal A/B | trend review LaTeX seed | no-skill fail 1.1/3.0; with-skill pass 3.0/3.0 | Strongest current deployment gate; separates taxonomy/validation discipline from fluent generic review prose. |
| `2026-07-01-latex-skill-ab-sample/` | LaTeX sample A/B | sample LaTeX production | comparison report present | Earlier LaTeX production sanity artifact. |

## Standard Run Shape

Save each classic baseline-agent run as:

```text
evaluation/runs/YYYY-MM-DD_task-name/
├── prompt.md
├── skill-version.md
├── baseline-output.md
├── evaluator-scorecard.md
├── evaluator-decision.md
└── patched-skill-diff.md
```

For simulated baseline-agent runs, `recommended-patch.md` is acceptable instead of `patched-skill-diff.md` when no external model or A/B variant was actually executed.

Do not count a run as improvement unless score increases or hallucination decreases.

## Deterministic Evaluator Reports

For manuscript A/B runs, add deterministic surface reports beside each variant:

```text
evaluation/runs/YYYY-MM-DD-*-ab/
├── no_skill/main.tex
├── with_skill/main.tex
├── evaluator-no-skill.md
└── evaluator-with-skill.md
```

These reports are conservative structure/risk scans. They do not replace manual rubric scoring.
