---
name: feature-closeout
description: Finalize a feature with full checks, smoke evidence, ADR/docs updates, and complete spec records.
---

1) Read the feature spec `spec/features/<feature-id>-<slug>.md`.
   - `<feature-id>` must use `F<epic>.<feature>` (example: `F1.1`).
2) Confirm all closure criteria:
   - Acceptance criteria satisfied
   - Full checks passing (`test-runner` full mode)
   - Smoke-test passing with evidence artifacts under `artifacts/smoke/...`
   - Any failures were handled and documented in Debug log
3) Ensure the feature spec includes an `## Evidence` section with:
   - `Smoke artifacts: <path>`
   - `Smoke summary: <brief>`
   - Optional key metrics (latency/error buckets)
4) Run `adr-review` if decisions changed or are implied by implementation.
5) Run `docs-update` for user-facing changes.
6) Run `docs-index-refresh` to reflect feature status.
7) Update the feature spec with:
   - Files changed
   - Commands run
   - Links to docs and ADRs
8) End by stating `Feature <feature-id> is ready to merge/release` plus any remaining TODOs.
