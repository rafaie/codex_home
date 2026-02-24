# SDLC Skill Pack for Codex (Spec-Driven, Feature-by-Feature)

This package provides a feature-level SDLC workflow for Codex:
- clarify requirements with lightweight intake
- create and maintain feature specs
- implement AC-by-AC with a fast inner loop
- enforce real smoke evidence before shipping
- keep docs and ADRs aligned

It includes:
- `prompts/` (optional lifecycle prompts)
- `skills/` (primary workflow engine)
- `templates/` (starter files for downstream repos)

---

## Folder layout

- `skills/<skill-name>/SKILL.md`
- `prompts/*.md`
- `templates/`

---

## How to invoke skills

In Codex CLI / IDE:
- Type `$<skill-name>` (for example `$qa-intake`, `$implement-feature`)
- Or use `/skills` and select a skill

---

## Recommended feature workflow (hard cutover)

For each feature:

1) **Clarify**: `$qa-intake`
2) **Spec**: `$feature-kickoff`
3) **Test strategy**: `$test-plan`
4) **Tests**: `$write-tests`
5) **Implement (fast loop)**: `$implement-feature`
6) **Debug if needed**: `$debug-loop`
7) **Ship endgame (one command)**: `$ship-feature`

`$ship-feature` runs full checks + smoke + ADR/docs/index updates and emits a readiness summary with evidence paths.

Use `$release-prep` for release-level work across features.

---

## Smoke-first workflow rules

- Smoke is required for runnable paths (CLI/module/script features).
- Smoke executes the real entrypoint through subprocess.
- Smoke must produce evidence artifacts under `artifacts/smoke/...`:
  - `summary.json`
  - `cases/<case_id>.json`
  - `stdout.txt`
  - `stderr.txt`
  - `timing.json`
- Smoke mode is **live-first** when credentials are present, with offline fallback.

---

## Command contract (`codex.toml`)

Skills look for these keys under `[commands]`:
- `test` (legacy compatibility)
- `test_quick`
- `test_full`
- `lint`
- `format`
- `typecheck`
- `smoke`

Starter example: `templates/codex.toml`.

---

## Skill catalog (high-level)

### Intake and planning
- `session-start`
- `project-intake`
- `backlog-builder`
- `feature-slicer`
- `qa-intake`
- `spec-linter`

### Testing and debugging
- `test-plan`
- `write-tests`
- `test-runner` (quick/full + smoke)
- `smoke-test`
- `failure-triage`
- `flaky-test-hunter`
- `debug-loop`

### Implementation and docs
- `feature-kickoff`
- `implement-feature`
- `ship-feature`
- `feature-closeout`
- `docs-update`
- `docs-index-refresh`

### Architecture and release
- `adr-review`
- `architecture-updater`
- `release-prep`

---

## Quick reference

Most common:
- `$qa-intake`
- `$feature-kickoff`
- `$test-plan`
- `$write-tests`
- `$implement-feature`
- `$test-runner`
- `$smoke-test`
- `$ship-feature`
- `$debug-loop`
- `$adr-review`
- `$docs-update`
- `$docs-index-refresh`
- `$release-prep`
