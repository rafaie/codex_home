# AGENTS.md (starter)
# This file provides repository-level guidance to Codex.

## Workflow
- Use spec-driven development.
- For new work: run `$qa-intake` → `$feature-kickoff` → `$test-plan` → `$write-tests` → `$implement-feature`.
- If tests fail: `$debug-loop`.
- After shipping a feature: `$adr-review` (if decisions changed), `$docs-update`, then `$docs-index-refresh`.

## Conventions (edit for your repo)
- Specs: `spec/features/` and `spec/decisions/`
- Project docs: `spec/` (index, brief, architecture, changelog)
- Tests: `tests/`

## Commands
- Prefer commands from `codex.toml` when present.
