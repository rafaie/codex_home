# Codex Home (Global) — Instructions

This repository is my Codex home directory. It is not a single project.
It provides reusable prompts, skills, and templates that I apply to
other project repositories.

## How to use this home with any project
- Always treat the target repo as the source of truth for implementation.
- If the target repo has its own `AGENTS.md`, follow it first.
- If the target repo has a local `codex.toml`, use its command overrides.
- If there is no local `codex.toml`, use the defaults described below.
- Do not add `spec/` or `docs/` here; those live in each project repo.

## Default command assumptions (override per project)
When prompts/skills mention tests or checks and no local override exists,
use these defaults:
- Tests: `uv run pytest -q`
- Lint: `uv run ruff check .`
- Format: `uv run ruff format . --check`
- Types: `uv run mypy src`

## Per-project overrides
Create a `codex.toml` in the target repo root to override commands:

```toml
[commands]
test = "uv run pytest -q"
lint = "uv run ruff check ."
format = "uv run ruff format . --check"
typecheck = "uv run mypy src"
```

## Guardrails
- Never edit or delete user project files unless asked to.
- When instructions conflict, this file is secondary to the project’s
  `AGENTS.md` and explicit user requests.
- Keep changes small, and document decisions in the project’s spec/logs.
