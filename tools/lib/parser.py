"""MSL Parser - Parse MSL markdown files into structured data."""

import re
from pathlib import Path
from typing import Dict, List, Optional, Any
import yaml


class MSLParser:
    """Parse MSL markdown files into structured data."""
    
    def __init__(self):
        self.req_pattern = re.compile(r'^-\s*(REQ-\d+:)?\s*(.+)$', re.MULTILINE)
        self.marker_pattern = re.compile(r'^\[([\!\?\@\#]|x|\s)\]\s*(.+)$')
        
    def parse_file(self, file_path: str) -> Dict[str, Any]:
        """Parse an MSL file and return structured data."""
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
            
        content = path.read_text(encoding='utf-8')
        return self.parse_content(content, file_path)
    
    def parse_content(self, content: str, source: str = "unknown") -> Dict[str, Any]:
        """Parse MSL content and return structured data."""
        result = {
            "source": source,
            "level": 0,
            "metadata": {},
            "title": None,
            "summary": None,
            "requirements": [],
            "notes": None,
            "raw_content": content
        }
        
        # Extract frontmatter if present
        frontmatter, body = self._extract_frontmatter(content)
        if frontmatter:
            result["metadata"] = frontmatter
            result["level"] = 1 if "id" in frontmatter else 2
        
        # Extract file ID from path if no frontmatter ID
        if "id" not in result["metadata"] and source != "unknown":
            result["metadata"]["id"] = Path(source).stem
            
        # Apply defaults
        self._apply_defaults(result["metadata"])
        
        # Parse body sections
        sections = self._parse_sections(body)
        
        # Extract title
        if "title" in sections:
            result["title"] = sections["title"]
            
        # Extract summary
        if "summary" in sections:
            result["summary"] = sections["summary"]
            
        # Extract requirements
        if "requirements" in sections:
            result["requirements"] = self._parse_requirements(sections["requirements"])
            
        # Extract notes
        if "notes" in sections:
            result["notes"] = sections["notes"]
            
        return result
    
    def _extract_frontmatter(self, content: str) -> tuple[Optional[Dict], str]:
        """Extract YAML frontmatter and return (metadata, remaining_content)."""
        if not content.startswith('---'):
            # Check for HTML comment style extends
            comment_extends = re.search(r'<!--\s*extends:\s*([^\s]+)\s*-->', content)
            if comment_extends:
                metadata = {"extends": comment_extends.group(1)}
                body = re.sub(r'<!--\s*extends:\s*[^\s]+\s*-->\n?', '', content)
                return metadata, body
            return None, content
            
        try:
            parts = content.split('---', 2)
            if len(parts) >= 3:
                metadata = yaml.safe_load(parts[1])
                body = parts[2]
                return metadata or {}, body
        except yaml.YAMLError:
            pass
            
        return None, content
    
    def _apply_defaults(self, metadata: Dict[str, Any]):
        """Apply smart defaults to metadata."""
        defaults = {
            "spec": "v1",
            "type": "requirement",
            "status": "draft"
        }
        
        for key, value in defaults.items():
            if key not in metadata:
                metadata[key] = value
    
    def _parse_sections(self, content: str) -> Dict[str, str]:
        """Parse markdown sections."""
        sections = {}
        
        # Extract title (first # heading)
        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if title_match:
            sections["title"] = title_match.group(1).strip()
        
        # Extract sections by ## headings
        section_pattern = re.compile(r'^##\s+(\w+)\s*$', re.MULTILINE)
        matches = list(section_pattern.finditer(content))
        
        for i, match in enumerate(matches):
            section_name = match.group(1).lower()
            start = match.end()
            end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
            section_content = content[start:end].strip()
            sections[section_name] = section_content
            
        return sections
    
    def _parse_requirements(self, content: str) -> List[Dict[str, Any]]:
        """Parse requirements section into structured list."""
        requirements = []
        lines = content.split('\n')
        
        for line in lines:
            line = line.strip()
            if not line or not line.startswith('-'):
                continue
                
            req = self._parse_requirement_line(line)
            if req:
                requirements.append(req)
                
        return requirements
    
    def _parse_requirement_line(self, line: str) -> Optional[Dict[str, Any]]:
        """Parse a single requirement line."""
        # Remove leading dash
        line = line[1:].strip()
        
        requirement = {
            "text": line,
            "id": None,
            "priority": "medium",
            "status": "pending",
            "tags": [],
            "assignee": None,
            "inheritance": "inherit",
            "original_text": line
        }
        
        # Check for REQ-XXX ID
        id_match = re.match(r'^(REQ-\d+):\s*(.+)$', line)
        if id_match:
            requirement["id"] = id_match.group(1)
            line = id_match.group(2)
            requirement["text"] = line
        
        # Check for inheritance markers
        if line.startswith("[OVERRIDE]") or line.lower().startswith("modified:"):
            requirement["inheritance"] = "override"
            line = re.sub(r'^\[(OVERRIDE)\]|^modified:\s*', '', line, flags=re.IGNORECASE)
            requirement["text"] = line.strip()
        elif line.startswith("[NEW]") or line.lower().startswith("new:"):
            requirement["inheritance"] = "new"
            line = re.sub(r'^\[(NEW)\]|^new:\s*', '', line, flags=re.IGNORECASE)
            requirement["text"] = line.strip()
        elif line.startswith("[INHERIT]"):
            requirement["inheritance"] = "inherit"
            line = line.replace("[INHERIT]", "").strip()
            requirement["text"] = line
            
        # Check for quick markers
        if line.startswith('['):
            marker_match = re.match(r'^\[([\!\?\@\#a-z]|x|\s)\]\s*(.+)$', line)
            if marker_match:
                marker = marker_match.group(1)
                text = marker_match.group(2)
                requirement["text"] = text
                
                if marker == '!':
                    requirement["priority"] = "critical"
                elif marker == '?':
                    requirement["status"] = "uncertain"
                elif marker == 'x':
                    requirement["status"] = "complete"
                elif marker == ' ':
                    requirement["status"] = "pending"
                elif marker.startswith('@'):
                    requirement["assignee"] = marker[1:]
                elif marker.startswith('#'):
                    requirement["tags"].append(marker[1:])
                    
        return requirement


class MSLLevel:
    """Determine MSL level of a document."""
    
    @staticmethod
    def detect(parsed: Dict[str, Any]) -> int:
        """Detect the MSL level of a parsed document."""
        metadata = parsed.get("metadata", {})
        
        # Level 2: Full metadata
        if any(key in metadata for key in ["extends", "tags", "priority", "status", "variables"]):
            return 2
            
        # Level 1: Has ID
        if "id" in metadata:
            return 1
            
        # Level 0: Pure markdown
        return 0