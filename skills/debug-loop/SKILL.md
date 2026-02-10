---
name: debug-loop
description: Debug by reproducing, minimizing, writing regression tests, fixing, and documenting.
---

1) Reproduce the failure (exact command, inputs, environment).
2) Minimize to the smallest failing case.
3) Add a regression test that fails before the fix.
4) Fix the root cause.
5) Re-run the project test command (`codex.toml` `test` if present; otherwise `uv run pytest -q`).
6) Update the feature spec Debug log with repro, root cause, fix, and regression test.
