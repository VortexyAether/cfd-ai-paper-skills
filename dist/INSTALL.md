# Install Notes

This archive is a source package for the CFD-AI paper skills package.
Use the root `SKILL.md` as the umbrella entrypoint, then route to focused subskills under `skills/*/SKILL.md` as needed.

```bash
tar -xzf cfd-ai-paper-skills-v0.6.1.tar.gz
cd cfd-ai-paper-skills-v0.6.1
python3 scripts/validate_package.py
python3 scripts/run_static_evals.py
```

The package contains the root entrypoint, local subskills, references, rubrics, examples, templates, evaluation tasks, and benchmark run artifacts.
No external credentials are required for the deterministic validators.
