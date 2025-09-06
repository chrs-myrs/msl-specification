---
id: msl-project-organization
type: standard
governed-by: msl-usage-standards
tags: [standard, project, organization, best-practices]
---

# MSL Project Organization Standard [MSL]

## Summary

This standard defines how to organize MSL-based projects for maximum discoverability by AI agents and human developers. Following this standard ensures consistent, maintainable specification-driven projects.

## Requirements

### Project Initialization

- Every MSL-based project SHALL begin with creating a PURPOSE.md specification
- PURPOSE.md SHALL be an MSL specification defining project goals, constraints, and philosophy
- PURPOSE.md SHALL be located at the project root directory
- AI agents SHALL read PURPOSE.md first when starting work on any project
- PURPOSE.md SHALL reference this organization standard for structure guidance

### PURPOSE.md Structure

- PURPOSE.md SHALL include a "## Requirements" section with project goals
- PURPOSE.md SHALL define project constraints and non-goals
- PURPOSE.md SHALL specify which MSL level (L0, L1, or L2) the project uses
- PURPOSE.md SHALL list key stakeholders and their concerns
- PURPOSE.md SHALL define success criteria for the project

### Specification Directory Structure

- Project specifications SHALL be organized in a `/specs` directory at project root
- Specifications SHALL be grouped by functional area in subdirectories
- Each specification SHALL have a clear, descriptive filename using kebab-case
- All specifications SHALL use the `.md` extension
- Specification files SHALL NOT use spaces in filenames

### Recommended Specification Categories

- `/specs/core/` SHALL contain fundamental project specifications
  - Core business logic
  - Data models
  - System constraints
- `/specs/features/` SHALL contain feature specifications
  - User-facing features
  - Feature requirements
  - Acceptance criteria
- `/specs/architecture/` SHALL contain system design specifications
  - System components
  - Integration points
  - Technical decisions
- `/specs/apis/` SHALL contain interface specifications
  - REST APIs
  - GraphQL schemas
  - Event contracts
- `/specs/standards/` SHALL contain project-specific standards
  - Coding standards
  - Testing requirements
  - Documentation standards

### AI Agent Workflow

- Agents SHALL create PURPOSE.md as the first file in any new project
- Agents SHALL create the `/specs` directory structure after PURPOSE.md
- Agents SHALL organize specifications according to these categories
- Agents SHALL ensure all specifications are cross-referenced appropriately
- Agents SHALL maintain a README.md that points to PURPOSE.md
- Agents SHALL update PURPOSE.md when project scope changes

### Specification Naming Conventions

- Feature specs SHALL be named: `feature-name.md`
- API specs SHALL be named: `service-api.md` or `resource-api.md`
- Architecture specs SHALL be named: `component-architecture.md`
- Data model specs SHALL be named: `entity-model.md`
- Standard specs SHALL be named: `project-standard-name.md`

### Cross-Referencing

- Specifications SHALL reference related specs using relative paths
- Specifications SHALL use markdown links for cross-references
- Child specifications SHALL declare parent specs using `extends:` in frontmatter
- Related specifications SHALL be listed in a "## Related Specifications" section

### Versioning and Evolution

- Major specification changes SHALL be tracked in version control
- Breaking changes SHALL be documented in the specification
- Deprecated requirements SHALL be marked with [DEPRECATED] markers
- New requirements SHALL be marked with [NEW] when added to existing specs

### Best Practices

- Projects SHOULD define their own metaspecs for domain-specific governance
- Complex projects SHOULD create an INDEX.md listing all specifications
- All specifications SHOULD be validated using msl-lint before implementation
- Projects SHOULD maintain traceability between specs and implementation
- Specifications SHOULD be updated when implementation reveals new requirements

### Anti-Patterns to Avoid

- Specifications SHALL NOT include implementation code
- Specifications SHALL NOT be deeply nested (maximum 2 levels of subdirectories)
- Specifications SHALL NOT duplicate requirements across multiple files
- Specifications SHALL NOT use proprietary formats or tools

## Examples

### Minimal Project Structure
```
my-project/
├── PURPOSE.md          # Project purpose and constraints
├── README.md          # Points to PURPOSE.md
└── specs/
    └── core/
        └── main-feature.md
```

### Standard Project Structure
```
my-project/
├── PURPOSE.md
├── README.md
├── specs/
│   ├── INDEX.md       # Optional specification index
│   ├── core/
│   │   ├── user-model.md
│   │   └── business-logic.md
│   ├── features/
│   │   ├── authentication.md
│   │   └── reporting.md
│   └── apis/
│       └── rest-api.md
└── src/               # Implementation (not part of MSL)
```

### Enterprise Project Structure
```
my-project/
├── PURPOSE.md
├── README.md
├── specs/
│   ├── INDEX.md
│   ├── metaspecs/     # Project-specific governance
│   │   └── api-metaspec.md
│   ├── core/
│   ├── features/
│   ├── architecture/
│   ├── apis/
│   └── standards/
│       ├── testing-standards.md
│       └── security-standards.md
└── [implementation directories]
```

## Notes

This standard is itself an MSL specification, demonstrating that MSL can define its own organizational patterns. AI agents reading this via context7 or similar tools can immediately understand how to structure new MSL projects.

The flexibility of this standard allows projects to start simple (just PURPOSE.md) and grow organically as complexity increases, embodying MSL's progressive enhancement philosophy.