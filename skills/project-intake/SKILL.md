---
name: project-intake
description: Bootstrap a new project repo, then turn a rough project idea into a concise Project Brief and starting spec docs.
---

1) Confirm you are in the target project repo, not the global Codex home directory.
   - If the current repo is `/Users/mostafa/.codex` or another Codex home, stop and ask for the target project path.
   - If the repo already has `AGENTS.md`, follow it first.
2) Bootstrap missing SDLC files from `/Users/mostafa/.codex/templates/`.
   - Create missing directories: `spec/`, `spec/templates/`, `spec/decisions/`, `spec/features/`, `scripts/`.
   - Create `AGENTS.md` from `templates/AGENTS.md` only if missing.
   - Create `codex.toml` from `templates/codex.toml` only if missing.
   - Copy starter templates into `spec/templates/` only if missing:
     - `adr.md`
     - `architecture.md`
     - `backlog.md`
     - `feature.md`
     - `implementation.md`
     - `test-plan.md`
     - `test-results.md`
     - `status.md`
     - `evidence.md`
     - `spec_index.md`
   - Create smoke starters only if missing:
     - `spec/smoke.md` from `templates/smoke.md`
     - `spec/smoke_registry.yaml` from `templates/smoke_registry.yaml`
     - `scripts/smoke.py` from `templates/smoke.py`
   - Do not overwrite existing repo-local files unless the user explicitly asks.
3) Read the user’s project idea (or `spec/idea.md` if it exists), plus the newly bootstrapped `AGENTS.md` and `codex.toml`.
4) Ask up to 5 targeted questions only if essential info is missing (goal, users, constraints, success metrics).
5) Create/update:
   - `spec/brief.md` (1–2 pages) with: Goal, Users, Scope/Non-scope, Constraints, Risks, Milestones.
   - `spec/index.md` (navigation hub) with links to brief, architecture, ADRs, and backlog.
   - Prefer `spec/templates/spec_index.md` for a new `spec/index.md`.
6) Initialize the project workflow state:
   - Ensure `spec/changelog.md` exists with an initial entry.
   - Ensure `spec/decisions/` exists; do not create an ADR unless a real decision is present.
   - Leave `spec/backlog.md` for `backlog-builder` unless the user explicitly asks to create it now.
7) End with:
   - Files created
   - Files preserved because they already existed
   - Any commands the user should customize in `codex.toml`
   - Proposed “first 3 work items” list (thin vertical slices)
   - Exact next command: `Run $backlog-builder`
