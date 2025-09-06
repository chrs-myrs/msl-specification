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

### Optional MSL-CONFIG.md

- Projects MAY include an MSL-CONFIG.md file at the project root
- MSL-CONFIG.md SHALL customize MSL usage for the specific project
- MSL-CONFIG.md MAY specify default MSL level, organization pattern, and naming conventions
- MSL-CONFIG.md MAY include project-specific templates and patterns
- AI agents SHALL check for and cache MSL-CONFIG.md when present
- See `/examples/MSL-CONFIG.md` for configuration examples

### Specification Directory Structure

- Project specifications SHOULD be organized for easy discovery (see Organization Patterns below)
- Specifications SHOULD be grouped by functional area or component
- Each specification SHALL have a clear, descriptive filename using kebab-case
- All specifications SHALL use the `.md` extension
- Specification files SHALL NOT use spaces in filenames

### Recommended Specification Categories

When using centralized organization, consider these categories:
- `core/` - Fundamental project specifications
  - Core business logic
  - Data models
  - System constraints
- `features/` - Feature specifications
  - User-facing features
  - Feature requirements
  - Acceptance criteria
- `architecture/` - System design specifications
  - System components
  - Integration points
  - Technical decisions
- `apis/` - Interface specifications
  - REST APIs
  - GraphQL schemas
  - Event contracts
- `standards/` - Project-specific standards
  - Coding standards
  - Testing requirements
  - Documentation standards

### AI Agent Workflow

- Agents SHALL create PURPOSE.md as the first file in any new project
- Agents SHALL recognize and work with any organization pattern (centralized, colocated, or hybrid)
- Agents SHOULD default to centralized `/specs` for new projects unless directed otherwise
- Agents SHALL discover specifications regardless of their location in the project
- Agents SHALL ensure all specifications are cross-referenced appropriately
- Agents SHALL maintain a README.md that points to PURPOSE.md
- Agents SHALL update PURPOSE.md when project scope changes
- Agents SHOULD create or update INDEX.md when using colocated patterns for discoverability

### Specification Naming Conventions

- Feature specs SHALL be named: `feature-name.md` or `feature-name.spec.md`
- API specs SHALL be named: `service-api.md` or `resource-api.md`
- Architecture specs SHALL be named: `component-architecture.md`
- Data model specs SHALL be named: `entity-model.md`
- Standard specs SHALL be named: `project-standard-name.md`
- Colocated specs MAY use `.spec.md` suffix for clarity (e.g., `auth.spec.md`)

### Discoverability Requirements

- Projects using colocated patterns SHALL maintain an INDEX.md listing all specification locations
- Projects SHOULD use consistent patterns within the same codebase
- README.md SHALL document which organization pattern the project uses
- Specifications SHALL be discoverable by searching for `[MSL]` markers
- Projects MAY use `.mslignore` file to exclude non-specification markdown files from discovery
- AI agents SHALL check common locations: `/specs`, `/src/**/*.spec.md`, `/docs/specs`

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

## Organization Patterns

MSL supports multiple organization patterns. Choose based on your project's needs:

### Pattern 1: Centralized (/specs)
**Best for:** AI-first development, spec-first workflow, clear separation of concerns

```
project/
├── PURPOSE.md
├── specs/
│   ├── core/
│   ├── features/
│   └── apis/
└── src/
```

**Benefits:**
- AI agents find all specs in one location
- Clear separation of requirements from implementation
- Easy to review all project requirements at once
- Supports spec-first development workflow

**Trade-offs:**
- Requires discipline to keep specs updated with code changes
- Developers may not see specs in their daily workflow

### Pattern 2: Colocated (alongside code)
**Best for:** Maintaining spec-code sync, developer workflow, component ownership

```
project/
├── PURPOSE.md
├── src/
│   ├── auth/
│   │   ├── auth.ts
│   │   └── auth.spec.md
│   └── payments/
│       ├── payments.ts
│       └── payments.spec.md
└── README.md
```

**Benefits:**
- Specs naturally updated when code changes
- Developers see specs in their workflow
- Clear component ownership
- Proven pattern (similar to colocated tests)

**Trade-offs:**
- AI agents need to search multiple locations
- Harder to see all requirements at once

### Pattern 3: Hybrid
**Best for:** Large projects, mixed teams, balancing both approaches

```
project/
├── PURPOSE.md
├── specs/              # System-level specs
│   ├── architecture/
│   └── standards/
├── src/
│   ├── auth/
│   │   └── auth.spec.md    # Component specs
│   └── payments/
│       └── payments.spec.md
└── docs/
```

**Benefits:**
- System requirements centralized for easy review
- Implementation details colocated for maintenance
- Supports different types of specifications optimally

**Trade-offs:**
- Need clear guidelines on what goes where
- Slightly more complex initial setup

### Choosing a Pattern

Consider these factors:
- **Team size:** Small teams may prefer simplicity of colocation
- **AI usage:** Heavy AI usage benefits from centralized specs
- **Project type:** Libraries may prefer colocation, applications may prefer centralized
- **Development workflow:** Spec-first favors centralized, iterative favors colocated

## Examples

### Example 1: Centralized Pattern (Traditional)
```
my-project/
├── PURPOSE.md          # Project purpose and constraints
├── MSL-CONFIG.md      # Optional: Project-specific MSL configuration
├── README.md          # Points to PURPOSE.md, documents pattern used
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
└── src/               # Implementation
    ├── auth/
    │   └── auth.ts
    └── reporting/
        └── reporting.ts
```

### Example 2: Colocated Pattern (Component-based)
```
my-library/
├── PURPOSE.md
├── README.md          # Documents colocated pattern
├── INDEX.md           # Lists all spec locations
├── src/
│   ├── auth/
│   │   ├── auth.ts
│   │   ├── auth.spec.md      # Component specification
│   │   └── auth.test.ts
│   ├── database/
│   │   ├── database.ts
│   │   ├── database.spec.md  # Component specification
│   │   └── database.test.ts
│   └── api/
│       ├── api.ts
│       └── api.spec.md        # Component specification
└── package.json
```

### Example 3: Hybrid Pattern (Mixed approach)
```
enterprise-app/
├── PURPOSE.md
├── README.md          # Documents hybrid pattern
├── specs/             # System-level specifications
│   ├── INDEX.md       # Maps all specifications
│   ├── architecture/
│   │   └── system-design.md
│   ├── standards/
│   │   ├── coding-standards.md
│   │   └── security-standards.md
│   └── metaspecs/
│       └── api-metaspec.md
├── src/
│   ├── auth/
│   │   ├── auth.ts
│   │   └── auth.spec.md      # Component spec
│   ├── payments/
│   │   ├── payments.ts
│   │   └── payments.spec.md  # Component spec
│   └── shared/
│       └── shared.spec.md    # Shared utilities spec
└── docs/
    └── api-docs.md
```

## Notes

This standard is itself an MSL specification, demonstrating that MSL can define its own organizational patterns. AI agents reading this via context7 or similar tools can immediately understand how to structure new MSL projects.

The flexibility of this standard allows projects to start simple (just PURPOSE.md) and grow organically as complexity increases, embodying MSL's progressive enhancement philosophy.