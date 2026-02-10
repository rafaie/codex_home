# AGENTS.md (starter)
# This file provides repository-level guidance to Codex.

## Workflow
- Use spec-driven development.
- For new projects: run `$project-intake` → `$backlog-builder`.
- For each feature: run `$qa-intake` (if requirements are unclear) → `$feature-kickoff` → `$spec-linter` → `$test-plan` → `$write-tests` → `$implement-feature`.
- Then run `$feature-closeout` as the required final feature step (definition of done).
- `feature-closeout` includes ADR/docs/index hygiene (`$adr-review` when needed, `$docs-update`, `$docs-index-refresh`).
- If tests fail: `$debug-loop` (or `$failure-triage` when many failures exist).
- Before release: run `$release-prep`.

## Conventions (edit for your repo)
- Specs: `spec/features/` and `spec/decisions/`
- Feature IDs: `F<epic>.<feature>` (example: `F1.1`) and filenames `spec/features/<feature-id>-<slug>.md`
- Project docs: `spec/` (index, brief, architecture, changelog)
- Tests: `tests/`

## Commands
- Prefer commands from `codex.toml` when present.
