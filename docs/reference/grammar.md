# MSL Grammar Reference

## Complete Grammar Definition

### Document Structure

```
MSLDocument ::= [Frontmatter] Content

Frontmatter ::= "---" NEWLINE 
                YAMLContent 
                "---" NEWLINE

Content ::= Title [Summary] Requirements [Notes] [CustomSections]
```

### Frontmatter Fields

```yaml
spec: v1 | v1.1                    # Specification version
id: string                         # Unique identifier
type: requirement | template       # Document type
extends: parent-id                 # Parent specification
tags: [string, ...]               # Categorization tags
priority: critical | high | medium | low
status: draft | active | complete | deprecated | uncertain | pending
assignee: string                   # Owner/assignee
variables:                        # Template variables
  key: value
```

### Content Sections

```
Title ::= "#" SPACE Text NEWLINE

Summary ::= "##" SPACE "Summary" NEWLINE 
           ParagraphText

Requirements ::= "##" SPACE "Requirements" NEWLINE
                RequirementList

RequirementList ::= (RequirementItem NEWLINE)*

RequirementItem ::= "-" SPACE [Marker] [ID ":"] [Inheritance] Text

Notes ::= "##" SPACE "Notes" NEWLINE
         ParagraphText
```

### Requirement Components

```
ID ::= "REQ-" Number+

Marker ::= "[" MarkerChar "]"
MarkerChar ::= "!" | "?" | "x" | " " | "@" Username | "#" Tag

Inheritance ::= "[OVERRIDE]" | "[NEW]" | "[INHERIT]" |
               "Modified:" | "New:"

Text ::= Any markdown-formatted text
```

## Syntax Elements

### Markers

| Marker | Meaning | Example |
|--------|---------|---------|
| `[!]` | Critical/High priority | `- [!] Must encrypt data` |
| `[?]` | Uncertain/needs clarification | `- [?] Support OAuth?` |
| `[x]` | Completed | `- [x] User login implemented` |
| `[ ]` | Pending/not started | `- [ ] Add password reset` |
| `[@user]` | Assigned to user | `- [@alice] Review security` |
| `[#tag]` | Tagged with label | `- [#mvp] Core feature` |

### Inheritance Markers

| Marker | Usage | Description |
|--------|-------|-------------|
| `[OVERRIDE]` | Replace parent requirement | Full replacement |
| `[NEW]` | Add new requirement | Not in parent |
| `[INHERIT]` | Explicitly inherit | Keep parent version |
| `Modified:` | Alternative to OVERRIDE | More readable |
| `New:` | Alternative to NEW | More readable |

## Level-Based Grammar

### Level 0: Pure Markdown
```markdown
# Any Title
Any content with a section called:
## Requirements
- List items
```

### Level 1: Basic Structure
```markdown
---
id: identifier
---
# Title
## Requirements
- REQ-001: Requirement text
- REQ-002: Another requirement
```

### Level 2: Full Features
```markdown
---
spec: v1
id: identifier
extends: parent-id
tags: [tag1, tag2]
priority: high
status: draft
variables:
  name: value
---
# ${name} Title
## Requirements
- REQ-001: [OVERRIDE] Modified requirement
- REQ-002: [NEW] Additional requirement
```

## YAML Frontmatter Schema

```yaml
$schema: http://json-schema.org/draft-07/schema#
type: object
properties:
  spec:
    type: string
    enum: [v1, v1.1]
    default: v1
  id:
    type: string
    pattern: ^[a-z0-9-]+$
  type:
    type: string
    enum: [requirement, template]
    default: requirement
  extends:
    type: string
  tags:
    type: array
    items:
      type: string
  priority:
    type: string
    enum: [critical, high, medium, low]
  status:
    type: string
    enum: [draft, active, complete, deprecated, uncertain, pending]
  assignee:
    type: string
  variables:
    type: object
    additionalProperties: true
```

## File Naming Conventions

```
filename.md           # Standard MSL file
filename.msl          # Alternative extension
template-name.md      # Template file
spec-id.md           # ID-based naming
YYYY-MM-DD.md        # Date-based naming
prefix-name.md       # Prefixed naming
```

## Special Patterns

### Comment-Style Extends
```markdown
<!-- extends: parent-spec -->

# Specification
```

### Inline Variable Substitution
```markdown
${variable_name}      # Jinja2 style
$variable_name       # Simple style
```

### Nested Requirements
```markdown
- REQ-001: High-level requirement
  - Sub-requirement one
  - Sub-requirement two
  - Edge case handling
```

## Escaping

### Special Characters
- Use `\[` to show literal square bracket
- Use `\#` to show literal hash at line start
- Use `\-` to show literal dash at line start

### Code Blocks
````markdown
```
Code blocks are ignored by MSL parser
- This is not a requirement
```
````

## Reserved Keywords

These words have special meaning in MSL:

- Document sections: `Requirements`, `Summary`, `Notes`
- Inheritance: `OVERRIDE`, `NEW`, `INHERIT`, `Modified`, `New`
- Frontmatter: `spec`, `id`, `extends`, `tags`, `priority`, `status`

## Extension Points

MSL allows custom sections and fields:

### Custom Sections
```markdown
## Testing Strategy
Custom content here

## Acceptance Criteria
Custom content here
```

### Custom Frontmatter
```yaml
---
id: my-spec
custom_field: value
organization_specific: data
---
```

## Grammar Validation Rules

1. **ID Uniqueness**: REQ-XXX IDs must be unique within a file
2. **ID Format**: IDs should follow REQ-NNN pattern (configurable)
3. **Inheritance Consistency**: Child specs can't override non-existent parent requirements
4. **Marker Validity**: Only one marker type per requirement
5. **Variable Closure**: All ${variables} must be defined

## BNF Grammar

For formal parsing:

```bnf
<msl-document> ::= <frontmatter>? <content>
<frontmatter>  ::= "---" <newline> <yaml> "---" <newline>
<content>      ::= <title> <sections>*
<title>        ::= "#" <space> <text> <newline>
<sections>     ::= <requirements> | <summary> | <notes> | <custom>
<requirements> ::= "##" <space> "Requirements" <newline> <req-list>
<req-list>     ::= <requirement>*
<requirement>  ::= "-" <space> <req-content> <newline>
<req-content>  ::= <marker>? <req-id>? <inheritance>? <text>
<marker>       ::= "[" <marker-char> "]" <space>
<marker-char>  ::= "!" | "?" | "x" | " " | "@" <username> | "#" <tag>
<req-id>       ::= "REQ-" <number>+ ":" <space>
<inheritance>  ::= "[" <inherit-type> "]" <space>
<inherit-type> ::= "OVERRIDE" | "NEW" | "INHERIT"
```

## Examples

### Minimal Valid MSL
```markdown
# X
## Requirements
- Y
```

### Complete MSL
```markdown
---
spec: v1.1
id: complete-example
type: requirement
extends: base-template
tags: [example, complete]
priority: high
status: active
assignee: alice
variables:
  service: UserAPI
  timeout: 30
---

# ${service} Specification

## Summary
Complete example showing all MSL features.

## Requirements
- REQ-001: [!] Critical requirement
- REQ-002: [OVERRIDE] Modified from parent
- REQ-003: [NEW] Added requirement
- REQ-004: [@alice] Assigned requirement
- REQ-005: [#mvp] Tagged requirement
- REQ-006: [x] Completed requirement
- REQ-007: [?] Uncertain requirement
- REQ-008: [ ] Pending requirement

## Notes
Additional context and documentation.