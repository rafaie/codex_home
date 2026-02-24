# Codex Home Spec Index

Navigation for the global Codex home (`~/.codex`) skill pack.

## Start here
- [`README.md`](../README.md)
- [`AGENTS.md`](../AGENTS.md)
- [`templates/codex.toml`](../templates/codex.toml)
- [`spec/changelog.md`](changelog.md)
- [`spec/decisions/`](decisions/)

## Current status
- Workflow is now hard-cutover to quick inner loop + required smoke evidence for runnable paths.
- New endgame flow is `$ship-feature` as the standard one-command shipping path.
- Smoke policy is live-first with offline fallback and required artifact contract.

## Features and workflow
### Planned
- Expand smoke registry/template examples for more provider patterns.

### In Progress
- None tracked in this global home spec index.

### Implemented
- `qa-intake` now produces a verification/evidence contract and smoke questions when applicable.
- `test-runner` now supports quick/full modes and always includes smoke results.
- `implement-feature` and `feature-closeout` now require smoke milestones/evidence.
- Added new skills: `smoke-test`, `ship-feature`.
- Updated templates for smoke sections and evidence placeholders.

## Decisions
- [`ADR-0001-live-first-smoke-harness.md`](decisions/ADR-0001-live-first-smoke-harness.md)

## Notes
- `release-prep` remains a release-level skill and is not the per-feature endgame.
