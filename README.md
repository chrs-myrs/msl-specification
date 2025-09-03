# MSL: Markdown Specification Language

<div align="center">

**Write specifications that actually get read, updated, and followed.**

[![Version](https://img.shields.io/badge/spec-v1.1-blue.svg)](docs/spec/v1.1/specification.md)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://python.org)
[![GitHub Stars](https://img.shields.io/github/stars/chrs-myrs/msl-specification?style=social)](https://github.com/chrs-myrs/msl-specification)

[Quick Start](#-quick-start) • [Why MSL?](docs/why-msl.md) • [Examples](#-real-world-example) • [Documentation](docs/)

</div>

---

## 🎯 The Problem

You've been there: Complex specification formats that require special tools. YAML frontmatter nightmares. Requirements that get out of sync. Specs that nobody updates because they're too painful to edit.

## ✨ The Solution

MSL is just markdown with conventions. **Start with a simple list, grow into a full specification system.** No tools required until you need them.

```markdown
# Login System

## Requirements
- Users can log in with email/password
- Sessions expire after 30 minutes  
- Failed logins lock after 5 attempts
```

**↑ That's valid MSL.** Save it, commit it, share it. Done.

## 🚀 Quick Start

### 30 Seconds to Your First Spec

1. **Create a markdown file** with your requirements:

```markdown
# My API

## Requirements
- Accept JSON requests
- Return JSON responses
- Authenticate with API keys
```

2. **That's it.** You've written your first MSL spec.

### When You Need More

Add structure progressively:

```markdown
---
id: payment-api
priority: high
tags: [api, payments]
---

# Payment API

## Requirements
- REQ-001: [!] Process credit card payments
- REQ-002: Support refunds within 30 days
- REQ-003: [?] International payment support
```

## 📈 Progressive Enhancement

<table>
<tr>
<td width="33%" align="center">

**Level 0: Pure Markdown**  
No learning curve

```markdown
# Feature
## Requirements
- Thing one
- Thing two
```

</td>
<td width="33%" align="center">

**Level 1: Add IDs**  
When you need references

```markdown
---
id: feature
---
# Feature
## Requirements  
- REQ-001: Thing one
- REQ-002: Thing two
```

</td>
<td width="33%" align="center">

**Level 2: Full Power**  
Enterprise ready

```markdown
---
id: feature
extends: base
tags: [backend]
---
# Feature
## Requirements
- REQ-001: [OVERRIDE] Modified
- REQ-003: [NEW] Addition
```

</td>
</tr>
</table>

## 🌟 Why MSL?

### For Individuals
- **Start immediately** - No setup, no tools, just write
- **Stay organized** - Your filesystem is your database
- **Git-native** - Branch, diff, and merge naturally
- **AI-friendly** - LLMs understand MSL out of the box

### For Teams  
- **Gradual adoption** - Start simple, add process as needed
- **Review-friendly** - Readable diffs in pull requests
- **Template reuse** - Inherit from base specifications
- **Tool-optional** - Read and write without special software

### Compared to Alternatives

| | MSL | YAML/JSON | Word/PDF | Confluence/Notion |
|---|:---:|:---:|:---:|:---:|
| **No tools required** | ✅ | ❌ | ❌ | ❌ |
| **Git-friendly** | ✅ | ⚠️ | ❌ | ❌ |
| **Progressive complexity** | ✅ | ❌ | ❌ | ⚠️ |
| **Readable diffs** | ✅ | ⚠️ | ❌ | ❌ |
| **Inheritance** | ✅ | ⚠️ | ❌ | ❌ |

📖 **[See detailed comparisons with DOORS, Jira, ReqIF, and more →](docs/why-msl.md)**

## 🎯 MSL Self-Specification Achievement

**MSL is now completely self-specified** - meaning MSL is defined entirely using MSL itself! This validates MSL's expressive completeness and demonstrates its capability to specify complex systems.

### ✅ Bootstrap Complete

MSL successfully defines itself through a layered architecture:

```
Level 0 Foundation → Level 1 Structure → Level 2 Advanced
     ↓                    ↓                    ↓
Grammar Spec → Semantics Spec → Processing Spec → Complete Integration
```

- **[Level 0](specs/msl-l0-foundation.md)** - Pure markdown foundation
- **[Level 1](specs/msl-l1-structure.md)** - Adds frontmatter and IDs  
- **[Level 2](specs/msl-l2-advanced.md)** - Full feature set with inheritance
- **[Grammar](specs/msl-grammar.md)** - Formal syntax rules
- **[Semantics](specs/msl-semantics.md)** - Behavioral interpretation  
- **[Processing](specs/msl-processing.md)** - Tool requirements
- **[Complete](specs/msl-complete.md)** - Unified MSL specification

### 🔄 Self-Validation

The self-specifications pass validation using MSL's own tools:
```bash
msl-lint specs/  # ✅ Checked 7 files, found 0 errors
```

This proves that MSL is mature enough to specify itself and can handle complex, real-world specification challenges.

**[Explore the Self-Specifications →](specs/)**

## 💡 Real-World Example

Start with a todo list, evolve into a tracked project:

<details>
<summary><b>Day 1: Quick notes</b></summary>

```markdown
# Shopping Cart

## Requirements
- Add items to cart
- Remove items from cart
- Calculate totals
```
</details>

<details>
<summary><b>Day 5: Add priority markers</b></summary>

```markdown
# Shopping Cart

## Requirements
- [!] Add items to cart
- [!] Remove items from cart  
- Calculate totals
- [ ] Save cart for later
- [?] Guest checkout
```
</details>

<details>
<summary><b>Day 20: Full tracking</b></summary>

```markdown
---
id: shopping-cart
tags: [frontend, e-commerce]
status: in-progress
---

# Shopping Cart

## Requirements
- REQ-001: [x] Add items to cart
- REQ-002: [x] Remove items from cart
- REQ-003: [@alice] Calculate totals with tax
- REQ-004: [ ] Save cart for later
- REQ-005: [?] Guest checkout support
```
</details>

## 🛠️ Optional Tools

Tools are available when you need them:

```bash
# Validate your specs
msl-lint specs/

# Render templates
msl-render template.md -v service_name=PaymentAPI

# Resolve inheritance
msl-resolve derived-spec.md
```

### Installation

```bash
pip install msl-tools
# or use directly from the repo
python tools/cli/msl-lint my-spec.md
```

## 📚 Learn More

<table>
<tr>
<td>

**📖 Guides**
- [Quick Start](docs/guides/quick-start.md)
- [Solo Workflow](docs/guides/solo-workflow.md)  
- [Team Workflow](docs/guides/team-workflow.md)
- [LLM Integration](docs/guides/llm-integration.md)

</td>
<td>

**📝 Reference**
- [Full Specification](docs/spec/v1.1/specification.md)
- [Grammar Reference](docs/reference/grammar.md)
- [Markers Guide](docs/reference/markers.md)
- [Examples](examples/)

</td>
<td>

**🚧 Coming Soon**
- VS Code Extension (Q1 2025)
- Obsidian Plugin (Q1 2025)
- Web Editor (Q2 2025)
- [See Roadmap →](docs/spec/roadmap.md)

</td>
</tr>
</table>

## 🤝 Contributing

MSL is open source and we'd love your help!

- **Use it** and tell us what works (and what doesn't)
- **Star the repo** if you find it useful
- **Submit PRs** for tools, docs, or examples
- **Share your specs** as examples for others

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## 💬 Community

- [GitHub Discussions](https://github.com/chrs-myrs/msl-specification/discussions) - Ask questions, share ideas
- [Issues](https://github.com/chrs-myrs/msl-specification/issues) - Report bugs, request features

## 📄 License

MIT - Use it however you want. See [LICENSE](LICENSE) for details.

---

<div align="center">

**Ready to write better specs?**

[Get Started with the Quick Start Guide →](docs/guides/quick-start.md)

*Created for developers who want specifications that work with them, not against them.*

</div>