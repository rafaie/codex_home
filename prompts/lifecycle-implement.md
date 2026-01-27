---
description: Implement a feature from its spec
argument-hint: FEATURE_ID=<F-0001>
---

Implement feature $FEATURE_ID based on its spec file in spec/features/.

Rules:
- Use the feature spec as source of truth.
- Implement in small steps.
- Add/modify tests as you go.
- Update the feature spec Implementation Log after each major step.

Do:
0) Ask clarifying questions before continuing, then follow the matching skill.
1) Implement AC1..ACn.
2) Run: `uv run pytest -q`
3) If tests fail, switch to the debug loop.
4) Update README/docs if needed.
