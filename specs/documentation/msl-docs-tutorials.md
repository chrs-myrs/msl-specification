---
msl: L1
id: msl-docs-tutorials
tags: [documentation, tutorials, hands-on]
priority: medium
status: active
references:
  - msl-docs-root: "Part of documentation system"
  - msl-l0-foundation: "Starting point for tutorials"
  - msl-l1-structure: "Intermediate tutorial topics"
  - msl-l2-advanced: "Advanced tutorial topics"
---

# MSL Tutorials Documentation Specification [MSL]

## Summary

This specification defines requirements for hands-on MSL tutorials that guide users through practical specification development scenarios with step-by-step instructions and progressive complexity.

## Requirements

### Tutorial Structure

- REQ-001: [!] [NEW] Each tutorial must solve a real-world problem
- REQ-002: [!] [NEW] Tutorials must be completeable in ≤30 minutes
- REQ-003: [NEW] Each tutorial must build on previous knowledge
- REQ-004: [NEW] Tutorials must include starter files if needed
- REQ-005: [NEW] Each step must be independently verifiable

### Tutorial Categories

- REQ-101: [!] [NEW] Must include "Your First MSL Specification" tutorial
- REQ-102: [NEW] Must include "Adding Validation" tutorial
- REQ-103: [NEW] Must include "Using Inheritance" tutorial
- REQ-104: [NEW] Must include "Creating Templates" tutorial
- REQ-105: [NEW] Must include "Building Specification Sets" tutorial

### Step Requirements

- REQ-201: [!] [NEW] Each step must have: objective, action, verification
- REQ-202: [NEW] Steps must be numbered and sequentially dependent
- REQ-203: [NEW] Each step must show expected output
- REQ-204: [NEW] Common errors must be addressed preemptively
- REQ-205: [NEW] Each step must advance toward final goal

### Learning Objectives

- REQ-301: [!] [NEW] Each tutorial must state exactly 3 learning objectives
- REQ-302: [NEW] Objectives must be measurable with pass/fail criteria
- REQ-303: [NEW] Tutorial must demonstrate achieving each objective with verification step
- REQ-304: [NEW] Summary must list all 3 objectives with completion checkmarks
- REQ-305: [NEW] Next steps must reference ≥2 objectives from current tutorial

### Code Examples

- REQ-401: [!] [NEW] All code must be complete and runnable
- REQ-402: [NEW] Code must follow MSL best practices defined in msl-usage-standards
- REQ-403: [NEW] Diff views must show changes with ≥3 lines context
- REQ-404: [NEW] Final code must be available as complete file ≤100 lines
- REQ-405: [NEW] Code must include 1 comment per 10 lines explaining key concepts

### Common Pitfalls Section

- REQ-501: [!] [NEW] Must highlight inheritance misuse with ≥3 examples
- REQ-502: [NEW] Must show correct vs incorrect patterns side-by-side
- REQ-503: [NEW] Must explain "is-a" test with ≥5 test questions
- REQ-504: [NEW] Must demonstrate using references with ≥2 examples
- REQ-505: [NEW] Must include ≥5 specific debugging tips for common errors

## Validation Criteria

Tutorial documentation is valid when:
- Each tutorial achieves stated objectives
- All code examples execute correctly
- Steps follow logical progression
- Common errors are addressed
- Completion time is ≤30 minutes

## Notes

Tutorials are the primary hands-on learning path for MSL. They must balance educational value with practical application, ensuring users gain confidence through successful completion.

---
*Specification format: [MSL Level 1](https://github.com/chrs-myrs/msl-specification)*