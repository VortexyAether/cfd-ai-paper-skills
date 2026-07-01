---
name: related-work-synthesis
description: Use when searching, reading, organizing, and writing related work for CFD-AI/SciML papers, with emphasis on taxonomy, close-prior-art risk, and gap positioning.
version: 0.4.0
author: CFD-AI Paper Skills maintainers
metadata:
  short-description: Related-work taxonomy and gap synthesis for CFD-AI/SciML
---

# Related Work Synthesis for CFD-AI / SciML

## Trigger

Use for literature review, related work, prior-art risk, “how is my work different?”, finding journal references, and citation positioning.

## Workflow

### 1. Define axes

Identify:

- physical domain,
- task: prediction/surrogate/closure/reconstruction/control/discovery,
- ML family: PINN/operator/CNN/GNN/generative/ROM,
- data regime,
- target journal community.

### 2. Search families

Use multiple query types:

- exact method terms,
- physical-domain terms,
- competing method terms,
- review/survey terms,
- target-journal terms,
- gold-author names: Fukami, Brunton, Maulik, Lee, Vinuesa.

### 3. Extract metadata

For each paper:

- title/authors/year/venue,
- DOI/arXiv/URL,
- problem setting,
- method,
- evidence,
- limitation,
- relevance,
- how close it is.

### 4. Build taxonomy

Prefer categories:

First classify by fluid-mechanics workflow role:

- discovery/governing equations,
- modeling/surrogate/acceleration,
- sensing/reconstruction/super-resolution,
- experiments/design/digital twins,
- turbulence closure/ROM,
- graph/mesh/geometric modeling,
- uncertainty/verifiability,
- control/optimization,
- domain-specific wafer/CVD/process models.

Then classify by ML family: PINN, neural operator, CNN/U-Net, GNN, sparse identification, ROM/latent dynamics, RL, generative, or statistical surrogate.

Use progressive disclosure:

| Need | Read |
|---|---|
| Workflow taxonomy | `references/gold-papers/brunton-2020-machine-learning-fluid-mechanics.md` |
| Sparse discovery | `references/gold-papers/brunton-2016-sindy-pnas.md` |
| ML workflow staging | `references/gold-papers/brunton-2021-applying-ml-fluid-mechanics.md` |
| CFD opportunity map | `references/gold-papers/vinuesa-2022-enhancing-cfd-ml.md` |
| Experiments | `references/gold-papers/vinuesa-2023-transformative-ml-experiments-nrp.md` |

### 5. Prior-art risk

Mark papers as:

- background,
- adjacent,
- close,
- dangerous close prior art.

Dangerous close prior art requires explicit differentiation or experiment.

### 6. Gap paragraph

Use:

> Prior work primarily addresses X under Y conditions using Z. However, A remains unresolved, especially for B. The present work targets A by C and evaluates it through D.

No fake novelty. If the work is incremental, frame it honestly.

## Output template

1. Search scope
2. Taxonomy
3. Key papers
4. Dangerous close prior art
5. Gap statement
6. Draft related-work paragraphs
7. Missing citation/BibTeX TODOs

Add:

| Paper | Workflow role | ML insertion point | Prior-art risk | Source scope |
|---|---|---|---|---|

Gap paragraph must name the CFD bottleneck, closest prior role, unresolved boundary, proposed mechanism, and decisive evidence.

## Anti-patterns

- Organizing related work as a citation list instead of a taxonomy.
- Treating all ML-for-CFD papers as interchangeable.
- Overstating novelty without naming closest prior art.
- Filling missing bibliographic details from memory.
- Sorting papers only by model family without workflow role.

## Verification

- Do not cite papers not checked.
- Keep URLs/DOIs/arXiv IDs with claims.
- Mark uncertain claims.
- Separate background from close prior art.
- Every paper has source scope: full text, abstract only, metadata only, or TODO.
