---
name: ship-feature
description: "Execute the endgame path for one work item: full checks, smoke evidence, ADR/docs/index updates, and release-readiness summary."
---

1) Read target work item folder `spec/features/<work-id>-<slug>/`.
   - `<work-id>` must use `S-<stream>-<nnn>` (example: `S-core-001`) for new work.
   - For legacy single-file specs, read the matching file under `spec/features/`.
2) Verify spec completeness before execution:
   - `feature.md` has acceptance criteria
   - `test-plan.md` exists and has planned coverage
   - `test-plan.md` has a smoke plan (scenario + fixture + pass/fail mode + artifact expectation)
   - API-facing work has Google-style docstring expectations documented or a clear no-change rationale
   - `status.md` has owner/status/next action
3) Run `test-runner` in full mode.
   - `test-runner` full mode owns the smoke execution for this flow.
   - Do not run `smoke-test` a second time unless the full-mode smoke artifact is missing, stale, or explicitly invalid.
4) Validate the smoke artifact emitted by `test-runner`.
   - Fail the flow if required smoke artifacts are missing: `summary.json`, `cases/<case_id>.json`, `stdout.txt`, `stderr.txt`, `timing.json`.
   - Record the artifact path and summary in the work item evidence docs.
5) Run `adr-review` when architecture/design decisions changed or the spec indicates ADR is required.
6) Run `docs-update` when user-facing behavior changed.
7) Run `docs-index-refresh` to keep spec navigation current.
8) Update the work item docs:
   - `test-results.md`: full checks, smoke outcome, failures/fixes
   - `implementation.md`: commands run and implementation summary
   - `status.md`: final status and remaining TODOs
9) Ensure evidence is recorded:
   - `Smoke artifacts: <path>`
   - `Smoke summary: <brief>`
   - optional `Key metrics: latency/error buckets`
10) End with a concise readiness summary:
   - work item ID
   - pass/fail of full checks
   - pass/fail of docstring checks when configured
   - pass/fail of the full-mode smoke stage
   - evidence paths
   - ADR/docs/index update status
   - final line: `Ready to ship` only when all required checks passed.
