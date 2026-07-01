# CFD-AI benchmark landscape

Source scope: distilled from the related repository/source scope in internal source-scope notes, existing package gold-paper notes, and browser-inspected public pages for PDEBench, DeepXDE, DrivAerNet, and The Well. This is an internal benchmark-design reference, not a complete survey.

## Why this landscape matters

CFD-AI papers fail review when they validate only the easiest axis. A surrogate can look strong on random snapshot splits and still fail under held-out geometry, Reynolds number, mesh, boundary condition, long rollout, or coupled-solver deployment. Benchmark prompts should therefore force the agent to ask: what is the workflow role, what is the validation axis, what failure mode is being tested, and what evidence is reproducible?

## Landscape map

| Area | Typical task | Required validation axis | Common failure mode | Reproducibility minimum |
|---|---|---|---|---|
| Data-driven surrogates | Learn state-to-state, parameter-to-field, or geometry-to-QoI maps from simulation data. | Held-out time, parameters, geometry, mesh, and QoIs. | Random snapshot split overstates generalization. | Dataset provenance, solver, grid, train/test split, metrics, runtime/hardware. |
| Physics-informed surrogates | Add PDE residuals, boundary penalties, conservation-inspired losses, or neural-operator constraints. | Residual plus physical diagnostics and boundary-condition transfer. | Equating residual loss with physical consistency. | PDE form, nondimensionalization, residual weighting, BC/IC treatment, optimization settings. |
| ML-assisted numerical solutions | Replace or accelerate solver stages, ROM components, initialization, closure terms, or design-loop screening. | Coupled-solver stability, cost accounting, and failure detection. | Offline accuracy does not survive solver coupling. | Coupling interface, CFL/time step, solver tolerances, wall-clock breakdown, fallback policy. |
| Turbulence closure | Learn RANS/LES closure terms, SGS stresses, discrepancy fields, or uncertainty regions. | A priori diagnostics plus a posteriori coupled runs. | Good term fit worsens mean flow after solver feedback. | Invariance treatment, training flows, target definition, solver integration, UQ/calibration. |
| PIV/reconstruction | Reconstruct velocity/pressure/vorticity from sparse/noisy measurements or images. | Noise, seeding density, sensor sparsity, temporal transfer, spectra. | Visual field match hides spectral or derivative errors. | Measurement model, noise level, train/test regimes, derivative/QoI diagnostics. |
| Lift/drag/aero design | Predict coefficients, surface pressure, wake fields, or design sensitivities. | Held-out geometry families and validation against high-fidelity CFD or experiment. | Geometry leakage through near-duplicate shapes. | Geometry parameterization, mesh policy, turbulence model, force integration, split by design. |
| Flow control | Learn policies, controllers, reduced models, or optimization loops. | Closed-loop stability, actuator limits, delay/noise, energy budget. | Offline reward or open-loop metric does not transfer. | Plant model, action limits, observation set, seeds, episode protocol, baseline controller. |
| Multiphase/reacting/non-Newtonian | Model interfaces, closures, reduced dynamics, or surrogate PDE solves. | Regime transfer, conservation, interface metrics, stiffness. | Smooth field errors miss topology/interface failures. | Phase variables, closure assumptions, solver details, stiffness handling, conservation checks. |

## Dataset/tool anchors

| Resource | Source-supported role | Use in benchmark prompts | Caution |
|---|---|---|---|
| PDEBench | Scientific-ML benchmark with multiple PDE datasets, forward/inverse tasks, generated datasets, and baselines such as FNO, U-Net, and PINN. | Good anchor for benchmark-landscape classification, split design, and model-family comparison. | It is broader than CFD; do not imply every task is industrial CFD validation. |
| DeepXDE | PINN/scientific-ML library supporting multiple backends and complex geometries. | Good anchor for physics-informed surrogate tooling and PINN workflow examples. | A library feature is not validation evidence. |
| DrivAerNet / DrivAerNet++ | Automotive aerodynamic dataset family with CFD simulations, geometry/mesh data, coefficients, and ML benchmark use cases. | Good anchor for lift/drag, geometry-conditioned surrogates, and engineering split design. | Check license and exact dataset version before public claims or commercial workflow use. |
| The Well | Large physics-simulation dataset collection with benchmark infrastructure and fluid/astrophysical entries. | Good anchor for large-scale spatiotemporal benchmark design and data logistics. | Not all datasets are CFD; classify domain and governing physics explicitly. |
| Curated ML-fluid repositories | Broad inventory of reviews, papers, datasets, codes, and application areas. | Good for coverage checks and prompt seeds. | They are lists, not proof of benchmark quality or current consensus. |

## Validation axes that should be forced apart

No-skill outputs often compress these into "generalization" or "accuracy". Benchmark prompts should require separate rows because each axis supports a different claim.

| Axis | Claim it can support | Evidence needed | Common overclaim to block |
|---|---|---|---|
| Held-out time / rollout horizon | Temporal interpolation or bounded extrapolation for the same regime. | Rollout protocol, teacher-forcing policy, drift metrics, stability/failure horizon. | "Stable long-term prediction" from one-step loss. |
| Held-out Reynolds/Mach/parameter regime | Regime transfer within the stated nondimensional range. | Train/test parameter ranges, nondimensional groups, regime labels, failure cases. | "Generalizable surrogate" from random parameter mixing. |
| Held-out geometry family/topology | Design-space transfer or geometry-conditioned prediction. | Split by design family/topology, geometry parameterization, leakage check, force/field diagnostics. | "Works for new geometries" from near-duplicate shapes. |
| Mesh/resolution transfer | Discretization robustness or operator-like behavior. | Mesh policy, resolution ladder, interpolation/projection method, conservation/QoI drift. | "Mesh independent" from same-grid testing. |
| Boundary/initial-condition transfer | Scenario transfer under changed forcing or inflow/outflow conditions. | BC/IC definitions, training coverage, boundary residuals, QoI sensitivity. | "Physics-aware" from residual terms alone. |
| Cross-solver or cross-fidelity transfer | Portability beyond one numerical setup. | Solver/fidelity definitions, calibration differences, domain mismatch, uncertainty bounds. | "Deployable" from one solver's offline data. |
| Coupled-solver deployment | Closed-loop numerical usefulness. | Coupling interface, residual behavior, CFL/time step, fallback policy, wall-clock accounting. | "Real-time CFD acceleration" from neural inference timing only. |
| Physical diagnostic agreement | Field error supports the intended physics/QoI claim. | Spectra, conservation, forces, pressure, stresses, vorticity, dissipation, uncertainty calibration. | "Physically consistent" from low MSE or visual agreement. |
| Data/license/logistics | Reproducible benchmark reuse. | Source, version, license, preprocessing, storage format, seeds, hardware/runtime. | "Open benchmark" without verified reuse conditions. |

## Prompt requirements for future hard benchmarks

Every new CFD-AI benchmark task should ask for:

- workflow role: surrogate, closure, solver acceleration, reconstruction, control, design, or review/taxonomy;
- validation axis: regime, geometry, mesh, BC/IC, parameter, time horizon, QoI, diagnostic, UQ, reproducibility;
- split design: random snapshot, held-out time, held-out parameter, held-out geometry, held-out mesh, or cross-solver;
- failure mode: leakage, solver-coupling instability, spectral drift, conservation violation, force/QoI mismatch, uncertainty miscalibration, or unreproducible setup;
- evidence table: what claim is allowed, what evidence is supplied, what remains TODO;
- reviewer traps: unsupported "state-of-the-art", "real-time", "generalizable", "physically consistent", "solves turbulence", or "deployable".
- source-boundary table: what is a dataset, a tool, a benchmark suite, a curated list, or a review claim, and what each one can and cannot prove.

## Unknowns/TODO

- This file does not verify individual benchmark leaderboards.
- Exact dataset sizes, licenses, and citation metadata must be checked against the current upstream source before public claims.
- Add future source notes for FD-Bench or other emerging CFD-specific benchmark suites only after direct source inspection.
