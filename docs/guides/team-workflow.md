# Team Workflow Guide

> How teams can collaborate effectively using MSL

## Team Benefits

MSL enables teams to:
- **Review specs in pull requests** - See exactly what changed
- **Merge specifications** - Git handles conflicts naturally
- **Share templates** - Standardize without rigidity
- **Track ownership** - Know who owns what
- **Maintain history** - See how specs evolved

## Getting Started as a Team

### 1. Establish Conventions

Create a `SPEC_CONVENTIONS.md`:

```markdown
# Specification Conventions

## File Structure
- Specs go in `/specs` directory
- Use kebab-case for filenames
- Group by feature area

## ID Format
- Use REQ-XXX for requirements
- Sequential numbering within files
- Prefix with component (AUTH-REQ-001)

## Required Frontmatter
- id: Unique identifier
- owner: GitHub username
- status: draft|review|approved|deprecated

## Review Process
- All specs require PR review
- Tag domain experts for review
- Approval from tech lead required
```

### 2. Directory Structure

```
project/
├── specs/
│   ├── templates/
│   │   ├── api-spec.md
│   │   └── feature-spec.md
│   ├── architecture/
│   │   └── system-design.md
│   ├── features/
│   │   ├── authentication.md
│   │   └── payments.md
│   └── README.md
```

### 3. Template Library

Create shared templates in `specs/templates/`:

```markdown
---
id: api-template
type: template
---

# ${service_name} API

## Metadata
- Owner: ${owner}
- Status: ${status}
- Version: ${version}

## Requirements
- REQ-001: RESTful design
- REQ-002: JSON request/response
- REQ-003: Authentication required
- REQ-004: Rate limiting: ${rate_limit} rpm
```

## Collaboration Patterns

### Feature Development

1. **Developer creates spec**
```bash
git checkout -b feature/user-profiles
cp specs/templates/feature-spec.md specs/features/user-profiles.md
# Edit spec...
```

2. **Open PR for review**
```bash
git add specs/features/user-profiles.md
git commit -m "Add user profiles specification"
git push origin feature/user-profiles
# Create PR
```

3. **Team reviews in PR**
- Comments on specific lines
- Suggests changes
- Approves when ready

4. **Merge when approved**
```bash
git merge feature/user-profiles
```

### Spec Evolution

Track changes through git history:

```bash
# See spec history
git log -p specs/features/auth.md

# See who changed what
git blame specs/features/auth.md

# Compare versions
git diff v1.0..v2.0 specs/features/auth.md
```

## Review Best Practices

### What to Review

- **Completeness** - Are all cases covered?
- **Clarity** - Is it unambiguous?
- **Feasibility** - Can it be implemented?
- **Testability** - Can we verify it works?
- **Conflicts** - Does it contradict other specs?

### Review Checklist

```markdown
## Spec Review Checklist
- [ ] Requirements are clear and testable
- [ ] Edge cases are documented
- [ ] Security implications considered
- [ ] Performance requirements stated
- [ ] Dependencies identified
- [ ] Breaking changes noted
```

### Using PR Comments

```markdown
# In GitHub PR:

Line 15: "Users can log in"
Comment: "Should specify: email, username, or both?"

Line 23: "Fast response time"
Comment: "Please define 'fast' - suggest < 200ms p95"
```

## Advanced Patterns

### Spec Ownership

Use frontmatter to track ownership:

```yaml
---
id: payment-processing
owner: @alice
reviewers: [@bob, @carol]
approvers: [@tech-lead]
status: approved
approved_date: 2024-12-20
---
```

### Cross-References

Link related specifications:

```markdown
## Related Specs
- See [Authentication](../auth.md) for user context
- See [Database Schema](../db/schema.md) for storage
- Implements [RFC-001](../rfcs/001-api-design.md)
```

### Versioning Strategies

#### Approach 1: Version in Frontmatter
```yaml
---
version: 2.1.0
changes:
  2.1.0: Added webhook support
  2.0.0: Breaking change to auth
  1.0.0: Initial version
---
```

#### Approach 2: Git Tags
```bash
git tag spec-auth-v1.0.0
git tag spec-auth-v2.0.0
```

#### Approach 3: Separate Files
```
specs/
├── auth-v1.md (deprecated)
├── auth-v2.md (current)
└── auth-v3.md (draft)
```

## Team Tools

### CI/CD Integration

`.github/workflows/spec-lint.yml`:
```yaml
name: Spec Validation
on:
  pull_request:
    paths:
      - 'specs/**/*.md'

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
      - run: pip install msl-tools
      - run: msl-lint specs/
```

### Automation Scripts

`scripts/new-spec.sh`:
```bash
#!/bin/bash
TEMPLATE=$1
NAME=$2
cp specs/templates/${TEMPLATE}.md specs/features/${NAME}.md
sed -i "s/\${id}/${NAME}/g" specs/features/${NAME}.md
sed -i "s/\${owner}/${USER}/g" specs/features/${NAME}.md
echo "Created specs/features/${NAME}.md"
```

### Documentation Generation

Generate docs from specs:

```python
# scripts/generate-docs.py
import os
from pathlib import Path

specs = Path('specs').glob('**/*.md')
with open('docs/requirements.md', 'w') as out:
    for spec in specs:
        content = spec.read_text()
        # Extract and format requirements...
        out.write(formatted_content)
```

## Communication

### Slack Integration

Notify on spec changes:

```yaml
# .github/workflows/notify.yml
- name: Notify Slack
  if: contains(github.event.head_commit.message, 'spec')
  uses: slack-notify@v1
  with:
    message: "Spec updated: ${{ github.event.head_commit.message }}"
```

### Status Meetings

Use specs as meeting agenda:

```markdown
## Sprint Planning - 2024-12-21

### Specs for Review
- [ ] payment-processing.md - @alice
- [ ] user-profiles.md - @bob

### Specs in Progress
- authentication-v2.md - @carol (blocked)
- api-redesign.md - @dave (in review)
```

## Conflict Resolution

### Merge Conflicts

Git typically handles MSL merges well:

```bash
# Both edited requirements
<<<<<<< HEAD
- REQ-001: User login with email
=======
- REQ-001: User login with username
>>>>>>> feature

# Resolution:
- REQ-001: User login with email or username
```

### Specification Conflicts

When specs contradict:

1. **Document both perspectives**
```markdown
## Conflict: Authentication Method

### Option A: JWT Tokens
- Pros: Stateless, scalable
- Cons: Can't revoke easily

### Option B: Session Cookies
- Pros: Easy revocation
- Cons: Requires session store

### Decision: [Pending]
```

2. **Schedule resolution meeting**
3. **Document decision in spec**
4. **Update conflicting specs**

## Migration from Other Systems

### From Confluence/Wiki

1. Export pages as Markdown
2. Add MSL structure:
   - Add `## Requirements` sections
   - Convert lists to requirements
   - Add frontmatter metadata

### From JIRA

```python
# scripts/jira-to-msl.py
import jira

for issue in jira.search("type = Story"):
    with open(f"specs/{issue.key}.md", "w") as f:
        f.write(f"# {issue.summary}\n\n")
        f.write(f"## Requirements\n")
        for criterion in issue.acceptance_criteria:
            f.write(f"- {criterion}\n")
```

### From Word/PDF

1. Convert to Markdown (pandoc)
2. Clean up formatting
3. Structure as MSL
4. Review and refine

## Scaling Considerations

### Large Teams (50+)

- Use namespaced IDs: `TEAM-COMPONENT-REQ-001`
- Implement spec registry/index
- Automate cross-reference checking
- Regular spec sync meetings

### Multiple Repositories

```yaml
# specs/external-refs.yml
external_specs:
  - repo: backend-api
    path: specs/api.md
    version: v2.1.0
  - repo: frontend-app
    path: specs/ui.md
    version: v3.0.0
```

### Compliance Requirements

For regulated industries:

```yaml
---
id: payment-processing
compliance: [PCI-DSS, GDPR]
audit_trail:
  - date: 2024-12-01
    reviewer: Security Team
    status: approved
  - date: 2024-12-15
    reviewer: Legal Team
    status: approved
---
```

## Success Metrics

Track specification effectiveness:

- **Coverage**: % of features with specs
- **Currency**: % of specs updated in last quarter
- **Clarity**: # of clarification requests
- **Compliance**: % of implementations matching specs
- **Velocity**: Time from spec to implementation

## Common Pitfalls

### Avoid These

1. **Over-structuring too early** - Start simple
2. **Spec-only PRs** - Include specs with code changes
3. **Outdated specs** - Update specs as you code
4. **Tool obsession** - Markdown first, tools second
5. **Approval paralysis** - Draft specs are useful too

### Embrace These

1. **Living documents** - Specs evolve
2. **Pragmatic detail** - Enough, not everything
3. **Clear ownership** - Someone owns each spec
4. **Regular reviews** - Keep specs current
5. **Team conventions** - Consistency helps

## Getting Help

- Team lead for process questions
- `#specs` Slack channel for discussions
- [MSL Documentation](https://github.com/chrs-myrs/msl-specification)
- Team retrospectives for process improvement

Remember: The goal is clear communication, not perfect documentation.