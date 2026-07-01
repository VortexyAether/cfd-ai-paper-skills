# Recommended Patch

Add a wake-prediction reviewer rule:

1. If the claim says cylinder wake, wake flow, or unsteady flow prediction, require a table for Re/regime, domain/BC/IC, solver, mesh, timestep/CFL, train/test split, rollout horizon, and physical diagnostics.
2. Generic "add baselines" is invalid unless baselines are named.
3. Generalization must state unseen time, Re, geometry, BC, or regime. Random snapshots do not count.

