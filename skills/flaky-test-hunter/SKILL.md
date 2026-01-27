---
name: flaky-test-hunter
description: Identify and stabilize flaky tests (seeds, time, isolation) without hiding failures.
---

1) Re-run the failing test(s) multiple times (and/or with randomized order if supported).
2) Determine the flake type: time, concurrency, ordering, shared state, external dependency.
3) Stabilize by:
   - Removing shared mutable state
   - Using deterministic seeds/time control
   - Hermetic fixtures/test doubles
   - Reducing reliance on network/timeouts
4) Add a regression test or harness that reproduces the flake deterministically if possible.
5) Re-run the relevant suite and document the root cause + fix in the feature spec Debug log.
