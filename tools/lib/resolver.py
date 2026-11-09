"""MSL Resolver - Resolve inheritance chains in MSL documents."""

import os
import re
from typing import Dict, Any, List, Optional, Tuple
from pathlib import Path
from .parser import MSLParser

FRONTMATTER_ID = re.compile(r"^id:\s*([^\s#]+)")
SKIP_DIRS = {"node_modules", "var", "build", "dist", "generated", "__pycache__"}


class MSLResolver:
    """Resolve inheritance and merge specifications."""
    
    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        self.parser = MSLParser()
        self._cache = {}
        self._id_index: Optional[Dict[str, List[Path]]] = None
        self._implicit_index: Dict[str, List[Path]] = {}
        
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
        path = self._find_spec(spec_id)
        if path is None:
            raise FileNotFoundError(f"Specification not found: {spec_id}")
        return self.parser.parse_file(str(path))

    def _find_spec(self, spec_id: str) -> Optional[Path]:
        """Find a spec by explicit id anywhere under base_path, else by implicit id (file name)."""
        if self._id_index is None:
            self._id_index, self._implicit_index = self._index_ids()
        # An explicit id takes precedence over a file name that matches it
        for index in (self._id_index, self._implicit_index):
            paths = index.get(spec_id, [])
            if len(paths) > 1:
                listed = ", ".join(str(path) for path in paths)
                raise ValueError(f"Specification id {spec_id} is declared by more than one document: {listed}")
            if paths:
                return paths[0]
        return None

    def _index_ids(self) -> Tuple[Dict[str, List[Path]], Dict[str, List[Path]]]:
        """Map explicit frontmatter ids, and implicit ids of documents without one, to their files."""
        explicit: Dict[str, List[Path]] = {}
        implicit: Dict[str, List[Path]] = {}
        for root, dirs, files in os.walk(self.base_path):
            dirs[:] = sorted(d for d in dirs if not d.startswith(".") and d not in SKIP_DIRS)
            for name in sorted(files):
                if not name.endswith((".md", ".msl")):
                    continue
                path = Path(root) / name
                spec_id = self._frontmatter_id(path)
                if spec_id:
                    explicit.setdefault(spec_id, []).append(path)
                else:
                    implicit.setdefault(self._implicit_id(name), []).append(path)
        return explicit, implicit

    @staticmethod
    def _implicit_id(name: str) -> str:
        """A document's file name without its extension, counting .spec.md as one extension."""
        for suffix in (".spec.md", ".md", ".msl"):
            if name.endswith(suffix):
                return name[: -len(suffix)]
        return name

    @staticmethod
    def _frontmatter_id(path: Path) -> Optional[str]:
        """Return the id declared in a file's leading frontmatter, if any."""
        try:
            with open(path, encoding="utf-8") as handle:
                if handle.readline().rstrip() != "---":
                    return None
                for line in handle:
                    if line.rstrip() == "---":
                        return None
                    match = FRONTMATTER_ID.match(line)
                    if match:
                        return match.group(1).strip("'\"")
        except (OSError, UnicodeDecodeError):
            return None
        return None
        
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