---
name: release-prep
description: Prepare a release run checks, update changelog, verify docs, summarize notes.
---

1) Read `codex.toml` (if present) for canonical commands.
2) Run checks:
   - Use `codex.toml` commands when defined: `test`, `lint`, `format`, `typecheck`.
   - If not defined, run `uv run pytest -q`, `uv run ruff check .`, `uv run ruff format . --check`, and `uv run mypy src`.
3) Update `spec/changelog.md`.
4) Verify `README.md` is accurate.
5) Summarize release notes.
