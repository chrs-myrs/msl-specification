# MSL - Markdown Specification Language

> Lightweight specifications that grow with your needs

[![Version](https://img.shields.io/badge/spec-v1.1-blue.svg)](docs/spec/v1.1/specification.md)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://python.org)

## Zero to Specification in 30 Seconds

MSL works with plain markdown. Start simple:

```markdown
# Login System

## Requirements
- Users can log in with email/password
- Sessions expire after 30 minutes
- Failed logins lock after 5 attempts
```

That's valid MSL. Add structure as needed:

```markdown
---
id: login-system
---

# Login System

## Requirements
- REQ-001: Users can log in with email/password
- REQ-002: Sessions expire after 30 minutes
- REQ-003: Failed logins lock after 5 attempts
```

## Why MSL?

- **Progressive Enhancement**: Start with plain markdown, add structure only when needed
- **Tool-Optional**: Human-readable without any tools
- **Git-Friendly**: Plain text diffs, simple merges
- **AI-Ready**: LLMs understand and generate MSL naturally
- **Inheritance**: Build complex specs from simple templates

## Quick Start

### Install Tools (Optional)

```bash
# Install MSL CLI tools
pip install msl-tools

# Or use without installation
python tools/cli/msl-lint my-spec.md
```

### Write Your First Spec

Create `my-feature.md`:

```markdown
# My Feature

## Requirements
- [!] Critical thing that must work
- Normal priority requirement
- [?] Something we're unsure about
```

### Validate

```bash
msl lint my-feature.md
```

## Three Levels of MSL

### Level 0: Pure Markdown
Any markdown with `## Requirements`. No tools needed.

### Level 1: Basic Structure
Add IDs and references. Still readable as plain markdown.

### Level 2: Full Metadata
Enterprise features: inheritance, variables, workflow states.

See [Quick Start Guide](docs/guides/quick-start.md) for details.

## Documentation

- [Specification v1.1](docs/spec/v1.1/specification.md) - Full specification
- [Quick Start Guide](docs/guides/quick-start.md) - Get started in minutes
- [Solo Workflow](docs/guides/solo-workflow.md) - Individual developer guide
- [Team Workflow](docs/guides/team-workflow.md) - Collaboration patterns
- [Examples](examples/) - Real-world usage

## Tools

### Available Now

- `msl-lint` - Validate MSL files
- `msl-render` - Process templates and variables
- `msl-resolve` - Resolve inheritance chains

### Roadmap

- **Q1 2025**: VS Code and Obsidian plugins
- **Q2 2025**: Web-based editor
- **Q3 2025**: Collaboration features

See [Roadmap](docs/spec/roadmap.md) for details.

## Examples

Browse the [examples/](examples/) directory:

```
examples/
├── minimal/        # Simple specs without frontmatter
├── basic/          # Specs with IDs and structure
├── advanced/       # Full metadata and inheritance
└── real-world/     # Production use cases
```

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

- Report bugs via [GitHub Issues](https://github.com/chrs-myrs/msl-specification/issues)
- Submit improvements via Pull Requests
- Join discussions in [Discussions](https://github.com/chrs-myrs/msl-specification/discussions)

## Philosophy

MSL follows these principles:

1. **Start Simple**: No upfront complexity tax
2. **Grow Naturally**: Add structure when you need it
3. **Stay Readable**: Always valid markdown
4. **Tool Optional**: Never require special software

## License

MIT - See [LICENSE](LICENSE) for details.

## Credits

Created for developers who want specifications that work with them, not against them.