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
  - specs/interfaces/ - API/data contracts, including the MSL language levels and `standards/`
  - specs/artifacts/ - agents, commands and validators
  - specs/workspace/metaspecs/ - MSL metaspecs governing this repository's own specs; plain `.md`, because MSL's `type: metaspec` is not a LiveSpec type (registries/decisions.md, DEC-001)
  - A script's spec sits beside the script as `<script>.spec.md`
  - `specs/msl-l0-foundation.md`, `msl-l1-structure.md` and `msl-l2-advanced.md` are pointers kept at published paths, not specs

- [!] Files outside every spec's `specifies:` by choice
  - PURPOSE.md, CHANGELOG.md, LICENSE, .gitignore, project.yaml and `registries/`

## Validation
- Files placed in correct folders
- No ambiguous file locations
