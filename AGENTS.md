# MSL Specification Agent Configuration

> **Generated file** - Do not edit directly. Regenerate using /livespec:audit context

## Summary

MSL (Markdown Specification Language) bridges human intent and AI implementation with stable, unambiguous specifications for AI-driven development. It stays human-readable and reviewable without special tools. This repository holds the language, its optional tools, its documentation and its examples, and must exemplify MSL itself (dogfooding).

Success means: agents implement working code from MSL specs alone; humans understand specs without training; specs stay valid markdown on GitHub with no custom renderers; MSL specifies its own language, tools and docs; advanced features never break basic use.

## Constraints

MSL SHALL NOT:
- define implementation details or algorithms (specs say WHAT, not HOW)
- act as a programming or scripting language (no executable syntax or runtime semantics)
- enforce runtime behaviour or validation (validation is a tooling concern)
- require specific tools or IDEs (plain text editors must suffice)
- mandate project structures (folder layout is a recommendation)

MSL SHALL remain a pure specification markup language; markdown is the only required format dependency.

## CRITICAL: Spec-First Protocol

Before creating ANY permanent file ("is it committed to git?"):

1. **TodoWrite gate**: add the todo "Create spec for [filename]" first. Mark it complete only once the spec exists.
2. **Check**: `scripts/livespec/check-requires-spec.sh path/to/file`. Exit 0 = spec exists or not needed. Exit 1 = STOP and create the spec.
3. **Plan mode for new files**: the plan shows the todo, the spec path (for example `specs/features/[name].spec.md`) and the passed check. Optional when editing existing files or working in `var/`, `generated/`, `.archive/`.

Permanent (needs a spec): code, tests, config, documentation, agent definitions, skills, commands. Not permanent: `var/`, `generated/`, `.archive/`, `build/`, logs, caches. `specs/workspace/*.spec.md` are themselves specs.

One spec may cover several files that serve the same observable purpose. No exceptions: "obvious", "auto-generated" and "just infrastructure" files still need a spec.

PURPOSE.md stays under 20 content lines (vision and success criteria only). Route everything else immediately: "must comply with X" to `specs/foundation/constraints.spec.md`; "users can do X" to `outcomes.spec.md`; "will use X tech" to `specs/strategy/architecture.spec.md`; "system does X" to `specs/features/`; "team follows X" to `specs/workspace/`. Check with `scripts/livespec/validate-purpose.sh`.

## Core Principles

- Specs are created before implementation: check `specs/features/` for the behaviour spec, and guide to spec creation if it is missing.
- MSL minimalism: requirements specify WHAT, not HOW; apply the four-question test before adding a requirement.

## Folder Organization Decision Tests

Domain: software. Specs boundary: specifications only.

- `specs/foundation/` - outcomes and constraints
- `specs/strategy/` - architectural decisions
- `specs/features/` - observable behaviours
- `specs/interfaces/` - API and data contracts, including the MSL language levels and `standards/`
- `specs/artifacts/` - agents, commands and validators
- `specs/workspace/metaspecs/` - metaspecs governing this repository's own specs; plain `.md`, because MSL's `type: metaspec` is not a LiveSpec type (DEC-001)
- A script's spec sits beside it as `scripts/<script>.spec.md`
- `specs/msl-l0-foundation.md`, `msl-l1-structure.md` and `msl-l2-advanced.md` are pointers kept at published paths, not specs

Outside every spec's `specifies:` by choice: PURPOSE.md, CHANGELOG.md, LICENSE, .gitignore, project.yaml and `registries/`.

Test: does each file sit in exactly one obvious folder? If the location is ambiguous, re-examine the classification.

## Key Behaviors

Every spec names the files it governs in `specifies:`. Read the governing spec before changing a path, and change both together.

| Paths | Governing spec |
|-------|----------------|
| `docs/` (guides, spec/, patterns/, workflows/, proposals/, contributing, tools, why-msl, roadmap, changelog, agent-guide), `examples/`, `README.md`, `CONTRIBUTING.md`, `specs/README.md` | `specs/features/documentation/msl-docs-base.spec.md` |
| `docs/getting-started.md`, `docs/user-guide.md`, `docs/reference.md` and `docs/reference/`, `docs/tutorials/` | `specs/features/documentation/msl-docs-{getting-started,user-guide,reference,tutorials}.spec.md` |
| `llms.txt`, `docs/implementation-reference.md` | `specs/features/context7-optimization/msl-llms-txt.spec.md`, `msl-implementation-reference.spec.md` |
| `tools/`, `package.json`, `pyproject.toml`, `pytest.ini`, `requirements-dev.txt`, `.pre-commit-config.yaml` | `specs/features/msl-tools.spec.md` |
| `tests/` | `specs/features/testing/msl-testing-framework.spec.md` |
| `.claude/agents/msl-validator.md`, `msl-batch-validator.md`, `pre-push-completeness-checker.md` | `specs/artifacts/msl-validation-agent.spec.md`, `msl-batch-validator.spec.md`, `pre-push-completeness-checker.spec.md` |
| `scripts/run_tests.sh`, `scripts/cleanup_tests_for_pytest.py` | `scripts/<script>.spec.md` beside each |

- `docs/agent-guide.md` is the public primer for agents outside this repo, not these instructions.
- Tools stay optional: no MSL document may need them to be read or written.
- Validators vendored into `scripts/livespec/` are governed upstream by LiveSpec and are not specified here.
- A new script gets its own `<script>.spec.md` beside it.

## Development Patterns and Workflows

- Specs and what they govern change together: documentation specs with `docs/`, `llms.txt`, README and `examples/`; agent specs with `.claude/agents/`; the tools spec with `tools/`; the testing spec with `tests/`.
- Quality bar before commit: validation score 80/100 or more (`msl-validator` per spec, `msl-batch-validator` for integration); at least 90% of requirements testable; under 20% duplication; at most 4 inheritance levels.
- Every specification title ends with `[MSL]`, except conventions vendored from LiveSpec (`specs/workspace/standards/`), which stay as shipped.
- Use `extends` only for a true "is-a" relationship where every parent requirement applies. Never `extends: msl-l2-advanced` unless defining a new MSL level. Use `msl: L1`/`L2` for features used and `references:` for other relationships.
- Start at the lowest MSL level that meets the need.
- User documentation stays conservative: consolidate, simplify or remove before adding; serve the common case; push advanced topics (such as metaspecs) to appendices.
- Run the pre-push completeness checker before any push.

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

Language definitions: `specs/interfaces/msl-l0-foundation.spec.md`, `msl-l1-structure.spec.md`, `msl-l2-advanced.spec.md`.

## Spec Dependencies

- Only governance specs (`specs/foundation/`, `specs/strategy/`, `specs/workspace/`) carry `derives-from`: foundation and workspace derive from `PURPOSE.md`, strategy from foundation.
- MSL's own specs link upward through `satisfies:` and `guided-by:`.
- Per DEC-001, in `*.spec.md` files `derives-from` means "based on" and `type:` is a LiveSpec type, where MSL L2 defines them differently. The MSL meanings still hold in the language specs' text, the docs and the examples.

## Context Compression

Moderate: strategic extraction, balanced inline and reference. Detailed implementation specs and interface contracts are referenced, not inlined.

## Common Anti-Patterns

- Changing a spec without the docs, agent, tool or tests it governs, or the reverse.
- Creating a permanent file that no spec's `specifies:` lists.
- Using `extends` for organisational hierarchy rather than "is-a".
- Starting at L2 when L0 would do; adding documentation instead of simplifying it.
- Specifying implementation (HOW) in requirements.
- Giving a metaspec or other MSL-typed document a `.spec.md` name, or treating the pointer files at `specs/msl-l*.md` as specs.

## Reference Library

- `registries/decisions.md` - DEC-001 (LiveSpec's meanings of `derives-from` and `type:` apply in `*.spec.md` files)
- `specs/INDEX.md` - navigation for agents
- `specs/interfaces/standards/` - usage, extension and project-organisation standards
- `specs/workspace/metaspecs/` - metaspecs for language, core, documentation, validation and testing
- `specs/features/` (tools, `documentation/`, `context7-optimization/`, `testing/`) and `specs/artifacts/` (agents)
- `docs/agent-guide.md`, `docs/implementation-reference.md`, `llms.txt` - public agent-facing material

---
*Agent configuration for MSL Specification (LiveSpec v5.13.0)*
*Generated from workspace specs*

<!-- livespec-context-sources: sha256:bdf09b5d6fd82ad21142aeab679948d0e17886bc659a6e57b20fb8cb8d90a9a1 n=33 -->
