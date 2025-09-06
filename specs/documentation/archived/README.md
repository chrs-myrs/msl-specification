# Archived Documentation Specifications

This directory contains documentation specifications that have been consolidated or merged to reduce duplication and follow DRY principles.

## Consolidation Summary

### Merged into msl-docs-base.md
- **msl-docs-root.md** - Common requirements moved to base, documentation system architecture concepts preserved

### Merged into other specs
- **msl-docs-why-msl.md** - Value proposition content merged into getting-started
- **msl-docs-tools.md** - Tool documentation requirements merged into reference
- **msl-docs-workflows.md** - Workflow guides merged into tutorials
- **msl-docs-project.md** - Project documentation merged into user-guide
- **msl-docs-readme.md** - README requirements merged into getting-started

## Rationale

These specifications were archived as part of a simplification effort to:
1. Eliminate redundant requirements across documentation specs
2. Implement proper inheritance using `extends:`
3. Reduce complexity by consolidating similar documentation types
4. Follow the DRY (Don't Repeat Yourself) principle

## Active Documentation Specs

The current simplified structure includes:
- `msl-docs-base.md` - Common documentation requirements
- `msl-docs-getting-started.md` - Quick start (extends base)
- `msl-docs-user-guide.md` - Comprehensive guide (extends base)
- `msl-docs-reference.md` - Technical reference (extends base)
- `msl-docs-tutorials.md` - Hands-on learning (extends base)

All documentation specs are now governed by `msl-documentation-metaspec.md`.

## Note

These archived specifications are retained for historical reference and to preserve any unique concepts that may be useful in the future. They should not be used for new documentation generation.