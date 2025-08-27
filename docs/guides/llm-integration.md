# LLM Integration Guide

> How to use MSL effectively with AI assistants like ChatGPT, Claude, and Copilot

## Why MSL Works with LLMs

MSL is naturally LLM-friendly because:
- It's **plain markdown** that LLMs already understand
- It has **consistent patterns** that LLMs can learn
- It's **human-readable** so prompts stay simple
- It **scales progressively** matching LLM context windows

## Common Use Cases

### 1. Generate Specs from Ideas

**Prompt:**
```markdown
Convert this feature description to MSL format:

"We need a shopping cart that lets users add products, 
update quantities, apply coupon codes, and checkout. 
Must work with our existing payment system and support 
guest checkout."
```

**LLM Response:**
```markdown
# Shopping Cart

## Requirements
- REQ-001: Users can add products to cart
- REQ-002: Users can update product quantities
- REQ-003: Users can remove products from cart
- REQ-004: System validates product availability
- REQ-005: Users can apply coupon codes
- REQ-006: System calculates totals with discounts
- REQ-007: Integration with existing payment system required
- REQ-008: Guest checkout without account creation
- REQ-009: Cart persists across sessions for logged-in users
- REQ-010: Cart expires after 30 days of inactivity
```

### 2. Review and Improve Specs

**Prompt:**
```markdown
Review this MSL spec for completeness and suggest improvements:

# User Authentication

## Requirements
- Users can log in
- Users can log out
- Password reset
```

**LLM Response:**
```markdown
# User Authentication

## Requirements

### Core Authentication
- REQ-001: Users can log in with email/password
- REQ-002: Users can log out from all devices
- REQ-003: Session management with timeout

### Password Management  
- REQ-004: Password reset via email
- REQ-005: Password complexity requirements (min 8 chars, mixed case, numbers)
- REQ-006: Password change requires current password

### Security (Missing)
- REQ-007: [!] Account lockout after 5 failed attempts
- REQ-008: [!] Two-factor authentication support
- REQ-009: [!] Secure password storage (bcrypt/scrypt)
- REQ-010: CAPTCHA after 3 failed attempts

### User Experience (Missing)
- REQ-011: Remember me option
- REQ-012: Social login integration (Google, GitHub)
- REQ-013: Email verification for new accounts
```

### 3. Generate Test Cases

**Prompt:**
```markdown
Generate test cases for these MSL requirements:

## Requirements
- REQ-001: Users can upload images up to 5MB
- REQ-002: Supported formats: JPG, PNG, GIF
- REQ-003: Images are automatically resized to max 1920x1080
```

**LLM Response:**
```markdown
# Image Upload Test Cases

## Test Coverage for Requirements

### REQ-001: File Size Validation
- TC-001-1: Upload 4.9MB image → Success
- TC-001-2: Upload 5.0MB image → Success  
- TC-001-3: Upload 5.1MB image → Error: "File too large"
- TC-001-4: Upload 0KB file → Error: "Invalid file"

### REQ-002: Format Validation
- TC-002-1: Upload .jpg file → Success
- TC-002-2: Upload .png file → Success
- TC-002-3: Upload .gif file → Success
- TC-002-4: Upload .bmp file → Error: "Unsupported format"
- TC-002-5: Upload .txt renamed to .jpg → Error: "Invalid image"

### REQ-003: Resize Validation
- TC-003-1: Upload 1920x1080 image → No resize
- TC-003-2: Upload 3840x2160 image → Resized to 1920x1080
- TC-003-3: Upload 800x600 image → No resize (smaller than max)
- TC-003-4: Upload 2000x1000 image → Resized to 1920x960 (maintains ratio)
```

### 4. Find Missing Requirements

**Prompt:**
```markdown
What requirements am I missing for a password reset feature?

Current requirements:
- REQ-001: User can request password reset
- REQ-002: Email sent with reset link
- REQ-003: User sets new password
```

**LLM Response:**
```markdown
Missing requirements for password reset:

## Security Requirements
- REQ-004: [!] Reset token expires after 1 hour
- REQ-005: [!] Reset token single-use only
- REQ-006: [!] Rate limiting on reset requests (max 3 per hour)
- REQ-007: Verify email exists before sending (or show generic message)

## User Experience
- REQ-008: Clear error messages for expired/invalid tokens
- REQ-009: Confirm password field for new password
- REQ-010: Success notification and redirect to login

## Edge Cases
- REQ-011: Handle multiple reset requests (invalidate previous)
- REQ-012: Prevent reset for deactivated accounts
- REQ-013: Log security events for audit trail

## Email Requirements
- REQ-014: Email must contain user's name
- REQ-015: Email must explain why received
- REQ-016: Include support contact for unrequested resets
```

### 5. Convert Between Formats

**Prompt:**
```markdown
Convert these user stories to MSL requirements:

As a customer
I want to filter products by price
So that I can find products within my budget

As a customer
I want to sort products by rating
So that I can find the best products
```

**LLM Response:**
```markdown
# Product Browsing

## Requirements

### Filtering
- REQ-001: Users can filter products by minimum price
- REQ-002: Users can filter products by maximum price  
- REQ-003: Users can filter products by price range
- REQ-004: Price filters update results in real-time
- REQ-005: Active filters shown with clear option

### Sorting
- REQ-006: Users can sort products by rating (high to low)
- REQ-007: Users can sort products by rating (low to high)
- REQ-008: Default sort is highest rated first
- REQ-009: Sort preference persists during session
- REQ-010: Sort works with active filters
```

## Advanced Techniques

### Template Generation

**Prompt:**
```markdown
Create an MSL template for API endpoint specifications that I can reuse
```

### Inheritance Resolution

**Prompt:**
```markdown
I have a base spec:
[paste base.md]

And a child spec that extends it:
[paste child.md]

Show me the fully resolved requirements
```

### Gap Analysis

**Prompt:**
```markdown
Compare these two MSL specs and identify gaps:

Spec A: [paste]
Spec B: [paste]
```

### Compliance Checking

**Prompt:**
```markdown
Review this MSL spec for GDPR compliance issues:
[paste spec]
```

## Best Practices

### 1. Provide Context
```markdown
"We're building a B2B SaaS platform for small businesses.
Convert these requirements to MSL format: ..."
```

### 2. Use Examples
```markdown
"Following this MSL format:
- REQ-XXX: [priority] requirement text

Add requirements for: ..."
```

### 3. Iterative Refinement
```markdown
"Make these requirements more specific and testable:
[paste requirements]"
```

### 4. Request Explanations
```markdown
"Add these requirements and explain why each is important:
- Security requirements for file upload"
```

## Prompt Templates

### Spec Creation
```markdown
Create an MSL specification for [feature].
Context: [domain/industry]
Users: [user types]
Constraints: [technical/business constraints]
```

### Spec Review
```markdown
Review this MSL spec for:
1. Completeness
2. Clarity
3. Testability
4. Security gaps
5. Performance considerations

[paste spec]
```

### Spec Extension
```markdown
This is my base MSL spec: [paste]

Create a child spec that extends it for [specific use case]
Mark inherited, overridden, and new requirements
```

## Working with Different LLMs

### ChatGPT
- Excellent at generating comprehensive specs
- Good at finding edge cases
- Can maintain context across long conversations

### Claude
- Strong at reviewing and improving structure
- Excellent at explaining rationale
- Good at identifying security concerns

### GitHub Copilot
- Best for inline requirement completion
- Good at following existing patterns
- Useful for generating IDs sequentially

### Local LLMs
- Use for sensitive requirements
- Prompt with more examples
- Be specific about format requirements

## Automation Ideas

### Git Hooks
```bash
#!/bin/bash
# .git/hooks/pre-commit
# Use LLM to review MSL changes

changes=$(git diff --cached -- "*.md")
if [ ! -z "$changes" ]; then
  echo "$changes" | llm "Review these MSL changes for issues"
fi
```

### CI Integration
```yaml
- name: LLM Spec Review
  run: |
    for spec in specs/*.md; do
      cat $spec | llm "Validate this MSL spec format"
    done
```

## Limitations

LLMs can help but remember:
- They may generate plausible but incorrect requirements
- They don't know your specific business context
- They can't replace domain expertise
- Always review generated content carefully

## Future Possibilities

As LLMs evolve, expect:
- Direct MSL validation in IDEs
- Automatic test generation from requirements
- Real-time consistency checking
- Natural language queries over spec corpus

---

*MSL + LLMs = Specifications at the speed of thought*