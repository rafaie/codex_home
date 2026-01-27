---
name: test-runner
description: Run the right checks consistently and summarize failures into actionable buckets.
---

1) Read `codex.toml` (if present) for canonical commands; otherwise use sensible defaults.
2) Run in this order (skip steps not applicable to the repo):
   - format/lint
   - typecheck
   - unit tests
   - feature-scoped tests (by path/marker if available)
3) Summarize results:
   - What passed
   - What failed (top 3 failure signatures)
   - Likely category: env/setup vs flaky vs deterministic bug vs expectation mismatch
4) Recommend the next action:
   - `debug-loop` for deterministic failures
   - `failure-triage` if there are many failures
   - `flaky-test-hunter` if it appears intermittent
