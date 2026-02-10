---
name: implement-feature
description: Implement a feature end-to-end based on its spec/features file.
---

1) Read project `AGENTS.md`, `codex.toml` (if present), and the target `spec/features/<feature-id>-<slug>.md`.
   - `<feature-id>` must use `F<epic>.<feature>` (example: `F1.1`).
2) Convert acceptance criteria into a checklist.
3) Implement iteratively (respect `codex.toml` command overrides if present):
   - Make the smallest code change to satisfy one criterion
   - Add/adjust tests
   - Run the project test command (`codex.toml` `test` if present; otherwise `uv run pytest -q`)
4) Completion rule: all checklist items should be checked before calling the feature implemented.
   - If an item is blocked/deferred, leave it unchecked and record reason, owner/next step, and follow-up feature ID.
5) Update the feature spec Implementation log with files changed, commands run, decisions, and any deferred checklist items.
6) If tests fail, invoke `debug-loop`.
7) If user-facing behavior changed, invoke `docs-update`.
