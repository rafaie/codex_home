---
name: feature-kickoff
description: Create a feature spec under spec/features/ (and ADR if needed).
---

1) Read `AGENTS.md` (repo root) and follow its conventions and commands.
2) Collect inputs: Feature ID (F-XXXX), title, goal, constraints.
3) Create `spec/features/F-XXXX-<slug>.md`:
   - Prefer `spec/templates/feature.md` if present.
   - Otherwise use `assets/default_feature_template.md`.
4) Fill: Problem, Scope, Acceptance Criteria, initial Implementation plan, initial Test plan.
5) If a major decision is required, create `spec/decisions/ADR-XXXX-<slug>.md` (prefer `spec/templates/adr.md` if present).
6) Stop after writing specs. Do NOT implement code.
7) End by listing the next 3 tasks.
