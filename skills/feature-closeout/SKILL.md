---
name: feature-closeout
description: Deprecated compatibility fallback for older repos that have not adopted ship-feature.
---

1) Prefer `ship-feature` for migrated repos. Use this skill only for older repos whose `AGENTS.md` still requires `feature-closeout`.
2) Read the target work item folder `spec/features/<work-id>-<slug>/` or the matching legacy single-file spec under `spec/features/`.
3) Confirm all closure criteria:
   - Acceptance criteria satisfied
   - Full checks passing (`test-runner` full mode)
   - Smoke-test passing with evidence artifacts under `artifacts/smoke/...`
   - Any failures were handled and documented in Debug log
4) Ensure evidence is recorded in `test-results.md`, `implementation.md`, or the legacy `## Evidence` section:
   - `Smoke artifacts: <path>`
   - `Smoke summary: <brief>`
   - Optional key metrics (latency/error buckets)
5) Run `adr-review` if decisions changed or are implied by implementation.
6) Run `docs-update` for user-facing changes.
7) Run `docs-index-refresh` to reflect work item status.
8) Update the docs with:
   - Files changed
   - Commands run
   - Links to docs and ADRs
9) End by stating `Work item <work-id> is ready to merge/release` plus any remaining TODOs.
