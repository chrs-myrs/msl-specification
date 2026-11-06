---
type: behavior
category: features
fidelity: behavioral
criticality: IMPORTANT
failure_mode: Without a governing spec, every tool change trips the spec-first gate and agents write duplicate specs beside the MSL tools spec that already governs these files
governed-by: []
satisfies:
  - specs/foundation/outcomes.spec.md
  - specs/foundation/constraints.spec.md
guided-by:
  - specs/strategy/architecture.spec.md
specifies:
  - tools/
  - tests/
---

# MSL Tools [MSL]

## Summary

Connects the spec-first gate to the MSL specs that already govern the optional validation tools and their tests.

## Requirements

- [!] Tool and test requirements live in the detailed MSL specs, not here
  - `specs/applications/msl-tools-spec.md` governs `tools/`
  - `specs/testing/msl-testing-framework.md` governs `tests/`
- [!] Tools stay optional: no MSL document needs them to be read or written
- [!] New tool or test requirements go into the detailed MSL spec, never into a new `*.spec.md`

## Validation

- Every file under the paths above is named by this spec's `specifies:`
- No `*.spec.md` repeats a requirement held in the detailed MSL specs
