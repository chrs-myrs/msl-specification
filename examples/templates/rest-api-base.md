---
id: rest-api-base
type: template
tags: [template, api]
variables:
  service_name: Service
  rate_limit: 100
  api_version: v1
---

# ${service_name} REST API Template

## Summary
Base template for RESTful API specifications.

## Requirements

### API Design
- REQ-001: RESTful endpoint design following REST principles
- REQ-002: JSON request/response format with Content-Type headers
- REQ-003: Rate limiting: ${rate_limit} requests per minute
- REQ-004: API versioning via URL path (/${api_version})

### HTTP Methods
- REQ-005: GET for resource retrieval (idempotent)
- REQ-006: POST for resource creation
- REQ-007: PUT for full resource updates (idempotent)
- REQ-008: PATCH for partial resource updates
- REQ-009: DELETE for resource removal (idempotent)

### Response Standards
- REQ-010: HTTP status codes follow RFC 7231
- REQ-011: Consistent error response format:
  ```json
  {
    "error": {
      "code": "ERROR_CODE",
      "message": "Human readable message",
      "details": {}
    }
  }
  ```
- REQ-012: Pagination for list endpoints using cursor or offset
- REQ-013: Filtering support via query parameters

### Security
- REQ-014: HTTPS only (TLS 1.2+)
- REQ-015: API key authentication via header
- REQ-016: Request signing for sensitive operations
- REQ-017: CORS headers for browser access

### Documentation
- REQ-018: OpenAPI 3.0 specification
- REQ-019: Interactive API documentation
- REQ-020: Code examples in multiple languages

## Notes
This template provides a foundation for RESTful APIs. Extend it and override requirements as needed for specific services.