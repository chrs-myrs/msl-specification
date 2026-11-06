# MSL Specification Agent Configuration

> **Generated file** - Do not edit directly. Regenerate using /livespec:audit context

## Summary

MSL (Markdown Specification Language) bridges human intent and AI implementation with stable, unambiguous specifications for AI-driven development. It stays human-readable and reviewable without special tools. This repository holds the language, its optional tools, its documentation and its examples, and must exemplify MSL itself (dogfooding).

Success means: agents implement working code from MSL specs alone; humans understand specs without training; specs stay valid markdown on GitHub with no custom renderers; MSL specifies its own language, tools and docs; advanced features never break basic use.

## CRITICAL: Spec-First Protocol

Before creating ANY permanent file ("is it committed to git?"):

1. **TodoWrite gate**: add the todo "Create spec for [filename]" first. Mark it complete only once the spec exists.
2. **Check**: `scripts/livespec/check-requires-spec.sh path/to/file`. Exit 0 = spec exists or not needed. Exit 1 = STOP and create the spec.
3. **Plan mode for new files**: the plan shows the todo, the spec path (for example `specs/features/[name].spec.md`) and the passed check. Optional when editing existing files or working in `var/`, `generated/`, `.archive/`.

Permanent (needs a spec): code, tests, config, documentation, agent definitions, skills, commands. Not permanent: `var/`, `generated/`, `.archive/`, `build/`, logs, caches. `specs/workspace/*.spec.md` are themselves specs.

One spec may cover several files that serve the same observable purpose. No exceptions: "obvious", "auto-generated" and "just infrastructure" files still need a spec.

PURPOSE.md stays under 20 content lines (vision and success criteria only). Route everything else immediately: "must comply with X" to `specs/foundation/constraints.spec.md`; "users can do X" to `outcomes.spec.md`; "will use X tech" to `specs/strategy/architecture.spec.md`; "system does X" to `specs/features/`; "team follows X" to `specs/workspace/`. Check with `scripts/livespec/validate-purpose.sh`.

## Constraints

MSL SHALL NOT:
- define implementation details or algorithms (specs say WHAT, not HOW)
- act as a programming or scripting language (no executable syntax or runtime semantics)
- enforce runtime behaviour or validation (validation is a tooling concern)
- require specific tools or IDEs (plain text editors must suffice)
- mandate project structures (folder layout is a recommendation)

MSL SHALL remain a pure specification markup language; markdown is the only required format dependency.

## Core Principles

- Specs are created before implementation: check `specs/features/` for the behaviour spec, and guide to spec creation if it is missing.
- MSL minimalism: requirements specify WHAT, not HOW; apply the four-question test before adding a requirement.

## Folder Organization Decision Tests

Domain: software. Specs boundary: specifications only.

- `specs/foundation/` - outcomes and constraints
- `specs/strategy/` - architectural decisions
- `specs/features/` - observable behaviours
- `specs/interfaces/` - API and data contracts
- `specs/artifacts/` - specs for agents, commands and validators

MSL's own specs keep their published layout until their rename (`registries/debt.md`, DEBT-001): `specs/msl-l*.md`, `applications/`, `documentation/`, `standards/`, `metaspecs/`, `testing/`, `context7-optimization/`. These are not misplaced files; leave them where they are.

Test: does each file sit in exactly one obvious folder? If the location is ambiguous, re-examine the classification.

## Key Behaviors

The repository's MSL specs are not `*.spec.md`, so four bridge specs connect the spec-first gate to them. Requirements live in the detailed MSL spec, never in the bridge; new requirements go into the detailed spec, never into a new `*.spec.md`.

| Paths | Bridge spec | Detailed spec |
|-------|-------------|---------------|
| `docs/`, `examples/`, `README.md`, `CONTRIBUTING.md`, `llms.txt` | `specs/features/msl-documentation.spec.md` | `specs/documentation/`, `specs/context7-optimization/` |
| `tools/`, `tests/` | `specs/features/msl-tools.spec.md` | `specs/applications/msl-tools-spec.md`, `specs/testing/msl-testing-framework.md` |
| `.claude/agents/` | `specs/artifacts/msl-agents.spec.md` | `specs/applications/msl-validation-agent.md`, `msl-batch-validator.md` |
| `scripts/run_tests.sh`, `scripts/cleanup_tests_for_pytest.py` | `specs/artifacts/repo-scripts.spec.md` | `scripts/*-msl-spec.md` beside each script |

- `README.md`, `CONTRIBUTING.md` and `examples/` have no detailed spec: follow the conservative documentation rule below; examples stay valid MSL at the level they demonstrate.
- `docs/agent-guide.md` is itself an MSL document, governed by its own Requirements section. It is the public primer for agents outside this repo, not these instructions.
- `pre-push-completeness-checker` has no detailed spec yet; `msl-agents.spec.md` governs it until one exists.
- Tools stay optional: no MSL document may need them to be read or written.
- Validators vendored into `scripts/livespec/` are governed upstream by LiveSpec and are not specified here.
- A new script gets its own MSL spec beside it and an entry in `repo-scripts.spec.md` `specifies:`.

## Quick Start

1. Read the governing spec for the path you are changing (table above).
2. Change spec and counterpart together (see Development Patterns).
3. Validate modified specs with `msl-validator`; run `msl-batch-validator` for integration.
4. Run the pre-push completeness checker before any push.

## MSL Format Quick Reference

- **L0**: markdown with a `## Requirements` section. The default; start here.
- **L1**: L0 plus YAML frontmatter (ids, tags, priority).
- **L2**: L1 plus markers, templates and formal semantics. Only when needed.
- Titles end with `[MSL]`. Requirements are specific and testable, stating WHAT.

```markdown
# Login System [MSL]

## Requirements

- Sessions expire after 30 minutes of inactivity
```

Language definitions: `specs/msl-l0-foundation.md`, `specs/msl-l1-structure.md`, `specs/msl-l2-advanced.md`.

## Development Patterns and Workflows

- Specs and what they govern change together: documentation specs with `docs/`; the agent specs with `.claude/agents/`; the tools spec with `tools/`.
- Quality bar before commit: validation score 80/100 or more; at least 90% of requirements testable; under 20% duplication; at most 4 inheritance levels.
- Every specification title ends with `[MSL]`, except conventions vendored from LiveSpec (`specs/workspace/standards/`), which stay as shipped.
- Use `extends` only for a true "is-a" relationship where every parent requirement applies. Never `extends: msl-l2-advanced` unless defining a new MSL level. Use `msl: L1`/`L2` for features used and `references:` for other relationships.
- Start at the lowest MSL level that meets the need.
- User documentation stays conservative: consolidate, simplify or remove before adding; serve the common case; push advanced topics (such as metaspecs) to appendices.
- Run the pre-push completeness checker before any push.

## Spec Dependencies

- Foundation and workspace specs carry `derives-from: PURPOSE.md`; strategy specs derive from foundation specs.
- Feature specs link upward with `satisfies` and `guided-by`; artifact specs link upward with `satisfies`.
- In these governance specs `derives-from` means "based on" (DEC-001), not the narrower "computed from" of MSL L2. Language specs, docs and examples keep the L2 meaning.

## Context Compression

Moderate: strategic extraction, balanced inline and reference. Detailed implementation specs and interface contracts are referenced, not inlined.

## Common Anti-Patterns

- Writing a new `*.spec.md` that repeats a requirement held in a detailed MSL spec.
- Changing a spec without its counterpart (docs, agent, tool), or the reverse.
- Using `extends` for organisational hierarchy rather than "is-a".
- Starting at L2 when L0 would do; adding documentation instead of simplifying it.
- Specifying implementation (HOW) in requirements.

## Reference Library

- `registries/decisions.md` - DEC-001 (meaning of `derives-from`)
- `registries/debt.md` - DEBT-001 (MSL specs reach LiveSpec only through bridge specs; the bridges' `specifies:` must track moves)
- `specs/INDEX.md` - navigation for agents; `specs/standards/msl-project-organization.md` - structure we follow
- `docs/agent-guide.md`, `docs/implementation-reference.md`, `llms.txt` - public agent-facing material
- `specs/applications/` (tools and validators), `specs/documentation/`, `specs/testing/`, `specs/metaspecs/`

---
*Agent configuration for MSL Specification (LiveSpec v5.13.0)*
*Generated from workspace specs*

<!-- livespec-context-sources: sha256:84a510d79e22626041e67a1f4206ce306e004018b6d67681060517970bf0c446 n=19 -->
