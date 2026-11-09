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
specifies:
  - .claude/agents/pre-push-completeness-checker.md
---

# Pre-Push Completeness Checker [MSL]

## Summary

An agent that, before a push, reports whether a change carries everything it needs to go to origin: specs, documentation, tests, changelog and version metadata.

## Requirements

- REQ-001: Lists every file the push adds, modifies or deletes
- REQ-002: Reports each changed permanent file that no spec's `specifies:` names
- REQ-003: Reports a spec changed without its counterpart, or a counterpart changed without its spec
  - Documentation specs with `docs/`, agent specs with `.claude/agents/`, the tools spec with `tools/`, a script's spec with the script
- REQ-004: Reports a behaviour change that arrives without a matching test change
- REQ-005: Reports a user-visible change with no CHANGELOG entry, and a release with no version bump or tag
- REQ-006: Reports changed usage that README or `docs/` do not yet reflect
- REQ-007: Reports any credential or secret in the change
- REQ-008: Scales its bar to the change: a minor fix or internal refactor needs fewer companions than a new feature or a format change
- REQ-009: Gives each issue a specific action that would resolve it
- REQ-010: Ends with one verdict, `READY TO PUSH` or `NEEDS ATTENTION`, and a one-line reason
- REQ-011: Changes no file unless the user asks it to

## Validation

- A push that adds a script without a spec naming it gets `NEEDS ATTENTION`, citing that script
- A typo fix in `docs/` gets `READY TO PUSH` without demands for a version bump or tag
- Every run ends with exactly one verdict line
