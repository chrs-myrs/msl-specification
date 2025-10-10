---
id: msl-purpose-and-limitations
type: specification
governed-by: msl-core-metaspec
tags: [core, philosophy, limitations, purpose]
---

# MSL Purpose and Limitations [MSL]

## Summary

This specification defines the core purpose of MSL (Markdown Specification Language) and its intentional limitations. Every MSL project should reference this to maintain clarity about what MSL is and isn't.

## Requirements

### Core Purpose

- MSL SHALL bridge the gap between human intent and AI implementation
- MSL SHALL provide stable, unambiguous specifications for AI-driven development
- MSL SHALL remain human-readable and reviewable without special tools
- MSL SHALL enable specification-first development workflows
- MSL SHALL be discoverable and parseable by AI tools (context7, LLMs, etc.)
- MSL SHALL prove its capability through self-specification (dogfooding)

### Target Users

- MSL SHALL serve developers working with AI assistants
- MSL SHALL serve AI agents generating code from specifications
- MSL SHALL serve project managers defining requirements
- MSL SHALL serve quality assurance teams validating implementations
- MSL SHALL serve documentation teams maintaining project specs

### Intentional Limitations

- MSL SHALL NOT define implementation details or algorithms
- MSL SHALL NOT act as a programming or scripting language
- MSL SHALL NOT enforce runtime behavior or validation
- MSL SHALL NOT require specific tools or IDEs to read or write
- MSL SHALL NOT mandate specific project structures (only recommend)
- MSL SHALL remain a pure specification markup language

### Philosophy Principles

- Simplicity SHALL always enable flexibility
- Progressive enhancement SHALL allow starting simple and adding complexity only when needed
- Intuitive readability SHALL prioritize understandability - specs should be mostly comprehensible without MSL knowledge
- Specifications work best when they trust implementers' judgment
- Dogfooding SHALL demonstrate that MSL can specify anything, including itself
- Specifications SHALL be AI-first but human-friendly
- Markdown SHALL remain the foundation (no proprietary formats)
- Optional features SHALL never break basic functionality

### Success Metrics

- An AI agent SHALL be able to implement working code from MSL specifications alone
- A human SHALL be able to understand an MSL specification without training
- MSL specifications SHALL remain valid markdown viewable on GitHub
- Complex projects SHALL be specifiable using MSL's optional advanced features
- MSL SHALL successfully specify its own language, tools, and documentation

### Integration Requirements

- MSL SHALL integrate with version control systems (git)
- MSL SHALL be discoverable by documentation tools (context7, etc.)
- MSL SHALL support progressive disclosure of complexity
- MSL SHALL allow for project-specific extensions via metaspecs
- MSL SHALL maintain backward compatibility with simpler levels

## Notes

This specification itself is written in MSL, demonstrating the principle of dogfooding. It uses Level 1 features (frontmatter, requirement IDs) while remaining readable as plain markdown.

The fact that MSL can specify its own purpose and limitations proves its completeness as a specification language. This self-referential capability is not a curiosity but a key feature that ensures MSL can handle any specification need.