---
store: registry
type: decisions
schema_version: 2
last_reviewed: 2026-11-09
entries:
  - id: DEC-001
    summary: Where LiveSpec and MSL L2 define a frontmatter field differently, this repository's *.spec.md files follow LiveSpec
    severity: n/a
    status: accepted
    date: 2026-11-06
    alternatives_considered: [Widen REQ-446 and REQ-422 to cover LiveSpec's meanings, Use other fields for LiveSpec links and kinds, Drop LiveSpec traceability]
---

# Decision Registry

Tracks architecture and design choices with rejected alternatives. Resolved entries are removed — git history holds the record.

---

## DEC-001: LiveSpec's field meanings apply in this repository's *.spec.md files

**Context**: MSL L2 and LiveSpec 5.13.0 define some of the same frontmatter fields differently, in the repository that defines MSL:
- `derives-from:` means "generated or computed from" a source in MSL L2, and an artefact that cannot be recomputed from its sources is misclassified (REQ-416, REQ-446, REQ-446b). LiveSpec uses it for "based on", and its validators require it: foundation and workspace specs derive from `PURPOSE.md`, strategy specs from foundation specs.
- `type:` names a document kind such as template, extension or metaspec in MSL L2 (REQ-422). LiveSpec requires one of its own spec types (contract, behavior, agent and others), and its frontmatter validator rejects any other value.
- `governed-by:` means governance in both. Here MSL's values are metaspec or standard ids, which LiveSpec does not resolve as paths, so the two readings coexist.

**Alternatives considered**: Widening REQ-446 and REQ-422 would change the language to fit one tool, and remains open as a language question. Using other fields is not possible: LiveSpec makes `type:` mandatory for every spec and `derives-from:` mandatory for strategy specs, and the commit hook blocks without them. Dropping LiveSpec traceability would lose the upward links back to `PURPOSE.md`.

**Consequence**: In `*.spec.md` files, `derives-from` means "based on" and `type:` is a LiveSpec type. Only the governance specs (`specs/foundation/`, `specs/strategy/`, `specs/workspace/`) carry `derives-from`; MSL's own specs link upward through `satisfies:` and `guided-by:`. MSL documents that need an MSL `type:` stay outside LiveSpec's spec set: the metaspecs (`type: metaspec`) live in `specs/workspace/metaspecs/` as plain `.md`. `msl-project-organization` dropped `type: standard`, a value MSL does not define. The MSL meanings still hold in the language specs' own text, the documentation and the examples. Anyone reading the `*.spec.md` files as examples of MSL usage sees `derives-from` and `type` used outside their MSL definitions.

**Related**: `specs/interfaces/msl-l2-advanced.spec.md` (REQ-416, REQ-422, REQ-446, REQ-446a, REQ-446b); `specs/workspace/standards/dependencies.spec.md`; `specs/workspace/taxonomy.spec.md`
