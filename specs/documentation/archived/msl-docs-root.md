---
msl: L1
id: msl-docs-root
tags: [documentation, meta, root]
priority: critical
status: active
references:
  - msl-l2-advanced: "Language specification being documented"
  - msl-usage-standards: "Quality standards for documentation"
---

# MSL Documentation System Specification [MSL]

## Summary

This specification defines the documentation system for MSL, establishing requirements for comprehensive, accessible, and maintainable documentation that serves both human readers and AI agents effectively while minimizing context overhead for MCP servers.

## Requirements

### Documentation System Architecture

- REQ-001: [!] [NEW] Documentation must be organized as a hierarchy of MSL specifications
- REQ-002: [!] [NEW] Each documentation specification must define requirements, not content
- REQ-003: [!] [NEW] Documentation must be generateable from specifications
- REQ-004: [!] [NEW] Documentation must be validatable against specifications
- REQ-005: [NEW] Each specification must map to exactly one documentation file

### Context Optimization

- REQ-101: [!] [NEW] Each documentation spec must be ≤500 lines for MCP efficiency
- REQ-102: [!] [NEW] Specs must support progressive disclosure (summary → details)
- REQ-103: [NEW] Cross-references must use relative paths and REQ-IDs
- REQ-104: [NEW] Documentation must be chunked for incremental loading
- REQ-105: [NEW] Each spec must declare its context dependencies explicitly

### Human Accessibility

- REQ-201: [!] [NEW] Documentation must follow progressive learning paths
- REQ-202: [NEW] Each document must have clear learning objectives
- REQ-203: [NEW] Examples must be practical and incrementally complex
- REQ-204: [NEW] Documentation must use consistent terminology
- REQ-205: [NEW] Navigation must support multiple entry points

### AI/Agent Accessibility

- REQ-301: [!] [NEW] Documentation must include structured metadata
- REQ-302: [NEW] Each document must declare its purpose and scope
- REQ-303: [NEW] Prerequisites must be explicitly listed
- REQ-304: [NEW] Documents must support semantic search
- REQ-305: [NEW] API documentation must include machine-readable schemas

### Documentation Categories

- REQ-401: [!] [NEW] System must include getting-started documentation
- REQ-402: [!] [NEW] System must include comprehensive user guide
- REQ-403: [!] [NEW] System must include technical reference
- REQ-404: [NEW] System must include step-by-step tutorials
- REQ-405: [NEW] System must include API/tool documentation
- REQ-406: [NEW] System must include examples and patterns

### Inheritance Guidance

- REQ-451: [!] [NEW] Documentation must explain inheritance "is-a" requirement
- REQ-452: [!] [NEW] Documentation must provide valid/invalid inheritance examples
- REQ-453: [NEW] Documentation must warn against common inheritance mistakes
- REQ-454: [NEW] Documentation must explain difference between `msl:` level and `extends:`
- REQ-455: [NEW] Documentation must recommend using `references:` for non-inheritance

### Quality Requirements

- REQ-501: [!] [NEW] Documentation must achieve ≥90% coverage of public features
- REQ-502: [NEW] Examples must be executable and testable
- REQ-503: [NEW] Documentation must be version-synchronized with specs
- REQ-504: [NEW] Cross-references must be validated for accuracy
- REQ-505: [NEW] Documentation must pass readability metrics (grade ≤12)

### Generation Requirements

- REQ-601: [!] [NEW] Documentation must be generatable from specs + templates
- REQ-602: [NEW] Generation must support multiple output formats (MD, HTML, PDF)
- REQ-603: [NEW] Generated docs must include source spec references
- REQ-604: [NEW] Generation must support incremental updates
- REQ-605: [NEW] Generated docs must preserve custom sections

## Documentation Hierarchy

### Level 1: Documentation Categories
- `msl-docs-getting-started.md` - Quick start and setup
- `msl-docs-user-guide.md` - Comprehensive usage guide
- `msl-docs-reference.md` - Technical reference
- `msl-docs-tutorials.md` - Step-by-step tutorials
- `msl-docs-api.md` - Tool and API documentation

### Level 2: Specific Topics
User Guide topics:
- `msl-docs-writing.md` - Writing specifications
- `msl-docs-validation.md` - Validation and quality
- `msl-docs-inheritance.md` - Inheritance and templates

Reference topics:
- `msl-docs-syntax.md` - Syntax reference
- `msl-docs-markers.md` - Markers reference
- `msl-docs-frontmatter.md` - Frontmatter reference

## Validation Criteria

Documentation is valid when:
- All required sections are present
- Examples are executable
- Cross-references resolve correctly
- Readability metrics pass
- Coverage metrics meet thresholds

## Notes

This meta-specification demonstrates MSL's self-referential capability by using MSL to specify its own documentation system. Each child specification defines requirements for specific documentation, enabling systematic documentation generation and validation.

---
*Specification format: [MSL Level 2](https://github.com/chrs-myrs/msl-specification)*