# MSL User Guide

**Complete guide to writing, validating, and managing MSL specifications. Learn best practices, patterns, and advanced features for effective specification management.**

## Table of Contents

1. [Introduction](#introduction)
2. [Writing Your First Specification](#writing-your-first-specification)
3. [Understanding MSL Levels](#understanding-msl-levels)
4. [Structuring Requirements](#structuring-requirements)
5. [Using Inheritance](#using-inheritance)
6. [Templates and Variables](#templates-and-variables)
7. [Markers and Annotations](#markers-and-annotations)
8. [Validation and Quality](#validation-and-quality)
9. [Best Practices](#best-practices)
10. [Common Patterns](#common-patterns)
11. [Troubleshooting](#troubleshooting)
12. [Quick Reference](#quick-reference)

## Introduction

MSL (Markdown Specification Language) lets you write specifications that are both human-friendly and machine-processable. This guide covers everything from basic markdown specs to advanced inheritance patterns.

### Prerequisites

- Basic markdown knowledge
- A text editor
- (Optional) Git for version control
- (Optional) Node.js for validation tools

### Learning Paths

Choose your path based on your goals:

#### 🚀 Beginner Path (2 hours)
1. [Writing Your First Specification](#writing-your-first-specification)
2. [Understanding MSL Levels](#understanding-msl-levels) (Level 0 only)
3. [Structuring Requirements](#structuring-requirements) (Basic section)
4. [Best Practices](#best-practices) (Top 5 only)

#### 💼 Intermediate Path (4 hours)
1. Complete Beginner Path
2. [Understanding MSL Levels](#understanding-msl-levels) (All levels)
3. [Markers and Annotations](#markers-and-annotations)
4. [Validation and Quality](#validation-and-quality)
5. [Common Patterns](#common-patterns)

#### 🎯 Advanced Path (8 hours)
1. Complete Intermediate Path
2. [Using Inheritance](#using-inheritance)
3. [Templates and Variables](#templates-and-variables)
4. All best practices and patterns
5. [Troubleshooting](#troubleshooting) deep dive

## Writing Your First Specification

### Task: Create a Simple Feature Specification

**Prerequisites:** Text editor, 10 minutes

Let's specify a user login feature:

```markdown
# User Login Feature

## Summary
Allow users to authenticate with the system using credentials.

## Requirements
- Users can log in with email and password
- System shows error for invalid credentials
- Users remain logged in for 7 days
- Users can explicitly log out
```

This is valid MSL Level 0 - just markdown with a Requirements section.

### Task: Add Structure for Tracking

**Prerequisites:** Understanding of IDs, 15 minutes

Let's add structure to track individual requirements:

```markdown
---
id: user-login
version: 1.0
assignee: auth-team
---
# User Login Feature

## Summary
Authentication system for user access control.

## Requirements
- REQ-001: Users authenticate with email and password
- REQ-002: System validates credentials against user database
- REQ-003: Invalid credentials show generic error message
- REQ-004: Session persists for 7 days with remember-me option
- REQ-005: Users can explicitly terminate session via logout
```

Now you have MSL Level 1 with trackable requirements.

### DO's and DON'Ts

**DO:**
- ✅ Start with plain markdown (Level 0)
- ✅ Add structure only when needed
- ✅ Keep requirements focused and atomic

**DON'T:**
- ❌ Start with complex features
- ❌ Mix multiple concerns in one requirement
- ❌ Add IDs before you need tracking

## Understanding MSL Levels

### Level Selection Decision Tree

```
Do you need requirement tracking?
├─ No → Use Level 0 (pure markdown)
└─ Yes → Do you need inheritance?
    ├─ No → Use Level 1 (structured)
    └─ Yes → Use Level 2 (advanced)
```

### Level 0: Foundation (Pure Markdown)

**Use Cases:**
- Quick brainstorming
- Early project phases
- Simple documentation
- Personal notes

**Example: API Endpoint Sketch**
```markdown
# Payment API

## Requirements
- Process credit card payments
- Support refunds within 30 days  
- Generate receipts for all transactions
- Handle multiple currencies
```

**Example: Bug Fix Specification**
```markdown
# Fix Login Timeout Issue

## Requirements
- Extend session timeout to 30 minutes
- Show warning before timeout
- Allow session extension without re-login
```

### Level 1: Structure (IDs and Metadata)

**Use Cases:**
- Team collaboration
- Requirement tracking
- Change management
- Compliance documentation

**Example: Database Schema**
```markdown
---
id: user-database
version: 2.0
tags: [database, postgresql, users]
---
# User Database Schema

## Requirements
- REQ-001: Users table contains email, hashed password, created_at
- REQ-002: Email must be unique across all users
- REQ-003: Passwords use bcrypt with cost factor 12
- REQ-004: Soft deletes via deleted_at timestamp
```

**Example: Microservice Contract**
```markdown
---
id: order-service
version: 1.0
assignee: platform-team
priority: high
---
# Order Service API

## Requirements
- REQ-001: POST /orders creates new order with items array
- REQ-002: GET /orders/{id} returns order details
- REQ-003: All endpoints require JWT authentication
- REQ-004: Responses use JSON with standard error format
```

### Level 2: Advanced (Inheritance and Templates)

**Use Cases:**
- Product families
- Multi-tenant systems
- Regulatory compliance
- Platform variations

**Example: Mobile App Variants**
```markdown
---
id: mobile-app-pro
extends: mobile-app-basic
---
# Professional Mobile App

## Requirements
- REQ-001: [OVERRIDE] Support unlimited data storage
- REQ-010: [NEW] Advanced analytics dashboard
- REQ-011: [NEW] API access for integrations
```

**Example: Regional Compliance**
```markdown
---
id: payment-eu
extends: payment-global
variables:
  region: EU
  currency: EUR
---
# EU Payment Processing

## Requirements
- REQ-001: [OVERRIDE] Comply with PSD2 regulations
- REQ-020: [NEW] Support SEPA transfers
- REQ-021: [NEW] GDPR-compliant data handling
```

## Structuring Requirements

### Basic Requirement Structure

Every requirement should be:
- **Atomic**: One testable behavior
- **Clear**: Unambiguous meaning
- **Measurable**: Pass/fail criteria

**Example: Well-Structured Requirements**
```markdown
## Requirements

### Authentication
- REQ-001: System authenticates users via OAuth 2.0
- REQ-002: Failed authentication returns 401 status code
- REQ-003: Token expires after 1 hour of inactivity

### Authorization  
- REQ-010: System checks user permissions before resource access
- REQ-011: Missing permissions return 403 status code
- REQ-012: Permission changes take effect within 5 seconds
```

### Grouping Related Requirements

Use subsections for logical grouping:

```markdown
## Requirements

### User Management
- REQ-100: Admins can create user accounts
- REQ-101: Users receive email confirmation on creation
- REQ-102: Unconfirmed accounts expire after 7 days

### Security
- REQ-200: Passwords require minimum 12 characters
- REQ-201: System enforces 2FA for admin accounts
- REQ-202: Failed login attempts lock account after 5 tries

### Performance
- REQ-300: Login completes within 2 seconds
- REQ-301: System supports 1000 concurrent users
- REQ-302: Database queries execute within 100ms
```

### Requirement ID Patterns

Use consistent, meaningful ID patterns:

```markdown
## Requirements

# Category-based IDs
- AUTH-001: Authentication requirement
- AUTHZ-001: Authorization requirement
- PERF-001: Performance requirement

# Numbered sequences
- REQ-001-099: Core functionality
- REQ-100-199: Security requirements
- REQ-200-299: Performance requirements

# Hierarchical IDs
- REQ-001: Main requirement
- REQ-001.1: Sub-requirement
- REQ-001.1.1: Detailed requirement
```

## Using Inheritance

### The "IS-A" Rule

**Critical**: Only use `extends` when there's a true "IS-A" relationship.

✅ **CORRECT Inheritance:**
```markdown
---
id: admin-user
extends: basic-user
---
# Admin IS-A User (with additional privileges)
```

❌ **INCORRECT Inheritance:**
```markdown
---
id: login-documentation
extends: user-guide  
---
# Login docs are NOT a type of user guide
```

### Inheritance Patterns

**Pattern 1: Product Tiers**
```markdown
# base-plan.md
---
id: base-plan
---
## Requirements
- REQ-001: 10GB storage
- REQ-002: Email support
- REQ-003: Basic analytics

# pro-plan.md  
---
id: pro-plan
extends: base-plan
---
## Requirements
- REQ-001: [OVERRIDE] 100GB storage
- REQ-004: [NEW] Priority support
- REQ-005: [NEW] Advanced analytics
```

**Pattern 2: Platform Variants**
```markdown
# app-core.md
---
id: app-core
---
## Requirements
- REQ-001: User authentication
- REQ-002: Data synchronization
- REQ-003: Offline mode

# app-ios.md
---
id: app-ios
extends: app-core
---
## Requirements
- REQ-010: [NEW] Face ID authentication
- REQ-011: [NEW] iOS widget support
- REQ-012: [NEW] Apple Pay integration
```

### Override and Extension Semantics

Use clear markers for requirement changes:

```markdown
## Requirements

# Overriding parent requirements
- REQ-001: [OVERRIDE] New behavior replaces parent's REQ-001
- REQ-001: [override] Alternative syntax (lowercase)

# Adding new requirements
- REQ-100: [NEW] Additional requirement not in parent
- REQ-100: [new] Alternative syntax (lowercase)

# Deprecating requirements
- REQ-050: [DEPRECATED] Will be removed in v2.0
- REQ-050: [REMOVED] No longer applicable
```

## Templates and Variables

### Creating Reusable Templates

Templates use variables for customization:

```markdown
---
id: api-service-template
type: template
variables:
  service_name: "Service Name"
  port: 8080
  auth_method: "JWT"
---
# {{service_name}} API

## Requirements
- REQ-001: Service runs on port {{port}}
- REQ-002: Authentication via {{auth_method}}
- REQ-003: Health check at /health endpoint
- REQ-004: Structured JSON logging
```

### Using Templates

Instantiate templates with specific values:

```markdown
---
id: user-service
extends: api-service-template
variables:
  service_name: "User Management"
  port: 8081
  auth_method: "OAuth 2.0"
---
# User Management Service

## Requirements
- REQ-010: [NEW] CRUD operations for users
- REQ-011: [NEW] Role-based permissions
```

### Variable Patterns

**Pattern 1: Configuration Variables**
```markdown
---
variables:
  max_file_size: "10MB"
  timeout_seconds: 30
  retry_count: 3
---
## Requirements
- REQ-001: Files must be ≤ {{max_file_size}}
- REQ-002: Requests timeout after {{timeout_seconds}} seconds
- REQ-003: Failed requests retry {{retry_count}} times
```

**Pattern 2: Environment Variables**
```markdown
---
variables:
  environment: "production"
  region: "us-east-1"
  log_level: "info"
---
## Requirements
- REQ-001: Deploy to {{environment}} environment
- REQ-002: Host in {{region}} region
- REQ-003: Set logging to {{log_level}} level
```

## Markers and Annotations

### Priority Markers

Indicate requirement importance:

```markdown
## Requirements
- REQ-001: [!] Critical security requirement
- REQ-002: [!!] Blocker - must have for launch
- REQ-003: Standard priority (no marker)
- REQ-004: [?] Nice to have, optional feature
```

### Assignment Markers

Track responsibility:

```markdown
## Requirements
- REQ-001: [@backend] API endpoint implementation
- REQ-002: [@frontend] UI component development
- REQ-003: [@qa] Test case creation
- REQ-004: [@devops] Deployment configuration
```

### Status Markers

Track implementation state:

```markdown
## Requirements
- REQ-001: [✓] Completed requirement
- REQ-002: [⚠] In progress with issues
- REQ-003: [✗] Blocked by dependencies
- REQ-004: [→] Deferred to next release
```

### Tag Markers

Categorize requirements:

```markdown
## Requirements
- REQ-001: [#security] Encryption requirement
- REQ-002: [#performance] [#critical] Response time requirement
- REQ-003: [#ux] [#accessibility] Screen reader support
- REQ-004: [#compliance] [#gdpr] Data retention policy
```

### Combining Markers

Use multiple markers for rich annotations:

```markdown
## Requirements
- REQ-001: [!] [@backend] [#security] [✓] Implement JWT authentication
- REQ-002: [!!] [@frontend] [#ux] [⚠] Responsive design for mobile
- REQ-003: [@qa] [#testing] [→] Automated regression tests
```

## Validation and Quality

### Quality Metrics

MSL validation checks these dimensions:

**1. DRY Compliance (Don't Repeat Yourself)**
- Score: 0-100 (target ≥85)
- Measures: Text duplication across requirements
- Fix: Extract common patterns to templates

**2. Requirement Testability**
- Score: Percentage of testable requirements
- Target: ≥90% have clear pass/fail criteria
- Fix: Add measurable criteria to vague requirements

**3. Architectural Cohesion**
- Score: How well requirements relate to spec purpose
- Target: ≥80 cohesion score
- Fix: Move unrelated requirements to separate specs

**4. Specification Coupling**
- Score: Dependencies between specifications
- Target: ≤3 levels of inheritance depth
- Fix: Flatten deep hierarchies

### Running Validation

**Command Line Validation:**
```bash
# Validate single file
msl-validate spec.md

# Validate with detailed report
msl-validate spec.md --verbose

# Validate directory recursively
msl-validate ./specs --recursive

# Check specific quality threshold
msl-validate spec.md --min-score 80
```

**Validation Output Example:**
```
Validating: user-auth.md
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Overall Score: 82/100 ✓

Quality Breakdown:
├─ DRY Compliance: 88/100 ✓
├─ Testability: 75/100 ⚠
├─ Cohesion: 90/100 ✓
└─ Coupling: 85/100 ✓

Issues Found (3):
⚠ REQ-002: Missing measurable criteria
⚠ REQ-005: Duplicate text with REQ-003
⚠ REQ-008: Ambiguous term "quickly"

Recommendations:
1. Add timeout value to REQ-002
2. Extract common text to template
3. Replace "quickly" with "within 2 seconds"
```

### Improving Quality Scores

**Before (Low Quality):**
```markdown
- REQ-001: System should be fast
- REQ-002: Good user experience
- REQ-003: Handle errors appropriately
```

**After (High Quality):**
```markdown
- REQ-001: API responds within 200ms for 95th percentile
- REQ-002: UI provides feedback within 100ms of user action
- REQ-003: Errors display user-friendly message with recovery action
```

## Best Practices

### Top 10 MSL Best Practices

1. **Start Simple**: Begin with Level 0, add complexity when needed
2. **One Requirement, One Test**: Each requirement should map to one test
3. **Use Consistent IDs**: Pick a pattern and stick to it
4. **Avoid Deep Inheritance**: Maximum 3 levels deep
5. **Name Files Clearly**: Use `feature-name.md` (lowercase-kebab-case)
6. **Group Related Requirements**: Use sections for organization
7. **Version Important Specs**: Track changes with version numbers
8. **Validate Regularly**: Check quality before committing
9. **Document Assumptions**: State what you're NOT specifying
10. **Review Like Code**: Specifications need peer review

### DO's and DON'Ts by Feature

**Writing Requirements:**

DO:
- ✅ Write atomic, testable requirements
- ✅ Use active voice ("System sends email")

DON'T:
- ❌ Combine multiple behaviors in one requirement
- ❌ Use passive voice ("Email is sent")

**Using Inheritance:**

DO:
- ✅ Verify true "IS-A" relationship
- ✅ Document why inheritance is used

DON'T:
- ❌ Use extends for organizational grouping
- ❌ Create inheritance chains > 3 levels

**File Organization:**

DO:
- ✅ One specification per file
- ✅ Group related specs in folders

DON'T:
- ❌ Mix multiple features in one spec
- ❌ Create deeply nested folder structures

**Validation:**

DO:
- ✅ Run validation before committing
- ✅ Fix critical issues immediately

DON'T:
- ❌ Ignore validation warnings
- ❌ Accept scores below 80/100

**Templates:**

DO:
- ✅ Create templates for repeated patterns
- ✅ Document template variables

DON'T:
- ❌ Over-engineer templates
- ❌ Use templates for one-off specs

## Common Patterns

### Pattern 1: API Specification

**Use Case:** RESTful service documentation

```markdown
---
id: user-api
version: 2.0
tags: [api, rest, users]
---
# User Management API

## Summary
RESTful API for user CRUD operations.

## Requirements

### Endpoints
- REQ-001: GET /users - List all users (paginated)
- REQ-002: GET /users/{id} - Get single user
- REQ-003: POST /users - Create new user
- REQ-004: PUT /users/{id} - Update user
- REQ-005: DELETE /users/{id} - Delete user

### Authentication
- REQ-010: All endpoints require Bearer token
- REQ-011: Tokens expire after 1 hour
- REQ-012: 401 response for invalid tokens

### Response Format
- REQ-020: Success responses use 2xx codes
- REQ-021: Errors include message and code
- REQ-022: All responses use JSON format
```

### Pattern 2: Database Schema

**Use Case:** Table structure documentation

```markdown
---
id: user-schema
version: 1.0
tags: [database, postgresql]
---
# User Database Schema

## Requirements

### Table Structure
- REQ-001: users table with id, email, password_hash
- REQ-002: id is UUID primary key
- REQ-003: email has unique constraint
- REQ-004: created_at and updated_at timestamps

### Relationships
- REQ-010: users.id foreign key to profiles.user_id
- REQ-011: users.id foreign key to sessions.user_id
- REQ-012: Cascade delete for dependent records

### Indexes
- REQ-020: Index on email for login queries
- REQ-021: Index on created_at for sorting
- REQ-022: Composite index on (email, deleted_at)
```

### Pattern 3: UI Component

**Use Case:** Frontend component behavior

```markdown
---
id: login-form
version: 1.0
tags: [ui, component, authentication]
---
# Login Form Component

## Requirements

### Visual Design
- REQ-001: Email and password input fields
- REQ-002: "Remember me" checkbox
- REQ-003: Submit button disabled until valid input

### Validation
- REQ-010: Email format validation on blur
- REQ-011: Password minimum 8 characters
- REQ-012: Show inline error messages

### Behavior
- REQ-020: Submit triggers authentication API
- REQ-021: Show loading state during submission
- REQ-022: Redirect to dashboard on success
- REQ-023: Display API error messages
```

### Pattern 4: Microservice Contract

**Use Case:** Service communication specification

```markdown
---
id: order-service-contract
version: 1.0
tags: [microservice, contract]
---
# Order Service Contract

## Requirements

### Commands (Incoming)
- REQ-001: CreateOrder with items, user_id, address
- REQ-002: CancelOrder with order_id, reason
- REQ-003: UpdateShipping with order_id, address

### Events (Outgoing)
- REQ-010: OrderCreated with full order details
- REQ-011: OrderCancelled with order_id, timestamp
- REQ-012: ShippingUpdated with tracking info

### Queries
- REQ-020: GetOrder by order_id returns full details
- REQ-021: ListOrders by user_id with pagination
- REQ-022: SearchOrders by status, date range
```

### Pattern 5: Configuration Specification

**Use Case:** Application configuration requirements

```markdown
---
id: app-config
version: 1.0
tags: [configuration, deployment]
---
# Application Configuration

## Requirements

### Environment Variables
- REQ-001: DATABASE_URL for PostgreSQL connection
- REQ-002: REDIS_URL for cache connection
- REQ-003: JWT_SECRET for token signing
- REQ-004: LOG_LEVEL (debug|info|warn|error)

### Feature Flags
- REQ-010: NEW_DASHBOARD toggles UI redesign
- REQ-011: BATCH_PROCESSING enables job queue
- REQ-012: MAINTENANCE_MODE shows downtime page

### Limits
- REQ-020: MAX_UPLOAD_SIZE default 10MB
- REQ-021: SESSION_TIMEOUT default 30 minutes
- REQ-022: RATE_LIMIT default 100 req/min
```

## Troubleshooting

### Common Issues and Solutions

**Issue 1: Validation fails with "No Requirements section"**

*Symptom:* Valid markdown but MSL validation fails

*Solution:* Ensure you have `## Requirements` (with capital R):
```markdown
# Wrong
## requirements
## Requirement
## Requirements:

# Correct
## Requirements
```

**Issue 2: Inheritance not working as expected**

*Symptom:* Parent requirements not appearing in child spec

*Solution:* Check the inheritance chain:
```bash
# Validate parent exists
ls parent-spec.md

# Check extends syntax
grep "extends:" child-spec.md

# Validate both files
msl-validate parent-spec.md child-spec.md
```

**Issue 3: High DRY violation score**

*Symptom:* Validation shows duplicate text warnings

*Solution:* Extract common patterns:
```markdown
# Before (duplication)
- REQ-001: API returns JSON with status and data
- REQ-002: API returns JSON with status and error
- REQ-003: API returns JSON with status and message

# After (using template)
---
variables:
  response_format: "JSON with status and"
---
- REQ-001: API returns {{response_format}} data
- REQ-002: API returns {{response_format}} error
- REQ-003: API returns {{response_format}} message
```

**Issue 4: Requirements not testable**

*Symptom:* Low testability score

*Solution:* Add measurable criteria:
```markdown
# Before (not testable)
- REQ-001: System should be fast
- REQ-002: Good error handling

# After (testable)
- REQ-001: System responds within 500ms
- REQ-002: Errors return HTTP status and message
```

**Issue 5: Circular inheritance detected**

*Symptom:* Validation error about circular references

*Solution:* Review and fix inheritance chain:
```markdown
# Wrong (circular)
# a.md extends b.md
# b.md extends c.md
# c.md extends a.md  ← Circular!

# Correct (linear)
# base.md (no extends)
# a.md extends base.md
# b.md extends a.md
```

**Issue 6: Variables not substituting**

*Symptom:* See `{{variable}}` in output

*Solution:* Define variables in frontmatter:
```markdown
---
id: my-spec
variables:
  missing_var: "value here"
---
```

**Issue 7: Override not working**

*Symptom:* Parent requirement still appears

*Solution:* Use same REQ-ID as parent:
```markdown
# Parent spec
- REQ-001: Original requirement

# Child spec (correct)
- REQ-001: [OVERRIDE] New requirement

# Child spec (wrong - different ID)
- REQ-999: [OVERRIDE] Won't override REQ-001
```

**Issue 8: Specification too complex**

*Symptom:* Hard to understand, low cohesion score

*Solution:* Split into multiple specs:
```markdown
# Before (mixed concerns)
# payment-system.md with 100+ requirements

# After (separated)
# payment-api.md (30 requirements)
# payment-database.md (20 requirements)
# payment-ui.md (25 requirements)
# payment-integration.md (25 requirements)
```

**Issue 9: Level confusion**

*Symptom:* Using L2 features in L0 spec

*Solution:* Declare correct level:
```markdown
---
msl: L2  # Must declare L2 for inheritance
extends: parent-spec
---
```

**Issue 10: Git merge conflicts in specs**

*Symptom:* Conflicting requirement IDs

*Solution:* Use ranges for different contributors:
```markdown
# Developer A uses REQ-001 to REQ-099
# Developer B uses REQ-100 to REQ-199
# Developer C uses REQ-200 to REQ-299
```

## Quick Reference

### MSL Levels at a Glance

| Feature | Level 0 | Level 1 | Level 2 |
|---------|---------|---------|---------|
| Markdown | ✅ | ✅ | ✅ |
| Requirements section | ✅ | ✅ | ✅ |
| Frontmatter | ❌ | ✅ | ✅ |
| Requirement IDs | ❌ | ✅ | ✅ |
| Inheritance | ❌ | ❌ | ✅ |
| Templates | ❌ | ❌ | ✅ |
| Variables | ❌ | ❌ | ✅ |

### Common Markers

| Marker | Meaning | Example |
|--------|---------|---------|
| `[!]` | High priority | `REQ-001: [!] Critical feature` |
| `[@user]` | Assignment | `REQ-002: [@alice] Implement API` |
| `[#tag]` | Category | `REQ-003: [#security] Encrypt data` |
| `[OVERRIDE]` | Replace parent | `REQ-001: [OVERRIDE] New behavior` |
| `[NEW]` | Addition | `REQ-100: [NEW] Extra feature` |
| `[✓]` | Complete | `REQ-004: [✓] Implemented` |

### File Naming Conventions

| Type | Pattern | Example |
|------|---------|---------|
| Feature | `feature-name.md` | `user-auth.md` |
| API | `service-api.md` | `payment-api.md` |
| Schema | `table-schema.md` | `user-schema.md` |
| Template | `type-template.md` | `api-template.md` |
| Version | `feature-v2.md` | `auth-v2.md` |

### Validation Commands

```bash
# Basic validation
msl-validate spec.md

# Validate directory
msl-validate ./specs/

# Set quality threshold
msl-validate spec.md --min-score 80

# Output format
msl-validate spec.md --format json

# Check specific rules
msl-validate spec.md --rules dry,testability

# Fix common issues
msl-validate spec.md --fix
```

### Inheritance Checklist

Before using `extends`:
- [ ] Is there a true "IS-A" relationship?
- [ ] Would composition be better than inheritance?
- [ ] Is inheritance depth ≤ 3 levels?
- [ ] Are you overriding for specialization (not organization)?
- [ ] Have you documented the inheritance reason?

## Glossary

**MSL Terms:**

- **Atomic Requirement**: Single, testable behavior
- **Cohesion**: How well requirements relate to specification purpose
- **Coupling**: Dependencies between specifications
- **DRY**: Don't Repeat Yourself principle
- **Extension**: Adding new requirements via inheritance
- **Frontmatter**: YAML metadata at document start
- **Inheritance**: Deriving from parent specification
- **Level**: MSL complexity tier (0, 1, or 2)
- **Marker**: Special annotation like `[!]` or `[@user]`
- **Override**: Replacing parent requirement in child
- **Requirement**: Testable specification statement
- **Template**: Reusable specification with variables
- **Testability**: Whether requirement has clear pass/fail criteria
- **Validation**: Quality checking of specifications
- **Variable**: Placeholder for template customization

---

**Ready to write better specifications?** Start with [Getting Started](getting-started.md) or explore [Tutorials](tutorials/) for hands-on learning.

For complete language details, see the [Reference](reference.md). For tool usage, check the [Tools Guide](tools.md).