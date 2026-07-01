# Skill Quality Rubric

Use this to score each `skills/*/SKILL.md` and decide whether a v0.3 patch should be kept.

| Axis | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Trigger specificity | Generic helper | Broad domain | Clear task trigger | Clear task trigger with exclusions |
| One-job focus | Multiple unrelated jobs | Mostly focused | Focused with small overlaps | Single job; routes adjacent work elsewhere |
| Progressive disclosure | All detail inline | Some links | Clear cockpit links | Cockpit plus exact when-to-read references/templates/rubrics |
| Output schema | Missing | Loose bullets | Structured schema | Schema supports evaluator scoring and unknown/TODO discipline |
| Anti-patterns | Missing | Generic | Domain-specific | Domain-specific and evaluator-detectable |
| Verification | Missing | Generic checklist | Domain checklist | Checklist maps to rubrics/eval tasks |
| Gold-paper alignment | Decorative names | Superficial | Uses patterns | Points to exact gold-paper files and lessons |
| Eval readiness | None | Manual only | Task/rubric linked | Baseline-agent evaluation has concrete pass/fail criteria |

## Keep/patch rule

Keep a skill change only if it improves at least one axis without lowering schema compliance or hallucination control.

