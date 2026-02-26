---
criticality: IMPORTANT
failure_mode: Without shared philosophy, contributors add complexity that conflicts with MSL's core design intent, eroding its simplicity and accessibility
---

# MSL Design Philosophy

## Requirements

- [!] Simplicity SHALL always enable flexibility
  - Simple constructs compose into complex specifications without requiring complex syntax
- [!] Progressive enhancement SHALL allow starting simple and adding complexity only when needed
  - Level 0 (plain markdown) is always valid; higher levels add optional structure
- [!] Intuitive readability SHALL prioritise understandability
  - Specifications must be mostly comprehensible without MSL knowledge
- [!] Specifications SHALL trust implementers' judgement
  - Over-specification is a defect; under-specification delegates appropriately
- [!] Dogfooding SHALL demonstrate that MSL can specify anything, including itself
  - Self-specification is a key validation of language completeness
- [!] Specifications SHALL be AI-first but human-friendly
  - Machine parseability and human readability are complementary, not competing
- [!] Markdown SHALL remain the foundation
  - No proprietary formats; standard markdown tooling always works
- [!] Optional features SHALL never break basic functionality
  - Advanced features are additive; basic specs remain valid without them
