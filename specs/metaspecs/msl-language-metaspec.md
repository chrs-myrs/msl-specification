---
msl: L2
id: msl-language-metaspec
type: metaspec
version: 1.0.0
tags: [metaspec, language, grammar, semantics]
priority: critical
status: active
---

# MSL Language Definition Metaspec [MSL]

## Summary

This metaspec governs specifications that define language features, syntax, and semantics for MSL. It ensures that language-defining specifications provide complete, unambiguous, and implementable definitions suitable for tool developers and language processors.

Language specifications differ from application specifications - they must provide formal definitions that enable consistent implementation across different tools and platforms.

## Structural Requirements

### Language Definition Sections

- REQ-001: [!] MUST have formal syntax definition section for new constructs
- REQ-002: [!] MUST have semantic definition section explaining meaning and behavior  
- REQ-003: [!] MUST have processing requirements section for tool implementers
- REQ-004: MUST have compatibility section addressing backward/forward compatibility
- REQ-005: SHOULD have validation rules section for conformance checking

### Syntax Specification

- REQ-101: [!] Level 2 and above MUST provide BNF or EBNF grammar
- REQ-102: Syntax patterns MUST use consistent notation across specifications
- REQ-103: New syntax MUST be clearly distinguished from existing syntax
- REQ-104: Regular expressions MUST use PCRE-compatible syntax
- REQ-105: Character encoding MUST be specified (UTF-8 default)

## Semantic Requirements

### Semantic Clarity

- REQ-201: [!] Each language construct MUST have unambiguous semantics
- REQ-202: [!] Semantic definitions MUST specify evaluation order
- REQ-203: Inheritance and override semantics MUST be precisely defined
- REQ-204: Error conditions MUST be explicitly specified
- REQ-205: Edge cases and corner cases MUST be addressed

### Behavioral Specification

- REQ-301: Processing order MUST be explicitly defined
- REQ-302: Side effects MUST be documented if present
- REQ-303: Conflict resolution rules MUST be specified
- REQ-304: Default values and behaviors MUST be stated
- REQ-305: Optional vs mandatory behavior MUST be distinguished

## Grammar Requirements

### BNF/EBNF Standards

- REQ-401: [!] Grammar MUST be complete for all defined constructs
- REQ-402: Grammar MUST use standard BNF or EBNF notation
- REQ-403: Terminal symbols MUST be clearly distinguished from non-terminals
- REQ-404: Grammar MUST be parseable by standard parser generators
- REQ-405: Ambiguous grammar rules MUST be resolved with precedence rules

### Grammar Organization

- REQ-501: Grammar rules MUST be organized from high-level to detailed
- REQ-502: Related rules MUST be grouped together
- REQ-503: Recursive rules MUST have clear termination conditions
- REQ-504: Optional elements MUST use consistent notation

## Implementation Requirements

### Tool Guidance

- REQ-601: [!] MUST provide clear implementation guidance for processors
- REQ-602: MUST specify minimum required capabilities for conformant tools
- REQ-603: MUST define error messages and warning categories
- REQ-604: SHOULD provide reference implementation or pseudocode
- REQ-605: SHOULD include performance considerations

### Validation Requirements

- REQ-701: MUST define what constitutes a valid document at this level
- REQ-702: MUST specify required vs optional validation checks
- REQ-703: MUST define severity levels for validation issues
- REQ-704: MUST provide validation test cases

## Compatibility Requirements

### Version Compatibility

- REQ-801: [!] MUST maintain backward compatibility with lower levels
- REQ-802: [!] MUST document any breaking changes explicitly
- REQ-803: MUST provide migration path for deprecated features
- REQ-804: MUST specify version detection mechanisms
- REQ-805: SHOULD provide forward compatibility considerations

### Cross-Level Interaction

- REQ-901: MUST define how features interact with lower-level features
- REQ-902: MUST specify precedence when features conflict
- REQ-903: MUST define fallback behavior for unsupported features
- REQ-904: MUST ensure graceful degradation when possible

## Examples

### Compliant Language Specification Structure

```markdown
---
id: msl-l3-advanced-queries
extends: msl-l2-advanced
governed-by: [msl-core-metaspec, msl-language-metaspec]
---

# MSL Level 3: Query Language [MSL]

## Summary
Adds query capabilities for requirement selection and filtering...

## Formal Grammar

### BNF Notation
```bnf
<query>      ::= <selector> (<filter>)*
<selector>   ::= "REQ" | "ALL" | <req-pattern>
<filter>     ::= "[" <condition> "]"
<condition>  ::= <field> <operator> <value>
```

## Semantic Definitions

### Query Evaluation
1. Selector identifies initial requirement set
2. Filters apply left-to-right, narrowing the set
3. Empty result sets return null, not error

## Processing Requirements

### Parser Implementation
- Parse query string into AST
- Validate syntax against BNF
- Apply semantic rules
- Return requirement set

## Validation Rules
- Queries must match BNF grammar
- Field names must exist in schema
- Operators must be valid for field type
```

### Grammar Definition Example

```bnf
# MSL Level 2 Marker Grammar
<requirement>     ::= "-" <space> <req-content> <newline>
<req-content>     ::= <markers>? <req-id>? <inheritance>? <text>
<markers>         ::= (<marker> <space>)*
<marker>          ::= "[" <marker-content> "]"
<marker-content>  ::= <priority-marker> | <status-marker> | 
                      <assignment-marker> | <tag-marker>
<priority-marker> ::= "!"
<status-marker>   ::= "x" | " " | "?"
```

## Notes

Language metaspecs are more rigorous than application metaspecs because they define the foundation that all other specifications build upon. A language specification must be:

1. **Complete** - Every construct fully specified
2. **Unambiguous** - Only one interpretation possible
3. **Implementable** - Sufficient detail for tool builders
4. **Testable** - Clear conformance criteria

The formal grammar requirement (BNF/EBNF) ensures that different implementations will parse MSL consistently. The semantic definitions ensure they will interpret it consistently.

This metaspec itself demonstrates the pattern - providing formal structure for language specifications while being written in MSL.

---
*Specification format: [MSL Level 2](https://github.com/chrs-myrs/msl-specification)*