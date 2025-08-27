# Contributing to MSL

Thank you for your interest in contributing to the Markdown Specification Language! We welcome contributions from everyone.

## Ways to Contribute

### 1. Use MSL and Provide Feedback
- Try MSL in your projects
- Report what works well and what doesn't
- Share your use cases and workflows

### 2. Improve Documentation
- Fix typos and clarify confusing sections
- Add examples and use cases
- Translate documentation to other languages
- Write guides and tutorials

### 3. Contribute Code
- Fix bugs in tools
- Add new features to CLI tools
- Improve parser and validator
- Create editor plugins

### 4. Enhance the Specification
- Propose new features via issues
- Discuss improvements in GitHub Discussions
- Submit spec changes via pull requests

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/chrs-myrs/msl-specification.git
   cd msl-specification
   ```
3. **Create a branch** for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Make your changes** and test them
5. **Commit your changes** with clear messages:
   ```bash
   git commit -m "Add support for X in msl-lint"
   ```
6. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Open a Pull Request** on GitHub

## Development Setup

### Python Tools
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest tools/tests/

# Run linter on examples
./tools/cli/msl-lint examples/
```

### Testing Your Changes
- Add tests for new features
- Ensure all tests pass before submitting PR
- Test with various MSL levels (0, 1, 2)
- Validate examples still work

## Pull Request Guidelines

### Before Submitting
- [ ] Tests pass locally
- [ ] Code follows existing style
- [ ] Documentation updated if needed
- [ ] Examples added for new features
- [ ] Changelog entry added (for significant changes)

### PR Title Format
- `feat: Add new feature X`
- `fix: Resolve issue with Y`
- `docs: Update documentation for Z`
- `test: Add tests for feature A`
- `refactor: Improve B implementation`

### PR Description
Include:
- What problem does this solve?
- How does it solve it?
- Any breaking changes?
- Related issues/discussions

## Specification Changes

Changes to the MSL specification itself require extra care:

1. **Open an issue first** to discuss the proposed change
2. **Consider backward compatibility** - avoid breaking existing specs
3. **Update version number** if adding new features
4. **Provide migration path** for breaking changes
5. **Update all relevant documentation**
6. **Add examples** demonstrating new features

### Spec Versioning
- **Patch (1.1.x)**: Clarifications, typo fixes
- **Minor (1.x.0)**: New features, backward compatible
- **Major (x.0.0)**: Breaking changes (avoid if possible)

## Code Style

### Python
- Follow PEP 8
- Use type hints where appropriate
- Add docstrings to functions and classes
- Keep functions focused and small

### Markdown
- Use consistent heading levels
- Include code examples with syntax highlighting
- Keep line length reasonable (80-100 chars)
- Use reference links for repeated URLs

## Community Guidelines

### Be Respectful
- Welcome newcomers and help them get started
- Respect different perspectives and experiences
- Give and accept constructive feedback gracefully
- Focus on what's best for the community

### Communication Channels
- **GitHub Issues**: Bug reports, feature requests
- **GitHub Discussions**: Questions, ideas, general discussion
- **Pull Requests**: Code contributions, documentation improvements

### Response Times
- Issues: Acknowledged within 7 days
- Pull Requests: Initial review within 14 days
- Not all contributions will be accepted, but all will be considered

## Recognition

Contributors are recognized in:
- Git commit history
- GitHub contributors page
- Release notes for significant contributions
- CONTRIBUTORS.md file (for regular contributors)

## Questions?

If you have questions about contributing:
1. Check existing issues and discussions
2. Read the documentation
3. Open a new discussion if still unclear

## License

By contributing to MSL, you agree that your contributions will be licensed under the MIT License.

Thank you for helping make MSL better!