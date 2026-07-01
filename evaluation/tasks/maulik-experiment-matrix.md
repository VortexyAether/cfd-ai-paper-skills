# Task: Maulik experiment matrix

## Skill under test

- `experiment-design-for-sciml`
- `cfd-ml-paper-reviewer`

## Gold reference

- `references/gold-papers/maulik-2020-probabilistic-neural-networks-prf.md`
- Additional Maulik-related closure/verifiable-SciML papers may be used only if source-scoped and marked.

## Dumb-agent prompt

A paper claims a data-driven turbulence closure is generalizable and trustworthy. Design the minimum experiment matrix needed for journal review.

## Expected answer-key patterns

- Baselines: classical closure/ROM and relevant ML closure models.
- Tests on unseen conditions and possibly unstructured grids if claimed.
- Physical diagnostics, not only regression error.
- Uncertainty or error bounds if “trustworthy/verifiable” is claimed.
- Differentiable physics / closure consistency if relevant.
