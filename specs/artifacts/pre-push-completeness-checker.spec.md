---
msl: L1
id: pre-push-completeness-checker
type: agent
category: artifacts
fidelity: behavioral
criticality: IMPORTANT
failure_mode: Without a governing spec, pushes reach origin with specs, documentation or changelog out of step with the change, and each run of the checker applies a different bar
governed-by: []
satisfies:
  - specs/foundation/outcomes.spec.md
guided-by:
  - specs/workspace/patterns.spec.md
specifies:
  - .claude/agents/pre-push-completeness-checker.md
---

# Pre-Push Completeness Checker [MSL]

## Summary

An agent that, before a push, reports whether a change carries everything it needs to go to origin: specs, tests, documentation, changelog and release metadata.

A permanent file is one that is committed and lies outside `var/`, `generated/`, `.archive/` and `build/`.

## Requirements

- REQ-001: Lists every file the push adds, modifies or deletes
- REQ-002: Reports each added or moved permanent file that no spec's `specifies:` names, directly or through a folder containing it
- REQ-003: Reports a change to a governed file that its spec no longer describes, and a spec change whose governed files were left behind, as paired by each spec's `specifies:`
- REQ-004: Reports a behaviour change in `tools/` or `scripts/` that arrives without a change under `tests/`
- REQ-005: Reports a change to what MSL users read or run (the language specs, `docs/`, `tools/`, README, `llms.txt`) that has no CHANGELOG entry under Unreleased
- REQ-006: Reports usage that the change alters (a command, flag, field or published path) and that README, `docs/` or the roadmap do not yet reflect
- REQ-007: For a release, meaning the user says so or the change moves Unreleased entries under a version heading, reports a version that `pyproject.toml` and `package.json` do not carry, or a missing tag for it
- REQ-008: Reports work the change leaves incomplete: new TODO markers, orphaned files, and references to files it removed
- REQ-009: Reports version-control hygiene problems
  - Any credential, secret or personal data in the change
  - A new generated folder missing from `.gitignore`
  - A branch name or commit message that misdescribes the change
- REQ-010: Applies its bar by change class
  - Wording or typo fix: needs nothing beyond itself
  - Internal refactor with no behaviour change: needs passing tests
  - New or changed behaviour, format or field: needs everything REQ-002 to REQ-006 checks
- REQ-011: Gives each issue a specific action that would resolve it
- REQ-012: Ends with one verdict, `READY TO PUSH` or `NEEDS ATTENTION`, and a one-line reason
- REQ-013: Changes no file unless the user asks it to

## Validation

- A push that adds `scripts/new.sh` with no spec naming it gets `NEEDS ATTENTION`, citing that file
- A typo fix in `docs/` gets `READY TO PUSH`, with no demand for a CHANGELOG entry, version bump or tag
- A behaviour change in `tools/` with no test change is reported under REQ-004
- Every run ends with exactly one verdict line
