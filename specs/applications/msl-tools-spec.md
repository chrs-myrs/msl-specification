---
msl: L2
id: msl-tools-spec
tags: [tools, processing, validation, cli, applications]
priority: critical
status: active
assignee: msl-tools-team
references:
  - msl-l2-advanced: "Complete MSL language definition with grammar and semantics"
---

# MSL Tools Specification [MSL]

## Summary

This specification defines the requirements for MSL processing tools and implementations. It uses MSL to specify how MSL processors, validators, and command-line tools must behave to ensure consistent and correct MSL handling across different platforms and implementations.

This specification serves as the implementation guide for MSL toolchain developers and defines the expected behavior of MSL processing workflows. It demonstrates MSL being used to specify software tools that process MSL itself.

**Note:** This is an APPLICATION of MSL - it uses MSL to specify tool behavior rather than extending the MSL language definition.

## Requirements

### Core Processing Principles

- REQ-001: [!] MSL processors must correctly parse all syntax rules defined in `msl-grammar.md`
- REQ-002: [!] MSL processors must correctly interpret all behavioral rules defined in `msl-semantics.md`  
- REQ-003: [!] MSL processors must provide consistent behavior across platforms and implementations
- REQ-004: [!] MSL processing must be deterministic given identical input and configuration
- REQ-005: [!] MSL processors must fail gracefully with clear error messages for invalid input

### File Processing Requirements

- REQ-101: [!] [@msl-tools] Processors must support `.md` and `.msl` file extensions
- REQ-102: [!] [@msl-tools] Processors must handle UTF-8 encoded files correctly
- REQ-103: [@msl-tools] Processors must accept both Unix (LF) and Windows (CRLF) line endings
- REQ-104: [@msl-tools] Processors must preserve file metadata and timestamps when possible
- REQ-105: [@msl-tools] Processors must handle missing or inaccessible files with appropriate errors

### YAML Frontmatter Processing

- REQ-201: [!] [@msl-tools] Processors must parse YAML frontmatter using YAML 1.2 specification
- REQ-202: [!] [@msl-tools] Processors must handle missing frontmatter by defaulting to Level 0 processing
- REQ-203: [@msl-tools] Processors must preserve unknown frontmatter fields for tool interoperability
- REQ-204: [@msl-tools] Processors must validate frontmatter schema against MSL grammar rules
- REQ-205: [#error-handling] Invalid YAML must trigger fallback to Level 0 processing with warnings

### Document Structure Processing

- REQ-301: [!] [@msl-tools] Processors must identify and parse document title from level 1 heading
- REQ-302: [!] [@msl-tools] Processors must locate "Requirements" section and extract requirement list
- REQ-303: [@msl-tools] Processors must parse optional Summary, Notes, and custom sections
- REQ-304: [@msl-tools] Processors must preserve markdown formatting in non-requirement content
- REQ-305: [@msl-tools] Processors must handle documents with missing or malformed structure gracefully

### Requirement Processing

- REQ-401: [!] [@msl-tools] Processors must extract REQ-XXX identifiers and requirement text
- REQ-402: [!] [@msl-tools] Processors must parse and interpret quick markers correctly
- REQ-402.1: [NEW] Processors must support composite markers with pipe-separated components (v1.4.0+)
- REQ-402.2: [NEW] Processors must parse key:value pairs within composite markers for metrics and metadata
- REQ-402.3: [NEW] Processors must validate marker combinations for consistency (e.g., not both blocked and complete)
- REQ-403: [@msl-tools] Processors must validate REQ-ID uniqueness within documents
- REQ-404: [@msl-tools] Processors must support nested requirement lists with proper indentation
- REQ-405: [@msl-tools] Processors must preserve requirement text formatting and markdown syntax

### Inheritance Processing

- REQ-501: [!] [@msl-tools] Processors must resolve inheritance chains following MSL semantic rules
- REQ-502: [!] [@msl-tools] Processors must detect and reject circular inheritance dependencies
- REQ-503: [!] [@msl-tools] Processors must apply inheritance markers correctly per semantic specification
- REQ-504: [@msl-tools] Processors must validate parent document existence before inheritance processing
- REQ-505: [@msl-tools] Processors must generate complete resolved specification from inheritance chain
- REQ-506: [@msl-tools] Processors must handle missing parent documents with clear error messages

### Template Processing

- REQ-601: [!] [#templates] [@msl-tools] [NEW] Processors must identify template documents by `type: template` in frontmatter
- REQ-602: [!] [#templates] [@msl-tools] [NEW] Processors must perform variable substitution for `${variable_name}` patterns
- REQ-603: [!] [#templates] [@msl-tools] [NEW] Processors must validate all variable references are defined before substitution
- REQ-604: [#templates] [@msl-tools] [NEW] Processors must support variable inheritance in template chains
- REQ-605: [#templates] [@msl-tools] [NEW] Processors must generate errors for undefined variable references with helpful context

### Validation Processing

- REQ-701: [!] [@msl-lint] [NEW] MSL linting must validate document structure against grammar rules
- REQ-702: [!] [@msl-lint] [NEW] Linting must validate semantic consistency of inheritance relationships
- REQ-703: [!] [@msl-lint] [NEW] Linting must validate marker syntax and semantic usage
- REQ-704: [@msl-lint] [NEW] Linting must validate REQ-ID uniqueness and format compliance
- REQ-705: [@msl-lint] [NEW] Linting must validate frontmatter schema compliance
- REQ-706: [@msl-lint] [NEW] Linting must provide actionable error messages with file:line:column locations
- REQ-707: [@msl-lint] [NEW] Linting must support batch processing of multiple files and directories

### Rendering Processing

- REQ-801: [!] [@msl-render] [NEW] Rendering must support template instantiation with variable substitution
- REQ-802: [!] [@msl-render] [NEW] Rendering must resolve inheritance chains to produce complete specifications
- REQ-803: [@msl-render] [NEW] Rendering must preserve markdown formatting in output
- REQ-804: [@msl-render] [NEW] Rendering must support multiple output formats (markdown, HTML, PDF)
- REQ-805: [@msl-render] [NEW] Rendering must provide options for requirement filtering and selection

### CLI Tool Requirements

- REQ-901: [!] [@msl-tools] CLI tools must provide consistent command-line interface across platforms
- REQ-902: [!] [@msl-tools] CLI tools must support standard Unix conventions (exit codes, stdout/stderr)
- REQ-903: [@msl-tools] CLI tools must provide help documentation and usage examples
- REQ-904: [@msl-tools] CLI tools must support batch processing with glob patterns
- REQ-905: [@msl-tools] CLI tools must provide verbose and quiet operation modes
- REQ-906: [@msl-tools] CLI tools must support configuration files for default options

### Error Handling Requirements

- REQ-1001: [!] [#error-handling] [@msl-tools] Processors must provide clear error messages with file and line information
- REQ-1002: [#error-handling] [@msl-tools] Processors must distinguish between errors (blocking) and warnings (advisory)
- REQ-1003: [#error-handling] [@msl-tools] Processors must use appropriate exit codes for success/failure status
- REQ-1004: [#error-handling] [@msl-tools] Processors must handle interrupted operations gracefully
- REQ-1005: [#error-handling] [@msl-tools] Processors must provide debugging output in verbose mode

### Performance Requirements

- REQ-1101: [!] [@msl-tools] [#performance] [NEW] Processors must handle ≤100 specs in <1s, ≤10,000 specs in <60s
- REQ-1102: [@msl-tools] [#performance] [NEW] Memory usage must stay ≤4GB for specification sets up to 100,000 requirements
- REQ-1103: [@msl-tools] [#performance] [NEW] Progress indicators required for operations exceeding 5 seconds
- REQ-1104: [@msl-tools] [#performance] [NEW] Parallel processing must achieve ≥70% efficiency on multi-core systems
- REQ-1105: [@msl-tools] [#performance] [NEW] Cache must improve repeated operation performance by ≥50%

### Integration Requirements

- REQ-1201: [@msl-tools] [#integration] Processors must support JSON output for tool integration
- REQ-1202: [@msl-tools] [#integration] Processors must support machine-readable error formats
- REQ-1203: [@msl-tools] [#integration] Processors must provide APIs for programmatic access
- REQ-1204: [@msl-tools] [#integration] Processors must support configuration via environment variables
- REQ-1205: [@msl-tools] [#integration] Processors must integrate with standard development workflows

### Compatibility Requirements

- REQ-1301: [!] [@msl-tools] [#backward-compatibility] Processors must handle all MSL levels (0, 1, 2) correctly
- REQ-1302: [!] [@msl-tools] [#backward-compatibility] Newer processors must process older MSL documents
- REQ-1303: [@msl-tools] [#forward-compatibility] Processors should handle unknown constructs gracefully
- REQ-1304: [@msl-tools] [#compatibility] Processors must maintain consistent behavior across versions
- REQ-1305: [@msl-tools] [#compatibility] Processors must provide migration assistance for version updates

## Common CLI Tool Patterns

### Standard CLI Behaviors

- REQ-1401: [!] [@msl-tools] [NEW] All CLI tools must accept file paths, globs, or directories as input
- REQ-1402: [!] [@msl-tools] [NEW] All CLI tools must support `--format` flag for output format (text, json, xml, markdown)
- REQ-1403: [!] [@msl-tools] [NEW] All CLI tools must return exit code 0 for success, non-zero for errors
- REQ-1404: [@msl-tools] [NEW] All CLI tools must support `--output` flag to specify output file
- REQ-1405: [@msl-tools] [NEW] All CLI tools must support `--verbose` and `--quiet` flags for output control
- REQ-1406: [@msl-tools] [NEW] All CLI tools must provide `--help` flag with usage examples
- REQ-1407: [@msl-tools] [NEW] All CLI tools must support `--version` flag to display version information

## CLI Tool Specifications

### msl-lint Tool

- REQ-1501: [!] [@msl-lint] [INHERIT] Standard CLI behaviors from REQ-1401 through REQ-1407
- REQ-1502: [!] [@msl-lint] [NEW] `msl-lint <files>` validates MSL documents against grammar and semantics
- REQ-1503: [@msl-lint] [NEW] Supports `--check-ids` flag to validate REQ-ID uniqueness across files
- REQ-1504: [@msl-lint] [NEW] Supports `--level` flag to validate against specific MSL level (0, 1, or 2)
- REQ-1505: [@msl-lint] [NEW] Supports `--fix` flag to automatically fix correctable issues
- REQ-1506: [@msl-lint] [NEW] Provides line-by-line error reporting with context

### msl-render Tool  

- REQ-1601: [!] [@msl-render] [INHERIT] Standard CLI behaviors from REQ-1401 through REQ-1407
- REQ-1602: [!] [@msl-render] [NEW] `msl-render <template>` instantiates template with variables
- REQ-1603: [@msl-render] [NEW] Supports `-v variable=value` flag for variable assignment
- REQ-1604: [@msl-render] [NEW] Supports `--vars-file` flag to load variables from YAML/JSON file
- REQ-1605: [@msl-render] [NEW] Supports `--resolve` flag to resolve complete inheritance chains
- REQ-1606: [@msl-render] [NEW] Validates all template variables are defined before rendering

### msl-validate Tool

- REQ-1701: [!] [@msl-validate] [INHERIT] Standard CLI behaviors from REQ-1401 through REQ-1407
- REQ-1702: [!] [@msl-validate] [NEW] `msl-validate <files>` performs comprehensive validation
- REQ-1703: [@msl-validate] [NEW] Validates inheritance chain completeness and consistency  
- REQ-1704: [@msl-validate] [NEW] Validates cross-document references and dependencies
- REQ-1705: [@msl-validate] [NEW] Supports `--strict` flag for enhanced validation rules
- REQ-1706: [@msl-validate] [NEW] Provides validation reports with actionable recommendations
- REQ-1707: [@msl-validate] [NEW] Generates quality score (0-100) with breakdown by category

## Processing Workflow

### Standard Processing Pipeline

- REQ-1801: [!] [@msl-tools] [NEW] Parse file and extract frontmatter using YAML 1.2 processor
- REQ-1802: [!] [@msl-tools] [NEW] Parse document structure and identify required sections
- REQ-1803: [!] [@msl-tools] [NEW] Extract requirements and parse markers, IDs, and inheritance
- REQ-1804: [@msl-tools] [NEW] Resolve inheritance chains and perform variable substitution
- REQ-1805: [@msl-tools] [NEW] Validate semantic consistency and generate warnings/errors
- REQ-1806: [@msl-tools] [NEW] Generate output in requested format with proper encoding

### Error Recovery Processing

- REQ-1901: [#error-handling] [@msl-tools] [NEW] Invalid frontmatter triggers Level 0 fallback processing
- REQ-1902: [#error-handling] [@msl-tools] [NEW] Missing sections continue processing with warnings
- REQ-1903: [#error-handling] [@msl-tools] [NEW] Invalid markers treated as plain text with warnings
- REQ-1904: [#error-handling] [@msl-tools] [NEW] Processing continues after non-fatal errors when possible
- REQ-1905: [#error-handling] [@msl-tools] [NEW] Complete error reporting provided at end of processing

## Examples

### CLI Usage Examples

```bash
# Lint all MSL files in specs directory
msl-lint specs/*.md

# Render template with variables
msl-render template.md -v service=UserAPI -v version=2.0

# Validate inheritance chains
msl-validate --check-inheritance specs/
```

### Processing Pipeline Example

```
Input: user-auth.md
  ↓
Parse YAML frontmatter → Extract: id, extends, variables
  ↓  
Parse document structure → Extract: title, requirements, sections
  ↓
Extract requirements → Parse: REQ-IDs, markers, inheritance
  ↓
Resolve inheritance → Merge: parent requirements, apply markers
  ↓
Substitute variables → Replace: ${var} with values
  ↓
Validate semantics → Check: IDs, references, consistency
  ↓
Output: Processed specification
```

## Notes

This tool specification demonstrates how MSL can be used to specify complex software requirements. The MSL tools themselves are specified using MSL, creating a practical example of MSL in action.

The specification supports both simple single-file processing and complex multi-document workflows with inheritance, templates, and validation, showing MSL's capability for specifying sophisticated software systems.

---
*Specification format: [MSL Level 2](https://github.com/chrs-myrs/msl-specification)*