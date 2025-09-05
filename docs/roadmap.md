# MSL Roadmap

**Building the foundation for AI-powered software development**

## Vision (2024-2026)

MSL will become the industry standard for human-AI collaboration in software development, enabling developers to work at the speed of thought while maintaining quality and control.

### Strategic Goals
1. **Universal AI Compatibility** - Every major AI assistant understands MSL natively
2. **Zero Friction Adoption** - Start with markdown, scale to enterprise
3. **Ecosystem Growth** - Rich tooling, integrations, and community
4. **Quality Assurance** - Catch AI hallucinations before production

## Release Schedule

### Version 1.2.1 - Released (Metaspec Governance)
**Released:** January 2025  
**Theme:** Specification Governance Foundation

#### Delivered Features
- **Metaspec Governance Proposal** - New `governed-by` frontmatter field for explicit specification compliance
- **CONFORMS-TO Relationship** - Distinct from inheritance (IS-A) and templates (DEFINES)
- **Validation Foundation** - Enables automated compliance checking against metaspec requirements
- **Composition Support** - Multiple metaspecs can govern a single specification

See [docs/proposals/metaspec-governance.md](proposals/metaspec-governance.md) for details.

### Version 1.3.0 - Q1 2025 (Foundation Complete)
**Target Date:** February 2025  
**Theme:** Core Tools & Validation

#### Committed Features
| Feature | Priority | Effort | Status | Description |
|---------|----------|--------|--------|-------------|
| Python Package | High | 2w | In Progress | PyPI distribution of tools |
| Comprehensive Test Suite | High | 2w | In Progress | Full test coverage |
| JSON Schema Validation | High | 1w | In Progress | Schema-based validation |
| Pre-commit Hooks | High | Done | ✅ | MSL linting on commit |

### Version 1.4.0 - Q1 2025 (Quick Wins)
**Target Date:** March 2025  
**Theme:** Enhanced Expressiveness

#### Committed Features
| Feature | Priority | Effort | Description |
|---------|----------|--------|-------------|
| **Hierarchical Requirements** | Critical | 2w | Nested requirements with parent-child relationships |
| **Composite Markers** | High | 1w | Rich metadata with `[priority\|status\|@owner]` syntax |
| **Validation Rules Config** | High | 2w | Project-specific `.mslrc` validation configuration |

#### Technical Details
- **Hierarchical**: `REQ-001.1`, `REQ-001.2` for sub-requirements
- **Composite**: Multiple markers in single brackets separated by pipes
- **Validation**: Custom rules, severity levels, project standards

### Version 1.5.0 - Q2 2025 (LiveSync Core)
**Target Date:** May 2025  
**Theme:** Bidirectional Code Synchronization

#### Committed Features
| Feature | Priority | Effort | Description |
|---------|----------|--------|-------------|
| **Bidirectional Code Links** | Critical | 4w | `[↔ src/auth.js:45-67]` live sync |
| **Lifecycle Stage Markers** | High | 2w | `[stage:design]`, `[stage:testing]` tracking |
| **Gap Detection** | High | 3w | `[gap:test]`, `[gap:doc]` automatic detection |

#### LiveSync Architecture
- **Forward Sync**: Spec → Code generation and updates
- **Backward Sync**: Code → Spec extraction and updates
- **Conflict Resolution**: Automated and manual merge strategies
- **Real-time Monitoring**: Continuous consistency checking

### Version 1.6.0 - Q3 2025 (Enterprise Ready)
**Target Date:** August 2025  
**Theme:** Team Collaboration & Advanced Features

#### Committed Features
| Feature | Priority | Effort | Description |
|---------|----------|--------|-------------|
| **Dependency Markers** | High | 2w | `[depends:REQ-001]`, `[blocks:REQ-002]` |
| **Review Workflow** | High | 3w | `[review:pending]`, approval tracking |
| **Typed Template Variables** | Medium | 3w | Schema-validated template parameters |
| **Inline Metadata** | Medium | 1w | Rich nested metadata under requirements |

#### Enterprise Features
- **Dependency Graph**: Critical path analysis, bottleneck detection
- **Review States**: pending, approved, changes-requested, blocked
- **Template Types**: string, number, boolean, array, object with validation
- **Metadata Schema**: Estimate, risk, complexity, stakeholders

## Long-Term Vision (Q4 2025 and Beyond)

### Q4 2025 Goals
- **IDE Integration** - VS Code extension with LiveSync
- **AI Training** - MSL-aware AI models
- **Visual Editor** - Web-based specification builder
- **Tool Ecosystem** - Rich CLI, API, and library support

### 2026 Goals  
- **Industry Standard** - MSL as the de facto spec language
- **Full LiveSync Platform** - Complete bidirectional development
- **AI Co-Development** - Specifications guide AI implementation
- **Enterprise Scale** - Support for 10,000+ spec projects
- **Global Adoption** - 100,000+ active developers

## Current Development (Q1 2025)

### In Progress
- [ ] Python package for PyPI (80% complete)
- [ ] Comprehensive test suite (70% complete) 
- [ ] JSON Schema validation (60% complete)
- [x] Pre-commit hooks (complete)

### Recently Completed
- [x] MSL v1.2.1 with metaspec governance
- [x] Documentation restructure
- [x] Claude Code agents
- [x] Core validation tools

## Community Priorities

Based on community feedback, these features are highly requested:

1. **GraphQL Specification Support** (127 votes)
2. **Database Migration Generation** (98 votes)
3. **OpenAPI/Swagger Export** (87 votes)
4. **Terraform Infrastructure Specs** (76 votes)
5. **Docker Compose Generation** (65 votes)

## Research & Development

### Active Research Areas
- **Specification Mining** - Extract specs from existing code
- **Formal Verification** - Prove implementation matches specification
- **Natural Language Processing** - Better requirement understanding
- **AI Behavior Prediction** - Predict AI implementation from specs

### Experimental Features (Alpha)
- Specification diffing and merging
- Voice-to-specification transcription
- Specification animation/visualization
- Cross-specification dependency analysis
- Metaspec governance (Proposed in v1.2.1, implementation planned)

## Contributing to the Roadmap

### How to Influence Priorities
1. **Vote on Issues** - 👍 issues you want prioritized
2. **Submit RFCs** - Propose major features via RFC process
3. **Join Working Groups** - Participate in feature development
4. **Sponsor Development** - Fund specific features

### Working Groups
- **AI Integration WG** - Meets Tuesdays 2pm UTC
- **Enterprise Features WG** - Meets Wednesdays 3pm UTC
- **Tools & Ecosystem WG** - Meets Thursdays 4pm UTC
- **Documentation WG** - Meets Fridays 1pm UTC

## Metrics & Success Criteria

### Adoption Metrics (Current → Target)
- GitHub Stars: 5.2k → 20k
- NPM Weekly Downloads: 45k → 200k
- Active Contributors: 127 → 500
- Enterprise Customers: 23 → 100

### Quality Metrics (Current → Target)
- Average Spec Quality Score: 82 → 90
- AI Implementation Success Rate: 78% → 95%
- Time to First Spec: 12 min → 5 min
- Documentation Coverage: 85% → 100%

## Deprecation Schedule

### To Be Deprecated
| Feature | Deprecated In | Removed In | Migration Path |
|---------|--------------|------------|----------------|
| `inherits` keyword | 1.2.0 | 2.0.0 | Use `extends` |
| XML export | 1.2.0 | 2.0.0 | Use JSON export |
| Node.js 12 support | 1.3.0 | 2.0.0 | Upgrade to Node 16+ |
| Legacy validation API | 1.4.0 | 2.1.0 | Use v2 API |

## Release Process

### Release Cycle
- **Major Versions** (X.0.0): Annually in Q4
- **Minor Versions** (1.X.0): Quarterly
- **Patch Versions** (1.2.X): As needed for bugs/security

### Release Criteria
- All committed features complete
- Quality score ≥95 for all specifications
- Documentation 100% updated
- Migration guide provided
- Community preview period (2 weeks)

## Get Involved

### Priority Discussions
- [2.0.0 Planning](https://github.com/chrs-myrs/msl-specification/discussions/200)
- [AI Integration RFC](https://github.com/chrs-myrs/msl-specification/discussions/195)
- [Enterprise Features](https://github.com/chrs-myrs/msl-specification/discussions/188)

### Sponsorship
Support MSL development:
- GitHub Sponsors: [Sponsor MSL](https://github.com/sponsors/msl)
- Open Collective: [MSL Collective](https://opencollective.com/msl)
- Enterprise Support: enterprise@msl-lang.org

---

**Updated:** 2025-01-04  
**Next Review:** 2025-02-01  
**Maintainer:** MSL Core Team

*This roadmap is subject to change based on community feedback and technical discoveries.*