# Solo Developer Workflow

> How to use MSL effectively as an individual developer

## Philosophy

When working alone, your specification system should:
- **Start instantly** - No setup overhead
- **Stay flexible** - Change without ceremony
- **Track naturally** - Use git as your database
- **Scale gradually** - Add complexity only when needed

## Getting Started

### Your First Spec

Create specs alongside your code:

```
my-project/
├── src/
├── specs/
│   └── features.md
└── README.md
```

Start with plain markdown:

```markdown
# Features

## Requirements
- User authentication
- Data persistence
- API endpoints
```

### Evolution Pattern

Watch how a spec naturally evolves:

#### Week 1: Brain dump
```markdown
# Project Ideas

## Requirements
- Need user login
- Store data somewhere
- REST API probably
```

#### Week 2: Getting specific
```markdown
# Authentication System

## Requirements
- Email/password login
- JWT tokens
- Password reset via email
- 2FA optional
```

#### Week 4: Tracking progress
```markdown
# Authentication System

## Requirements
- [x] Email/password login
- [x] JWT tokens
- [ ] Password reset via email
- [?] 2FA optional
```

#### Week 8: Full structure
```markdown
---
id: auth-system
tags: [backend, security]
---

# Authentication System

## Requirements
- REQ-001: [x] Email/password login
- REQ-002: [x] JWT tokens (15min expiry)
- REQ-003: [@next-sprint] Password reset
- REQ-004: [?] 2FA support
```

## File Organization Patterns

### By Feature
```
specs/
├── auth.md
├── api.md
├── database.md
└── ui.md
```

### By Status
```
specs/
├── active/
│   └── current-sprint.md
├── backlog/
│   └── future-ideas.md
└── done/
    └── completed.md
```

### By Date (Journal Style)
```
specs/
├── 2024-12-15.md
├── 2024-12-20.md
└── 2024-12-21.md
```

### Flat with Prefixes
```
specs/
├── 01-auth.md
├── 02-api.md
├── 03-database.md
└── xx-ideas.md
```

## Quick Markers for Solo Work

Use inline markers instead of frontmatter:

| Marker | Meaning | Use Case |
|--------|---------|----------|
| `[!]` | Critical | Must have |
| `[?]` | Uncertain | Need to research |
| `[x]` | Done | Completed |
| `[ ]` | Todo | Not started |
| `[@today]` | Time-based | Personal deadline |
| `[#mvp]` | Tagged | Categorization |

Example:
```markdown
## Requirements
- [!] Fix login bug
- [x] Add user profiles
- [@today] Deploy to staging
- [?] Add social login
- [#v2] Advanced analytics
```

## Git Workflow

### Daily Commits
```bash
# Quick save everything
git add -A && git commit -m "Specs update"

# Or with more context
git commit -am "Add auth requirements"
```

### Using Branches
```bash
# New feature planning
git checkout -b feature/payment-specs
# ... edit specs ...
git commit -am "Plan payment system"
git checkout master
```

### Tagging Milestones
```bash
# Mark important points
git tag -a v1-spec -m "Version 1 requirements complete"
git tag planning-done
git tag mvp-defined
```

## Templates for Common Patterns

### API Endpoint
```markdown
# ${Endpoint Name}

## Requirements
- Method: ${GET|POST|PUT|DELETE}
- Path: ${/api/resource}
- Auth: ${Required|Optional|None}
- Request: ${Schema}
- Response: ${Schema}
- Errors: ${List}
```

### Feature Spec
```markdown
# ${Feature Name}

## Requirements
- User story
- Acceptance criteria
- Edge cases
- Performance needs
- Security considerations
```

### Bug Report
```markdown
# Bug: ${Title}

## Requirements
- Reproduce: Steps
- Expected: Behavior
- Actual: What happens
- Fix: Solution approach
```

## LLM Integration

### Quick Commands

Generate specs:
```markdown
"Convert this user story to MSL format:
As a user, I want to reset my password
so that I can regain access to my account"
```

Review specs:
```markdown
"Review this MSL spec for completeness:
[paste your spec]"
```

Find gaps:
```markdown
"What requirements am I missing for a payment system?
Current requirements:
[paste your requirements]"
```

## Tips and Tricks

### 1. Start Ugly
Don't worry about structure initially. Just write.

### 2. Refactor When Needed
When a spec gets messy, take 5 minutes to reorganize.

### 3. Use Your Editor
- Set up markdown snippets
- Use outline view for navigation
- Enable spell check

### 4. Keep Specs Close to Code
```
src/
├── auth/
│   ├── login.js
│   └── login.spec.md
```

### 5. Version Control Everything
Specs are code. Treat them as such.

### 6. Don't Over-Engineer
If you don't need IDs, don't add them.
If you don't need frontmatter, skip it.

## Common Workflows

### Planning a New Feature
1. Create `feature-name.md`
2. Brain dump requirements
3. Add markers for priority
4. Implement highest priority first
5. Check off as you complete

### Refactoring
1. Document current behavior
2. Mark what needs to change
3. Update spec as you refactor
4. Spec becomes your checklist

### Debugging
1. Create `bug-investigation.md`
2. Document symptoms
3. Add requirements for fix
4. Track what you've tried
5. Document solution

## Advanced Patterns

### Inheritance for Variants
```markdown
<!-- extends: base-api -->

# User API

## Requirements
- [INHERIT] Standard REST endpoints
- [NEW] User-specific validations
```

### Variables for Reuse
```markdown
---
variables:
  timeout: 30
  rate_limit: 100
---

## Requirements
- Timeout after ${timeout} seconds
- Rate limit: ${rate_limit} req/min
```

## Tools for Solo Developers

### Essential
- Your text editor
- Git

### Optional
- `msl-lint` - Catch issues early
- `msl-render` - Process templates

### Nice to Have
- Editor plugin (when available)
- Quick scripts for common tasks

## Moving to Team Work

When you're ready to collaborate:

1. **Add IDs** to requirements for clear references
2. **Use frontmatter** for metadata
3. **Create templates** for consistency
4. **Document conventions** in README
5. **Set up CI** to validate specs

See [Team Workflow](team-workflow.md) for details.

## Remember

The best specification system is the one you actually use. Start simple, stay consistent, and let it grow with your needs.