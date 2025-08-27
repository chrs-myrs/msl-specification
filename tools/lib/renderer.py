"""MSL Renderer - Render MSL documents with templates and variables."""

from typing import Dict, Any, Optional
import re


class MSLRenderer:
    """Render MSL documents with variable substitution."""
    
    def __init__(self):
        self.jinja2_available = False
        try:
            import jinja2
            self.jinja2_available = True
        except ImportError:
            pass
            
    def render(self, content: str, variables: Dict[str, Any]) -> str:
        """Render content with variable substitution."""
        if self.jinja2_available:
            return self._render_jinja2(content, variables)
        else:
            return self._render_simple(content, variables)
            
    def _render_jinja2(self, content: str, variables: Dict[str, Any]) -> str:
        """Render using Jinja2 if available."""
        import jinja2
        template = jinja2.Template(content)
        return template.render(**variables)
        
    def _render_simple(self, content: str, variables: Dict[str, Any]) -> str:
        """Simple variable substitution without Jinja2."""
        result = content
        
        for key, value in variables.items():
            # Replace ${variable} syntax
            result = result.replace(f"${{{key}}}", str(value))
            # Also replace $variable syntax
            result = re.sub(rf'\${key}\b', str(value), result)
            
        return result
        
    def render_parsed(self, parsed: Dict[str, Any]) -> str:
        """Render a parsed MSL document back to markdown."""
        lines = []
        
        # Add frontmatter if present
        metadata = parsed.get("metadata", {})
        if metadata and any(k != "id" for k in metadata.keys()):
            lines.append("---")
            for key, value in metadata.items():
                if isinstance(value, list):
                    lines.append(f"{key}: [{', '.join(str(v) for v in value)}]")
                elif isinstance(value, dict):
                    lines.append(f"{key}:")
                    for k, v in value.items():
                        lines.append(f"  {k}: {v}")
                else:
                    lines.append(f"{key}: {value}")
            lines.append("---")
            lines.append("")
            
        # Add title
        if parsed.get("title"):
            lines.append(f"# {parsed['title']}")
            lines.append("")
            
        # Add summary
        if parsed.get("summary"):
            lines.append("## Summary")
            lines.append(parsed["summary"])
            lines.append("")
            
        # Add requirements
        if parsed.get("requirements"):
            lines.append("## Requirements")
            for req in parsed["requirements"]:
                line = "- "
                if req.get("id"):
                    line += f"{req['id']}: "
                    
                # Add inheritance marker if present
                inheritance = req.get("inheritance")
                if inheritance == "override":
                    line += "[OVERRIDE] "
                elif inheritance == "new":
                    line += "[NEW] "
                elif inheritance == "inherit" and req.get("id"):
                    line += "[INHERIT] "
                    
                # Add priority/status markers
                if req.get("priority") == "critical":
                    line = "- [!] " + line[2:]
                elif req.get("status") == "uncertain":
                    line = "- [?] " + line[2:]
                elif req.get("status") == "complete":
                    line = "- [x] " + line[2:]
                elif req.get("status") == "pending":
                    line = "- [ ] " + line[2:]
                    
                line += req.get("text", "")
                lines.append(line)
            lines.append("")
            
        # Add notes
        if parsed.get("notes"):
            lines.append("## Notes")
            lines.append(parsed["notes"])
            lines.append("")
            
        return "\n".join(lines)