# Tutorial: Using Inheritance

**Time:** 25 minutes  
**Level:** Intermediate  
**Outcome:** Build specification families with inheritance

## Learning Objectives

By completing this tutorial, you will:

✅ **Understand** the "IS-A" relationship rule for inheritance  
✅ **Create** child specifications that extend parents  
✅ **Avoid** common inheritance mistakes  

## Prerequisites

- Completed [Your First MSL Specification](first-spec.md)
- Understanding of MSL Level 1 (IDs and structure)
- A base specification to extend

## The Scenario

Your task manager was successful! Now the enterprise team wants a "Pro" version with additional features. Instead of duplicating the specification, you'll use inheritance to build on the existing one.

## Step-by-Step Instructions

### Step 1: Understand the IS-A Test

**Objective:** Learn when inheritance is appropriate  
**Action:** Apply the IS-A test

Ask yourself: "IS the new specification A type of the parent?"

✅ **CORRECT Examples:**
- Pro Task Manager **IS-A** Task Manager (with more features)
- Admin User **IS-A** User (with elevated privileges)  
- Electric Car **IS-A** Car (with different power source)

❌ **INCORRECT Examples:**
- Documentation **IS-NOT-A** Specification
- Login Page **IS-NOT-A** User System
- Task Manager Settings **IS-NOT-A** Task Manager

**The Rule:** Only use `extends` when the child is truly a specialized version of the parent.

### Step 2: Prepare the Parent Specification

**Objective:** Set up base specification for inheritance  
**Action:** Save your task-manager.md as the parent

```bash
# Ensure parent spec has an ID
cat task-manager.md | grep "id:"
# Should show: id: task-manager
```

Parent specification (task-manager.md):
```markdown
---
id: task-manager
version: 1.0
---
# Task Management System

## Requirements
- REQ-001: Users can create tasks with title and description
- REQ-002: Tasks have three states: todo, in-progress, done
- REQ-003: Users can update task state
- REQ-004: Users can delete tasks
- REQ-005: Tasks display in list sorted by creation date
```

### Step 3: Create Child Specification

**Objective:** Create pro version that extends base  
**Action:** Create task-manager-pro.md

```markdown
---
id: task-manager-pro
version: 1.0
extends: task-manager
---
# Task Management Pro

## Summary
Enterprise task management system with advanced features extending the base task manager.

## Requirements
```

**Key Point:** The `extends: task-manager` line inherits all parent requirements

### Step 4: Add New Requirements

**Objective:** Add pro-only features  
**Action:** Add requirements with [NEW] marker

```markdown
---
id: task-manager-pro
version: 1.0
extends: task-manager
---
# Task Management Pro

## Summary
Enterprise task management system with advanced features extending the base task manager.

## Requirements

### Additional Features
- REQ-010: [NEW] Tasks can have assignees (multiple users)
- REQ-011: [NEW] Tasks support file attachments (max 10MB each)
- REQ-012: [NEW] Tasks have priority levels: critical, high, medium, low
- REQ-013: [NEW] Tasks can have due dates with overdue warnings
- REQ-014: [NEW] Tasks support markdown in descriptions
```

**Verification:** Pro version now has all 5 base requirements plus 5 new ones

### Step 5: Override Parent Requirements

**Objective:** Modify inherited behavior  
**Action:** Override specific parent requirements

```markdown
## Requirements

### Modified Base Behavior
- REQ-002: [OVERRIDE] Tasks have five states: todo, in-progress, review, testing, done
- REQ-005: [OVERRIDE] Tasks display with priority sorting, then by date

### Additional Features  
- REQ-010: [NEW] Tasks can have assignees (multiple users)
- REQ-011: [NEW] Tasks support file attachments (max 10MB each)
- REQ-012: [NEW] Tasks have priority levels: critical, high, medium, low
- REQ-013: [NEW] Tasks can have due dates with overdue warnings
- REQ-014: [NEW] Tasks support markdown in descriptions
```

**Important:** Use the same REQ-ID as parent to override

### Step 6: Validate Inheritance

**Objective:** Ensure valid inheritance structure  
**Action:** Validate the child specification

```bash
msl-validate task-manager-pro.md --check-inheritance
```

**Expected Output:**
```
Inheritance Analysis:
  
Parent: task-manager.md ✓
  - Found and loaded successfully
  - 5 requirements inherited
  
Child: task-manager-pro.md
  - 2 requirements overridden (REQ-002, REQ-005)
  - 5 new requirements added
  - 3 requirements inherited unchanged
  
Total Requirements: 10
No circular inheritance ✓
Depth: 1 (Maximum: 3) ✓
```

### Step 7: Common Inheritance Mistake - Wrong Relationship

**Objective:** Learn from a common mistake  
**Action:** See what NOT to do

❌ **WRONG - Creating task-manager-docs.md:**
```markdown
---
id: task-manager-docs
extends: task-manager  # WRONG! Docs are not a type of task manager
---
# Task Manager Documentation
```

**Why it's wrong:** Documentation describes the system but IS-NOT-A system itself

✅ **CORRECT - Use references instead:**
```markdown
---
id: task-manager-docs
references:
  - task-manager: "System being documented"
---
# Task Manager Documentation
```

### Step 8: Build Inheritance Chain

**Objective:** Create multi-level inheritance  
**Action:** Create enterprise version extending pro

```markdown
---
id: task-manager-enterprise
version: 1.0
extends: task-manager-pro
---
# Task Management Enterprise

## Summary
Multi-team task management with advanced security and compliance features.

## Requirements

### Enterprise Features
- REQ-020: [NEW] Tasks support team namespaces
- REQ-021: [NEW] Role-based access control (RBAC) for tasks
- REQ-022: [NEW] Audit log for all task modifications
- REQ-023: [NEW] SSO integration for authentication
- REQ-024: [NEW] Data encryption at rest and in transit

### Modified Pro Behavior
- REQ-011: [OVERRIDE] File attachments support up to 100MB with virus scanning
```

**Inheritance Chain:**
```
task-manager (5 requirements)
    └── task-manager-pro (10 requirements) 
            └── task-manager-enterprise (15 requirements)
```

### Step 9: Verify Complete Inheritance

**Objective:** Understand full requirement set  
**Action:** Generate flattened specification

```bash
# Tool to show all inherited requirements
msl-validate task-manager-enterprise.md --show-inherited
```

**Output:**
```markdown
## Inherited Requirements (Flattened View)

From task-manager:
- REQ-001: Users can create tasks with title and description
- REQ-003: Users can update task state  
- REQ-004: Users can delete tasks

From task-manager (overridden by task-manager-pro):
- REQ-002: Tasks have five states: todo, in-progress, review, testing, done
- REQ-005: Tasks display with priority sorting, then by date

From task-manager-pro:
- REQ-010: Tasks can have assignees (multiple users)
- REQ-012: Tasks have priority levels: critical, high, medium, low
- REQ-013: Tasks can have due dates with overdue warnings
- REQ-014: Tasks support markdown in descriptions

From task-manager-pro (overridden by task-manager-enterprise):
- REQ-011: File attachments support up to 100MB with virus scanning

From task-manager-enterprise:
- REQ-020: Tasks support team namespaces
- REQ-021: Role-based access control (RBAC) for tasks
- REQ-022: Audit log for all task modifications
- REQ-023: SSO integration for authentication
- REQ-024: Data encryption at rest and in transit
```

### Step 10: Use Inheritance with AI

**Objective:** Have AI implement inherited specification  
**Action:** Give AI the complete chain

```markdown
"Please implement the enterprise task management system. Here are the specifications in inheritance order:

1. BASE SPECIFICATION (task-manager.md):
[Paste base spec]

2. PRO SPECIFICATION (task-manager-pro.md):
[Paste pro spec with extends: task-manager]

3. ENTERPRISE SPECIFICATION (task-manager-enterprise.md):
[Paste enterprise spec with extends: task-manager-pro]

Implement the complete enterprise version with all inherited and overridden requirements."
```

**AI Understanding:** AI will correctly merge all requirements and implement the complete system

## Complete Example Specifications

### Base (task-manager.md)
```markdown
---
id: task-manager
version: 1.0
---
# Task Management System

## Requirements
- REQ-001: Users can create tasks with title and description
- REQ-002: Tasks have three states: todo, in-progress, done
- REQ-003: Users can update task state
- REQ-004: Users can delete tasks
- REQ-005: Tasks display in list sorted by creation date
```

### Pro (task-manager-pro.md)
```markdown
---
id: task-manager-pro
version: 1.0
extends: task-manager
---
# Task Management Pro

## Requirements

### Modified Base Behavior
- REQ-002: [OVERRIDE] Tasks have five states: todo, in-progress, review, testing, done
- REQ-005: [OVERRIDE] Tasks display with priority sorting, then by date

### Additional Features
- REQ-010: [NEW] Tasks can have assignees (multiple users)
- REQ-011: [NEW] Tasks support file attachments (max 10MB each)
- REQ-012: [NEW] Tasks have priority levels: critical, high, medium, low
- REQ-013: [NEW] Tasks can have due dates with overdue warnings
- REQ-014: [NEW] Tasks support markdown in descriptions
```

### Enterprise (task-manager-enterprise.md)
```markdown
---
id: task-manager-enterprise  
version: 1.0
extends: task-manager-pro
---
# Task Management Enterprise

## Requirements

### Enterprise Features
- REQ-020: [NEW] Tasks support team namespaces
- REQ-021: [NEW] Role-based access control (RBAC) for tasks
- REQ-022: [NEW] Audit log for all task modifications
- REQ-023: [NEW] SSO integration for authentication
- REQ-024: [NEW] Data encryption at rest and in transit

### Modified Pro Behavior
- REQ-011: [OVERRIDE] File attachments support up to 100MB with virus scanning
```

## Verification

Your inheritance structure is correct when:

✅ IS-A test passes for all inheritance  
✅ Child specifications extend appropriate parents  
✅ Override markers used for modified requirements  
✅ New markers used for additional requirements  
✅ No circular inheritance exists  
✅ Inheritance depth ≤ 3 levels  

## Common Pitfalls

### Pitfall 1: Wrong Relationship
❌ **Wrong:** `api-docs extends: api-spec`  
✅ **Right:** `api-v2 extends: api-v1`  
**Test:** Docs are not a type of API

### Pitfall 2: Forgetting Markers
❌ **Wrong:** `REQ-010: New requirement` (no marker)  
✅ **Right:** `REQ-010: [NEW] New requirement`  
**Why:** Markers clarify inheritance behavior

### Pitfall 3: Wrong ID for Override
❌ **Wrong:** `REQ-999: [OVERRIDE] Modified behavior`  
✅ **Right:** `REQ-002: [OVERRIDE] Modified behavior`  
**Rule:** Use parent's REQ-ID to override

### Pitfall 4: Deep Inheritance
❌ **Wrong:** 5+ levels of inheritance  
✅ **Right:** Maximum 3 levels  
**Why:** Deep chains become hard to understand

### Pitfall 5: Circular Inheritance
❌ **Wrong:** A extends B, B extends A  
✅ **Right:** Clear parent-child direction  
**Check:** `msl-validate --check-inheritance`

## The IS-A Test Questions

Before using `extends`, ask these questions:

1. **Can I say "X IS-A Y"?**
   - ✅ "Pro Task Manager IS-A Task Manager"
   - ❌ "Documentation IS-A Task Manager"

2. **Does the child specialize the parent?**
   - ✅ Pro version adds enterprise features
   - ❌ Settings page isn't a specialization

3. **Would inheritance create confusion?**
   - ✅ Clear relationship is obvious
   - ❌ Forced relationship needs explanation

4. **Could composition work better?**
   - ✅ True IS-A needs inheritance
   - ❌ HAS-A relationship needs references

5. **Is the depth reasonable?**
   - ✅ 1-3 levels of inheritance
   - ❌ 4+ levels indicates wrong pattern

## Next Steps

Excellent! You now understand MSL inheritance:
- When to use extends (IS-A test)
- How to override and extend
- Common mistakes to avoid

**Continue learning:**

1. [**Creating Templates**](templates.md) - Reusable specification patterns
2. [**Building Specification Sets**](spec-sets.md) - Architect complete systems
3. [**Team Collaboration**](team-specs.md) - Coordinate inherited specs

**Challenge:** Create a product family:
- Basic Blog Platform
- Pro Blog (extends Basic)
- Enterprise Blog (extends Pro)

Each level should truly be a specialized version of its parent!

---

**Remember:** Inheritance is powerful but often overused. When in doubt, prefer composition with references over inheritance with extends.