---
type: behavior
category: features
fidelity: behavioral
criticality: IMPORTANT
failure_mode: Without a governing spec, every documentation change trips the spec-first gate and agents write duplicate specs beside the MSL documentation specs that already govern these files
governed-by: []
satisfies:
  - specs/foundation/outcomes.spec.md
guided-by:
  - specs/strategy/philosophy.spec.md
specifies:
  - docs/
  - examples/
  - README.md
  - CONTRIBUTING.md
  - llms.txt
---

# MSL Documentation [MSL]

## Summary

Connects the spec-first gate to the MSL specs that already govern this repository's documentation.

## Requirements

- [!] Documentation requirements live in the detailed MSL specs, not here
  - `specs/documentation/` governs the guides, tutorials and reference in `docs/`
  - `specs/context7-optimization/msl-llms-txt-spec.md` governs `llms.txt`
  - `specs/context7-optimization/msl-implementation-reference-spec.md` governs `docs/implementation-reference.md`
  - `docs/agent-guide.md` is itself an MSL document; its own Requirements section governs it
- [!] Files with no detailed spec (`README.md`, `CONTRIBUTING.md`, `examples/`) follow the conservative documentation rule in `specs/workspace/patterns.spec.md`, and examples stay valid MSL at the level they demonstrate
- [!] New documentation requirements go into the detailed MSL spec, never into a new `*.spec.md`

## Validation

- Every file under the paths above is named by this spec's `specifies:`
- No `*.spec.md` repeats a requirement held in the detailed MSL specs
