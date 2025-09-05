"""MSL Parser - Parse MSL markdown files into structured data."""

import re
from pathlib import Path
from typing import Dict, List, Optional, Any
import yaml


class MSLParser:
    """Parse MSL markdown files into structured data."""
    
    def __init__(self):
        self.req_pattern = re.compile(r'^-\s*(REQ-\d+:)?\s*(.+)$', re.MULTILINE)
        self.hierarchical_req_pattern = re.compile(r'^(REQ-\d+(?:\.\d+)*):?\s*(.+)$')
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
        """Parse requirements section into structured list with hierarchy support."""
        requirements = []
        lines = content.split('\n')
        current_parent = None
        parent_stack = []  # Stack to track parent requirements at each level
        
        for line_num, line in enumerate(lines):
            # Check indentation level (count leading spaces)
            indent_level = len(line) - len(line.lstrip())
            line_content = line.strip()
            
            if not line_content or not line_content.startswith('-'):
                continue
            
            # Parse the requirement
            req = self._parse_requirement_line(line_content)
            if not req:
                continue
                
            # Determine hierarchy based on indentation (2 spaces per level)
            depth = indent_level // 2
            req["depth"] = depth
            req["parent_id"] = None
            req["children"] = []
            
            # Handle hierarchical structure
            if depth == 0:
                # Top-level requirement
                requirements.append(req)
                parent_stack = [req]  # Reset stack with this as root
                current_parent = req
            else:
                # Sub-requirement - find appropriate parent
                while len(parent_stack) > depth:
                    parent_stack.pop()
                    
                if parent_stack:
                    parent = parent_stack[-1]
                    req["parent_id"] = parent.get("id")
                    
                    # Auto-generate hierarchical ID if not provided
                    if not req.get("id") and parent.get("id"):
                        parent_child_count = len(parent["children"]) + 1
                        req["id"] = f"{parent['id']}.{parent_child_count}"
                    
                    parent["children"].append(req)
                    parent_stack.append(req)
                else:
                    # Orphaned sub-requirement, add as top-level
                    requirements.append(req)
                    parent_stack = [req]
                
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
            "original_text": line,
            "markers": {},  # For composite markers
            "categories": [],  # For categorization markers
            "metrics": {}  # For metric markers
        }
        
        # Check for REQ-XXX ID (including hierarchical dot notation)
        id_match = re.match(r'^(REQ-\d+(?:\.\d+)*):\s*(.+)$', line)
        if id_match:
            requirement["id"] = id_match.group(1)
            line = id_match.group(2)
            requirement["text"] = line
            
            # Extract hierarchy info from dot notation
            if '.' in requirement["id"]:
                parts = requirement["id"].split('.')
                requirement["parent_ref"] = '.'.join(parts[:-1])
                requirement["hierarchy_level"] = len(parts) - 1
            else:
                requirement["hierarchy_level"] = 0
        
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
            
        # Check for markers (both simple and composite)
        if line.startswith('['):
            # Extract marker content between brackets
            marker_match = re.match(r'^\[([^\]]+)\]\s*(.+)$', line)
            if marker_match:
                marker_content = marker_match.group(1)
                text = marker_match.group(2)
                requirement["text"] = text
                
                # Parse markers (check for composite, key:value, or code links)
                if ('|' in marker_content or ':' in marker_content or 
                    marker_content.startswith('↔') or marker_content.startswith('<->') or
                    marker_content.startswith('→') or marker_content.startswith('->') or
                    marker_content.startswith('←') or marker_content.startswith('<-')):
                    self._parse_composite_markers(marker_content, requirement)
                else:
                    # Handle simple markers for backward compatibility
                    self._parse_simple_marker(marker_content, requirement)
                    
        return requirement
    
    def _parse_simple_marker(self, marker: str, requirement: Dict[str, Any]):
        """Parse a simple single marker."""
        if marker == '!':
            requirement["priority"] = "critical"
        elif marker == '!!':
            requirement["priority"] = "urgent"
        elif marker == '~':
            requirement["priority"] = "low"
        elif marker == '?':
            requirement["status"] = "uncertain"
        elif marker == 'x':
            requirement["status"] = "complete"
        elif marker == ' ':
            requirement["status"] = "pending"
        elif marker.startswith('@'):
            # Handle @user or @team-name
            requirement["assignee"] = marker[1:]
        elif marker.startswith('#'):
            requirement["tags"].append(marker[1:])
        else:
            # Store as a general marker
            requirement["markers"][marker] = True
    
    def _parse_composite_markers(self, marker_content: str, requirement: Dict[str, Any]):
        """Parse composite markers separated by pipes."""
        # Check if this is a code link first (before splitting)
        if (marker_content.startswith('↔') or marker_content.startswith('<->') or
            marker_content.startswith('→') or marker_content.startswith('->') or
            marker_content.startswith('←') or marker_content.startswith('<-')):
            # Treat entire content as a single code link component
            if '|' in marker_content:
                # Split but keep the first arrow part intact
                first_pipe = marker_content.index('|')
                components = [marker_content[:first_pipe].strip()] + marker_content[first_pipe+1:].split('|')
            else:
                components = [marker_content]
        else:
            components = marker_content.split('|')
        
        for component in components:
            component = component.strip()
            
            # Skip empty components
            if not component:
                continue
                
            # Check for code links first
            if component.startswith('↔'):
                # Bidirectional code link (unicode arrow)
                link_text = component[1:].strip()
                self._parse_code_link(requirement, link_text)
            elif component.startswith('<->'):
                # Bidirectional code link (ASCII)
                link_text = component[3:].strip()
                self._parse_code_link(requirement, link_text)
            elif component.startswith('→'):
                # Forward code link (unicode arrow)
                link_text = component[1:].strip()
                self._parse_code_link(requirement, link_text, direction='forward')
            elif component.startswith('->'):
                # Forward code link (ASCII)
                link_text = component[2:].strip()
                self._parse_code_link(requirement, link_text, direction='forward')
            elif component.startswith('←'):
                # Backward code link (unicode arrow)
                link_text = component[1:].strip()
                self._parse_code_link(requirement, link_text, direction='backward')
            elif component.startswith('<-'):
                # Backward code link (ASCII)
                link_text = component[2:].strip()
                self._parse_code_link(requirement, link_text, direction='backward')
            # Check for key:value pairs
            elif ':' in component:
                key, value = component.split(':', 1)
                key = key.strip()
                value = value.strip()
                
                # Handle specific key types
                if key in ['estimate', 'actual', 'variance']:
                    requirement["metrics"][key] = value
                elif key == 'progress':
                    requirement["metrics"]["progress"] = value
                elif key == 'coverage':
                    requirement["metrics"]["coverage"] = value
                elif key == 'confidence':
                    requirement["metrics"]["confidence"] = value
                elif key == 'sprint':
                    requirement["markers"]["sprint"] = value
                elif key == 'phase':
                    requirement["markers"]["phase"] = value
                elif key == 'milestone':
                    requirement["markers"]["milestone"] = value
                elif key == 'vendor':
                    requirement["markers"]["vendor"] = value
                elif key == 'eta':
                    requirement["markers"]["eta"] = value
                elif key == 'deployed':
                    requirement["status"] = f"deployed:{value}"
                elif key == 'stage':
                    requirement["markers"]["stage"] = value
                elif key == 'gap':
                    requirement["markers"]["gap"] = value
                elif key == 'review':
                    requirement["markers"]["review"] = value
                elif key == 'depends':
                    requirement["markers"]["depends"] = value
                elif key == 'blocks':
                    requirement["markers"]["blocks"] = value
                elif key == 'after':
                    requirement["markers"]["after"] = value
                elif key == 'parallel':
                    requirement["markers"]["parallel"] = value
                else:
                    # Store generic key:value
                    requirement["markers"][key] = value
            else:
                # Handle non key:value components
                if component in ['!', '!!', '~']:
                    # Priority markers
                    if component == '!':
                        requirement["priority"] = "critical"
                    elif component == '!!':
                        requirement["priority"] = "urgent"
                    elif component == '~':
                        requirement["priority"] = "low"
                elif component.startswith('@'):
                    # Assignment markers
                    assignee = component[1:]
                    if assignee.startswith('team-'):
                        requirement["assignee"] = assignee
                    elif assignee.startswith('role:'):
                        requirement["assignee"] = assignee
                    else:
                        requirement["assignee"] = assignee
                elif component.startswith('#'):
                    # Tag markers
                    requirement["tags"].append(component[1:])
                elif component in ['blocked', 'testing', 'review', 'complete', 'pending']:
                    # Status markers
                    requirement["status"] = component
                elif component in ['security', 'performance', 'ui', 'api', 'database']:
                    # Category markers
                    requirement["categories"].append(component)
                elif component in ['mvp', 'tested', 'deployed', 'external']:
                    # Boolean flag markers
                    requirement["markers"][component] = True
                else:
                    # Store as generic marker
                    requirement["markers"][component] = True
    
    def _parse_code_link(self, requirement: Dict[str, Any], link_text: str, direction: str = 'bidirectional'):
        """Parse code link and add to requirement."""
        if "code_links" not in requirement:
            requirement["code_links"] = []
        
        # Parse link format: file.ext:line or file.ext:start-end
        parts = link_text.split(':')
        if len(parts) >= 2:
            file_path = parts[0].strip()
            line_spec = ':'.join(parts[1:]).strip()
            
            # Parse line specification
            if '-' in line_spec:
                # Range format: 45-67
                line_parts = line_spec.split('-')
                start_line = line_parts[0].strip()
                end_line = line_parts[1].strip() if len(line_parts) > 1 else start_line
                
                requirement["code_links"].append({
                    "file": file_path,
                    "start_line": start_line,
                    "end_line": end_line,
                    "direction": direction,
                    "raw": link_text
                })
            else:
                # Single line format: 45
                requirement["code_links"].append({
                    "file": file_path,
                    "line": line_spec,
                    "direction": direction,
                    "raw": link_text
                })
        else:
            # Just file path, no line numbers
            requirement["code_links"].append({
                "file": link_text.strip(),
                "direction": direction,
                "raw": link_text
            })


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