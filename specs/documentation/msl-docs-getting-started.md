---
msl: L1
id: msl-docs-getting-started
extends: msl-docs-base
tags: [documentation, getting-started, quickstart]
priority: critical
status: active
governed-by: msl-documentation-metaspec
references:
  - msl-l0-foundation: "First level to document"
---

# MSL Getting Started Documentation Specification [MSL]

## Summary

This specification defines requirements for MSL getting-started documentation that enables new users to understand MSL's value proposition and begin using it quickly with minimal friction.

## Requirements

### Quick Start Focus

- REQ-001: [!] Document MUST begin with clear MSL value proposition
- REQ-002: [!] Document MUST include [→ quickstart section](docs/getting-started.md) that gets users productive fast
- REQ-003: [!] Document MUST provide a complete "Hello World" MSL example
- REQ-004: Document MUST clearly state any prerequisites
- REQ-005: Document SHOULD be completable in under 15 minutes

### Progressive Learning Path

- REQ-101: [!] Examples MUST progress from simple to complex
- REQ-102: Initial example MUST use only L0 features
- REQ-103: Each example MUST build on previous knowledge
- REQ-104: Examples MUST include validation steps

### Next Steps Guidance

- REQ-201: [!] Document MUST include clear "What's Next?" section
- REQ-202: Document MUST help users choose appropriate MSL level
- REQ-203: Document MUST link to relevant learning resources

## Validation Criteria

Getting-started documentation is valid when:
- New users can create their first spec quickly
- Examples work as shown
- Learning path is clear
- Value proposition resonates

## Notes

The getting-started guide is the primary entry point for new MSL users. It must balance brevity with completeness, providing just enough information to be productive without overwhelming newcomers. This specification inherits common documentation requirements from msl-docs-base and adds only the unique aspects of introductory documentation.

---
*Specification format: [MSL Level 2](https://github.com/chrs-myrs/msl-specification)*