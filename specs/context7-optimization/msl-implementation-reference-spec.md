---
msl: L2
id: msl-implementation-reference
tags: [implementation, reference, grammar, validation, python]
priority: critical
status: active
---

# MSL Implementation Reference Specification [MSL]

## Summary

This specification defines requirements for a consolidated implementation reference that provides everything needed to implement MSL validation and processing tools. This single document serves as the authoritative source for AI systems to understand how to build MSL-compliant tools.

## Requirements

### Document Structure

- REQ-001: [!] Document MUST be self-contained with no external dependencies
- REQ-002: [!] Document MUST be located at `/docs/implementation-reference.md`
- REQ-003: Document MUST be organized in implementation order (parse → validate → process)
- REQ-004: Document MUST include table of contents with anchor links
- REQ-005: Document size SHOULD be under 30KB for optimal context window usage

### Formal Grammar Section

- REQ-101: [!] MUST include complete BNF grammar copied from msl-l2-advanced.md
- REQ-102: [!] MUST include EBNF notation for complex rules
- REQ-103: MUST provide grammar for all three MSL levels (L0, L1, L2)
- REQ-104: MUST include examples of valid and invalid syntax for each rule
- REQ-105: Grammar MUST be suitable for parser generator input

### Parser Implementation

- REQ-201: [!] MUST include complete Python parser implementation
- REQ-202: Parser MUST handle all three MSL levels progressively
- REQ-203: Parser MUST extract: frontmatter, requirements, markers, inheritance
- REQ-204: Implementation MUST be <200 lines of readable Python
- REQ-205: MUST include error handling with line numbers

### Validation Implementation

- REQ-301: [!] MUST include complete validation logic from msl-lint tool
- REQ-302: MUST show how to check for Requirements section
- REQ-303: MUST show duplicate REQ-ID detection
- REQ-304: MUST show marker conflict detection
- REQ-305: MUST include inheritance chain validation

### Quality Metrics

- REQ-401: [!] MUST include algorithms for calculating quality score (0-100)
- REQ-402: MUST show DRY compliance calculation (<20% duplication)
- REQ-403: MUST show testability scoring (≥90% measurable)
- REQ-404: MUST show cohesion/coupling calculations
- REQ-405: MUST provide score interpretation thresholds

### Template Processing

- REQ-501: MUST include template variable substitution implementation
- REQ-502: MUST show Jinja2-style `${variable}` processing
- REQ-503: MUST handle nested variable resolution
- REQ-504: MUST include undefined variable error handling

### Inheritance Resolution

- REQ-601: MUST include complete inheritance resolution algorithm
- REQ-602: MUST show how [OVERRIDE], [NEW], [INHERIT] markers work
- REQ-603: MUST handle multi-level inheritance chains
- REQ-604: MUST detect circular inheritance
- REQ-605: MUST show requirement merging logic

### Working Examples

- REQ-701: [!] MUST include 3-5 complete, runnable Python scripts
- REQ-702: Examples MUST cover: basic validation, inheritance resolution, template rendering
- REQ-703: Each example MUST include sample input and expected output
- REQ-704: Examples MUST be copy-paste runnable with no modifications
- REQ-705: Examples MUST demonstrate error cases

### Testing Utilities

- REQ-801: MUST include test helper functions
- REQ-802: MUST show how to validate MSL programmatically
- REQ-803: MUST include assertion helpers for quality metrics
- REQ-804: SHOULD include performance benchmarks

## Examples

### Structure Example

```markdown
# MSL Implementation Reference

## Table of Contents
1. [Grammar Specification](#grammar)
2. [Parser Implementation](#parser)
3. [Validator Implementation](#validator)
4. [Quality Metrics](#metrics)
5. [Complete Examples](#examples)

## Grammar Specification

### BNF Grammar
```bnf
<msl-document> ::= <frontmatter>? <content>
<frontmatter>  ::= "---" <newline> <yaml> "---" <newline>
...
```

## Parser Implementation

```python
import re
import yaml
from pathlib import Path

class MSLParser:
    def parse(self, content):
        # Complete implementation here
        ...
```
```

### Complete Validator Example

```python
#!/usr/bin/env python3
"""Complete MSL validator implementation"""

def validate_msl(file_path):
    """Validate an MSL file and return issues list"""
    content = Path(file_path).read_text()
    issues = []
    
    # Check for Requirements section
    if '## Requirements' not in content:
        issues.append({
            'severity': 'error',
            'message': 'Missing ## Requirements section',
            'line': None
        })
    
    # Check for duplicate REQ-IDs
    req_ids = re.findall(r'REQ-\d+', content)
    if len(req_ids) != len(set(req_ids)):
        duplicates = [id for id in req_ids if req_ids.count(id) > 1]
        issues.append({
            'severity': 'error', 
            'message': f'Duplicate REQ-IDs: {duplicates}',
            'line': None
        })
    
    return issues
```

## Notes

This implementation reference consolidates all technical details needed to implement MSL tools. By providing complete, runnable code in a single document, AI systems can understand the full implementation without needing to piece together fragments from multiple sources. This dramatically improves the accuracy of AI-generated MSL tools.

---
*Specification format: [MSL Level 2](https://github.com/chrs-myrs/msl-specification)*