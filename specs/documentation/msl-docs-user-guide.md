---
msl: L1
id: msl-docs-user-guide
extends: msl-docs-base
tags: [documentation, user-guide, comprehensive]
priority: high
status: active
governed-by: msl-documentation-metaspec
references:
  - msl-l0-foundation: "Basic level to document"
  - msl-l1-structure: "Structural features to document"
  - msl-l2-advanced: "Advanced features to document"
---

# MSL User Guide Documentation Specification [MSL]

## Summary

This specification defines requirements for comprehensive MSL user documentation covering all features, best practices, and common use cases for specification authors.

## Requirements

### Task-Oriented Organization

- REQ-001: [!] [→ Guide](docs/user-guide.md) MUST be organized by user tasks, not features
- REQ-002: [!] Content MUST follow natural user journey from basic to advanced
- REQ-003: Each section MUST be self-contained with clear scope

### Core Topics Coverage

- REQ-101: [!] MUST cover all three MSL levels (L0, L1, L2) with use cases
- REQ-102: [!] MUST explain inheritance and the "is-a" relationship requirement
- REQ-103: [!] MUST cover validation and quality metrics
- REQ-104: MUST explain markers, templates, and other L2 features
- REQ-105: MUST introduce metaspecs and their governance role

### Best Practices and Patterns

- REQ-201: [!] MUST include DO and DON'T examples for key features
- REQ-202: MUST provide specification design patterns
- REQ-203: MUST explain MSL level selection criteria
- REQ-204: MUST include common issues and solutions

### Multiple Learning Paths

- REQ-301: [!] MUST support different user expertise levels
- REQ-302: MUST include practical examples from various domains
- REQ-303: MUST provide glossary of MSL terminology

## Validation Criteria

User guide documentation is valid when:
- All MSL features are documented comprehensively
- Best practices are clear and actionable
- Multiple learning paths are supported
- Content helps users accomplish real tasks

## Notes

The user guide provides comprehensive coverage of MSL for users who need more than a quick start. It inherits common documentation requirements from msl-docs-base and focuses on the unique aspects of comprehensive, task-oriented documentation.

---
*Specification format: [MSL Level 1](https://github.com/chrs-myrs/msl-specification)*