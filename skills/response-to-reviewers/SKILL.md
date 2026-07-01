---
name: response-to-reviewers
description: Use when preparing point-by-point responses and manuscript revision plans for CFD-AI/SciML journal reviews.
version: 0.3.0
author: VA + TARS
metadata:
  short-description: Response-letter strategy for CFD-AI/SciML revisions
---

# Response to Reviewers

## Trigger

Use when handling reviewer comments, editor decisions, major/minor revisions, rebuttals, or response letters.

## Core rule

Be polite, concrete, and evidence-based. Do not argue emotionally. Annoying, yes. Effective, also yes.

## Workflow

### 1. Parse comments

For each comment identify:

- type: clarity / experiment / method / citation / formatting / disagreement,
- severity,
- requested action,
- manuscript location affected.

### 2. Decide response strategy

Options:

- agree + changed,
- agree + added experiment,
- partially agree + clarify scope,
- respectfully disagree + evidence,
- cannot do + limitation/future work.

### 3. Map to manuscript edits

Every substantive response should cite:

- section,
- page/line if available,
- figure/table/equation,
- added text or experiment.

### 4. CFD-AI specific reviewer demands

Common demands:

- add baseline,
- add unseen Re/geometry tests,
- add solver/grid/CFL details,
- add conservation/physics residual,
- add ablation,
- clarify data split,
- tone down claims.

### 5. Tone template

Use:

> We thank the reviewer for this constructive comment. We agree that [issue] requires clarification. We have revised Section X to [change]. Specifically, we now [evidence/edit]. The revised manuscript states: “...”.

For disagreement:

> We appreciate the reviewer’s concern. While we agree that [general concern] is important, in the present study [scope/evidence]. To avoid overstatement, we have revised the claim in Section X from A to B.

## Output template

1. Reviewer-comment table
2. Response strategy per comment
3. Required manuscript edits
4. New experiments/figures needed
5. Draft response letter
6. Risky comments needing advisor decision

## Anti-patterns

- Thanking the reviewer without a concrete manuscript change.
- Arguing tone before addressing the technical evidence gap.
- Promising new experiments that are not in the revised manuscript.
- Failing to quote or locate changed manuscript text.

## Verification

- Every reviewer point is answered.
- Tone is polite.
- Changes are traceable to manuscript sections.
- Claims are weakened when evidence is insufficient.
