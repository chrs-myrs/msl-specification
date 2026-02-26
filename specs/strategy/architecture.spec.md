---
criticality: IMPORTANT
failure_mode: Without integration requirements, MSL risks being built in isolation from the ecosystems where developers actually work
---

# MSL Integration Architecture

## Requirements

- [!] MSL SHALL integrate with version control systems (git)
  - Specifications are plain text files suitable for git diff and history
- [!] MSL SHALL be discoverable by documentation tools (e.g. Context7)
  - Standard markdown structure enables indexing without custom parsers
- [!] MSL SHALL support progressive disclosure of complexity
  - Simple projects use Level 0; complex projects add structure incrementally
- [!] MSL SHALL allow for project-specific extensions via metaspecs
  - Teams can define custom requirement types without breaking core MSL
- [!] MSL SHALL maintain backward compatibility with simpler levels
  - A Level 0 spec remains valid as the project adopts higher levels
