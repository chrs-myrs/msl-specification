# Tutorial: Creating Templates

**Time:** 20 minutes  
**Level:** Intermediate-Advanced  
**Outcome:** Build reusable specification patterns with variables

## Learning Objectives

By completing this tutorial, you will:

✅ **Create** reusable templates with variables  
✅ **Extract** common patterns from specifications  
✅ **Instantiate** templates for specific use cases  

## Prerequisites

- Completed [Using Inheritance](inheritance.md)
- Understanding of MSL Level 2 features
- Multiple similar specifications to refactor

## The Scenario

You're building microservices. Each service has similar structure: API endpoints, database, authentication. Instead of copying specifications, you'll create a template that all services can use.

## Step-by-Step Instructions

### Step 1: Identify Template Candidates

**Objective:** Find repeated patterns  
**Action:** Review existing specifications

Look for specifications with:
- Similar structure
- Repeated requirements
- Only minor variations

Example pattern in multiple services:
```markdown
# User Service
- REQ-001: Service runs on port 8081
- REQ-002: Authenticate with JWT tokens
- REQ-003: Connect to PostgreSQL database
- REQ-004: Health check at /health endpoint

# Order Service  
- REQ-001: Service runs on port 8082
- REQ-002: Authenticate with JWT tokens
- REQ-003: Connect to PostgreSQL database
- REQ-004: Health check at /health endpoint

# Product Service
- REQ-001: Service runs on port 8083
- REQ-002: Authenticate with JWT tokens
- REQ-003: Connect to PostgreSQL database
- REQ-004: Health check at /health endpoint
```

**Pattern Found:** Only the port number changes!

### Step 2: Create Template Specification

**Objective:** Build reusable template  
**Action:** Create microservice-template.md

```markdown
---
id: microservice-template
type: template
variables:
  service_name: "Microservice"
  port: 8080
  database: "PostgreSQL"
  auth_method: "JWT"
---
# {{service_name}} Service

## Summary
{{service_name}} microservice with standard infrastructure requirements.

## Requirements

### Service Configuration
- REQ-001: Service runs on port {{port}}
- REQ-002: Service exposes health check at /health endpoint
- REQ-003: Service implements graceful shutdown on SIGTERM

### Authentication & Authorization  
- REQ-004: Service authenticates requests using {{auth_method}} tokens
- REQ-005: Service validates token expiration and signature
- REQ-006: Service returns 401 for invalid authentication

### Database
- REQ-007: Service connects to {{database}} database
- REQ-008: Service uses connection pooling (min: 5, max: 20)
- REQ-009: Service implements retry logic for transient failures

### API Standards
- REQ-010: Service returns JSON responses
- REQ-011: Service uses RESTful URL patterns
- REQ-012: Service implements pagination for list endpoints
```

**Key Elements:**
- `type: template` marks this as a template
- `variables` section defines placeholders
- `{{variable}}` syntax for substitution

### Step 3: Use Template in Child Specification

**Objective:** Create specific service from template  
**Action:** Create user-service.md using template

```markdown
---
id: user-service
extends: microservice-template
variables:
  service_name: "User Management"
  port: 8081
  database: "PostgreSQL"
  auth_method: "OAuth 2.0"
---
# User Management Service

## Requirements

### Additional User Service Requirements
- REQ-020: [NEW] Service provides CRUD operations for users
- REQ-021: [NEW] Service hashes passwords using bcrypt
- REQ-022: [NEW] Service enforces unique email addresses
- REQ-023: [NEW] Service supports user role management
```

**Result:** User service has all template requirements with variables replaced, plus new user-specific requirements

### Step 4: Verify Variable Substitution

**Objective:** Ensure template variables work  
**Action:** Validate and view expanded specification

```bash
msl-validate user-service.md --expand
```

**Expected Output (Expanded):**
```markdown
# User Management Service

## Requirements

### Service Configuration
- REQ-001: Service runs on port 8081
- REQ-002: Service exposes health check at /health endpoint
- REQ-003: Service implements graceful shutdown on SIGTERM

### Authentication & Authorization
- REQ-004: Service authenticates requests using OAuth 2.0 tokens
- REQ-005: Service validates token expiration and signature
- REQ-006: Service returns 401 for invalid authentication

### Database
- REQ-007: Service connects to PostgreSQL database
- REQ-008: Service uses connection pooling (min: 5, max: 20)
- REQ-009: Service implements retry logic for transient failures

[... plus new requirements]
```

### Step 5: Create Multiple Services from Template

**Objective:** Demonstrate template reusability  
**Action:** Create order and product services

**order-service.md:**
```markdown
---
id: order-service
extends: microservice-template
variables:
  service_name: "Order Processing"
  port: 8082
  database: "PostgreSQL"
  auth_method: "JWT"
---
# Order Processing Service

## Requirements

### Order-Specific Requirements
- REQ-020: [NEW] Service creates orders with items and quantities
- REQ-021: [NEW] Service calculates order totals and taxes
- REQ-022: [NEW] Service integrates with payment gateway
- REQ-023: [NEW] Service sends order confirmation emails
```

**product-service.md:**
```markdown
---
id: product-service
extends: microservice-template
variables:
  service_name: "Product Catalog"
  port: 8083
  database: "MongoDB"  # Different database!
  auth_method: "API Key"
---
# Product Catalog Service

## Requirements

### Product-Specific Requirements
- REQ-020: [NEW] Service manages product inventory
- REQ-021: [NEW] Service supports product categories
- REQ-022: [NEW] Service handles product images
- REQ-023: [NEW] Service implements full-text search
```

### Step 6: Advanced Template with Conditionals

**Objective:** Create flexible template  
**Action:** Add optional sections to template

```markdown
---
id: microservice-template-v2
type: template
variables:
  service_name: "Microservice"
  port: 8080
  database: "PostgreSQL"
  auth_method: "JWT"
  enable_caching: false
  cache_type: "Redis"
  enable_messaging: false
  message_broker: "RabbitMQ"
---
# {{service_name}} Service

## Requirements

### Service Configuration
- REQ-001: Service runs on port {{port}}
- REQ-002: Service exposes health check at /health endpoint

### Authentication & Authorization
- REQ-004: Service authenticates using {{auth_method}}

### Database
- REQ-007: Service connects to {{database}} database

{{#if enable_caching}}
### Caching
- REQ-030: Service uses {{cache_type}} for caching
- REQ-031: Service implements cache TTL of 5 minutes
- REQ-032: Service invalidates cache on updates
{{/if}}

{{#if enable_messaging}}
### Message Queue
- REQ-040: Service publishes events to {{message_broker}}
- REQ-041: Service implements retry with exponential backoff
- REQ-042: Service handles poison messages
{{/if}}
```

### Step 7: Extract Template from Existing Specs

**Objective:** Refactor existing specifications  
**Action:** Identify and extract common patterns

Given these existing specs:
```markdown
# API Gateway
- REQ-001: Rate limit: 100 requests per minute per IP
- REQ-002: CORS headers for browser requests
- REQ-003: Request logging with correlation IDs
- REQ-004: Circuit breaker for downstream services

# Payment API
- REQ-001: Rate limit: 100 requests per minute per IP
- REQ-002: CORS headers for browser requests  
- REQ-003: Request logging with correlation IDs
- REQ-004: Circuit breaker for downstream services
- REQ-005: PCI compliance logging

# Search API
- REQ-001: Rate limit: 1000 requests per minute per IP  # Different!
- REQ-002: CORS headers for browser requests
- REQ-003: Request logging with correlation IDs
- REQ-004: Circuit breaker for downstream services
- REQ-005: Elasticsearch integration
```

Extract to template:
```markdown
---
id: api-gateway-template
type: template
variables:
  api_name: "API"
  rate_limit: 100
---
# {{api_name}}

## Requirements

### Common API Requirements
- REQ-001: Rate limit: {{rate_limit}} requests per minute per IP
- REQ-002: CORS headers for browser requests
- REQ-003: Request logging with correlation IDs
- REQ-004: Circuit breaker for downstream services
```

### Step 8: Template Composition

**Objective:** Combine multiple templates  
**Action:** Create specification using multiple templates

```markdown
---
id: payment-service-complete
extends: microservice-template
includes:
  - api-gateway-template
  - security-template
variables:
  service_name: "Payment Processing"
  port: 8084
  database: "PostgreSQL"
  auth_method: "OAuth 2.0"
  rate_limit: 50  # Stricter for payments
---
# Payment Processing Service

## Requirements
[Inherits from all templates plus:]

### Payment-Specific
- REQ-100: [NEW] Process credit card payments via Stripe
- REQ-101: [NEW] Implement PCI compliance requirements
```

### Step 9: Validate Template Usage

**Objective:** Ensure correct template application  
**Action:** Check all services using template

```bash
# Find all specs using the template
grep -r "extends: microservice-template" *.md

# Validate all at once
msl-validate *.md --check-templates
```

**Expected Output:**
```
Template Usage Analysis:

microservice-template:
  Used by: 5 specifications
  - user-service.md ✓
  - order-service.md ✓
  - product-service.md ✓
  - payment-service.md ✓
  - notification-service.md ✓
  
All variable substitutions valid ✓
No undefined variables ✓
```

### Step 10: Generate Services with AI

**Objective:** Use templates with AI implementation  
**Action:** Give AI template and instance

```markdown
"Please implement the User Service based on these specifications:

1. TEMPLATE (microservice-template.md):
[Paste template]

2. SERVICE SPECIFICATION (user-service.md):
---
extends: microservice-template
variables:
  service_name: "User Management"
  port: 8081
  database: "PostgreSQL"  
  auth_method: "OAuth 2.0"
---

Additional Requirements:
- REQ-020: Service provides CRUD operations for users
- REQ-021: Service hashes passwords using bcrypt

Implement complete service with all template requirements applied."
```

**AI Result:** Complete service implementation with all template patterns

## Complete Template Example

Here's a production-ready template:

```markdown
---
id: rest-api-template
type: template
variables:
  api_name: "REST API"
  version: "v1"
  port: 3000
  auth_type: "Bearer Token"
  rate_limit_rpm: 600
  response_format: "JSON"
  enable_pagination: true
  page_size: 20
  enable_filtering: true
  enable_sorting: true
  enable_versioning: true
---
# {{api_name}} {{version}}

## Summary
RESTful API service implementing {{api_name}} with standard patterns.

## Requirements

### API Configuration
- REQ-001: API runs on port {{port}}
- REQ-002: API version {{version}} accessible at /{{version}}/
- REQ-003: API returns {{response_format}} responses

### Authentication & Security
- REQ-010: API requires {{auth_type}} authentication
- REQ-011: API rate limits to {{rate_limit_rpm}} requests/minute
- REQ-012: API implements CORS for browser access
- REQ-013: API sanitizes all input to prevent injection

### Standard Endpoints
- REQ-020: GET /{{version}}/health returns service status
- REQ-021: GET /{{version}}/info returns API metadata
- REQ-022: OPTIONS requests return allowed methods

{{#if enable_pagination}}
### Pagination
- REQ-030: List endpoints support ?page and ?limit parameters
- REQ-031: Default page size is {{page_size}} items
- REQ-032: Response includes total count and page metadata
{{/if}}

{{#if enable_filtering}}
### Filtering
- REQ-040: List endpoints support field-based filtering
- REQ-041: Filters use query parameters: ?field=value
- REQ-042: Multiple filters combine with AND logic
{{/if}}

{{#if enable_sorting}}  
### Sorting
- REQ-050: List endpoints support ?sort parameter
- REQ-051: Sort format: ?sort=field:asc or field:desc
- REQ-052: Multiple sort fields supported
{{/if}}

### Error Handling
- REQ-060: Errors return appropriate HTTP status codes
- REQ-061: Error responses include code, message, details
- REQ-062: Validation errors list all field issues

### Performance
- REQ-070: API responds within 200ms for 95th percentile
- REQ-071: API handles 100 concurrent connections
- REQ-072: API implements request timeout of 30 seconds
```

## Verification

Your template is successful when:

✅ Common patterns extracted into template  
✅ Variables defined for all variations  
✅ Child specs only contain unique requirements  
✅ Template reused by multiple specifications  
✅ Variable substitution works correctly  

## Common Pitfalls

### Pitfall 1: Over-Templating
❌ **Wrong:** Creating templates for one-off specs  
✅ **Right:** Templates for 3+ similar specifications

### Pitfall 2: Too Many Variables
❌ **Wrong:** 20+ variables in one template  
✅ **Right:** 5-10 essential variables

### Pitfall 3: Implementation in Template
❌ **Wrong:** Including technology choices  
✅ **Right:** Behavior-only requirements

### Pitfall 4: No Default Values
❌ **Wrong:** All variables required  
✅ **Right:** Sensible defaults provided

### Pitfall 5: Complex Conditionals
❌ **Wrong:** Nested if/else logic  
✅ **Right:** Simple optional sections

## Next Steps

Excellent! You've mastered templates:
- Creating reusable patterns
- Using variables effectively
- Extracting from existing specs

**Continue learning:**

1. [**Building Specification Sets**](spec-sets.md) - Architect systems with templates
2. [**Team Collaboration**](team-specs.md) - Share templates across teams
3. [**CI/CD Integration**](cicd.md) - Validate template usage

**Challenge:** Create a complete microservices architecture:
1. Create templates for different service types
2. Generate 10 service specifications
3. Have AI implement one service
4. Verify template consistency

---

**Pro Tip:** Good templates are discovered, not designed. Extract them from real specifications after you see patterns emerge.