# MSL Specification Index [MSL]

## Summary

This index lists every specification in this directory and helps AI agents and developers find their way around MSL. The language is defined in three levels, L0 to L2; everything else here applies, documents or governs it.

The folders follow [LiveSpec](https://github.com/chrs-myrs/livespec) categories. That layout is this repository's choice; MSL does not require it.

## Directory Structure

```
specs/
├── interfaces/                          # The language: a format contract
│   ├── msl-l0-foundation.spec.md        # Pure markdown with requirements
│   ├── msl-l1-structure.spec.md         # + Optional frontmatter & IDs (extends L0)
│   ├── msl-l2-advanced.spec.md          # + Markers, templates, formal spec (extends L1)
│   └── standards/                       # Quality and design standards
├── features/                            # Tools, documentation, context7 and testing specs
├── artifacts/                           # Claude Code agent specs
├── workspace/metaspecs/                 # Metaspecs governing MSL's own specs
└── foundation/, strategy/, workspace/   # LiveSpec governance for this repository
```

## For AI Agents

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
- **Simple project?** → Use Level 0 (just markdown with requirements). Most projects need no more
- **Need structure?** → Use Level 1 (add frontmatter and IDs)
- **Complex needs?** → Use Level 2 (markers, inheritance, templates)

Worked examples of each level are in [docs/getting-started.md](../docs/getting-started.md) and the agent guide.

## Core Language Specifications

- [interfaces/msl-l0-foundation.spec.md](interfaces/msl-l0-foundation.spec.md) - **Start here for basics**
  - Plain markdown with a `## Requirements` section; no tools needed
  - Also defines how a document identifies itself as MSL
- [interfaces/msl-l1-structure.spec.md](interfaces/msl-l1-structure.spec.md) - **Add structure when needed**
  - YAML frontmatter, requirement IDs, basic inheritance with `extends`
  - Plain L0 documents are valid L1
- [interfaces/msl-l2-advanced.spec.md](interfaces/msl-l2-advanced.spec.md) - **The complete language (all features optional)**
  - Markers: [!], [@user], [#tag], [x]; advanced inheritance; templates and variables
  - Contains the formal grammar (BNF) and semantics; this is where automation begins

```
msl-l0-foundation  →  msl-l1-structure  →  msl-l2-advanced
   (extends)             (extends)
```

Specs outside `interfaces/` use MSL but do not extend the language.

## Standards and Best Practices

- [interfaces/standards/msl-project-organization.spec.md](interfaces/standards/msl-project-organization.spec.md) - **How to structure projects**
- [interfaces/standards/msl-usage-standards.spec.md](interfaces/standards/msl-usage-standards.spec.md) - DRY, inheritance patterns and quality metrics
- [interfaces/standards/msl-extension-standards.spec.md](interfaces/standards/msl-extension-standards.spec.md) - How to extend MSL

## Governance Specifications (Metaspecs)

Metaspecs are specifications that govern other specifications.

- [workspace/metaspecs/msl-core-metaspec.md](workspace/metaspecs/msl-core-metaspec.md) - Governs all MSL specifications
- [workspace/metaspecs/msl-language-metaspec.md](workspace/metaspecs/msl-language-metaspec.md) - Governs language specs
- [workspace/metaspecs/msl-validation-metaspec.md](workspace/metaspecs/msl-validation-metaspec.md) - Validation rules
- [workspace/metaspecs/msl-documentation-metaspec.md](workspace/metaspecs/msl-documentation-metaspec.md) - Documentation governance
- [workspace/metaspecs/testing-framework-metaspec.md](workspace/metaspecs/testing-framework-metaspec.md) - Testing standards

## Tools and Agents

- [features/msl-tools.spec.md](features/msl-tools.spec.md) - Requirements for MSL processing tools
- [features/testing/msl-testing-framework.spec.md](features/testing/msl-testing-framework.spec.md) - Testing infrastructure for the tools
- [artifacts/msl-validation-agent.spec.md](artifacts/msl-validation-agent.spec.md) - Validation agent
- [artifacts/msl-batch-validator.spec.md](artifacts/msl-batch-validator.spec.md) - Batch validation across a spec tree
- [artifacts/pre-push-completeness-checker.spec.md](artifacts/pre-push-completeness-checker.spec.md) - Completeness check before a push

### For Tool Implementers
1. Start with [interfaces/msl-l2-advanced.spec.md](interfaces/msl-l2-advanced.spec.md): requirements, BNF grammar, semantics and processing rules
2. Build progressively: parse L0 (markdown), then L1 (frontmatter, IDs), then L2 (full features)
3. Use [features/msl-tools.spec.md](features/msl-tools.spec.md) for tool requirements

## Documentation Specifications

These specify MSL's own documentation, using inheritance from a common base:

- [features/documentation/msl-docs-base.spec.md](features/documentation/msl-docs-base.spec.md) - Common documentation requirements
- [features/documentation/msl-docs-getting-started.spec.md](features/documentation/msl-docs-getting-started.spec.md) - Quick start spec (extends base)
- [features/documentation/msl-docs-user-guide.spec.md](features/documentation/msl-docs-user-guide.spec.md) - User guide spec (extends base)
- [features/documentation/msl-docs-reference.spec.md](features/documentation/msl-docs-reference.spec.md) - Reference spec (extends base)
- [features/documentation/msl-docs-tutorials.spec.md](features/documentation/msl-docs-tutorials.spec.md) - Tutorial spec (extends base)
- [features/context7-optimization/msl-llms-txt.spec.md](features/context7-optimization/msl-llms-txt.spec.md) - `llms.txt` for AI agents and context7
- [features/context7-optimization/msl-implementation-reference.spec.md](features/context7-optimization/msl-implementation-reference.spec.md) - Implementation reference

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
1. Use msl-lint for syntax checking (`msl-lint specs/`)
2. Verify against relevant metaspecs
3. Ensure cross-references are valid
4. Check requirement testability

## Key Concepts

- **Dogfooding**: MSL specifies itself, proving its completeness
- **Progressive Enhancement**: Start simple, add complexity only when needed ([philosophy](strategy/philosophy.spec.md))
- **Metaspecs**: Specifications that govern other specifications
- **Levels**: L0 (simple) → L1 (structured) → L2 (advanced)

For human readers: browse [examples/](../examples/) for practical demonstrations.
