---
name: write-tests
description: Add or improve tests based on a work item folder's acceptance criteria and test plan.
---

1) Read project `AGENTS.md`, `codex.toml` (if present), and the target work item folder `spec/features/<work-id>-<slug>/`.
   - Source acceptance criteria from `feature.md`.
   - Source planned coverage from `test-plan.md`.
   - For legacy single-file specs, read the matching file under `spec/features/`.
2) Refine the test matrix only if the existing `test-plan.md` has gaps.
3) Implement tests under `tests/`.
4) Run the quick test command (`test_quick`, else `test`, else `uv run pytest -q`).
5) Update `test-results.md` with:
   - tests added/updated
   - command run + outcome
   - failures and fixes, if any
