# SDLC Skill Pack for Codex (Spec‑Driven, Feature‑by‑Feature)

This package gives you a **feature‑level SDLC workflow** in Codex:
- start from an incomplete idea
- clarify via Q&A
- write/maintain **feature specs**
- implement **AC-by-AC**
- keep **tests / docs / ADRs / architecture** up to date
- repeat, feature by feature

It includes:
- `prompts/` (your lifecycle custom prompts — handy, but optional)
- `skills/` (the primary workflow engine; recommended)

---

## Folder layout

- `skills/<skill-name>/SKILL.md`  
  Each folder is one skill.
- `prompts/*.md`  
  Your original lifecycle prompts.
- `templates/`  
  Starter templates for `AGENTS.md`, `codex.toml`, `spec/index.md`, `spec/architecture.md`, feature spec & ADR templates.
- `repo_starter/`  
  A “copy‑into‑repo” starter that places everything in repo-friendly locations (including `.codex/skills`).

---

## How to invoke skills

**Best practice:** invoke skills explicitly so Codex loads the skill instructions.

In Codex CLI / IDE:
- Type: `$qa-intake` or `$feature-kickoff` (etc.)
- Or use: `/skills` and select the skill

Then write your request underneath.

Example:
```text
$qa-intake
I want to add a new metric module that computes accuracy and F1 for TOMI. Ask me the minimum questions and produce a brief.
```

---

## Recommended “feature-by-feature” SDLC loop

For each feature:

1) **Clarify**: `$qa-intake`  
2) **Spec**: `$feature-kickoff` (creates/updates `spec/features/F-XXXX-*.md`)  
3) **Test strategy**: `$test-plan` (writes a test matrix into the spec)  
4) **Tests**: `$write-tests` (AC → tests, traceable to feature ID)  
5) **Implement**: `$implement-feature` (AC-by-AC; run checks)  
6) **Debug if needed**: `$debug-loop` (repro → regression test → fix → verify → document)  
7) **Decisions**: `$adr-review` (create/update ADRs, link from the feature spec)  
8) **Docs**: `$docs-update` + `$docs-index-refresh`  
9) **Closeout**: `$feature-closeout` (enforces “definition of done”)

Use `$release-prep` when you’re cutting a release (not necessarily per feature).

---

## Skill catalog (what each one does)

### Start / orientation
- **`session-start`**  
  Reads `AGENTS.md`, `codex.toml`, and key specs (like `spec/index.md`) and summarizes repo state + suggests the next best features.

### Idea → backlog
- **`project-intake`**  
  Turns your “project idea” doc into a crisp **Project Brief** and initializes `spec/index.md` as a living map.
- **`backlog-builder`**  
  Converts the brief into a backlog (`spec/backlog.md`) with epics, feature IDs, dependencies, and suggested ordering.
- **`feature-slicer`**  
  Breaks big epics into small, shippable “one‑PR” features.

### Q&A + spec quality
- **`qa-intake`**  
  Asks clarifying questions first, then outputs a structured brief and recommends the next skill.
- **`spec-linter`**  
  Checks a feature spec for completeness: testable AC, edge cases, non‑goals, dependencies, risks.

### Tests + debugging
- **`test-plan`**  
  Converts AC into a test matrix (unit/integration/e2e) and writes it into the feature spec.
- **`test-runner`**  
  Runs the right checks (lint/type/test) and summarizes failures into actionable buckets.
- **`failure-triage`**  
  When many tests fail: clusters issues (env vs flaky vs code) and provides an efficient attack plan.
- **`flaky-test-hunter`**  
  Stabilizes flaky tests (seeds, timeouts, isolation, hermetic fixtures).
- **`debug-loop`**  
  The disciplined debug workflow: repro → minimize → regression test → fix → verify → document.

### Implementation + documentation
- **`feature-kickoff`**  
  Creates the feature spec file and initial plan; triggers ADR creation when the feature involves a significant decision.
- **`implement-feature`**  
  Implements AC-by-AC, keeps changes small, runs tests, and updates the feature’s implementation log.
- **`docs-update`**  
  Updates user-facing docs, README, changelog entries, and links back to the feature.
- **`docs-index-refresh`**  
  Keeps `spec/index.md` accurate as a *living navigation hub* (not “complete”, just correct).

### Architecture + ADR hygiene
- **`adr-review`**  
  Creates/updates ADRs when decisions change, links ADRs from the feature spec, and keeps decision records aligned with reality.
- **`architecture-updater`**  
  Updates `spec/architecture.md` so architecture stays consistent with ADRs and implementation.

### Closeout + release
- **`feature-closeout`**  
  Runs a final feature checklist: tests green, spec/index updated, ADR linked (if needed), spec updated, ready to merge.
- **`release-prep`**  
  Runs final checks, compiles release notes, and updates changelog for a release.

---

## Examples

### Example A — from idea doc to first implemented feature
1) Put your idea in `spec/idea.md` (can be messy; bullet points are fine).
2) Run:
```text
$project-intake
Use spec/idea.md. Create spec/brief.md and initialize spec/index.md.
```
3) Build backlog:
```text
$backlog-builder
Use spec/brief.md. Create/update spec/backlog.md with 5–15 small features.
```
4) Pick the top feature (e.g., `F-0001`) and clarify:
```text
$qa-intake
Feature F-0001: implement a dataset loader for TOMI with cleaning and a simple CLI entrypoint.
```
5) Create the spec:
```text
$feature-kickoff
Feature ID: F-0001
Title: TOMI dataset loader + cleaning
Use the brief above and write the spec.
```
6) Plan tests:
```text
$test-plan
For F-0001, add a test matrix into the spec and propose minimal fixtures.
```
7) Generate tests:
```text
$write-tests
For F-0001, write tests that map to each acceptance criterion.
```
8) Implement:
```text
$implement-feature
Implement F-0001 AC-by-AC. Run tests as you go.
```
9) If something breaks:
```text
$debug-loop
Here is the failing test output: <paste>
```
10) Update docs and index:
```text
$docs-update
Update README and spec pages for F-0001 and add a changelog entry.
```
```text
$docs-index-refresh
Update spec/index.md to link F-0001 spec, spec pages, and any ADRs.
```

### Example B — when a decision changes (ADR)
```text
$adr-review
Feature F-0003 introduced a decision about storage format (JSONL vs Parquet). Create/update an ADR and link it from the feature spec.
```

### Example C — large failure burst
```text
$failure-triage
Here are the failing tests from CI: <paste>
```
Then follow with `$debug-loop` on the top cluster.

---

## Make the skills “feel native” to your repo

### 1) Use `AGENTS.md` for guardrails
Put your coding standards, test commands, folder conventions, and “definition of done” in `AGENTS.md`.
Codex will apply it automatically at session start.

### 2) Use `codex.toml` for commands
If your repo’s commands differ (e.g., not `uv`/`pytest`), put your canonical lint/test/typecheck commands in `codex.toml` so skills stay correct.

---

## Troubleshooting

- **Skill not found:** ensure the skill is under `~/.codex/skills/<name>/SKILL.md` (home) or `.codex/skills/<name>/SKILL.md` (repo).
- **Skill didn’t follow the workflow:** invoke it explicitly (`$skill-name`) so Codex loads the full instructions.
- **Spec/index feels “behind”:** treat it as a navigation page. Run `$docs-index-refresh` after each feature.

---

## Quick reference

Most common:
- `$qa-intake`
- `$feature-kickoff`
- `$test-plan`
- `$write-tests`
- `$implement-feature`
- `$debug-loop`
- `$adr-review`
- `$docs-update`
- `$docs-index-refresh`
- `$feature-closeout`
- `$release-prep`
