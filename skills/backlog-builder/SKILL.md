---
name: backlog-builder
description: Convert docs/brief.md into an initial backlog of epics and features with IDs and dependencies.
---

1) Read `docs/brief.md`, `docs/index.md` (if present), and repository conventions from `AGENTS.md`.
2) Produce a backlog with:
   - Epics (2–6)
   - Features per epic (3–10), each small enough to ship in 1–2 PRs
   - Each feature: title, 1–2 sentence goal, rough acceptance criteria, dependencies, risk notes
3) Write/update:
   - `spec/backlog.md`
   - Ensure `docs/index.md` links to the backlog.
4) End by recommending the next feature to spec (run `feature-kickoff`).
