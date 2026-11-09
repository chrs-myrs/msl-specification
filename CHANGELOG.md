# Changelog

All notable changes to the MSL Specification will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **`derives-from:` Relationship Field**: New L2 frontmatter field for declaring generation/computation provenance (REQ-416, REQ-446, REQ-446a, REQ-446b)
  - Distinct from `implements:` — derives-from means "computed from source material", not "fulfils requirements"
  - Updated bidirectional pairs (REQ-445) to include derives-from ↔ derived-by
  - Added usage example in Traceability section
- **Testing Framework**: Comprehensive pytest-based testing infrastructure
  - Pytest configuration with markers for test organization
  - Shared fixtures via conftest.py for common test setup
  - Test runner script for simplified execution
  - Requirements-dev.txt for development dependencies
  - MSL specifications for all new scripts
- Spec for the pre-push completeness checker agent, `specs/artifacts/pre-push-completeness-checker.spec.md`

### Changed
- Migrated all test files from standalone execution to pytest
- Updated pre-commit configuration for MSL linting
- **MSL agent guide moved** from `/AGENTS.md` to [`docs/agent-guide.md`](docs/agent-guide.md); `specs/INDEX.md`, `examples/MSL-CONFIG.md` and `llms.txt` now point to it
- Adopted LiveSpec v5 (5.13.0) for repository governance: `project.yaml`, workspace specs in `specs/workspace/`, `registries/`, and vendored validators in `scripts/livespec/`
- `AGENTS.md` is now this repository's own agent context, generated from its specs; `CLAUDE.md` and `.livespec-version` removed
- **Spec paths moved; links to them break.** MSL's own specs are now `*.spec.md` files in LiveSpec category folders. Update any bookmark, link or context7 reference that uses an old path:

  | Old path | New path |
  |---|---|
  | `specs/msl-l0-foundation.md`, `msl-l1-structure.md`, `msl-l2-advanced.md` | `specs/interfaces/msl-l*.spec.md` (the old paths remain as pointers) |
  | `specs/standards/*.md` | `specs/interfaces/standards/*.spec.md` |
  | `specs/documentation/*.md` | `specs/features/documentation/*.spec.md` |
  | `specs/context7-optimization/msl-llms-txt-spec.md`, `msl-implementation-reference-spec.md` | `specs/features/context7-optimization/msl-llms-txt.spec.md`, `msl-implementation-reference.spec.md` |
  | `specs/testing/msl-testing-framework.md` | `specs/features/testing/msl-testing-framework.spec.md` |
  | `specs/applications/msl-tools-spec.md` | `specs/features/msl-tools.spec.md` |
  | `specs/applications/msl-validation-agent.md`, `msl-batch-validator.md` | `specs/artifacts/*.spec.md` |
  | `specs/metaspecs/*.md` | `specs/workspace/metaspecs/*.md` |
  | `scripts/*-msl-spec.md` | `scripts/*.spec.md` |

- The resolver in `tools/lib/` finds an `extends:` parent by its frontmatter `id` anywhere in the project (msl-tools REQ-507); previously it found only parents named `{id}.md` at the project root, `specs/` or `templates/`, so most nested parents failed to resolve

### Removed
- Stale RELEASE_CHECKLIST.md (superseded by pre-push completeness checker agent)
- Placeholder community channels (Discord, Twitter, example email, Stack Overflow) and dead links from README and `docs/contributing.md`

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