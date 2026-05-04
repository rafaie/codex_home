# AGENTS.md (starter)
# This file provides repository-level guidance to Codex.

## Workflow
- Use spec-driven development.
- For new projects: run `$project-intake` → `$backlog-builder`.
  - `$project-intake` initializes missing SDLC files (`AGENTS.md`, `codex.toml`, `spec/templates/`, smoke starters, `spec/docstrings.md`, `spec/brief.md`, `spec/index.md`, `spec/changelog.md`) without overwriting existing repo-local files.
- For each work item: run `$qa-intake` (if requirements are unclear) → `$feature-kickoff` → `$spec-linter` → `$implementation-phase`.
- Then run `$ship-feature` as the required final work item step (definition of done).
- `ship-feature` includes full checks + smoke evidence and ADR/docs/index hygiene (`$adr-review` when needed, `$docs-update`, `$docs-index-refresh`).
- Use `$feature-closeout` only when your repo has not adopted `$ship-feature` yet.
- If tests fail: `$debug-loop` (or `$failure-triage` when many failures exist).
- Before release: run `$release-prep`.

## Conventions (edit for your repo)
- Specs: `spec/features/` and `spec/decisions/`
- Work item IDs: `S-<stream>-<nnn>` (example: `S-core-001`)
- Work item folders: `spec/features/<work-id>-<slug>/`
- Work item docs: `feature.md`, `implementation.md`, `test-plan.md`, `test-results.md`, `status.md`, `evidence/README.md`
- Project docs: `spec/` (index, brief, architecture, changelog)
- Tests: `tests/`
- Python docstrings: Google style for public APIs, CLI entrypoints, data models/schemas, provider/client wrappers, integration boundaries, non-trivial private helpers, and shared test fixtures. Do not add docstrings that only restate the function name.

## Commands
- Prefer commands from `codex.toml` when present.
- Run `[commands].docstrings` when configured; otherwise rely on review guidance and existing lint settings.
