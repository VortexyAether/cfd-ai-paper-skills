# Weak Review to Reviewer Audit

## Input abstract

> We propose a robust physics-informed AI model for turbulent wake prediction. The model achieves state-of-the-art accuracy and generalizes to unseen flow regimes. Velocity contours show excellent agreement with CFD, and the method is fast enough for real-time design.

## Weak review

The abstract is promising but needs more details. Please add more baselines, more metrics, and explain the model better. Also clarify real-time performance.

## Reviewer-audit version

### Gate summary

| Gate | Decision | Reason |
|---|---|---|
| Submission readiness | reject-risk | Every major claim is unsupported by named evidence. |
| Fatal issues | 4 | generalization, physical consistency, state-of-the-art, real-time deployment |
| Highest-risk claim | `generalizes to unseen flow regimes` | No held-out axis or split protocol is supplied. |

### Reviewer-risk ledger

| Severity | Claim / issue | Missing evidence | Required fix | Safer wording |
|---|---|---|---|---|
| Fatal | `generalizes to unseen flow regimes` | held-out Reynolds number, geometry, BC/IC, mesh, time horizon, or forcing axis | Add a leakage-safe split table and performance by held-out axis. | `is evaluated on the stated held-out Reynolds-number cases` |
| Fatal | `state-of-the-art accuracy` | named baselines, same data, same split, same metrics, uncertainty/repeated seeds | Add same-scope classical and ML baselines. | `outperforms the named baseline on the stated metric under the stated split` |
| Fatal | `physics-informed` / physical agreement | where physics enters and physical diagnostics | State loss/constraint/evaluation role; report divergence, residuals, force/Strouhal or other QoIs. | `includes a physics residual term and is assessed with stated physical diagnostics` |
| Major | `real-time design` | hardware, latency, memory, batch size, solver-coupled workflow | Add end-to-end timing and scope of use. | `reduces inference time for the tested surrogate query on stated hardware` |

### Minimum rescue artifacts

1. Flow/numerics table: geometry, Re, BC/IC, solver, mesh, timestep/CFL, train/test regimes.
2. Validation matrix: random split vs unseen time vs unseen Re/geometry/BC/mesh.
3. Baseline table: CFD/ROM/classical interpolation or closure baseline plus ML baselines under same metric.
4. Diagnostic figure: GT/pred/error, same color scale, divergence/residual or force/frequency plot, failure case.
5. Runtime table: hardware, memory, latency, batch size, solver-coupled cost, fallback condition.

## Lesson

A reviewer audit is not “more comments.” It is a gate: claim, missing evidence, rejection risk, and the artifact that rescues the claim.
