---
name: adr-review
description: Ensure architectural decisions are recorded and linked (create/update ADRs) at work item level.
---

1) Read the target work item folder `spec/features/<work-id>-<slug>/` and any related code changes (diff).
   - For new work, `<work-id>` must use `S-<stream>-<nnn>` (example: `S-core-001`).
   - For legacy single-file specs, read the matching file under `spec/features/`.
2) Decide if any of these happened:
   - A major design choice was made/changed (architecture, data model, interfaces, metrics)
   - A tradeoff was chosen (perf vs cost vs correctness)
   - A new dependency/technology was introduced
3) If yes, create or update an ADR under `spec/decisions/`:
   - Prefer `spec/templates/adr.md` if present.
   - Use a concise format: Context, Decision, Alternatives, Consequences, Links.
4) Ensure `feature.md` (or the legacy single-file spec) links to the ADR(s) in a “Decisions/ADRs” section.
5) End by recommending `docs-index-refresh` or `docs-update`.
