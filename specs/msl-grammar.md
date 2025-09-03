---
id: msl-grammar
tags: [grammar, syntax, validation, formalization]
priority: critical
status: active
assignee: msl-core-team
references:
  - msl-language: "Complete MSL language definition"
  - msl-l0-foundation: "Level 0 syntax rules"
  - msl-l1-structure: "Level 1 syntax rules"  
  - msl-l2-advanced: "Level 2 syntax rules"
---

# MSL Grammar Specification

## Summary

This specification provides the formal grammar definition for Markdown Specification Language (MSL). It describes the syntax rules, validation patterns, and structural constraints for the MSL language defined in `msl-language.md` and its constituent levels.

This grammar specification serves as the authoritative reference for MSL syntax implementation and enables consistent behavior across different MSL processors and platforms.

**Note:** This specification DESCRIBES the MSL language syntax rather than extending it. It references the MSL language definition to provide formal grammar rules.

## Requirements

### Document Structure Grammar

- REQ-001: [!] MSL documents must conform to MSLDocument production rule
- REQ-002: [!] `MSLDocument ::= [Frontmatter] Content`
- REQ-003: [!] `Frontmatter ::= "---" NEWLINE YAMLContent "---" NEWLINE`
- REQ-004: [!] `Content ::= Title [Summary] Requirements [Notes] [CustomSections]`
- REQ-005: Frontmatter block is optional and when absent creates Level 0 document
- REQ-006: Content must always include Title and Requirements sections at minimum

### Frontmatter Grammar

- REQ-101: [!] YAML frontmatter must conform to YAML 1.2 specification
- REQ-102: Frontmatter must begin with exactly three dashes on separate line
- REQ-103: Frontmatter must end with exactly three dashes on separate line
- REQ-104: Empty lines before or after frontmatter delimiters are permitted
- REQ-105: [#validation] Malformed YAML must cause fallback to Level 0 processing

### Frontmatter Fields Grammar

- REQ-201: `id` field must match pattern `^[a-z0-9][a-z0-9-]*[a-z0-9]$|^[a-z0-9]$`
- REQ-202: `extends` field must reference valid MSL document identifier
- REQ-203: `tags` field must be array of strings matching tag name pattern
- REQ-204: `priority` field must be one of: critical, high, medium, low
- REQ-205: `status` field must be one of: draft, active, complete, deprecated, uncertain, pending
- REQ-206: `type` field must be one of: requirement, template
- REQ-207: [#templates] `variables` field must be object with string keys
- REQ-208: Custom fields are permitted but must follow YAML syntax rules

### Title Grammar

- REQ-301: [!] `Title ::= "#" SPACE Text NEWLINE`
- REQ-302: [!] Title must be exactly heading level 1 (single hash)
- REQ-303: [!] Title must be followed by exactly one space before text
- REQ-304: Title text may contain markdown inline formatting
- REQ-305: [#templates] Title text may contain variable references `${variable_name}`

### Requirements Section Grammar

- REQ-401: [!] `Requirements ::= "##" SPACE "Requirements" NEWLINE RequirementList`
- REQ-402: [!] Requirements heading must be exactly level 2 (double hash)
- REQ-403: [!] Requirements heading text must be exactly "Requirements"
- REQ-404: [!] `RequirementList ::= (RequirementItem NEWLINE)*`
- REQ-405: Requirements section must contain at least one requirement item

### Requirement Item Grammar

- REQ-501: [!] `RequirementItem ::= "-" SPACE [Markers] [ID] [Inheritance] Text`
- REQ-502: [!] Requirement items must begin with dash and single space
- REQ-503: All components after dash-space are optional but order is significant
- REQ-504: [#markers] `Markers ::= ("[" MarkerChar "]" SPACE)*`
- REQ-505: [#ids] `ID ::= "REQ-" [0-9]+ ":" SPACE`
- REQ-506: [#inheritance] `Inheritance ::= ("[" InheritanceType "]" SPACE) | (InheritanceKeyword ":" SPACE)`

### Marker Grammar

- REQ-601: [!] `MarkerChar ::= "!" | "?" | "x" | " " | ("@" Username) | ("#" TagName)`
- REQ-602: Priority markers: `[!]` critical, `[?]` uncertain  
- REQ-603: Status markers: `[x]` complete, `[ ]` pending
- REQ-604: [#assignment] Assignment markers: `[@username]` where username matches `[a-z0-9][a-z0-9-]*`
- REQ-605: [#tagging] Tag markers: `[#tagname]` where tagname matches `[a-z0-9][a-z0-9-]*`
- REQ-606: Multiple markers permitted but each type at most once per requirement
- REQ-607: Markers must be followed by single space before next component

### Inheritance Grammar

- REQ-701: [!] `InheritanceType ::= "OVERRIDE" | "NEW" | "INHERIT"`
- REQ-702: [!] `InheritanceKeyword ::= "Modified" | "New"`
- REQ-703: Inheritance markers valid only in documents with `extends` frontmatter field
- REQ-704: [#validation] OVERRIDE requires matching REQ-ID in parent document
- REQ-705: [#validation] NEW requires REQ-ID not present in parent document
- REQ-706: [#validation] INHERIT requires matching REQ-ID in parent document

### Variable Reference Grammar

- REQ-801: [#templates] `VariableRef ::= "${" VariableName "}"`
- REQ-802: [#templates] `VariableName ::= [a-zA-Z][a-zA-Z0-9_]*`
- REQ-803: [#templates] Variable references may appear in title, requirement text, and content
- REQ-804: [#validation] All variable references must resolve to defined variables
- REQ-805: [#templates] Undefined variables must cause processing error

### Optional Section Grammar

- REQ-901: `Summary ::= "##" SPACE "Summary" NEWLINE ParagraphText`
- REQ-902: `Notes ::= "##" SPACE "Notes" NEWLINE ParagraphText`  
- REQ-903: `CustomSection ::= "##" SPACE SectionName NEWLINE Content`
- REQ-904: Custom sections may use any level 2+ heading not conflicting with reserved names
- REQ-905: Reserved section names: Requirements, Summary, Notes

### File Format Grammar

- REQ-1001: MSL documents must use `.md` or `.msl` file extension
- REQ-1002: Files must be valid UTF-8 encoded text
- REQ-1003: Line endings may be LF (Unix) or CRLF (Windows) 
- REQ-1004: Files must be parseable by CommonMark specification
- REQ-1005: [#compatibility] Files must render in GitHub-flavored markdown

### Validation Rules

- REQ-1101: [!] [@msl-lint] REQ-IDs must be unique within single document
- REQ-1102: [!] [@msl-lint] Document IDs must be unique within specification set
- REQ-1103: [!] [@msl-lint] Circular inheritance chains must be rejected
- REQ-1104: [@msl-lint] Missing parent documents should generate warnings
- REQ-1105: [@msl-lint] Malformed markers should generate warnings
- REQ-1106: [@msl-lint] Inconsistent inheritance markers should generate errors

### Error Handling Grammar

- REQ-1201: [#error-handling] Invalid YAML frontmatter must not prevent Level 0 processing
- REQ-1202: [#error-handling] Unknown frontmatter fields must be preserved but ignored  
- REQ-1203: [#error-handling] Malformed markers must be treated as plain text
- REQ-1204: [#error-handling] Invalid inheritance markers must generate clear error messages
- REQ-1205: [#error-handling] Missing variable definitions must halt template processing

## BNF Grammar Reference

### Complete Formal Grammar

```bnf
<msl-document>    ::= <frontmatter>? <content>
<frontmatter>     ::= "---" <newline> <yaml-content> "---" <newline>
<content>         ::= <title> <sections>*
<title>           ::= "#" <space> <text> <newline>
<sections>        ::= <requirements> | <summary> | <notes> | <custom-section>
<requirements>    ::= "##" <space> "Requirements" <newline> <req-list>
<req-list>        ::= <requirement>*
<requirement>     ::= "-" <space> <req-content> <newline>
<req-content>     ::= <markers>? <req-id>? <inheritance>? <text>
<markers>         ::= ("[" <marker-char> "]" <space>)*
<marker-char>     ::= "!" | "?" | "x" | " " | "@" <username> | "#" <tag>
<req-id>          ::= "REQ-" <digits> ":" <space>
<inheritance>     ::= ("[" <inherit-type> "]" <space>) | (<inherit-word> ":" <space>)
<inherit-type>    ::= "OVERRIDE" | "NEW" | "INHERIT"
<inherit-word>    ::= "Modified" | "New"
<variable-ref>    ::= "${" <variable-name> "}"
<variable-name>   ::= <letter> (<letter> | <digit> | "_")*
```

## Examples

### Grammar-Compliant Document

```markdown
---
id: example-spec
extends: parent-spec
tags: [feature, backend]
priority: high
status: active
---

# Example Specification

## Requirements
- [!] [@alice] REQ-001: [OVERRIDE] Critical requirement with assignment
- [x] [#mvp] REQ-002: [NEW] Completed MVP feature  
- [ ] REQ-003: Pending requirement without markers
```

### Template Grammar Usage

```markdown
---
id: service-template
type: template
variables:
  service_name: DefaultService
---

# ${service_name} Specification

## Requirements
- REQ-001: Service must be named ${service_name}
```

## Notes

This grammar specification provides the formal foundation for MSL syntax validation and processing. All MSL tools must implement this grammar to ensure consistency and interoperability across the MSL ecosystem.

The BNF grammar serves as the normative reference for parser implementation, while the requirements provide implementation guidance and validation rules.