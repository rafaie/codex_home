# Changelog

## 2026-05-03
- Updated `project-intake` to bootstrap new target repos with missing `AGENTS.md`, `codex.toml`, `spec/templates/`, smoke starter files, `spec/brief.md`, `spec/index.md`, and `spec/changelog.md`.
- Hardened the smoke/ship contract so `test-runner` full mode owns smoke execution and `ship-feature` validates the emitted artifact instead of rerunning live smoke.
- Updated the smoke harness starter to honor scenario `mode`/`run_profile`, apply budget precedence, write synthetic case artifacts for run-level failures, and include command/artifact/fixture/provider metadata in `summary.json`.
- Tightened `test-plan` and `spec-linter` requirements for smoke planning, evidence placeholders, `test-results.md`, and `evidence/README.md`.

## 2026-02-22
- Added default smoke-first workflow guidance: fast inner loop + required smoke evidence.
- Added `smoke-test` and `ship-feature` skills.
- Updated `qa-intake`, `test-runner`, `implement-feature`, `feature-closeout`, and `feature-kickoff` for smoke-aware flow.
- Updated feature templates and `templates/codex.toml` command contract (`test_quick`, `test_full`, `smoke`).
- Added smoke starter templates: `templates/smoke.md`, `templates/smoke_registry.yaml`, `templates/smoke.py`.
- Migrated new work item IDs to `S-<stream>-<nnn>` and new docs to folder layout under `spec/features/<work-id>-<slug>/`.
