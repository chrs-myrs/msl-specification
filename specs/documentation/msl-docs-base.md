---
msl: L1
id: msl-docs-base
tags: [documentation, base, common]
priority: critical
status: active
governed-by: msl-documentation-metaspec
references:
  - msl-l2-advanced: "Language specification being documented"
  - msl-usage-standards: "Quality standards for documentation"
---

# MSL Documentation Base Specification [MSL]

## Summary

This specification defines the common requirements that all MSL documentation must follow, establishing a foundation for consistent, accessible, and maintainable documentation across all types and topics.

## Requirements

### Core Structure

- REQ-001: [!] Documentation MUST be written in Markdown format
- REQ-002: [!] Documentation MUST include clear headings and logical organization
- REQ-003: Documentation MUST map to its governing specification
- REQ-004: Documentation MUST declare its purpose and scope upfront
- REQ-005: Documentation MUST use consistent MSL terminology

### Accessibility

- REQ-101: [!] Documentation MUST be readable by target audience
- REQ-102: Documentation MUST support progressive learning (simple to complex)
- REQ-103: Documentation MUST define technical terms before use
- REQ-104: Documentation MUST be accessible offline (no external dependencies)

### Examples and Code

- REQ-201: [!] Examples MUST be practical and relevant
- REQ-202: Examples MUST be syntactically correct and executable
- REQ-203: Code blocks MUST use appropriate syntax highlighting
- REQ-204: Examples SHOULD show both correct and incorrect usage

### Navigation and References

- REQ-301: [!] Cross-references MUST use consistent link format
- REQ-302: Prerequisites MUST be explicitly stated
- REQ-303: Documentation MUST provide clear next steps
- REQ-304: External references MUST be stable and versioned

### Quality and Maintenance

- REQ-401: [!] Documentation MUST be synchronized with implementation
- REQ-402: Documentation MUST be reviewed for accuracy
- REQ-403: Documentation MUST follow version control practices
- REQ-404: Documentation SHOULD include last-updated timestamp

### Machine Readability

- REQ-501: Documentation MUST include structured metadata when relevant
- REQ-502: Documentation MUST support search indexing
- REQ-503: API documentation MUST include machine-readable schemas where applicable

## Inheritance Note

Documentation specifications that extend this base MUST:
1. Use `extends: msl-docs-base` in frontmatter
2. Only add domain-specific requirements
3. Not duplicate base requirements
4. Focus on unique aspects of their documentation type

## Validation Criteria

Documentation is valid when it:
- Follows all base requirements
- Is accurate and up-to-date
- Serves its intended audience effectively
- Maintains consistency with other documentation

## Notes

This base specification extracts common requirements from all documentation types, eliminating duplication while ensuring consistency. Child specifications need only define what makes them unique, following the DRY principle and MSL's inheritance model.

By keeping these requirements high-level and principle-based rather than prescriptive, we trust documentation authors to interpret and apply them appropriately for their specific context.

---
*Specification format: [MSL Level 1](https://github.com/chrs-myrs/msl-specification)*