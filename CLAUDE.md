# MSL Specification Project - Claude Code Instructions

## Project Overview
This repository contains the MSL (Markdown Specification Language) specification and its ecosystem. MSL is a progressive enhancement of markdown for writing formal specifications with requirements traceability, inheritance, and validation capabilities.

## ⚠️ CRITICAL: Inheritance Rules

**NEVER use `extends` unless there's a true "is-a" relationship!**

Before using `extends: parent-spec`, ask:
1. Is this spec truly a specialized type of the parent?
2. Can I naturally say "X IS A Y"?
3. Would ALL parent requirements apply to this child?

**Common Mistakes to Avoid:**
- ❌ DON'T: `extends: msl-l2-advanced` (unless creating a new MSL level)
- ❌ DON'T: `extends: msl-docs-root` (doc specs are peers, not subtypes)
- ❌ DON'T: Use extends for organizational hierarchy

**Correct Patterns:**
- ✅ DO: Use `msl: L1` or `msl: L2` to declare which MSL features you use
- ✅ DO: Use `references:` for non-inheritance relationships
- ✅ DO: Leave out `extends` entirely (most specs don't need it)

**Valid Inheritance Examples:**
```yaml
# Valid: auth-api IS A rest-api
extends: rest-api

# Invalid: docs are not a type of language spec
extends: msl-l2-advanced  # WRONG!
```

## Project Structure
```
msl-specification/
├── specs/                      # MSL specifications
│   ├── msl-l0-foundation.md   # Level 0: Basic markdown + requirements
│   ├── msl-l1-structure.md    # Level 1: + Frontmatter & inheritance
│   ├── msl-l2-advanced.md     # Level 2: + Advanced features
│   ├── standards/              # Quality and extension standards
│   └── applications/           # Tool and agent specifications
├── .claude/agents/             # Claude Code agent definitions
│   ├── msl-validator.md        # Individual spec validator
│   └── msl-batch-validator.md  # Batch validation agent
└── scripts/                    # Utility scripts
```

## MSL Levels
- **L0**: Basic markdown with `## Requirements` section
- **L1**: L0 + YAML frontmatter, inheritance via `extends`
- **L2**: L1 + markers, templates, formal semantics

## Key Concepts
1. **Self-Specification**: MSL specifications are themselves valid MSL documents
2. **Progressive Enhancement**: Each level builds on the previous
3. **Validation**: Comprehensive quality metrics and architectural analysis
4. **Inheritance**: Specifications can extend others with proper "is-a" relationships

## Available Agents

### msl-validator
Validates individual MSL specifications for:
- Architectural quality and DRY compliance
- Requirement testability (≥90% target)
- Inheritance correctness (≤4 levels)
- Quality score (0-100, ≥80 for production)

Usage: "Please validate this MSL specification"

### msl-batch-validator  
Validates entire specification sets:
- Finds all MSL files recursively
- Builds inheritance graphs
- Generates aggregate reports
- Identifies cross-specification issues

Usage: "Run the batch validator on the specs folder"

## Quality Standards
All MSL specifications should:
- Score ≥80/100 on validation
- Have ≥90% testable requirements
- Maintain <20% duplication (DRY)
- Use ≤4 inheritance levels
- Include [MSL] marker in title

## Working with MSL

### Creating Specifications
1. Start with L0 for simple specs
2. Add frontmatter for L1 features
3. Use L2 only when advanced features needed
4. Always include `## Requirements` section
5. Make requirements testable with measurable criteria

### Validating Specifications
```bash
# Validate single spec
"Please validate specs/my-spec.md"

# Batch validate
"Run the MSL batch validator on specs/"
```

### Common Tasks
- **Add new spec**: Create .md file with Requirements section
- **Extend existing**: Use `extends:` in frontmatter
- **Check quality**: Run validation agent
- **Review architecture**: Use batch validator

## Important Notes
1. **MSL is self-referential**: The language specifies itself
2. **Validation is recursive**: Validators are specified in MSL
3. **Quality matters**: All core specs score 88-95/100
4. **Keep it simple**: Use lowest MSL level that meets needs

## Development Workflow
1. Write/modify specification
2. Run validator to check quality
3. Address any issues found
4. Run batch validator to check integration
5. Commit when quality score ≥80

## References
- MSL Repository: https://github.com/chrs-myrs/msl-specification
- Core Specs: `/specs/msl-l0-foundation.md`, `msl-l1-structure.md`, `msl-l2-advanced.md`
- Standards: `/specs/standards/msl-usage-standards.md`
- Tools: `/specs/applications/msl-tools-spec.md`