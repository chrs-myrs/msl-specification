---
id: msl-l2-advanced
extends: msl-l1-structure
tags: [specification, level-2, advanced]
priority: high
status: active
---

# MSL Level 2: Advanced Features

## Summary

MSL Level 2 extends MSL Level 1 with advanced features including quick markers, sophisticated inheritance, templates, and comprehensive metadata. This level provides enterprise-grade specification management while maintaining backward compatibility with lower levels.

Level 2 enables complex specification workflows including requirement prioritization, assignment, templating, and advanced inheritance patterns.

## Requirements

### Level 1 Inheritance

- REQ-001: [INHERIT] All MSL Level 1 structured specification requirements
- REQ-002: [INHERIT] YAML frontmatter and document identification features
- REQ-003: [INHERIT] Basic inheritance and processing requirements

### Quick Markers

- REQ-101: [!] Requirements may include quick markers in square brackets at line start
- REQ-102: [!] Priority markers must use exclamation `[!]` for critical/high priority
- REQ-103: Status markers must support completion `[x]`, pending `[ ]`, uncertain `[?]`
- REQ-104: Assignment markers must use at-symbol format `[@username]` for assignee
- REQ-105: Tag markers must use hash format `[#tagname]` for categorization
- REQ-106: Multiple markers may be combined on single requirement line
- REQ-107: Markers must be placed before requirement text and REQ-ID when present

### Advanced Inheritance

- REQ-201: [NEW] Child documents must support explicit inheritance control markers
- REQ-202: [NEW] `[OVERRIDE]` marker replaces parent requirement with new content
- REQ-203: [NEW] `[NEW]` marker indicates requirement not present in parent document
- REQ-204: [NEW] `[INHERIT]` marker explicitly preserves parent requirement unchanged
- REQ-205: [NEW] Alternative syntax "Modified:" and "New:" provide readable inheritance
- REQ-206: Requirements without inheritance markers inherit parent by default when IDs match
- REQ-207: Child requirements with new REQ-IDs are implicitly `[NEW]` requirements

### Template System

- REQ-301: Documents may specify `type: template` in frontmatter for reusable patterns
- REQ-302: Templates must define variables section in frontmatter for substitution
- REQ-303: Variable substitution uses `${variable_name}` syntax in content
- REQ-304: Child documents may override template variables in their frontmatter
- REQ-305: Templates enable creation of specification families with consistent structure
- REQ-306: Template inheritance combines with variable substitution for powerful patterns

### Enhanced Metadata

- REQ-401: [OVERRIDE] Frontmatter supports comprehensive priority levels: critical, high, medium, low
- REQ-402: [NEW] Frontmatter supports detailed status tracking: draft, active, complete, deprecated, uncertain, pending
- REQ-403: [NEW] Frontmatter may include assignee field for ownership tracking
- REQ-404: [NEW] Frontmatter supports variables section for template functionality
- REQ-405: [NEW] Custom frontmatter fields enable organization-specific metadata
- REQ-406: Metadata in frontmatter provides defaults that markers can override per-requirement

### Marker Processing

- REQ-501: [!] MSL processors must parse and interpret quick markers correctly
- REQ-502: [!] Priority markers must affect requirement priority metadata
- REQ-503: Status markers must affect requirement completion tracking
- REQ-504: Assignment markers must enable requirement ownership queries
- REQ-505: Tag markers must enable requirement categorization and filtering
- REQ-506: Marker conflicts between frontmatter and inline markers must favor inline

### Advanced Validation

- REQ-601: [NEW] Processors must validate inheritance marker consistency
- REQ-602: [NEW] Override markers require existence of parent requirement with same ID
- REQ-603: [NEW] New markers must not conflict with existing parent requirement IDs
- REQ-604: [NEW] Variable references must resolve to defined variables
- REQ-605: [NEW] Template validation must ensure all variables have defaults or are provided
- REQ-606: [NEW] Circular template inheritance must be detected and rejected

### Processing Capabilities

- REQ-701: [@msl-tools] Level 2 processors must support template rendering
- REQ-702: [@msl-tools] Processors must resolve inheritance hierarchies correctly
- REQ-703: [@msl-tools] Processors must provide requirement querying by markers
- REQ-704: [@msl-tools] Processors must validate marker syntax and combinations
- REQ-705: [@msl-tools] Processors must maintain backward compatibility with Levels 0 and 1

## Examples

### Quick Markers Usage

```markdown
## Requirements
- [!] [@alice] [#security] Implement authentication system
- [x] [@bob] [#mvp] Basic user registration complete
- [ ] [#v2] Advanced analytics dashboard
- [?] [#research] Machine learning recommendations
```

### Advanced Inheritance

```markdown
---
id: payment-api
extends: rest-api-base
---

# Payment API

## Requirements
- REQ-001: [INHERIT] Standard REST endpoint design
- REQ-002: [OVERRIDE] Rate limiting: 30 requests per minute for payment ops
- REQ-003: [NEW] PCI DSS compliance required for card processing
```

### Template with Variables

```markdown
---
id: service-template
type: template
variables:
  service_name: GenericService
  max_connections: 100
---

# ${service_name} Configuration

## Requirements
- REQ-001: Maximum ${max_connections} concurrent connections
- REQ-002: Service name must be "${service_name}"
```

## Notes

MSL Level 2 provides the full power of the MSL specification system. The combination of quick markers, advanced inheritance, and templates enables sophisticated specification management for large projects and organizations.

The layered approach ensures that Level 2 documents remain valid Level 1 and Level 0 documents when processed by simpler tools, maintaining universal accessibility while providing advanced capabilities when needed.

Level 2 specifications can drive automated requirement tracking, project management integration, and sophisticated documentation generation workflows.