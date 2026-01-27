---
name: feature-slicer
description: Slice a large feature/epic into small, shippable feature specs.
---

1) Read the target epic/feature from `spec/backlog.md` (or user text) plus `docs/brief.md`.
2) Produce 5–12 slices that are:
   - Vertically valuable (end-to-end)
   - Independently testable
   - Low-risk first (spikes/prototypes early only if needed)
3) Update `spec/backlog.md` with the new feature IDs and ordering.
4) Update `docs/index.md` so Planned/In Progress lists reflect the slices.
5) Recommend running `feature-kickoff` for the first slice.
