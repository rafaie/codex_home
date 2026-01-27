---
name: architecture-updater
description: Keep high-level architecture docs/diagrams aligned with the evolving codebase.
---

1) Read `docs/architecture.md` (if present), `docs/index.md`, and recent ADRs under `spec/decisions/`.
2) Update/create `docs/architecture.md` with:
   - Components (bulleted)
   - Data flow (steps)
   - External dependencies
   - Key interfaces/contracts (links)
   - “What changed recently” (short changelog)
3) If useful, add/update a diagram under `docs/diagrams/` (e.g., Mermaid).
4) Ensure `docs/index.md` links to architecture and the latest ADRs.
