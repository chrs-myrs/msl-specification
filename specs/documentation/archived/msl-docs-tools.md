---
msl: L1
id: msl-docs-tools
tags: [documentation, tools, cli, integration]
priority: high
status: active
references:
  - msl-docs-root: "Part of documentation system"
  - msl-tools-spec: "MSL tools to document"
  - msl-validation-agent: "MSL validation agent to document"
  - msl-batch-validator: "MSL batch validator to document"
---

# MSL Tools Documentation Specification [MSL]

## Summary

This specification defines requirements for documenting MSL's own tools and processing systems, including CLI tools (msl-lint, msl-validate, msl-render), validation agents, and integration APIs specific to the MSL ecosystem.

## Requirements

### MSL Tool Documentation

- REQ-001: [!] [NEW] Each MSL tool must document: purpose, installation, basic usage
- REQ-002: [!] [NEW] MSL CLI tools must document all flags and options
- REQ-003: [NEW] Exit codes and their meanings must be specified
- REQ-004: [NEW] Configuration file formats must be documented (.msl-validate.yml, etc.)
- REQ-005: [NEW] Environment variables must be listed

### MSL CLI Tools Coverage

- REQ-101: [!] [NEW] Must document msl-lint tool completely
- REQ-102: [!] [NEW] Must document msl-validate tool completely
- REQ-103: [!] [NEW] Must document msl-render tool completely
- REQ-104: [NEW] Must document msl-batch-validate tool
- REQ-105: [NEW] Must document any future MSL tools

### Code Examples

- REQ-201: [!] [NEW] Each MSL tool must include usage examples
- REQ-202: [NEW] Examples must show: basic usage, advanced usage, error cases
- REQ-203: [NEW] Examples must be tested against actual MSL tools
- REQ-204: [NEW] Examples must include common workflow patterns
- REQ-205: [NEW] Examples must show both success and failure cases

### Integration Guides

- REQ-301: [!] [NEW] Must include MSL in CI/CD pipeline guide
- REQ-302: [NEW] Must include IDE/editor MSL support guide
- REQ-303: [NEW] Must include MSL validation pipeline setup
- REQ-304: [NEW] Must include batch validation workflow guide
- REQ-305: [NEW] Must include performance tips for large spec sets

### MSL-Specific Formats

- REQ-401: [!] [NEW] MSL validation output must document JSON, XML, and Markdown formats
- REQ-402: [NEW] MSL configuration schemas must use JSON Schema draft-07
- REQ-403: [NEW] MSL error messages must include: code, file, line, column, message
- REQ-404: [NEW] MSL reports must specify markdown table and JSON formats
- REQ-405: [NEW] MSL must document breaking changes for each version transition

### Claude Code Agent Integration

- REQ-501: [!] [NEW] MSL Claude Code agents usage must include ≥3 invocation examples
- REQ-502: [NEW] MSL agent capabilities must list ≥10 features and ≥5 limitations
- REQ-503: [NEW] MSL agent examples must show request and response formats
- REQ-504: [NEW] MSL context must specify <100KB recommended, <500KB maximum
- REQ-505: [NEW] MCP server integration must explain context7 protocol with examples

## Validation Criteria

API documentation is valid when:
- All endpoints are documented
- Examples execute successfully
- Schemas validate correctly
- Integration guides are complete
- Agent integration works as documented

## Notes

API and tools documentation enables the MSL ecosystem to grow through integrations. Clear, comprehensive documentation with working examples is essential for adoption.

---
*Specification format: [MSL Level 1](https://github.com/chrs-myrs/msl-specification)*