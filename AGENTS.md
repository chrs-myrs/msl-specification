# MSL Specification Agent Configuration

> **Generated file** - Do not edit directly. Regenerate using /livespec:audit context

## Summary

MSL (Markdown Specification Language) bridges human intent and AI implementation with stable, unambiguous specifications that stay human-readable without special tools. Success means: agents implement working code from specs alone; humans read specs without training; specs remain valid markdown on GitHub; MSL specifies itself (dogfooding); advanced features are optional and never break basic use.

## ⚠️ CRITICAL: Spec-First Protocol

Before creating ANY permanent file (anything committed to git: code, tests, config, docs, agent/skill/command definitions):

1. **TodoWrite gate**: add todo "Create spec for [filename]" BEFORE any file operation; complete it only after the spec exists.
2. **Check**: `scripts/livespec/check-requires-spec.sh path/to/file` (exit 0 = spec exists or not needed; exit 1 = STOP, create spec).
3. **Plan mode** for new files: plan shows the todo, the spec path (`specs/features/[name].spec.md`) and the passed check. Optional for edits to existing files and work in `var/`, `generated/`, `.archive/`.

No spec needed: `var/`, `generated/`, `.archive/`, `build/`, logs, caches. `specs/workspace/*.spec.md` are themselves specs. One spec may cover several files serving the same observable purpose (test: same observable purpose = one spec).

No exceptions: "obvious", "auto-generated", "just infrastructure" and "everyone knows what X is" are all still permanent files and need a spec.

PURPOSE.md stays under 20 content lines (vision and success criteria only). Route everything else at once: "must comply with X" to `specs/foundation/constraints.spec.md`; "users can do X" to `specs/foundation/outcomes.spec.md`; "will use X tech" to `specs/strategy/architecture.spec.md`; "system does X" to `specs/features/[feature].spec.md`.

## Constraints

MSL's intentional limits (all critical). MSL SHALL NOT:
- define implementation details or algorithms (specs say WHAT, not HOW)
- act as a programming or scripting language (no executable syntax or runtime semantics)
- enforce runtime behaviour or validation (validation is a tooling concern)
- require specific tools or IDEs (a plain text editor must suffice)
- mandate project structures (folder layout is a recommendation)

MSL SHALL remain a pure specification markup language: markdown is the only required format dependency.

## Core Principles

- Specs are created before implementation. Check `specs/features/` for a behaviour spec; guide to spec creation if missing.
- MSL minimalism: requirements specify WHAT not HOW; apply the four-question test before adding any requirement.
- Simplicity enables flexibility; progressive enhancement (Level 0 is always valid, higher levels are optional).
- Trust implementers: over-specification is a defect. Be AI-first but human-friendly; markdown stays the foundation.

## Folder Organization Decision Tests

Domain: software; specs boundary: specifications only.
- `specs/foundation/` - outcomes and constraints
- `specs/strategy/` - architectural decisions
- `specs/features/` - observable behaviours
- `specs/interfaces/` - API and data contracts
- `specs/workspace/` - how this project works (constitution, taxonomy, patterns, context architecture)

Test: a file in the wrong folder, or with an ambiguous location, is a defect.

## MSL Format Quick Reference

- **L0**: markdown with a `## Requirements` section. Default; most specs need nothing more.
- **L1**: L0 plus YAML frontmatter (`id`, `tags`, `priority`) and optional `REQ-001` identifiers.
- **L2**: L1 plus markers, templates and inheritance. Rarely needed.
- Every spec title ends with `[MSL]`. Requirements are specific, testable, and about WHAT.

```markdown
# Login System [MSL]

## Summary

Authentication and session management.

## Requirements

- Users can authenticate with email and password
- Sessions expire after 30 minutes of inactivity
```

Decision: just requirements = L0; need metadata/IDs = L1; need inheritance/templates = L2.

## Development Patterns and Workflows

This repository must exemplify the standards it defines.
- **Change together**: documentation specs (`specs/documentation/`) with `docs/`; the agent spec (`specs/applications/msl-validation-agent.md`) with `.claude/agents/`; the tools spec (`specs/applications/msl-tools-spec.md`) with `tools/`.
- **Quality bar before commit**: validation score 80/100 or more (msl-validator per spec, msl-batch-validator for integration); at least 90% of requirements testable; under 20% duplication; at most 4 inheritance levels; `[MSL]` in every title.
- **`extends` only for a true "is-a"** where every parent requirement applies. Never `extends: msl-l2-advanced` unless defining a new MSL level. Use `msl: L1` or `msl: L2` to declare features and `references:` for other relationships.
- **Lowest level first**: start at the simplest MSL level that meets the need.
- **Conservative user docs**: consolidate, simplify or remove before adding; serve the common case; move advanced topics such as metaspecs to appendices.
- **Pre-push**: run the pre-push completeness checker (`.claude/agents/pre-push-completeness-checker.md`) before any push.

## Spec Dependencies

- Foundation and workspace specs derive from PURPOSE.md (`derives-from`).
- Strategy specs derive from foundation specs (`derives-from`).
- Feature specs link upward with `satisfies` (outcomes or constraints) and `guided-by` (strategy).
- Each spec has a failure mode; every requirement should be traceable upward.

## Context Compression

Moderate: key rules are inline, large examples and detailed standards are referenced. Regenerate this file rather than editing it.

## Common Anti-Patterns

- Over-specifying ("exactly 120px wide, #007bff"); prefer "clearly visible".
- Wrong inheritance: `extends` for organisation rather than "is-a".
- Starting at L2 with templates and markers when L0 would do.
- Adding documentation instead of simplifying existing documentation.
- Creating a permanent file without its spec.
- Changing a spec without its docs, agent definition or tool counterpart (or the reverse).

## Reference Library

- `PURPOSE.md` - vision and success criteria
- `specs/INDEX.md`, `specs/README.md` - spec navigation
- `specs/msl-l0-foundation.md`, `specs/msl-l1-structure.md`, `specs/msl-l2-advanced.md` - the language levels
- `specs/standards/` - usage, organisation and extension standards
- `specs/applications/` - validator, batch validator and tools specs
- `specs/metaspecs/` - metaspecs (advanced)
- `docs/` - user documentation (`docs/guides/quick-start.md` to begin)
- `.claude/agents/` - msl-validator, msl-batch-validator, pre-push-completeness-checker

---
*Agent configuration for MSL Specification (LiveSpec v5.13.0)*
*Generated from workspace specs*

<!-- livespec-context-sources: sha256:818d28b5ae86cb3bd19eec50e8310030966d25d4c141bada87cf59bc5248cd05 n=15 -->
