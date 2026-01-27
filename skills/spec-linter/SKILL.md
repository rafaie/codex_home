---
name: spec-linter
description: Review a feature spec for clarity, testability, and completeness before implementation.
---

1) Read the target `spec/features/F-XXXX-*.md` and project conventions from `AGENTS.md`.
2) Check for:
   - Clear problem statement and scope/non-scope
   - Acceptance criteria that are testable and unambiguous
   - Inputs/outputs defined (formats, schemas, examples)
   - Edge cases + error handling expectations
   - Test plan is present (unit/integration/e2e as appropriate)
   - ADR linkage if decisions are involved
3) Produce a short “Spec Gaps” list, then either:
   - Propose edits, or
   - Apply edits directly if the user asks.
4) End by recommending the next skill (usually `write-tests` or `implement-feature`).
