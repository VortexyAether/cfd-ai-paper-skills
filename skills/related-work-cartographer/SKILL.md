---
name: related-work-cartographer
description: Use when mapping CFD-AI/SciML related work into a taxonomy, identifying nearest prior art, and writing gap/positioning paragraphs without citation dumping.
version: 0.4.0
author: VA + TARS
metadata:
  short-description: Related-work map and prior-art risk audit
---

# Related Work Cartographer

## Trigger

Use for related-work structure, prior-art risk, journal positioning, and “how is this different?” questions.

## Workflow

1. Extract contribution claims.
2. Define comparison axes: physics fidelity, geometry generalization, temporal extrapolation, resolution transfer, data efficiency, conservation, runtime, uncertainty.
3. Build a Brunton-style workflow taxonomy before model-family taxonomy.
4. Classify literature: background / adjacent / close / dangerous close.
5. Draft gap paragraph.

## Progressive disclosure

Read only the relevant gold notes:

| Need | Read |
|---|---|
| Field/workflow taxonomy | `references/gold-papers/brunton-2020-machine-learning-fluid-mechanics.md` |
| Sparse discovery / interpretable dynamics | `references/gold-papers/brunton-2016-sindy-pnas.md` |
| ML workflow staging | `references/gold-papers/brunton-2021-applying-ml-fluid-mechanics.md` |
| CFD opportunity map | `references/gold-papers/vinuesa-2022-enhancing-cfd-ml.md` |
| Experiments | `references/gold-papers/vinuesa-2023-transformative-ml-experiments-nrp.md` |

## Output schema

| Category | Key papers | What they solve | Limitation | Relation to this work |
|---|---|---|---|---|

Then add:

| Paper | Workflow role | ML insertion point | Prior-art risk | Source scope |
|---|---|---|---|---|

Workflow roles: discovery, modeling, sensing/reconstruction, experiments, closure, ROM, control, optimization, acceleration, UQ.

ML insertion points: problem formulation, data curation, architecture, loss, optimization, deployment/control.

## Gap paragraph template

Prior work primarily addresses X under Y conditions using Z. However, A remains unresolved, especially for B. The present work targets A by C and evaluates it through D.

The paragraph must name the CFD bottleneck, closest prior role, unresolved boundary, proposed mechanism, and decisive evidence. "Our method improves accuracy and efficiency" is not a gap.

## Anti-patterns

- Chronological citation dump with no taxonomy.
- Claiming novelty because no identical title was found.
- Ignoring adjacent CFD, ROM, closure, PINN, operator, or control literatures.
- Inventing citation details or DOI values.
- Method-list taxonomies that never say where the method enters the fluid-mechanics workflow.

## Verification

- No paper cited without source check.
- Preprint vs peer-reviewed status marked when relevant.
- Dangerous close prior art is not hidden.
- Every cited paper has a source scope: full text, abstract only, metadata only, or TODO.
