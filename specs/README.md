# MSL Specifications Directory

This directory contains the complete specification of Markdown Specification Language (MSL), organized as a progressive enhancement from simple to sophisticated.

## 📁 Directory Structure

```
specs/
├── Core Language (Progressive Enhancement)
│   ├── msl-l0-foundation.md      # Pure markdown with requirements
│   ├── msl-l1-structure.md       # + Optional frontmatter & IDs (extends L0)
│   └── msl-l2-advanced.md        # + Markers, templates, formal spec (extends L1)
│
├── standards/                     # Quality & Design Standards  
│   ├── msl-usage-standards.md    # DRY, inheritance, architecture principles
│   └── msl-extension-standards.md # Extension design guidelines
│
└── applications/                  # MSL in Practice
    ├── msl-tools-spec.md         # Tool implementation requirements
    └── msl-validation-agent.md   # Intelligent validation agent
```

## 🎯 Architecture Overview

### Core Language Definition (L0 → L1 → L2)

MSL is defined through three levels of progressive enhancement:

1. **[msl-l0-foundation.md](msl-l0-foundation.md)** - Just markdown with a Requirements section
   - Human-friendly, no tools needed
   - Perfect for simple specifications
   - Uses gentle "should" language

2. **[msl-l1-structure.md](msl-l1-structure.md)** - Adds optional structure
   - YAML frontmatter for metadata
   - REQ-IDs for requirement tracking
   - Basic inheritance with `extends`
   - Everything is optional - L0 docs are valid L1

3. **[msl-l2-advanced.md](msl-l2-advanced.md)** - **Complete MSL specification**
   - Quick markers for status, priority, assignment
   - Advanced inheritance controls
   - Template system with variables
   - **Contains formal grammar (BNF) and semantics**
   - This is where automation begins

**Key Insight:** L2 IS the complete MSL language. It includes all features plus the formal specifications needed for tool implementation.

### Standards & Best Practices

Quality standards that extend L2 with guidelines:

- **[standards/msl-usage-standards.md](standards/msl-usage-standards.md)** - DRY principles, inheritance patterns, quality metrics
- **[standards/msl-extension-standards.md](standards/msl-extension-standards.md)** - How to create domain-specific MSL extensions

### Applications

Real-world MSL specifications that demonstrate the language:

- **[applications/msl-tools-spec.md](applications/msl-tools-spec.md)** - Requirements for MSL processing tools
- **[applications/msl-validation-agent.md](applications/msl-validation-agent.md)** - Intelligent agent for validating MSL quality

## 🔄 Inheritance Relationships

```
msl-l0-foundation (human-friendly foundation)
    ↓ extends
msl-l1-structure (+ optional structure)
    ↓ extends  
msl-l2-advanced (+ advanced features + formal spec = COMPLETE MSL)
    ↓ extended by
standards/* (quality guidelines)

applications/* use MSL but don't extend the language
```

## ✅ Key Design Principles

### 1. Progressive Enhancement
- Start simple (L0) - just markdown with requirements
- Add structure when needed (L1) - IDs and metadata
- Use full power when required (L2) - markers, templates, automation

### 2. Human-Friendly to Automation-Ready
- L0-L1: Designed for humans, uses gentle language
- L2: Provides formal specification for tool builders
- "Formalization appears where automation begins"

### 3. Self-Specification
- Each level is itself a valid MSL document
- MSL specifications use MSL to define MSL
- Demonstrates the language by example

### 4. Simplicity
- L2 contains everything - no separate "complete" spec needed
- Grammar and semantics consolidated where they're used
- Each document has a single, clear purpose

## 🚀 Quick Start Guide

### For Writing Specifications

**Simple spec?** Use Level 0:
```markdown
# My Feature [MSL]

## Requirements
- System does X
- Users can Y
- Performance is Z

---
*Specified using [MSL](https://github.com/chrs-myrs/msl-specification)*
```

**Need tracking?** Add Level 1 features:
```markdown
---
msl: L1
id: my-feature
---

# My Feature [MSL]

## Requirements
- REQ-001: System does X
- REQ-002: Users can Y
```

**Complex project?** Use Level 2:
```markdown
---
msl: L2
id: my-feature
extends: base-feature
---

# My Feature [MSL]

## Requirements
- [!] [@alice] REQ-001: [OVERRIDE] Critical security requirement
- [x] [#mvp] REQ-002: [NEW] Completed MVP feature
```

### Identifying MSL Documents

MSL documents should be identifiable through one or more of these methods:

1. **Title Marker**: Include `[MSL]` in the document title
2. **Repository Link**: Link to the MSL specification
3. **Frontmatter Field**: Use `msl: L0/L1/L2` in YAML frontmatter

These are encouraged but not required - the presence of a `## Requirements` section is the minimum for an MSL document.

### For Tool Implementers

1. Start with [msl-l2-advanced.md](msl-l2-advanced.md) - it contains:
   - Complete feature requirements
   - Formal BNF grammar
   - Semantic definitions
   - Processing rules

2. Follow the progressive approach:
   - Parse L0 first (just markdown)
   - Add L1 (frontmatter, IDs)
   - Implement L2 (full features)

3. Use [applications/msl-tools-spec.md](applications/msl-tools-spec.md) for tool requirements

## 🔍 Validation

All specifications in this directory are valid MSL documents:

```bash
# Each spec can be validated according to its level
msl-lint specs/

# L0 specs just need markdown + requirements
# L1 specs may have frontmatter + IDs
# L2 specs may use all features
```

## 📝 Summary

This architecture achieves:
- **Simplicity**: Three levels, progressively enhanced
- **Completeness**: L2 contains the entire language + formal spec
- **Usability**: Human-friendly at low levels, automation-ready at L2
- **Demonstration**: Every spec is itself a valid MSL document

The key insight: **Start simple, enhance as needed.** Most projects only need L0 or L1. When you need the full power of MSL, L2 provides everything including the formal specification for building tools.