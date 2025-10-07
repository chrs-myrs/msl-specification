---
msl: L2
id: msl-extension-standards
version: 1.0.0
tags: [standards, extensions, design, architecture]
priority: high
status: active
assignee: msl-core-team
references:
  - msl-l2-advanced: "Uses MSL Level 2 features"
  - msl-usage-standards: "Core MSL quality and usage guidelines (REQ-601-609 for documentation, REQ-201-209 for architecture)"
  - msl-validation-agent: "Automated quality validation (REQ-501-505)"
---

# MSL Extension Standards [MSL]

## Summary

This specification defines the design principles, quality standards, and best practices for creating MSL extensions. MSL extensions add domain-specific features while maintaining compatibility with core MSL, enabling specialized specification patterns for different industries, domains, and organizational needs.

These extension standards ensure that MSL extensions are well-designed, maintainable, interoperable, and provide clear value over alternative approaches.

## Requirements

### Extension Design Principles

- REQ-001: [!] Extensions must clearly document added features and their specific purpose
- REQ-002: [!] Extensions must not break core MSL functionality or backward compatibility
- REQ-003: Extensions must extend appropriate MSL levels (typically msl-l2-advanced)
- REQ-004: Extensions must provide clear value proposition over base MSL features
- REQ-005: Extensions must follow MSL usage standards and architectural principles

### Extension Quality Criteria

- REQ-101: [!] [NEW] Extensions must address problems reported by ≥3 organizations or reduce specification complexity by ≥30%
- REQ-102: [NEW] Extensions must provide ≥25% improvement in: lines of code, processing time, or error reduction
- REQ-103: [x] [NEW] Extensions must comply with `msl-usage-standards.REQ-601-609` for documentation
- REQ-104: [NEW] Extensions must score ≥80/100 on maintainability metrics (see `msl-usage-standards.REQ-701-710`)
- REQ-105: [ ] [@community] [NEW] Public extensions should target adoption by ≥5 organizations

### Compatibility Requirements

- REQ-201: [!] [NEW] Extensions must maintain backward compatibility: existing specs remain valid, behavior unchanged
- REQ-202: [x] [NEW] Breaking changes require major version increment and migration guide
- REQ-203: [NEW] Behavioral changes must be documented with before/after examples
- REQ-204: [ ] [@migration-team] [NEW] Migration paths must include automated conversion tools when feasible
- REQ-205: [NEW] Extensions must degrade gracefully: fail to L2 behavior when extension unsupported

### Extension Architecture Standards

- REQ-301: [!] [NEW] Extensions must follow architectural principles from `msl-usage-standards.REQ-201-209`
- REQ-302: [x] [NEW] Extensions must maintain cohesion score ≥85/100 for their specialized domain
- REQ-303: [x] [NEW] Extensions must have coupling score ≤15/100 with unrelated specifications
- REQ-304: [!] [#limit] [NEW] Extension inheritance chains must not exceed 4 levels total depth
- REQ-305: [ ] [@arch-review] [NEW] Extensions requiring multiple concerns must use composition pattern

### Semantic Design Standards

- REQ-401: [x] [NEW] Extension markers must follow pattern: `[domain-action]` (e.g., `[api-version]`, `[test-coverage]`)
- REQ-402: [NEW] Extension syntax must pass readability test: 80% comprehension by non-experts
- REQ-403: [x] [NEW] Extension features must compose with L2 features without conflicts
- REQ-404: [NEW] Extension behavior must be deterministic: same input → same output 100% of time
- REQ-405: [!] [NEW] Extensions must have <10% feature overlap with core MSL or published extensions

### Documentation Requirements

- REQ-501: [!] [NEW] Extensions must comply with all documentation standards in `msl-usage-standards.REQ-601-609`
- REQ-502: [x] [NEW] Extensions must additionally provide: integration guide, migration path, compatibility matrix
- REQ-503: [ ] [@doc-team] [NEW] Extension examples must show: basic usage, advanced patterns, anti-patterns
- REQ-504: [NEW] Extension documentation must include performance impact: processing time, memory usage
- REQ-505: [x] [NEW] Extension changelog must follow semantic versioning with breaking changes highlighted

### Versioning and Evolution Standards

- REQ-601: Extensions must follow semantic versioning principles (major.minor.patch)
- REQ-602: Extension major versions must provide clear migration paths
- REQ-603: Extensions must maintain backward compatibility within major versions
- REQ-604: Extension deprecation must provide adequate notice and alternatives
- REQ-605: Extensions must evolve conservatively to maintain ecosystem stability

### Community Standards

- REQ-701: Public extensions should be designed for broad community adoption
- REQ-702: Extensions should include contribution guidelines for community involvement
- REQ-703: Extensions should provide clear support and maintenance commitments
- REQ-704: Extensions should avoid vendor lock-in or proprietary dependencies
- REQ-705: Extensions should be licensed compatibly with MSL ecosystem

## Extension Categories

### Domain-Specific Extensions

- REQ-801: API specification extensions for REST, GraphQL, or other API patterns
- REQ-802: Security specification extensions for compliance and vulnerability management
- REQ-803: Infrastructure specification extensions for deployment and operations
- REQ-804: Testing specification extensions for test case and coverage management
- REQ-805: Documentation specification extensions for technical writing workflows

### Organizational Extensions

- REQ-901: Enterprise extensions for compliance reporting and audit trails
- REQ-902: Workflow extensions for approval processes and change management
- REQ-903: Integration extensions for tool-specific import/export capabilities
- REQ-904: Governance extensions for policy enforcement and standards compliance
- REQ-905: Collaboration extensions for team coordination and communication

### Technical Extensions

- REQ-1001: Validation extensions for custom quality rules and metrics
- REQ-1002: Rendering extensions for specialized output formats and templates
- REQ-1003: Processing extensions for custom inheritance and composition patterns
- REQ-1004: Analysis extensions for requirement mining and gap identification
- REQ-1005: Automation extensions for CI/CD integration and workflow triggers

## Quality Assessment

### Extension Evaluation Criteria

- REQ-1101: Problem-solution fit: Does extension address real, unmet needs?
- REQ-1102: Design quality: Is extension well-architected and maintainable?
- REQ-1103: Documentation quality: Is extension clearly explained and exemplified?
- REQ-1104: Community value: Does extension benefit broader MSL ecosystem?
- REQ-1105: Compatibility: Does extension integrate cleanly with core MSL?

### Extension Review Process

- REQ-1201: New extensions must undergo design review before implementation
- REQ-1202: Extension quality must be assessed against these standards
- REQ-1203: Extension compatibility must be validated across MSL tools
- REQ-1204: Extension documentation must be reviewed for completeness and clarity
- REQ-1205: Extension adoption and feedback must be monitored post-release

## Examples

### Well-Designed API Extension

```markdown
---
id: rest-api-extension
extends: msl-l2-advanced
type: extension
tags: [api, rest, web-services]
version: 1.0.0
adds:
  markers:
    - "[#endpoint]": "HTTP endpoint specification"
    - "[#auth]": "Authentication requirement"
    - "[#rate-limit]": "Rate limiting specification"
  sections:
    - "## API Endpoints": "Required endpoint documentation"
    - "## Authentication": "API authentication methods"
---

# REST API Extension for MSL

## Summary
Extension for specifying RESTful APIs using MSL, adding HTTP-specific markers and sections.

## Requirements
- REQ-001: [#endpoint] All API endpoints must be documented with HTTP method and path
- REQ-002: [#auth] Authentication requirements must be clearly specified
- REQ-003: [#rate-limit] Rate limiting policies must be defined for each endpoint
```

### Security Extension Pattern

```markdown
---
id: security-extension
extends: msl-l2-advanced
type: extension
tags: [security, compliance, audit]
version: 1.0.0
adds:
  markers:
    - "[#vuln]": "Security vulnerability requirement"
    - "[#compliance]": "Compliance requirement"
    - "[#audit]": "Audit trail requirement"
---

# Security Extension for MSL

## Requirements
- REQ-001: [#vuln] All input validation requirements must be specified
- REQ-002: [#compliance] GDPR data handling requirements must be documented
- REQ-003: [#audit] All security-relevant actions must generate audit logs
```

### Governance Framework Extension (LiveSpec)

LiveSpec demonstrates domain-specific extensions for governance frameworks:

```yaml
---
criticality: CRITICAL
failure_mode: Framework unsecured without proper governance
constrained_by:
  - .livespec/standard/metaspecs/behavior.spec.md
derives_from:
  - PURPOSE.md
specifies: dist/prompts/4-evolve/4a-detect-drift.md
---
```

**Pattern**: Document-level priority + traceability for 50+ policy specifications
**Domain**: Methodology frameworks, standards bodies, compliance documentation
**Reference**: https://github.com/chrs-myrs/livespec

## Extension Registry

### Registry Requirements

- REQ-1201: [!] [@registry-team] [NEW] Public extensions must be registered in community extension registry
- REQ-1202: [NEW] Registry must include: search by domain, version compatibility matrix, adoption metrics
- REQ-1203: [x] [NEW] Registry entries must provide: description, examples, documentation link, maintainer contact
- REQ-1204: [NEW] Registry must validate extensions score ≥80/100 before listing
- REQ-1205: [ ] [NEW] Registry should provide automated compatibility testing between extensions

## Anti-Patterns

### Extension Anti-Patterns to Avoid

- REQ-1301: [#anti-pattern] Kitchen sink extensions that add unrelated features
- REQ-1302: [#anti-pattern] Extensions that duplicate existing MSL functionality
- REQ-1303: [#anti-pattern] Extensions that break MSL semantic consistency
- REQ-1304: [#anti-pattern] Extensions with poor documentation or unclear purpose
- REQ-1305: [#anti-pattern] Extensions that create vendor lock-in or proprietary dependencies
- REQ-1306: [#anti-pattern] Extensions that add frontmatter fields duplicating `[!]` marker functionality (use requirement-level markers instead)

## Notes

MSL extensions enable domain-specific specialization while maintaining the core MSL philosophy of simplicity and progressive enhancement. Well-designed extensions should feel like natural additions to MSL rather than external bolt-ons.

These standards ensure that the MSL extension ecosystem remains healthy, interoperable, and valuable to the broader community while avoiding fragmentation and compatibility issues.

### Implementation References

- **Quality Validation**: Use `msl-validation-agent` to validate extension quality (≥80/100 required)
- **Architecture Standards**: Follow `msl-usage-standards.REQ-201-209` for architectural principles
- **Documentation Standards**: Comply with `msl-usage-standards.REQ-601-609` for documentation
- **Example Extensions**: See `applications/` directory for well-designed extension examples

### Rationale for Key Thresholds

- **≥3 organizations**: Ensures extension addresses genuine widespread need, not single-org customization
- **≥25% improvement**: Justifies complexity cost of extension vs using base MSL
- **<10% feature overlap**: Prevents fragmentation and confusion in extension ecosystem
- **≥80/100 quality score**: Ensures production readiness and maintainability

---
*Specification format: [MSL Level 2](https://github.com/chrs-myrs/msl-specification)*