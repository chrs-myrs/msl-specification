# Metaspec Governance Proposal for MSL

## Summary

This proposal introduces a new `governed-by` frontmatter field that allows specifications to explicitly declare which metaspec governs their structure, requirements, and quality standards. This creates a formal governance relationship distinct from inheritance (`extends`) and templates (`type: template`).

## Motivation

Currently, MSL has implicit metaspec patterns through:
- **Templates**: Define reusable patterns with variables
- **Standards**: Define quality requirements (like `msl-usage-standards`)
- **Extension specs**: Define how to extend MSL itself

However, there's no explicit way to:
1. Declare that a spec must conform to a particular metaspec
2. Validate that a spec meets its metaspec's requirements
3. Query which specs are governed by which metaspecs
4. Enforce architectural patterns across specification families

## Proposed Syntax

### Basic Governance

```yaml
---
id: user-api
governed-by: rest-api-metaspec
---
```

### Multiple Governance (Composition)

```yaml
---
id: payment-api
governed-by: [rest-api-metaspec, pci-compliance-metaspec]
---
```

### Versioned Governance

```yaml
---
id: user-service
governed-by: microservice-metaspec@v2.0
---
```

## Semantic Differences

### `extends` vs `governed-by` vs `type: template`

| Feature | `extends` | `governed-by` | `type: template` |
|---------|-----------|---------------|------------------|
| Relationship | IS-A (inheritance) | CONFORMS-TO (governance) | DEFINES (pattern) |
| Requirements | Inherits parent requirements | Must meet metaspec criteria | Provides variable substitution |
| Validation | Checks REQ-ID conflicts | Validates structure/quality | Validates variable resolution |
| Multiple | No (single parent) | Yes (multiple metaspecs) | No (is or isn't template) |
| Purpose | Specialize behavior | Ensure compliance | Create reusable patterns |

## Metaspec Structure

A metaspec is a specification that defines requirements for other specifications:

```markdown
---
id: rest-api-metaspec
type: metaspec
version: 1.0.0
---

# REST API Metaspec

## Summary

This metaspec governs all REST API specifications, ensuring they meet organizational standards for API design, documentation, and quality.

## Structural Requirements

- MUST have `## Endpoints` section documenting all endpoints
- MUST have `## Authentication` section describing auth method
- MUST have `## Error Handling` section with error codes
- MUST include OpenAPI spec reference or inline definition
- MUST specify rate limiting requirements

## Quality Requirements

- ALL endpoints MUST have request/response examples
- ALL error codes MUST have descriptions
- Authentication MUST specify token format and lifetime
- Rate limits MUST specify requests per time unit

## Validation Rules

- Endpoint paths MUST follow REST conventions
- HTTP methods MUST be semantically correct
- Status codes MUST follow RFC 7231
- Content-Type MUST be specified for all requests/responses
```

## Implementation Examples

### Example 1: API Specification

```markdown
---
id: user-management-api
governed-by: rest-api-metaspec
tags: [api, users, authentication]
---

# User Management API

## Endpoints

- `GET /users` - List all users
- `GET /users/{id}` - Get user by ID
- `POST /users` - Create new user
- `PUT /users/{id}` - Update user
- `DELETE /users/{id}` - Delete user

## Authentication

Bearer token authentication required for all endpoints.
Tokens expire after 1 hour.

## Error Handling

- `400` - Invalid request format
- `401` - Missing or invalid authentication
- `403` - Insufficient permissions
- `404` - User not found
- `429` - Rate limit exceeded

## Rate Limiting

- 100 requests per minute per API key
- 10 requests per second burst limit
```

### Example 2: Multiple Governance

```markdown
---
id: payment-processing-api
governed-by: [rest-api-metaspec, pci-compliance-metaspec, high-availability-metaspec]
priority: critical
---

# Payment Processing API

[Content meeting requirements of all three metaspecs]
```

### Example 3: Service Specification

```markdown
---
id: notification-service
governed-by: microservice-metaspec@v2.0
extends: base-service
---

# Notification Service

[Content that both inherits from base-service AND conforms to microservice-metaspec v2.0]
```

## Validation Capabilities

With `governed-by`, validators can:

1. **Check structural compliance**: Verify required sections exist
2. **Validate content patterns**: Ensure content matches metaspec rules
3. **Score quality metrics**: Rate compliance with metaspec standards
4. **Generate reports**: Show which requirements are met/unmet
5. **Suggest fixes**: Provide guidance on meeting metaspec requirements

### Validation Example

```bash
$ msl-validate user-api.md
Validating against: rest-api-metaspec

✓ Has required ## Endpoints section
✓ Has required ## Authentication section  
✗ Missing required ## Error Handling section
✓ Has required ## Rate Limiting section
✗ Missing OpenAPI spec reference

Compliance Score: 60/100
Required fixes:
- Add ## Error Handling section with error codes
- Add OpenAPI spec reference or inline definition

Suggestions:
- Consider adding request/response examples for each endpoint
- Specify authentication token format (JWT, OAuth2, etc.)
```

## Benefits

1. **Explicit Governance**: Clear declaration of which patterns a spec must follow
2. **Automated Validation**: Tools can validate compliance automatically
3. **Architectural Enforcement**: Ensure specs follow organizational patterns
4. **Quality Assurance**: Metaspecs can enforce quality standards
5. **Discovery**: Query which specs are governed by which metaspecs
6. **Evolution**: Version metaspecs to evolve patterns over time
7. **Composition**: Apply multiple governance patterns to a single spec

## Migration Path

### Phase 1: Documentation
- Document existing implicit metaspecs
- Identify common patterns across specifications
- Create formal metaspec documents

### Phase 2: Optional Adoption
- Add `governed-by` as optional field
- Provide validation tooling
- Generate compliance reports

### Phase 3: Enforcement
- Require `governed-by` for new specifications
- Validate in CI/CD pipelines
- Block non-compliant specifications

## Open Questions

1. Should metaspecs themselves be governed by a meta-metaspec?
2. How do we handle conflicts between multiple metaspecs?
3. Should governance be inherited through `extends` chains?
4. Do we need a registry of approved metaspecs?
5. Should metaspecs support partial compliance levels?

## Related Work

- **JSON Schema**: Uses `$schema` to point to governing schema
- **OpenAPI**: Uses `openapi: 3.0.0` to declare version compliance
- **TypeScript**: Uses `extends` in tsconfig for configuration inheritance
- **XML**: Uses DTD/XSD for document type definitions

## Conclusion

The `governed-by` field provides explicit metaspec governance for MSL specifications, enabling:
- Clear architectural patterns
- Automated compliance validation  
- Quality enforcement
- Specification discovery and organization

This complements existing MSL features (inheritance, templates) while solving a distinct need for governance and compliance.