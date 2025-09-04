---
msl: L1
id: msl-docs-getting-started
tags: [documentation, getting-started, quickstart]
priority: critical
status: active
references:
  - msl-docs-root: "Part of documentation system"
  - msl-l0-foundation: "First level to document"
---

# MSL Getting Started Documentation Specification [MSL]

## Summary

This specification defines requirements for MSL getting-started documentation that enables new users to understand MSL's value proposition and begin using it within 15 minutes.

## Requirements

### Content Structure

- REQ-001: [!] [NEW] Document must begin with 3-sentence MSL value proposition
- REQ-002: [!] [NEW] Document must include 5-minute quickstart section
- REQ-003: [!] [NEW] Document must provide complete "Hello World" MSL example
- REQ-004: [NEW] Document must list prerequisites and installation steps
- REQ-005: [NEW] Document must link to next learning resources

### Quickstart Requirements

- REQ-101: [!] [NEW] Quickstart must create first MSL spec in ≤10 steps
- REQ-102: [!] [NEW] Each step must be ≤2 sentences with example
- REQ-103: [NEW] Must cover L0 basics only (no advanced features)
- REQ-104: [NEW] Must include validation of created spec
- REQ-105: [NEW] Must show expected output for each step

### Examples Requirements

- REQ-201: [!] [NEW] Must include 3 progressive examples: simple, moderate, complex
- REQ-202: [NEW] Simple example must be ≤20 lines
- REQ-203: [NEW] Examples must be copy-pasteable and runnable
- REQ-204: [NEW] Each example must highlight different MSL feature
- REQ-205: [NEW] Examples must include comments explaining key concepts

### Navigation Requirements

- REQ-301: [!] [NEW] Must provide clear "What's Next?" section
- REQ-302: [NEW] Must link to user guide for comprehensive learning
- REQ-303: [NEW] Must link to reference for syntax details
- REQ-304: [NEW] Must link to tutorials for hands-on practice
- REQ-305: [NEW] Must include decision tree for choosing MSL level

### Accessibility Requirements

- REQ-401: [!] [NEW] Must be readable in 10 minutes
- REQ-402: [NEW] Must use zero undefined acronyms/jargon
- REQ-403: [NEW] Must include visual diagram of MSL levels
- REQ-404: [NEW] Code blocks must have syntax highlighting
- REQ-405: [NEW] Must work offline (no external dependencies)

## Validation Criteria

Getting-started documentation is valid when:
- New user can create first spec in ≤15 minutes
- All examples execute successfully
- No prerequisites beyond text editor
- Links to next resources are valid
- Readability score ≤ grade 10

## Notes

The getting-started guide is the primary entry point for new MSL users. It must balance brevity with completeness, providing just enough information to be productive without overwhelming newcomers.

---
*Specification format: [MSL Level 2](https://github.com/chrs-myrs/msl-specification)*