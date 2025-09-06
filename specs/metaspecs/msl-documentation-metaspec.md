---
msl: L2
id: msl-documentation-metaspec
type: metaspec
version: 1.0.0
tags: [metaspec, documentation, governance, principles]
priority: critical
status: active
---

# MSL Documentation Metaspec [MSL]

## Summary

This metaspec governs all MSL documentation specifications, establishing universal principles and quality standards that ensure documentation serves both human readers and AI agents effectively while maintaining simplicity and avoiding over-specification.

## Core Principles

### Documentation Philosophy

- REQ-001: [!] Documentation MUST prioritize clarity over completeness
- REQ-002: [!] Documentation MUST follow "progressive disclosure" - simple first, details later
- REQ-003: [!] Documentation MUST avoid prescriptive metrics in favor of principles
- REQ-004: Documentation SHOULD use writer's judgment for specific implementations
- REQ-005: Documentation MUST be task-oriented rather than feature-oriented

### Structural Requirements

- REQ-101: [!] All documentation specs MUST extend a common base specification
- REQ-102: [!] Documentation specs MUST NOT duplicate requirements from the base
- REQ-103: Documentation specs MUST only add domain-specific requirements
- REQ-104: Documentation hierarchy MUST be shallow (≤2 inheritance levels)
- REQ-105: Documentation specs MUST focus on "what" not "how"

## Quality Standards

### Content Quality

- REQ-201: [!] Documentation MUST be accurate and synchronized with implementation
- REQ-202: [!] Examples MUST be practical and executable
- REQ-203: Documentation MUST use consistent terminology
- REQ-204: Documentation MUST be accessible to target audience
- REQ-205: Documentation SHOULD include both positive and negative examples

### Simplicity Requirements

- REQ-301: [!] Documentation specs MUST be ≤300 lines to maintain focus
- REQ-302: [!] Requirements MUST be high-level principles, not detailed rules
- REQ-303: Avoid specifying exact quantities (e.g., "≥3 examples") unless critical
- REQ-304: Trust documentation authors to interpret principles appropriately
- REQ-305: Documentation specs SHOULD have ≤20 requirements total

## Governance Rules

### Specification Compliance

- REQ-401: [!] Documentation specs MUST be valid MSL documents
- REQ-402: [!] Documentation specs MUST use proper inheritance with `extends:`
- REQ-403: Documentation specs MUST NOT use `extends:` unless true "is-a" relationship
- REQ-404: Documentation specs MUST declare governance by this metaspec
- REQ-405: Documentation specs MUST achieve ≥80 validation score

### Evolution Control

- REQ-501: Changes to documentation specs MUST maintain backward compatibility
- REQ-502: New documentation types MUST extend the base specification
- REQ-503: Documentation consolidation MUST preserve essential requirements
- REQ-504: Deprecated documentation specs MUST be archived, not deleted

## Anti-Patterns to Avoid

### Over-Specification

- REQ-601: [!] MUST NOT specify exact numbers unless functionally required
- REQ-602: [!] MUST NOT create documentation about documentation beyond necessity
- REQ-603: MUST NOT duplicate requirements available through inheritance
- REQ-604: MUST NOT create complex validation rules for subjective qualities
- REQ-605: MUST NOT mandate specific formatting beyond MSL requirements

### Complexity Creep

- REQ-701: MUST NOT add requirements that increase cognitive load without clear benefit
- REQ-702: MUST NOT create deep inheritance hierarchies
- REQ-703: MUST NOT mix governance concerns with content requirements
- REQ-704: MUST NOT specify implementation details in requirement specs

## Examples

### Good: High-Level Principle
```yaml
# Good - Principle-based requirement
REQ-001: Documentation MUST include practical examples

# Bad - Over-specified requirement  
REQ-001: Documentation MUST include exactly 3 examples with 10-15 lines each
```

### Good: Proper Inheritance
```yaml
# Good - True "is-a" relationship
extends: msl-docs-base  # Tutorial IS A type of documentation

# Bad - Not an "is-a" relationship
extends: msl-l2-advanced  # Docs are not a type of language spec
```

### Good: Simple Structure
```markdown
msl-docs-base.md (common requirements)
├── msl-docs-getting-started.md (extends base)
├── msl-docs-user-guide.md (extends base)
├── msl-docs-reference.md (extends base)
└── msl-docs-tutorials.md (extends base)
```

## Notes

This metaspec embodies the lesson that documentation specifications should guide and constrain, not micromanage. By focusing on principles over prescriptions, we enable documentation authors to use their judgment while ensuring consistency and quality.

The goal is documentation that helps users succeed, not documentation that passes arbitrary metrics. This metaspec ensures all MSL documentation remains focused on this goal while avoiding the trap of over-engineering documentation about documentation.

---
*Specification format: [MSL Level 2](https://github.com/chrs-myrs/msl-specification)*