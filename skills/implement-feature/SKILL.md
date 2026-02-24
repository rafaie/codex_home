---
name: implement-feature
description: Implement a feature end-to-end based on its spec/features file with a fast inner loop and smoke milestones.
---

1) Read project `AGENTS.md`, `codex.toml` (if present), and target `spec/features/<feature-id>-<slug>.md`.
   - `<feature-id>` must use `F<epic>.<feature>` (example: `F1.1`).
2) Convert acceptance criteria into a checklist.
3) Implement iteratively, one AC at a time:
   - Make the smallest change to satisfy one criterion
   - Add/adjust tests
   - Run quick checks (`test_quick`, else `test`, else `uv run pytest -q`)
4) Run full checks plus smoke at required milestones:
   - End of the final AC
   - Any change to core/shared modules
   - Any CLI, API, schema, or I/O behavior change
5) Completion rule:
   - All checklist items are checked, and
   - `test-runner` full mode passes, and
   - `smoke-test` passes with evidence artifacts.
   - If an item is blocked/deferred, leave it unchecked and record reason, owner/next step, and follow-up feature ID.
6) Update the feature spec Implementation log with:
   - Files changed
   - Commands run + outcomes
   - Key decisions/trade-offs
   - Smoke evidence path (`artifacts/smoke/...`)
7) If checks fail, invoke `debug-loop`.
8) If user-facing behavior changed, invoke `docs-update`.
