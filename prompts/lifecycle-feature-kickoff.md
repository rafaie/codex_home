---
description: Start a new feature spec under spec/features/
argument-hint: FEATURE_ID=<F-0001> TITLE="..." GOAL="..." CONSTRAINTS="..."
---

Start a new feature spec.

Inputs:
- Feature ID: $FEATURE_ID
- Feature title: $TITLE
- Goal: $GOAL
- Constraints: $CONSTRAINTS

Do:
1) Create spec/features/$FEATURE_ID-<slug>.md using spec/templates/feature.md if present; otherwise use the default template.
2) Fill Problem, Scope, Acceptance Criteria, Implementation plan, Test plan.
3) If a key design decision is needed, create a draft ADR under spec/decisions/.
4) Stop after writing the spec; do NOT implement yet.
