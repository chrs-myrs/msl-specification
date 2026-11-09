# MSL Specification Index [MSL]

## Summary

This index helps AI agents and developers navigate the MSL specification ecosystem. Start here to understand MSL's structure and find relevant specifications.

## For AI Agents - Efficient Configuration

### One-Time Setup (Cache for Session)
1. **Fetch and cache**: [`docs/agent-guide.md`](../docs/agent-guide.md) - Essential MSL knowledge (90% of what you need)
2. **Check for**: Project-specific `MSL-CONFIG.md` (if it exists)
3. **Result**: Minimal context use, fewer context7 lookups, consistent MSL usage

### First-Time Project Setup
1. **Read First**: [PURPOSE.md](../PURPOSE.md) - Understand what MSL is and isn't
2. **Read Second**: [interfaces/standards/msl-project-organization.spec.md](interfaces/standards/msl-project-organization.spec.md) - Learn how to structure projects
3. **Create**: PURPOSE.md for your specific project
4. **Follow**: Organization standards for all subsequent specifications

### Quick Decision Guide
- **Simple project?** → Use Level 0 (just markdown with requirements)
- **Need structure?** → Use Level 1 (add frontmatter and IDs)
- **Complex needs?** → Use Level 2 (markers, inheritance, templates)

### A Note on Simplicity

MSL works best when specifications start simple. Consider:
- Most projects only need L0 (plain markdown with requirements)
- High-level requirements often work better than detailed prescriptions
- You can always add detail later if needed

## Core Language Specifications

### Foundation Levels
- [interfaces/msl-l0-foundation.spec.md](interfaces/msl-l0-foundation.spec.md) - **Start here for basics**
  - Plain markdown with `## Requirements` section
  - No special syntax needed
  - Perfect for simple specifications
  
- [interfaces/msl-l1-structure.spec.md](interfaces/msl-l1-structure.spec.md) - **Add structure when needed**
  - Adds YAML frontmatter for metadata
  - Requirement IDs (REQ-001, REQ-002, etc.)
  - Document identification and versioning
  
- [interfaces/msl-l2-advanced.spec.md](interfaces/msl-l2-advanced.spec.md) - **Advanced features (all optional)**
  - Markers: [!], [@user], [#tag], [x]
  - Inheritance with `extends:`
  - Templates and variables
  - Composite markers for rich metadata

### Purpose and Philosophy
- [PURPOSE.md](../PURPOSE.md) - Core purpose and limitations (at repository root)

## Governance Specifications (Metaspecs)

Metaspecs are specifications that govern other specifications. They prove MSL can specify anything, including itself.

- [workspace/metaspecs/msl-core-metaspec.md](workspace/metaspecs/msl-core-metaspec.md) - Governs all MSL specifications
- [workspace/metaspecs/msl-language-metaspec.md](workspace/metaspecs/msl-language-metaspec.md) - Governs language specs
- [workspace/metaspecs/msl-validation-metaspec.md](workspace/metaspecs/msl-validation-metaspec.md) - Validation rules
- [workspace/metaspecs/msl-documentation-metaspec.md](workspace/metaspecs/msl-documentation-metaspec.md) - Documentation governance
- [workspace/metaspecs/testing-framework-metaspec.md](workspace/metaspecs/testing-framework-metaspec.md) - Testing standards

## Standards and Best Practices

- [interfaces/standards/msl-project-organization.spec.md](interfaces/standards/msl-project-organization.spec.md) - **How to structure projects**
- [interfaces/standards/msl-usage-standards.spec.md](interfaces/standards/msl-usage-standards.spec.md) - Usage patterns and conventions
- [interfaces/standards/msl-extension-standards.spec.md](interfaces/standards/msl-extension-standards.spec.md) - How to extend MSL

## Documentation Specifications

These prove MSL can specify its own documentation (simplified with inheritance):

- [features/documentation/msl-docs-base.spec.md](features/documentation/msl-docs-base.spec.md) - Common documentation requirements
- [features/documentation/msl-docs-getting-started.spec.md](features/documentation/msl-docs-getting-started.spec.md) - Quick start spec (extends base)
- [features/documentation/msl-docs-user-guide.spec.md](features/documentation/msl-docs-user-guide.spec.md) - User guide spec (extends base)
- [features/documentation/msl-docs-reference.spec.md](features/documentation/msl-docs-reference.spec.md) - Reference spec (extends base)
- [features/documentation/msl-docs-tutorials.spec.md](features/documentation/msl-docs-tutorials.spec.md) - Tutorial spec (extends base)

## Application Specifications

Specifications for MSL tools (implementations may be in separate repositories):

- [artifacts/msl-validation-agent.spec.md](artifacts/msl-validation-agent.spec.md) - Validation tool spec
- [artifacts/msl-batch-validator.spec.md](artifacts/msl-batch-validator.spec.md) - Batch validation spec
- [features/msl-tools.spec.md](features/msl-tools.spec.md) - General tools spec
- [artifacts/pre-push-completeness-checker.spec.md](artifacts/pre-push-completeness-checker.spec.md) - Pre-push completeness agent spec

## Testing Framework

- [features/testing/msl-testing-framework.spec.md](features/testing/msl-testing-framework.spec.md) - Testing infrastructure spec

## Context7 Optimization

For AI agents using context7:

- [features/context7-optimization/msl-llms-txt.spec.md](features/context7-optimization/msl-llms-txt.spec.md) - LLM optimization
- [features/context7-optimization/msl-implementation-reference.spec.md](features/context7-optimization/msl-implementation-reference.spec.md) - Implementation guide

## Navigation Tips for AI Agents

### When creating a new project:
1. Always start with PURPOSE.md
2. Create /specs directory structure
3. Use appropriate MSL level based on complexity
4. Reference this index for patterns

### When extending existing projects:
1. Read PURPOSE.md first
2. Check for project-specific metaspecs
3. Follow existing patterns in the project
4. Maintain consistency with project standards

### When validating specifications:
1. Use msl-lint for syntax checking
2. Verify against relevant metaspecs
3. Ensure cross-references are valid
4. Check requirement testability

## Key Concepts

- **Dogfooding**: MSL specifies itself, proving its completeness
- **Progressive Enhancement**: Start simple, add complexity only when needed
- **Metaspecs**: Specifications that govern other specifications
- **Levels**: L0 (simple) → L1 (structured) → L2 (advanced)

## Notes

This index itself is an MSL specification, demonstrating that MSL can organize and describe its own structure. The self-referential nature isn't just clever—it's proof that MSL is complete enough to handle any specification need.

For human readers: Browse the examples/ directory for practical demonstrations.
For AI agents: Parse this index to understand the complete MSL ecosystem.