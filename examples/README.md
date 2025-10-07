# MSL Examples

This directory contains examples demonstrating MSL at different complexity levels.

## Directory Structure

- **minimal/** - Level 0: Pure markdown, no special syntax required
- **basic/** - Level 1: Basic structure with IDs
- **advanced/** - Level 2: Full metadata, inheritance, variables
- **templates/** - Reusable template patterns
- **real-world/** - Complete real-world specifications

## Quick Tour

### Minimal (Level 0)
Start here if you're new to MSL. These are just markdown files with a requirements section.

### Basic (Level 1)
Add IDs when you need to reference requirements or track them individually.

### Advanced (Level 2)
Use full metadata for enterprise features like inheritance, workflow states, and templates.

### Templates
Reusable patterns you can extend for common specification types.

### Real-World
Complete examples from actual projects showing MSL in production use.

- **LiveSpec**: Large-scale governance framework (51 specs) - https://github.com/chrs-myrs/livespec

## Running Examples

Validate any example:
```bash
msl-lint examples/basic/login.md
```

Render a template:
```bash
msl-render examples/templates/api.md -v service_name=UserAPI
```

Check all examples:
```bash
msl-lint examples/
```