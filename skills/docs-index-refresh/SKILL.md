---
name: docs-index-refresh
description: Maintain spec/index.md as a living navigation hub that evolves work item by work item.
---

1) Read `spec/index.md` (if present), `spec/brief.md`, `spec/backlog.md`, and recent work item folders under `spec/features/`.
2) Update/create `spec/index.md` to include:
   - Start here links (brief, README, architecture, ADRs, backlog)
   - Current status (1–3 bullets)
   - Work items: Planned/In Progress/Implemented (with links to each `spec/features/<work-id>-<slug>/status.md` and `feature.md`)
   - Decisions: link to `spec/decisions/`
3) Keep it concise; it does NOT need to be “complete.” Prefer accurate links and current state.
4) End by listing what changed in `spec/index.md`.
