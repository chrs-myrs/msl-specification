---
msl: L2
id: msl-batch-validator
extends: msl-tools-spec
tags: [tools, validation, batch-processing, cli]
priority: high
status: active
assignee: msl-tools-team
references:
  - msl-validation-agent: "Individual specification validator (REQ-001-1205)"
  - msl-usage-standards: "Quality standards to enforce (REQ-701-710)"
  - msl-tools-spec: "Common CLI patterns (REQ-1401-1407)"
---

# MSL Batch Validation Tool [MSL]

## Summary

This specification defines a batch validation tool that validates all MSL specifications within a directory structure, leveraging the MSL validation agent for individual file analysis while providing aggregate reporting and cross-specification insights.

The tool serves as a project-wide quality assurance mechanism, ensuring consistent MSL usage across entire specification sets.

## Requirements

### Core Functionality

- REQ-001: [!] [NEW] Tool must detect MSL specifications using these criteria:
  - Primary: Files containing `## Requirements` section
  - Secondary: Files with `[MSL]` in title (# heading)
  - Tertiary: Files with `msl:` field in YAML frontmatter
  - Extension: `.md` or `.msl` files meeting above criteria
- REQ-002: [!] [NEW] Tool must validate each specification using msl-validation-agent (REQ-001-1205)
- REQ-003: [NEW] Tool must generate both individual and aggregate validation reports in markdown format
- REQ-004: [NEW] Tool must identify MSL level from frontmatter `msl:` field or default to L0
- REQ-005: [NEW] Tool must process inheritance chains in dependency order (parents before children)

### Batch Processing

- REQ-101: [!] [NEW] Tool must process specifications in topological order based on `extends` field
- REQ-102: [NEW] Tool must continue validation after individual failures, reporting all errors at end
- REQ-103: [NEW] Tool must display progress indicator for operations >5 seconds (e.g., "[12/45] Validating user-auth.md")
- REQ-104: [NEW] Tool must support `--level` flag to filter by MSL level (L0, L1, L2)
- REQ-105: [NEW] Tool must support glob patterns for exclusion (e.g., `--exclude="**/drafts/**"`)

### Cross-Specification Analysis

- REQ-201: [!] [NEW] Tool must build inheritance graph from `extends` fields and visualize as tree
- REQ-202: [NEW] Tool must detect broken references (missing parent specs, invalid REQ-XXX refs)
- REQ-203: [NEW] Tool must report distribution metrics: count by level, average score by level
- REQ-204: [NEW] Tool must identify orphaned specifications with no inheritance relationships
- REQ-205: [NEW] Tool must detect and reject circular inheritance within 100ms of detection

### Reporting

- REQ-301: [!] [NEW] Tool must generate summary with these aggregate metrics:
  - Average quality score (0-100)
  - DRY compliance percentage (<20% duplication target)
  - Average inheritance depth (≤4 target)
  - Requirement testability percentage (≥90% target)
  - Distribution by score category per msl-usage-standards.REQ-706-709
- REQ-302: [NEW] Tool must list all specifications with: path, level, score, status (✅/⚠️/❌)
- REQ-303: [NEW] Tool must highlight critical issues (score <70) in first 100 words of report
- REQ-304: [NEW] Tool must provide ≥3 prioritized recommendations using impact/effort matrix
- REQ-305: [NEW] Tool must support verbosity: summary (1 page), normal (with issues), detailed (all feedback)

### CLI Interface

- REQ-401: [!] [INHERIT] Standard CLI behaviors from msl-tools-spec.REQ-1401-1407
- REQ-402: [NEW] Tool must provide `msl-batch-validate <path>` command (defaults to `.`)
- REQ-403: [NEW] Tool must support `--level=L0|L1|L2` flag to filter by MSL level
- REQ-404: [NEW] Tool must support `--threshold=N` flag for minimum acceptable score (default: 80)
- REQ-405: [NEW] Tool must return exit codes: 0 (all pass), 1 (quality issues), 2 (errors)

### Integration

- REQ-501: [!] [NEW] Tool must invoke msl-validation-agent for each specification found
- REQ-502: [NEW] Tool must support `.msl-validate.yml` configuration in project root
- REQ-503: [NEW] Tool must output markdown reports compatible with GitHub/GitLab rendering
- REQ-504: [NEW] Tool must support `--quiet` flag outputting only: score, pass/fail, error count
- REQ-505: [NEW] Tool must cache results with file hash, improving repeat performance by ≥50%

### Error Handling

- REQ-601: [!] [NEW] Tool must handle file access errors gracefully and continue processing
- REQ-602: [NEW] Tool must report malformed specifications as errors but continue validation
- REQ-603: [NEW] Tool must aggregate all errors and report in summary at end
- REQ-604: [NEW] Tool must validate configuration file schema before processing
- REQ-605: [NEW] Tool must provide helpful error messages with file paths and line numbers

### Performance Requirements

- REQ-701: [!] [NEW] Tool must process: ≤10 specs in <2s, ≤100 specs in <30s, ≤1000 specs in <5min
- REQ-702: [NEW] Tool must use ≤500MB memory for specification sets up to 1000 files
- REQ-703: [NEW] Tool must achieve ≥70% parallel processing efficiency on multi-core systems
- REQ-704: [NEW] Tool must display progress updates every 5 seconds for long operations
- REQ-705: [NEW] Tool must support `--jobs=N` flag to control parallel processing threads

## Examples

### Basic Usage

```bash
# Validate all specs in current directory
msl-batch-validate

# Validate specific directory
msl-batch-validate ./specs

# Validate only L2 specifications with custom threshold
msl-batch-validate --level=L2 --threshold=85

# Detailed validation with verbose output
msl-batch-validate --verbose --jobs=4

# CI/CD integration with quiet mode
msl-batch-validate --quiet --threshold=80 || exit 1
```

### Expected Output

```markdown
# MSL Batch Validation Report

## Summary
- **Total Specifications**: 7
- **Average Quality Score**: 91/100
- **Critical Issues**: 0
- **Warnings**: 3

## Specification Scores

| Specification | Level | Score | Status |
|--------------|-------|--------|---------|
| msl-l0-foundation.md | L0 | 92/100 | ✅ Excellent |
| msl-l1-structure.md | L1 | 92/100 | ✅ Excellent |
| msl-l2-advanced.md | L2 | 95/100 | ✅ Excellent |
| msl-usage-standards.md | L2 | 88/100 | ✅ Good |
| msl-extension-standards.md | L2 | 90/100 | ✅ Excellent |
| msl-tools-spec.md | L2 | 89/100 | ✅ Good |
| msl-validation-agent.md | L2 | 91/100 | ✅ Excellent |

## Inheritance Structure
```
msl-l0-foundation
  └── msl-l1-structure
      └── msl-l2-advanced
          ├── msl-usage-standards
          └── msl-extension-standards
```

## Top Recommendations

1. **Clarify requirement testability** in msl-l0-foundation.md (High Impact)
2. **Add validation requirements** to msl-l1-structure.md (Medium Impact)
3. **Enhance error handling specs** in msl-tools-spec.md (Low Impact)

## No Critical Issues Found ✅

All specifications meet minimum quality standards.
```

### Configuration File

```yaml
# .msl-validate.yml
validation:
  exclude:
    - "**/archive/**"
    - "**/drafts/**"
  
  thresholds:
    minimum_score: 70
    warning_score: 80
    excellent_score: 90
  
  checks:
    dry_compliance: true
    inheritance_validation: true
    requirement_quality: true
    architecture_analysis: true
```

## Notes

This batch validation tool extends the individual MSL validation agent to provide project-wide quality assurance. It enables teams to maintain consistent MSL quality across large specification sets and integrates well with CI/CD pipelines for automated quality checks.

The tool demonstrates MSL's capability to specify practical development tools that enhance the MSL ecosystem.

---
*Specification format: [MSL Level 2](https://github.com/chrs-myrs/msl-specification)*