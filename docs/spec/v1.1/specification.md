# Markdown Specification Language (MSL) v1.1

> Lightweight specifications that grow with your needs

## Zero to Specification in 30 Seconds

MSL works with plain markdown. Start simple:

```markdown
# Login System

## Requirements
- Users can log in with email/password
- Sessions expire after 30 minutes
- Failed logins lock after 5 attempts
```

That's valid MSL. Add structure as needed:

```markdown
---
id: login-system
---

# Login System

## Requirements
- REQ-001: Users can log in with email/password
- REQ-002: Sessions expire after 30 minutes
- REQ-003: Failed logins lock after 5 attempts
```

---

# Core Specification

## Three Levels of Structure

### Level 0: Pure Markdown
- Any markdown file with `## Requirements` section
- No frontmatter needed
- Filename becomes implicit ID
- Perfect for quick notes and initial thoughts

### Level 1: Basic Structure
```yaml
---
id: my-spec
---
```
- Adds explicit ID
- Enables referencing from other specs
- Minimal overhead

### Level 2: Full Metadata
```yaml
---
spec: v1
id: my-spec
extends: parent-spec
tags: [area, category]
priority: high
status: draft
---
```
- Full inheritance support
- Categorisation and workflow
- Enterprise-ready

## Automatic Conventions

When frontmatter is absent or minimal, MSL applies smart defaults:

| Missing | Default Value | Example |
|---------|--------------|---------|
| No frontmatter | Filename as ID | `login.md` → `id: login` |
| No `spec` | `v1` | Assumes current version |
| No `type` | `requirement` | Most common type |
| No `status` | `draft` | Safe default |
| No `priority` | Inferred from markers | `[!]` → high |

## Progressive Enhancement

### Start Minimal
```markdown
# My Feature

## Requirements
- Thing one
- Thing two
```

### Add IDs When Needed
```markdown
# My Feature

## Requirements
- REQ-001: Thing one
- REQ-002: Thing two
```

### Add Metadata When Useful
```markdown
---
tags: [backend, api]
---

# My Feature

## Requirements
- REQ-001: Thing one
- REQ-002: Thing two
```

### Enable Inheritance When Scaling
```markdown
---
extends: base-template
---

# My Feature

## Requirements
- REQ-001: [OVERRIDE] Modified thing one
- REQ-002: Thing two
- REQ-003: [NEW] Thing three
```

## Quick Markers

For solo work, use inline markers instead of frontmatter:

```markdown
# My Spec

## Requirements
- [!] Critical requirement
- [?] Uncertain requirement  
- [x] Completed requirement
- [ ] Pending requirement
- [@alice] Assigned requirement
- [#api] Tagged requirement
```

These map to:
- `[!]` → `priority: critical`
- `[?]` → `status: uncertain`
- `[x]` → `status: complete`
- `[ ]` → `status: pending`
- `[@user]` → `assignee: user`
- `[#tag]` → `tags: [tag]`

## Simplified Inheritance

When extending specs without full frontmatter:

```markdown
<!-- extends: base-spec -->

# Enhanced Feature

## Requirements
- Base requirement one (inherited)
- Modified: Base requirement two with changes
- New: Additional requirement
```

Keywords `Modified:` and `New:` are alternatives to `[OVERRIDE]` and `[NEW]`.

---

# Solo Practitioner Workflow

## File-Based Organization

For solo work, leverage filesystem as database:

```
specs/
├── active/          # Current work
│   ├── login.md
│   └── api.md
├── templates/       # Reusable patterns
│   └── rest-api.md
├── archive/         # Completed/deprecated
│   └── 2024/
└── ideas/          # Rough drafts
    └── untitled-1.md
```

## Personal Conventions

### Daily Specs
Name files by date for journal-style specs:
```
specs/daily/
├── 2024-12-19.md
├── 2024-12-20.md
└── 2024-12-21.md
```

### Project Prefixes
Use prefixes instead of folders for flat structure:
```
specs/
├── proj1-auth.md
├── proj1-api.md
├── proj2-design.md
└── proj2-implementation.md
```

## Git-Light Workflow

For solo work, minimal git usage:

```bash
# Quick save
git add -A && git commit -m "Update specs"

# Daily checkpoint  
git commit -am "Specs for $(date +%Y-%m-%d)"

# Mark milestones
git tag milestone-1
```

## LLM Integration for Solo Work

### Quick Processing
```markdown
"Here's my MSL spec: [paste]. Please:
1. Add REQ IDs if missing
2. Identify any contradictions  
3. Suggest missing requirements"
```

### Spec Generation
```markdown
"Convert these notes to MSL format:
- Need user login
- Must be secure
- Fast response time"
```

### Inheritance Resolution
```markdown
"I have base.md with [requirements].
I have feature.md that extends base.
Show me the complete resolved requirements."
```

---

# Tooling Roadmap

## Phase 1: CLI Tools (Current)

### msl-lint
```bash
#!/usr/bin/env python3
"""Minimal MSL linter"""
import re
import sys
from pathlib import Path

def lint(file_path):
    content = Path(file_path).read_text()
    issues = []
    
    # Check for requirements section
    if '## Requirements' not in content:
        issues.append("Missing ## Requirements section")
    
    # Check for duplicate IDs
    ids = re.findall(r'REQ-\d+', content)
    if len(ids) != len(set(ids)):
        issues.append("Duplicate requirement IDs")
    
    return issues

for file in sys.argv[1:]:
    issues = lint(file)
    if issues:
        print(f"{file}:")
        for issue in issues:
            print(f"  - {issue}")
```

### msl-render
```bash
#!/usr/bin/env python3
"""Render MSL with Jinja2 template processing"""
import yaml
import jinja2
from pathlib import Path

def render(file_path):
    content = Path(file_path).read_text()
    
    # Extract frontmatter if present
    meta = {}
    if content.startswith('---'):
        _, fm, content = content.split('---', 2)
        meta = yaml.safe_load(fm) or {}
    
    # Process with Jinja2
    template = jinja2.Template(content)
    return template.render(**meta.get('variables', {}))

print(render(sys.argv[1]))
```

## Phase 2: Editor Integration (Q1 2025)

### VS Code Extension
- Syntax highlighting for MSL markers
- Go to definition for `extends:`
- Autocomplete for requirement IDs
- Inline validation

### Obsidian Plugin
- Render inheritance inline
- Graph view of spec relationships
- Dataview integration for queries
- Quick markers palette

## Phase 3: Web UI (Q2 2025)

### MSL Studio (Electron App)
- Visual inheritance tree
- Drag-drop requirement organization
- Git integration UI
- Export to various formats

### Features
- Split view: source/rendered
- Requirement dependency graph
- Change impact analysis
- Template library

## Phase 4: Collaboration Features (Q3 2025)

### For Small Teams
- Merge conflict resolution UI
- Comment threads on requirements
- Simple approval workflow
- Notification on inheritance changes

---

# Appendices

## Appendix A: Complete Grammar

### Frontmatter (All Optional)

```yaml
---
spec: v1                    # Version (default: v1)
id: string                  # Identifier (default: filename)
type: requirement|template  # Type (default: requirement)
extends: parent-id          # Parent spec (default: none)
tags: [tag1, tag2]         # Categories (default: [])
priority: critical|high|medium|low  # (default: from markers or medium)
status: draft|active|complete|deprecated  # (default: draft)
variables:                  # For template substitution
  key: value
---
```

### Content Sections

```markdown
# Title (Required)

## Summary (Optional)
Brief description.

## Requirements (Required for Level 1+)
- Requirement text
- REQ-XXX: Requirement with ID

## Notes (Optional)
Additional context.
```

### Inline Markers

```markdown
[!] Critical
[?] Uncertain
[x] Complete
[ ] Pending
[@user] Assigned
[#tag] Tagged
[OVERRIDE] or Modified:
[NEW] or New:
[INHERIT] or (default)
```

## Appendix B: Migration Paths

### From Todo Lists
```markdown
Before:
- [ ] Add login
- [ ] Add logout
- [x] Setup database

After:
# Auth System
## Requirements
- [ ] Add login
- [ ] Add logout  
- [x] Setup database
```

### From User Stories
```markdown
Before:
As a user, I want to log in
so that I can access my account

After:
# User Authentication
## Requirements
- Users can log in to access their account
```

### From Existing Specs
Add MSL markers gradually:
1. Add `## Requirements` heading
2. Add frontmatter with ID
3. Add REQ- prefixes
4. Extract common parts to base specs

## Appendix C: Examples

### Minimal Personal Spec
```markdown
# Weekend Project

## Requirements
- [!] Fix login bug
- Add dark mode
- [ ] Write tests
```

### Template with Variables
```markdown
---
id: api-template
variables:
  service_name: UserService
  rate_limit: 100
---

# ${service_name} API

## Requirements
- REQ-001: Rate limit ${rate_limit} req/min
- REQ-002: JSON responses only
```

### Inherited Spec
```markdown
---
extends: api-template
variables:
  service_name: PaymentService
  rate_limit: 30
---

# ${service_name} API

## Requirements
- REQ-001: [INHERIT] Rate limit ${rate_limit} req/min
- REQ-002: [INHERIT] JSON responses only
- REQ-003: [NEW] PCI compliance required
```

---

*MSL v1.1 - Optimized for solo practitioners*  
*Extensions and complexity available when needed*