---
description: Debug failures with regression tests and documentation
argument-hint: FEATURE_ID=<F-0001> ERROR_OUTPUT="<paste>"
---

We are debugging feature $FEATURE_ID.

Inputs:
- Error output: $ERROR_OUTPUT

Do:
0) Ask clarifying questions before continuing, then follow the matching skill.
1) Reproduce the failure.
2) Minimize to the smallest cause.
3) Write a regression test (fails before fix).
4) Fix the bug.
5) Re-run tests.
6) Update the feature spec Debug Log.
