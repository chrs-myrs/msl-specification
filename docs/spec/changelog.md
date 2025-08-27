# MSL Specification Changelog

## [1.1.0] - 2024-12-21

### Added
- Progressive enhancement levels (0, 1, 2) for gradual adoption
- Solo practitioner workflow optimizations
- Quick markers (`[!]`, `[?]`, `[x]`, etc.) as alternatives to frontmatter
- Automatic conventions and smart defaults
- File-based organization patterns
- Simplified inheritance syntax with `Modified:` and `New:` keywords
- Comment-based extends syntax (`<!-- extends: base-spec -->`)
- Support for Jinja2 template variables

### Changed
- Frontmatter now completely optional (Level 0 support)
- Filename becomes implicit ID when frontmatter absent
- Relaxed requirement for `## Requirements` section in Level 0
- Default values for all metadata fields

### Improved
- Documentation focuses on zero-to-spec in 30 seconds
- Examples start with minimal cases
- Clear migration paths from other formats
- LLM integration examples added

## [1.0.0] - 2024-10-01

### Initial Release
- Core specification structure
- Frontmatter metadata
- Requirement sections
- Basic inheritance with `extends`
- REQ-XXX ID format
- Override markers (`[OVERRIDE]`, `[NEW]`, `[INHERIT]`)
- Tags and categorization
- Priority and status fields

## Planned Features

See [roadmap.md](roadmap.md) for upcoming features.