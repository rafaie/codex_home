# Codex Home

This is my global Codex home folder (`~/.codex`). It is not a single
project repo; it is a reusable toolbox for all projects.

## What lives here
- `prompts/`: reusable lifecycle prompts (kickoff, implement, debug, docs, release).
- `skills/`: task-specific workflows Codex can invoke.
- `templates/`: reusable templates to copy into project repos.
- `docs/`: usage examples and documentation index.
- `AGENTS.md`: global instructions for using this home across projects.

## How I use this with any project
1) Open the target project repo.
2) If the repo has `AGENTS.md`, that is the source of truth.
3) If the repo has `codex.toml`, use it to override commands.
4) Otherwise, follow the defaults in `AGENTS.md` in this repo.

## Per-project command overrides
Place a `codex.toml` in the project root with command overrides:

```toml
[commands]
test = "uv run pytest -q"
lint = "uv run ruff check ."
format = "uv run ruff format . --check"
typecheck = "uv run mypy src"
```

## Bootstrap checklist for new repos
- Add a project `AGENTS.md` (repo-specific conventions).
- Add `codex.toml` with test/lint/typecheck commands.
- Create `spec/` and `docs/` if you plan to use lifecycle prompts.
