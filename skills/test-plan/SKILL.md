---
name: test-plan
description: Create a feature-level test plan from acceptance criteria and add it to the feature spec.
---

1) Read `AGENTS.md`, `codex.toml` (if present), and the target feature spec `spec/features/<feature-id>-<slug>.md`.
   - `<feature-id>` must use `F<epic>.<feature>` (example: `F1.1`).
2) Convert acceptance criteria into a test matrix:
   - Unit tests (fast, isolated)
   - Integration tests (component boundaries)
   - End-to-end / scenario tests (happy path + key edge cases)
   - Negative/error cases (validation, permissions, timeouts, etc.)
3) Decide what to mock vs run for real (with rationale).
4) Update the feature spec “Test plan” section with:
   - Test cases mapped to ACs
   - Test data/fixtures needed
   - Any required test hooks/utilities
5) End by recommending `write-tests`.
   - Output exactly:
     - `Next recommended skill:`
     - `Run $write-tests <feature-id> to implement the planned unit/integration/edge-case tests.`
   - Replace `<feature-id>` with the real ID from the target spec (example: `F1.2`).
   - Do not use markdown links or absolute file paths in this recommendation.
