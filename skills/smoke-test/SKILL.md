---
name: smoke-test
description: Run a real entrypoint smoke test, emit required artifacts, classify failures, and recommend the next action.
---

1) Resolve the smoke command.
   - Read `codex.toml` and use `[commands].smoke` when present.
   - If absent, use `uv run python scripts/smoke.py` when `scripts/smoke.py` exists.
   - If neither exists, fail as `config_error` and report the missing command/script.
2) Scope smoke to the requested work item when provided.
   - Prefer `--work-item <work-id>` for `scripts/smoke.py`.
   - Treat `--feature` as a deprecated compatibility alias only.
3) Run smoke using the real entrypoint path.
   - Smoke must execute a subprocess command path (CLI/module/script), not only import-level calls.
   - Use tiny fixture inputs under `tests/fixtures/smoke/` when available.
4) Enforce required artifact contract under `artifacts/smoke/<run-id>/` (or equivalent configured directory):
   - `summary.json`
   - `cases/<case_id>.json`
   - `stdout.txt`
   - `stderr.txt`
   - `timing.json`
5) Validate outputs.
   - Always validate schema contract.
   - Always validate invariants (required fields/ranges/non-empty critical fields).
   - Golden comparison is optional per scenario and must support explicit `--record` updates.
6) Summarize every run:
   - command run
   - work item ID (`work_item`) when provided
   - fixture(s)/scenario(s)
   - exit code
   - artifact locations
   - wall-clock time
   - budget telemetry (`requests_used`, `time_budget_exceeded`, max request/time settings)
   - failure bucket counts
7) Classify failures into one primary bucket per case/run summary:
   - `config_error`, `fixture_error`, `auth`, `permission_error`, `network_error`, `timeout`, `rate_limit`, `quota_exceeded`, `provider_error`, `invalid_response`, `parse_error`, `schema_error`, `invariant_error`, `golden_mismatch`, `budget_exceeded`, `artifact_error`, `subprocess_error`, `internal_error`
8) Use this exit-code mapping:
   - `0` pass
   - `10` config/fixture/auth/permission failure
   - `12` artifact failure
   - `20` subprocess failure
   - `22` network failure
   - `23` timeout
   - `24` rate limit
   - `25` quota exceeded
   - `26` provider error
   - `30` invalid/parse error
   - `40` schema validation failure
   - `41` invariants failure
   - `50` golden mismatch
   - `55` budget exceeded
   - `60` internal/unclassified
9) If multiple failures occur, prioritize exit code in this order:
   - artifact -> config/fixture/auth/permission -> quota -> rate_limit -> network -> timeout -> provider -> subprocess -> invalid/parse -> schema -> invariant -> golden -> budget -> internal
10) Recommend next action:
   - deterministic smoke/runtime/packaging issues -> `debug-loop`
   - fixture/golden updates only when behavior change is intentional and documented
