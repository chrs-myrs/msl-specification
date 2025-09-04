# Changelog

All notable changes to MSL (Markdown Specification Language) will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- AI-first positioning and documentation for human-AI collaboration workflows
- Comprehensive tutorials for AI implementation patterns
- Claude Code agent specifications for MSL validation
- MCP (Model Context Protocol) integration via context7
- Batch validation capabilities for large specification sets

### Changed
- Complete documentation rewrite focusing on AI-powered development
- README now emphasizes MSL as essential AI infrastructure
- Improved inheritance validation with clearer IS-A relationship rules

### Fixed
- Inheritance marker detection in validation tools
- DRY compliance scoring accuracy
- Cross-reference resolution in complex inheritance chains

## [1.2.0] - 2024-01-15

### Added
- MSL Level 2 Advanced Features (#125)
  - Template specifications with variable substitution
  - Conditional sections in templates
  - Multi-template composition support
- AI Readiness validation checks (#118)
  - Natural language clarity scoring
  - Token efficiency analysis
  - Context window optimization
- Claude Code agent support (#112)
  - MSL validation agent for quality analysis
  - Batch validator for specification suites
  - Automatic template extraction
- Comprehensive tutorials (#105)
  - Step-by-step first specification guide
  - AI implementation workflow tutorial
  - Team collaboration patterns

### Changed
- [BREAKING] Inheritance now requires explicit markers (#120)
  - `[OVERRIDE]` required for parent requirement replacement
  - `[NEW]` required for additional requirements
  - Migration: Add markers to existing child specifications
- Improved validation scoring algorithm (#115)
  - More accurate DRY compliance detection
  - Better testability assessment
  - Weighted scoring across dimensions
- Documentation structure reorganized (#108)
  - Clear separation of concepts, guides, and reference
  - AI-focused workflow documentation
  - Improved navigation and discovery

### Deprecated
- `inherits` keyword in favor of `extends` (#119)
  - Will be removed in version 2.0.0
  - Migration: Replace `inherits:` with `extends:`

### Removed
- Legacy XML export format (#114)
  - Use JSON export instead
  - Migration tool available at tools/xml-to-json.js

### Fixed
- Circular inheritance detection edge cases (#124)
- Variable substitution in nested templates (#121)
- Validation performance for large specifications (#117)
- Cross-reference validation across inheritance chains (#113)

### Security
- Input sanitization for template variables (#122)
- Path traversal prevention in file validation (#116)

## [1.1.0] - 2023-11-01

### Added
- MSL Level 1 Structured Features (#95)
  - Frontmatter metadata support
  - Requirement ID format (REQ-XXX)
  - Structural validation rules
- Basic inheritance with `extends` (#89)
  - Parent-child specification relationships
  - Requirement override capabilities
  - Maximum 3-level inheritance depth
- CLI tool suite (#82)
  - `msl-validate` for quality checking
  - `msl-lint` for style enforcement
  - `msl-render` for documentation generation
- GitHub Actions CI/CD templates (#78)

### Changed
- Validation now includes quality scoring (#91)
  - 0-100 quality score
  - Multiple dimension assessment
  - Configurable thresholds
- Improved error messages with fix suggestions (#86)
- Better handling of large specification sets (#83)

### Fixed
- Markdown parsing edge cases (#94)
- Windows path handling (#90)
- Memory leaks in validation tool (#87)
- Unicode handling in requirements (#84)

## [1.0.0] - 2023-09-15

### Added
- MSL Level 0 Foundation (#45)
  - Pure markdown compatibility
  - Required `## Requirements` section
  - No tooling dependencies
- Initial validation tool (#40)
  - Basic structure checking
  - Requirements section detection
  - Markdown format validation
- Documentation (#35)
  - Getting started guide
  - User guide basics
  - Initial examples
- Project structure (#30)
  - Core specifications
  - Documentation framework
  - Example specifications

### Changed
- Established semantic versioning (#42)
- Defined MSL level system (L0, L1, L2) (#38)
- Set quality standards and validation rules (#36)

### Fixed
- Initial bugs in validation logic (#44)
- Documentation typos and clarity (#41)
- Example specification errors (#37)

## [0.9.0] - 2023-07-01 [Beta]

### Added
- Initial MSL concept and syntax definition
- Basic validation prototype
- Proof of concept examples
- Community feedback incorporation

### Notes
- Beta release for early adopters
- API and syntax subject to change
- Not recommended for production use

---

## Migration Guides

### Migrating from 1.1.x to 1.2.0

#### Breaking Change: Inheritance Markers

Old format (1.1.x):
```markdown
extends: parent-spec
## Requirements
- REQ-001: Modified requirement  # No marker needed
- REQ-010: New requirement       # No marker needed
```

New format (1.2.0):
```markdown
extends: parent-spec
## Requirements
- REQ-001: [OVERRIDE] Modified requirement  # Marker required
- REQ-010: [NEW] New requirement           # Marker required
```

**Migration Script:**
```bash
# Automatic migration available
npx msl-migrate inheritance-markers ./specs/
```

#### Deprecation: inherits → extends

Old format:
```yaml
inherits: parent-spec
```

New format:
```yaml
extends: parent-spec
```

This will become an error in 2.0.0. Update now to avoid issues.

### Migrating from 1.0.x to 1.1.0

No breaking changes. New features are additive:
- Add frontmatter for metadata (optional)
- Add REQ-IDs for tracking (optional)
- Use inheritance for related specs (optional)

---

## Version Support Policy

| Version | Status | Support Until | Notes |
|---------|--------|---------------|-------|
| 1.2.x | **Current** | Active development | Recommended for new projects |
| 1.1.x | Maintained | 2024-07-01 | Security fixes only |
| 1.0.x | Deprecated | 2024-03-01 | Critical security fixes only |
| 0.9.x | End of Life | - | No support |

## Compatibility Matrix

| MSL Version | Tool Version | Node.js | Features |
|-------------|-------------|---------|----------|
| 1.2.0 | 1.2.x | 14+ | All features |
| 1.1.0 | 1.1.x | 12+ | No templates |
| 1.0.0 | 1.0.x | 10+ | Level 0 only |

---

[Unreleased]: https://github.com/chrs-myrs/msl-specification/compare/v1.2.0...HEAD
[1.2.0]: https://github.com/chrs-myrs/msl-specification/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/chrs-myrs/msl-specification/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/chrs-myrs/msl-specification/releases/tag/v1.0.0
[0.9.0]: https://github.com/chrs-myrs/msl-specification/releases/tag/v0.9.0