---
store: registry
type: debt
schema_version: 2
last_reviewed: 2026-11-06
entries:
  - id: DEBT-001
    summary: MSL specs are not *.spec.md, so LiveSpec sees them only through four bridge specs
    severity: medium
    status: open
---

# Debt Registry

Tracks accepted technical/spec shortcuts with known cost. Resolved entries are removed — git history holds the record.

---

## DEBT-001: MSL specs reach LiveSpec only through bridge specs

**Context**: LiveSpec recognises a spec only as a `*.spec.md` file, and counts a file as governed only when a spec's `specifies:` names it. This repository's 24 MSL specs (`specs/msl-l*.md`, `applications/`, `documentation/`, `metaspecs/`, `standards/`, `testing/`, `context7-optimization/`, plus `scripts/*-msl-spec.md`) predate that convention. Four thin bridge specs (`specs/features/msl-documentation.spec.md`, `msl-tools.spec.md`, `specs/artifacts/msl-agents.spec.md`, `repo-scripts.spec.md`) cover the governed paths and point to the detailed MSL spec for each. They were accepted over renaming, because a rename also means moving every spec into a LiveSpec category folder, adding v5 frontmatter and rewriting links across README, docs, llms.txt, INDEX.md and `extends:` paths.
**Impact**: The coverage report still lists 41 ungoverned files: the 24 MSL specs, 11 root configuration files, 4 registries and the 2 script specs. The bridge specs' `specifies:` has to track moves in docs/, tools/, tests/, .claude/agents/ and scripts/. Requirements could drift into a bridge spec instead of the detailed MSL spec.
**Effort**: A dedicated branch: move and rename the 24 specs into LiveSpec categories, add v5 frontmatter and `specifies:`, rewrite links and context7 paths, confirm `tools/lib/resolver.py` still resolves `extends:`, then delete the bridge specs.
