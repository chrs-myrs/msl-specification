# Tutorial: Your First MSL Specification

**Time:** 15 minutes  
**Level:** Beginner  
**Outcome:** Create an AI-ready task management specification

## Learning Objectives

By completing this tutorial, you will:

✅ **Write** a complete MSL specification from scratch  
✅ **Structure** requirements for AI implementation  
✅ **Validate** your specification for quality  

## Prerequisites

- Any text editor
- 15 minutes of uninterrupted time
- (Optional) AI assistant to test implementation

## The Scenario

You need a simple task management system. Instead of spending hours prompting an AI with trial and error, you'll write a precise MSL specification that any AI can implement correctly on the first try.

## Step-by-Step Instructions

### Step 1: Create Your Specification File

**Objective:** Set up your first MSL file  
**Action:** Create a new file called `task-manager.md`

```bash
# In your terminal or file explorer
touch task-manager.md
# Or just create a new file in your editor
```

**Verification:** You have an empty file named `task-manager.md`

### Step 2: Add the Document Title

**Objective:** Give your specification a clear name  
**Action:** Add a title using markdown heading

```markdown
# Task Management System
```

**Expected Output:** Your file now has a title  
**Why This Matters:** AI uses the title to understand the system's purpose

### Step 3: Add the Requirements Section (Required!)

**Objective:** Create the mandatory Requirements section  
**Action:** Add the Requirements header and your first requirement

```markdown
# Task Management System

## Requirements
- Users can create tasks with title and description
```

**Verification:** You now have valid MSL Level 0!  
**Common Error:** Using lowercase "requirements" - it must be `## Requirements` with capital R

### Step 4: Add Core Functionality Requirements

**Objective:** Define what the system must do  
**Action:** Add more requirements for core features

```markdown
# Task Management System

## Requirements
- Users can create tasks with title and description
- Tasks have three states: todo, in-progress, done
- Users can update task state
- Users can delete tasks
- Tasks display in a list sorted by creation date
```

**Expected Output:** 5 clear, testable requirements  
**AI Benefit:** Each requirement becomes a specific implementation point

### Step 5: Add Error Handling Requirements

**Objective:** Ensure robust AI implementation  
**Action:** Add requirements for error cases

```markdown
# Task Management System

## Requirements
- Users can create tasks with title and description
- Tasks have three states: todo, in-progress, done
- Users can update task state
- Users can delete tasks
- Tasks display in a list sorted by creation date
- Empty task titles are rejected with error message
- Task state transitions must be valid (todo→in-progress→done)
- Deleted tasks cannot be recovered
```

**Verification:** 8 total requirements including error handling  
**Why This Matters:** Prevents AI from making assumptions about error behavior

### Step 6: Add Performance Requirements

**Objective:** Define non-functional requirements  
**Action:** Add performance and UX requirements

```markdown
# Task Management System

## Requirements
- Users can create tasks with title and description
- Tasks have three states: todo, in-progress, done
- Users can update task state
- Users can delete tasks
- Tasks display in a list sorted by creation date
- Empty task titles are rejected with error message
- Task state transitions must be valid (todo→in-progress→done)
- Deleted tasks cannot be recovered
- Task operations complete within 100ms
- Maximum 1000 tasks supported
- UI updates immediately on state change
```

**Expected Output:** Complete specification with functional and non-functional requirements

### Step 7: Test with AI (Optional but Recommended)

**Objective:** See your specification in action  
**Action:** Give your specification to an AI assistant

```markdown
Prompt: "Please implement this task management system according to the specification in task-manager.md:

[Paste your complete specification]

Use React for the frontend."
```

**Expected Result:** AI generates a complete, working implementation that matches every requirement

### Step 8: Add Structure for Tracking (Level 1)

**Objective:** Enable requirement tracking  
**Action:** Add IDs to requirements

```markdown
# Task Management System

## Requirements
- REQ-001: Users can create tasks with title and description
- REQ-002: Tasks have three states: todo, in-progress, done
- REQ-003: Users can update task state
- REQ-004: Users can delete tasks
- REQ-005: Tasks display in a list sorted by creation date
- REQ-006: Empty task titles are rejected with error message
- REQ-007: Task state transitions must be valid (todo→in-progress→done)
- REQ-008: Deleted tasks cannot be recovered
- REQ-009: Task operations complete within 100ms
- REQ-010: Maximum 1000 tasks supported
- REQ-011: UI updates immediately on state change
```

**Verification:** Each requirement now has a unique ID  
**AI Benefit:** Can reference specific requirements in implementation

### Step 9: Add Metadata (Optional)

**Objective:** Add context for team collaboration  
**Action:** Add frontmatter with metadata

```markdown
---
id: task-manager
version: 1.0
author: Your Name
date: 2024-01-15
tags: [task-management, ui, react]
---
# Task Management System

## Requirements
- REQ-001: Users can create tasks with title and description
- REQ-002: Tasks have three states: todo, in-progress, done
- REQ-003: Users can update task state
- REQ-004: Users can delete tasks
- REQ-005: Tasks display in a list sorted by creation date
- REQ-006: Empty task titles are rejected with error message
- REQ-007: Task state transitions must be valid (todo→in-progress→done)
- REQ-008: Deleted tasks cannot be recovered
- REQ-009: Task operations complete within 100ms
- REQ-010: Maximum 1000 tasks supported
- REQ-011: UI updates immediately on state change
```

**Expected Output:** Complete Level 1 MSL specification

### Step 10: Validate Your Specification

**Objective:** Ensure specification quality  
**Action:** If you have MSL tools installed:

```bash
msl-validate task-manager.md
```

**Expected Output:**
```
✓ task-manager.md
  Quality Score: 88/100
  Testability: 100% (all requirements measurable)
  No critical issues found
```

## Complete Specification

Here's your complete specification:

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
A simple task management system for tracking work items through states.

## Requirements

### Core Functionality
- REQ-001: Users can create tasks with title and description
- REQ-002: Tasks have three states: todo, in-progress, done
- REQ-003: Users can update task state
- REQ-004: Users can delete tasks
- REQ-005: Tasks display in a list sorted by creation date

### Validation & Error Handling
- REQ-006: Empty task titles are rejected with error message
- REQ-007: Task state transitions must be valid (todo→in-progress→done)
- REQ-008: Deleted tasks cannot be recovered

### Performance & Limits
- REQ-009: Task operations complete within 100ms
- REQ-010: Maximum 1000 tasks supported
- REQ-011: UI updates immediately on state change
```

## Verification

Your specification is complete when:

✅ File has `## Requirements` section  
✅ Each requirement is clear and testable  
✅ Error cases are specified  
✅ Performance requirements are included  
✅ AI can implement from specification alone  

Test by asking an AI:
> "Implement the task management system from this specification. Include all requirements."

The AI should build exactly what you specified without asking clarifying questions.

## Common Pitfalls

### Pitfall 1: Vague Requirements
❌ **Wrong:** "Tasks should load quickly"  
✅ **Right:** "Tasks load within 100ms"

### Pitfall 2: Implementation Details
❌ **Wrong:** "Store tasks in PostgreSQL database"  
✅ **Right:** "Tasks persist between sessions"

### Pitfall 3: Missing Error Cases  
❌ **Wrong:** Only happy path requirements  
✅ **Right:** Include validation and error handling

### Pitfall 4: Assumptions
❌ **Wrong:** "Users can edit tasks" (what can they edit?)  
✅ **Right:** "Users can edit task title and description"

### Pitfall 5: No Acceptance Criteria
❌ **Wrong:** "System should be user-friendly"  
✅ **Right:** "All actions complete within 100ms"

## Next Steps

Congratulations! You've written your first MSL specification. You now know how to:
- Structure requirements for AI implementation
- Make requirements testable and clear
- Avoid common specification mistakes

**Ready to level up?** Try these tutorials:

1. [**Adding Validation**](validation.md) - Ensure your specifications meet quality standards
2. [**AI Implementation Workflow**](ai-implementation.md) - Master the spec-to-code workflow
3. [**Using Inheritance**](inheritance.md) - Build on this specification with variants

**Challenge:** Extend your task manager specification with:
- Priority levels (high, medium, low)
- Due dates with overdue highlighting
- Task categories/tags
- Search functionality

Then give it to an AI and watch it build your enhanced system perfectly!

---

**Remember:** MSL turns AI from a guess-and-check tool into a precise implementation partner. Every minute spent on specifications saves hours of debugging and rework.