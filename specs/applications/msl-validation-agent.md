---
msl: L2
id: msl-validation-agent
tags: [agent, validation, architecture, quality, claude-code]
priority: critical
status: active
assignee: msl-validation-team
references:
  - msl-usage-standards: "Quality standards this agent enforces (REQ-001-710)"
  - msl-extension-standards: "Extension design principles to validate (REQ-001-505)"
  - msl-l2-advanced: "MSL language definition being validated"
---

# MSL Validation Agent Specification [MSL]

## Summary

This specification defines a Claude Code agent that performs intelligent architectural validation of MSL specifications. The agent evaluates MSL documents against the quality standards defined in `msl-usage-standards.md` and `msl-extension-standards.md`, providing high-level architectural feedback beyond basic syntax validation.

This agent demonstrates MSL's capability to specify intelligent software systems and serves as a practical example of using MSL to define AI agent behavior and requirements.

**Note:** This specification uses MSL to define an AI agent that validates MSL specifications, creating a recursive self-validation capability.

## Requirements

### Agent Core Capabilities

- REQ-001: [!] [@agent] Agent must analyze MSL specifications for architectural quality
- REQ-002: [!] [@agent] Agent must validate compliance with MSL usage standards
- REQ-003: [!] [@agent] Agent must assess extension quality against extension standards
- REQ-004: [@agent] Agent must provide ≥3 prioritized recommendations per critical issue found
- REQ-005: [@agent] Agent must generate quality metrics (0-100 scale) with category breakdowns

### Common Validation Patterns

- REQ-101: [!] [@agent] [NEW] Agent must detect violations using configurable thresholds:
  - 100% text match = duplicate (critical)
  - >80% similarity = near-duplicate (high)
  - >60% pattern match = template opportunity (medium)
- REQ-102: [!] [@agent] [NEW] Agent must analyze structural patterns for improvement opportunities
- REQ-103: [@agent] [NEW] Agent must provide specific refactoring recommendations with examples
- REQ-104: [@agent] [NEW] Agent must prioritize violations by impact (critical/high/medium/low)

### DRY Principle Validation

- REQ-111: [!] [@agent] [INHERIT] Common validation patterns from REQ-101-104 for DRY analysis
- REQ-112: [@agent] [NEW] Agent must detect duplicate requirements within inheritance chain
- REQ-113: [@agent] [NEW] Agent must recommend base specification extraction when ≥3 duplicates found
- REQ-114: [@agent] [NEW] Agent must identify shared terminology requiring centralization

### Inheritance Protocol Validation

- REQ-201: [!] [@agent] [INHERIT] Common validation patterns from REQ-101-104 for inheritance analysis
- REQ-202: [!] [@agent] [NEW] Agent must validate "is-a" relationships with >85% semantic alignment
- REQ-203: [@agent] [NEW] Agent must flag inheritance chains exceeding 4 levels depth
- REQ-204: [@agent] [NEW] Agent must detect and report circular dependencies within 100ms
- REQ-205: [@agent] [NEW] Agent must validate correct usage of [OVERRIDE], [NEW], [INHERIT] markers

### Architecture Quality Assessment

- REQ-301: [!] [@agent] [INHERIT] Common validation patterns from REQ-101-104 for architecture analysis
- REQ-302: [!] [@agent] [NEW] Agent must calculate cohesion score: related requirements ÷ total requirements × 100
- REQ-303: [@agent] [NEW] Agent must measure coupling: external dependencies ÷ total requirements × 100
- REQ-304: [@agent] [NEW] Agent must identify improvements reducing coupling by ≥20% or increasing cohesion by ≥15%
- REQ-305: [@agent] [NEW] Agent must validate single responsibility with ≥85% requirement alignment to primary concern

### Requirement Quality Analysis

- REQ-401: [!] [@agent] [INHERIT] Common validation patterns from REQ-101-104 for requirement analysis
- REQ-402: [!] [@agent] [NEW] Agent must flag requirements lacking measurable criteria (pass/fail threshold)
- REQ-403: [@agent] [NEW] Agent must identify ambiguous terms and suggest specific replacements:
  - "fast" → "completes within X seconds"
  - "user-friendly" → "requires ≤X clicks"
  - "scalable" → "handles X concurrent users"
- REQ-404: [@agent] [NEW] Agent must validate requirement atomicity: 1 assertion per requirement
- REQ-405: [@agent] [NEW] Agent must ensure ≥90% requirements have testable acceptance criteria

### Extension Validation

- REQ-501: [@agent] Agent must validate extension design against extension standards
- REQ-502: [@agent] Agent must assess extension value proposition and purpose clarity
- REQ-503: [@agent] Agent must verify extension compatibility with core MSL
- REQ-504: [@agent] Agent must evaluate extension documentation quality
- REQ-505: [@agent] Agent must identify extension anti-patterns and design issues

### Intelligent Recommendations

- REQ-601: [!] [@agent] [NEW] Agent must provide ≥3 specific recommendations per major issue with:
  - Concrete fix with before/after example
  - Estimated effort (low/medium/high)
  - Impact assessment (critical/high/medium/low)
  - Rationale explaining the improvement
- REQ-602: [@agent] [NEW] Agent must prioritize recommendations using impact/effort matrix
- REQ-603: [@agent] [NEW] Agent must group recommendations by category: structure, architecture, quality, organization
- REQ-604: [@agent] [NEW] Agent must provide implementation guidance with code examples when applicable

### Platform Integration Requirements

- REQ-701: [!] [@agent] [NEW] Agent must provide platform-agnostic core validation engine
- REQ-702: [@agent] [NEW] Agent must support adapter pattern for different platforms
- REQ-703: [@agent] [NEW] Agent must expose standardized API for validation operations
- REQ-704: [@agent] [NEW] Agent must support configuration via JSON/YAML for organizational standards
- REQ-705: [@agent] [NEW] Agent must maintain validation history with timestamp and version tracking

### Claude Code Integration

- REQ-711: [!] [@claude-code] [NEW] Claude Code adapter must implement agent system integration
- REQ-712: [@claude-code] [NEW] Must support Claude Code's subagent_type: "msl-validator"
- REQ-713: [@claude-code] [NEW] Must provide Claude-specific metadata and prompts for agent generation
- REQ-714: [@claude-code] [NEW] Must support batch processing via Task tool with file paths
- REQ-715: [@claude-code] [NEW] Must output markdown reports compatible with Claude Code interface

### Reporting and Feedback

- REQ-801: [!] [@agent] [NEW] Agent must generate markdown reports containing:
  - Quality score (0-100) with breakdown by category
  - Issues list with severity (critical/high/medium/low)
  - ≥3 prioritized recommendations per major issue
  - Executive summary (≤5 sentences)
- REQ-802: [@agent] [NEW] Agent must track quality trends across validation runs
- REQ-803: [@agent] [NEW] Agent must highlight critical issues in report summary within first 100 words
- REQ-804: [@agent] [NEW] Agent must support custom report templates via configuration

### Self-Validation Capability

- REQ-901: [!] [#meta] Agent must be able to validate its own specification when requested
- REQ-902: [#meta] Agent must demonstrate recursive validation capability
- REQ-903: [#meta] Agent must validate the MSL standards it enforces when requested
- REQ-904: [#meta] Agent must provide feedback on MSL specification quality overall
- REQ-905: [#meta] Agent must identify opportunities for MSL standard improvements

## Agent Behavior Specification

### Validation Workflow

- REQ-1001: [!] [@workflow] Agent must follow consistent validation workflow across all specifications
- REQ-1002: [@workflow] Parse specification structure and extract metadata
- REQ-1003: [@workflow] Analyze inheritance chains and dependency relationships
- REQ-1004: [@workflow] Evaluate requirements against quality standards
- REQ-1005: [@workflow] Generate recommendations and quality metrics
- REQ-1006: [@workflow] Produce structured reports with actionable feedback

### Error Handling

- REQ-1101: [@agent] Agent must handle malformed MSL documents gracefully
- REQ-1102: [@agent] Agent must provide clear error messages for parsing failures
- REQ-1103: [@agent] Agent must continue analysis when possible despite errors
- REQ-1104: [@agent] Agent must report both structural and content quality issues
- REQ-1105: [@agent] Agent must distinguish between critical errors and improvement suggestions

### Performance Requirements

- REQ-1201: [!] [@agent] [NEW] Agent must process specifications: ≤10 reqs in <1s, ≤100 reqs in <5s, ≤1000 reqs in <30s
- REQ-1202: [@agent] [NEW] Agent must handle specification sets up to 100 documents with <2GB memory
- REQ-1203: [@agent] [NEW] Agent must provide progress updates every 5 seconds for operations >5s
- REQ-1204: [@agent] [NEW] Agent must achieve ≥70% parallel processing efficiency on multi-core systems
- REQ-1205: [@agent] [NEW] Agent must improve repeat validation performance by ≥50% via caching

## Usage Examples

### Basic Validation Command

```bash
# Validate single specification
msl-validate-agent specs/user-auth.md

# Validate specification set
msl-validate-agent specs/

# Generate detailed report
msl-validate-agent specs/ --report=detailed --format=json
```

### Expected Output Format

```json
{
  "specification": "specs/user-auth.md",
  "quality_score": 85,
  "issues": [
    {
      "type": "DRY_VIOLATION",
      "severity": "medium",
      "location": "REQ-003",
      "message": "Requirement duplicated in authentication-base.md",
      "recommendation": "Use inheritance: extends authentication-base"
    }
  ],
  "metrics": {
    "dry_score": 78,
    "cohesion_score": 92,
    "coupling_score": 85,
    "inheritance_depth": 2
  },
  "recommendations": [
    {
      "category": "inheritance",
      "priority": "high",
      "description": "Extract common authentication patterns into base specification"
    }
  ]
}
```

### Validation Report Example

```markdown
# MSL Validation Report: User Authentication Specification

## Quality Score: 85/100

### Issues Found (2 medium, 1 low)

#### DRY Violations
- **REQ-003**: Duplicated in `authentication-base.md`
  - *Recommendation*: Use `extends: authentication-base` and `[INHERIT]` marker

#### Architecture
- **Cohesion**: High (92/100) - Requirements well-focused on authentication
- **Coupling**: Good (85/100) - Minimal external dependencies

### Recommendations
1. **High Priority**: Extract shared authentication patterns into base specification
2. **Medium Priority**: Add acceptance criteria to REQ-005 and REQ-007
3. **Low Priority**: Consider splitting OAuth requirements into separate extension
```

## Integration with MSL Ecosystem

### Tool Integration

- REQ-1301: [@integration] Agent must integrate with existing MSL tools (msl-lint, msl-render)
- REQ-1302: [@integration] Agent must complement syntax validation with architectural analysis
- REQ-1303: [@integration] Agent must provide consistent CLI interface with other MSL tools
- REQ-1304: [@integration] Agent must support configuration files for organizational customization
- REQ-1305: [@integration] Agent must integrate with CI/CD pipelines for automated quality checks

### Ecosystem Enhancement

- REQ-1401: [@ecosystem] Agent enhances MSL specification quality across projects
- REQ-1402: [@ecosystem] Agent promotes MSL best practices through automated guidance
- REQ-1403: [@ecosystem] Agent identifies common patterns for potential MSL core enhancements
- REQ-1404: [@ecosystem] Agent provides data for MSL language evolution decisions
- REQ-1405: [@ecosystem] Agent demonstrates MSL's capability for specifying intelligent systems

## Notes

This MSL validation agent represents a sophisticated example of using MSL to specify intelligent software behavior. The agent's ability to validate MSL specifications demonstrates MSL's expressive power and creates a recursive self-improvement capability for the MSL ecosystem.

The agent serves as both a practical quality assurance tool and a showcase of MSL's potential for specifying complex, intelligent systems that understand and improve MSL itself.

---
*Specification format: [MSL Level 2](https://github.com/chrs-myrs/msl-specification)*