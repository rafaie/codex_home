# Smoke Test Contract (Live-First, No UI)

## Purpose
Smoke verifies the real runnable path quickly (target under 10-30s) and emits deterministic evidence artifacts.

## Required coverage
- Real entrypoint is executed via subprocess (CLI/module/script).
- Tiny fixture input is used (`tests/fixtures/smoke/`).
- Output passes schema validation and invariants.
- Golden comparison is optional per scenario and updated only via explicit `--record`.

## Mode policy
- Default to live canary when provider credentials are available (`SMOKE_LIVE=1` or provider API keys).
- Fallback to offline mode when live credentials are unavailable.
- Keep live runs tiny and cheap (1-3 cases, low token budget, temperature 0 by default).

## Required artifacts
Write artifacts for every run under `artifacts/smoke/<timestamp>/`:
- `summary.json`
- `cases/<case_id>.json`
- `stdout.txt`
- `stderr.txt`
- `timing.json`

`summary.json` must include:
- run config/mode
- budgets
- per-provider stats
- failure bucket counts
- `artifact_version`

Each `cases/<case_id>.json` must include:
- input pointer/hash
- request params
- raw response (redacted)
- parsed output
- validation results
- primary `failure_bucket`

## Failure taxonomy
Use one primary failure bucket per case and aggregate in summary:
- `config_error`, `fixture_error`, `auth`, `permission_error`, `network_error`, `timeout`, `rate_limit`, `quota_exceeded`, `provider_error`, `invalid_response`, `parse_error`, `schema_error`, `invariant_error`, `golden_mismatch`, `budget_exceeded`, `artifact_error`, `subprocess_error`, `internal_error`

## Update policy
- Update fixtures/goldens only when behavior change is intentional and documented in feature spec logs.
- Keep scenario definitions small and feature-owned (via `spec/smoke_registry.yaml`).
