---
name: adr-review
description: Ensure architectural decisions are recorded and linked (create/update ADRs) at feature level.
---

1) Read the target feature spec `spec/features/<feature-id>-<slug>.md` and any related code changes (diff).
   - `<feature-id>` must use `F<epic>.<feature>` (example: `F1.1`).
2) Decide if any of these happened:
   - A major design choice was made/changed (architecture, data model, interfaces, metrics)
   - A tradeoff was chosen (perf vs cost vs correctness)
   - A new dependency/technology was introduced
3) If yes, create or update an ADR under `spec/decisions/`:
   - Prefer `spec/templates/adr.md` if present.
   - Use a concise format: Context, Decision, Alternatives, Consequences, Links.
4) Ensure the feature spec links to the ADR(s) in a “Decisions/ADRs” section.
5) End by recommending `docs-index-refresh` or `docs-update`.
