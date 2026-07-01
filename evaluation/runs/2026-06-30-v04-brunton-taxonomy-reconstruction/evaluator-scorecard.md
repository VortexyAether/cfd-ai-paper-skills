# Evaluator Scorecard

## Verdict

fail

## Rubric table

| Axis | Score 0-3 | Evidence | Fix |
|---|---:|---|---|
| Taxonomy quality | 1 | Categories are method labels, not workflow roles. | Use workflow roles: discovery, modeling, sensing/reconstruction, control, optimization, simulation acceleration, experiments. |
| Gold-paper alignment | 1 | Brunton 2021 five-stage workflow and SINDy discovery pattern missing. | Skill should route to Brunton 2016/2021 notes. |
| Prior-art risk | 1 | No close/dangerous-close classification. | Require background/adjacent/close/dangerous-close. |
| Gap paragraph | 0 | Generic "improves accuracy and efficiency." | Require bottleneck, unresolved condition, mechanism, evidence. |
| Non-hallucination | 2 | Does not invent exact citations but says "many papers." | Require TODO instead of vague placeholders. |
| Output schema | 2 | Table exists. | Add source-scope and role columns. |
| Actionability | 1 | Cannot guide manuscript edits. | Require exact positioning axes. |

Average: 1.14

## Blocking failures

- Method-list taxonomy instead of workflow taxonomy.
- Generic gap paragraph.
- No source-scoped citation discipline.

