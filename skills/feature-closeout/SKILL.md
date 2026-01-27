---
name: feature-closeout
description: Finalize a feature: tests green, ADRs captured, docs updated, and spec fully recorded.
---

1) Read the feature spec `spec/features/F-XXXX-*.md`.
2) Confirm:
   - Acceptance criteria satisfied
   - Tests added/updated and passing (run test command)
   - Any failures were handled and documented (Debug log)
3) Run `adr-review` if decisions changed or are implied by the implementation.
4) Run `docs-update` for user-facing changes.
5) Run `docs-index-refresh` to reflect the feature status (move to Implemented).
6) Update the feature spec with:
   - Files changed
   - Commands run
   - Links to docs and ADRs
7) End by stating “Feature F-XXXX is ready to merge/release” plus any remaining TODOs.
