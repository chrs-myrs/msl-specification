# Contributing to MSL

Thank you for your interest in contributing to MSL! This project thrives on community participation, whether you're fixing bugs, adding features, improving documentation, or sharing ideas.

## Code of Conduct

By participating in this project, you agree to uphold our commitment to respectful, inclusive collaboration. We welcome contributors from all backgrounds and experience levels.

### Our Standards
- Use welcoming and inclusive language
- Respect differing viewpoints and experiences
- Accept constructive criticism gracefully
- Focus on what's best for the community
- Show empathy toward other community members

### Unacceptable Behavior
- Harassment, discrimination, or derogatory comments
- Public or private harassment
- Publishing others' private information
- Other conduct deemed unprofessional

## Contribution Process

Follow these 7 steps to contribute:

### 1. Find or Create an Issue
- Check [existing issues](https://github.com/chrs-myrs/msl-specification/issues)
- For new ideas, create an issue first for discussion
- Look for `good-first-issue` labels if you're new

### 2. Fork and Clone
```bash
# Fork via GitHub UI, then:
git clone https://github.com/YOUR-USERNAME/msl-specification.git
cd msl-specification
git remote add upstream https://github.com/chrs-myrs/msl-specification.git
```

### 3. Create Feature Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/issue-number
```

### 4. Make Your Changes
- Write MSL specifications for new features
- Validate specifications: `msl-validate specs/`
- Update documentation if needed
- Add tests for new functionality

### 5. Commit with Conventional Format
```bash
git commit -m "type: description

- Detailed explanation
- References #issue-number"
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

### 6. Push and Create PR
```bash
git push origin feature/your-feature-name
```

Then create PR via GitHub with:
- Clear title following commit format
- Description of changes
- Link to related issue
- Screenshots if applicable

### 7. Address Review Feedback
- Respond to reviewer comments
- Make requested changes
- Push updates to same branch
- PR will be merged once approved

## Development Environment Setup

### Prerequisites
```bash
# Node.js 14+ required
node --version

# Install dependencies
npm install

# Install MSL tools globally
npm install -g msl-tools
```

### Project Structure
```
msl-specification/
├── specs/           # MSL specifications
│   ├── core/       # Core language specs
│   ├── applications/ # Tool specifications
│   └── documentation/ # Doc specifications
├── docs/           # User documentation
├── examples/       # Example specifications
├── .claude/        # Claude Code agents
└── tools/          # Utility scripts
```

### Running Tests
```bash
# Validate all specifications
npm run validate

# Check specification quality
npm run quality-check

# Run specific validation
msl-validate specs/core/msl-l2-advanced.md
```

### Local Documentation
```bash
# Generate documentation
npm run docs:build

# Serve documentation locally
npm run docs:serve
# Visit http://localhost:3000
```

## Review and Merge Criteria

### What We Look For
✅ **Specification Quality**
- Validates successfully (score ≥85/100)
- Follows MSL best practices
- Includes examples
- Documents edge cases

✅ **Code Quality** (if applicable)
- Passes all tests
- Follows style guidelines
- Includes appropriate comments
- No security vulnerabilities

✅ **Documentation**
- Updates relevant docs
- Clear commit messages
- PR description complete
- Changelog entry added

### Merge Requirements
- ✅ All CI checks pass
- ✅ At least one maintainer approval
- ✅ No unresolved conversations
- ✅ Specification validation ≥85/100
- ✅ Documentation updated

## Good First Issues

Perfect for newcomers to MSL:

### Documentation
1. **Improve Getting Started Tutorial** [#42](https://github.com/chrs-myrs/msl-specification/issues)
   - Add more examples
   - Clarify common confusion points
   - Effort: Small

2. **Add API Specification Examples** [#56](https://github.com/chrs-myrs/msl-specification/issues)
   - Create REST API examples
   - Show GraphQL patterns
   - Effort: Medium

3. **Translate README to Other Languages** [#71](https://github.com/chrs-myrs/msl-specification/issues)
   - Spanish, French, German, etc.
   - Maintain in docs/i18n/
   - Effort: Medium

### Specifications
4. **Create Database Schema Template** [#83](https://github.com/chrs-myrs/msl-specification/issues)
   - MSL template for databases
   - Include common patterns
   - Effort: Medium

5. **Add Microservice Specification Set** [#94](https://github.com/chrs-myrs/msl-specification/issues)
   - Complete example architecture
   - Show inheritance patterns
   - Effort: Large

### Tools
6. **Add JSON Export Format** [#105](https://github.com/chrs-myrs/msl-specification/issues)
   - Export MSL to JSON
   - Preserve all metadata
   - Effort: Medium

7. **Improve Validation Error Messages** [#112](https://github.com/chrs-myrs/msl-specification/issues)
   - More helpful error text
   - Include fix suggestions
   - Effort: Small

## Issue Templates

### Bug Report
```markdown
**Description:**
Clear description of the bug

**Steps to Reproduce:**
1. Step one
2. Step two
3. ...

**Expected Behavior:**
What should happen

**Actual Behavior:**
What actually happens

**Environment:**
- MSL version:
- Node version:
- OS:
```

### Feature Request
```markdown
**Problem:**
What problem does this solve?

**Proposed Solution:**
How should it work?

**Alternatives Considered:**
Other approaches tried

**Use Case:**
Real-world example
```

## Pull Request Template

```markdown
## Description
Brief description of changes

## Related Issue
Fixes #(issue number)

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation
- [ ] Refactoring

## Checklist
- [ ] Specifications validate successfully
- [ ] Documentation updated
- [ ] Tests pass
- [ ] Changelog entry added

## Screenshots (if applicable)
```

## Commit Message Format

Follow Conventional Commits:

```
type(scope): subject

body

footer
```

### Examples
```bash
feat(validation): add AI readiness check

- Checks natural language clarity
- Validates measurable criteria
- Ensures no implementation details

Closes #145

---

fix(inheritance): correct override behavior

Override markers now properly replace parent requirements
instead of duplicating them.

BREAKING CHANGE: REQ-ID must match parent for overrides

---

docs(tutorials): improve inheritance examples

- Add more IS-A test examples
- Clarify common mistakes
- Include debugging tips
```

## Branching Strategy

- `main` - Stable releases
- `develop` - Integration branch
- `feature/*` - New features
- `fix/*` - Bug fixes
- `docs/*` - Documentation only
- `release/*` - Release preparation

## Communication Channels

### Primary Channels
1. **GitHub Issues** - Bug reports, features
2. **GitHub Discussions** - Questions, ideas
3. **Discord** - Real-time chat [Join](https://discord.gg/msl)

### Additional Resources
- **Email**: msl@example.com (maintainers)
- **Twitter**: [@MSLSpec](https://twitter.com/mslspec)
- **Stack Overflow**: Tag `msl-specification`

## Recognition

Contributors are recognized in:
- [CONTRIBUTORS.md](CONTRIBUTORS.md) - All contributors
- Release notes - Per-release contributions
- README credits - Significant contributions

## Questions?

- Check the [FAQ](docs/faq.md)
- Ask in [GitHub Discussions](https://github.com/chrs-myrs/msl-specification/discussions)
- Join our [Discord](https://discord.gg/msl)

---

**Thank you for contributing to MSL! Together we're building the foundation for AI-powered software development.**