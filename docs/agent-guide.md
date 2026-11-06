# MSL Agent Configuration [MSL]

## Summary

This document provides essential MSL knowledge for AI agents. Cache this once per session to handle 90% of MSL operations without repeated context7 lookups. Check for project-specific `MSL-CONFIG.md` for overrides.

## Requirements

### Agent Behavior
- Agents SHALL cache this document for the entire session
- Agents SHALL check for project-specific MSL-CONFIG.md files
- Agents SHALL start with the simplest MSL level that meets needs
- Agents SHALL fetch detailed specs only when triggered by specific needs

## Quick Start Template (80% of Cases)

```markdown
# [Component/Feature Name] [MSL]

## Summary

[One clear sentence describing what this specifies]

## Requirements

- [Specific, testable requirement]
- [Another requirement focused on WHAT, not HOW]
- [Keep requirements high-level when possible]
```

That's it. Most specifications need nothing more than this L0 format.

## Decision Tree

```
Need to specify something?
├─ Just requirements? → **Use L0** (markdown with ## Requirements)
├─ Need metadata/IDs? → **Use L1** (add YAML frontmatter)
└─ Need inheritance/templates? → **Use L2** (rarely needed)
```

**Remember:** Start with L0. You can always add complexity later if truly needed.

## Essential Templates

### L0: Basic Specification
```markdown
# Login System [MSL]

## Summary

Specification for user authentication and session management.

## Requirements

- Users can authenticate with email and password
- Sessions expire after 30 minutes of inactivity
- Failed attempts lock account after 5 tries
```

### L1: Specification with Metadata
```markdown
---
id: user-authentication
tags: [security, auth, core]
priority: high
---

# User Authentication [MSL]

## Summary

Core authentication system requirements with security constraints.

## Requirements

- REQ-001: System must support email/password authentication
- REQ-002: System must implement 2FA for admin accounts
- REQ-003: Password reset must use secure token with 1-hour expiry
```

### L1: API Specification
```markdown
---
id: rest-api
tags: [api, rest, interface]
---

# REST API Specification [MSL]

## Summary

RESTful API requirements for the application backend.

## Requirements

- REQ-001: API must follow REST principles
- REQ-002: All endpoints must return JSON
- REQ-003: Authentication via Bearer tokens
- REQ-004: Rate limiting of 100 requests per minute
```

### L1: Component Specification (Colocated)
```markdown
---
id: payment-processor
tags: [payments, component]
---

# Payment Processor [MSL]

## Summary

Payment processing component handling transactions and refunds.

## Requirements

- REQ-001: Support credit card and PayPal payments
- REQ-002: Process refunds within 24 hours
- REQ-003: Maintain PCI compliance
```

## Organization Patterns

### Pattern 1: Centralized (Default for new projects)
```
project/
├── PURPOSE.md              # Always create first
├── specs/
│   ├── core/
│   ├── features/
│   └── apis/
```

### Pattern 2: Colocated (When specs should live with code)
```
project/
├── PURPOSE.md
├── src/
│   ├── auth/
│   │   ├── auth.ts
│   │   └── auth.spec.md   # Specification next to implementation
```

### Pattern 3: Hybrid (Large projects)
```
project/
├── PURPOSE.md
├── specs/                  # System-level specs
└── src/
    └── components/
        └── *.spec.md       # Component specs
```

## Key Principles to Remember

1. **Start simple** - Add complexity only when it solves a real problem
2. **High-level requirements** - Specify WHAT, not HOW
3. **Trust implementers** - Don't over-prescribe details
4. **Each requirement costs** - Every requirement adds maintenance burden
5. **Avoid premature abstraction** - Don't use inheritance without true "is-a" relationship

## Common Anti-Patterns to Avoid

❌ **Over-specification**
```markdown
Bad:  "Button must be exactly 120px wide with #007bff color"
Good: "Submit button must be clearly visible"
```

❌ **Wrong inheritance**
```markdown
Bad:  extends: msl-l2-advanced  # (unless creating new MSL level)
Good: extends: rest-api-base     # (when your API IS A REST API)
```

❌ **Starting too complex**
```markdown
Bad:  Starting with L2, templates, and markers
Good: Starting with L0, adding features as needed
```

## Validation Checklist (Without Full Validator)

Before committing a specification, check:
- [ ] Requirements are specific and testable
- [ ] No duplicate requirements across specs
- [ ] Using the simplest MSL level that works
- [ ] Title includes [MSL] marker
- [ ] Requirements focus on WHAT, not HOW
- [ ] No unnecessary inheritance

## When to Fetch Full Specifications

Fetch detailed specs only when you need:

| Need | Fetch | When |
|------|-------|------|
| Inheritance syntax | `msl-l2-advanced.md` | Using `extends:` or templates |
| Validation rules | `msl-validation-agent.md` | Running formal validation |
| Organization details | `msl-project-organization.md` | Setting up new project structure |
| Quality standards | `msl-usage-standards.md` | Reviewing specification quality |
| All features | `msl-l0/l1/l2-*.md` | Learning specific level details |

## Project-Specific Configuration

Projects can override defaults with `MSL-CONFIG.md`:

```markdown
# MSL Configuration for [Project Name]

msl-level: L1              # Default level for this project
organization: colocated    # Where specs live
spec-suffix: .spec.md      # Naming convention

## Custom Templates
[Project-specific templates here]
```

## Quick Examples by Use Case

### Specifying a New Feature
```markdown
# User Dashboard [MSL]

## Requirements
- Display user's recent activity
- Show account statistics
- Allow quick actions
```

### Specifying an API Endpoint
```markdown
# GET /users/{id} [MSL]

## Requirements
- Return user data as JSON
- Require authentication
- Include related resources via ?include parameter
```

### Specifying a Component
```markdown
# Data Validation Module [MSL]

## Requirements
- Validate against JSON schema
- Return detailed error messages
- Support custom validation rules
```

## Final Notes

This document gives you working knowledge of MSL. For the full specification, see `/specs/`. Remember: MSL is just markdown with requirements - keep it simple, make it useful.

---
*Agent configuration for [MSL Specification](https://github.com/chrs-myrs/msl-specification)*