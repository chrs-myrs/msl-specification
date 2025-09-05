# MSL User Guide

**Complete guide to writing, validating, and managing MSL specifications. Learn best practices, patterns, and advanced features for effective specification management.**

## Table of Contents

1. [Introduction](#introduction)
2. [Writing Your First Specification](#writing-your-first-specification)
3. [Understanding MSL Levels](#understanding-msl-levels)
4. [Structuring Requirements](#structuring-requirements)
5. [Project Organization](#project-organization)
6. [Tool and Script Integration](#tool-and-script-integration)
7. [Using Inheritance](#using-inheritance)
8. [Markers and Annotations](#markers-and-annotations)
9. [Validation and Quality](#validation-and-quality)
10. [Best Practices](#best-practices)
11. [Common Patterns](#common-patterns)
12. [Troubleshooting](#troubleshooting)
13. [Quick Reference](#quick-reference)
14. [Advanced Topics](#advanced-topics)

## Introduction

MSL (Markdown Specification Language) lets you write specifications that are both human-friendly and machine-processable. This guide covers everything from basic markdown specs to advanced inheritance patterns.

> **💡 Key Insight:** 99% of users just need regular specifications. MSL is simple markdown with a Requirements section. Start there, add complexity only when needed.

### Quick Setup for AI-Assisted Development

If you're using Claude or other AI assistants with MCP support, add this to your personal configuration (e.g., in your CLAUDE.md or user-level memory):

```markdown
## My Development Preferences
- When I mention MSL, refer to https://github.com/chrs-myrs/msl-specification via context7 MCP
- Use MSL format for specifications: markdown with a ## Requirements section
- Keep specs alongside implementations (e.g., script.py and script-spec.md)
```

This enables you to simply say "write an MSL spec for this" in any project, and your AI assistant will know exactly what you mean.

### Prerequisites

- Basic markdown knowledge
- A text editor
- (Optional) Git for version control
- (Optional) Node.js for validation tools

### Learning Paths

Choose your path based on your goals:

#### 🚀 Quick Start (30 minutes)
1. [Writing Your First Specification](#writing-your-first-specification)
2. [Project Organization](#project-organization)
3. [Tool and Script Integration](#tool-and-script-integration)

#### 📋 Full Guide (2 hours)
1. Complete Quick Start
2. [Understanding MSL Levels](#understanding-msl-levels)
3. [Markers and Annotations](#markers-and-annotations)
4. [Validation and Quality](#validation-and-quality)
5. [Best Practices](#best-practices)

#### 🎯 Advanced Path (8 hours)
1. Complete Intermediate Path
2. [Using Inheritance](#using-inheritance)
3. [Templates and Variables](#templates-and-variables)
4. [Metaspecs and Governance](#metaspecs-and-governance)
5. All best practices and patterns
6. [Troubleshooting](#troubleshooting) deep dive

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

### Hierarchical Requirements (v1.4.0+)

Use indentation to create parent-child requirement relationships for better organization:

#### Indentation-Based Hierarchy

```markdown
## Requirements
- REQ-001: Authentication system
  - REQ-001.1: Login with email/password
  - REQ-001.2: OAuth integration
    - REQ-001.2.1: Google OAuth
    - REQ-001.2.2: GitHub OAuth
    - REQ-001.2.3: Facebook OAuth
  - REQ-001.3: Session management
    - REQ-001.3.1: JWT token generation
    - REQ-001.3.2: Token refresh mechanism
    - REQ-001.3.3: Session timeout handling
```

#### Dot Notation IDs

Sub-requirements use dot notation to show their relationship:
- `REQ-001` - Parent requirement
- `REQ-001.1` - First child
- `REQ-001.2` - Second child
- `REQ-001.2.1` - First grandchild of second child

#### Auto-Generated IDs

If you omit IDs, they're generated based on the parent:

```markdown
## Requirements
- REQ-001: User management
  - Email validation          # Becomes REQ-001.1
  - Password requirements     # Becomes REQ-001.2
    - Minimum 8 characters    # Becomes REQ-001.2.1
    - Special character       # Becomes REQ-001.2.2
```

#### Combining with Composite Markers

Hierarchical requirements work seamlessly with composite markers:

```markdown
## Requirements
- REQ-001: [!|mvp] E-commerce platform
  - REQ-001.1: [stage:implementation|progress:75%] Product catalog
    - REQ-001.1.1: [@backend] Database schema
    - REQ-001.1.2: [@frontend] Product display
  - REQ-001.2: [blocked|depends:REQ-001.1] Shopping cart
    - REQ-001.2.1: [gap:test] Add to cart
    - REQ-001.2.2: [estimate:3d] Update quantity
  - REQ-001.3: [stage:design] Checkout process
```

#### Best Practices

1. **Limit Depth**: Keep hierarchy to 4 levels maximum
2. **Consistent IDs**: Use dot notation consistently
3. **Logical Grouping**: Group related requirements under parents
4. **Clear Parents**: Parent requirements should be high-level features
5. **Atomic Children**: Child requirements should be specific and testable

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
- REQ-301: Page load time under 3 seconds on 3G
- REQ-302: API responses within 200ms for cached data
```

## Bidirectional Code Links (v1.5.0+)

Link requirements directly to their implementations in code with bidirectional traceability.

### Link Syntax

#### Bidirectional Links (↔)
Link both ways between specification and code:
```markdown
- REQ-001: [↔ src/auth.js:45-67] Authentication implementation
- REQ-002: [<-> lib/validator.py:100] Input validation logic
```

#### Forward Links (→)
Link from specification to code:
```markdown
- REQ-003: [→ app/main.java:25] Entry point implementation
- REQ-004: [-> tests/integration.test.js] Integration test coverage
```

#### Backward Links (←)
Link from code back to specification:
```markdown
- REQ-005: [← config.yaml:10-20] Configuration documented here
- REQ-006: [<- deploy.sh:5] Deployment script references
```

### Line Number Formats

```markdown
# Single line reference
[↔ src/utils.py:42]

# Line range reference
[↔ src/api.js:100-150]

# Whole file reference
[↔ src/config.yaml]
```

### Code Comments

Mark code implementations with MSL comments:

**Python:**
```python
# MSL: REQ-001
def authenticate(username, password):
    """User authentication implementation."""
    # Implementation here
```

**JavaScript:**
```javascript
// MSL: REQ-002
function validateInput(data) {
  /* MSL requirement implementation */
  return data.length > 0;
}
```

**Java:**
```java
// @implements REQ-003
public class AuthManager {
    /* MSL: REQ-004 */
    public boolean login(String user, String pass) {
        // Implementation
    }
}
```

### Composite Markers with Code Links

Combine code links with other markers:

```markdown
## Requirements
- REQ-001: [!|security|↔ auth/login.py:50-100] Secure login implementation
- REQ-002: [stage:testing|→ tests/auth_test.js:25-50] Auth tests in progress
- REQ-003: [@alice|← docs/api.md:100|gap:doc] API needs documentation
```

### Code Scanner

Use the MSL code scanner to find all implementations:

```python
from lib.code_scanner import CodeScanner

scanner = CodeScanner()

# Find all implementations of a requirement
impls = scanner.find_requirement_implementations("REQ-001", "./src")

# Generate reverse link mapping
links = scanner.generate_reverse_links("specs/auth.md", "./src")

# Verify bidirectional consistency
results = scanner.verify_bidirectional_links("specs/auth.md", "./")
```

### Best Practices

1. **Use Bidirectional Links** for critical requirements that need full traceability
2. **Use Forward Links** when documenting planned implementations
3. **Use Backward Links** when code references external specifications
4. **Include Line Numbers** for precise traceability to specific functions
5. **Keep Links Updated** when refactoring code or moving files

### Validation

The validator checks code links for:
- Valid file path format
- Numeric line numbers
- Logical line ranges (start < end)
- File existence (when configured)

Configure validation in `.mslrc`:
```yaml
# Link Validation
validate_file_paths: true  # Check that linked files exist
check_dead_links: false    # Don't check for broken links (expensive)
```

### Tool Support

**CLI Commands:**
```bash
# Scan code for MSL references
msl-scan ./src

# Verify bidirectional links
msl-verify specs/auth.md --code ./src

# Generate link report
msl-links --report specs/ src/
```

**IDE Integration:**
- VS Code extension shows linked code on hover
- Jump to implementation from requirement
- Jump to requirement from code comment
- Real-time link validation

### Examples

#### Complete Specification with Code Links

```markdown
# Authentication Module [MSL]

## Requirements

### Core Authentication
- REQ-001: [↔ src/auth/core.py:45-120] User authentication via OAuth 2.0
  - REQ-001.1: [→ src/auth/oauth.py:15-45] OAuth token generation
  - REQ-001.2: [→ src/auth/oauth.py:50-75] Token refresh mechanism
  - REQ-001.3: [← tests/auth_test.py:100-200] Token validation tests

### Security Features
- REQ-002: [!|security|↔ src/auth/security.py] Security controls
  - REQ-002.1: [→ src/auth/security.py:25-40] Password hashing with bcrypt
  - REQ-002.2: [→ src/auth/security.py:45-60] Rate limiting implementation
  - REQ-002.3: [→ src/auth/security.py:65-90] Session timeout handling

### API Endpoints
- REQ-003: [→ src/api/auth.js:100-150] REST API authentication endpoints
  - REQ-003.1: [→ src/api/auth.js:100-110] POST /auth/login
  - REQ-003.2: [→ src/api/auth.js:115-125] POST /auth/logout
  - REQ-003.3: [→ src/api/auth.js:130-140] POST /auth/refresh
```

## Validation Configuration (v1.4.0+)

Customize MSL validation rules for your project using configuration files or frontmatter.

### Configuration Methods

#### 1. Project Configuration File (.mslrc)

Create a `.mslrc` file in your project root to define validation rules:

```yaml
# MSL Validation Configuration
# Place this file as .mslrc in your project root

# ID Format Rules
require_ids: true
id_format: "^REQ-\\d{3}$"  # Require REQ-NNN format
id_sequence_check: false    # Don't require sequential IDs

# Content Rules
require_markers:
  - priority      # Every requirement must have priority
  - owner         # Every requirement must have an owner
forbid_markers:
  - deprecated    # Don't allow deprecated markers
  - obsolete      # Don't allow obsolete markers

# Hierarchy Rules
max_depth: 4         # Maximum nesting depth for hierarchical requirements
min_requirements: 5  # Minimum number of requirements per document
max_requirements: 100 # Maximum number of requirements per document

# Link Validation
require_code_links: false  # Don't require code links
validate_file_paths: true  # Check that linked files exist
check_dead_links: false    # Don't check for broken links (expensive)

# Custom Validators
custom_validators:
  - security_keywords_check      # Check for security keywords
  - api_consistency_check        # Validate API requirements
  - performance_requirements_check # Check performance criteria
  - testability_check            # Ensure requirements are testable

# Severity Overrides
severity_overrides:
  security_keywords_check: error  # Treat security issues as errors
  testability_check: warning       # Testability issues are warnings

# Strict Mode
strict: false  # Don't enforce all strict validation rules
```

#### 2. Document-Level Configuration (Frontmatter)

Override validation rules for a specific document:

```yaml
---
msl: L1
id: auth-spec
validation:
  require_ids: true
  id_format: "^AUTH-\\d{4}$"
  min_requirements: 10
  require_markers: [priority, security]
  custom_validators: [security_keywords_check]
---

# Authentication Specification [MSL]
```

### Built-in Custom Validators

MSL includes several pre-configured validators:

#### security_keywords_check
Ensures security-related requirements are properly marked:
- Detects keywords: password, encryption, authentication, token, etc.
- Warns if security keywords found without `[security]` category

#### api_consistency_check
Validates API requirements follow RESTful conventions:
- Checks endpoints specify HTTP methods (GET, POST, PUT, DELETE)
- Ensures API requirements follow consistent patterns

#### performance_requirements_check
Ensures performance requirements have measurable criteria:
- Detects performance keywords: latency, throughput, response time
- Requires numeric metrics (e.g., "less than 200ms", "99.9% uptime")

#### testability_check
Identifies requirements with vague, untestable language:
- Flags words like: should, might, possibly, user-friendly, intuitive
- Encourages specific, measurable requirements

### Configuration Examples

#### Example 1: API Project Configuration

```yaml
# .mslrc for REST API project
require_ids: true
id_format: "^API-\\d{3}$"
require_markers:
  - method        # HTTP method
  - endpoint      # API endpoint
  - response      # Expected response
custom_validators:
  - api_consistency_check
  - performance_requirements_check
```

#### Example 2: Security-Critical Project

```yaml
# .mslrc for security-focused project
require_ids: true
require_markers:
  - security
  - review_status
  - threat_model
forbid_markers:
  - draft
  - untested
custom_validators:
  - security_keywords_check
  - testability_check
severity_overrides:
  security_keywords_check: error
strict: true
```

#### Example 3: Agile Development Project

```yaml
# .mslrc for agile project
require_markers:
  - priority
  - sprint
  - assignee
  - estimate
max_requirements: 20  # Keep specs focused
custom_validators:
  - testability_check
```

### Configuration Priority

Configuration is loaded in this order (later overrides earlier):
1. Default MSL settings
2. Home directory `~/.mslrc`
3. Project root `.mslrc`
4. Parent directories `.mslrc` (searched upward)
5. Document frontmatter `validation:` section

### Writing Custom Validators

Create custom validators in Python:

```python
from lib.config import CustomValidators

@CustomValidators.register("domain_specific_check")
def check_domain_requirements(requirement):
    """Validate domain-specific requirements."""
    text = requirement.get('text', '').lower()
    
    # Your validation logic here
    if 'domain_term' in text and 'required_marker' not in requirement.get('markers', {}):
        return "Domain term found without required marker"
    
    return None  # Return None if validation passes
```

### Validation Commands

```bash
# Validate with project config
./msl-lint specs/my-spec.md

# Override config options
./msl-lint --require-ids --min-requirements 10 specs/

# Use specific config file
./msl-lint --config custom.mslrc specs/
```

### Best Practices

1. **Start Simple**: Begin with minimal configuration, add rules as needed
2. **Team Agreement**: Discuss and agree on validation rules as a team
3. **Progressive Enhancement**: Stricter rules for production specs
4. **Document Rules**: Comment your `.mslrc` to explain why rules exist
5. **Version Control**: Commit `.mslrc` to ensure consistent validation

### Common Patterns

#### Progressive Validation
Different rules for different stages:

```yaml
# .mslrc.draft - Initial development
min_requirements: 1
require_ids: false

# .mslrc.review - Code review stage
min_requirements: 5
require_ids: true
custom_validators: [testability_check]

# .mslrc.production - Production requirements
min_requirements: 10
require_ids: true
id_sequence_check: true
strict: true
```

#### Component-Specific Rules
Different validation for different components:

```yaml
# frontend/.mslrc
require_markers: [ui_component, accessibility]
custom_validators: [ui_consistency_check]

# backend/.mslrc
require_markers: [api_endpoint, database]
custom_validators: [api_consistency_check, performance_requirements_check]

# infrastructure/.mslrc
require_markers: [resource, cost_estimate]
custom_validators: [cost_validation_check]
```
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

### Real-World Example: How MSL Specifies Itself

MSL uses inheritance to build progressively complex levels. Here's the actual inheritance chain:

```markdown
# msl-l0-foundation.md (Base - No inheritance)
---
msl: L0
id: msl-l0-foundation
---
## Requirements
- REQ-001: Documents must be valid CommonMark markdown
- REQ-002: Must contain ## Requirements section
# ... 8 more basic requirements

# msl-l1-structure.md (Inherits from L0)
---
msl: L1
id: msl-l1-structure
extends: msl-l0-foundation  # IS-A Level 0 spec
---
## Requirements
- REQ-001: [INHERIT] All Level 0 markdown requirements
- REQ-101: [NEW] Support YAML frontmatter for metadata
- REQ-102: [NEW] Requirement IDs in format REQ-NNN
# ... 15 additional requirements

# msl-l2-advanced.md (Inherits from L1)
---
msl: L2
id: msl-l2-advanced
extends: msl-l1-structure  # IS-A Level 1 spec
governed-by: [msl-core-metaspec, msl-language-metaspec]
---
## Requirements
- REQ-001: [INHERIT] All MSL Level 1 structured specification requirements
- REQ-101: [NEW|!] Requirements may include quick markers
- REQ-108: [NEW] Support composite markers with pipe-separation
# ... 98 total requirements across all categories
```

### REQ-ID Numbering Strategies

MSL demonstrates three numbering approaches:

#### 1. Category-Based Numbering (MSL L2 uses this)
```markdown
## Requirements
### Core Language (001-099)
- REQ-001: [INHERIT] Level 1 requirements
- REQ-002: Core parsing rules

### Quick Markers (100-199)
- REQ-101: Priority markers with [!]
- REQ-102: Status markers [x] [ ] [?]

### Templates (200-299)  
- REQ-201: Template variable substitution
- REQ-202: Variable validation rules
```

#### 2. Hierarchical Numbering (For sub-requirements)
```markdown
- REQ-001: Main authentication requirement
  - REQ-001.1: Username/password authentication
  - REQ-001.2: Two-factor authentication
    - REQ-001.2.1: SMS-based 2FA
    - REQ-001.2.2: App-based 2FA
```

#### 3. Continuation Numbering (Simple inheritance)
```markdown
# Parent has REQ-001 through REQ-050
# Child continues from REQ-051
- REQ-051: [NEW] First new requirement in child
- REQ-052: [NEW] Second new requirement
```

### Inheritance Markers Explained

| Marker | Purpose | MSL Usage Example |
|--------|---------|-------------------|
| `[INHERIT]` | Keep parent requirement as-is | L2 inherits all L1 requirements |
| `[OVERRIDE]` | Replace parent requirement | L2 overrides L1's validation rules |
| `[NEW]` | Add requirement not in parent | L2 adds markers, templates, etc. |
| `[DEPRECATED]` | Mark for future removal | Old syntax being phased out |
| `[REMOVED]` | Was in parent, now gone | Removed experimental features |

### Anti-Patterns to Avoid

❌ **Deep Inheritance Chains**
```markdown
# AVOID: More than 3 levels
A extends B extends C extends D extends E
```

❌ **Cross-Domain Inheritance**
```markdown
# WRONG: API spec extending database spec
id: payment-api
extends: user-database  # APIs aren't databases!
```

❌ **Circular Dependencies**
```markdown
# ERROR: A extends B, B extends A
id: spec-a
extends: spec-b  # Creates infinite loop
```

## Project Organization

### Recommended Project Structure

Most projects benefit from a simple, consistent structure:

```
/your-project/
├── specs/                 # All your MSL specifications
│   ├── api/              # API specifications
│   ├── components/       # Component specifications
│   └── features/         # Feature specifications
├── src/                  # Implementation code
├── tests/                # Test files
└── scripts/              # Utility scripts with their specs
```

### Key Principles

1. **Keep specs close to code** - Specifications live in the same repository as implementation
2. **Mirror your architecture** - Organize specs like you organize code
3. **Start simple** - Don't over-organize until you need to
4. **One spec per component** - Each major component gets its own specification

### Example: Script with Specification

When creating scripts, keep the spec alongside:

```
scripts/
├── data-migration.py           # The implementation
└── data-migration-spec.md      # The MSL specification
```

The spec defines WHAT the script does:
```markdown
# Data Migration Script [MSL]

## Requirements
- REQ-001: Migrate user data from old to new schema
- REQ-002: Validate data integrity during migration
- REQ-003: Support rollback on error
```

The implementation shows HOW it's done (in `data-migration.py`).

## Tool and Script Integration

### Specification-First Development

1. **Write the spec first** - Define WHAT before HOW
2. **Link code to requirements** - Use comments to reference requirements
3. **Keep them in sync** - Update spec when requirements change

### Code-to-Spec Linking

Link your implementation to requirements using comments:

**Python:**
```python
# MSL: REQ-001
def migrate_users(old_db, new_db):
    """Migrate user data from old to new schema."""
    # Implementation here
```

**JavaScript:**
```javascript
// MSL: REQ-002
function validateData(data) {
    // Validates data integrity
    return isValid(data);
}
```

### Practical Example: API Development

1. **Create the specification** (`specs/api/payment-api.md`):
```markdown
# Payment API [MSL]

## Requirements
- REQ-001: Process credit card payments
- REQ-002: Support refunds within 30 days
- REQ-003: Return transaction ID on success
```

2. **Implement with references** (`src/payment-api.js`):
```javascript
// MSL: REQ-001
async function processPayment(card, amount) {
    // Implementation
    return { transactionId: "..." };  // MSL: REQ-003
}

// MSL: REQ-002
async function refundPayment(transactionId) {
    // Check 30-day window and process refund
}
```

3. **Validate alignment** - Ensure all requirements are implemented

### Common Patterns

**Pattern 1: Microservice Specifications**
```
services/
├── user-service/
│   ├── spec.md          # Service specification
│   ├── src/             # Implementation
│   └── tests/           # Tests reference spec requirements
```

**Pattern 2: Tool Specifications**
```
tools/
├── validator/
│   ├── validator-spec.md    # What the tool should do
│   ├── validator.py         # How it does it
│   └── test_validator.py    # Tests against spec
```

**Pattern 3: Feature Specifications**
```
features/
├── authentication/
│   ├── auth-spec.md         # Feature requirements
│   ├── implementation/      # Code that meets requirements
│   └── docs/               # User documentation
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

### Simple Markers (v1.0+)

#### Priority Markers

Indicate requirement importance:

```markdown
## Requirements
- REQ-001: [!] Critical security requirement
- REQ-002: [!!] Urgent blocker - must have for launch
- REQ-003: Standard priority (no marker)
- REQ-004: [~] Low priority, nice to have
- REQ-005: [?] Uncertain, needs clarification
```

#### Assignment Markers

Track responsibility:

```markdown
## Requirements
- REQ-001: [@alice] API endpoint implementation
- REQ-002: [@bob] UI component development
- REQ-003: [@team-qa] Test case creation
- REQ-004: [@role:architect] System design
```

#### Status Markers

Track implementation state:

```markdown
## Requirements
- REQ-001: [x] Completed requirement
- REQ-002: [ ] Pending requirement
- REQ-003: [?] Uncertain status
```

#### Tag Markers

Categorize requirements:

```markdown
## Requirements
- REQ-001: [#security] Encryption requirement
- REQ-002: [#performance] Response time requirement
```

### Composite Markers (v1.4.0+)

Composite markers allow multiple metadata elements in a single bracket, separated by pipes (`|`).

#### Basic Composite Syntax

```markdown
## Requirements
- REQ-001: [!|security|@team-security] Critical security vulnerability fix
- REQ-002: [blocked|external|vendor:acme] Third-party dependency
- REQ-003: [mvp|tested|deployed] Core feature ready for production
```

#### Priority and Status Combinations

```markdown
## Requirements
- REQ-001: [!!|blocked] Urgent but blocked by dependencies
- REQ-002: [~|review] Low priority item in review
- REQ-003: [!|testing|sprint:15] Critical feature in testing for sprint 15
```

#### Progress and Metrics

Track quantitative data with key:value pairs:

```markdown
## Requirements
- REQ-001: [stage:implementation|progress:60%] Core module development
- REQ-002: [stage:testing|coverage:85%|confidence:high] Validation logic
- REQ-003: [estimate:5d|actual:7d|variance:+2d] Complex migration task
- REQ-004: [sprint:15|milestone:v1.0|phase:2] Feature for release
```

#### Dependencies and Relationships

Express requirement relationships:

```markdown
## Requirements
- REQ-001: Core authentication module
- REQ-002: [depends:REQ-001] User profile management
- REQ-003: [blocks:REQ-004,REQ-005] Database migration
- REQ-004: [after:REQ-003|parallel:REQ-005] UI component
- REQ-005: [after:REQ-003|parallel:REQ-004] API endpoint
```

#### Gap Detection

Identify missing pieces:

```markdown
## Requirements
- REQ-001: [gap:test] Payment processing - needs test coverage
- REQ-002: [gap:doc] Complex algorithm - needs documentation
- REQ-003: [gap:implementation] Planned feature - not yet built
- REQ-004: [gap:review:security] Encryption - needs security review
```

#### Complex Real-World Examples

```markdown
## Requirements
- REQ-001: [!|security|stage:implementation|progress:75%] Payment encryption module
  - Critical security feature currently being implemented
  
- REQ-002: [mvp|depends:REQ-001|estimate:3d|@team-backend] Payment processing
  - MVP feature dependent on encryption, estimated 3 days
  
- REQ-003: [blocked|external|vendor:stripe|eta:2025-Q1] Stripe webhook integration
  - Blocked by external vendor, expected Q1 2025
  
- REQ-004: [stage:deployed:prod|version:v1.2.0|confidence:high] User authentication
  - Deployed to production in v1.2.0 with high confidence
```

### Marker Categories Reference

| Category | Purpose | Examples |
|----------|---------|----------|
| **Priority** | Importance level | `!` (critical), `!!` (urgent), `~` (low) |
| **Status** | Current state | `blocked`, `testing`, `review`, `complete` |
| **Assignment** | Ownership | `@user`, `@team-name`, `@role:architect` |
| **Stage** | Lifecycle phase | `stage:design`, `stage:testing`, `stage:deployed:env` |
| **Metrics** | Quantitative data | `progress:60%`, `coverage:85%`, `estimate:5d` |
| **Dependencies** | Relationships | `depends:REQ-X`, `blocks:REQ-Y`, `after:REQ-Z` |
| **Gaps** | Missing pieces | `gap:test`, `gap:doc`, `gap:implementation` |
| **Categories** | Classification | `security`, `performance`, `ui`, `api` |
| **Flags** | Boolean markers | `mvp`, `tested`, `deployed`, `external` |

### Validation Rules

Composite markers are validated for:
- **Progress/Coverage**: Must be 0-100%
- **Confidence**: Must be high/medium/low
- **Stage**: Must be valid lifecycle stage
- **Dependencies**: Must reference valid requirement IDs
- **Conflicts**: Cannot be both blocked and complete
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

## Common Pitfalls to Avoid

### 1. The Over-Specification Trap

**What goes wrong:** Including implementation details instead of requirements.

❌ **Bad Specification:**
```markdown
- REQ-001: System uses PostgreSQL 14.2 with connection pooling set to 100
- REQ-002: Authentication implemented using bcrypt with 12 rounds
- REQ-003: Frontend uses React 18.2.0 with Material-UI components
```

✅ **Good Specification:**
```markdown
- REQ-001: System must persist data with ACID compliance
- REQ-002: Passwords must be cryptographically hashed
- REQ-003: User interface must be responsive across devices
```

**Why it matters:** Specifications define WHAT, not HOW. Implementation details belong in code, not specs.

### 2. Confusing Meta-Specs with Regular Specs

**What goes wrong:** Creating meta-specifications for specific tools or features.

❌ **Wrong Approach:**
```markdown
# database-migration-tool-metaspec.md
type: metaspec  # WRONG! This is a specific tool, not a class
```

✅ **Correct Approach:**
```markdown
# database-migration-tool-spec.md
type: specification  # RIGHT! Specific tool gets regular spec
```

**Rule:** Meta-specs are for document templates, not tool specifications.

### 3. Misusing Inheritance

**What goes wrong:** Using `extends` for organizational grouping instead of true IS-A relationships.

❌ **Incorrect:**
```markdown
id: login-feature
extends: authentication-module  # Features aren't modules
```

✅ **Correct:**
```markdown
id: oauth-login
extends: basic-login  # OAuth login IS-A type of login
```

### 4. Inconsistent Requirement IDs

**What goes wrong:** Mixing ID formats within a specification.

❌ **Inconsistent:**
```markdown
- REQ-1: First requirement
- REQ-002: Second requirement  
- REQUIREMENT-3: Third requirement
- Req04: Fourth requirement
```

✅ **Consistent:**
```markdown
- REQ-001: First requirement
- REQ-002: Second requirement
- REQ-003: Third requirement
- REQ-004: Fourth requirement
```

### 5. Untestable Requirements

**What goes wrong:** Vague language that can't be verified.

❌ **Untestable:**
```markdown
- REQ-001: System should be fast
- REQ-002: Interface must be user-friendly
- REQ-003: Performance should be good
```

✅ **Testable:**
```markdown
- REQ-001: API responses must complete within 200ms for 95% of requests
- REQ-002: Interface must pass WCAG 2.1 Level AA accessibility standards
- REQ-003: System must handle 1000 concurrent users without degradation
```

### 6. Circular Dependencies

**What goes wrong:** Creating inheritance loops.

❌ **Creates Infinite Loop:**
```markdown
# spec-a.md
extends: spec-b

# spec-b.md
extends: spec-a  # ERROR: Circular dependency!
```

**Detection:** Use validation tools that check for circular dependencies.

### 7. Marker Inconsistency

**What goes wrong:** Using markers differently across requirements.

❌ **Inconsistent Usage:**
```markdown
- REQ-001: [!] Critical feature
- REQ-002: High priority feature  # Missing [!] marker
- REQ-003: [CRITICAL] Another feature  # Wrong marker format
```

✅ **Consistent:**
```markdown
- REQ-001: [!] Critical authentication feature
- REQ-002: [!] Critical authorization feature
- REQ-003: [@alice] Standard feature assigned to Alice
```

### 8. Missing Context in Child Specs

**What goes wrong:** Child specs that don't explain their relationship to parent.

❌ **No Context:**
```markdown
extends: base-spec
# No explanation of what this adds/changes
```

✅ **Clear Context:**
```markdown
extends: base-api-spec
# Extends base API with authentication and rate limiting
```

### Quick Validation Checklist

Before finalizing your specification:
- [ ] All requirements use consistent ID format
- [ ] No implementation details in requirements
- [ ] All requirements are testable
- [ ] Inheritance uses true IS-A relationships
- [ ] No circular dependencies
- [ ] Markers used consistently
- [ ] Meta-specs only for document templates
- [ ] Context provided for inheritance

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

### Inheritance Markers

| Marker | Purpose | When to Use | Example |
|--------|---------|-------------|---------|
| `[INHERIT]` | Keep parent req as-is | Explicitly show inheritance | `REQ-001: [INHERIT] All L1 requirements` |
| `[OVERRIDE]` | Replace parent req | Change parent behavior | `REQ-001: [OVERRIDE] 100GB storage` |
| `[NEW]` | Add new req | Extend parent spec | `REQ-100: [NEW] OAuth support` |
| `[DEPRECATED]` | Mark for removal | Phase out feature | `REQ-050: [DEPRECATED] Legacy API` |
| `[REMOVED]` | No longer applies | Document removal | `REQ-050: [REMOVED] Old auth method` |

### Common Markers

| Marker | Meaning | Example |
|--------|---------|---------|
| `[!]` | High priority | `REQ-001: [!] Critical feature` |
| `[@user]` | Assignment | `REQ-002: [@alice] Implement API` |
| `[#tag]` | Category | `REQ-003: [#security] Encrypt data` |
| `[✓]` | Complete | `REQ-004: [✓] Implemented` |
| `[x]` | Done | `REQ-005: [x] Tested` |
| `[ ]` | Pending | `REQ-006: [ ] In progress` |
| `[?]` | Uncertain | `REQ-007: [?] Needs clarification` |

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

### REQ-ID Numbering Conventions

| Strategy | Pattern | Use Case | Example |
|----------|---------|----------|---------|
| **Sequential** | REQ-001, REQ-002... | Simple specs | Basic requirements |
| **Category-based** | 100s, 200s, 300s | Complex specs | MSL L2 uses this |
| **Hierarchical** | REQ-001.1, REQ-001.2 | Sub-requirements | Nested features |
| **Prefixed** | AUTH-001, API-002 | Multi-domain | Mixed components |

### Inheritance Do's and Don'ts

#### ✅ DO:
- Use `extends` only for IS-A relationships
- Document why you're inheriting
- Keep inheritance depth ≤ 3 levels
- Use [INHERIT], [OVERRIDE], [NEW] markers
- Validate parent spec exists

#### ❌ DON'T:
- Use `extends` for organizational grouping
- Create circular dependencies
- Inherit across unrelated domains
- Override without clear reason
- Mix inheritance and governance carelessly

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

## Advanced Topics

> **Note:** Most users won't need these advanced concepts. They're here for completeness and special use cases.

### Metaspecs and Governance

**Metaspecs** are specifications that govern other specifications - think of them as "specs for specs". They're rarely needed unless you're:
- Building a framework that needs consistent documentation structure
- Enforcing organizational standards across many teams
- Creating reusable specification templates

**99% of users should use regular specifications instead.**

#### The Three Relationship Types

| Relationship | Keyword | Meaning | When to Use |
|-------------|---------|---------|------------|
| **Inheritance** | `extends` | IS-A relationship | Specializing an existing spec |
| **Governance** | `governed-by` | CONFORMS-TO relationship | Following standards |
| **Template** | `type: template` | DEFINES pattern | Creating reusable patterns |

#### Simple Governance Example

```markdown
---
id: payment-api
governed-by: pci-compliance-standards  # Must follow PCI rules
---
```

#### When You Might Need Metaspecs

- **Large organizations**: Enforcing consistent documentation across teams
- **Compliance requirements**: Ensuring specs meet regulatory standards
- **Framework development**: Defining structure for plugin specifications

For detailed metaspec documentation, see the [MSL specification repository](https://github.com/chrs-myrs/msl-specification/tree/master/specs/standards).

### Self-Referential Architecture

MSL uses itself to specify itself - the language specifications are written in MSL, validated by MSL tools, and governed by MSL metaspecs. This proves MSL can handle any level of complexity, but **you don't need this complexity for normal use**.

---

**Ready to write better specifications?** Start with [Getting Started](getting-started.md) or explore [Tutorials](tutorials/) for hands-on learning.

For complete language details, see the [Reference](reference.md). For tool usage, check the [Tools Guide](tools.md).