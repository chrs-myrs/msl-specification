---
criticality: CRITICAL
failure_mode: Without these boundaries, MSL risks becoming a programming language or tool-dependent format, losing its core value as a human-readable specification markup language
---

# MSL Intentional Limitations

## Requirements

- [!] MSL SHALL NOT define implementation details or algorithms
  - Specifications describe WHAT, not HOW
  - Implementation decisions belong to the implementer
- [!] MSL SHALL NOT act as a programming or scripting language
  - No executable syntax or runtime semantics
- [!] MSL SHALL NOT enforce runtime behaviour or validation
  - Validation is a tooling concern, not a language concern
- [!] MSL SHALL NOT require specific tools or IDEs to read or write
  - Plain text editors must be sufficient
- [!] MSL SHALL NOT mandate specific project structures
  - Folder layout is a recommendation, not a requirement
- [!] MSL SHALL remain a pure specification markup language
  - Markdown is the only required format dependency
