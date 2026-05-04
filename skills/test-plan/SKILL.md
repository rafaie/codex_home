---
name: test-plan
description: Create a work item test plan from acceptance criteria and add it to the work item docs.
---

1) Read `AGENTS.md`, `codex.toml` (if present), and the target work item folder `spec/features/<work-id>-<slug>/`.
   - `<work-id>` must use `S-<stream>-<nnn>` (example: `S-core-001`) for new work.
   - For legacy single-file specs, read the matching file under `spec/features/`.
   - Source acceptance criteria from `feature.md` (or the legacy single-file spec).
2) Convert acceptance criteria into a test matrix:
   - Unit tests (fast, isolated)
   - Integration tests (component boundaries)
   - End-to-end / scenario tests (happy path + key edge cases)
   - Negative/error cases (validation, permissions, timeouts, etc.)
3) Decide what to mock vs run for real (with rationale).
4) Update `test-plan.md` with:
   - Test cases mapped to ACs
   - Test data/fixtures needed
   - Any required test hooks/utilities
   - Smoke plan fields:
     - scenario ID/name
     - fixture path
     - expected output shape (schema and invariants)
     - pass/fail mode (schema/invariants only, or schema/invariants/golden)
     - runtime constraints (mode, network/env, time budget, request/token budget)
     - artifact path expectation (`artifacts/smoke/...`)
5) End by recommending `write-tests`.
   - Output exactly:
     - `Next recommended skill:`
     - `Run $write-tests <work-id> to implement the planned unit/integration/edge-case tests.`
   - Replace `<work-id>` with the real ID from the target folder (example: `S-core-001`).
   - Do not use markdown links or absolute file paths in this recommendation.
