---
name: project-intake
description: Turn a rough project idea into a concise Project Brief and a starting spec/index.md.
---

1) Read the user’s project idea (or `spec/idea.md` if it exists), plus `AGENTS.md` and `codex.toml` if present.
2) Ask up to 5 targeted questions only if essential info is missing (goal, users, constraints, success metrics).
3) Create/update:
   - `spec/brief.md` (1–2 pages) with: Goal, Users, Scope/Non-scope, Constraints, Risks, Milestones.
   - `spec/index.md` (navigation hub) with links to brief, architecture, ADRs, and backlog.
4) End with a proposed “first 3 features” list (thin vertical slices) and recommend running `backlog-builder`.
