---
msl: L2
id: msl-llms-txt
tags: [context7, ai-optimization, llms-txt, discovery]
priority: critical
status: active
---

# MSL llms.txt File Specification [MSL]

## Summary

This specification defines requirements for the `/llms.txt` file that enables AI systems and context7 to properly discover, understand, and implement MSL. The llms.txt file acts as a structured entry point that guides AI systems to the most important MSL resources in the correct learning order.

## Requirements

### File Location and Format

- REQ-001: [!] File MUST be named `llms.txt` and located at repository root (`/llms.txt`)
- REQ-002: [!] File MUST use plain text markdown format with clear sections
- REQ-003: File MUST be human-readable and AI-parseable simultaneously
- REQ-004: File size SHOULD be under 10KB to fit in context windows
- REQ-005: File MUST use UTF-8 encoding without BOM

### Content Structure

- REQ-101: [!] MUST begin with one-paragraph MSL overview explaining what MSL is and why it exists
- REQ-102: [!] MUST include "Core Language Specifications" section with ordered links to L0, L1, L2
- REQ-103: [!] MUST include "Implementation Guide" section linking to consolidated reference
- REQ-104: MUST include "Quick Start" section with minimal working example
- REQ-105: MUST include "Topics" section listing searchable keywords for context7

### Language Specification Links

- REQ-201: [!] MUST link to specs in learning order: L0 → L1 → L2
- REQ-202: Each spec link MUST include brief description of what that level adds
- REQ-203: Links MUST use relative paths from repository root
- REQ-204: Links MUST point to actual specification files, not documentation
- REQ-205: SHOULD indicate that specs are self-referential (written in MSL)

### Implementation Reference

- REQ-301: [!] MUST link to implementation-reference.md with complete examples
- REQ-302: MUST indicate that reference contains BNF grammar and Python implementation
- REQ-303: MUST state that examples are self-contained and runnable
- REQ-304: SHOULD mention validation algorithms and quality metrics

### Search Topics

- REQ-401: [!] MUST include "Topics:" section with comma-separated keywords
- REQ-402: Topics MUST include at minimum: "specification", "requirements", "markdown", "validation", "inheritance"
- REQ-403: Topics SHOULD align with common search queries about MSL
- REQ-404: Topics enable context7's topic filtering feature

### Examples Section

- REQ-501: MUST include one complete minimal MSL example (5-10 lines)
- REQ-502: Example MUST be valid MSL Level 0 (just markdown)
- REQ-503: Example MUST demonstrate core value proposition
- REQ-504: Example SHOULD show progression possibility (mention L1/L2 features)

### Metadata and Versioning

- REQ-601: MUST include MSL version being documented
- REQ-602: MUST include last updated date
- REQ-603: MUST include repository URL
- REQ-604: SHOULD include links to tools and validators

## Examples

### Minimal Compliant llms.txt

```markdown
# MSL - Markdown Specification Language

MSL enables precise requirement specifications using plain markdown, progressing from simple lists to validated, inheritable specifications with templates. It bridges human intent and AI implementation.

## Core Language Specifications (Read in Order)

1. [Level 0 Foundation](specs/msl-l0-foundation.md) - Pure markdown with requirements
2. [Level 1 Structure](specs/msl-l1-structure.md) - Adds IDs and frontmatter
3. [Level 2 Advanced](specs/msl-l2-advanced.md) - Full features with formal grammar

## Implementation Guide

Complete implementation details: [Implementation Reference](docs/implementation-reference.md)
- BNF grammar for parsing
- Python validator implementation  
- Runnable examples
- Quality metrics

## Quick Example

```markdown
# Login System

## Requirements
- Users can authenticate with email/password
- Sessions expire after 30 minutes
```

Topics: specification, requirements, markdown, validation, inheritance, templates, msl

Version: 1.2.1 | Updated: 2025-01-05 | Repo: github.com/chrs-myrs/msl-specification
```

## Notes

The llms.txt file is inspired by the robots.txt convention but for LLMs. Just as robots.txt tells web crawlers what to index, llms.txt tells AI systems what's important for understanding and implementing MSL. This single file dramatically improves context7's ability to provide complete, accurate MSL information rather than fragmented snippets.

---
*Specification format: [MSL Level 2](https://github.com/chrs-myrs/msl-specification)*