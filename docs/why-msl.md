# Why MSL (Markdown Specification Language) Exists

## The Problem

Requirements and specifications tend to evolve through predictable stages:

1. **Quick notes** in whatever tool is handy
2. **Structured documents** as complexity grows
3. **Inheritance patterns** as variations multiply
4. **Full management systems** for team coordination

Most tools force you to choose your complexity level upfront. Start in Notepad? You'll need to migrate everything when you need structure. Start in DOORS? You'll spend more time fighting the tool than writing requirements.

## What MSL Provides

MSL is markdown that scales. Write naturally, add structure incrementally:

```markdown
Start here:           Add IDs later:        Add inheritance when needed:
# Login              # Login               ---
- Allow login        - REQ-001: Login      extends: auth-base
- Stay secure        - REQ-002: Security   ---
```

The same files work throughout your project's lifecycle. No migrations, no lock-in, no wasted ceremony.

## Comparison with Alternatives

### MSL vs. Plain Markdown/Text Files

| Aspect | Plain Markdown | MSL |
|--------|---------------|-----|
| **Learning curve** | None | None to minimal |
| **Structure** | Convention-based | Optional enforcement |
| **Inheritance** | Copy-paste | Built-in extends |
| **Tool requirements** | Any editor | Any editor |
| **Scalability** | Poor beyond ~20 requirements | Good to ~500 requirements |

**Choose plain markdown when**: You have <10 requirements that won't have variants  
**Choose MSL when**: You're already writing markdown but need light structure

### MSL vs. Requirements Management Tools (DOORS, Jama, Polarion)

| Aspect | Enterprise Tools | MSL |
|--------|-----------------|-----|
| **Cost** | $1000s per user/year | Free |
| **Learning curve** | Weeks of training | Minutes to hours |
| **Collaboration** | Built-in workflows | Git-based |
| **Traceability** | Comprehensive | Basic via extends |
| **Compliance** | Industry certified | Self-managed |
| **Scale** | 10,000+ requirements | ~500 comfortable max |

**Choose enterprise tools when**: Regulatory compliance requires it, or managing 1000+ requirements  
**Choose MSL when**: You want requirements-as-code in your repo

### MSL vs. Wiki/Confluence

| Aspect | Wiki Systems | MSL |
|--------|-------------|-----|
| **Storage** | Database/cloud | Files in git |
| **Version control** | Built-in but limited | Full git power |
| **Offline work** | Limited/none | Full support |
| **Search** | Powerful | Basic (grep/IDE) |
| **Rich media** | Full support | Markdown limits |

**Choose wikis when**: Non-technical stakeholders need web-based editing  
**Choose MSL when**: You want requirements versioned with code

### MSL vs. Issue Trackers (Jira, GitHub Issues)

| Aspect | Issue Trackers | MSL |
|--------|---------------|-----|
| **Granularity** | One item per issue | Multiple reqs per file |
| **Organization** | Labels and projects | Folders and inheritance |
| **Discussion** | Built-in comments | PR reviews |
| **Workflow** | Status transitions | Git flow |
| **Integration** | APIs and webhooks | File-based |

**Choose issue trackers when**: Requirements need individual workflows/assignment  
**Choose MSL when**: Requirements are relatively stable specifications

### MSL vs. Specialized Formats (SysML, ReqIF)

| Aspect | Formal Specifications | MSL |
|--------|---------------------|-----|
| **Expressiveness** | Complete modeling | Basic text + metadata |
| **Validation** | Formal verification | Convention checking |
| **Tool dependency** | Requires specific tools | Any text editor |
| **Interoperability** | Industry standard | Markdown only |
| **Learning curve** | Significant | Minimal |

**Choose formal specs when**: System engineering or safety-critical domains  
**Choose MSL when**: You need lightweight structure without tool lock-in

### MSL vs. Documentation Generators (Sphinx, MkDocs)

| Aspect | Doc Generators | MSL |
|--------|---------------|-----|
| **Purpose** | Publishing | Authoring + publishing |
| **Structure** | Presentation-focused | Content-focused |
| **Inheritance** | Include files | Semantic inheritance |
| **Output** | HTML/PDF priority | Markdown priority |
| **Build requirement** | Always needs build | Optional build |

**Choose doc generators when**: Publishing is primary goal  
**Choose MSL when**: Requirements management is primary, publishing secondary

## When MSL Makes Sense

MSL fits best when you:

- Work alone or in small teams (1-10 people)
- Manage 10-500 requirements
- Already use git and markdown
- Want requirements versioned with code
- Need inheritance but not complex workflows
- Value simplicity over features

## When to Use Something Else

MSL is **not** the right choice when you:

- Need regulatory compliance documentation
- Manage 1000+ requirements
- Require formal verification/proofs
- Have non-technical stakeholders doing primary authoring
- Need complex workflow automation
- Require real-time collaboration

## The MSL Philosophy

MSL exists because there's a gap between "notes in a text file" and "enterprise requirements platform" that affects millions of developers. We write specs in markdown anyway—MSL just adds the minimal structure to make that sustainable as projects grow.

It's not trying to replace DOORS or Jira. It's trying to make your existing markdown files 10% more powerful without making them 50% more complex.

## Migration Paths

MSL explicitly supports migration both up and down:

**Starting simpler than MSL?**
- Keep writing plain markdown
- Add `## Requirements` heading when ready
- Add IDs when you need references

**Outgrowing MSL?**
- Export to CSV → Import to Jira/DOORS
- Convert to ReqIF for tool interchange
- Generate documentation with Sphinx/MkDocs

The goal is to be useful for as long as possible without trapping you when needs change.

---

*MSL is requirements management for people who think enterprise tools are overkill but copy-paste isn't enough.*