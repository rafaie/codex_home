---
name: spec-linter
description: Review a work item documentation folder for clarity, testability, and completeness before implementation.
---

1) Read the target work item folder `spec/features/<work-id>-<slug>/` and project conventions from `AGENTS.md`.
   - `<work-id>` must use `S-<stream>-<nnn>` (example: `S-core-001`) for new work.
   - For legacy single-file specs, read the matching file under `spec/features/`.
2) Check for:
   - `feature.md`: clear problem statement, scope/non-scope, testable acceptance criteria, inputs/outputs, ADR linkage
   - `implementation.md`: initial implementation plan
   - `test-plan.md`: unit/integration/e2e/edge/smoke plan
   - `test-results.md`: command/result placeholders and evidence section
   - `status.md`: current status, owner, next action, blockers
   - `evidence/README.md`: evidence index with smoke artifact/summary placeholders
   - Smoke placeholders: scenario, fixture, pass/fail mode, runtime budget, artifact path
   - Legacy single-file specs: equivalent sections are present
3) Produce a short “Spec Gaps” list, then either:
   - Propose edits, or
   - Apply edits directly if the user asks.
4) End by recommending the next skill (usually `write-tests` or `implement-feature`).
