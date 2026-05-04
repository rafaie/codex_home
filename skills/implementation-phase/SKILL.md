---
name: implementation-phase
description: Run test-plan, write-tests, and implement-feature in sequence for one work item.
---

1) Read project `AGENTS.md`, `codex.toml` (if present), and target work item folder `spec/features/<work-id>-<slug>/`.
   - `<work-id>` must use `S-<stream>-<nnn>` (example: `S-core-001`) for new work.
   - For legacy single-file specs, read the matching file under `spec/features/`.
2) Execute the implementation phase in this exact order for the same work item ID:
   - `Run $test-plan <work-id>`
   - `Run $write-tests <work-id>`
   - `Run $implement-feature <work-id>`
3) Validate outcomes after each step:
   - `test-plan`: `test-plan.md` is updated with AC-mapped cases and fixtures.
   - `write-tests`: tests are added/updated under `tests/` and test command is run.
   - `implement-feature`: AC checklist is completed, required checks pass, and work item docs include commands + smoke evidence.
4) Failure handling:
   - Deterministic failures: run `debug-loop`.
   - Many simultaneous failures: run `failure-triage`.
   - Do not continue to the next step until the current step is resolved or explicitly deferred.
5) End with a concise status summary:
   - completed steps
   - blockers/deferred items (if any)
   - next recommended command:
     - `Run $ship-feature <work-id> ...` when all steps are complete
     - otherwise `Run $debug-loop ...` with the failing signature
