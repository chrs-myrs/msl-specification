"""MSL Validator - Validate MSL documents against the specification."""

import re
from typing import List, Dict, Any, Optional
from pathlib import Path


class ValidationIssue:
    """Represents a validation issue."""
    
    def __init__(self, level: str, message: str, line: Optional[int] = None, column: Optional[int] = None):
        self.level = level  # "error", "warning", "info"
        self.message = message
        self.line = line
        self.column = column
        
    def __str__(self):
        location = ""
        if self.line:
            location = f":{self.line}"
            if self.column:
                location += f":{self.column}"
        return f"[{self.level.upper()}]{location} {self.message}"


class MSLValidator:
    """Validate MSL documents."""
    
    def __init__(self, strict: bool = False):
        self.strict = strict
        self.req_id_pattern = re.compile(r'^REQ-\d+$')
        self.hierarchical_req_id_pattern = re.compile(r'^REQ-\d+(?:\.\d+)*$')
        
    def validate(self, parsed: Dict[str, Any]) -> List[ValidationIssue]:
        """Validate a parsed MSL document."""
        issues = []
        
        # Check for requirements section (Level 1+)
        if parsed.get("level", 0) >= 1 and not parsed.get("requirements"):
            issues.append(ValidationIssue(
                "warning",
                "Missing ## Requirements section (required for Level 1+)"
            ))
            
        # Check for title
        if not parsed.get("title"):
            issues.append(ValidationIssue(
                "warning",
                "Missing document title (# Title)"
            ))
            
        # Validate metadata
        issues.extend(self._validate_metadata(parsed.get("metadata", {})))
        
        # Validate requirements
        issues.extend(self._validate_requirements(parsed.get("requirements", [])))
        
        return issues
    
    def _validate_metadata(self, metadata: Dict[str, Any]) -> List[ValidationIssue]:
        """Validate frontmatter metadata."""
        issues = []
        
        # Check spec version
        if "spec" in metadata and metadata["spec"] not in ["v1", "v1.1"]:
            issues.append(ValidationIssue(
                "warning",
                f"Unknown spec version: {metadata['spec']}"
            ))
            
        # Check type
        if "type" in metadata and metadata["type"] not in ["requirement", "template"]:
            issues.append(ValidationIssue(
                "warning",
                f"Unknown document type: {metadata['type']}"
            ))
            
        # Check priority
        if "priority" in metadata:
            valid_priorities = ["critical", "high", "medium", "low"]
            if metadata["priority"] not in valid_priorities:
                issues.append(ValidationIssue(
                    "warning",
                    f"Invalid priority: {metadata['priority']}. Valid values: {', '.join(valid_priorities)}"
                ))
                
        # Check status
        if "status" in metadata:
            valid_statuses = ["draft", "active", "complete", "deprecated", "uncertain", "pending"]
            if metadata["status"] not in valid_statuses:
                issues.append(ValidationIssue(
                    "warning",
                    f"Invalid status: {metadata['status']}. Valid values: {', '.join(valid_statuses)}"
                ))
                
        # Check extends reference
        if "extends" in metadata:
            # In a real implementation, we'd check if the parent exists
            if self.strict and not self._check_parent_exists(metadata["extends"]):
                issues.append(ValidationIssue(
                    "error",
                    f"Parent spec not found: {metadata['extends']}"
                ))
                
        return issues
    
    def _validate_requirements(self, requirements: List[Dict[str, Any]]) -> List[ValidationIssue]:
        """Validate requirements list."""
        issues = []
        seen_ids = {}
        
        for i, req in enumerate(requirements):
            # Check for duplicate IDs
            if req.get("id"):
                # Accept both flat and hierarchical IDs
                if not (self.req_id_pattern.match(req["id"]) or 
                        self.hierarchical_req_id_pattern.match(req["id"])):
                    issues.append(ValidationIssue(
                        "warning",
                        f"Invalid requirement ID format: {req['id']}. Expected REQ-XXX or REQ-XXX.Y.Z"
                    ))
                    
                if req["id"] in seen_ids:
                    issues.append(ValidationIssue(
                        "error",
                        f"Duplicate requirement ID: {req['id']} (first seen at requirement {seen_ids[req['id']] + 1})"
                    ))
                else:
                    seen_ids[req["id"]] = i
                    
            # Check for empty requirements
            if not req.get("text", "").strip():
                issues.append(ValidationIssue(
                    "warning",
                    f"Empty requirement at position {i + 1}"
                ))
            
            # Validate composite markers
            if req.get("markers") or req.get("metrics"):
                issues.extend(self._validate_composite_markers(req, i))
            
            # Validate hierarchical structure
            if req.get("children"):
                issues.extend(self._validate_hierarchy(req, i))
                
        # Check for sequential IDs (optional)
        if self.strict:
            expected_ids = [f"REQ-{i:03d}" for i in range(1, len(requirements) + 1)]
            actual_ids = [req.get("id") for req in requirements if req.get("id")]
            
            if actual_ids and actual_ids != expected_ids[:len(actual_ids)]:
                issues.append(ValidationIssue(
                    "info",
                    "Requirement IDs are not sequential"
                ))
                
        return issues
    
    def _validate_composite_markers(self, requirement: Dict[str, Any], index: int) -> List[ValidationIssue]:
        """Validate composite markers for consistency and correctness."""
        issues = []
        req_id = requirement.get("id", f"requirement {index + 1}")
        
        # Check for conflicting status markers
        status = requirement.get("status")
        markers = requirement.get("markers", {})
        
        if status == "blocked" and status == "complete":
            issues.append(ValidationIssue(
                "error",
                f"Conflicting status in {req_id}: cannot be both blocked and complete"
            ))
        
        # Validate metrics values
        metrics = requirement.get("metrics", {})
        
        # Validate progress percentage
        if "progress" in metrics:
            progress_str = metrics["progress"]
            if progress_str.endswith('%'):
                try:
                    progress = int(progress_str[:-1])
                    if not 0 <= progress <= 100:
                        issues.append(ValidationIssue(
                            "warning",
                            f"Progress in {req_id} should be between 0-100%: {progress_str}"
                        ))
                except ValueError:
                    issues.append(ValidationIssue(
                        "warning",
                        f"Invalid progress format in {req_id}: {progress_str}"
                    ))
        
        # Validate coverage percentage
        if "coverage" in metrics:
            coverage_str = metrics["coverage"]
            if coverage_str.endswith('%'):
                try:
                    coverage = int(coverage_str[:-1])
                    if not 0 <= coverage <= 100:
                        issues.append(ValidationIssue(
                            "warning",
                            f"Coverage in {req_id} should be between 0-100%: {coverage_str}"
                        ))
                except ValueError:
                    issues.append(ValidationIssue(
                        "warning",
                        f"Invalid coverage format in {req_id}: {coverage_str}"
                    ))
        
        # Validate confidence levels
        if "confidence" in metrics:
            valid_confidence = ["high", "medium", "low"]
            if metrics["confidence"] not in valid_confidence:
                issues.append(ValidationIssue(
                    "warning",
                    f"Invalid confidence in {req_id}: {metrics['confidence']}. Valid values: {', '.join(valid_confidence)}"
                ))
        
        # Validate stage transitions
        if "stage" in markers:
            valid_stages = ["design", "implementation", "testing", "review", "deployed", "deprecated"]
            stage = markers["stage"]
            
            # Handle deployed:env format
            if stage.startswith("deployed:"):
                base_stage = "deployed"
            else:
                base_stage = stage
                
            if base_stage not in valid_stages:
                issues.append(ValidationIssue(
                    "warning",
                    f"Invalid stage in {req_id}: {stage}. Valid stages: {', '.join(valid_stages)}"
                ))
        
        # Validate gap types
        if "gap" in markers:
            valid_gaps = ["test", "doc", "implementation", "review", "spec", "performance"]
            gap = markers["gap"]
            
            # Handle gap:subtype format
            if ':' in gap:
                gap_type = gap.split(':')[0]
            else:
                gap_type = gap
                
            if gap_type not in valid_gaps:
                issues.append(ValidationIssue(
                    "warning",
                    f"Invalid gap type in {req_id}: {gap}. Valid types: {', '.join(valid_gaps)}"
                ))
        
        # Validate dependencies reference existing requirements
        if self.strict:
            for dep_type in ["depends", "blocks", "after", "parallel"]:
                if dep_type in markers:
                    dep_value = markers[dep_type]
                    # Split comma-separated dependencies
                    deps = [d.strip() for d in dep_value.split(',')]
                    for dep in deps:
                        if not self.req_id_pattern.match(dep):
                            issues.append(ValidationIssue(
                                "warning",
                                f"Invalid dependency format in {req_id} [{dep_type}]: {dep}"
                            ))
        
        return issues
    
    def _validate_hierarchy(self, requirement: Dict[str, Any], index: int) -> List[ValidationIssue]:
        """Validate hierarchical requirement structure."""
        issues = []
        req_id = requirement.get("id", f"requirement {index + 1}")
        
        # Check depth limit (default max 4 levels)
        max_depth = 4
        
        def check_depth(req: Dict[str, Any], current_depth: int = 0) -> int:
            if current_depth > max_depth:
                issues.append(ValidationIssue(
                    "warning",
                    f"Requirement hierarchy exceeds recommended depth of {max_depth} levels at {req.get('id', 'unknown')}"
                ))
                return current_depth
            
            max_child_depth = current_depth
            for child in req.get("children", []):
                child_depth = check_depth(child, current_depth + 1)
                max_child_depth = max(max_child_depth, child_depth)
            
            return max_child_depth
        
        check_depth(requirement)
        
        # Validate parent-child ID consistency
        parent_id = requirement.get("id")
        if parent_id:
            for i, child in enumerate(requirement.get("children", [])):
                child_id = child.get("id")
                if child_id:
                    # Check if child ID follows parent.N pattern
                    expected_prefix = f"{parent_id}."
                    if not child_id.startswith(expected_prefix):
                        issues.append(ValidationIssue(
                            "warning",
                            f"Child requirement {child_id} doesn't follow parent ID pattern {expected_prefix}N"
                        ))
                    
                    # Check for duplicate child IDs
                    child_ids = [c.get("id") for c in requirement.get("children", []) if c.get("id")]
                    if child_ids.count(child_id) > 1:
                        issues.append(ValidationIssue(
                            "error",
                            f"Duplicate child ID {child_id} under parent {parent_id}"
                        ))
        
        # Validate child requirements recursively
        for child in requirement.get("children", []):
            if child.get("children"):
                issues.extend(self._validate_hierarchy(child, index))
        
        return issues
    
    def _check_parent_exists(self, parent_id: str) -> bool:
        """Check if a parent spec exists (placeholder for real implementation)."""
        # In a real implementation, this would check the filesystem or a registry
        return True
    
    def validate_file(self, file_path: str) -> List[ValidationIssue]:
        """Validate an MSL file directly."""
        from .parser import MSLParser
        
        try:
            parser = MSLParser()
            parsed = parser.parse_file(file_path)
            issues = self.validate(parsed)
            
            # Add file context to issues
            for issue in issues:
                issue.file = file_path
                
            return issues
            
        except Exception as e:
            return [ValidationIssue("error", f"Failed to parse file: {e}")]
    
    def validate_directory(self, directory: str, pattern: str = "**/*.md") -> Dict[str, List[ValidationIssue]]:
        """Validate all MSL files in a directory."""
        from pathlib import Path
        
        results = {}
        path = Path(directory)
        
        for file_path in path.glob(pattern):
            if file_path.is_file():
                issues = self.validate_file(str(file_path))
                if issues:
                    results[str(file_path)] = issues
                    
        return results