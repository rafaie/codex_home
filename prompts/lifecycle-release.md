---
description: Prepare a release for completed features
argument-hint: VERSION=<v0.1.0>
---

Prepare a release.

Do:
0) Ask clarifying questions before continuing, then follow the matching skill.
1) Ensure all tests/lint/type checks pass:
   - `uv run pytest -q`
   - `uv run ruff check .`
   - `uv run ruff format . --check`
   - `uv run mypy src`
2) Update spec/changelog.md for $VERSION.
3) Verify README is accurate.
4) Summarize release notes.
