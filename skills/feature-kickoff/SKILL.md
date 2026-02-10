---
name: feature-kickoff
description: Create a feature spec under spec/features/ (and ADR if needed).
---

1) Read project `AGENTS.md` (repo root) and `codex.toml` (if present) and follow their conventions and commands.
2) Collect inputs: Feature ID (`F<epic>.<feature>`, example `F1.1`), title, goal, constraints.
3) Create `spec/features/<feature-id>-<slug>.md` (use the actual feature ID):
   - Prefer `spec/templates/feature.md` if present.
   - Otherwise use `assets/default_feature_template.md`.
4) Fill: Problem, Scope, Acceptance Criteria, initial Implementation plan, initial Test plan.
5) If no ADRs exist yet, create `spec/decisions/ADR-0001-initial-architecture.md` (prefer `spec/templates/adr.md` if present).
6) If a major decision is required, create `spec/decisions/ADR-XXXX-<slug>.md` (prefer `spec/templates/adr.md` if present).
7) Stop after writing specs. Do NOT implement code.
8) End by listing the next 3 tasks.
   - Tasks must be distinct (no duplicates).
   - Use this default sequence unless the user explicitly asks for a different flow:
     1) `Run $test-plan <feature-id> to expand executable validation checks for this feature spec.`
     2) `Run $write-tests <feature-id> to add/adjust tests mapped to the acceptance criteria.`
     3) `Run $implement-feature <feature-id> to implement the code iteratively against the checklist.`
   - `<feature-id>` must be the real ID for the spec you just created (example: `F1.1`).
   - Keep each task line concrete and non-redundant.
