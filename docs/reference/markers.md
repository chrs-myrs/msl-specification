# MSL Quick Markers Reference

Quick markers let you add metadata to requirements without using frontmatter. Perfect for rapid development and personal projects.

## Priority & Status Markers

### Core Markers

| Marker | Meaning | Use When | Example |
|--------|---------|----------|---------|
| `[!]` | Critical/High Priority | Must have, blocker, urgent | `- [!] Fix security vulnerability` |
| `[?]` | Uncertain/Needs Clarification | Unsure, needs research, TBD | `- [?] Support IE11?` |
| `[x]` | Completed/Done | Finished, implemented, tested | `- [x] User login working` |
| `[ ]` | Pending/Todo | Not started, planned | `- [ ] Add password reset` |

### Examples in Context

```markdown
## Requirements
- [!] Critical: Data must be encrypted at rest
- [x] Completed: User authentication implemented  
- [ ] Pending: Add forgot password feature
- [?] Uncertain: Do we need SAML support?
```

## Assignment Markers

Use `[@username]` to assign requirements:

```markdown
## Requirements
- [@alice] Design the API endpoints
- [@bob] Implement database schema
- [@carol] Write integration tests
- [@team-frontend] Build UI components
```

### Special Assignments

```markdown
- [@me] Personal todo
- [@anyone] Up for grabs
- [@review] Needs review
- [@blocked] Blocked on dependencies
```

## Tag Markers

Use `[#tag]` to categorize requirements:

```markdown
## Requirements
- [#mvp] Core user authentication
- [#v2] Advanced analytics dashboard
- [#security] Implement rate limiting
- [#performance] Optimize database queries
- [#ux] Improve error messages
```

### Common Tag Patterns

```markdown
# Version Tags
- [#v1] [#v1.1] [#v2]

# Priority Tags  
- [#must-have] [#nice-to-have] [#future]

# Component Tags
- [#backend] [#frontend] [#api] [#database]

# Type Tags
- [#feature] [#bugfix] [#enhancement] [#refactor]
```

## Combining Markers

You can combine multiple markers:

```markdown
## Requirements
- [!] [@alice] [#security] Implement 2FA
- [?] [#v2] Machine learning recommendations
- [x] [@bob] [#mvp] Basic CRUD operations
- [ ] [#performance] Add caching layer
```

## Time-Based Markers

For personal productivity:

```markdown
## Requirements
- [@today] Finish login component
- [@tomorrow] Start API integration
- [@this-week] Complete testing
- [@sprint-3] Implement notifications
- [@q1-2025] Plan architecture redesign
```

## Status Flow

Show requirement lifecycle:

```markdown
## Requirements
- [ ] Design feature          # Not started
- [ ] [@alice] Design feature # Assigned
- [~] Design feature          # In progress (custom)
- [?] Design feature          # Blocked/unclear
- [x] Design feature          # Complete
```

## Custom Markers

Create your own conventions:

```markdown
## Requirements
- [P0] Highest priority (custom priority system)
- [EST:3d] Estimated 3 days
- [BLOCKED] Waiting on dependency
- [REVIEW] Ready for review
- [TESTED] Has test coverage
```

## Inheritance Markers

When extending specifications:

| Marker | Purpose | Example |
|--------|---------|---------|
| `[OVERRIDE]` | Replace parent requirement | `- REQ-001: [OVERRIDE] Modified login flow` |
| `[NEW]` | Add new requirement | `- REQ-005: [NEW] Add OAuth support` |
| `[INHERIT]` | Explicitly keep parent version | `- REQ-002: [INHERIT] Standard timeout` |

Alternative syntax:
```markdown
- Modified: Changed login to use JWT
- New: Added biometric authentication
```

## Escaping Markers

When you need literal brackets:

```markdown
## Requirements
- Use \[square brackets\] in text        # Shows [square brackets]
- Array access uses data\[index\]        # Shows data[index]
- Not a marker: \[@literal\]            # Shows [@literal]
```

## Marker Best Practices

### DO
- ✅ Use consistent markers across your project
- ✅ Document custom markers in README
- ✅ Keep markers simple and memorable
- ✅ Use markers that work with your tools

### DON'T
- ❌ Mix different marker styles randomly
- ❌ Create too many custom markers
- ❌ Use markers that conflict with Markdown
- ❌ Forget to escape literal brackets

## Tool Support

### Grep/Search
```bash
# Find critical requirements
grep '\[!\]' specs/*.md

# Find Alice's tasks
grep '\[@alice\]' specs/*.md

# Find incomplete items
grep '\[ \]' specs/*.md
```

### VS Code Snippets
```json
{
  "Critical Requirement": {
    "prefix": "req!",
    "body": ["- [!] ${1:requirement}"]
  },
  "Assigned Requirement": {
    "prefix": "req@",
    "body": ["- [@${1:user}] ${2:requirement}"]
  }
}
```

### Git Aliases
```bash
# Show completed requirements in last commit
git diff HEAD^ HEAD | grep '+ .*\[x\]'

# Find TODOs
git grep '\[ \]' -- '*.md'
```

## Migration Path

### From Todo Apps
```markdown
Before: ☐ Add login
After:  - [ ] Add login

Before: ✓ Setup database  
After:  - [x] Setup database

Before: ⚠ Check security
After:  - [!] Check security
```

### From Issue Trackers
```markdown
Before: P0 - Critical bug
After:  - [!] Critical bug

Before: Assigned to Alice
After:  - [@alice] Task

Before: Label: frontend
After:  - [#frontend] Task
```

## Quick Reference Card

```
Priority:     [!] = critical    [?] = uncertain
Status:       [x] = done        [ ] = pending
Assignment:   [@user] = assigned to user
Tags:         [#tag] = categorized with tag
Inheritance:  [NEW] [OVERRIDE] [INHERIT]

Combine as needed: - [!] [@alice] [#security] Fix auth
```

## Examples Gallery

### Sprint Planning
```markdown
## Sprint 15 Goals
- [!] [@alice] [#mvp] Complete user authentication
- [!] [@bob] [#mvp] Deploy to staging
- [ ] [@carol] [#testing] Write E2E tests
- [?] [#research] Investigate GraphQL migration
```

### Bug Tracking
```markdown
## Known Issues
- [!] [#prod] Memory leak in worker process
- [x] [#fixed] Login redirect loop
- [ ] [@john] [#ui] Button alignment on mobile
- [?] [#cannot-reproduce] Intermittent timeout
```

### Feature Planning
```markdown
## Payment System
- [x] [#done] Research payment providers
- [!] [@team] [#current] Implement Stripe integration
- [ ] [#next] Add PayPal support
- [?] [#future] Cryptocurrency payments?
```

---

*Quick markers: Making requirements trackable without the overhead*