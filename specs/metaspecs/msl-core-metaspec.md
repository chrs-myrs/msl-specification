---
msl: L2
id: msl-core-metaspec
type: metaspec
version: 1.0.0
tags: [metaspec, core, governance, self-referential]
priority: critical
status: active
---

# MSL Core Metaspec [MSL]

## Summary

This metaspec governs all core MSL language specifications (L0, L1, L2, and future levels). It ensures consistency, quality, and proper progressive enhancement across the foundational specifications that define MSL itself.

This is a self-referential metaspec - the core MSL specifications are governed by a metaspec written in MSL, demonstrating the language's capability to specify itself.

## Structural Requirements

### Mandatory Sections

- REQ-001: [!] MUST have a level-1 heading with specification name and `[MSL]` marker
- REQ-002: [!] MUST have `## Summary` section explaining the specification's purpose and role
- REQ-003: [!] MUST have `## Requirements` section containing all normative requirements
- REQ-004: [!] MUST have `## Examples` section demonstrating key concepts with code blocks
- REQ-005: [!] MUST have `## Notes` section providing context and rationale
- REQ-006: [!] MUST end with specification format attribution line

### Section Content Requirements

- REQ-101: Summary MUST explain how this level relates to other levels
- REQ-102: Summary MUST identify what new capabilities this level adds
- REQ-103: Requirements MUST be organized into logical subsections
- REQ-104: Examples MUST show progression from minimal to complete usage
- REQ-105: Notes MUST explain design decisions and trade-offs

## Progressive Enhancement Requirements

### Level Relationships

- REQ-201: [!] Each level MUST properly extend the previous level using `extends` field
- REQ-202: [!] Level 0 MUST NOT have any dependencies (foundation layer)
- REQ-203: [!] Higher levels MUST maintain backward compatibility with lower levels
- REQ-204: [!] Each level MUST explicitly state inherited requirements
- REQ-205: [!] New requirements MUST be clearly marked as additions to previous level

### Feature Introduction

- REQ-301: Each level MUST introduce a coherent set of related features
- REQ-302: Features MUST follow the complexity progression: simple → structured → advanced
- REQ-303: Optional features MUST be clearly distinguished from mandatory features
- REQ-304: Each level MUST be independently useful without requiring higher levels

## Quality Requirements

### Documentation Standards

- REQ-401: [!] All requirements MUST be testable with clear pass/fail criteria
- REQ-402: [!] Language MUST be precise and unambiguous
- REQ-403: [!] Technical terms MUST be defined before first use
- REQ-404: Examples MUST be complete and syntactically valid
- REQ-405: MUST avoid forward references to higher-level features

### Consistency Requirements

- REQ-501: Terminology MUST be consistent across all core specifications
- REQ-502: Requirement numbering MUST follow consistent patterns
- REQ-503: Example formatting MUST use consistent markdown code blocks
- REQ-504: Cross-references MUST use specification IDs when referring to other specs

## Self-Referential Requirements

### MSL Compliance

- REQ-601: [!] Core specifications MUST be valid MSL documents at their declared level
- REQ-602: [!] L0 spec MUST be written in pure MSL Level 0 format
- REQ-603: [!] L1 spec MUST use Level 1 features (frontmatter, REQ-IDs)
- REQ-604: [!] L2 spec MUST demonstrate Level 2 features (markers, inheritance)
- REQ-605: [!] Specifications MUST "eat their own dog food" - use the features they define

### Meta-Governance

- REQ-701: Core specifications SHOULD declare governance by this metaspec
- REQ-702: Governance declaration MUST use proposed `governed-by` field when available
- REQ-703: This metaspec MUST itself conform to its own requirements
- REQ-704: Future core specifications MUST be validated against this metaspec

## Validation Rules

### Structural Validation

- REQ-801: Validator MUST check presence of all mandatory sections
- REQ-802: Validator MUST verify proper inheritance chain
- REQ-803: Validator MUST ensure backward compatibility claims are accurate
- REQ-804: Validator MUST check that examples match specification level

### Semantic Validation

- REQ-901: Validator MUST verify requirements are internally consistent
- REQ-902: Validator MUST check that inherited requirements are preserved
- REQ-903: Validator MUST ensure new features don't break existing patterns
- REQ-904: Validator MUST validate self-referential compliance

## Examples

### Compliant Core Specification Structure

```markdown
---
msl: L1
id: msl-l1-structure  
extends: msl-l0-foundation
governed-by: [msl-core-metaspec, msl-language-metaspec]
---

# MSL Level 1: Structured Specifications [MSL]

## Summary
[Explains L1's role and what it adds to L0]

## Requirements

### Foundation Requirements
[Requirements inherited from L0]

### New L1 Features
[Requirements unique to L1]

## Examples
[Shows L0 → L1 progression]

## Notes
[Explains design rationale]

---
*Specification format: [MSL Level 1](https://github.com/chrs-myrs/msl-specification)*
```

### Progressive Enhancement Pattern

```markdown
L0: Pure markdown with requirements
 ↓ extends
L1: Adds frontmatter and REQ-IDs
 ↓ extends  
L2: Adds markers and templates
 ↓ extends
L3: [Future advanced features]
```

## Notes

This metaspec creates a self-validating system where MSL uses its own features to govern its own specifications. This demonstrates MSL's maturity and capability while ensuring the core specifications maintain consistent quality.

The self-referential nature (MSL specifications governed by MSL metaspecs) provides:
1. **Proof of Concept** - MSL is powerful enough to specify itself
2. **Quality Assurance** - Core specs must meet their own standards
3. **Educational Value** - Shows metaspec patterns by example
4. **Evolution Control** - Future levels must conform to established patterns

This metaspec should be considered the authoritative governance for all core MSL language specifications.

---
*Specification format: [MSL Level 2](https://github.com/chrs-myrs/msl-specification)*