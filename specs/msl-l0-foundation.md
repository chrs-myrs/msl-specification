# MSL Level 0: Foundation Specification

## Summary

This specification defines the minimal structural requirements for Markdown Specification Language (MSL) documents using only pure markdown. MSL Level 0 forms the foundation upon which higher levels build additional features.

MSL Level 0 requires no special tools, frontmatter, or complex syntax. Any markdown processor can render these specifications, making them universally accessible and human-readable.

## Requirements

### Document Structure

- MSL documents must have a title as the first heading level 1
- Title must use hash syntax with single hash and space
- Document title should describe the system, feature, or component being specified
- Title must be followed by at least one section

### Requirements Section

- MSL documents must contain exactly one section titled "Requirements"
- Requirements section must use heading level 2 syntax  
- Requirements section heading must be exactly "## Requirements"
- Requirements section must contain at least one requirement

### Requirement Format

- Requirements must be written as markdown list items
- List items must use dash syntax with space after dash
- Each requirement must be a single list item
- Requirements should be clear, testable, and specific
- Requirements may contain sub-items using indented list syntax

### Content Guidelines  

- Requirements should avoid implementation details when possible
- Requirements should focus on what the system must do, not how
- Requirements may reference other requirements within the same document
- Requirements should be written in present tense
- Requirements should use "must", "should", or "may" to indicate necessity level

### Optional Sections

- Documents may include additional sections beyond Requirements
- Common optional sections include Summary, Notes, Examples
- Optional sections must use heading level 2 or lower
- Optional sections may appear before or after Requirements section
- Custom sections are permitted for domain-specific needs

### File Format

- MSL documents must use markdown file extension (.md)
- Documents must be valid markdown that renders in standard processors
- Documents should use UTF-8 encoding
- Line endings may be Unix (LF) or Windows (CRLF)
- Filenames should be descriptive and use kebab-case when possible

### Markdown Compatibility

- MSL Level 0 must be compatible with CommonMark specification
- Documents must render correctly in GitHub-flavored markdown
- Documents should avoid markdown extensions that break compatibility
- Code blocks, tables, and other markdown features may be used in content
- Links and references follow standard markdown syntax

### Processing Expectations

- MSL Level 0 documents can be processed by any markdown renderer
- Document structure can be extracted using standard markdown parsers
- Requirements can be identified by finding "## Requirements" section
- List items under Requirements section represent individual requirements
- No special MSL processing tools are required for Level 0

## Notes

MSL Level 0 provides the foundation for more advanced MSL features. This specification itself demonstrates MSL Level 0 compliance by using only standard markdown syntax.

The key insight of MSL Level 0 is that useful specifications can be written with minimal syntax while remaining completely compatible with existing markdown tools and workflows.

Higher MSL levels build upon this foundation by adding structured metadata, requirement IDs, inheritance, and other advanced features, but all MSL documents must remain valid Level 0 documents at their core.