# Multi-Agent Paper Workflow Scorecard

Use for `multi-agent-paper-orchestrator` benchmark outputs.

| Axis | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Role separation | one voice | labels only | distinct outputs | role-scoped artifacts with forbidden actions |
| Source scope | invented facts | vague | mostly TODO | explicit supplied/allowed/forbidden scope |
| Reviewer severity | none | generic | Fatal/Major | Fatal/Major tied to claims and fixes |
| Evidence audit | none | obvious claims | claim map | claim type + evidence + TODO + safe status |
| Experiment rescue | none | vague | concrete tests | tests/baselines/metrics per risky claim |
| Figure/table rescue | none | generic figures | evidence figures | each figure/table supports a claim |
| Editorial rewrite | none | polish | safer rewrite | field-native, evidence-bounded rewrite |
| Edit-review loop | none/unbounded | named only | residual-driven second pass | bounded cycles with explicit stop reason |
| Gatekeeper | none | approves | before/after | residual blockers, new-overclaim check, continue/stop decision |
| Non-hallucination | invents details | assumptions | mostly scoped | all hidden details TODO |

Pass threshold: average >= 2.5 and no invented scientific details.
