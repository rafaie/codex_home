---
name: implementation-phase
description: Run test-plan, write-tests, and implement-feature in sequence for one feature.
---

1) Read project `AGENTS.md`, `codex.toml` (if present), and target `spec/features/<feature-id>-<slug>.md`.
   - `<feature-id>` must use `F<epic>.<feature>` (example: `F1.1`).
2) Execute the implementation phase in this exact order for the same feature ID:
   - `Run $test-plan <feature-id>`
   - `Run $write-tests <feature-id>`
   - `Run $implement-feature <feature-id>`
3) Validate outcomes after each step:
   - `test-plan`: feature spec Test plan is updated with AC-mapped cases and fixtures.
   - `write-tests`: tests are added/updated under `tests/` and test command is run.
   - `implement-feature`: AC checklist is completed, required checks pass, and Implementation log includes commands + smoke evidence.
4) Failure handling:
   - Deterministic failures: run `debug-loop`.
   - Many simultaneous failures: run `failure-triage`.
   - Do not continue to the next step until the current step is resolved or explicitly deferred.
5) End with a concise status summary:
   - completed steps
   - blockers/deferred items (if any)
   - next recommended command:
     - `Run $ship-feature <feature-id> ...` when all steps are complete
     - otherwise `Run $debug-loop ...` with the failing signature

