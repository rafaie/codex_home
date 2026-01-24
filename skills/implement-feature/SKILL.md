---
name: implement-feature
description: Implement a feature end-to-end based on its spec/features file.
---

1) Read `AGENTS.md` and the target `spec/features/F-XXXX-...md`.
2) Convert acceptance criteria into a checklist.
3) Implement iteratively:
   - Make the smallest code change to satisfy one criterion
   - Add/adjust tests
   - Run `uv run pytest -q`
4) Update the feature spec Implementation log with files changed, commands run, and decisions.
5) If tests fail, invoke `debug-loop`.
6) If user-facing behavior changed, invoke `docs-update`.
