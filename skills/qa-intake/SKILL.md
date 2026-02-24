---
name: qa-intake
description: Ask clarifying questions, then produce a structured brief and recommend the next SDLC skill to run.
---

1) Ground in repo context before asking questions.
   - Read `AGENTS.md`, `codex.toml` (if present), and relevant backlog/feature specs.
   - Do not ask for details already defined in repo docs; confirm defaults instead.
2) Restate the request in one sentence.
3) Ask only the minimum clarifying questions needed (typically 5–9). Do NOT implement yet.
   - Goal/outcome
   - Acceptance criteria / examples of success
   - Inputs/outputs (files, formats, APIs, datasets)
   - Constraints (time, tools, language, "must not")
   - Priority tradeoff (correctness vs speed vs cost)
   - Edge cases / non-goals (if relevant)
4) If the request touches a runnable script/CLI/module, ask smoke-contract questions.
   - Real entrypoint command (exact invocation)
   - Smoke fixture path(s) and what they represent
   - Pass/fail mode (schema + invariants only, or schema + invariants + golden)
   - Runtime constraints (time budget, network policy, required env vars)
   - Artifact locations (`artifacts/smoke/...`)
5) After the user answers, produce:

## Brief
- Goal:
- Context:
- Acceptance criteria:
- Constraints:
- Inputs:
- Outputs:
- Risks/unknowns:
- Verification & evidence:
  - Unit/integration coverage:
  - Smoke contract (entrypoint, fixture, pass/fail):
  - Required artifact paths:
- Plan (3–7 steps):

## Next skill
Recommend ONE of:
- feature-kickoff
- implement-feature
- write-tests
- test-plan
- test-runner
- smoke-test
- ship-feature
- feature-closeout
- docs-index-refresh
- debug-loop
- docs-update
- adr-review
- architecture-updater
- release-prep

...and show the exact command the user should run next.
