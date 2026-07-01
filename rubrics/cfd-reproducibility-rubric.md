# CFD Reproducibility Rubric

Score each axis 0-3. A paper can be scientifically interesting and still fail reproducibility.

| Axis | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Governing equations | Missing | Named only | Equations stated | Equations plus assumptions/nondimensionalization |
| Geometry/domain | Missing | Vague geometry | Domain mostly specified | Domain, coordinates, dimensions, units/scales |
| BC/IC | Missing | Partial | Mostly specified | Complete BC/IC and source/forcing details |
| Regime numbers | Missing | One number only | Main Re/Ma/Pe/etc. | All relevant nondimensional groups and ranges |
| Mesh/grid | Missing | Resolution only | Type and resolution | Mesh quality, convergence/refinement evidence |
| Time integration | Missing | Time step only | Time step/CFL | Time scheme, CFL, horizon, averaging window |
| Solver | Missing | Software only | Key settings | Version, schemes, tolerances, commands/configs |
| Data splits | Missing | Random only | Train/val/test stated | Leakage-safe split across time/Re/geometry/BC |
| ML training | Missing | Architecture only | Hyperparameters mostly stated | Seeds, runs, optimizer, schedule, normalization, code |
| Compute | Missing | Vague | Hardware or runtime | Hardware, runtime, memory, cost and reproducibility commands |

## Critical fail triggers

- Missing BC/IC for CFD-generated data.
- Random split used to support regime generalization.
- Solver or mesh convergence absent for a numerical-method claim.
- Code/data URL is placeholder or private without access note.

