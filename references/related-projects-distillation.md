# Related projects distillation

Source scope: inspected browser-accessible README/key pages listed in internal source-scope notes. Shell raw fetch and shallow clone were blocked by DNS resolution for `raw.githubusercontent.com`; no upstream code was vendored. `Zejun-W/AI-Research-Writing-Skills-Hub` could not be verified cleanly in this environment, so it is listed only as `unknown/TODO`.

## Comparison

| Project | What it contributes | What not to import | Pattern to adopt |
|---|---|---|---|
| `jin-s13/ai-research-writing-skill` | Strong user-facing framing around evidence-backed paper generation, claim-evidence maps, verified citations, figures, LaTeX output, reviewer critique, and build checks. | Do not copy general ML/AI conference scope or venue-specific template claims into a CFD-AI package. | Present the package as an operational workflow that creates artifacts, not as a prompt collection. |
| `zengrong233/awesome-ai-research-writing-skill` | Codex-oriented conversion of a prompt catalog into `SKILL.md` plus routed `references/` files. | Do not center prompt browsing as the main user value. | Keep `SKILL.md` narrow and route deeper task instructions into references. |
| `Zejun-W/AI-Research-Writing-Skills-Hub` | unknown/TODO: repository access was not verified. | Do not cite its structure or claims until inspected. | No adoption decision. |
| `WillDreamer/Awesome-AI4CFD` | A broad AI4CFD literature/resource map. | Do not treat a curated list as a benchmark ontology or proof of coverage. | Use as a reminder to cover solver acceleration, surrogate modeling, flow control, turbulence, and benchmark resources. |
| `ikespand/awesome-machine-learning-fluid-mechanics` | Wide map of ML in fluid mechanics: books, events, datasets, tools, CFD codes, and application domains. | Do not import broad lists into user docs. | Distill dataset/tool classes into review and reproducibility axes. |
| `YunchaoYang/Machine_Learning_Fluid_Dynamics` | Compact taxonomy of review papers, turbulence closure, flow approximation, PIV, lift/drag, flow control, multiphase, tools, and neural-operator topics. | Do not use old list entries as current-state claims without follow-up verification. | Add harder benchmarks that force turbulence-closure and benchmark-landscape reasoning. |

## Adopted package principles

| Principle | Reason |
|---|---|
| User docs should lead with what the agent will do. | Related writing-skill repos are strongest when they describe outputs and workflows, not internal build history. |
| Keep internal evaluation separate from public onboarding. | Users need quickstart, workflows, and task examples; maintainers need benchmarks and distillation notes. |
| Use `references/` for dense domain maps. | CFD-AI landscape material is too broad for `SKILL.md` or the README. |
| Treat claim-evidence as a contract. | Both writing-skill and CFD-AI review needs converge on provenance, limitation boundaries, and reviewer risk. |
| Add benchmark prompts that punish shallow review prose. | The CFD resource lists expose domains where generic academic writing fails: closure modeling, coupled-solver validation, split design, and reproducibility. |

## Internal improvement targets

| Target | Benchmark pressure |
|---|---|
| Turbulence closure review benchmark | Forces a priori vs a posteriori distinction, invariance, coupled-solver evidence, RANS/LES traps, and uncertainty. |
| Benchmark landscape review | Forces datasets/tools to be classified by validation axis, split design, failure modes, and reproducibility rather than popularity. |
| Public README rewrite | Prevents internal gold-author/evaluator history from becoming the first user experience. |
| Deterministic evaluator profiles | Adds profile names for new benchmarks while preserving the script's limited role as a surface scan only. |

## Caveats

- This distillation is a source-scope snapshot, not a literature review.
- Curated "awesome" lists are useful for coverage prompts but not authoritative rankings.
- Repository README content can drift; future benchmark changes should cite a fresh source-scope note.
- Unknown facts remain TODO; do not infer DOI values, official installer commands, or paper-specific claims from these sources.
