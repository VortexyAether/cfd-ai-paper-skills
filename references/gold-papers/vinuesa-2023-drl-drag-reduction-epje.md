---
title: Vinuesa 2023 DRL drag reduction EPJ E deep analysis
created: 2026-06-30
updated: 2026-06-30
status: v0.4-arxiv-abstract-grounded
source_scope: arXiv metadata/abstract and DOI metadata; full PDF not read in this pass
---

# Vinuesa 2023: Deep reinforcement learning for turbulent drag reduction in channel flows

## Metadata

| Field | Value |
|---|---|
| Title | Deep reinforcement learning for turbulent drag reduction in channel flows |
| Authors | L. Guastoni, J. Rabault, P. Schlatter, H. Azizpour, Ricardo Vinuesa |
| Year / venue | 2023, European Physical Journal E |
| DOI / arXiv / URL | DOI: https://doi.org/10.1140/epje/s10189-023-00285-8; arXiv: https://arxiv.org/abs/2301.09889 |
| Role | Vinuesa senior/last author; corresponding-author status unknown/TODO |

## Source Scope

ArXiv metadata/abstract plus DOI metadata. Full environment, reward, and numerical details are TODO.

## Why Answer Key

This paper is an answer key for ML control papers because it benchmarks DRL against a classical turbulence-control strategy in a high-fidelity channel-flow environment. It names the action, observation configurability, friction Reynolds number, and drag-reduction comparison.

## Abstract Grammar

| Move | Pattern |
|---|---|
| Context | Turbulent channel-flow drag reduction is a long-standing control problem. |
| Gap | Existing physically grounded strategies can be too simple for high-dimensional nonlinear flows. |
| Method | RL environment with wall blowing/suction and configurable observations; DDPG agent. |
| Evidence | Minimal and larger channel at Re_tau = 180; comparison with opposition control. |
| Implication | DRL can outperform opposition control in the tested benchmark environment. |

## Introduction Move Structure

1. Establish drag reduction as a physically important turbulent-flow control task.
2. Explain why benchmark environments matter for data-driven control.
3. Define action/observation space and high-fidelity simulator.
4. Compare against a known classical controller.
5. Report scoped drag-reduction results.

## Method/Reproducibility Checklist

| Item | Status |
|---|---|
| Flow | Confirmed: turbulent channel flow. |
| Regime | Confirmed: Re_tau = 180. |
| Control action | Confirmed: wall blowing/suction. |
| Observations | Confirmed: configurable velocity/pressure variables and locations. |
| Algorithm | Confirmed: DDPG as commonly used DRL algorithm. |
| Baseline | Confirmed: opposition control. |
| Drag reduction | Confirmed from abstract: 43 percent and 46 percent, about 20 percentage points over opposition control. |
| Solver/environment implementation | TODO. |
| Reward, training budget, seeds | TODO. |

## Experiment/Evidence Stack

1. RL environment definition.
2. Channel-flow numerical setup.
3. Action/observation/reward specification.
4. Classical opposition-control baseline.
5. DRL performance in minimal and larger channels.
6. Physical interpretation of control behavior and limitations.

## Figure Grammar With Confidence Labels

| Figure role | Confidence |
|---|---|
| RL/control environment schematic | likely |
| Channel-flow setup and wall actuation | likely |
| Drag-reduction time histories/statistics | confirmed by abstract but exact panels TODO |
| Opposition control vs DDPG comparison | confirmed by abstract but exact panels TODO |
| Observation/action sensitivity | likely/TODO |
| Flow-field/control interpretation | TODO |

## Reviewer-Defense Patterns

- Uses a classical control baseline, not only uncontrolled flow.
- Reports two channel sizes to avoid a single narrow environment claim.
- Names the state/action interface.
- Keeps the benchmark/environment contribution visible.

## Skill Lessons

- `cfd-ml-paper-reviewer` should require closed-loop baselines and reward/action details for control papers.
- `sciml-experiment-auditor` should require training seeds, stability, and physical constraints for RL.
- `cfd-reproducibility-checker` should request environment code, simulator settings, and observation definitions.

## Eval Task Derived From Paper

Ask a dumb reviewer to audit a DRL drag-reduction claim. It must ask for closed-loop baseline, reward, action limits, observation variables, simulator fidelity, seeds, and physical side effects.

## Unknowns/TODOs

- Full PDF extraction for solver, reward, hyperparameters, seeds, and code availability.
- Corresponding-author status.

