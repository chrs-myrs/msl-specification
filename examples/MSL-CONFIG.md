# MSL Configuration for Example Project [MSL]

## Summary

This example shows how projects can customize their MSL usage. Place this file at your project root to override default MSL behaviors for AI agents.

## Configuration

```yaml
# MSL Configuration
msl-level: L1                    # Default MSL level for this project (L0, L1, or L2)
organization: hybrid             # Spec organization pattern (centralized, colocated, or hybrid)
spec-suffix: .spec.md           # File naming convention for specifications
auto-validate: true             # Run validation on spec changes
```

## Project Patterns

### Where Specifications Live
- System-level specs: `/specs/architecture/`
- API contracts: `/specs/apis/`
- Component specs: Colocated with implementation (`src/*/**.spec.md`)
- Test specs: `/specs/testing/`

### Naming Conventions
- Features: `feature-{name}.spec.md`
- APIs: `{service}-api.spec.md`
- Components: `{component}.spec.md`
- Data models: `{entity}-model.spec.md`

## Custom Templates

### Feature Specification Template
```markdown
---
id: feature-{name}
tags: [feature, {category}]
priority: {high|medium|low}
sprint: {number}
---

# {Feature Name} [MSL]

## Summary
{One paragraph describing the feature}

## Requirements
- REQ-001: {Functional requirement}
- REQ-002: {Non-functional requirement}
- REQ-003: {Acceptance criterion}

## Dependencies
- {Related feature or component}
```

### API Endpoint Template
```markdown
---
id: {method}-{path}
tags: [api, rest, {resource}]
---

# {METHOD} {/path} [MSL]

## Summary
{Endpoint description}

## Requirements
- REQ-001: Request format
- REQ-002: Response format
- REQ-003: Authentication required
- REQ-004: Rate limiting rules
- REQ-005: Error responses
```

### Component Specification Template
```markdown
---
id: {component-name}
tags: [component, {layer}]
extends: {base-component}  # if applicable
---

# {Component Name} [MSL]

## Summary
{Component responsibility}

## Requirements
### Interface
- REQ-101: Public API surface
- REQ-102: Input validation

### Behavior
- REQ-201: Core functionality
- REQ-202: Error handling

### Performance
- REQ-301: Response time requirements
- REQ-302: Resource constraints
```

## Project-Specific Rules

### Required Metadata
All specifications in this project MUST include:
- `id`: Unique identifier
- `tags`: At least one category tag
- `priority`: high, medium, or low
- `owner`: Team or person responsible

### Inheritance Rules
- UI components extend: `ui-component-base`
- API specs extend: `rest-api-base`
- Service specs extend: `microservice-base`

### Validation Rules
- All requirements must have REQ-{number} format
- Requirements must be measurable
- Each spec must have at least 3 requirements
- Specs must be reviewed before implementation

## AI Agent Instructions

When working in this project:
1. Always use L1 (with frontmatter) unless specified otherwise
2. Place component specs next to their implementation
3. Use the templates above for consistency
4. Run validation before committing specs
5. Update INDEX.md when adding new specifications

## Quick Reference

| Spec Type | Location | Template | Default Level |
|-----------|----------|----------|---------------|
| System | `/specs/architecture/` | System template | L1 |
| Feature | `/specs/features/` | Feature template | L1 |
| API | `/specs/apis/` | API template | L1 |
| Component | `src/{component}/` | Component template | L1 |
| Data Model | `/specs/models/` | Model template | L0 |

## Notes

This configuration helps AI agents work efficiently with MSL in this specific project. It overrides general MSL defaults with project-specific patterns while maintaining MSL principles.

Agents should cache this file along with `/AGENTS.md` for optimal performance.

---
*MSL Configuration Example - Customize for your project needs*