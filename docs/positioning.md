# Positioning

## Audience

This package is for researchers, reviewers, and agent builders working on CFD-AI / SciML papers. It is especially useful when a manuscript involves numerical evidence that can be overstated by generic AI-writing assistance.

## What Makes It Different

| Compared with | Difference |
|---|---|
| Generic academic writing prompts | This package checks CFD/SciML evidence, splits, diagnostics, solver details, and reviewer traps. |
| General AI paper-writing skills | This package specializes in CFD-AI claims: mesh, regime, BC/IC, solver coupling, turbulence closure, reconstruction, and physical diagnostics. |
| CFD-AI resource lists | This package uses resource lists for source scope and taxonomy, but focuses on producing auditable writing/review artifacts. |
| LaTeX templates | This package can produce LaTeX, but its main value is deciding what claims, tables, figures, and TODOs belong in the paper. |

## Core Promise

The package should make an agent more conservative, more domain-aware, and more useful in CFD-AI writing. It should not merely make prose smoother.

## Intended Outputs

- claim-evidence maps;
- reviewer-risk reports;
- CFD reproducibility checklists;
- SciML experiment matrices;
- related-work taxonomies;
- figure/story plans;
- LaTeX manuscript seeds;
- response-to-reviewer tables;
- benchmark review prompts.

## Related Project Positioning

General research-writing skill repositories show useful patterns: evidence-backed paper workflows, modular references, prompt routing, citation checks, and build readiness. This package adopts those patterns where they fit.

CFD-AI resource repositories provide useful landscape coverage across turbulence closure, flow approximation, PIV/reconstruction, aero coefficients, flow control, multiphase flows, datasets, tools, and open-source codes. This package uses that coverage to harden benchmark prompts and review checklists.

The package should not copy upstream content. It should summarize, attribute source scope, and convert patterns into CFD-AI-specific tasks.

## What This Package Should Not Claim

- It should not claim to verify scientific truth without evidence.
- It should not claim broad CFD coverage from a single benchmark.
- It should not claim official support for any agent platform.
- It should not invent installation commands.
- It should not invent paper facts, DOI values, author roles, solver settings, benchmark numbers, or dataset licenses.

## Maintenance Direction

Public docs should stay user-centered: installation pattern, skill usage, workflows, examples, limitations, and positioning.

Internal references and evaluation files should carry the development logic: source scope, related-project distillation, benchmark hardening, evaluator limits, and package-quality checks.
