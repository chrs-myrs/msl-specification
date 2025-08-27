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
                if not self.req_id_pattern.match(req["id"]):
                    issues.append(ValidationIssue(
                        "warning",
                        f"Invalid requirement ID format: {req['id']}. Expected REQ-XXX"
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