---
msl: L2
id: msl-usage-standards
extends: msl-l2-advanced
tags: [standards, best-practices, quality, architecture]
priority: critical
status: active
assignee: msl-core-team
---

# MSL Usage Standards [MSL]

## Summary

This specification defines the quality standards, best practices, and architectural principles for effective MSL usage. These standards ensure that MSL specifications are maintainable, reusable, consistent, and follow sound software engineering principles.

These usage standards serve as the foundation for architectural validation and quality assessment of MSL specification sets, enabling both human reviewers and automated agents to evaluate specification quality.

**Related Specifications:**
- See `msl-extension-standards` (REQ-001-105) for extension design guidelines
- See `msl-validation-agent` (REQ-101-405) for automated validation implementation
- See `msl-l2-advanced` for complete MSL language features

## Requirements

### DRY (Don't Repeat Yourself) Principles

- REQ-001: [!] [NEW] Specifications must avoid duplicate requirements across different documents
- REQ-002: [!] [@review-team] [NEW] Common requirement patterns must be extracted into base specifications or templates
- REQ-003: [x] [NEW] Identical or near-identical requirements must use inheritance instead of copy-paste
- REQ-004: [x] [NEW] Shared terminology and definitions must be centralized in base specifications  
- REQ-005: [ ] [@automation-team] [NEW] Copy-paste violations must be identified and refactored using appropriate MSL features

#### DRY Violation Thresholds

- REQ-006: [!] [#metric] Requirements with 100% identical text across specifications violate DRY
- REQ-007: [#metric] Requirements with >80% text similarity should use template variables
- REQ-008: [#metric] Three or more repeated patterns indicate need for base specification extraction

### Inheritance Protocol Standards

- REQ-101: [!] [NEW] Inheritance must be used when extending or modifying existing behavior
- REQ-102: [!] [#limit] [NEW] Inheritance chains must not exceed 4 levels deep for maintainability
- REQ-103: [x] [NEW] Child specifications must inherit from the most appropriate abstraction level
- REQ-104: [x] [NEW] Inheritance should create logical "is-a" relationships between specifications
- REQ-105: [ ] [@arch-team] [NEW] Multiple inheritance or composition should be used for "has-a" relationships

#### Inheritance Anti-Patterns

- REQ-106: [#anti-pattern] Deep inheritance chains (>4 levels) create maintenance complexity
- REQ-107: [#anti-pattern] Inheriting from unrelated specifications violates logical relationships
- REQ-108: [#anti-pattern] Using inheritance for code reuse without logical relationship
- REQ-109: [#anti-pattern] Circular inheritance dependencies must be prevented

### Specification Architecture Standards

- REQ-201: [!] Each specification must have a single, well-defined primary concern
- REQ-202: Specifications must maintain high cohesion within their domain
- REQ-203: Specifications must minimize coupling to unrelated domains
- REQ-204: Specification granularity must be appropriate - neither too fine nor too coarse
- REQ-205: Logical dependencies must form an acyclic directed graph

#### Architecture Quality Metrics

- REQ-206: Specification cohesion measured by requirement relatedness within document
- REQ-207: Specification coupling measured by external dependencies and references
- REQ-208: Specification depth measured by inheritance chain length
- REQ-209: Specification breadth measured by number of direct children

### Template Usage Standards

- REQ-301: Templates must define reusable specification patterns with clear parameters
- REQ-302: Template variables must have meaningful names and documented purposes
- REQ-303: Templates must provide sensible defaults for optional variables
- REQ-304: Template inheritance chains must follow same depth limits as regular inheritance
- REQ-305: Templates must be designed for extension and customization

#### Template Best Practices

- REQ-306: Templates should represent domain-specific specification families
- REQ-307: Template variables should enable meaningful customization without breaking intent
- REQ-308: Template documentation must include usage examples and customization guidelines
- REQ-309: Template versions should maintain backward compatibility when possible

### Requirement Quality Standards

- REQ-401: [!] [NEW] Requirements must be testable with pass/fail criteria
- REQ-402: [!] [@qa-team] [NEW] Requirements must have explicit acceptance criteria or measurable thresholds
- REQ-403: [x] [NEW] Requirements must use consistent terminology across specification set
- REQ-404: [NEW] Requirements must match audience: high-level for stakeholders, detailed for implementers
- REQ-405: [x] [NEW] Requirements must specify "what" not "how" - behavior over implementation

#### Requirement Writing Guidelines

- REQ-406: [x] Requirements should use active voice (subject performs action)
- REQ-407: [!] [#quality] Requirements must avoid subjective terms - replace with measurable criteria:
  - Instead of "fast" → "completes within 2 seconds"
  - Instead of "user-friendly" → "requires ≤3 clicks to complete"
  - Instead of "scalable" → "handles 1000 concurrent users"
- REQ-408: [x] Requirements should specify thresholds: percentages, time limits, or quantities
- REQ-409: [!] Requirements must be atomic - one testable assertion per requirement
- REQ-410: [ ] [@doc-team] Requirements should include rationale in Notes when purpose unclear

### Naming and Organization Standards

- REQ-501: Specification IDs must use consistent naming conventions (kebab-case)
- REQ-502: Specification titles must clearly indicate purpose and scope
- REQ-503: Requirement IDs must be unique within specification and follow REQ-XXX format
- REQ-504: Directory structure must reflect logical organization of specification domains
- REQ-505: File names must be descriptive and indicate specification purpose

#### Naming Convention Examples

- REQ-506: [#example] `user-authentication.md` better than `auth.md` or `UserAuth.md`
- REQ-507: [#example] `REQ-001` through `REQ-999` within single specification
- REQ-508: [#example] Group related requirements with consistent numbering (REQ-100-199 for security)
- REQ-509: [#example] Specification IDs should match file names without extension


### Documentation Standards

- REQ-601: Specifications must include summary section explaining purpose and scope
- REQ-602: Specifications must provide examples demonstrating key concepts
- REQ-603: Specifications must document relationships to other specifications
- REQ-604: Specifications must include notes section for additional context when needed
- REQ-605: Specifications must maintain change history and version information

#### Documentation Quality Requirements

- REQ-606: Summary sections must be concise but complete explanations of specification purpose
- REQ-607: Examples must be realistic and demonstrate actual usage patterns
- REQ-608: Notes sections must provide context not captured in requirements
- REQ-609: Specifications must explain rationale for major design decisions

### Quality Metrics and Validation

- REQ-701: [!] [@validation-team] [NEW] Specifications must achieve minimum quality score of 80/100
- REQ-702: [x] [#metric] DRY compliance: <20% requirement duplication across specifications
- REQ-703: [x] [#metric] Inheritance depth: ≤4 levels with logical "is-a" relationships
- REQ-704: [x] [#metric] Requirement testability: ≥90% with clear pass/fail criteria
- REQ-705: [x] [#metric] Cohesion/Coupling ratio: >0.8 (high cohesion, low coupling)

#### Quality Scoring Thresholds

- REQ-706: [#scoring] Excellent: 90-100 points - exemplary specification
- REQ-707: [#scoring] Good: 80-89 points - production ready
- REQ-708: [#scoring] Acceptable: 70-79 points - needs minor improvements
- REQ-709: [#scoring] Poor: <70 points - requires significant refactoring
- REQ-710: [!] [#validation] Specifications scoring <70 must be refactored before acceptance

### Cross-Specification Relationships

- REQ-801: [!] [NEW] Specifications must explicitly reference related specifications using `document-id.REQ-XXX` format
- REQ-802: [NEW] Cross-references must be bidirectional when specifications depend on each other
- REQ-803: [NEW] Reference graph depth should not exceed 3 levels to prevent complexity
- REQ-804: [#validation] Broken references to non-existent specifications must be fixed
- REQ-805: [NEW] Reference purposes: extends (inheritance), uses (dependency), validates (quality check)

### Refactoring Guidelines

- REQ-851: Specifications violating DRY principles must be refactored using inheritance or templates
- REQ-852: Deep inheritance chains must be refactored to reduce complexity
- REQ-853: Low-cohesion specifications must be split into focused documents
- REQ-854: Highly-coupled specifications must be refactored to reduce dependencies
- REQ-855: Refactoring must preserve semantic meaning and requirement traceability

#### Refactoring Patterns

- REQ-856: [x] Extract common base specification from duplicated requirements
- REQ-857: [x] Create templates from repeated specification patterns
- REQ-858: [ ] Split specifications by primary concern to increase cohesion
- REQ-859: [ ] Use composition instead of inheritance for unrelated functionality
- REQ-860: [ ] Merge related specifications if separation provides no value

## Validation Process

### Automated Validation

- REQ-901: [!] [@automation] [NEW] Automated agents must validate specifications against all usage standards
- REQ-902: [x] [NEW] Validation must identify violations with: file, line number, severity, fix suggestion
- REQ-903: [x] [NEW] Validation must generate scores: DRY, Inheritance, Cohesion, Coupling, Overall
- REQ-904: [ ] [@tools-team] [NEW] Validation must support batch processing with progress reporting
- REQ-905: [x] [NEW] Validation must output markdown reports for human review

### Manual Review Process

- REQ-1001: [!] [@review-team] [NEW] Human reviewers must verify quality score ≥80 before approval
- REQ-1002: [x] [NEW] Pull requests must include architectural impact assessment
- REQ-1003: [ ] [NEW] Changes reducing quality score >5 points require justification
- REQ-1004: [NEW] Priority levels: Critical (blocks), High (1 day), Medium (1 week), Low (backlog)
- REQ-1005: [x] [@training] [NEW] Teams must complete MSL standards training quarterly

## Examples

### DRY Violation and Fix

**Before (DRY Violation):**
```markdown
# API Specification A
## Requirements
- REQ-001: Must authenticate with API key
- REQ-002: Must return JSON responses
- REQ-003: Must handle rate limiting

# API Specification B  
## Requirements
- REQ-001: Must authenticate with API key
- REQ-002: Must return JSON responses
- REQ-003: Must log all requests
```

**After (DRY Compliant):**
```markdown
# Base API Template
## Requirements
- REQ-001: Must authenticate with API key
- REQ-002: Must return JSON responses

# API Specification A extends Base API Template
## Requirements
- REQ-001: [INHERIT] Must authenticate with API key
- REQ-002: [INHERIT] Must return JSON responses  
- REQ-003: [NEW] Must handle rate limiting

# API Specification B extends Base API Template
## Requirements
- REQ-001: [INHERIT] Must authenticate with API key
- REQ-002: [INHERIT] Must return JSON responses
- REQ-003: [NEW] Must log all requests
```

### Good Inheritance Structure

```markdown
# Foundation: msl-l0-foundation.md (basic markdown)
# Level 1: msl-l1-structure.md extends msl-l0-foundation (adds frontmatter)
# Level 2: msl-l2-advanced.md extends msl-l1-structure (adds markers)
# Extension: api-extension.md extends msl-l2-advanced (adds API features)
# Application: user-api.md extends api-extension (specific API implementation)
```

### Template Usage Example

```markdown
---
id: rest-api-template
type: template
variables:
  service_name: "Generic Service"
  rate_limit: 100
---

# ${service_name} REST API

## Requirements
- REQ-001: Rate limit ${rate_limit} requests per minute
- REQ-002: JSON request/response format required
- REQ-003: HTTPS only for all endpoints
```

## Notes

These usage standards provide the foundation for high-quality MSL specifications. They enable both human developers and automated validation agents to assess and improve specification quality systematically.

Following these standards results in maintainable, reusable, and consistent specification sets that effectively capture requirements while avoiding common architectural problems.

### Implementation References

- **Automated Validation**: See `msl-validation-agent.REQ-101` through `REQ-405` for agent implementation
- **Extension Design**: See `msl-extension-standards.REQ-001` through `REQ-105` for extension guidelines  
- **Tool Support**: See `msl-tools-spec.REQ-601` through `REQ-605` for linting implementation
- **Batch Processing**: See `msl-batch-validator.REQ-301` through `REQ-305` for project-wide validation

### Rationale for Key Limits

- **4-level inheritance limit**: Balances reusability with comprehension complexity
- **80% similarity threshold**: Empirically determined to catch meaningful duplication
- **80/100 minimum score**: Ensures production-ready quality while allowing minor issues

---
*Specification format: [MSL Level 2](https://github.com/chrs-myrs/msl-specification)*