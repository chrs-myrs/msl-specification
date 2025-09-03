---
id: msl-semantics
extends: msl-grammar
tags: [semantics, behavior, interpretation]
priority: critical
status: active
assignee: msl-core-team
---

# MSL Semantics Specification

## Summary

This specification defines the semantic meaning and behavioral interpretation of MSL constructs. While MSL Grammar defines syntax rules, MSL Semantics defines what MSL elements mean and how they should be processed and interpreted.

The semantics specification provides the authoritative reference for MSL behavior, enabling consistent interpretation across different tools, platforms, and use cases.

## Requirements

### Core Semantic Principles

- REQ-001: [!] [INHERIT] All MSL Grammar syntax rules must be semantically meaningful
- REQ-002: [!] MSL documents represent executable specifications with testable requirements
- REQ-003: [!] MSL specifications define "what" systems must do, not "how" to implement
- REQ-004: [!] MSL constructs must have unambiguous semantic interpretation
- REQ-005: Lower MSL levels must be semantically compatible with higher levels

### Document Identity Semantics

- REQ-101: Document `id` creates unique namespace for requirement references
- REQ-102: [#inheritance] Documents with same `id` in inheritance chain represent versions of same specification
- REQ-103: [#references] External references to documents must use `id`, not filename
- REQ-104: [#namespacing] Document `id` enables requirement addressing as `document-id.REQ-XXX`
- REQ-105: Missing `id` field creates implicit identity from filename without extension

### Requirement Identity Semantics

- REQ-201: [!] REQ-XXX identifiers create unique addressable requirement within document
- REQ-202: [!] Requirements without explicit IDs cannot be referenced externally
- REQ-203: [#inheritance] REQ-IDs enable precise inheritance control between parent and child
- REQ-204: [#traceability] REQ-IDs enable requirement traceability across specification evolution
- REQ-205: REQ-ID numbering suggests logical grouping but does not enforce ordering

### Inheritance Semantics

- REQ-301: [!] [OVERRIDE] `extends` relationship creates parent-child semantic dependency
- REQ-302: [!] [NEW] Child documents inherit parent's complete requirement set by default
- REQ-303: [!] [NEW] Child requirements with matching parent REQ-IDs replace parent requirements
- REQ-304: [NEW] `[INHERIT]` marker preserves parent requirement unchanged in child context
- REQ-305: [NEW] `[OVERRIDE]` marker explicitly replaces parent requirement with new content
- REQ-306: [NEW] `[NEW]` marker adds requirement not present in parent specification
- REQ-307: [NEW] Requirements without inheritance markers inherit parent when REQ-IDs match
- REQ-308: [#validation] Inheritance chain creates acyclic directed graph of dependencies

### Marker Semantics

- REQ-401: [!] [OVERRIDE] Quick markers modify semantic meaning of individual requirements
- REQ-402: [!] [NEW] Priority markers indicate urgency and implementation order
- REQ-403: [!] [NEW] `[!]` marker indicates critical priority requiring immediate attention
- REQ-404: [NEW] `[?]` marker indicates uncertainty requiring clarification or research
- REQ-405: [NEW] Status markers track requirement lifecycle and completion state
- REQ-406: [NEW] `[x]` marker indicates requirement satisfaction and implementation completion
- REQ-407: [NEW] `[ ]` marker indicates pending requirement awaiting implementation
- REQ-408: [NEW] Assignment markers create responsibility relationships
- REQ-409: [NEW] `[@user]` marker assigns requirement ownership to specific individual or team
- REQ-410: [NEW] Tag markers enable requirement categorization and filtering
- REQ-411: [NEW] `[#tag]` marker associates requirement with semantic category or feature set

### Template Semantics

- REQ-501: [#templates] Templates define reusable specification patterns with parameterization
- REQ-502: [#templates] `type: template` creates specification intended for extension, not direct use
- REQ-503: [#templates] Template variables enable specification family creation with consistent structure
- REQ-504: [#templates] Variable substitution occurs before semantic processing of content
- REQ-505: [#templates] Child documents may override template variables to customize behavior
- REQ-506: [#templates] Template inheritance combines pattern reuse with requirement inheritance
- REQ-507: [#templates] Undefined variables create semantic errors preventing specification instantiation

### Status Lifecycle Semantics

- REQ-601: Document and requirement status indicates specification maturity and stability
- REQ-602: `draft` status indicates specification under development, subject to change
- REQ-603: `active` status indicates stable specification in current use
- REQ-604: `complete` status indicates implemented and validated specification
- REQ-605: `deprecated` status indicates specification superseded by newer version
- REQ-606: `uncertain` status indicates specification requiring clarification or research
- REQ-607: `pending` status indicates approved specification awaiting implementation

### Priority Semantics

- REQ-701: Priority levels indicate implementation urgency and business importance
- REQ-702: `critical` priority indicates requirements blocking system operation
- REQ-703: `high` priority indicates requirements needed for core functionality
- REQ-704: `medium` priority indicates standard requirements for complete system
- REQ-705: `low` priority indicates nice-to-have requirements for enhanced system
- REQ-706: Priority conflicts between frontmatter and markers resolved by marker precedence

### Tag Semantics

- REQ-801: [#categorization] Tags create semantic categories for requirement organization
- REQ-802: [#filtering] Tags enable requirement filtering and query operations
- REQ-803: [#workflow] Tags may indicate development phases: `[#mvp]`, `[#v2]`, `[#future]`
- REQ-804: [#architecture] Tags may indicate system components: `[#frontend]`, `[#backend]`, `[#api]`
- REQ-805: [#process] Tags may indicate requirement types: `[#feature]`, `[#bugfix]`, `[#security]`
- REQ-806: [#custom] Organizations may define custom tag semantics for specific needs

### Processing Order Semantics

- REQ-901: [!] [@msl-tools] MSL processing must follow deterministic semantic order
- REQ-902: [!] [@msl-tools] Variable substitution occurs before requirement processing
- REQ-903: [!] [@msl-tools] Inheritance resolution occurs before marker interpretation
- REQ-904: [@msl-tools] Template instantiation occurs before child document processing
- REQ-905: [@msl-tools] Validation occurs after complete semantic processing
- REQ-906: [@msl-tools] Circular dependencies must be detected and rejected before processing

### Error Semantics

- REQ-1001: [#error-handling] Semantic errors must prevent incorrect specification interpretation
- REQ-1002: [#error-handling] Missing parent documents create semantic errors blocking child processing
- REQ-1003: [#error-handling] Undefined variable references create semantic errors in templates
- REQ-1004: [#error-handling] Invalid inheritance markers create semantic errors requiring correction
- REQ-1005: [#error-handling] Semantic warnings indicate potential issues without blocking processing

### Compatibility Semantics

- REQ-1101: [!] Level N documents must be semantically processable by Level N+ processors
- REQ-1102: [!] Level N+ processors must gracefully handle Level N documents
- REQ-1103: Unknown frontmatter fields must be preserved without semantic interpretation
- REQ-1104: [#backward-compatibility] MSL semantic evolution must maintain backward compatibility
- REQ-1105: [#forward-compatibility] MSL processors should handle unknown constructs gracefully

## Semantic Processing Model

### Inheritance Resolution Algorithm

- REQ-1201: [!] [@msl-tools] Process inheritance chain from root parent to final child
- REQ-1202: [!] [@msl-tools] Build complete requirement set by merging parent and child requirements
- REQ-1203: [@msl-tools] Apply inheritance markers to determine final requirement content
- REQ-1204: [@msl-tools] Validate inheritance consistency and marker compatibility
- REQ-1205: [@msl-tools] Generate resolved specification containing all effective requirements

### Variable Substitution Algorithm

- REQ-1301: [#templates] [@msl-tools] Collect variable definitions from frontmatter and inheritance chain
- REQ-1302: [#templates] [@msl-tools] Child variable definitions override parent definitions
- REQ-1303: [#templates] [@msl-tools] Replace all `${variable_name}` references with defined values
- REQ-1304: [#templates] [@msl-tools] Variable substitution applies to titles, requirements, and content
- REQ-1305: [#templates] [@msl-tools] Report errors for undefined variable references

### Validation Model

- REQ-1401: [@msl-tools] Validate document structure conforms to grammar rules
- REQ-1402: [@msl-tools] Validate semantic consistency of inheritance relationships
- REQ-1403: [@msl-tools] Validate marker usage follows semantic rules
- REQ-1404: [@msl-tools] Validate template completeness and variable resolution
- REQ-1405: [@msl-tools] Generate actionable error messages for semantic violations

## Examples

### Inheritance Semantics Example

```markdown
# Parent document defines base requirements
- REQ-001: Base authentication required
- REQ-002: HTTPS encryption required

# Child document modifies and extends
- REQ-001: [OVERRIDE] OAuth2 authentication required  # Replaces parent REQ-001
- REQ-002: [INHERIT] HTTPS encryption required        # Preserves parent REQ-002  
- REQ-003: [NEW] Rate limiting required               # Adds new requirement
```

### Template Semantics Example

```markdown
# Template defines pattern with variables
# ${service_name} must handle ${max_requests} requests per minute
# Child instantiation: "PaymentAPI must handle 100 requests per minute"
```

### Marker Semantics Example

```markdown
- [!] [@alice] [#security] REQ-001: Implement encryption
# Semantic interpretation:
# - Critical priority (blocks other work)
# - Assigned to alice (responsibility)  
# - Security category (compliance requirement)
```

## Notes

This semantics specification provides the behavioral foundation for MSL processing. While grammar defines syntax rules, semantics defines meaning and enables consistent interpretation across tools and teams.

The semantic model supports complex specification workflows while maintaining the simplicity and accessibility that makes MSL effective for individual and organizational use.