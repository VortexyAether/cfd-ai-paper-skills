# Reviewer-Editor Loop Rubric

Use this rubric when evaluating a workflow that first audits a CFD-AI/SciML draft as a reviewer, then rewrites it as an editor, then re-audits the rewritten text.

Score each axis 0--3.

| Score | Meaning |
|---:|---|
| 0 | Missing, unsafe, or misleading. |
| 1 | Generic improvement; little domain specificity. |
| 2 | Useful but incomplete; some claims or fixes remain weak. |
| 3 | Reviewer-grade and editor-grade; evidence-bounded, readable, and re-audited. |

## Axes

### 1. Reviewer gate quality

- 0: no gate decision.
- 1: vague “needs work.”
- 2: Fatal/Major issues identified.
- 3: Fatal/Major issues tied to exact claims, missing evidence, and minimum rescue artifacts.

### 2. Evidence preservation

- 0: editor invents facts to improve prose.
- 1: some unsupported assumptions remain.
- 2: most missing facts are marked TODO.
- 3: rewrite uses only supplied evidence and converts missing facts into scoped claims or TODOs.

### 3. Claim calibration

- 0: loaded claims remain.
- 1: loaded claims are softened but still broad.
- 2: claims are mostly bounded to evidence.
- 3: each claim names task, regime, evidence type, and limitation boundary.

### 4. Field-native manuscript texture

- 0: generic AI-for-science prose.
- 1: field terms appear but order is generic.
- 2: mostly physical problem -> gap -> method -> evidence -> limitation.
- 3: normal CFD-AI/SciML paper texture with physical object, variables, diagnostics, and restrained implication.

### 5. Reviewer-to-editor traceability

- 0: rewrite does not address audit.
- 1: rewrite addresses issues implicitly.
- 2: most Fatal/Major issues map to edits.
- 3: every Fatal/Major issue has an edit, TODO, experiment/table/figure, or claim removal.

### 6. Re-audit discipline

- 0: no re-audit.
- 1: re-audit only says “better.”
- 2: before/after risk is compared.
- 3: final residual risks and remaining TODOs are explicitly listed.

### 7. Actionability

- 0: no next steps.
- 1: vague “add validation.”
- 2: concrete experiments/tables/figures listed.
- 3: next actions are prioritized by what rescues each remaining claim.

## Pass gate

A reviewer-editor loop passes only if:

- no hidden solver/data/metric/citation details are invented;
- broad terms such as `robust`, `generalizable`, `state-of-the-art`, `real-time`, `physically consistent`, and `solver replacement` are removed, bounded, or tied to explicit evidence;
- the edited text is more readable **and** lower reviewer risk;
- the final re-audit explains what still cannot be claimed.
