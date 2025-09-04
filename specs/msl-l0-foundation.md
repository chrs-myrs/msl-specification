# MSL Level 0: Foundation [MSL]

## Summary

MSL Level 0 is the foundation of Markdown Specification Language. It's simply markdown with a requirements section. No special tools needed, no complex syntax to learn. If you can write markdown, you can write MSL Level 0.

## Requirements

### Core Structure

- Documents should have a title using a level-1 markdown heading
- Documents should include a "Requirements" section with a level-2 heading  
- Requirements should be listed using markdown bullet points (dashes)
- Each requirement should describe a specific capability, constraint, or behavior of the system
- Requirements should be testable - specific enough to determine unambiguously whether they are satisfied
- Documents remain valid markdown files viewable in any markdown reader
- Documents with empty Requirements sections are not valid MSL specifications
- Nested requirements using indentation are permitted but not required

### Optional Identification

- Documents should include `[MSL]` in their title for explicit identification
- Documents should include a link to the MSL specification repository
- These identification methods are encouraged but optional - a Requirements section is sufficient for L0

## Examples

### Minimal MSL Level 0 Document

```markdown
# Login System

## Requirements
- Users can log in with email and password
- Sessions expire after 30 minutes of inactivity
- Failed login attempts lock account after 5 tries
```

### With Title Identification

```markdown
# Login System [MSL]

## Requirements
- Users can log in with email and password
- Sessions expire after 30 minutes of inactivity
- Failed login attempts lock account after 5 tries
```

### With MSL Link

```markdown
# Shopping Cart Feature

## Summary
Basic shopping cart functionality for e-commerce site.

## Requirements
- Users can add items to cart
- Users can remove items from cart
- Cart calculates total including tax
- Cart persists across browser sessions

## Notes
Specified using [MSL](https://github.com/chrs-myrs/msl-specification)
```

### With Both Identifiers

```markdown
# Payment Processing [MSL]

## Requirements
- Process credit card payments securely
- Support refunds within 30 days
- Generate receipts for all transactions

---
*Specification format: [MSL Level 0](https://github.com/chrs-myrs/msl-specification)*
```

## Notes

This specification defines MSL Level 0 using MSL Level 0 format itself. The beauty of Level 0 is its simplicity - it's just markdown with requirements. No tooling required, no syntax to memorize, just write what your system needs to do.

Level 0 documents can be enhanced with Level 1 features (IDs, frontmatter) or Level 2 features (markers, templates) when needed, but they work perfectly well as simple markdown files.

---
*Specification format: [MSL Level 0](https://github.com/chrs-myrs/msl-specification)*