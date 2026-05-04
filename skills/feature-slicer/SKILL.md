---
name: feature-slicer
description: Slice a large feature/stream item into small, shippable work item specs.
---

1) Read the target stream/work item from `spec/backlog.md` (or user text) plus `spec/brief.md`.
2) Produce 5–12 slices that are:
   - Vertically valuable (end-to-end)
   - Independently testable
   - Low-risk first (spikes/prototypes early only if needed)
3) Update `spec/backlog.md` with the new work item IDs and ordering.
   - Use work item ID format `S-<stream>-<nnn>` (example: `S-core-001`).
4) Update `spec/index.md` so Planned/In Progress lists reflect the slices.
5) Recommend running `feature-kickoff` for the first slice.
