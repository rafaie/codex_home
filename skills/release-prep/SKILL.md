---
name: release-prep
description: Prepare a release run checks, update changelog, verify docs, summarize notes.
---

1) Read `codex.toml` (if present) for canonical commands.
2) Run checks:
   - Resolve commands with this fallback chain:
     - `format`: `format`, else `uv run ruff format . --check`
     - `lint`: `lint`, else `uv run ruff check .`
     - `typecheck`: `typecheck`, else `uv run mypy src`
     - `test_full`: `test_full`, else `test`, else `uv run pytest -q`
     - `smoke`: `smoke`, else `uv run python scripts/smoke.py` if present
   - Run in order: format/lint -> typecheck -> full tests -> smoke.
   - Treat smoke as a required release gate for runnable paths.
3) Update `spec/changelog.md`.
4) Verify `README.md` is accurate.
5) Summarize release notes.
