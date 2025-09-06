---
msl: L1
id: msl-docs-tutorials
extends: msl-docs-base
tags: [documentation, tutorials, hands-on]
priority: medium
status: active
governed-by: msl-documentation-metaspec
references:
  - msl-l0-foundation: "Starting point for tutorials"
  - msl-l1-structure: "Intermediate tutorial topics"
  - msl-l2-advanced: "Advanced tutorial topics"
---

# MSL Tutorials Documentation Specification [MSL]

## Summary

This specification defines requirements for hands-on MSL tutorials that guide users through practical specification development scenarios with step-by-step instructions.

## Requirements

### Hands-On Focus

- REQ-001: [!] Each tutorial MUST solve a real-world problem
- REQ-002: [!] Tutorials MUST be practical and completeable
- REQ-003: Tutorials MUST build on previous knowledge progressively

### Core Tutorial Topics

- REQ-101: [!] MUST include [→ tutorial for writing first MSL specification](tutorials/first-spec.md)
- REQ-102: MUST include tutorials for key MSL features:
  - [→ Validation tutorial](tutorials/validation.md)
  - [→ Inheritance tutorial](tutorials/inheritance.md)
  - [→ Templates tutorial](tutorials/templates.md)
- REQ-103: MUST cover [→ building complete specification sets](tutorials/specification-sets.md)

### Step-by-Step Guidance

- REQ-201: [!] Each step MUST have clear objective and verification
- REQ-202: Steps MUST be sequential and build toward final goal
- REQ-203: Common errors MUST be addressed proactively

### Learning Objectives

- REQ-301: [!] Each tutorial MUST state clear learning objectives
- REQ-302: Objectives MUST be measurable and achievable
- REQ-303: Tutorial MUST demonstrate achieving stated objectives

### Inheritance Pitfalls

- REQ-401: [!] MUST highlight common inheritance misuse patterns
- REQ-402: MUST explain the "is-a" relationship test
- REQ-403: MUST show correct usage of `references:` vs `extends:`

## Validation Criteria

Tutorial documentation is valid when:
- Tutorials achieve their learning objectives
- Steps build logically toward the goal
- Common pitfalls are addressed
- Users gain practical skills

## Notes

Tutorials are the primary hands-on learning path for MSL. They must balance educational value with practical application, ensuring users gain confidence through successful completion. This specification inherits common documentation requirements from msl-docs-base and focuses on the unique aspects of hands-on tutorial documentation.

---
*Specification format: [MSL Level 1](https://github.com/chrs-myrs/msl-specification)*