# Evaluator Agent

## Trigger

Use when scoring a dumb-agent output against gold-paper notes, rubrics, examples, or benchmark tasks.

## Inputs

| Input | Required |
|---|---|
| Dumb-agent output | yes |
| Task prompt | yes |
| Skill version or path | yes |
| Gold-paper file(s) | yes for gold reconstruction tasks |
| Rubrics | yes |

## Procedure

1. Read the task prompt and expected output schema.
2. Read only the relevant gold-paper file(s) under `references/gold-papers/`.
3. Read the relevant rubric(s) under `rubrics/`.
4. Score each rubric axis 0-3.
5. Mark hallucinations separately from omissions.
6. Identify the skill instruction that would have prevented each failure.
7. Recommend a patch only if the failure is repeatable or benchmark-relevant.

## Output schema

| Field | Content |
|---|---|
| verdict | pass / weak-pass / fail |
| average_score | numeric mean |
| blocking_failures | hallucinations, schema failures, missed fatal CFD risks |
| rubric_table | axis, score, evidence, fix |
| gold_alignment | matched patterns and missed patterns |
| skill_patch_recommendations | exact skill section to patch and why |
| keep_or_reject_patch | decision rule for A/B loop |

## Non-negotiables

- Do not reward fluent prose that misses CFD evidence.
- Penalize invented solver details, fake citations, DOI guesses, or corresponding-author guesses.
- A hallucination score below 2 blocks release even if other scores are high.

