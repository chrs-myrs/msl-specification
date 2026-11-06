---
type: taxonomy
category: workspace
fidelity: process
criticality: IMPORTANT
failure_mode: Incorrect folder organization without taxonomy
governed-by: []
applies_to:
  - this_project
derives-from:
  - PURPOSE.md
---

# Project Taxonomy [MSL]

## Requirements

- [!] Project classified by domain
  - Domain: software
  - Specs boundary: specifications_only

- [!] Folder organization follows domain
  - specs/foundation/ - outcomes and constraints
  - specs/strategy/ - architectural decisions
  - specs/features/ - observable behaviors
  - specs/interfaces/ - API/data contracts
  - specs/artifacts/ - agents, commands and validators
  - MSL's own specs keep their published layout (`specs/msl-l*.md`, `applications/`, `documentation/`, `standards/`, `metaspecs/`, `testing/`, `context7-optimization/`) until their rename (registries/debt.md, DEBT-001)

## Validation
- Files placed in correct folders
- No ambiguous file locations
