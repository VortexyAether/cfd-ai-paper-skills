# Gold-Paper Reconstruction Task Template

## Skill under test

- `[skill-name]`

## Gold reference

- Paper file: `references/gold-papers/[paper].md`
- Source scope allowed to dumb agent: title + abstract / gold note / full paper

## Dumb-agent prompt

Given only the allowed source scope, reconstruct:

1. physical problem and CFD regime,
2. gap and contribution,
3. method role and reproducibility details,
4. experiment/evidence stack,
5. likely figure sequence,
6. reviewer attack points,
7. unknowns/TODOs that must not be invented.

Return the assigned skill schema.

## Evaluator instructions

Read:

- the matching `references/gold-papers/*.md`,
- `rubrics/claim-evidence-rubric.md`,
- `rubrics/sciml-experiment-rubric.md`,
- `rubrics/figure-evidence-rubric.md`,
- `rubrics/skill-quality-rubric.md` if evaluating skill quality.

## Expected scoring table

| Axis | Score 0-3 | Evidence | Fix |
|---|---:|---|---|
| Gold-paper alignment |  |  |  |
| Physics specificity |  |  |  |
| Experiment stack |  |  |  |
| Figure grammar |  |  |  |
| Reviewer-defense realism |  |  |  |
| Unknown/TODO discipline |  |  |  |
| Output schema compliance |  |  |  |

