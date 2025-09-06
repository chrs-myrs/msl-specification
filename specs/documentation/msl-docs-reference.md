---
msl: L1
id: msl-docs-reference
extends: msl-docs-base
tags: [documentation, reference, technical]
priority: high
status: active
governed-by: msl-documentation-metaspec
references:
  - msl-l2-advanced: "Complete language to document"
---

# MSL Reference Documentation Specification [MSL]

## Summary

This specification defines requirements for MSL technical reference documentation providing comprehensive, searchable information about every language feature, syntax element, and semantic rule.

## Requirements

### Comprehensive Coverage

- REQ-001: [!] [→ Reference](docs/reference.md) MUST document all MSL syntax elements and features
- REQ-002: [!] MUST document all markers, frontmatter fields, and validation rules
- REQ-003: MUST include complete inheritance and governance rules
- REQ-004: MUST document error messages with solutions

### Consistent Structure

- REQ-101: [!] Reference MUST be organized for easy lookup (alphabetical/categorical)
- REQ-102: [!] Each entry MUST follow a consistent template
- REQ-103: Each entry MUST include syntax, description, and examples
- REQ-104: Each entry MUST specify its MSL level (L0/L1/L2)

### Search and Navigation

- REQ-201: [!] MUST support multiple navigation methods
- REQ-202: MUST provide quick reference index
- REQ-203: MUST include comprehensive glossary

### Machine Readability

- REQ-301: [!] Syntax definitions MUST be formally specified when appropriate
- REQ-302: Reference MUST support programmatic extraction of rules

## Validation Criteria

Reference documentation is valid when:
- All MSL features are comprehensively documented
- Examples demonstrate correct usage
- Information is easily discoverable
- Content serves both implementers and users

## Notes

The reference documentation serves as the authoritative source for MSL language details. It must be comprehensive enough for tool implementers while remaining accessible for specification authors. This specification inherits common documentation requirements from msl-docs-base and focuses on the unique aspects of technical reference documentation.

---
*Specification format: [MSL Level 1](https://github.com/chrs-myrs/msl-specification)*