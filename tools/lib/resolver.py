"""MSL Resolver - Resolve inheritance chains in MSL documents."""

from typing import Dict, Any, List, Optional
from pathlib import Path
from .parser import MSLParser


class MSLResolver:
    """Resolve inheritance and merge specifications."""
    
    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        self.parser = MSLParser()
        self._cache = {}
        
    def resolve(self, spec_id: str) -> Dict[str, Any]:
        """Resolve a specification with all its inheritance."""
        if spec_id in self._cache:
            return self._cache[spec_id]
            
        # Load the spec
        spec = self._load_spec(spec_id)
        
        # If it extends another spec, resolve parent first
        if "extends" in spec.get("metadata", {}):
            parent_id = spec["metadata"]["extends"]
            parent = self.resolve(parent_id)
            spec = self._merge_specs(parent, spec)
            
        self._cache[spec_id] = spec
        return spec
        
    def _load_spec(self, spec_id: str) -> Dict[str, Any]:
        """Load a specification by ID."""
        # Try to find the spec file
        possible_paths = [
            self.base_path / f"{spec_id}.md",
            self.base_path / f"{spec_id}.msl",
            self.base_path / "specs" / f"{spec_id}.md",
            self.base_path / "templates" / f"{spec_id}.md",
        ]
        
        for path in possible_paths:
            if path.exists():
                return self.parser.parse_file(str(path))
                
        raise FileNotFoundError(f"Specification not found: {spec_id}")
        
    def _merge_specs(self, parent: Dict[str, Any], child: Dict[str, Any]) -> Dict[str, Any]:
        """Merge parent and child specifications."""
        result = parent.copy()
        
        # Merge metadata
        result["metadata"] = {**parent.get("metadata", {}), **child.get("metadata", {})}
        
        # Use child's title and summary
        if child.get("title"):
            result["title"] = child["title"]
        if child.get("summary"):
            result["summary"] = child["summary"]
            
        # Merge requirements
        result["requirements"] = self._merge_requirements(
            parent.get("requirements", []),
            child.get("requirements", [])
        )
        
        # Use child's notes
        if child.get("notes"):
            result["notes"] = child["notes"]
            
        return result
        
    def _merge_requirements(self, parent_reqs: List[Dict], child_reqs: List[Dict]) -> List[Dict]:
        """Merge parent and child requirements based on inheritance markers."""
        result = []
        parent_by_id = {req["id"]: req for req in parent_reqs if req.get("id")}
        used_parent_ids = set()
        
        for req in child_reqs:
            inheritance = req.get("inheritance", "inherit")
            req_id = req.get("id")
            
            if inheritance == "new":
                # New requirement, just add it
                result.append(req)
            elif inheritance == "override" and req_id in parent_by_id:
                # Override parent requirement
                result.append(req)
                used_parent_ids.add(req_id)
            elif inheritance == "inherit" and req_id in parent_by_id:
                # Inherit from parent (possibly with modifications)
                parent_req = parent_by_id[req_id].copy()
                parent_req.update(req)
                result.append(parent_req)
                used_parent_ids.add(req_id)
            else:
                # Default: add as is
                result.append(req)
                
        # Add remaining parent requirements not overridden
        for req_id, req in parent_by_id.items():
            if req_id not in used_parent_ids:
                result.append(req)
                
        return result