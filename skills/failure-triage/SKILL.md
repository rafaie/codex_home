---
name: failure-triage
description: Triage many failures quickly and produce an efficient attack plan.
---

1) Collect failure output (CI logs, local run output, stack traces).
2) Cluster failures into groups by root signature.
3) Categorize each group:
   - Environment/setup
   - Dependency/version drift
   - Flaky/timing
   - Deterministic code defect
   - Test expectation mismatch
4) Produce an ordered plan:
   - Fix blockers first (env/setup)
   - Then highest-impact deterministic failures
   - Then flaky stabilization
5) For the first group, recommend the exact next skill:
   - `debug-loop` or `flaky-test-hunter`
