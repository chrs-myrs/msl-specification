# MSL Implementation Reference

This document provides everything needed to implement MSL validation and processing tools. It consolidates the complete grammar, parser implementation, validation logic, and quality metrics in a single, self-contained reference.

## Table of Contents

1. [Grammar Specification](#grammar-specification)
2. [Parser Implementation](#parser-implementation)
3. [Validator Implementation](#validator-implementation)
4. [Quality Metrics](#quality-metrics)
5. [Template Processing](#template-processing)
6. [Inheritance Resolution](#inheritance-resolution)
7. [Complete Examples](#complete-examples)
8. [Testing Utilities](#testing-utilities)

## Grammar Specification

### BNF Grammar

The complete formal grammar for MSL using BNF notation:

```bnf
<msl-document>    ::= <frontmatter>? <content>
<frontmatter>     ::= "---" <newline> <yaml-content> "---" <newline>
<yaml-content>    ::= <yaml-1.2-compliant-content>
<content>         ::= <title> <sections>*
<title>           ::= "#" <space> <text> <newline>
<sections>        ::= <requirements> | <summary> | <notes> | <custom-section>
<requirements>    ::= "##" <space> "Requirements" <newline> <req-list>
<req-list>        ::= <requirement>+
<requirement>     ::= "-" <space> <req-content> <newline>
<req-content>     ::= <markers>? <req-id>? <inheritance>? <text>
<markers>         ::= ("[" <marker-char> "]" <space>)*
<marker-char>     ::= "!" | "?" | "x" | " " | "@" <username> | "#" <tag>
<username>        ::= <letter> (<letter> | <digit> | "-")*
<tag>             ::= <letter> (<letter> | <digit> | "-")*
<req-id>          ::= "REQ-" <digits> ":" <space>
<inheritance>     ::= ("[" <inherit-type> "]" <space>) | (<inherit-word> ":" <space>)
<inherit-type>    ::= "OVERRIDE" | "NEW" | "INHERIT"
<inherit-word>    ::= "Modified" | "New"
<variable-ref>    ::= "${" <variable-name> "}"
<variable-name>   ::= <letter> (<letter> | <digit> | "_")*
<text>            ::= <any-markdown-content>
```

### EBNF Extensions for Complex Rules

```ebnf
(* Composite markers - v1.4.0+ *)
composite-marker  = "[" marker-component { "|" marker-component } "]" ;
marker-component  = simple-marker | key-value-pair ;
key-value-pair    = identifier ":" value ;
simple-marker     = "!" | "?" | "x" | " " | "@" identifier | "#" identifier ;

(* Nested requirements *)
nested-requirement = indent requirement ;
indent            = "  " | "\t" ;

(* Multi-line requirements *)
multi-line-req    = "-" " " req-content newline
                    { indent continuation-line newline } ;
continuation-line = text-without-dash ;
```

### Examples of Valid and Invalid Syntax

**Valid Level 0 (Pure Markdown):**
```markdown
# My Specification
## Requirements
- Users must authenticate
- Sessions expire after 30 minutes
```

**Valid Level 1 (With Frontmatter and IDs):**
```markdown
---
id: auth-spec
---
# Authentication
## Requirements
- REQ-001: Users must authenticate
- REQ-002: Sessions expire after 30 minutes
```

**Valid Level 2 (Full Features):**
```markdown
---
id: payment-api
extends: api-base
---
# Payment API
## Requirements
- [!] [@alice] REQ-001: [OVERRIDE] Process payments within 2 seconds
- [x] [#mvp] REQ-002: [NEW] Support card payments
- [progress:60%|coverage:85%] REQ-003: Implement refunds
```

**Invalid Syntax:**
```markdown
## Requirements
REQ-001 Users must authenticate        # Missing dash
- REQ001: Wrong format                  # Wrong ID format (needs REQ-)
- [INVALID] Unknown marker              # Unknown inheritance marker
- ${undefined_var} Template variable    # Undefined variable
```

## Parser Implementation

Complete Python parser implementation in under 200 lines:

```python
#!/usr/bin/env python3
"""MSL Parser - Complete implementation for parsing MSL documents."""

import re
import yaml
from typing import Dict, List, Optional, Any
from pathlib import Path

class MSLParser:
    """Parse MSL markdown files into structured data."""
    
    def __init__(self):
        # Core patterns
        self.req_pattern = re.compile(r'^-\s*(REQ-\d+:)?\s*(.+)$', re.MULTILINE)
        self.marker_pattern = re.compile(r'^\[([\!\?\@\#]|x|\s)\]\s*(.+)$')
        self.composite_pattern = re.compile(r'^\[([^\]]+)\]\s*(.+)$')
        
    def parse(self, content: str) -> Dict[str, Any]:
        """Parse MSL content and return structured document."""
        result = {
            "level": 0,
            "metadata": {},
            "title": None,
            "summary": None,
            "requirements": [],
            "notes": None
        }
        
        # Extract frontmatter
        frontmatter, body = self._extract_frontmatter(content)
        if frontmatter:
            result["metadata"] = frontmatter
            result["level"] = 1 if "id" in frontmatter else result["level"]
            if any(k in frontmatter for k in ["extends", "governed-by", "type"]):
                result["level"] = 2
        
        # Parse sections
        sections = self._parse_sections(body)
        
        # Extract title
        if title_match := re.search(r'^#\s+(.+)$', body, re.MULTILINE):
            result["title"] = title_match.group(1).strip()
            
        # Extract and parse requirements
        if "requirements" in sections:
            result["requirements"] = self._parse_requirements(sections["requirements"])
            # Detect Level 2 features
            for req in result["requirements"]:
                if req.get("markers") or req.get("inheritance") != "inherit":
                    result["level"] = 2
                    break
                    
        # Extract other sections
        result["summary"] = sections.get("summary")
        result["notes"] = sections.get("notes")
        
        return result
    
    def _extract_frontmatter(self, content: str) -> tuple[Optional[Dict], str]:
        """Extract YAML frontmatter."""
        if not content.startswith('---'):
            return None, content
            
        try:
            parts = content.split('---', 2)
            if len(parts) >= 3:
                metadata = yaml.safe_load(parts[1])
                return metadata or {}, parts[2]
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML frontmatter: {e}")
            
        return None, content
    
    def _parse_sections(self, content: str) -> Dict[str, str]:
        """Parse markdown sections by ## headings."""
        sections = {}
        pattern = re.compile(r'^##\s+(\w+)\s*$', re.MULTILINE)
        matches = list(pattern.finditer(content))
        
        for i, match in enumerate(matches):
            name = match.group(1).lower()
            start = match.end()
            end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
            sections[name] = content[start:end].strip()
            
        return sections
    
    def _parse_requirements(self, content: str) -> List[Dict[str, Any]]:
        """Parse requirements with all features."""
        requirements = []
        
        for line in content.split('\n'):
            if not line.strip().startswith('-'):
                continue
                
            req = self._parse_requirement_line(line)
            if req:
                requirements.append(req)
                
        return requirements
    
    def _parse_requirement_line(self, line: str) -> Dict[str, Any]:
        """Parse single requirement line with markers and IDs."""
        # Remove leading dash
        line = line[1:].strip()
        
        requirement = {
            "text": line,
            "id": None,
            "markers": {},
            "inheritance": "inherit"
        }
        
        # Extract markers
        if line.startswith('['):
            match = self.composite_pattern.match(line)
            if match:
                markers = match.group(1)
                line = match.group(2)
                requirement["text"] = line
                
                # Parse markers (composite or simple)
                if '|' in markers or ':' in markers:
                    for component in markers.split('|'):
                        if ':' in component:
                            key, value = component.split(':', 1)
                            requirement["markers"][key.strip()] = value.strip()
                        else:
                            self._parse_simple_marker(component.strip(), requirement)
                else:
                    self._parse_simple_marker(markers, requirement)
        
        # Extract REQ-ID
        if id_match := re.match(r'^(REQ-\d+):\s*(.+)$', line):
            requirement["id"] = id_match.group(1)
            line = id_match.group(2)
            requirement["text"] = line
            
        # Extract inheritance markers
        for marker, value in [("OVERRIDE", "override"), ("NEW", "new"), 
                              ("INHERIT", "inherit")]:
            if f"[{marker}]" in line:
                requirement["inheritance"] = value
                line = line.replace(f"[{marker}]", "").strip()
                requirement["text"] = line
                break
                
        return requirement
    
    def _parse_simple_marker(self, marker: str, requirement: Dict):
        """Parse simple markers into requirement properties."""
        if marker == "!":
            requirement["markers"]["priority"] = "critical"
        elif marker == "?":
            requirement["markers"]["status"] = "uncertain"
        elif marker == "x":
            requirement["markers"]["status"] = "complete"
        elif marker == " ":
            requirement["markers"]["status"] = "pending"
        elif marker.startswith("@"):
            requirement["markers"]["assignee"] = marker[1:]
        elif marker.startswith("#"):
            requirement["markers"]["tag"] = marker[1:]

# Example usage
if __name__ == "__main__":
    parser = MSLParser()
    
    example = '''---
id: example-spec
extends: base-spec
---
# Example Specification

## Requirements
- [!] [@alice] REQ-001: [NEW] Critical requirement
- [x] REQ-002: [INHERIT] Completed requirement
- [progress:60%|coverage:85%] REQ-003: Composite markers
- Simple requirement without ID or markers
'''
    
    result = parser.parse(example)
    print(f"Level: {result['level']}")
    print(f"ID: {result['metadata'].get('id')}")
    print(f"Requirements: {len(result['requirements'])}")
    for req in result["requirements"]:
        print(f"  - {req.get('id', 'NO-ID')}: {req['text'][:50]}...")
```

## Validator Implementation

Complete validation logic implementation:

```python
#!/usr/bin/env python3
"""MSL Validator - Complete validation implementation."""

from typing import List, Dict, Any, Set
from pathlib import Path

class ValidationIssue:
    """Represents a validation issue."""
    
    def __init__(self, severity: str, message: str, line: int = None):
        self.severity = severity  # "error", "warning", "info"
        self.message = message
        self.line = line
        
    def __str__(self):
        location = f":{self.line}" if self.line else ""
        return f"[{self.severity.upper()}]{location} {self.message}"

class MSLValidator:
    """Validate MSL documents against specification."""
    
    def validate_msl(self, file_path: str) -> List[ValidationIssue]:
        """Validate an MSL file and return issues list."""
        content = Path(file_path).read_text()
        issues = []
        
        # Parse document first
        from msl_parser import MSLParser
        parser = MSLParser()
        try:
            doc = parser.parse(content)
        except Exception as e:
            issues.append(ValidationIssue("error", f"Parse error: {e}"))
            return issues
        
        # Level-specific validation
        issues.extend(self._validate_structure(doc, content))
        issues.extend(self._validate_requirements(doc))
        issues.extend(self._validate_metadata(doc))
        issues.extend(self._validate_markers(doc))
        issues.extend(self._validate_inheritance(doc))
        
        return issues
    
    def _validate_structure(self, doc: Dict, content: str) -> List[ValidationIssue]:
        """Validate document structure."""
        issues = []
        
        # Check for Requirements section
        if '## Requirements' not in content:
            issues.append(ValidationIssue(
                "error", 
                "Missing ## Requirements section"
            ))
        
        # Check for title
        if not doc.get("title"):
            issues.append(ValidationIssue(
                "warning",
                "Missing document title (# Title)"
            ))
            
        # Level 1+ requires ID
        if doc["level"] >= 1 and not doc["metadata"].get("id"):
            issues.append(ValidationIssue(
                "error",
                "Level 1+ requires 'id' in frontmatter"
            ))
            
        return issues
    
    def _validate_requirements(self, doc: Dict) -> List[ValidationIssue]:
        """Validate requirements list."""
        issues = []
        requirements = doc.get("requirements", [])
        
        # Check for duplicate REQ-IDs
        req_ids = [r["id"] for r in requirements if r.get("id")]
        duplicates = set([x for x in req_ids if req_ids.count(x) > 1])
        
        for dup_id in duplicates:
            issues.append(ValidationIssue(
                "error",
                f"Duplicate REQ-ID: {dup_id}"
            ))
        
        # Check REQ-ID format
        import re
        req_pattern = re.compile(r'^REQ-\d{3}$')
        for req in requirements:
            if req.get("id") and not req_pattern.match(req["id"]):
                issues.append(ValidationIssue(
                    "warning",
                    f"Invalid REQ-ID format: {req['id']} (expected REQ-XXX)"
                ))
        
        # Check for empty requirements
        for i, req in enumerate(requirements, 1):
            if not req.get("text", "").strip():
                issues.append(ValidationIssue(
                    "warning",
                    f"Empty requirement at position {i}"
                ))
                
        return issues
    
    def _validate_metadata(self, doc: Dict) -> List[ValidationIssue]:
        """Validate frontmatter metadata."""
        issues = []
        metadata = doc.get("metadata", {})
        
        # Validate priority values
        if "priority" in metadata:
            valid = ["critical", "high", "medium", "low"]
            if metadata["priority"] not in valid:
                issues.append(ValidationIssue(
                    "warning",
                    f"Invalid priority: {metadata['priority']}"
                ))
        
        # Validate status values
        if "status" in metadata:
            valid = ["draft", "active", "complete", "deprecated", "pending"]
            if metadata["status"] not in valid:
                issues.append(ValidationIssue(
                    "warning", 
                    f"Invalid status: {metadata['status']}"
                ))
                
        # Check extends reference exists
        if "extends" in metadata:
            parent_path = Path(metadata["extends"])
            if not parent_path.exists():
                issues.append(ValidationIssue(
                    "error",
                    f"Parent spec not found: {metadata['extends']}"
                ))
                
        return issues
    
    def _validate_markers(self, doc: Dict) -> List[ValidationIssue]:
        """Validate marker conflicts."""
        issues = []
        
        for req in doc.get("requirements", []):
            markers = req.get("markers", {})
            
            # Check for conflicting markers
            if markers.get("priority") == "critical" and \
               markers.get("status") == "uncertain":
                issues.append(ValidationIssue(
                    "warning",
                    f"Conflicting markers [!] and [?] in {req.get('id', 'requirement')}"
                ))
                
            # Validate composite markers
            for key, value in markers.items():
                if key in ["progress", "coverage"]:
                    try:
                        pct = int(value.rstrip('%'))
                        if not 0 <= pct <= 100:
                            raise ValueError()
                    except:
                        issues.append(ValidationIssue(
                            "error",
                            f"Invalid percentage value: {key}:{value}"
                        ))
                        
        return issues
    
    def _validate_inheritance(self, doc: Dict) -> List[ValidationIssue]:
        """Validate inheritance markers."""
        issues = []
        
        # Inheritance markers only valid with extends
        if not doc["metadata"].get("extends"):
            for req in doc.get("requirements", []):
                if req.get("inheritance") != "inherit":
                    issues.append(ValidationIssue(
                        "error",
                        f"Inheritance marker {req['inheritance'].upper()} requires 'extends' in frontmatter"
                    ))
                    
        return issues

# Example usage
if __name__ == "__main__":
    validator = MSLValidator()
    issues = validator.validate_msl("example.md")
    for issue in issues:
        print(issue)
```

## Quality Metrics

Algorithms for calculating quality scores:

```python
#!/usr/bin/env python3
"""MSL Quality Metrics - Calculate quality scores for specifications."""

from typing import Dict, List, Set
import re
from pathlib import Path

class QualityAnalyzer:
    """Analyze MSL specifications for quality metrics."""
    
    def calculate_quality_score(self, spec_set: List[Dict]) -> Dict[str, float]:
        """Calculate overall quality score (0-100)."""
        scores = {
            "dry_compliance": self._calculate_dry_score(spec_set),
            "testability": self._calculate_testability_score(spec_set),
            "cohesion": self._calculate_cohesion_score(spec_set),
            "coupling": self._calculate_coupling_score(spec_set),
            "inheritance_depth": self._calculate_inheritance_score(spec_set)
        }
        
        # Weighted average
        weights = {
            "dry_compliance": 0.25,
            "testability": 0.30,
            "cohesion": 0.20,
            "coupling": 0.15,
            "inheritance_depth": 0.10
        }
        
        overall = sum(scores[k] * weights[k] for k in scores)
        scores["overall"] = overall
        
        return scores
    
    def _calculate_dry_score(self, spec_set: List[Dict]) -> float:
        """Calculate DRY compliance (<20% duplication = 100 score)."""
        all_requirements = []
        for spec in spec_set:
            for req in spec.get("requirements", []):
                all_requirements.append(req["text"])
        
        if not all_requirements:
            return 100.0
            
        # Find duplicates using similarity threshold
        duplicates = 0
        for i, req1 in enumerate(all_requirements):
            for req2 in all_requirements[i+1:]:
                similarity = self._text_similarity(req1, req2)
                if similarity > 0.8:  # 80% similarity threshold
                    duplicates += 1
        
        duplication_rate = duplicates / len(all_requirements)
        
        # Score calculation: 0% duplication = 100, 20% = 80, 40% = 60, etc.
        score = max(0, 100 - (duplication_rate * 100))
        return score
    
    def _calculate_testability_score(self, spec_set: List[Dict]) -> float:
        """Calculate testability (≥90% measurable = 100 score)."""
        total_reqs = 0
        testable_reqs = 0
        
        # Patterns indicating measurable requirements
        measurable_patterns = [
            r'\d+',  # Contains numbers
            r'must|shall|should',  # Modal verbs
            r'within|before|after|less than|greater than',  # Comparisons
            r'seconds|minutes|hours|days',  # Time units
            r'percent|%',  # Percentages
        ]
        
        for spec in spec_set:
            for req in spec.get("requirements", []):
                total_reqs += 1
                text = req["text"].lower()
                
                # Check if requirement is measurable
                if any(re.search(pattern, text) for pattern in measurable_patterns):
                    testable_reqs += 1
        
        if total_reqs == 0:
            return 100.0
            
        testability_rate = testable_reqs / total_reqs
        
        # Score: 90% testable = 100, 80% = 90, 70% = 80, etc.
        score = min(100, testability_rate * 111.11)
        return score
    
    def _calculate_cohesion_score(self, spec_set: List[Dict]) -> float:
        """Calculate cohesion (high relatedness within specs)."""
        cohesion_scores = []
        
        for spec in spec_set:
            requirements = spec.get("requirements", [])
            if len(requirements) < 2:
                cohesion_scores.append(100.0)
                continue
                
            # Calculate average similarity between requirements in same spec
            similarities = []
            for i, req1 in enumerate(requirements):
                for req2 in requirements[i+1:]:
                    sim = self._semantic_similarity(req1["text"], req2["text"])
                    similarities.append(sim)
            
            if similarities:
                avg_similarity = sum(similarities) / len(similarities)
                # Convert to score: higher similarity = higher cohesion
                cohesion_scores.append(avg_similarity * 100)
            else:
                cohesion_scores.append(100.0)
        
        return sum(cohesion_scores) / len(cohesion_scores) if cohesion_scores else 100.0
    
    def _calculate_coupling_score(self, spec_set: List[Dict]) -> float:
        """Calculate coupling (low external dependencies)."""
        coupling_scores = []
        
        for spec in spec_set:
            external_refs = 0
            total_elements = len(spec.get("requirements", []))
            
            # Count external references
            if spec["metadata"].get("extends"):
                external_refs += 1
            if spec["metadata"].get("governed-by"):
                external_refs += len(spec["metadata"]["governed-by"])
            if spec["metadata"].get("references"):
                external_refs += len(spec["metadata"]["references"])
                
            # Calculate coupling ratio
            if total_elements > 0:
                coupling_ratio = external_refs / total_elements
                # Convert to score: lower coupling = higher score
                score = max(0, 100 - (coupling_ratio * 50))
                coupling_scores.append(score)
            else:
                coupling_scores.append(100.0)
        
        return sum(coupling_scores) / len(coupling_scores) if coupling_scores else 100.0
    
    def _calculate_inheritance_score(self, spec_set: List[Dict]) -> float:
        """Calculate inheritance depth score (≤4 levels = 100)."""
        max_depth = 0
        
        for spec in spec_set:
            depth = self._get_inheritance_depth(spec, spec_set)
            max_depth = max(max_depth, depth)
        
        # Score: 0-4 levels = 100, 5 = 80, 6 = 60, etc.
        if max_depth <= 4:
            return 100.0
        else:
            return max(0, 100 - ((max_depth - 4) * 20))
    
    def _get_inheritance_depth(self, spec: Dict, spec_set: List[Dict]) -> int:
        """Get inheritance chain depth for a specification."""
        depth = 0
        current = spec
        visited = set()
        
        while current["metadata"].get("extends"):
            if current["metadata"]["id"] in visited:
                break  # Circular reference
            visited.add(current["metadata"]["id"])
            
            parent_id = current["metadata"]["extends"]
            parent = next((s for s in spec_set if s["metadata"].get("id") == parent_id), None)
            
            if not parent:
                break
                
            current = parent
            depth += 1
            
        return depth
    
    def _text_similarity(self, text1: str, text2: str) -> float:
        """Calculate text similarity (0-1)."""
        # Simple word-based similarity
        words1 = set(text1.lower().split())
        words2 = set(text2.lower().split())
        
        if not words1 or not words2:
            return 0.0
            
        intersection = words1.intersection(words2)
        union = words1.union(words2)
        
        return len(intersection) / len(union)
    
    def _semantic_similarity(self, text1: str, text2: str) -> float:
        """Calculate semantic similarity between requirements."""
        # Simplified semantic similarity based on shared keywords
        keywords1 = set(re.findall(r'\b\w+\b', text1.lower()))
        keywords2 = set(re.findall(r'\b\w+\b', text2.lower()))
        
        # Remove stop words
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 
                     'to', 'for', 'of', 'with', 'by', 'from', 'as', 'is', 'was',
                     'are', 'were', 'be', 'been', 'being', 'have', 'has', 'had'}
        
        keywords1 -= stop_words
        keywords2 -= stop_words
        
        if not keywords1 or not keywords2:
            return 0.0
            
        shared = keywords1.intersection(keywords2)
        total = keywords1.union(keywords2)
        
        return len(shared) / len(total)

# Score interpretation
def interpret_score(scores: Dict[str, float]) -> str:
    """Interpret quality scores."""
    overall = scores["overall"]
    
    if overall >= 90:
        level = "Excellent"
        action = "Ready for production"
    elif overall >= 80:
        level = "Good"
        action = "Minor improvements recommended"
    elif overall >= 70:
        level = "Acceptable"
        action = "Refactoring recommended"
    else:
        level = "Poor"
        action = "Significant refactoring required"
    
    return f"""
Quality Assessment: {level} ({overall:.1f}/100)
Action: {action}

Breakdown:
- DRY Compliance: {scores['dry_compliance']:.1f}/100
- Testability: {scores['testability']:.1f}/100
- Cohesion: {scores['cohesion']:.1f}/100
- Coupling: {scores['coupling']:.1f}/100
- Inheritance Depth: {scores['inheritance_depth']:.1f}/100
"""
```

## Template Processing

Template variable substitution implementation:

```python
#!/usr/bin/env python3
"""MSL Template Processing - Handle template rendering and variable substitution."""

import re
from typing import Dict, Any, List
from pathlib import Path

class TemplateProcessor:
    """Process MSL templates with variable substitution."""
    
    def __init__(self):
        self.variable_pattern = re.compile(r'\$\{([^}]+)\}')
    
    def render_template(self, template: Dict, variables: Dict[str, str]) -> str:
        """Render template with variable substitution."""
        # Merge variables: child overrides parent
        all_vars = {}
        
        # Start with template defaults
        if template["metadata"].get("variables"):
            all_vars.update(template["metadata"]["variables"])
            
        # Override with provided variables
        all_vars.update(variables)
        
        # Get template content
        content = template.get("raw_content", "")
        
        # Validate all variables are defined
        undefined = self._find_undefined_variables(content, all_vars)
        if undefined:
            raise ValueError(f"Undefined variables: {', '.join(undefined)}")
        
        # Perform substitution
        result = self._substitute_variables(content, all_vars)
        
        return result
    
    def _find_undefined_variables(self, content: str, variables: Dict) -> List[str]:
        """Find undefined variable references."""
        undefined = []
        
        for match in self.variable_pattern.finditer(content):
            var_name = match.group(1)
            if var_name not in variables:
                undefined.append(var_name)
                
        return undefined
    
    def _substitute_variables(self, content: str, variables: Dict) -> str:
        """Replace ${variable} with values."""
        def replacer(match):
            var_name = match.group(1)
            return variables.get(var_name, match.group(0))
            
        return self.variable_pattern.sub(replacer, content)
    
    def resolve_nested_variables(self, variables: Dict) -> Dict:
        """Resolve nested variable references."""
        resolved = {}
        unresolved = variables.copy()
        max_iterations = 10
        
        for _ in range(max_iterations):
            if not unresolved:
                break
                
            progress = False
            for key, value in list(unresolved.items()):
                # Check if value contains variable references
                if not isinstance(value, str):
                    resolved[key] = value
                    del unresolved[key]
                    progress = True
                elif not self.variable_pattern.search(value):
                    resolved[key] = value
                    del unresolved[key]
                    progress = True
                else:
                    # Try to resolve
                    try:
                        resolved_value = self._substitute_variables(value, resolved)
                        if resolved_value != value:
                            resolved[key] = resolved_value
                            del unresolved[key]
                            progress = True
                    except:
                        pass
            
            if not progress:
                raise ValueError(f"Circular variable references: {list(unresolved.keys())}")
                
        return resolved

# Example usage
if __name__ == "__main__":
    processor = TemplateProcessor()
    
    template = {
        "metadata": {
            "id": "api-template",
            "type": "template",
            "variables": {
                "service_name": "Generic API",
                "rate_limit": "100",
                "timeout": "30"
            }
        },
        "raw_content": """---
id: ${service_name}-api
type: template
variables:
  service_name: ${service_name}
  rate_limit: ${rate_limit}
---

# ${service_name} Specification

## Requirements
- REQ-001: Service name must be "${service_name}"
- REQ-002: Rate limit of ${rate_limit} requests per minute
- REQ-003: Timeout after ${timeout} seconds
"""
    }
    
    # Render with custom variables
    custom_vars = {
        "service_name": "Payment",
        "rate_limit": "50"
        # timeout will use default value
    }
    
    result = processor.render_template(template, custom_vars)
    print(result)
```

## Inheritance Resolution

Complete inheritance resolution algorithm:

```python
#!/usr/bin/env python3
"""MSL Inheritance Resolution - Resolve inheritance chains and merge requirements."""

from typing import Dict, List, Any, Optional
from pathlib import Path

class InheritanceResolver:
    """Resolve MSL inheritance hierarchies."""
    
    def resolve_inheritance(self, child: Dict, parent: Dict) -> Dict:
        """Resolve inheritance between child and parent specs."""
        resolved = child.copy()
        
        # Merge requirements
        resolved["requirements"] = self._merge_requirements(
            parent.get("requirements", []),
            child.get("requirements", [])
        )
        
        # Merge metadata (child overrides)
        resolved["metadata"] = self._merge_metadata(
            parent.get("metadata", {}),
            child.get("metadata", {})
        )
        
        return resolved
    
    def _merge_requirements(self, parent_reqs: List[Dict], child_reqs: List[Dict]) -> List[Dict]:
        """Merge requirements with inheritance markers."""
        merged = []
        processed_ids = set()
        
        # Process child requirements
        for child_req in child_reqs:
            req_id = child_req.get("id")
            inheritance = child_req.get("inheritance", "inherit")
            
            if req_id:
                processed_ids.add(req_id)
                
                # Find parent requirement with same ID
                parent_req = next((r for r in parent_reqs if r.get("id") == req_id), None)
                
                if inheritance == "override":
                    if not parent_req:
                        raise ValueError(f"Cannot override non-existent requirement: {req_id}")
                    merged.append(child_req)
                    
                elif inheritance == "new":
                    if parent_req:
                        raise ValueError(f"Requirement already exists in parent: {req_id}")
                    merged.append(child_req)
                    
                elif inheritance == "inherit":
                    if parent_req:
                        # Merge with parent
                        merged_req = parent_req.copy()
                        merged_req.update(child_req)
                        merged.append(merged_req)
                    else:
                        merged.append(child_req)
            else:
                # No ID, treat as new requirement
                merged.append(child_req)
        
        # Add parent requirements not processed by child
        for parent_req in parent_reqs:
            if parent_req.get("id") and parent_req["id"] not in processed_ids:
                merged.append(parent_req)
                
        return merged
    
    def _merge_metadata(self, parent_meta: Dict, child_meta: Dict) -> Dict:
        """Merge metadata with child overriding parent."""
        merged = parent_meta.copy()
        
        # Child overrides all fields except special ones
        for key, value in child_meta.items():
            if key == "extends":
                # Don't inherit extends field
                continue
            elif key == "tags" and "tags" in merged:
                # Combine tags
                merged["tags"] = list(set(merged["tags"] + value))
            elif key == "governed-by" and "governed-by" in merged:
                # Combine governance
                merged["governed-by"] = list(set(merged["governed-by"] + value))
            else:
                # Child overrides
                merged[key] = value
                
        return merged
    
    def detect_circular_inheritance(self, specs: List[Dict]) -> List[str]:
        """Detect circular inheritance chains."""
        circular = []
        
        for spec in specs:
            visited = set()
            current = spec
            
            while current.get("metadata", {}).get("extends"):
                spec_id = current["metadata"].get("id", "unknown")
                
                if spec_id in visited:
                    circular.append(spec_id)
                    break
                    
                visited.add(spec_id)
                
                parent_id = current["metadata"]["extends"]
                current = next((s for s in specs if s["metadata"].get("id") == parent_id), None)
                
                if not current:
                    break
                    
        return circular
    
    def resolve_chain(self, spec_id: str, specs: List[Dict]) -> Dict:
        """Resolve complete inheritance chain for a specification."""
        # Find target spec
        target = next((s for s in specs if s["metadata"].get("id") == spec_id), None)
        if not target:
            raise ValueError(f"Specification not found: {spec_id}")
        
        # Build inheritance chain
        chain = []
        current = target
        visited = set()
        
        while current:
            if current["metadata"].get("id") in visited:
                raise ValueError(f"Circular inheritance detected")
                
            chain.insert(0, current)  # Add to beginning
            visited.add(current["metadata"].get("id"))
            
            if not current["metadata"].get("extends"):
                break
                
            parent_id = current["metadata"]["extends"]
            current = next((s for s in specs if s["metadata"].get("id") == parent_id), None)
        
        # Resolve from root to target
        resolved = chain[0]
        for spec in chain[1:]:
            resolved = self.resolve_inheritance(spec, resolved)
            
        return resolved

# Marker processing logic
def apply_inheritance_markers(requirements: List[Dict]) -> List[Dict]:
    """Apply inheritance markers to requirements."""
    processed = []
    
    for req in requirements:
        marker = req.get("inheritance", "inherit")
        
        if marker == "override":
            # Replace parent requirement completely
            processed.append(req)
        elif marker == "new":
            # Add as new requirement
            processed.append(req)
        elif marker == "inherit":
            # Keep parent requirement, potentially with modifications
            processed.append(req)
            
    return processed

# Example usage
if __name__ == "__main__":
    resolver = InheritanceResolver()
    
    parent = {
        "metadata": {"id": "api-base", "priority": "high"},
        "requirements": [
            {"id": "REQ-001", "text": "Use HTTPS"},
            {"id": "REQ-002", "text": "Return JSON"},
            {"id": "REQ-003", "text": "Rate limit 100/min"}
        ]
    }
    
    child = {
        "metadata": {"id": "payment-api", "extends": "api-base"},
        "requirements": [
            {"id": "REQ-001", "text": "Use HTTPS", "inheritance": "inherit"},
            {"id": "REQ-003", "text": "Rate limit 30/min", "inheritance": "override"},
            {"id": "REQ-004", "text": "PCI compliance", "inheritance": "new"}
        ]
    }
    
    resolved = resolver.resolve_inheritance(child, parent)
    print("Resolved requirements:")
    for req in resolved["requirements"]:
        print(f"  - {req['id']}: {req['text']}")
```

## Complete Examples

### Example 1: Basic MSL Validation

```python
#!/usr/bin/env python3
"""Complete example: Validate an MSL file."""

from pathlib import Path
from msl_parser import MSLParser
from msl_validator import MSLValidator

def validate_file(file_path: str):
    """Validate an MSL file and report issues."""
    print(f"Validating: {file_path}")
    print("-" * 50)
    
    # Parse the file
    parser = MSLParser()
    try:
        content = Path(file_path).read_text()
        doc = parser.parse(content)
        print(f"✓ Parsed successfully (Level {doc['level']})")
    except Exception as e:
        print(f"✗ Parse error: {e}")
        return
    
    # Validate the document
    validator = MSLValidator()
    issues = validator.validate_msl(file_path)
    
    if not issues:
        print("✓ No validation issues found")
    else:
        print(f"Found {len(issues)} issues:")
        for issue in issues:
            print(f"  {issue}")
    
    print()

# Sample MSL content
sample_msl = """---
id: sample-spec
priority: high
---

# Sample Specification

## Summary
This is a sample MSL specification for validation.

## Requirements
- REQ-001: System must authenticate users
- REQ-002: Sessions must expire after 30 minutes
- REQ-001: Duplicate ID (will cause error)
- Invalid requirement without dash
"""

# Write sample and validate
Path("sample.md").write_text(sample_msl)
validate_file("sample.md")
```

### Example 2: Inheritance Resolution

```python
#!/usr/bin/env python3
"""Complete example: Resolve inheritance chain."""

from msl_parser import MSLParser
from inheritance_resolver import InheritanceResolver

# Create specification hierarchy
base_spec = """---
id: service-base
---
# Base Service
## Requirements
- REQ-001: Use HTTPS for all communication
- REQ-002: Log all requests
- REQ-003: Handle errors gracefully
"""

api_spec = """---
id: api-service
extends: service-base
---
# API Service
## Requirements
- REQ-002: [OVERRIDE] Log all requests with correlation ID
- REQ-004: [NEW] Return JSON responses
"""

payment_spec = """---
id: payment-api
extends: api-service
---
# Payment API
## Requirements
- REQ-003: [OVERRIDE] Handle payment errors with retry
- REQ-005: [NEW] PCI DSS compliance required
"""

# Parse all specs
parser = MSLParser()
specs = [
    parser.parse(base_spec),
    parser.parse(api_spec),
    parser.parse(payment_spec)
]

# Resolve inheritance
resolver = InheritanceResolver()
resolved = resolver.resolve_chain("payment-api", specs)

print("Resolved Payment API Requirements:")
print("=" * 50)
for req in resolved["requirements"]:
    inheritance = req.get("inheritance", "inherit")
    marker = f"[{inheritance.upper()}]" if inheritance != "inherit" else ""
    print(f"{req.get('id', 'NO-ID')}: {marker} {req['text']}")
```

### Example 3: Template Rendering

```python
#!/usr/bin/env python3
"""Complete example: Render template with variables."""

from msl_parser import MSLParser
from template_processor import TemplateProcessor

# Define template
template_content = """---
id: microservice-template
type: template
variables:
  service_name: GenericService
  port: 8080
  max_connections: 100
---

# ${service_name} Configuration

## Requirements
- REQ-001: Service name: ${service_name}
- REQ-002: Listen on port ${port}
- REQ-003: Maximum ${max_connections} concurrent connections
- REQ-004: Health check endpoint at /health
"""

# Parse template
parser = MSLParser()
template = parser.parse(template_content)
template["raw_content"] = template_content

# Render with custom variables
processor = TemplateProcessor()
custom_vars = {
    "service_name": "PaymentService",
    "port": "8443",
    "max_connections": "500"
}

rendered = processor.render_template(template, custom_vars)
print("Rendered Template:")
print("=" * 50)
print(rendered)

# Parse rendered result
rendered_doc = parser.parse(rendered)
print("\nExtracted Requirements:")
for req in rendered_doc["requirements"]:
    print(f"  - {req.get('id', 'NO-ID')}: {req['text']}")
```

## Testing Utilities

Helper functions for testing MSL implementations:

```python
#!/usr/bin/env python3
"""MSL Testing Utilities - Helper functions for testing MSL tools."""

import json
from pathlib import Path
from typing import Dict, List, Any

class MSLTestHelper:
    """Test helper functions for MSL validation."""
    
    @staticmethod
    def assert_valid_msl(file_path: str):
        """Assert that a file is valid MSL."""
        from msl_validator import MSLValidator
        validator = MSLValidator()
        issues = validator.validate_msl(file_path)
        errors = [i for i in issues if i.severity == "error"]
        
        if errors:
            raise AssertionError(f"MSL validation failed: {errors}")
    
    @staticmethod
    def assert_quality_score(spec_set: List[Dict], min_score: float = 80.0):
        """Assert minimum quality score."""
        from quality_analyzer import QualityAnalyzer
        analyzer = QualityAnalyzer()
        scores = analyzer.calculate_quality_score(spec_set)
        
        if scores["overall"] < min_score:
            raise AssertionError(
                f"Quality score {scores['overall']:.1f} below minimum {min_score}"
            )
    
    @staticmethod
    def create_test_spec(level: int = 0, **kwargs) -> str:
        """Create test MSL specification at given level."""
        if level == 0:
            return """# Test Specification
## Requirements
- Requirement 1
- Requirement 2
"""
        elif level == 1:
            return f"""---
id: {kwargs.get('id', 'test-spec')}
---
# Test Specification
## Requirements
- REQ-001: Requirement 1
- REQ-002: Requirement 2
"""
        elif level == 2:
            return f"""---
id: {kwargs.get('id', 'test-spec')}
extends: {kwargs.get('extends', '')}
---
# Test Specification
## Requirements
- [!] REQ-001: [NEW] Critical requirement
- [x] REQ-002: [OVERRIDE] Completed requirement
"""
    
    @staticmethod
    def benchmark_parser(file_path: str, iterations: int = 100):
        """Benchmark parser performance."""
        import time
        from msl_parser import MSLParser
        
        content = Path(file_path).read_text()
        parser = MSLParser()
        
        start = time.time()
        for _ in range(iterations):
            parser.parse(content)
        end = time.time()
        
        avg_time = (end - start) / iterations * 1000  # ms
        print(f"Average parse time: {avg_time:.2f}ms")
        
        return avg_time < 10  # Should parse in under 10ms

# Performance benchmarks
def run_benchmarks():
    """Run performance benchmarks."""
    helper = MSLTestHelper()
    
    print("Running MSL Performance Benchmarks")
    print("=" * 50)
    
    # Create test files of different sizes
    sizes = [10, 100, 1000]  # Number of requirements
    
    for size in sizes:
        # Create test file
        reqs = [f"- REQ-{i:03d}: Requirement {i}" for i in range(1, size + 1)]
        content = f"""---
id: benchmark-{size}
---
# Benchmark Specification

## Requirements
{chr(10).join(reqs)}
"""
        
        Path(f"benchmark-{size}.md").write_text(content)
        
        # Benchmark
        print(f"\n{size} requirements:")
        helper.benchmark_parser(f"benchmark-{size}.md", iterations=100)

if __name__ == "__main__":
    run_benchmarks()
```

## Implementation Checklist

When implementing MSL tools, ensure you handle:

- [ ] All three MSL levels (L0, L1, L2)
- [ ] YAML frontmatter parsing
- [ ] Requirement ID extraction (REQ-XXX)
- [ ] Quick markers ([!], [?], [x], [@user], [#tag])
- [ ] Composite markers (v1.4.0+)
- [ ] Inheritance markers ([OVERRIDE], [NEW], [INHERIT])
- [ ] Template variable substitution
- [ ] Inheritance chain resolution
- [ ] Circular dependency detection
- [ ] Quality metric calculation
- [ ] Error reporting with line numbers
- [ ] Backward compatibility

## Error Handling

Common errors and how to handle them:

| Error | Severity | Action |
|-------|----------|--------|
| Missing Requirements section | Error | Reject document |
| Duplicate REQ-ID | Error | Report all duplicates |
| Undefined template variable | Error | Halt processing |
| Circular inheritance | Error | Reject specification |
| Parent spec not found | Error | Cannot resolve |
| Invalid marker syntax | Warning | Treat as text |
| Non-sequential REQ-IDs | Info | Continue processing |
| Missing document title | Warning | Continue processing |

---

This implementation reference provides everything needed to build MSL-compliant tools. All code examples are self-contained and can be copied directly into implementation projects. The reference follows MSL Level 2 specification exactly, ensuring consistent behavior across all implementations.