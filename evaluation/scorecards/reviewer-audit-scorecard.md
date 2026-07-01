# Reviewer Audit Scorecard

Use for `reviewer-audit-toolkit` benchmark outputs.

| Axis | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Gate decision | none | vague verdict | severity labels | clear submission gate with blocker count |
| Claim extraction | misses claims | obvious hype only | most major claims | all loaded claims classified by type |
| Missing evidence | generic | some details | domain-specific surfaces | exact CFD/SciML surfaces tied to claims |
| Reviewer realism | polite comments | generic reviewer | credible field reviewer | rejection-risk specific and prioritized |
| Rescue plan | none | vague fixes | concrete fixes | experiment/table/figure/rewrite per Fatal claim |
| Non-hallucination | invents details | minor unsupported assumptions | mostly scoped | all hidden facts TODO |

Pass threshold: average >= 2.5 and no hallucinated solver/data/metric/citation details.
