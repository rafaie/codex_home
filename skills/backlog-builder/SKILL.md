---
name: backlog-builder
description: Convert spec/brief.md into an initial backlog of streams and shippable work items with IDs and dependencies.
---

1) Read `spec/brief.md`, `spec/index.md` (if present), and repository conventions from `AGENTS.md`.
2) Produce a backlog with:
   - Streams (2–6), such as `core`, `cli`, `docs`, `eval`, `infra`
   - Work items per stream (3–10), each small enough to ship in 1–2 PRs
   - Work item ID format: `S-<stream>-<nnn>` (example: `S-core-001`)
   - Each work item: ID, title, 1–2 sentence goal, rough acceptance criteria, dependencies, risk notes
3) Write/update:
   - `spec/backlog.md`
   - Ensure `spec/index.md` links to the backlog.
4) End by recommending the next work item to spec (run `feature-kickoff`).
