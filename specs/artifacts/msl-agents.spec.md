---
type: agent
category: artifacts
fidelity: behavioral
criticality: IMPORTANT
failure_mode: Without a governing spec, every agent change trips the spec-first gate and agents write duplicate specs beside the MSL agent specs that already govern these files
governed-by: []
satisfies:
  - specs/foundation/outcomes.spec.md
specifies:
  - .claude/agents/
---

# MSL Agents [MSL]

## Summary

Connects the spec-first gate to the MSL specs that govern this repository's Claude Code agents.

## Requirements

- [!] Validator agent requirements live in the detailed MSL specs, not here
  - `specs/applications/msl-validation-agent.md` governs `msl-validator`
  - `specs/applications/msl-batch-validator.md` governs `msl-batch-validator`
- [!] `pre-push-completeness-checker` reports, before a push, whether the specs, documentation, changelog and versioning that the pushed changes need are complete
  - It has no detailed MSL spec yet; this requirement governs it until one exists
- [!] New agent requirements go into a detailed MSL spec, never into a new `*.spec.md`

## Validation

- Every agent under `.claude/agents/` is named by this spec's `specifies:`
- Each agent's behaviour matches its governing requirement
