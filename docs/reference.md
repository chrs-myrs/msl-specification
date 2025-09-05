# MSL Language Reference

**Complete technical reference for MSL (Markdown Specification Language). Comprehensive documentation of syntax, semantics, and validation rules.**

## Quick Navigation

- [Syntax Elements](#syntax-elements)
- [Frontmatter Fields](#frontmatter-fields)
- [Markers](#markers)
- [Inheritance](#inheritance)
- [Templates & Variables](#templates--variables)
- [Validation Rules](#validation-rules)
- [Error Reference](#error-reference)
- [Formal Grammar](#formal-grammar)
- [Glossary](#glossary)
- [Cheat Sheet](#cheat-sheet)

## Syntax Elements

### Document Structure

#### Requirements Section
**Syntax:** `## Requirements`  
**Level:** L0, L1, L2  
**Required:** Yes  

The Requirements section is mandatory for all MSL documents.

**Valid Examples:**
```markdown
## Requirements
- Simple requirement
- REQ-001: ID-based requirement
```

**Invalid Examples:**
```markdown
## requirements     # Wrong case
## Requirement      # Wrong spelling
### Requirements    # Wrong level
```

**See Also:** [Requirement Format](#requirement-format), [Section Headers](#section-headers)

---

### Frontmatter

#### Frontmatter Block
**Syntax:** `---\n{yaml}\n---`  
**Level:** L1, L2  
**Required:** No (L0), Optional (L1, L2)  

YAML metadata at document start.

**Valid Examples:**
```yaml
---
id: my-spec
version: 1.0
---

---
msl: L2
extends: parent-spec
variables:
  key: value
---
```

**Invalid Examples:**
```yaml
--              # Wrong delimiter
id: my-spec     # Missing delimiters
---

---
{json}          # Not YAML
---
```

**See Also:** [Frontmatter Fields](#frontmatter-fields)

---

### Requirement Format

#### Basic Requirement
**Syntax:** `- {requirement text}`  
**Level:** L0, L1, L2  
**Required:** At least one  

Simple bullet-point requirement.

**Valid Examples:**
```markdown
- User can log in
- System sends confirmation email
```

---

#### ID-based Requirement
**Syntax:** `- {REQ-ID}: {requirement text}`  
**Level:** L1, L2  
**Required:** No  

Requirement with tracking identifier.

**Valid Examples:**
```markdown
- REQ-001: User authentication via OAuth
- AUTH-001: Check user credentials
- REQ-001.1: Sub-requirement example
```

**Invalid Examples:**
```markdown
- REQ001: Missing hyphen
- req-001: Wrong case (should be uppercase)
- 001: Missing prefix
```

**See Also:** [ID Patterns](#id-patterns)

---

## Frontmatter Fields

### Core Fields

#### id
**Type:** String  
**Level:** L1, L2  
**Required:** Recommended  
**Pattern:** `^[a-z0-9-]+$`  

Unique identifier for specification.

**Example:**
```yaml
id: user-authentication
```

---

#### version
**Type:** String  
**Level:** L1, L2  
**Required:** Optional  
**Pattern:** Semantic versioning recommended  

Specification version number.

**Example:**
```yaml
version: 2.1.0
```

---

#### msl
**Type:** String  
**Level:** L1, L2  
**Required:** Optional  
**Values:** `L0`, `L1`, `L2`  

Explicit MSL level declaration.

**Example:**
```yaml
msl: L2
```

---

#### extends
**Type:** String  
**Level:** L2 only  
**Required:** No  
**Pattern:** Parent specification ID  

Inheritance from parent specification.

**Example:**
```yaml
extends: base-api
```

**Validation Rules:**
- Parent must exist
- Must be true "IS-A" relationship
- Maximum 3 levels deep
- No circular references

**See Also:** [Inheritance](#inheritance)

---

#### variables
**Type:** Object  
**Level:** L2  
**Required:** No  

Key-value pairs for template substitution.

**Example:**
```yaml
variables:
  service_name: "User Service"
  port: 8080
  timeout: 30
```

**See Also:** [Templates & Variables](#templates--variables)

---

#### tags
**Type:** Array[String]  
**Level:** L1, L2  
**Required:** Optional  

Categorization tags.

**Example:**
```yaml
tags: [api, security, authentication]
```

---

#### assignee
**Type:** String  
**Level:** L1, L2  
**Required:** Optional  

Team or person responsible.

**Example:**
```yaml
assignee: platform-team
```

---

#### priority
**Type:** String  
**Level:** L1, L2  
**Required:** Optional  
**Values:** `low`, `medium`, `high`, `critical`  

Specification priority level.

**Example:**
```yaml
priority: high
```

---

#### status
**Type:** String  
**Level:** L1, L2  
**Required:** Optional  
**Values:** `draft`, `review`, `active`, `deprecated`  

Specification lifecycle state.

**Example:**
```yaml
status: active
```

---

#### references
**Type:** Object or Array  
**Level:** L1, L2  
**Required:** Optional  

Related specifications or documents.

**Example:**
```yaml
references:
  - api-guidelines: "REST API standards"
  - security-policy: "Security requirements"
```

---

## Markers

### Priority Markers

#### High Priority
**Syntax:** `[!]`  
**Level:** L0, L1, L2  
**Position:** After requirement ID, before text  

Indicates critical requirement.

**Example:**
```markdown
- REQ-001: [!] Must encrypt all data
- [!] Critical security requirement
```

---

#### Blocker Priority
**Syntax:** `[!!]`  
**Level:** L0, L1, L2  
**Position:** After requirement ID, before text  

Indicates blocking requirement.

**Example:**
```markdown
- REQ-001: [!!] Launch blocker
```

---

#### Optional Priority
**Syntax:** `[?]`  
**Level:** L0, L1, L2  
**Position:** After requirement ID, before text  

Indicates nice-to-have requirement.

**Example:**
```markdown
- REQ-001: [?] Optional enhancement
```

---

### Assignment Markers

#### Assignment
**Syntax:** `[@{assignee}]`  
**Level:** L0, L1, L2  
**Position:** Anywhere in requirement  

Assigns requirement to team/person.

**Example:**
```markdown
- REQ-001: [@backend] Implement API endpoint
- [@frontend] [@qa] Create UI tests
```

---

### Status Markers

#### Complete
**Syntax:** `[✓]` or `[DONE]`  
**Level:** L0, L1, L2  
**Position:** Anywhere in requirement  

Marks requirement as completed.

**Example:**
```markdown
- REQ-001: [✓] Implemented feature
```

---

#### In Progress
**Syntax:** `[⚠]` or `[WIP]`  
**Level:** L0, L1, L2  
**Position:** Anywhere in requirement  

Marks requirement as in progress.

---

#### Blocked
**Syntax:** `[✗]` or `[BLOCKED]`  
**Level:** L0, L1, L2  
**Position:** Anywhere in requirement  

Marks requirement as blocked.

---

#### Deferred
**Syntax:** `[→]` or `[DEFERRED]`  
**Level:** L0, L1, L2  
**Position:** Anywhere in requirement  

Marks requirement as deferred.

---

### Tag Markers

#### Hashtag
**Syntax:** `[#{tag}]`  
**Level:** L0, L1, L2  
**Position:** Anywhere in requirement  

Categorization tag.

**Example:**
```markdown
- REQ-001: [#security] [#critical] Encrypt passwords
```

---

### Inheritance Markers

#### Override
**Syntax:** `[OVERRIDE]` or `[override]`  
**Level:** L2 only  
**Position:** After requirement ID  

Replaces parent requirement.

**Example:**
```markdown
- REQ-001: [OVERRIDE] New implementation replacing parent
```

---

#### New
**Syntax:** `[NEW]` or `[new]`  
**Level:** L2 only  
**Position:** After requirement ID  

Adds requirement not in parent.

**Example:**
```markdown
- REQ-100: [NEW] Additional feature
```

---

#### Deprecated
**Syntax:** `[DEPRECATED]`  
**Level:** L0, L1, L2  
**Position:** After requirement ID  

Marks requirement for removal.

---

#### Removed
**Syntax:** `[REMOVED]`  
**Level:** L2  
**Position:** After requirement ID  

Removes parent requirement.

---

## Inheritance

### Basic Inheritance

**Syntax:**
```yaml
---
extends: parent-specification-id
---
```

**Rules:**
1. Child IS-A specialized parent
2. Child inherits all parent requirements
3. Child can override specific requirements
4. Child can add new requirements
5. Maximum 3 levels deep (practical limit: beyond 2-3 levels, abstraction becomes philosophy rather than engineering)

**Valid Example:**
```yaml
---
id: premium-user
extends: basic-user
---
## Requirements
- REQ-001: [OVERRIDE] Unlimited storage
- REQ-100: [NEW] Priority support
```

**Invalid Example:**
```yaml
---
id: user-documentation
extends: api-spec  # WRONG: Docs aren't a type of API
---
```

### Override Semantics

When child overrides parent requirement:
1. Must use same REQ-ID
2. Must include [OVERRIDE] marker
3. Completely replaces parent requirement
4. No merge of properties

**Example:**
```markdown
# Parent: basic-plan.md
- REQ-001: 10GB storage limit

# Child: pro-plan.md
- REQ-001: [OVERRIDE] 100GB storage limit
```

### Inheritance Chain Resolution

Requirements resolved in order:
1. Start with base (no extends)
2. Apply each child's overrides
3. Add each child's new requirements
4. Final result is merged set

**Example Chain:**
```
base.md
  └── intermediate.md (extends: base)
      └── final.md (extends: intermediate)
```

---

## Templates & Variables

### Template Definition

**Syntax:**
```yaml
---
type: template
variables:
  var_name: default_value
---
```

Templates use `{{variable}}` syntax for substitution.

**Example Template:**
```markdown
---
id: service-template
type: template
variables:
  service_name: "Service"
  port: 8080
---
# {{service_name}}

## Requirements
- REQ-001: Service runs on port {{port}}
```

### Variable Substitution

**Syntax:** `{{variable_name}}`  
**Level:** L2  
**Context:** Template content  

Variables replaced with values from frontmatter.

**Example Usage:**
```markdown
---
extends: service-template
variables:
  service_name: "User API"
  port: 8081
---
```

### Variable Scoping

1. Local variables override inherited
2. Undefined variables remain as `{{var}}`
3. No nested variable expansion
4. Case-sensitive names

---

## Validation Rules

### Document Validation

#### V-001: Requirements Section Required
**Level:** L0, L1, L2  
**Error:** "No Requirements section found"  
**Fix:** Add `## Requirements` section  

#### V-002: Valid YAML Frontmatter
**Level:** L1, L2  
**Error:** "Invalid YAML in frontmatter"  
**Fix:** Correct YAML syntax  

#### V-003: No Circular Inheritance
**Level:** L2  
**Error:** "Circular inheritance detected"  
**Fix:** Remove circular reference  

### Requirement Validation

#### V-101: Unique Requirement IDs
**Level:** L1, L2  
**Error:** "Duplicate requirement ID: {id}"  
**Fix:** Use unique IDs  

#### V-102: Valid ID Format
**Level:** L1, L2  
**Error:** "Invalid requirement ID format"  
**Fix:** Use pattern like REQ-001  

#### V-103: Testable Requirements
**Level:** L0, L1, L2  
**Warning:** "Requirement not testable"  
**Fix:** Add measurable criteria  

### Quality Validation

#### V-201: DRY Compliance
**Level:** L0, L1, L2  
**Warning:** "Duplicate text detected"  
**Fix:** Extract to template  
**Threshold:** ≥85% unique  

#### V-202: Cohesion Score
**Level:** L0, L1, L2  
**Warning:** "Low cohesion score"  
**Fix:** Move unrelated requirements  
**Threshold:** ≥80% related  

#### V-203: Coupling Limit
**Level:** L2  
**Warning:** "Deep inheritance hierarchy"  
**Fix:** Flatten inheritance  
**Threshold:** ≤3 levels  

---

## Error Reference

### Parse Errors

#### E-001: Missing Requirements Section
```
Error: No "## Requirements" section found
File: spec.md
Fix: Add ## Requirements section with at least one requirement
```

#### E-002: Invalid Frontmatter
```
Error: YAML parse error in frontmatter
Line: 3
Issue: Expected key-value pair
Fix: Check YAML syntax, ensure proper indentation
```

#### E-003: Unknown MSL Level
```
Error: Unknown MSL level "L3"
Valid: L0, L1, L2
Fix: Use valid MSL level
```

### Inheritance Errors

#### E-101: Parent Not Found
```
Error: Parent specification "base-spec" not found
File: child-spec.md
Fix: Ensure parent file exists and is accessible
```

#### E-102: Circular Inheritance
```
Error: Circular inheritance detected
Chain: a.md -> b.md -> c.md -> a.md
Fix: Remove circular reference
```

#### E-103: Inheritance Depth Exceeded
```
Error: Inheritance depth exceeds 3 levels
Chain: base -> l1 -> l2 -> l3 -> l4
Fix: Flatten inheritance hierarchy
```

### Validation Errors

#### E-201: Duplicate Requirement ID
```
Error: Duplicate requirement ID "REQ-001"
Lines: 15, 23
Fix: Use unique IDs for each requirement
```

#### E-202: Invalid Requirement Format
```
Error: Invalid requirement format
Line: 18
Expected: "- REQ-XXX: description" or "- description"
Fix: Follow requirement format
```

---

## Formal Grammar

### EBNF Notation

```ebnf
(* MSL Document Grammar *)
document        = [frontmatter], content ;
frontmatter     = "---", newline, yaml_content, newline, "---" ;
content         = {section} ;
section         = header, section_content ;
header          = "#", {#}, " ", text, newline ;
section_content = {paragraph | requirement_list} ;

(* Requirements *)
requirement_list = requirement, {requirement} ;
requirement      = "-", " ", [req_id, ":", " "], 
                   {marker}, " ", req_text, newline ;
req_id          = letter, {letter | digit | "-"}, "-", 
                  digit, {digit} ;
marker          = "[", marker_content, "]" ;
marker_content  = "!" | "!!" | "?" | "@", text | 
                  "#", text | "✓" | "⚠" | "✗" | "→" |
                  "OVERRIDE" | "NEW" | "DEPRECATED" ;

(* Text Elements *)
text            = {character} ;
req_text        = {character - newline} ;
yaml_content    = (* Valid YAML *) ;
paragraph       = text, newline, [newline] ;

(* Lexical Elements *)
letter          = "A".."Z" | "a".."z" ;
digit           = "0".."9" ;
character       = (* Any Unicode character *) ;
newline         = "\n" | "\r\n" ;
```

### Validation Rules in BNF

```bnf
<valid-msl-doc> ::= <has-requirements> <valid-structure> 
                    [<valid-frontmatter>] [<valid-inheritance>]

<has-requirements> ::= <document-with-requirements-section>

<valid-structure> ::= <markdown-document> <requirements-section>

<valid-frontmatter> ::= <yaml-block> <known-fields>

<valid-inheritance> ::= <extends-field> <parent-exists> 
                       <no-circular-ref> <max-depth-3>
```

---

## Glossary

### A-F

**Atomic Requirement**: Single, indivisible, testable behavior specification

**Cohesion**: Measure of how related requirements are within a specification

**Coupling**: Dependencies between different specifications

**DRY (Don't Repeat Yourself)**: Principle of avoiding duplication

**Extension**: Adding new requirements through inheritance

**Frontmatter**: YAML metadata block at document beginning

### G-L

**Inheritance**: Deriving specification from parent with overrides/additions

**Level**: MSL complexity tier (L0=basic, L1=structured, L2=advanced)

**Marker**: Special notation for metadata (e.g., `[!]`, `[@user]`)

### M-R

**Override**: Replacing parent requirement with new definition

**Priority Marker**: Notation indicating requirement importance

**Requirement**: Testable statement of system behavior

### S-Z

**Template**: Reusable specification with variable placeholders

**Testability**: Whether requirement has clear pass/fail criteria

**Validation**: Checking specification quality and correctness

**Variable**: Placeholder in template replaced with actual value

---

## Cheat Sheet

### Quick Syntax Reference

```markdown
# MSL Document Structure
---
id: spec-name           # L1+ frontmatter
version: 1.0
extends: parent         # L2 inheritance
variables:              # L2 templates
  key: value
---

# Document Title

## Summary (optional)
Brief description.

## Requirements (required)
- Simple requirement                          # L0
- REQ-001: ID-based requirement              # L1+
- REQ-002: [!] High priority                 # Priority
- REQ-003: [@team] Assigned                  # Assignment
- REQ-004: [#tag] Tagged                     # Category
- REQ-005: [✓] Complete                      # Status
- REQ-001: [OVERRIDE] Replace parent         # L2
- REQ-100: [NEW] Additional                  # L2
```

### Common Patterns

```markdown
# API Endpoint
- REQ-001: GET /resource returns 200 with JSON

# Performance
- REQ-002: Response within 500ms for 95th percentile

# Security
- REQ-003: Authenticate with JWT Bearer token

# Validation
- REQ-004: Email format matches RFC 5322

# Error Handling
- REQ-005: Invalid input returns 400 with message
```

### Validation Commands

```bash
# Basic validation
msl-validate spec.md

# Recursive directory
msl-validate ./specs/ --recursive

# Quality threshold
msl-validate spec.md --min-score 80

# Specific checks
msl-validate spec.md --rules dry,testability

# Fix issues
msl-validate spec.md --fix
```

### File Naming

```
feature-name.md         # Features
service-api.md          # APIs
table-schema.md         # Database
component-ui.md         # UI components
config-prod.md          # Configuration
template-base.md        # Templates
spec-v2.md             # Versions
```

---

**Need help?** See [User Guide](user-guide.md) for tutorials or [Getting Started](getting-started.md) for quick introduction.

For tools and automation, check [Tools Documentation](tools.md).