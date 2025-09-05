---
msl: L2
id: msl-l2-advanced
extends: msl-l1-structure
governed-by: [msl-core-metaspec, msl-language-metaspec]
tags: [specification, level-2, advanced, complete]
priority: high
status: active
---

# MSL Level 2: Complete Language with Formal Specification [MSL]

## Summary

MSL Level 2 is the **complete MSL language specification**. It extends Level 1 with advanced features (markers, templates, sophisticated inheritance) AND provides the formal grammar and semantics needed for tool implementation.

This is where **automation begins**. While L0 and L1 are designed for humans, L2 provides the precision needed for parsers, validators, and processing tools.

## Requirements

### Level 1 Inheritance

- REQ-001: [INHERIT] All MSL Level 1 structured specification requirements
- REQ-002: [INHERIT] YAML frontmatter and document identification features
- REQ-003: [INHERIT] Basic inheritance and processing requirements

### Quick Markers

- REQ-101: [!] Requirements may include quick markers in square brackets at line start
- REQ-102: [!] Priority markers must use exclamation `[!]` for critical/high priority
- REQ-103: Status markers must support completion `[x]`, pending `[ ]`, uncertain `[?]`
- REQ-104: Assignment markers must use at-symbol format `[@username]` for assignee
- REQ-105: Tag markers must use hash format `[#tagname]` for categorization
- REQ-106: Multiple markers may be combined on single requirement line
- REQ-106a: Marker combination order does not affect semantic processing
- REQ-106b: Conflicting markers (e.g., `[!]` and `[?]`) must generate processor warnings
- REQ-107: Markers must be placed before requirement text and REQ-ID when present
- REQ-107a: When markers conflict, inline markers override frontmatter defaults

### Composite Markers (v1.4.0+)

- REQ-108: [NEW] Requirements may use composite markers with pipe-separated components `[component1|component2|key:value]`
- REQ-109: [NEW] Composite markers support key:value pairs for metrics like `progress:60%` and `coverage:85%`
- REQ-110: [NEW] Composite markers enable rich metadata including stages, dependencies, and gaps
- REQ-111: [NEW] Processors must validate composite marker consistency and value ranges

### Hierarchical Requirements (v1.4.0+)

- REQ-112: [NEW] Requirements may be organized hierarchically using indentation (2 spaces per level)
- REQ-113: [NEW] Sub-requirements use dot notation IDs like `REQ-001.1`, `REQ-001.2.3`
- REQ-114: [NEW] Parent-child relationships are preserved in the document structure
- REQ-115: [NEW] Processors must auto-generate hierarchical IDs when omitted
- REQ-116: [NEW] Maximum recommended hierarchy depth is 4 levels
- REQ-117: [NEW] All markers and metadata apply independently at each hierarchy level

### Bidirectional Code Links (v1.5.0+)

- REQ-118: [NEW] System must parse bidirectional code link markers in format `[↔ file:line]` or `[<-> file:line]`
- REQ-119: [NEW] System must support forward-only links with `[→ file:line]` or `[-> file:line]`
- REQ-120: [NEW] System must support backward-only links with `[← file:line]` or `[<- file:line]`
- REQ-121: [NEW] Code links must support single line references (file:45) and ranges (file:45-67)
- REQ-122: [NEW] System must validate file paths in code links when configured
- REQ-123: [NEW] Code scanner must extract MSL references from source code comments
- REQ-124: [NEW] Code scanner must support common programming languages (Python, JS, Java, Go, etc.)

### Advanced Inheritance

- REQ-201: [NEW] Child documents must support explicit inheritance control markers
- REQ-202: [NEW] `[OVERRIDE]` marker replaces parent requirement with new content
- REQ-203: [NEW] `[NEW]` marker indicates requirement not present in parent document
- REQ-204: [NEW] `[INHERIT]` marker explicitly preserves parent requirement unchanged
- REQ-205: [NEW] Alternative syntax "Modified:" and "New:" provide readable inheritance
- REQ-206: Requirements without inheritance markers automatically inherit parent requirement content when REQ-IDs match
- REQ-207: Child requirements with new REQ-IDs are implicitly `[NEW]` requirements
- REQ-208: Inheritance markers are only valid in documents with `extends` field in frontmatter

### Template System

- REQ-301: Documents may specify `type: template` in frontmatter for reusable patterns
- REQ-302: Templates must define variables section in frontmatter for substitution
- REQ-303: Variable substitution uses `${variable_name}` syntax in content
- REQ-304: Child documents may override template variables in their frontmatter
- REQ-305: Templates enable creation of specification families with consistent structure
- REQ-306: Template inheritance combines with variable substitution for powerful patterns

### Enhanced Metadata

- REQ-401: [OVERRIDE] Frontmatter supports comprehensive priority levels: critical, high, medium, low
- REQ-402: [NEW] Frontmatter supports detailed status tracking: draft, active, complete, deprecated, uncertain, pending
- REQ-403: [NEW] Frontmatter may include assignee field for ownership tracking
- REQ-404: [NEW] Frontmatter supports variables section for template functionality
- REQ-405: [NEW] Custom frontmatter fields enable organization-specific metadata
- REQ-406: Metadata in frontmatter provides defaults that markers can override per-requirement

### Marker Processing

- REQ-501: [!] MSL processors must parse and interpret quick markers correctly
- REQ-502: [!] Priority markers must affect requirement priority metadata
- REQ-503: Status markers must affect requirement completion tracking
- REQ-504: Assignment markers must enable requirement ownership queries
- REQ-505: Tag markers must enable requirement categorization and filtering
- REQ-506: Marker conflicts between frontmatter and inline markers must favor inline

### Advanced Validation

- REQ-601: [NEW] Processors must validate inheritance marker consistency
- REQ-602: [NEW] Override markers require existence of parent requirement with same ID
- REQ-603: [NEW] New markers must not conflict with existing parent requirement IDs
- REQ-604: [NEW] Variable references must resolve to defined variables
- REQ-605: [NEW] Template validation must ensure all variables are either defined in frontmatter OR have defaults in parent templates
- REQ-606: [NEW] Circular template inheritance must be detected and rejected
- REQ-607: [NEW] Variable scope follows inheritance chain - child variables override parent variables

### Processing Capabilities

- REQ-701: [@msl-tools] Level 2 processors must support template rendering
- REQ-702: [@msl-tools] Processors must resolve inheritance hierarchies correctly
- REQ-703: [@msl-tools] Processors must provide requirement querying by markers
- REQ-704: [@msl-tools] Processors must validate marker syntax and combinations
- REQ-705: [@msl-tools] Processors must maintain backward compatibility with Level 0
- REQ-706: [@msl-tools] Processors must maintain backward compatibility with Level 1

### Performance Considerations

- REQ-801: Processors should handle specifications up to 1000 requirements efficiently
- REQ-802: Inheritance chains should be limited to 10 levels maximum for performance
- REQ-803: Template variable substitution should complete in linear time
- REQ-804: Circular dependency detection must complete before processing begins

## Formal Grammar Specification

### BNF Grammar

This section provides the complete formal grammar for MSL using BNF notation. This grammar is normative for tool implementations.

```bnf
<msl-document>    ::= <frontmatter>? <content>
<frontmatter>     ::= "---" <newline> <yaml-content> "---" <newline>
<yaml-content>    ::= <yaml-1.2-compliant-content>
<content>         ::= <title> <sections>*
<title>           ::= "#" <space> <text> <newline>
<sections>        ::= <requirements> | <summary> | <notes> | <custom-section>
<requirements>    ::= "##" <space> "Requirements" <newline> <req-list>
<req-list>        ::= <requirement>+
<requirement>     ::= "-" <space> <req-content> <newline>
<req-content>     ::= <markers>? <req-id>? <inheritance>? <text>
<markers>         ::= ("[" <marker-char> "]" <space>)*
<marker-char>     ::= "!" | "?" | "x" | " " | "@" <username> | "#" <tag>
<username>        ::= <letter> (<letter> | <digit> | "-")*
<tag>             ::= <letter> (<letter> | <digit> | "-")*
<req-id>          ::= "REQ-" <digits> ":" <space>
<inheritance>     ::= ("[" <inherit-type> "]" <space>) | (<inherit-word> ":" <space>)
<inherit-type>    ::= "OVERRIDE" | "NEW" | "INHERIT"
<inherit-word>    ::= "Modified" | "New"
<variable-ref>    ::= "${" <variable-name> "}"
<variable-name>   ::= <letter> (<letter> | <digit> | "_")*
<text>            ::= <any-markdown-content>
```

### Syntax Rules

#### Document Structure
- MSL documents must be valid UTF-8 encoded text files
- Files must use `.md` or `.msl` extension
- Line endings may be LF (Unix) or CRLF (Windows)
- Documents must be parseable by CommonMark specification

#### Frontmatter
- YAML frontmatter must conform to YAML 1.2 specification
- Frontmatter delimiters must be exactly three dashes
- Empty frontmatter block is valid: `---\n---`
- Unknown fields must be preserved but may be ignored

#### Identifiers
- Document IDs must match: `^[a-z0-9][a-z0-9-]*[a-z0-9]$|^[a-z0-9]$`
- REQ-IDs must match: `REQ-[0-9]+`
- Usernames must match: `^[a-z0-9][a-z0-9-]*$`
- Tags must match: `^[a-z0-9][a-z0-9-]*$`

#### Requirements Section
- Requirements heading must be exactly "## Requirements"
- Each requirement must start with "- " (dash space)
- Requirements may be nested using additional indentation
- Empty requirements section is invalid

## Semantic Definitions

### Core Semantics

#### Document Identity
- The `id` field creates a unique namespace for requirement references
- Documents without explicit `id` use filename without extension as implicit ID
- Document IDs enable external referencing as `document-id.REQ-XXX`
- Documents with same ID in inheritance chain represent versions of same specification

#### Requirement Identity
- REQ-XXX identifiers create unique addressable requirements within document
- Requirements without explicit IDs cannot be referenced externally
- REQ-IDs enable precise inheritance control between parent and child
- REQ-ID numbering suggests logical grouping but does not enforce ordering

### Inheritance Semantics

#### Basic Inheritance
- `extends` creates parent-child semantic dependency
- Child inherits parent's complete requirement set by default
- Child requirements with matching REQ-IDs replace parent requirements
- Requirements without markers inherit parent when REQ-IDs match

#### Inheritance Markers
- `[INHERIT]` - Preserves parent requirement unchanged
- `[OVERRIDE]` - Explicitly replaces parent requirement
- `[NEW]` - Adds requirement not present in parent
- Alternative syntax "Modified:" and "New:" provide readable forms

#### Inheritance Resolution
1. Process inheritance chain from root parent to final child
2. Build complete requirement set by merging requirements
3. Apply inheritance markers to determine final content
4. Validate consistency and marker compatibility
5. Generate resolved specification with all effective requirements

### Marker Semantics

#### Priority Markers
- `[!]` - Critical priority requiring immediate attention
- `[?]` - Uncertainty requiring clarification
- Inline markers override frontmatter defaults

#### Status Markers
- `[x]` - Requirement complete and implemented
- `[ ]` - Requirement pending implementation
- Status affects requirement lifecycle tracking

#### Assignment Markers
- `[@username]` - Assigns ownership to individual/team
- Creates responsibility relationships
- Enables ownership queries and filtering

#### Tag Markers
- `[#tagname]` - Associates requirement with category
- Common tags: `#mvp`, `#v2`, `#security`, `#performance`
- Enables categorization and filtering

### Template Semantics

#### Template Definition
- `type: template` creates reusable specification pattern
- Templates intended for extension, not direct use
- Variables enable specification family creation

#### Variable Substitution
- `${variable_name}` references replaced with values
- Substitution occurs before semantic processing
- Child documents may override template variables
- Undefined variables create processing errors

#### Template Processing
1. Collect variable definitions from frontmatter
2. Child definitions override parent definitions
3. Replace all variable references with values
4. Variable substitution applies to title, requirements, content
5. Report errors for undefined references

### Processing Order

The correct semantic processing order for MSL documents:

1. **Parse** - Extract frontmatter and content structure
2. **Resolve Templates** - Process variable substitutions
3. **Resolve Inheritance** - Build complete requirement set
4. **Process Markers** - Interpret priority, status, assignment, tags
5. **Validate** - Check consistency and completeness
6. **Generate Output** - Produce final processed specification

### Error Handling

#### Semantic Errors (Halt Processing)
- Missing parent documents
- Undefined template variables
- Invalid inheritance markers
- Circular inheritance chains

#### Semantic Warnings (Continue Processing)
- Duplicate REQ-IDs
- Unknown marker syntax
- Missing recommended fields
- Deprecated constructs

### Compatibility

#### Backward Compatibility
- Level 2 processors must handle Level 0 and Level 1 documents
- Unknown constructs should generate warnings, not errors
- Malformed sections should fall back to lower level processing

#### Forward Compatibility
- Unknown frontmatter fields must be preserved
- New marker types should be treated as text
- Extensions should not break core functionality

## Examples

### Quick Markers Usage

```markdown
## Requirements
- [!] [@alice] [#security] Implement authentication system
- [x] [@bob] [#mvp] Basic user registration complete
- [ ] [#v2] Advanced analytics dashboard
- [?] [#research] Machine learning recommendations
```

### Advanced Inheritance

```markdown
---
id: payment-api
extends: rest-api-base
---

# Payment API

## Requirements
- REQ-001: [INHERIT] Standard REST endpoint design
- REQ-002: [OVERRIDE] Rate limiting: 30 requests per minute for payment ops
- REQ-003: [NEW] PCI DSS compliance required for card processing
```

### Template with Variables

```markdown
---
id: service-template
type: template
variables:
  service_name: GenericService
  max_connections: 100
---

# ${service_name} Configuration

## Requirements
- REQ-001: Maximum ${max_connections} concurrent connections
- REQ-002: Service name must be "${service_name}"
```

### Complete L2 Document

```markdown
---
id: user-service
extends: service-template
tags: [backend, core, authentication]
priority: critical
status: active
assignee: backend-team
variables:
  service_name: UserAuthenticationService
  max_connections: 500
---

# ${service_name}

## Summary
Core authentication service handling user login, session management, and authorization.

## Requirements

### Authentication
- [!] [@security-team] REQ-001: [OVERRIDE] Maximum ${max_connections} concurrent connections
- [!] [#security] REQ-002: [NEW] Implement OAuth2 with PKCE flow
- [x] [#mvp] REQ-003: [NEW] Basic username/password authentication
- [ ] [#v2] REQ-004: [NEW] Multi-factor authentication support

### Session Management
- [!] REQ-005: [NEW] Sessions expire after 30 minutes of inactivity
- [ ] [@alice] REQ-006: [NEW] Implement session refresh tokens
- [?] [#research] REQ-007: [NEW] Distributed session storage

### Authorization
- REQ-008: [NEW] Role-based access control (RBAC)
- REQ-009: [NEW] Permission inheritance through role hierarchy
- [#future] REQ-010: [NEW] Attribute-based access control (ABAC)

## Notes
This service is critical infrastructure and must maintain 99.99% uptime.
```

## Tool Implementation Guide

### For Parser Implementers

1. **Start Simple**: Parse Level 0 first (just markdown with requirements)
2. **Add Structure**: Extend to Level 1 (frontmatter and IDs)  
3. **Full Implementation**: Add Level 2 features using this formal spec
4. **Validate**: Use the BNF grammar and semantic rules
5. **Test**: Ensure backward compatibility with all levels

### Required Capabilities

- YAML parsing for frontmatter
- Markdown parsing (CommonMark compatible)
- Regular expression support for patterns
- Graph traversal for inheritance chains
- Template variable substitution
- Error reporting with line numbers

### Validation Checklist

- [ ] Unique document IDs within specification set
- [ ] Unique REQ-IDs within each document
- [ ] No circular inheritance chains
- [ ] All parent documents exist
- [ ] All template variables defined
- [ ] Valid marker syntax
- [ ] Consistent inheritance markers

## Notes

MSL Level 2 represents the complete MSL language specification. It provides both human-friendly features for specification authors and formal definitions for tool implementers.

The progressive enhancement from L0→L1→L2 ensures that:
- Simple specs stay simple (L0)
- Structure is added when needed (L1)
- Full power is available for complex projects (L2)

This specification enables automated requirement tracking, project management integration, and sophisticated documentation workflows while maintaining the simplicity that makes MSL accessible to everyone.

---
*Specification format: [MSL Level 2](https://github.com/chrs-myrs/msl-specification)*