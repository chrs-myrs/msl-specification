# Tutorial: Adding Validation

**Time:** 20 minutes  
**Level:** Beginner  
**Outcome:** Ensure specification quality with automated validation

## Learning Objectives

By completing this tutorial, you will:

✅ **Install** MSL validation tools  
✅ **Validate** specifications for quality and AI-readiness  
✅ **Fix** common validation issues  

## Prerequisites

- Completed [Your First MSL Specification](first-spec.md)
- Node.js installed (for npm)
- Your `task-manager.md` file from the previous tutorial

## The Scenario

You have a specification, but how do you know it's good? Will AI understand it correctly? MSL validation ensures your specifications are clear, complete, and AI-ready before implementation.

## Step-by-Step Instructions

### Step 1: Install MSL Validation Tools

**Objective:** Set up validation environment  
**Action:** Install MSL tools globally

```bash
npm install -g msl-tools
```

**Verification:** Check installation
```bash
msl-validate --version
# Output: msl-validate version 1.0.0
```

**Common Error:** "npm: command not found"  
**Solution:** Install Node.js from [nodejs.org](https://nodejs.org)

### Step 2: Run Your First Validation

**Objective:** Validate your existing specification  
**Action:** Run validation on your task-manager.md

```bash
msl-validate task-manager.md
```

**Expected Output:**
```
Validating: task-manager.md
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ task-manager.md
  Overall Score: 82/100
  
  Quality Breakdown:
  ├─ DRY Compliance: 90/100 ✓
  ├─ Testability: 85/100 ✓
  ├─ Structure: 75/100 ⚠
  └─ Completeness: 80/100 ✓
  
  2 suggestions found (no errors)
```

### Step 3: Understand the Quality Score

**Objective:** Learn what validation checks  
**Action:** Run detailed validation

```bash
msl-validate task-manager.md --verbose
```

**Expected Output:**
```
Detailed Analysis:

DRY Compliance (90/100):
  ✓ No significant text duplication
  ⚠ Minor: "task" appears 15 times (consider using consistent terminology)

Testability (85/100):
  ✓ 11/11 requirements have clear pass/fail criteria
  ⚠ REQ-007: Could be more specific about invalid transitions

Structure (75/100):
  ⚠ Missing Summary section
  ⚠ Requirements not grouped by category
  ✓ Has required Requirements section

Completeness (80/100):
  ✓ Covers core functionality
  ✓ Includes error handling
  ⚠ Missing data persistence requirements
  ⚠ No user authentication specified
```

### Step 4: Fix Structure Issues

**Objective:** Improve specification structure  
**Action:** Add Summary section and group requirements

```markdown
---
id: task-manager
version: 1.0
author: Your Name
date: 2024-01-15
tags: [task-management, ui, react]
---
# Task Management System

## Summary
A simple task management system for tracking work items through states with validation and performance guarantees.

## Requirements

### Core Functionality
- REQ-001: Users can create tasks with title and description
- REQ-002: Tasks have three states: todo, in-progress, done
- REQ-003: Users can update task state
- REQ-004: Users can delete tasks
- REQ-005: Tasks display in a list sorted by creation date

### Validation & Error Handling
- REQ-006: Empty task titles are rejected with error message
- REQ-007: Task state transitions must follow: todo→in-progress→done or todo→done
- REQ-008: Deleted tasks cannot be recovered

### Performance & Limits
- REQ-009: Task operations complete within 100ms
- REQ-010: Maximum 1000 tasks supported
- REQ-011: UI updates immediately on state change
```

**Verification:** Re-run validation
```bash
msl-validate task-manager.md
# Structure score should improve to 90/100
```

### Step 5: Improve Testability

**Objective:** Make requirements more measurable  
**Action:** Add specific criteria to vague requirements

```markdown
### Validation & Error Handling
- REQ-006: Empty task titles are rejected with error message "Title is required"
- REQ-007: Invalid state transitions return 400 error with message "Invalid transition from {current} to {next}"
- REQ-008: Deleted tasks return 404 error when accessed
```

**Expected Result:** Testability score increases to 95/100

### Step 6: Check for DRY Violations

**Objective:** Identify and fix duplication  
**Action:** Run DRY-specific validation

```bash
msl-validate task-manager.md --rules dry
```

**Expected Output:**
```
DRY Analysis:
  
Potential Duplications:
  None detected ✓
  
Consistent Terminology:
  ✓ "task" used consistently (expected)
  ✓ "state" used consistently
  ✓ No conflicting terms
  
Score: 95/100 (Excellent)
```

### Step 7: Add Missing Requirements

**Objective:** Improve completeness  
**Action:** Add data persistence requirements

```markdown
### Data Persistence
- REQ-012: Tasks persist in browser localStorage
- REQ-013: Tasks survive page refresh
- REQ-014: localStorage errors display user-friendly message
```

**Verification:** Check improved completeness
```bash
msl-validate task-manager.md --min-score 85
```

### Step 8: Validate Against AI Readiness

**Objective:** Ensure AI can implement from spec  
**Action:** Run AI-readiness check

```bash
msl-validate task-manager.md --check ai-ready
```

**Expected Output:**
```
AI Readiness Check:
  
✓ Natural language requirements
✓ Clear acceptance criteria
✓ No implementation details
✓ Technology agnostic
✓ Measurable outcomes
  
AI Readiness: 100% ✓
  
This specification is ready for AI implementation.
Estimated tokens: 450 (fits all context windows)
```

### Step 9: Set Up Continuous Validation

**Objective:** Automate validation in your workflow  
**Action:** Create validation configuration

Create `.msl-validate.yml`:
```yaml
# MSL Validation Configuration
version: 1

# Quality thresholds
quality:
  min-overall-score: 85
  min-testability: 90
  min-dry-score: 85

# Validation rules
rules:
  dry-compliance:
    enabled: true
    threshold: 85
  testability:
    enabled: true
    min-score: 90
  ai-readiness:
    enabled: true
    required: true

# File patterns
include:
  - "*.md"
  - "specs/**/*.md"
exclude:
  - "README.md"
  - "docs/**/*.md"

# Output
output:
  format: text
  verbose: false
  colors: true
```

**Verification:** Run with config
```bash
msl-validate
# Automatically uses .msl-validate.yml configuration
```

### Step 10: Fix All Issues

**Objective:** Achieve excellent quality score  
**Action:** Apply all improvements

Final specification:
```markdown
---
id: task-manager
version: 1.0
author: Your Name
date: 2024-01-15
tags: [task-management, ui, react]
---
# Task Management System

## Summary
A simple task management system for tracking work items through defined states with validation, persistence, and performance guarantees.

## Requirements

### Core Functionality
- REQ-001: Users can create tasks with title (required) and description (optional)
- REQ-002: Tasks have three states: todo, in-progress, done
- REQ-003: Users can update task state following valid transitions
- REQ-004: Users can permanently delete tasks
- REQ-005: Tasks display in list sorted by creation date (newest first)

### Validation & Error Handling
- REQ-006: Empty task titles are rejected with error message "Title is required"
- REQ-007: Invalid state transitions return 400 error with message "Invalid transition from {current} to {next}"
- REQ-008: Deleted tasks return 404 error when accessed

### Performance & Limits
- REQ-009: All task operations complete within 100ms
- REQ-010: System supports maximum 1000 tasks
- REQ-011: UI updates immediately (<16ms) on state change

### Data Persistence
- REQ-012: Tasks persist in browser localStorage
- REQ-013: Tasks survive page refresh without data loss
- REQ-014: localStorage errors display "Unable to save tasks" with retry option
```

**Final Validation:**
```bash
msl-validate task-manager.md

✓ task-manager.md
  Overall Score: 95/100 (Excellent!)
  
  ├─ DRY Compliance: 95/100 ✓
  ├─ Testability: 100/100 ✓
  ├─ Structure: 95/100 ✓
  ├─ Completeness: 90/100 ✓
  └─ AI Readiness: 100/100 ✓
  
  Ready for AI implementation!
```

## Verification

Your validation setup is complete when:

✅ MSL tools are installed and working  
✅ Your specification scores ≥85/100  
✅ All requirements are testable  
✅ AI readiness check passes  
✅ Configuration file is created  

## Common Pitfalls

### Pitfall 1: Ignoring Low Scores
❌ **Wrong:** "75/100 is good enough"  
✅ **Right:** Fix issues until score ≥85/100

### Pitfall 2: Skipping AI Readiness
❌ **Wrong:** Assuming AI will understand  
✅ **Right:** Run `--check ai-ready` before implementation

### Pitfall 3: Over-Specifying
❌ **Wrong:** Adding implementation details to improve score  
✅ **Right:** Keep requirements behavior-focused

### Pitfall 4: Ignoring Warnings
❌ **Wrong:** Only fixing errors  
✅ **Right:** Address warnings for better quality

### Pitfall 5: Not Automating
❌ **Wrong:** Manual validation each time  
✅ **Right:** Set up `.msl-validate.yml` configuration

## Debugging Tips

1. **Score too low?** Run `--verbose` to see specifics
2. **DRY violations?** Look for repeated phrases
3. **Testability issues?** Add measurable criteria
4. **Structure problems?** Add Summary and group requirements
5. **Completeness gaps?** Think about edge cases

## Next Steps

Excellent! You now know how to:
- Validate specifications for quality
- Fix common validation issues  
- Ensure AI readiness

**Continue learning:**

1. [**AI Implementation Workflow**](ai-implementation.md) - Use validated specs with AI
2. [**CI/CD Integration**](cicd.md) - Automate validation in pipelines
3. [**Custom Validation Rules**](custom-validation.md) - Domain-specific checks

**Challenge:** Create a new specification and achieve 100/100 score:
- Shopping cart system
- User authentication
- Blog platform

Validate each and ensure AI can implement perfectly!

---

**Pro Tip:** High-quality specifications lead to high-quality AI implementations. Every point of validation score translates to fewer bugs and less rework.