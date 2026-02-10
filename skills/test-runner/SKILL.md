---
name: test-runner
description: Run the right checks consistently and summarize failures into actionable buckets.
---

1) Read `codex.toml` (if present) for canonical commands.
2) If `codex.toml` is absent, use defaults:
   - format: `uv run ruff format . --check`
   - lint: `uv run ruff check .`
   - typecheck: `uv run mypy src`
   - tests: `uv run pytest -q`
3) Run in this order (skip steps not applicable to the repo):
   - format/lint
   - typecheck
   - unit tests
   - feature-scoped tests (by path/marker if available)
4) Summarize results:
   - What passed
   - What failed (top 3 failure signatures)
   - Likely category: env/setup vs flaky vs deterministic bug vs expectation mismatch
5) Recommend the next action:
   - `debug-loop` for deterministic failures
   - `failure-triage` if there are many failures
   - `flaky-test-hunter` if it appears intermittent
