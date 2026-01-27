---
name: qa-intake
description: Ask clarifying questions, then produce a structured brief and recommend the next SDLC skill to run.
---

1) Restate the request in one sentence.
2) Ask only the minimum clarifying questions needed (typically 5–9). Do NOT implement anything yet.
   - Goal/outcome
   - Acceptance criteria / examples of success
   - Inputs/outputs (files, formats, APIs, datasets)
   - Constraints (time, tools, language, “must not”)
   - Priority tradeoff (correctness vs speed vs cost)
   - Edge cases / non-goals (if relevant)
3) After the user answers, produce:

## Brief
- Goal:
- Context:
- Acceptance criteria:
- Constraints:
- Inputs:
- Outputs:
- Risks/unknowns:
- Plan (3–7 steps):

## Next skill
Recommend ONE of:
- feature-kickoff
- implement-feature
- write-tests
- test-plan
- debug-loop
- docs-update
- adr-review
- architecture-updater
- release-prep
…and show the exact command the user should run next.
