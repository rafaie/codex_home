---
name: implement-feature
description: Implement a work item end-to-end based on its spec/features folder with a fast inner loop and smoke milestones.
---

1) Read project `AGENTS.md`, `codex.toml` (if present), and target work item folder `spec/features/<work-id>-<slug>/`.
   - `<work-id>` must use `S-<stream>-<nnn>` (example: `S-core-001`) for new work.
   - Read `feature.md`, `implementation.md`, `test-plan.md`, `test-results.md`, and `status.md` when present.
   - For legacy single-file specs, read the matching file under `spec/features/`.
2) Convert acceptance criteria into a checklist.
3) Implement iteratively, one AC at a time:
   - Make the smallest change to satisfy one criterion
   - Add/adjust tests
   - Add or update Google-style docstrings for new/changed public APIs, CLI entrypoints, data models/schemas, provider/client wrappers, integration boundaries, non-trivial private helpers, and shared test fixtures.
   - Do not add docstrings that only restate the function name.
   - Run quick checks (`test_quick`, else `test`, else `uv run pytest -q`)
4) Run full checks plus smoke at required milestones:
   - End of the final AC
   - Any change to core/shared modules
   - Any CLI, API, schema, or I/O behavior change
5) Completion rule:
   - All checklist items are checked, and
   - `test-runner` full mode passes, and
   - `smoke-test` passes with evidence artifacts.
   - If an item is blocked/deferred, leave it unchecked and record reason, owner/next step, and follow-up work item ID.
6) Update work item docs:
   - `implementation.md`: implementation log, files changed, key decisions/trade-offs
   - `test-results.md`: commands run + outcomes
   - `status.md`: current status, blockers, next action
   - `feature.md`: only update scope/AC/design if reality changed
7) Include docstring changes or intentional omissions in `implementation.md` when API-facing code changed.
8) Include smoke evidence path (`artifacts/smoke/...`) in `implementation.md` or `test-results.md` when smoke runs.
9) If checks fail, invoke `debug-loop`.
10) If user-facing behavior changed, invoke `docs-update`.
