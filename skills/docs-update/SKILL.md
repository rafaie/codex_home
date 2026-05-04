---
name: docs-update
description: Update README and spec docs after a work item ships.
---

1) Scan the work item folder (`feature.md`, `implementation.md`, `test-results.md`) for user-facing changes.
2) Update `README.md` (quickstart, usage examples, env vars/config).
3) Update/add pages under `spec/`.
   - Update `spec/docstrings.md` when project docstring policy or examples change.
4) Add an entry to `spec/changelog.md`.
5) Record updates in the work item docs:
   - `implementation.md`: docs files changed
   - `status.md`: docs/index status
   - legacy single-file specs: Docs/README section
