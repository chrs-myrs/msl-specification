# MSL Specification Index [MSL]

## Summary

This index helps AI agents and developers navigate the MSL specification ecosystem. Start here to understand MSL's structure and find relevant specifications.

## For AI Agents Starting New Projects

### Required Reading Order
1. **Read First**: [PURPOSE.md](../PURPOSE.md) - Understand what MSL is and isn't
2. **Read Second**: [standards/msl-project-organization.md](standards/msl-project-organization.md) - Learn how to structure projects
3. **Create**: PURPOSE.md for your specific project
4. **Follow**: Organization standards for all subsequent specifications

### Quick Decision Guide
- **Simple project?** → Use Level 0 (just markdown with requirements)
- **Need structure?** → Use Level 1 (add frontmatter and IDs)
- **Complex needs?** → Use Level 2 (markers, inheritance, templates)

## Core Language Specifications

### Foundation Levels
- [msl-l0-foundation.md](msl-l0-foundation.md) - **Start here for basics**
  - Plain markdown with `## Requirements` section
  - No special syntax needed
  - Perfect for simple specifications
  
- [msl-l1-structure.md](msl-l1-structure.md) - **Add structure when needed**
  - Adds YAML frontmatter for metadata
  - Requirement IDs (REQ-001, REQ-002, etc.)
  - Document identification and versioning
  
- [msl-l2-advanced.md](msl-l2-advanced.md) - **Advanced features (all optional)**
  - Markers: [!], [@user], [#tag], [x]
  - Inheritance with `extends:`
  - Templates and variables
  - Composite markers for rich metadata

### Purpose and Philosophy
- [PURPOSE.md](../PURPOSE.md) - Core purpose and limitations (at repository root)

## Governance Specifications (Metaspecs)

Metaspecs are specifications that govern other specifications. They prove MSL can specify anything, including itself.

- [metaspecs/msl-core-metaspec.md](metaspecs/msl-core-metaspec.md) - Governs all MSL specifications
- [metaspecs/msl-language-metaspec.md](metaspecs/msl-language-metaspec.md) - Governs language specs
- [metaspecs/msl-validation-metaspec.md](metaspecs/msl-validation-metaspec.md) - Validation rules
- [metaspecs/testing-framework-metaspec.md](metaspecs/testing-framework-metaspec.md) - Testing standards

## Standards and Best Practices

- [standards/msl-project-organization.md](standards/msl-project-organization.md) - **How to structure projects**
- [standards/msl-usage-standards.md](standards/msl-usage-standards.md) - Usage patterns and conventions
- [standards/msl-extension-standards.md](standards/msl-extension-standards.md) - How to extend MSL

## Documentation Specifications

These prove MSL can specify its own documentation:

- [documentation/msl-docs-root.md](documentation/msl-docs-root.md) - Documentation structure
- [documentation/msl-docs-user-guide.md](documentation/msl-docs-user-guide.md) - User guide spec
- [documentation/msl-docs-getting-started.md](documentation/msl-docs-getting-started.md) - Quick start spec
- [documentation/msl-docs-why-msl.md](documentation/msl-docs-why-msl.md) - Motivation spec
- [documentation/msl-docs-reference.md](documentation/msl-docs-reference.md) - Reference spec
- [documentation/msl-docs-tools.md](documentation/msl-docs-tools.md) - Tooling spec
- [documentation/msl-docs-workflows.md](documentation/msl-docs-workflows.md) - Workflow spec
- [documentation/msl-docs-tutorials.md](documentation/msl-docs-tutorials.md) - Tutorial spec
- [documentation/msl-docs-project.md](documentation/msl-docs-project.md) - Project docs spec
- [documentation/msl-docs-readme.md](documentation/msl-docs-readme.md) - README spec

## Application Specifications

Specifications for MSL tools (implementations may be in separate repositories):

- [applications/msl-validation-agent.md](applications/msl-validation-agent.md) - Validation tool spec
- [applications/msl-batch-validator.md](applications/msl-batch-validator.md) - Batch validation spec
- [applications/msl-tools-spec.md](applications/msl-tools-spec.md) - General tools spec

## Testing Framework

- [testing/msl-testing-framework.md](testing/msl-testing-framework.md) - Testing infrastructure spec

## Context7 Optimization

For AI agents using context7:

- [context7-optimization/msl-llms-txt-spec.md](context7-optimization/msl-llms-txt-spec.md) - LLM optimization
- [context7-optimization/msl-implementation-reference-spec.md](context7-optimization/msl-implementation-reference-spec.md) - Implementation guide

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