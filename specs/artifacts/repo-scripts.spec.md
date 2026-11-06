---
type: command
category: artifacts
fidelity: behavioral
criticality: IMPORTANT
failure_mode: Without a governing spec, every script change trips the spec-first gate even though each script already has its own MSL spec
governed-by: []
satisfies:
  - specs/foundation/outcomes.spec.md
specifies:
  - scripts/run_tests.sh
  - scripts/cleanup_tests_for_pytest.py
---

# Repository Scripts [MSL]

## Summary

Connects the spec-first gate to the MSL specs that sit beside this repository's own scripts.

## Requirements

- [!] Script requirements live in each script's MSL spec, not here
  - `scripts/run_tests-msl-spec.md` governs `scripts/run_tests.sh`
  - `scripts/cleanup_tests_for_pytest-msl-spec.md` governs `scripts/cleanup_tests_for_pytest.py`
- [!] Validators vendored into `scripts/livespec/` are governed upstream by LiveSpec and are not specified here
- [!] A new script gets its own MSL spec beside it and an entry in this spec's `specifies:`

## Validation

- Every project-authored script under `scripts/` is named by this spec's `specifies:`
- Each named script has an MSL spec beside it
