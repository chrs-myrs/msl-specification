---
msl: L1
id: msl-docs-readme
tags: [documentation, readme, landing-page]
priority: critical
status: active
references:
  - msl-docs-root: "Part of documentation system"
  - msl-l0-foundation: "Core language to introduce"
---

# MSL README Documentation Specification [MSL]

## Summary

This specification defines requirements for the MSL project README, which serves as the primary landing page and entry point for users discovering MSL through GitHub or other channels.

## Requirements

### Above-the-Fold Content

- REQ-001: [!] [NEW] README must communicate MSL's value in first 3 lines
- REQ-002: [!] [NEW] README must show working MSL example within first screen
- REQ-003: [!] [NEW] README must provide 30-second quickstart
- REQ-004: [NEW] README must include project badges (version, license, status)
- REQ-005: [NEW] README must have clear navigation links to docs

### Value Proposition

- REQ-101: [!] [NEW] Must clearly state the problem MSL solves
- REQ-102: [!] [NEW] Must show MSL's solution with immediate example
- REQ-103: [NEW] Must differentiate from alternatives (YAML, JSON, etc.)
- REQ-104: [NEW] Must highlight key benefits: progressive, git-friendly, tool-optional
- REQ-105: [NEW] Must include comparison table with other solutions
- REQ-106: [!] [NEW] Must highlight self-referential architecture as proof of power

### Progressive Complexity Demonstration

- REQ-201: [!] [NEW] Must show Level 0 → Level 1 → Level 2 progression
- REQ-202: [NEW] Each level must have visual example
- REQ-203: [NEW] Examples must be side-by-side for comparison
- REQ-204: [NEW] Must explain when to use each level
- REQ-205: [NEW] Must emphasize "start simple" philosophy

### Documentation Links

- REQ-301: [!] [NEW] Must link to generated documentation (not specs)
- REQ-302: [NEW] Must have clear "Getting Started" link
- REQ-303: [NEW] Must link to full user guide
- REQ-304: [NEW] Must link to examples directory
- REQ-305: [NEW] Must avoid linking to specification files directly

### Project Information

- REQ-401: [!] [NEW] Must include installation instructions (if any)
- REQ-402: [NEW] Must include contribution guidelines or link
- REQ-403: [NEW] Must include license information
- REQ-404: [NEW] Must include project status/maturity
- REQ-405: [NEW] Must include contact/support information

### Self-Specification Section

- REQ-501: [!] [NEW] Must mention MSL is self-specified
- REQ-502: [NEW] Must explain significance of self-specification
- REQ-503: [NEW] Must show validation scores as proof
- REQ-504: [NEW] Must link to specification directory for exploration
- REQ-505: [NEW] Must avoid overwhelming newcomers with meta-concepts

## Validation Criteria

README documentation is valid when:
- Value proposition is clear in <10 seconds
- Quickstart works without prerequisites
- All documentation links resolve
- Examples are correct and runnable
- Progressive nature is immediately apparent

## Notes

The README is often the only documentation users read. It must be compelling, accurate, and actionable while avoiding specification details that belong in proper documentation.

---
*Specification format: [MSL Level 1](https://github.com/chrs-myrs/msl-specification)*