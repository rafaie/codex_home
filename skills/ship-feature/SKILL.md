---
name: ship-feature
description: "Execute the endgame path for one feature: full checks, smoke evidence, ADR/docs/index updates, and release-readiness summary."
---

1) Read target spec `spec/features/<feature-id>-<slug>.md`.
   - `<feature-id>` must use `F<epic>.<feature>` (example: `F1.1`).
2) Verify spec completeness before execution:
   - acceptance criteria present
   - test plan present
   - smoke plan present (scenario + fixture + pass/fail mode + artifact expectation)
3) Run `test-runner` in full mode.
4) Run `smoke-test`.
   - Fail the flow if required smoke artifacts are missing.
5) Run `adr-review` when architecture/design decisions changed or the spec indicates ADR is required.
6) Run `docs-update` when user-facing behavior changed.
7) Run `docs-index-refresh` to keep spec navigation current.
8) Update the feature spec with a required `## Evidence` section:
   - `Smoke artifacts: <path>`
   - `Smoke summary: <brief>`
   - optional `Key metrics: latency/error buckets`
   - commands run and outcomes
9) End with a concise readiness summary:
   - feature ID
   - pass/fail of full checks
   - pass/fail of smoke
   - evidence paths
   - ADR/docs/index update status
   - final line: `Ready to ship` only when all required checks passed.
