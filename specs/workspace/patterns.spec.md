---
type: workspace
category: workspace
fidelity: process
criticality: IMPORTANT
failure_mode: Without these rules, specs drift from the docs, agents and tools they govern, and the repository meant to exemplify MSL falls below the bar it sets for others
governed-by: []
applies_to:
  - this_project
derives-from:
  - PURPOSE.md
---

# Repository Patterns [MSL]

## Summary

Working rules for the MSL specification repository, which must exemplify the standards it defines.

## Requirements

- [!] Specifications and what they govern change together
  - A spec names every file it governs in its `specifies:`
  - Documentation specs (`specs/features/documentation/`, `specs/features/context7-optimization/`) with `docs/`, `llms.txt`, README and `examples/`
  - Agent specs (`specs/artifacts/`) with `.claude/agents/`
  - Tools spec (`specs/features/msl-tools.spec.md`) with `tools/`; testing framework spec (`specs/features/testing/`) with `tests/`
  - A script's spec sits beside it as `<script>.spec.md`

- [!] Specifications meet the quality bar before commit
  - Validation score of 80/100 or more (msl-validator per spec, msl-batch-validator for integration)
  - At least 90% of requirements testable
  - Under 20% duplication; at most 4 inheritance levels
  - Every specification title ends with `[MSL]`
    - Except conventions vendored from LiveSpec (`specs/workspace/standards/`), which stay as shipped

- [!] `extends` is used only for a true "is-a" relationship in which every parent requirement applies
  - Never `extends: msl-l2-advanced` unless defining a new MSL level
  - `msl: L1` or `msl: L2` declares the features used; `references:` covers other relationships

- [!] Specifications start at the lowest MSL level that meets the need

- [!] User documentation stays conservative
  - Consolidate, simplify or remove before adding
  - Serve the common case; advanced topics such as metaspecs go to appendices

- [!] The pre-push completeness checker runs before any push

## Validation

- A change to a spec or its counterpart updates both sides
- Modified specs score 80 or more and carry `[MSL]` in their titles
- No `extends` without an is-a relationship
- New user documentation simplifies or replaces before it adds
