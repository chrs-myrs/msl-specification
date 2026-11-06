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

# Project Taxonomy

## Requirements

- [!] Project classified by domain
  - Domain: software
  - Specs boundary: specifications_only

- [!] Folder organization follows domain
  - specs/foundation/ - outcomes and constraints
  - specs/strategy/ - architectural decisions
  - specs/features/ - observable behaviors
  - specs/interfaces/ - API/data contracts

## Validation
- Files placed in correct folders
- No ambiguous file locations
