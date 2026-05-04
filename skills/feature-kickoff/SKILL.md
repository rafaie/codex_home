---
name: feature-kickoff
description: Create a work item documentation folder under spec/features/ (and ADR if needed).
---

1) Read project `AGENTS.md` (repo root) and `codex.toml` (if present) and follow conventions/commands.
2) Collect inputs: Work item ID (`S-<stream>-<nnn>`, example `S-core-001`), title, goal, constraints.
   - Accept legacy dotted `F` IDs only when updating older specs; create new work with `S-<stream>-<nnn>`.
3) Create a work item folder `spec/features/<work-id>-<slug>/` (use actual work item ID).
   - Prefer repo templates under `spec/templates/` if present.
   - Otherwise use this skill's `assets/default_*_template.md` files.
4) Create/update these documents inside the folder:
   - `feature.md`: problem, scope, acceptance criteria, design, ADR links
   - `implementation.md`: implementation plan and chronological implementation log
   - `test-plan.md`: unit/integration/e2e/edge/smoke test plan
   - `test-results.md`: commands run, outcomes, failures, fixes
   - `status.md`: status, owner, next action, blockers
   - `evidence/README.md`: directory placeholder and evidence index
5) Fill the initial docs.
   - `test-plan.md` must include smoke details: scenario, fixture, pass/fail mode, artifact path.
6) If no ADRs exist yet, create `spec/decisions/ADR-0001-initial-architecture.md` (prefer `spec/templates/adr.md` if present).
7) If a major decision is required, create `spec/decisions/ADR-XXXX-<slug>.md` (prefer `spec/templates/adr.md` if present).
8) Stop after writing docs. Do NOT implement code.
9) End by listing the next 3 tasks.
   - Tasks must be distinct (no duplicates).
   - Use this default sequence unless the user asks for a different flow:
     1) `Run $spec-linter <work-id> to review the work item docs for gaps.`
     2) `Run $implementation-phase <work-id> to plan tests, write tests, and implement the work item.`
     3) `Run $ship-feature <work-id> to execute full checks, smoke evidence, ADR/docs/index updates, and final readiness output.`
   - `<work-id>` must be the real ID for the folder you just created (example: `S-core-001`).
   - Keep each task line concrete and non-redundant.
