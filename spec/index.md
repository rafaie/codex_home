# Codex Home Spec Index

Navigation for the global Codex home (`~/.codex`) skill pack.

## Start here
- [`README.md`](../README.md)
- [`AGENTS.md`](../AGENTS.md)
- [`templates/codex.toml`](../templates/codex.toml)
- [`spec/changelog.md`](changelog.md)
- [`spec/decisions/`](decisions/)

## Current status
- Workflow uses stream/sequence work item IDs (`S-<stream>-<nnn>`) and folder-based docs under `spec/features/`.
- `$project-intake` bootstraps new target repos with SDLC starter files before writing `spec/brief.md` and `spec/index.md`.
- Default endgame flow is `$ship-feature` with full checks, smoke evidence, ADR/docs/index updates, and readiness output.
- Smoke policy is live-first with offline fallback, required artifact contract, and enforced run budgets.
- `test-runner` full mode is the canonical smoke owner for ship flow; `ship-feature` validates and records that artifact instead of rerunning smoke.

## Work items and workflow
### Planned
- Expand smoke registry/template examples for more provider patterns.

### In Progress
- None tracked in this global home spec index.

### Implemented
- `qa-intake` produces a verification/evidence contract and smoke questions when applicable.
- `test-runner` supports quick/full modes and always includes smoke results.
- `implementation-phase` orchestrates test planning, test writing, and implementation.
- `ship-feature` is the default endgame; `feature-closeout` remains a deprecated compatibility fallback.
- Templates now use work item folders with `feature.md`, `implementation.md`, `test-plan.md`, `test-results.md`, `status.md`, and `evidence/README.md`.
- `project-intake` now initializes missing `AGENTS.md`, `codex.toml`, `spec/templates/`, smoke starter files, `spec/brief.md`, `spec/index.md`, and `spec/changelog.md` in target repos.

## Decisions
- [`ADR-0001-live-first-smoke-harness.md`](decisions/ADR-0001-live-first-smoke-harness.md)

## Notes
- `project-intake` must run from the target project repo, not this global Codex home.
- `release-prep` remains a release-level skill and is not the per-work-item endgame.
