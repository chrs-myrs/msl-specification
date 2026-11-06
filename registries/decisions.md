---
store: registry
type: decisions
schema_version: 2
last_reviewed: 2026-11-06
entries:
  - id: DEC-001
    summary: Governance specs use LiveSpec's derives-from ("based on"), not MSL L2's narrower "computed from"
    severity: n/a
    status: accepted
    date: 2026-11-06
    alternatives_considered: [Widen REQ-446 to cover provenance by basis, Use another field for governance links, Drop LiveSpec traceability]
---

# Decision Registry

Tracks architecture and design choices with rejected alternatives. Resolved entries are removed — git history holds the record.

---

## DEC-001: Governance specs use LiveSpec's meaning of derives-from

**Context**: MSL L2 defines `derives-from:` as "generated or computed from" a source, and says an artefact that cannot be recomputed from its sources is misclassified (REQ-416, REQ-446, REQ-446b in `specs/msl-l2-advanced.md`). LiveSpec 5.13.0 uses the same field for "based on" and its validators require it: foundation and workspace specs must derive from `PURPOSE.md`, and strategy specs from foundation specs. The repository's governance specs (`specs/foundation/`, `specs/strategy/`, `specs/workspace/`) therefore carry the LiveSpec meaning, in the repository that defines the field.
**Alternatives considered**: Widening REQ-446 to cover provenance by basis would change the language to fit one tool, and remains open as a language question. Using a different field for governance links is not possible, because the LiveSpec frontmatter validator makes `derives-from` mandatory for strategy specs and blocks the commit without it. Dropping LiveSpec traceability would lose the upward links back to `PURPOSE.md`.
**Consequence**: In the governance specs, `derives-from` means "based on". The MSL language specs, documentation and examples keep the REQ-446 meaning. Anyone reading the governance specs as examples of MSL usage sees the field used outside its definition.
**Related**: `specs/msl-l2-advanced.md` (REQ-416, REQ-446, REQ-446a, REQ-446b); `specs/workspace/standards/dependencies.spec.md`
