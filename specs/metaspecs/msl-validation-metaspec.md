---
msl: L2
id: msl-validation-metaspec
type: metaspec
version: 1.0.0
tags: [metaspec, validation, quality, standards]
priority: high
status: active
---

# MSL Validation Metaspec [MSL]

## Summary

This metaspec governs all specifications that define validation rules, quality standards, and compliance requirements for MSL documents. It ensures that validation specifications provide clear, measurable, and implementable criteria for assessing specification quality.

Validation specifications differ from language specifications - they define quality metrics and best practices rather than syntax and semantics.

## Structural Requirements

### Validation Specification Sections

- REQ-001: [!] MUST have `## Requirements` section with validation criteria
- REQ-002: [!] MUST have `## Validation Process` section describing how validation is performed
- REQ-003: [!] MUST have `## Quality Metrics` section with measurable thresholds
- REQ-004: MUST have `## Examples` section showing compliant and non-compliant specifications
- REQ-005: SHOULD have `## Refactoring Guidelines` section for fixing violations

### Criteria Definition

- REQ-101: [!] Each validation rule MUST be testable with clear pass/fail criteria
- REQ-102: [!] Validation rules MUST specify severity levels (error, warning, info)
- REQ-103: Rules MUST include rationale explaining why the rule exists
- REQ-104: Rules MUST provide actionable fix suggestions
- REQ-105: Rules MUST be grouped into logical categories

## Quality Metric Requirements

### Metric Definition

- REQ-201: [!] Metrics MUST be quantifiable with numeric scores
- REQ-202: [!] Scoring algorithms MUST be clearly defined
- REQ-203: Thresholds MUST be specified for different quality levels
- REQ-204: Metrics MUST be objective and reproducible
- REQ-205: Composite scores MUST show component breakdown

### Threshold Specification

- REQ-301: MUST define minimum acceptable thresholds
- REQ-302: MUST specify ranges for quality grades (excellent, good, acceptable, poor)
- REQ-303: MUST explain consequences of falling below thresholds
- REQ-304: SHOULD provide industry benchmarks when available

## Validation Process Requirements

### Process Documentation

- REQ-401: [!] MUST describe validation workflow step-by-step
- REQ-402: MUST specify order of validation checks
- REQ-403: MUST define when validation should occur (commit, PR, release)
- REQ-404: MUST specify which validations are blocking vs advisory
- REQ-405: MUST describe how to handle validation exceptions

### Tool Requirements

- REQ-501: MUST specify required capabilities for validation tools
- REQ-502: MUST define output format for validation reports
- REQ-503: SHOULD provide tool configuration examples
- REQ-504: SHOULD specify performance requirements for validators

## Compliance Requirements

### Standards Alignment

- REQ-601: [!] Validation rules MUST align with MSL core principles
- REQ-602: Rules MUST NOT contradict language specifications
- REQ-603: Rules MUST support progressive enhancement philosophy
- REQ-604: Rules MUST maintain backward compatibility awareness

### Enforcement Levels

- REQ-701: MUST distinguish mandatory from recommended practices
- REQ-702: MUST specify enforcement contexts (development, CI, production)
- REQ-703: MUST define override/exception mechanisms
- REQ-704: MUST provide compliance reporting formats

## Example Requirements

### Positive and Negative Examples

- REQ-801: [!] MUST provide examples of specifications that pass validation
- REQ-802: [!] MUST provide examples of common violations
- REQ-803: MUST show before/after refactoring examples
- REQ-804: Examples MUST cover all major validation categories
- REQ-805: Examples MUST be realistic and representative

## Examples

### Compliant Validation Specification Structure

```markdown
---
id: api-validation-standards
governed-by: msl-validation-metaspec
type: validation
---

# API Specification Validation Standards [MSL]

## Requirements

### Structure Validation
- REQ-001: [!] API specs MUST have endpoints section
- REQ-002: [!] Each endpoint MUST specify HTTP method
- REQ-003: Endpoints MUST include request/response examples

## Quality Metrics

### Completeness Score (0-100)
- Endpoints documented: 40 points
- Authentication specified: 20 points  
- Error codes defined: 20 points
- Examples provided: 20 points

### Quality Thresholds
- Excellent: 90-100 (ready for production)
- Good: 75-89 (ready for review)
- Acceptable: 60-74 (needs improvement)
- Poor: <60 (requires significant work)

## Validation Process

1. Parse specification structure
2. Check required sections
3. Validate endpoint definitions
4. Calculate quality scores
5. Generate validation report

## Examples

### Compliant Specification
```markdown
## Endpoints
- `GET /users` - List users
  Request: `GET /api/users?page=1`
  Response: `200 OK {"users": [...]}`
```

### Non-Compliant Specification
```markdown
## Endpoints
- Get users endpoint exists
```

## Refactoring Guidelines

- Add missing HTTP methods
- Include request/response examples
- Specify authentication requirements
```

### Quality Metric Example

```yaml
DRY Compliance Metrics:
  calculation: |
    unique_requirements / total_requirements * 100
  thresholds:
    excellent: >= 95%
    good: >= 85%
    acceptable: >= 75%
    poor: < 75%
  severity: 
    < 75%: error
    75-85%: warning
    85-95%: info
```

## Notes

Validation metaspecs ensure that quality standards are consistently defined and measurable. They bridge the gap between language specifications (what is valid) and best practices (what is good).

Key principles for validation specifications:
1. **Measurable** - Quantifiable metrics, not subjective judgments
2. **Actionable** - Clear guidance on fixing violations
3. **Proportional** - Severity matches actual impact
4. **Automated** - Can be checked by tools, not just humans

This metaspec ensures all MSL validation specifications provide practical, implementable quality standards that improve specification quality without creating unnecessary barriers.

---
*Specification format: [MSL Level 2](https://github.com/chrs-myrs/msl-specification)*