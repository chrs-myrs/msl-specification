# Changelog

All notable changes to the MSL Specification will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **Testing Framework**: Comprehensive pytest-based testing infrastructure
  - Pytest configuration with markers for test organization
  - Shared fixtures via conftest.py for common test setup
  - Test runner script for simplified execution
  - Requirements-dev.txt for development dependencies
  - MSL specifications for all new scripts

### Changed
- Migrated all test files from standalone execution to pytest
- Updated pre-commit configuration for MSL linting

## [1.5.0] - 2025-09-05 (Preview)

### Added
- **Bidirectional Code Links**: Enhanced traceability between specs and implementation
  - Forward links (→): Spec points to code implementation
  - Backward links (←): Code references spec requirement
  - Bidirectional links (↔): Both spec and code reference each other
  - Line number ranges support for precise code location
  - Integration with composite markers for rich metadata
  - Code scanner for automatic reverse link generation

## [1.4.0] - 2025-09-05

### Added
- **Composite Markers**: Rich metadata in requirement markers
  - Multiple attributes in single marker using pipe separation
  - Support for metrics (progress:75%, coverage:85%)
  - Dependency relationships (depends:REQ-001, blocks:REQ-002)
  - Project management fields (sprint:15, milestone:v1.0)
  - Backward compatible with simple markers

- **Hierarchical Requirements**: Nested requirement structures
  - Parent-child relationships with indentation
  - Automatic ID generation for sub-requirements (REQ-001.1, REQ-001.1.1)
  - Depth validation and consistency checking
  - Preserves markers and metadata through hierarchy

- **Validation Configuration**: Customizable validation rules
  - .mslrc configuration files for project-specific rules
  - Custom validators for domain-specific requirements
  - ID format patterns and naming conventions
  - Required/forbidden marker enforcement
  - Min/max requirement counts

## [1.2.1] - 2025-09-05

### Added
- **Metaspec Governance Proposal**: New proposal for `governed-by` frontmatter field that enables specifications to explicitly declare which metaspec governs their structure and quality standards. See [docs/proposals/metaspec-governance.md](docs/proposals/metaspec-governance.md) for details.
  - Introduces CONFORMS-TO relationship distinct from IS-A (extends) and DEFINES (templates)
  - Enables automated validation against metaspec requirements
  - Supports multiple governance patterns through composition
  - Provides foundation for architectural enforcement

- **Context7 Optimization**: Added support for AI discovery and understanding of MSL through context7 and similar AI documentation systems
  - `/llms.txt` file at repository root acts as entry point for AI systems (like robots.txt for LLMs)
  - `/docs/implementation-reference.md` consolidates complete implementation details in one self-contained document
  - Guides AI systems to core specifications in proper learning order (L0→L1→L2)
  - Addresses fragmentation issues when AI systems access MSL through documentation tools

### Documentation
- Added comprehensive metaspec governance proposal with examples, validation capabilities, and migration path
- Created llms.txt for AI/LLM discovery with links to core specs and implementation guide
- Added complete implementation reference (30KB) with BNF grammar, Python parser/validator, and runnable examples
- Created MSL specifications for context7 optimization files in `/specs/context7-optimization/`

## [1.2.0] - 2025-09-04

### Changed
- **AI-First Positioning**: Complete reframing of MSL documentation for AI-powered development
  - Repositioned as critical infrastructure for "post-vibe-coding" era
  - Emphasized role as bridge between human intent and AI implementation
  - Updated all documentation with AI workflow examples

### Added
- **Comprehensive Documentation Suite**:
  - User Guide: Complete task-oriented guide for all MSL features
  - Reference: Formal language specification with EBNF grammar
  - Tools Guide: CLI tools, editor support, and automation
  - Workflow Guides: Solo, team, and AI collaboration patterns
  - Tutorials: Six step-by-step tutorials for beginners to advanced users
  - Project Documentation: Contributing guidelines, roadmap, and this changelog

### Documentation
- 15+ new documentation files (~40,000 words)
- AI-first examples and workflows throughout
- Clear progression from simple markdown to advanced features

## [1.1.0] - Previous Release

### Added
- MSL Level 2 advanced features (markers, templates, inheritance)
- Formal grammar specification in BNF
- Validation standards and quality metrics
- Extension mechanism for domain-specific features

### Changed
- Improved inheritance protocol with explicit markers
- Enhanced template system with variable substitution
- Better separation between language levels (L0, L1, L2)

## [1.0.0] - Initial Release

### Added
- MSL Level 0: Pure markdown specification format
- MSL Level 1: Structured specifications with frontmatter
- Basic inheritance with `extends`
- Requirement ID system (REQ-XXX)
- Initial documentation and examples

---

For detailed information about each release, see the [GitHub Releases](https://github.com/chrs-myrs/msl-specification/releases) page.