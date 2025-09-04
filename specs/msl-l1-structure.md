---
msl: L1
id: msl-l1-structure
extends: msl-l0-foundation
governed-by: [msl-core-metaspec, msl-language-metaspec]
tags: [specification, level-1]
---

# MSL Level 1: Structured Specifications [MSL]

## Summary

MSL Level 1 extends Level 0 by adding optional structure through YAML frontmatter and requirement IDs. These features enable document referencing, requirement tracking, and basic inheritance while maintaining full backward compatibility. Everything new in Level 1 is optional - plain Level 0 documents are valid Level 1.

## Requirements

### Foundation Requirements

- Documents inherit all Level 0 requirements (title, requirements section, markdown compatibility)
- Documents without Level 1 features remain valid Level 1 specifications
- Level 1 processors should handle Level 0 documents transparently

### Frontmatter Features

- Documents may include YAML frontmatter between triple-dash delimiters at the start
- Frontmatter may contain an `id` field to uniquely identify the document
- Frontmatter may contain an `extends` field to inherit from another specification
- Frontmatter may contain a `tags` field with an array of classification strings
- Frontmatter may contain `status` (draft, active, complete, deprecated) and `priority` (low, medium, high, critical) fields
- Documents without frontmatter are processed as standard Level 0 specifications

### Requirement Identifiers

- Requirements may begin with `REQ-NNN:` format for unique identification
- REQ-IDs enable precise requirement referencing within and across documents
- REQ-IDs must be unique within a single document - processors should warn about duplicates
- Requirements without REQ-IDs are valid but cannot be externally referenced
- REQ-ID numbers suggest logical grouping but don't enforce order
- Duplicate REQ-IDs should generate warnings but not prevent processing

### Basic Inheritance

- Documents with `extends` field inherit all requirements from the parent document
- Child documents may add new requirements not in the parent
- Child requirements with matching REQ-IDs replace parent requirements
- Inheritance creates reusable specification hierarchies

### Processing Conventions

- Tools should parse YAML frontmatter when present to extract metadata
- Tools should build requirement indices using REQ-IDs for cross-referencing
- Tools should resolve inheritance chains depth-first from parent to child
- Tools must warn about duplicate REQ-IDs within a document
- Tools must warn about references to non-existent parent documents
- Tools must treat malformed YAML frontmatter as body content and process as Level 0
- Circular inheritance references must be detected and reported as errors

### Identification Methods

- Level 1 documents inherit L0's encouraged identification methods (`[MSL]` in title, MSL repository link)
- Presence of YAML frontmatter itself serves as Level 1 identification
- Frontmatter should include `msl: L1` field for explicit level identification
- Documents are implicitly identified by frontmatter + Requirements section combination

## Examples

### Simple Level 1 Document

```markdown
---
msl: L1
id: user-authentication
tags: [security, backend]
status: active
---

# User Authentication [MSL]

## Requirements
- REQ-001: Support email/password authentication
- REQ-002: Implement OAuth2 for third-party login
- REQ-003: Provide password reset via email
```

### Document with Inheritance

```markdown
---
id: admin-authentication
extends: user-authentication
---

# Admin Authentication

## Requirements
- REQ-001: Support email/password with 2FA required
- REQ-004: Require hardware key for sensitive operations
- REQ-005: Log all authentication attempts
```

### Minimal Frontmatter

```markdown
---
id: payment-processing
---

# Payment Processing

## Requirements
- Process credit card payments
- Support refunds within 30 days
- Generate receipts for all transactions
```

## Notes

Level 1 provides just enough structure for teams that need requirement tracking and document relationships. The YAML frontmatter is ignored by standard markdown viewers, maintaining universal readability while enabling tool support.

All Level 1 features are optional enhancements. Use what helps your workflow, ignore what doesn't. When you need more advanced features like markers and templates, Level 2 is waiting.

---
*Specification format: [MSL Level 1](https://github.com/chrs-myrs/msl-specification)*