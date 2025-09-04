---
msl: L1
id: msl-docs-user-guide
tags: [documentation, user-guide, comprehensive]
priority: high
status: active
references:
  - msl-docs-root: "Part of documentation system"
  - msl-l0-foundation: "Basic level to document"
  - msl-l1-structure: "Structural features to document"
  - msl-l2-advanced: "Advanced features to document"
---

# MSL User Guide Documentation Specification [MSL]

## Summary

This specification defines requirements for comprehensive MSL user documentation covering all features, best practices, and common use cases for specification authors.

## Requirements

### Content Organization

- REQ-001: [!] [NEW] Guide must be organized by task, not by feature
- REQ-002: [!] [NEW] Each section must be self-contained with clear scope
- REQ-003: [NEW] Sections must follow user journey from basic to advanced
- REQ-004: [NEW] Each section must declare prerequisites explicitly
- REQ-005: [NEW] Cross-references must use consistent link format

### Core Topics Coverage

- REQ-101: [!] [NEW] Must cover writing first MSL specification
- REQ-102: [!] [NEW] Must explain all three MSL levels with use cases
- REQ-103: [!] [NEW] Must cover inheritance and extension patterns
- REQ-104: [NEW] Must explain validation and quality metrics
- REQ-105: [NEW] Must cover template usage and variables
- REQ-106: [NEW] Must explain markers and their semantics

### Best Practices

- REQ-201: [!] [NEW] Must include ≥2 "DO" and ≥2 "DON'T" examples per feature
- REQ-202: [NEW] Must provide ≥5 specification design patterns with use cases
- REQ-203: [NEW] Must explain MSL level selection with decision tree
- REQ-204: [NEW] Must specify naming: lowercase-kebab-case.md convention
- REQ-205: [NEW] Must include ≥10 common issues with solutions

### Examples and Scenarios

- REQ-301: [!] [NEW] Each feature must have ≥2 practical examples
- REQ-302: [NEW] Must include real-world case studies
- REQ-303: [NEW] Examples must show both specification and validation
- REQ-304: [NEW] Must include anti-patterns and their corrections
- REQ-305: [NEW] Examples must be drawn from different domains

### Accessibility

- REQ-401: [!] [NEW] Each topic must be readable in ≤15 minutes
- REQ-402: [NEW] Must support 3 learning styles: visual (diagrams), textual, practical (examples)
- REQ-403: [NEW] Must include glossary with ≥50 MSL terms defined
- REQ-404: [NEW] Must provide ≥3 one-page quick reference cards
- REQ-405: [NEW] Must provide 3 learning paths: beginner, intermediate, advanced

## Sub-Specifications

The user guide includes these detailed specifications:
- `msl-docs-writing.md` - Writing MSL specifications
- `msl-docs-validation.md` - Validation and quality assurance
- `msl-docs-inheritance.md` - Inheritance and templates

## Validation Criteria

User guide documentation is valid when:
- All MSL features are documented
- Each feature has working examples
- Best practices are actionable
- Navigation supports multiple paths
- Content is task-oriented

---
*Specification format: [MSL Level 2](https://github.com/chrs-myrs/msl-specification)*