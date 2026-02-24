---
name: test-runner
description: Run quick/full checks consistently, include smoke, and summarize failures into actionable buckets.
---

1) Read `codex.toml` (if present) for canonical commands.
2) Resolve commands (prefer `codex.toml`, otherwise defaults):
   - format: `uv run ruff format . --check`
   - lint: `uv run ruff check .`
   - typecheck: `uv run mypy src`
   - quick tests: `test_quick`, else `test`, else `uv run pytest -q`
   - full tests: `test_full`, else `test`, else `uv run pytest -q`
   - smoke: `smoke`, else `uv run python scripts/smoke.py` if present
3) Support two modes:
   - Quick mode:
     - format/lint
     - feature-scoped or quick tests (`test_quick` fallback chain)
     - smoke-test
   - Full mode:
     - format/lint
     - typecheck
     - full test suite (`test_full` fallback chain)
     - smoke-test
4) Always run smoke as its own stage after tests/checks and report it as a separate result bucket.
5) Summarize results:
   - Mode used and commands run
   - What passed
   - What failed (top 3 failure signatures)
   - Smoke result (pass/fail + artifact path when available)
   - Likely category: env/setup vs flaky vs deterministic bug vs expectation mismatch
6) Recommendation logic:
   - If unit/tests pass but smoke fails, prioritize packaging/runtime and invoke `debug-loop`.
   - If there are many failures, invoke `failure-triage`.
   - If failures appear intermittent, invoke `flaky-test-hunter`.
