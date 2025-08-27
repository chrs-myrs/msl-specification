# MSL Quick Start Guide

## Installation

MSL doesn't require installation - it's just markdown! However, optional tools are available:

```bash
# Option 1: Install globally
pip install msl-tools

# Option 2: Use directly from repository
git clone https://github.com/chrs-myrs/msl-specification.git
cd msl-specification
python tools/cli/msl-lint your-spec.md
```

## Your First Spec (Level 0)

Create `user-auth.md`:

```markdown
# User Authentication

## Summary
Basic authentication system for web application.

## Requirements
- Users can register with email and password
- Email verification required
- Password reset via email
- Session timeout after 30 minutes
```

This is valid MSL! No special syntax needed.

## Adding Structure (Level 1)

Add IDs when you need to reference requirements:

```markdown
# User Authentication

## Requirements
- REQ-001: Users can register with email and password
- REQ-002: Email verification required
- REQ-003: Password reset via email
- REQ-004: Session timeout after 30 minutes
```

## Adding Metadata (Level 2)

Add frontmatter for advanced features:

```markdown
---
id: user-auth
tags: [security, backend]
priority: high
status: draft
---

# User Authentication

## Requirements
- REQ-001: [!] Users can register with email and password
- REQ-002: [!] Email verification required
- REQ-003: Password reset via email
- REQ-004: Session timeout after 30 minutes
```

## Quick Markers

Use inline markers for rapid development:

- `[!]` - Critical priority
- `[?]` - Uncertain/needs clarification
- `[x]` - Completed
- `[ ]` - Pending
- `[@alice]` - Assigned to alice
- `[#api]` - Tagged with 'api'

## Validation

Check your specs:

```bash
# Lint a single file
msl-lint user-auth.md

# Lint all specs in directory
msl-lint specs/

# Check for ID conflicts
msl-lint --check-ids specs/
```

## Templates and Inheritance

Create reusable templates:

`templates/api-base.md`:
```markdown
---
id: api-template
type: template
---

# ${service_name} API

## Requirements
- REQ-001: RESTful endpoints
- REQ-002: JSON request/response
- REQ-003: Rate limiting
```

Use the template:

`payment-api.md`:
```markdown
---
extends: api-template
variables:
  service_name: Payment
---

# ${service_name} API

## Requirements
- REQ-001: [INHERIT] RESTful endpoints
- REQ-002: [INHERIT] JSON request/response
- REQ-003: [OVERRIDE] Rate limiting: 100 req/min
- REQ-004: [NEW] PCI compliance required
```

## File Organization

Suggested structure for projects:

```
project/
├── specs/
│   ├── features/       # Feature specifications
│   ├── apis/          # API specifications
│   └── templates/     # Reusable templates
├── requirements.md    # High-level requirements
└── architecture.md    # System architecture
```

## Next Steps

- Read [Solo Workflow Guide](solo-workflow.md) for individual developers
- Read [Team Workflow Guide](team-workflow.md) for collaboration
- Browse [Examples](../../examples/) for real-world usage
- See [Full Specification](../spec/v1.1/specification.md) for all features

## Common Patterns

### User Stories to MSL

```markdown
# Feature: User Login

## Requirements
- REQ-001: Users can log in with valid credentials
  - Given a registered user
  - When they provide correct email/password
  - Then they are authenticated
```

### Test Coverage Tracking

```markdown
## Requirements
- REQ-001: [x] Login with email (test: auth.test.js:15)
- REQ-002: [ ] Login with username
- REQ-003: [x] Password reset (test: auth.test.js:45)
```

### Progressive Detail

Start simple:
```markdown
## Requirements
- User login
```

Add detail when needed:
```markdown
## Requirements
- REQ-001: User login
  - Email or username
  - Password validation
  - Remember me option
  - OAuth support
```

## Tips

1. **Start without tools** - Just write markdown
2. **Add IDs when referencing** - Only when you need them
3. **Use markers for quick tracking** - `[!]`, `[?]`, `[x]`
4. **Template common patterns** - Don't repeat yourself
5. **Keep specs near code** - In the same repository