---
id: msl-l1-structure
extends: msl-l0-foundation
tags: [specification, level-1]
---

# MSL Level 1: Structured Specification

## Summary

MSL Level 1 extends MSL Level 0 by adding YAML frontmatter and structured requirement identifiers. This level enables document referencing, requirement tracking, and basic inheritance while maintaining full compatibility with Level 0.

Level 1 specifications can be processed by markdown renderers (ignoring frontmatter) or by MSL-aware tools that understand metadata and inheritance.

## Requirements

### Level 0 Inheritance

- REQ-001: [INHERIT] All MSL Level 0 document structure requirements
- REQ-002: [INHERIT] Requirements section format and content guidelines
- REQ-003: [INHERIT] Markdown compatibility and processing expectations

### YAML Frontmatter

- REQ-101: MSL Level 1 documents should include YAML frontmatter block
- REQ-102: Frontmatter must begin and end with three dashes on separate lines
- REQ-103: Frontmatter must contain valid YAML syntax
- REQ-104: Frontmatter must be placed at the beginning of the document
- REQ-105: Documents without frontmatter are valid Level 0 and should be processed accordingly

### Document Identification

- REQ-201: Frontmatter should include an "id" field with unique identifier
- REQ-202: Document ID must be a string using kebab-case format
- REQ-203: Document ID must be unique within the specification set
- REQ-204: When no ID is specified, filename without extension becomes implicit ID
- REQ-205: IDs enable referencing documents from other MSL specifications

### Requirement Identifiers

- REQ-301: Requirements may include explicit identifiers using REQ-NNN format
- REQ-302: Requirement IDs must be unique within a single document
- REQ-303: Requirement IDs should use sequential numbering starting from 001
- REQ-304: Requirement ID must be followed by colon and space before requirement text
- REQ-305: Requirements without explicit IDs are valid but cannot be referenced externally

### Basic Inheritance

- REQ-401: Frontmatter may include "extends" field referencing parent document ID
- REQ-402: Child documents inherit all requirements from parent documents
- REQ-403: Child documents may add new requirements not present in parent
- REQ-404: Inheritance creates a parent-child relationship between specifications
- REQ-405: Circular inheritance references are invalid and must be rejected

### Metadata Fields

- REQ-501: Frontmatter may include "tags" field as array of classification strings
- REQ-502: Frontmatter may include "status" field indicating document lifecycle stage
- REQ-503: Valid status values include draft, active, complete, deprecated
- REQ-504: Frontmatter may include custom fields for organizational needs
- REQ-505: Unknown frontmatter fields should be preserved but ignored by MSL processors

### Processing Requirements

- REQ-601: MSL Level 1 processors must parse YAML frontmatter
- REQ-602: Processors must extract document ID from frontmatter or filename
- REQ-603: Processors must identify requirements with explicit REQ-NNN identifiers
- REQ-604: Processors must validate requirement ID uniqueness within documents
- REQ-605: Processors should provide warnings for missing or malformed IDs
- REQ-606: Level 1 processors must maintain backward compatibility with Level 0

### Validation Rules

- REQ-701: Documents with malformed YAML frontmatter should be treated as Level 0
- REQ-702: Duplicate requirement IDs within a document must be flagged as errors
- REQ-703: References to non-existent parent documents must be flagged as errors
- REQ-704: Processors should validate that inherited requirements exist in parent
- REQ-705: Documents must remain valid when frontmatter is stripped

## Examples

### Minimal Level 1 Document

```markdown
---
id: example-spec
---

# Example Specification

## Requirements
- REQ-001: System must handle user input
- REQ-002: System must provide feedback
```

### Document with Inheritance

```markdown
---
id: child-spec
extends: parent-spec
tags: [feature, backend]
---

# Child Specification

## Requirements
- REQ-001: New requirement specific to child
- REQ-002: Another child-specific requirement
```

## Notes

MSL Level 1 provides the structured foundation needed for requirement management while preserving the simplicity and accessibility of Level 0. The addition of frontmatter and IDs enables tooling support without compromising human readability.

Level 1 specifications can be processed by standard markdown tools (which ignore frontmatter) or by MSL-aware processors that understand inheritance and provide additional validation and processing capabilities.