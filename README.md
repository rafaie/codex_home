# SDLC Skill Pack for Codex (Spec-Driven, Work-Item-by-Work-Item)

This package provides a work item level SDLC workflow for Codex:
- clarify requirements with lightweight intake
- create and maintain work item documentation folders
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

## Recommended work item workflow

For a brand-new project repo:

1) **Bootstrap + brief**: `$project-intake`
2) **Backlog**: `$backlog-builder`
3) **First work item docs**: `$feature-kickoff <work-id>`

`$project-intake` bootstraps missing SDLC starter files into the target repo:
- `AGENTS.md`
- `codex.toml`
- `spec/templates/*`
- `spec/smoke.md`
- `spec/smoke_registry.yaml`
- `spec/docstrings.md`
- `scripts/smoke.py`
- `spec/brief.md`
- `spec/index.md`

It does not overwrite existing repo-local files unless explicitly asked.

For each work item (default path):

1) **Clarify**: `$qa-intake`
2) **Docs**: `$feature-kickoff`
3) **Implementation phase**: `$implementation-phase`
4) **Debug if needed**: `$debug-loop`
5) **Ship endgame (one command)**: `$ship-feature`

`$implementation-phase <work-id>` orchestrates `$test-plan`, `$write-tests`, and `$implement-feature`.

`$ship-feature` runs full checks + smoke + ADR/docs/index updates and emits a readiness summary with evidence paths.

Compatibility path for repos that have not adopted `$ship-feature` yet:
- Use `$feature-closeout` as the final work item step instead of `$ship-feature`.

Use `$release-prep` for release-level work across work items.

---

## Smoke-first workflow rules

- Smoke is required for runnable-path work items (CLI/module/script).
- Smoke executes the real entrypoint through subprocess.
- Smoke must produce evidence artifacts under `artifacts/smoke/...`:
  - `summary.json`
  - `cases/<case_id>.json`
  - `stdout.txt`
  - `stderr.txt`
  - `timing.json`
- Smoke mode is **live-first** when credentials are present, with offline fallback.
- Scenario `mode`/`run_profile` filters must prevent offline fallback from running live-only scenarios.
- Smoke budget controls should be enforced (`--time-budget-sec`, `--max-requests`) and reported as `budget_exceeded` when limits are hit.

### Smoke harness starter expectations (`templates/smoke.py`)
- Uses live-first mode by default when credentials are available.
- Applies budget precedence as CLI override → selected scenario budget → harness default.
- Reports command, artifact path, selected scenarios, fixtures, provider stats, and budget telemetry in `summary.json`.
- Fails closed on output validation (`parse_error`, `schema_error`, `invariant_error`) instead of treating successful subprocess execution as a pass.

---

## Command contract (`codex.toml`)

Skills look for these keys under `[commands]`:
- `test` (legacy compatibility)
- `test_quick`
- `test_full`
- `lint`
- `format`
- `typecheck`
- `docstrings` (optional)
- `smoke`

Starter example: `templates/codex.toml`.

## Work item document layout

New work items use stream/sequence IDs and a folder-based documentation layout:

- ID format: `S-<stream>-<nnn>` (example: `S-core-001`)
- Folder: `spec/features/<work-id>-<slug>/`
- Required docs: `feature.md`, `implementation.md`, `test-plan.md`, `test-results.md`, `status.md`
- Evidence index: `evidence/README.md`

## Python docstring standard

Downstream Python projects should use Google-style docstrings where they improve maintainability:
- Public modules, classes, functions, and methods
- CLI entrypoints and command handlers
- Data models, schemas, provider/client wrappers, and integration boundaries
- Non-trivial private helpers
- Shared test fixtures/helpers

Avoid docstrings that only repeat the symbol name. Starter policy: `templates/docstrings.md`.

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
- `implementation-phase` (orchestrates `test-plan` -> `write-tests` -> `implement-feature`)
- `implement-feature`
- `ship-feature`
- `feature-closeout`
- `docs-update`
- `docs-index-refresh`

### Architecture and release
- `adr-review`
- `architecture-updater`
- `release-prep` (format/lint -> typecheck -> full tests -> smoke)

---

## Quick reference

Most common:
- `$project-intake`
- `$backlog-builder`
- `$qa-intake`
- `$feature-kickoff`
- `$implementation-phase`
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
