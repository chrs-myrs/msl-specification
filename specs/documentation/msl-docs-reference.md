---
msl: L1
id: msl-docs-reference
tags: [documentation, reference, technical]
priority: high
status: active
references:
  - msl-docs-root: "Part of documentation system"
  - msl-l2-advanced: "Complete language to document"
---

# MSL Reference Documentation Specification [MSL]

## Summary

This specification defines requirements for MSL technical reference documentation providing comprehensive, searchable information about every language feature, syntax element, and semantic rule.

## Requirements

### Content Structure

- REQ-001: [!] [NEW] Reference must be organized alphabetically and by category
- REQ-002: [!] [NEW] Each entry must follow consistent template structure
- REQ-003: [NEW] Entries must include syntax, semantics, and examples
- REQ-004: [NEW] Cross-references must be bidirectional
- REQ-005: [NEW] Each entry must be individually linkable

### Coverage Requirements

- REQ-101: [!] [NEW] Must document 100% of MSL syntax elements
- REQ-102: [!] [NEW] Must document all markers with semantic meanings
- REQ-103: [!] [NEW] Must document all frontmatter fields and types
- REQ-104: [NEW] Must include complete inheritance rules
- REQ-105: [NEW] Must document all validation requirements
- REQ-106: [NEW] Must include error messages and fixes

### Entry Template

- REQ-201: [!] [NEW] Each entry must include: name, syntax, description
- REQ-202: [NEW] Complex entries must include: parameters, return values
- REQ-203: [NEW] All entries must include: examples (valid and invalid)
- REQ-204: [NEW] Entries must specify: MSL level (L0/L1/L2)
- REQ-205: [NEW] Related entries must be cross-linked

### Search and Navigation

- REQ-301: [!] [NEW] Must support search by keyword, category, level
- REQ-302: [NEW] Must provide quick reference index
- REQ-303: [NEW] Must support "see also" navigation
- REQ-304: [NEW] Must include comprehensive glossary
- REQ-305: [NEW] Must provide syntax cheat sheet

### Machine Readability

- REQ-401: [!] [NEW] Each entry must have structured metadata
- REQ-402: [NEW] Syntax must be in formal notation (BNF/EBNF)
- REQ-403: [NEW] Examples must be marked as executable
- REQ-404: [NEW] Validation rules must be programmatically extractable
- REQ-405: [NEW] Must support generation of syntax validators

## Validation Criteria

Reference documentation is valid when:
- All syntax elements are documented
- All examples are valid MSL
- Cross-references resolve correctly
- Search returns relevant results
- Formal syntax parses correctly

## Notes

The reference documentation serves as the authoritative source for MSL language details. It must be comprehensive enough for tool implementers while remaining accessible for specification authors.

---
*Specification format: [MSL Level 1](https://github.com/chrs-myrs/msl-specification)*