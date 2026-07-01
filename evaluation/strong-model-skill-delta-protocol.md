# Strong-Model Skill Delta Protocol

Use this protocol when the base model is already strong enough that a no-skill output appears plausible. The purpose is to reveal whether the skill package still adds gold-paper closeness, source discipline, and field-native texture.

## Principle

Do not make the no-skill arm bad on purpose. Instead, remove package-specific scaffolding from the no-skill prompt and then evaluate both arms with the same gold-paper rubric.

## Arm separation

### No-skill arm

Allowed inputs:

- task prompt;
- raw paper metadata or dense source summary;
- minimal scientific honesty instruction: do not invent unknown solver, metric, citation, or figure details.

Disallowed inputs:

- package skill files;
- rubrics;
- field terminology guide;
- gold-paper style patterns;
- examples from this package;
- claim-evidence templates.

Expected behavior:

- The strong model may produce good prose and mark some unknowns.
- It will often lack inspectable claim-evidence structure, gold-paper paragraph moves, and field-native phrase gates.

### With-skill arm

Allowed inputs:

- same task prompt and source summary;
- relevant skill files;
- relevant gold-paper notes;
- `references/gold-paper-style-patterns.md`;
- `references/field-terminology-style-guide.md`;
- `rubrics/gold-paper-closeness-rubric.md`;
- `rubrics/vocabulary-style-rubric.md`;
- relevant examples.

Expected behavior:

- Output may be less flashy.
- It should be closer to gold-paper logic: physical context, narrow gap, method role, ordered evidence, limitation boundary.
- It should expose missing evidence instead of smoothing it over.

## Recommended benchmark order

1. Generate the no-skill arm first.
2. Save the no-skill transcript/source scope.
3. Load package guidance only after the no-skill artifact is sealed.
4. Generate the with-skill arm using the same source summary.
5. Score both arms using the same evaluator table.

## Scoring stack

Use all relevant rubrics, but make `gold-paper-closeness-rubric.md` decisive for this benchmark.

Minimum report sections:

1. model and reasoning setting;
2. source scope for each arm;
3. gold-paper closeness table;
4. vocabulary/style audit;
5. hallucination and unsupported-claim audit;
6. reproducibility audit;
7. verdict: where the skill still changes behavior;
8. package patch recommendations.

## What counts as a real skill win

A with-skill win is not merely better English. Count these as wins:

- no loaded adjective remains without evidence;
- the first paragraph starts from a physical/numerical bottleneck, not AI capability;
- contribution is framed as input/output mapping under a named flow/regime;
- evidence sequence includes baseline, quantitative metric, field/error view, physical diagnostic, and limitation;
- unknown solver/grid/split/figure details remain TODO instead of implied facts;
- captions state what claim the figure supports;
- related work is taxonomy-based, not chronological;
- limitations name the untested axis and required experiment.

## What counts as no-skill catching up

Record no-skill progress if it:

- marks unknown facts without package guidance;
- avoids broad deployment claims;
- gives reasonable field terms from the source summary;
- produces a readable manuscript seed.

The report should then say the skill margin narrowed, not that the skill failed.

## Patch trigger

Patch the package only when a failure is repeatable or conceptually important. Good patch triggers:

- with-skill output is too audit-heavy and not manuscript-like;
- the skill fails to catch AI-ish context paragraphs;
- figure captions remain decorative;
- no-skill and with-skill differ only cosmetically;
- evaluator cannot score gold-paper closeness from existing rubrics.
