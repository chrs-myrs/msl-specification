# Getting Started with MSL

**MSL lets you write specifications in markdown that are both human-friendly and machine-processable. Start with simple markdown, add structure only when you need it.**

In the next 5 minutes, you'll create your first MSL specification and understand the core concepts.

## Prerequisites

- A text editor (any editor - VS Code, Notepad, vim, etc.)
- Basic markdown knowledge (headers, lists)
- That's it! No tools or installation required

## Your First MSL Specification

### Step 1: Create a Markdown File

Create a file called `login-system.md`:

```markdown
# Login System

## Requirements
- Users can log in with username and password
- System remembers users for 30 days
- Password reset via email
```

**Congratulations!** You just wrote your first MSL specification. This is valid MSL Level 0.

### Step 2: Add a Requirements Section (Required)

MSL has only ONE hard requirement: a `## Requirements` section.

```markdown
# My System

## Requirements
- At least one requirement here
```

Without a Requirements section, it's just markdown - not MSL.

### Step 3: View Your Specification

Since MSL is just markdown:
- View it on GitHub
- Open in any markdown editor
- Share via email or Slack
- No special tools needed!

### Step 4: Validate Your Specification (Optional)

When you want to check quality:

```bash
# If you have Node.js:
npx msl-lint login-system.md

# Or online validator:
# https://msl-validator.example.com
```

## Understanding MSL Levels

MSL has three levels. **Start with Level 0 and only move up when needed:**

### Level 0: Pure Markdown
```markdown
# Payment Processing

## Requirements
- Accept credit cards
- Support refunds
- Send receipts
```
✅ Perfect for: Quick notes, early drafts, simple projects

### Level 1: Structured
```markdown
---
id: payment-v2
version: 2.0
assignee: payments-team
---
# Payment Processing

## Requirements
- REQ-001: Accept credit cards
- REQ-002: Support refunds within 30 days
- REQ-003: Email receipts immediately
```
✅ Perfect for: Tracking requirements, team collaboration

### Level 2: Advanced
```markdown
---
id: payment-v3
extends: payment-v2
---
# Payment Processing V3

## Requirements
- REQ-001: [OVERRIDE] Accept cards and crypto
- REQ-004: [NEW] Support installment payments
```
✅ Perfect for: Complex systems, inheritance, large projects

## When to Use Each Level

```
Start new specification?
    ↓
Use Level 0 (just markdown)
    ↓
Need requirement IDs for tracking?
    ↓
Add Level 1 (frontmatter + IDs)
    ↓
Need inheritance or templates?
    ↓
Use Level 2 (full features)
```

## Common Examples

### Example 1: Simple Feature Spec (Level 0)

```markdown
# User Profile Feature

## Requirements
- Users can upload profile photo
- Users can set display name
- Users can write bio (max 500 chars)
- Profile is public by default
- Users can make profile private
```

### Example 2: API Specification (Level 1)

```markdown
---
id: user-api
version: 1.0
tags: [api, rest, json]
---
# User API

## Requirements
- REQ-001: GET /users returns user list
- REQ-002: GET /users/{id} returns single user
- REQ-003: POST /users creates new user
- REQ-004: All endpoints require API key
- REQ-005: Responses use JSON format
```

### Example 3: Extended Specification (Level 2)

```markdown
---
id: admin-api
extends: user-api
---
# Admin API

## Requirements
- REQ-006: [NEW] DELETE /users/{id} removes user
- REQ-007: [NEW] PUT /users/{id}/ban bans user
- REQ-004: [OVERRIDE] Requires admin API key
```

## What's Next?

Now that you've created your first MSL specification:

### Learn More
📖 **[User Guide](user-guide.md)** - Comprehensive guide to all MSL features  
🎯 **[Tutorials](tutorials/)** - Step-by-step tutorials for common tasks  
🔍 **[Language Reference](reference.md)** - Complete syntax reference

### Choose Your Path

#### If you're working alone:
→ Read the [Solo Workflow Guide](workflows/solo.md)

#### If you're in a team:
→ Read the [Team Workflow Guide](workflows/team.md)  

#### If you want to use AI assistants:
→ Read the [AI Integration Guide](workflows/ai.md)

### Should I Use Level 0, 1, or 2?

| Question | Level 0 | Level 1 | Level 2 |
|----------|---------|---------|---------|
| Just starting? | ✅ **Yes** | No | No |
| Need requirement tracking? | No | ✅ **Yes** | Yes |
| Multiple related specs? | No | No | ✅ **Yes** |
| Team collaboration? | Maybe | ✅ **Yes** | Yes |
| Complex inheritance? | No | No | ✅ **Yes** |

**Remember: Start simple!** You can always add complexity later.

## Common Questions

**Q: Do I need to install anything?**  
A: No! MSL is just markdown. Tools are optional.

**Q: Can I convert existing documents?**  
A: Yes! Add a `## Requirements` section to any markdown file.

**Q: What if I make mistakes?**  
A: MSL is forgiving. If it's valid markdown with requirements, it's valid MSL.

**Q: Can I use my existing tools?**  
A: Yes! Any markdown editor works with MSL.

**Q: How do I share specifications?**  
A: Like any markdown file - GitHub, email, Slack, etc.

## Try It Yourself

1. Create a specification for something you're working on
2. Start with Level 0 - just markdown
3. Add structure only when you need it
4. Share it with your team

Welcome to MSL! 🎉

---

[← Back to README](../README.md) | [User Guide →](user-guide.md)