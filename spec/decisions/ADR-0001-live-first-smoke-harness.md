# ADR-0001: Live-First Smoke Harness and One-Command Ship Flow

## Context
The global Codex skill pack previously emphasized unit/lint/type checks but did not enforce a real end-to-end smoke contract as a first-class gate. This allowed packaging/runtime/entrypoint issues to escape the inner loop and made ship readiness less legible.

## Decision
Adopt a hard-cutover workflow with:
- quick checks during implementation (`test_quick`) and full checks at milestone/endgame (`test_full`)
- required smoke evidence for runnable paths
- live-first smoke mode when credentials exist, with offline fallback
- required smoke artifact contract (`summary.json`, `cases/*.json`, `stdout.txt`, `stderr.txt`, `timing.json`)
- a single composite endgame skill (`ship-feature`) to standardize final checks and evidence capture

## Alternatives considered
1) Keep existing closeout flow and make smoke optional.
- Rejected: inconsistent runtime confidence and missing evidence bundles.

2) Offline-first smoke by default.
- Rejected: weaker confidence for live provider integrations and drift detection.

3) Keep endgame split across multiple manual skill invocations.
- Rejected: higher operator overhead and easier to miss required steps.

## Consequences
- Stronger confidence in runnable-path readiness.
- Faster AC-level implementation loop with explicit milestone gates.
- Slightly higher up-front discipline due to mandatory smoke planning and evidence logging.
- Requires downstream repos to adopt smoke harness scaffolding for best results.

## Links
- `/Users/mostafa/.codex/README.md`
- `/Users/mostafa/.codex/spec/changelog.md`
- `/Users/mostafa/.codex/skills/smoke-test/SKILL.md`
- `/Users/mostafa/.codex/skills/ship-feature/SKILL.md`
