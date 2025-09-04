# Solo Developer MSL Workflow

**Complete guide for individual developers using MSL to manage personal specifications. Learn productivity patterns, organization strategies, and tooling setup for effective solo specification development.**

## Introduction

Working solo doesn't mean working without structure. MSL helps individual developers maintain clarity, track decisions, and build maintainable systems—even in single-person projects.

## Getting Started (Week 1)

### Day 1: First Specification

**Morning: Setup**
```bash
# Create project structure
mkdir -p my-project/specs
cd my-project

# Initialize git
git init
echo "specs/" >> .gitignore  # Initially ignore specs

# Create first spec
echo "# Login Feature

## Requirements
- Users can log in with email
- Session lasts 24 hours
- Show error for wrong password" > specs/login.md
```

**Afternoon: Validation**
```bash
# Install MSL tools locally
npm init -y
npm install --save-dev msl-tools

# Add validation script
npm set-script validate "msl-validate ./specs/"

# Run first validation
npm run validate
```

**Evening: Commit**
```bash
# Happy with spec? Track it
git add specs/login.md
git commit -m "Add login specification"
```

### Day 2-5: Building Momentum

```markdown
# Daily Workflow Pattern
1. Morning: Write/update specifications (30 min)
2. Code implementation based on specs
3. Evening: Validate and update specs (15 min)
4. Commit spec + code together
```

### Week 1 Checklist
- [ ] Created 3-5 basic specifications
- [ ] Set up validation tools
- [ ] Established daily rhythm
- [ ] Committed specs with code

## File Organization Strategies

### Small Projects (1-10 specs)

```
project/
├── specs/
│   ├── auth.md
│   ├── api.md
│   ├── database.md
│   └── ui-components.md
├── src/
└── package.json
```

**Key Points:**
- Flat structure
- One spec per major feature
- Keep specs next to code

### Medium Projects (10-50 specs)

```
project/
├── specs/
│   ├── core/
│   │   ├── auth.md
│   │   ├── data-model.md
│   │   └── api-base.md
│   ├── features/
│   │   ├── user-profile.md
│   │   ├── search.md
│   │   └── notifications.md
│   └── infrastructure/
│       ├── database.md
│       ├── caching.md
│       └── deployment.md
├── src/
└── .msl-validate.yml
```

**Organization Rules:**
1. Group by domain/layer
2. Core specs = stable, rarely change
3. Feature specs = evolve with development
4. Infrastructure = deployment/ops concerns

### Large Projects (50+ specs)

```
project/
├── specs/
│   ├── index.md           # Root navigation
│   ├── templates/         # Reusable patterns
│   │   ├── api-endpoint.md
│   │   └── database-table.md
│   ├── core/
│   │   └── [domain folders]
│   ├── features/
│   │   └── [feature folders]
│   ├── archive/          # Old specs
│   │   └── v1/
│   └── .navigation.yml   # Spec relationships
├── docs/                 # Generated from specs
└── tools/
    └── validate.sh      # Custom validation
```

## Productivity Patterns

### Pattern 1: Specification-First Development

**Trigger:** Starting new feature  
**Actions:**
1. Write specification (15-30 min)
2. Validate specification
3. Implement to spec
4. Update spec if reality differs

**Outcome:** Clear implementation target, documented decisions

**Example:**
```bash
# Morning planning
vim specs/new-feature.md
# Write requirements

# Validate before coding
msl-validate specs/new-feature.md

# Generate todo list from spec
grep "REQ-" specs/new-feature.md | sed 's/.*REQ/TODO REQ/' > TODO.md

# Code with spec open in split view
code --diff specs/new-feature.md src/feature.ts
```

**Time Estimate:** 15-30 min overhead, saves 2-4 hours debugging

### Pattern 2: Incremental Refinement

**Trigger:** Understanding evolves during implementation  
**Actions:**
1. Start with Level 0 (markdown)
2. Add IDs when tracking needed (Level 1)
3. Extract patterns to templates (Level 2)

**Outcome:** Specifications grow with understanding

**Example Timeline:**
```markdown
# Day 1: Quick notes
- Need user authentication
- Should work on mobile

# Day 5: Structured requirements
- REQ-001: OAuth 2.0 authentication
- REQ-002: Responsive design 320px-2048px

# Day 20: Template extraction
extends: auth-template
variables:
  provider: "Google OAuth"
  session_duration: 7200
```

### Pattern 3: Daily Specification Review

**Trigger:** End of workday  
**Actions:**
1. Review today's code changes
2. Update affected specifications
3. Run validation
4. Note tomorrow's spec updates

**Outcome:** Specs stay synchronized

**Daily Review Script:**
```bash
#!/bin/bash
# daily-review.sh

echo "=== Today's Changes ==="
git diff --name-only | grep -E "\.(ts|js|py)$"

echo "=== Affected Specs ==="
git diff --name-only | grep "\.md$"

echo "=== Validation ==="
msl-validate ./specs/ --changed-only

echo "=== Tomorrow's TODOs ==="
grep -r "TODO\|FIXME" specs/ | head -5
```

**Time: 10-15 minutes/day**

### Pattern 4: Refactoring with Confidence

**Trigger:** Code needs restructuring  
**Actions:**
1. Update specification first
2. Validate spec changes
3. Refactor code to match
4. Verify against spec

**Outcome:** Controlled refactoring

**Example:**
```bash
# Before refactoring
cp specs/monolith.md specs/monolith.backup.md

# Plan refactor in spec
vim specs/microservices.md

# Validate plan
msl-validate specs/microservices.md

# Execute refactor
./refactor-to-microservices.sh

# Verify result matches spec
msl-validate --check-implementation specs/microservices.md src/
```

### Pattern 5: Knowledge Capture

**Trigger:** Learning something new  
**Actions:**
1. Document in specification
2. Add examples
3. Create template if reusable

**Outcome:** Reusable knowledge base

**Capture Template:**
```markdown
# Learning: [Topic]
Date: [Today]

## What I Learned
- Key insight
- Important constraint
- Useful pattern

## Requirements (if applicable)
- REQ-XXX: Concrete requirement from learning

## Examples
\```code
// Working example
\```

## Anti-patterns
- What doesn't work and why
```

## Tooling Setup

### Essential Tools

**1. Editor Configuration (VS Code)**
```json
{
  "files.associations": {
    "*.msl": "markdown"
  },
  "msl.autoValidate": true,
  "msl.validateOnSave": true,
  "editor.wordWrap": "on",
  "markdown.preview.breaks": true
}
```

**2. Git Hooks**
```bash
# .git/hooks/pre-commit
#!/bin/bash
msl-validate ./specs/ --min-score 80 || {
  echo "Specification validation failed"
  exit 1
}
```

**3. Personal Dashboard**
```html
<!-- specs/dashboard.html -->
<!DOCTYPE html>
<html>
<head>
  <title>Spec Dashboard</title>
  <script>
    // Auto-refresh every 30s
    setTimeout(() => location.reload(), 30000);
  </script>
</head>
<body>
  <iframe src="../validation-report.html"></iframe>
  <iframe src="../coverage-report.html"></iframe>
</body>
</html>
```

**4. Quick Commands (`.bashrc`)**
```bash
alias spnew='touch specs/$(date +%Y%m%d)-draft.md'
alias spval='msl-validate ./specs/'
alias sprender='msl-render ./specs/ -o docs/'
alias spclean='rm specs/*.backup.md'
```

**5. Weekly Report Generator**
```bash
#!/bin/bash
# weekly-spec-report.sh

echo "# Weekly Specification Report"
echo "Week of $(date +%Y-%m-%d)"
echo ""
echo "## New Specifications"
find specs/ -mtime -7 -name "*.md" | wc -l
echo ""
echo "## Modified Specifications"
git log --since="1 week ago" --name-only | grep "specs/.*\.md" | sort | uniq
echo ""
echo "## Quality Metrics"
msl-validate ./specs/ --summary-only
```

## Maintenance Patterns

### Specification Gardening

**Weekly Tasks (30 min):**
1. Archive obsolete specs
2. Update index/navigation
3. Extract common patterns
4. Fix validation warnings

```bash
# Weekly gardening script
#!/bin/bash

# Archive old specs
find specs/ -name "*.deprecated.md" -mtime +30 \
  -exec mv {} specs/archive/ \;

# Update index
echo "# Specifications Index" > specs/index.md
echo "" >> specs/index.md
find specs/ -name "*.md" -not -path "*/archive/*" \
  | sort | while read f; do
    title=$(grep "^# " "$f" | head -1 | sed 's/# //')
    echo "- [$title]($f)" >> specs/index.md
done

# Check for patterns
msl-validate ./specs/ --find-patterns > patterns.md
```

### Version Migration

**When to Version:**
- Major feature changes
- Breaking API changes
- Significant refactoring

**Versioning Strategy:**
```bash
# Create version snapshot
cp specs/api.md specs/archive/api-v1.md
echo "Archived: $(date)" >> specs/archive/api-v1.md

# Update current spec
sed -i 's/version: 1.0/version: 2.0/' specs/api.md

# Add migration notes
echo "## Migration from v1" >> specs/api.md
echo "- Breaking: Changed auth method" >> specs/api.md
```

## Advanced Solo Techniques

### Self-Review Checklist

Before committing specifications:

```markdown
## Specification Quality Checklist
- [ ] Requirements are testable
- [ ] No duplicate requirements
- [ ] Examples provided for complex requirements
- [ ] Validation score > 80
- [ ] Related code references updated
- [ ] TODOs addressed or documented
```

### Personal Quality Metrics

Track your specification quality over time:

```javascript
// track-quality.js
const { validate } = require('msl-tools');
const fs = require('fs');

async function trackQuality() {
  const result = await validate('./specs/', {
    recursive: true
  });
  
  const metrics = {
    date: new Date().toISOString(),
    score: result.averageScore,
    files: result.fileCount,
    issues: result.totalIssues
  };
  
  // Append to metrics log
  fs.appendFileSync('spec-metrics.jsonl', 
    JSON.stringify(metrics) + '\n');
  
  // Generate trend chart
  generateChart('spec-metrics.jsonl', 'quality-trend.png');
}
```

### Learning from Mistakes

Keep a specification journal:

```markdown
# specs/lessons-learned.md

## 2024-01-15: Over-specification
**Mistake:** Specified implementation details
**Impact:** Had to update spec 5 times during coding
**Learning:** Specify behavior, not implementation
**Example:**
- Bad: "Store password as bcrypt hash with salt rounds 10"
- Good: "Store password securely, resistant to rainbow tables"

## 2024-01-20: Missing Error Cases
**Mistake:** Only specified happy path
**Impact:** Discovered 3 error cases during testing
**Learning:** Always include error requirements
**Template:**
- REQ-XXX: Normal behavior
- REQ-XXX-ERR-1: Error case 1
- REQ-XXX-ERR-2: Error case 2
```

## Adoption Roadmap

### Week 1: Foundation
- [ ] Install MSL tools
- [ ] Write first 3 specifications
- [ ] Set up basic validation
- [ ] Commit specs with code

### Week 2: Rhythm
- [ ] Daily specification updates
- [ ] Organize specs into folders
- [ ] Add git hooks
- [ ] Create first template

### Week 3: Automation
- [ ] Set up CI validation
- [ ] Create personal dashboard
- [ ] Automate reports
- [ ] Extract common patterns

### Week 4: Mastery
- [ ] All new features start with spec
- [ ] Quality score consistently >85
- [ ] Templates for common patterns
- [ ] Specification-driven development

## Common Obstacles and Solutions

### Obstacle 1: "I forget to update specs"
**Solution:** Git hooks + daily review ritual
```bash
# Force spec update check
git diff --name-only | grep -E "\.(ts|js|py)$" && \
  echo "Remember to update specifications!"
```

### Obstacle 2: "Specs feel like overhead"
**Solution:** Start minimal, grow incrementally
- Week 1: Just bullet points
- Week 2: Add requirement IDs
- Week 3: Add validation
- Week 4: Extract templates

### Obstacle 3: "I work on multiple projects"
**Solution:** Global MSL configuration
```bash
# ~/.msl-global.yml
defaults:
  minScore: 80
  author: "Your Name"
  
projects:
  project-a:
    path: ~/projects/a/specs
  project-b:
    path: ~/projects/b/specs
```

### Obstacle 4: "Specs get out of date"
**Solution:** Specification-code proximity
- Put specs near code they specify
- Link specs from code comments
- Update both in same commit

### Obstacle 5: "Too many specs to manage"
**Solution:** Progressive organization
1. Start flat (1-10 specs)
2. Group by domain (10-50 specs)
3. Add navigation/index (50+ specs)
4. Create templates for patterns

## Success Metrics

Track these KPIs weekly:

| Metric | Target | Measure |
|--------|--------|---------|
| Specification Coverage | >80% | Features with specs / Total features |
| Quality Score | >85 | Average validation score |
| Sync Rate | >90% | Specs updated with code / Code changes |
| Reuse Rate | >30% | Specs using templates / Total specs |
| Time to Spec | <30min | Average time to write specification |

## Day in the Life

**7:00 AM - Morning Planning (15 min)**
```bash
# Review yesterday's work
git log --oneline --since="yesterday"

# Check specification TODOs
grep -r "TODO" specs/ | head -10

# Plan today's specs
echo "Today: Auth refactor" >> specs/today.md
```

**10:00 AM - Feature Development (2 hours)**
```bash
# Write specification first
vim specs/new-feature.md

# Validate before coding
msl-validate specs/new-feature.md

# Code with spec visible
code --diff specs/new-feature.md src/feature.ts
```

**2:00 PM - Afternoon Review (10 min)**
```bash
# Quick validation check
msl-validate ./specs/ --changed-only

# Update specs based on morning's learning
git diff specs/
```

**5:00 PM - End of Day (15 min)**
```bash
# Final validation
npm run validate

# Commit spec and code together
git add specs/ src/
git commit -m "Add new feature with specification"

# Note tomorrow's tasks
echo "Tomorrow: Test error cases" >> specs/tomorrow.md
```

## Anti-Patterns to Avoid

### Anti-Pattern 1: Specification After Implementation
**Why it's bad:** Specs become documentation, not design tools
**Better approach:** Write specs first, update during implementation

### Anti-Pattern 2: Over-Detailed Specifications
**Why it's bad:** Brittle, requires constant updates
**Better approach:** Specify behavior, not implementation

### Anti-Pattern 3: Ignoring Validation Warnings
**Why it's bad:** Quality degrades over time
**Better approach:** Fix warnings immediately or document why they're acceptable

### Anti-Pattern 4: Copy-Paste Specifications
**Why it's bad:** Violates DRY, maintenance nightmare
**Better approach:** Extract templates, use inheritance

### Anti-Pattern 5: Abandoned Specifications
**Why it's bad:** Creates confusion, reduces trust
**Better approach:** Archive or delete obsolete specs

## Next Steps

Ready to collaborate? Check out the [Team Workflow Guide](team.md).

Want AI assistance? See the [AI Integration Workflow](ai.md).

---

**Remember:** Solo doesn't mean unstructured. MSL helps you think clearly, work systematically, and build maintainable systems—even when you're the only one who will ever read the specifications.