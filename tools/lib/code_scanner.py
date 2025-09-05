"""MSL Code Scanner - Extract MSL references from source code comments."""

import re
import os
from pathlib import Path
from typing import List, Dict, Any, Optional


class CodeScanner:
    """Scan source code for MSL requirement references."""
    
    # Common comment patterns for different languages
    COMMENT_PATTERNS = {
        '.py': [
            r'#\s*MSL:\s*(REQ-[\w.-]+)',  # Python single-line
            r'"""[\s\S]*?MSL:\s*(REQ-[\w.-]+)[\s\S]*?"""',  # Python docstring
            r"'''[\s\S]*?MSL:\s*(REQ-[\w.-]+)[\s\S]*?'''",  # Python docstring alt
        ],
        '.js': [
            r'//\s*MSL:\s*(REQ-[\w.-]+)',  # JavaScript single-line
            r'/\*[\s\S]*?MSL:\s*(REQ-[\w.-]+)[\s\S]*?\*/',  # JavaScript multi-line
        ],
        '.ts': [
            r'//\s*MSL:\s*(REQ-[\w.-]+)',  # TypeScript single-line
            r'/\*[\s\S]*?MSL:\s*(REQ-[\w.-]+)[\s\S]*?\*/',  # TypeScript multi-line
        ],
        '.java': [
            r'//\s*MSL:\s*(REQ-[\w.-]+)',  # Java single-line
            r'/\*[\s\S]*?MSL:\s*(REQ-[\w.-]+)[\s\S]*?\*/',  # Java multi-line
        ],
        '.c': [
            r'//\s*MSL:\s*(REQ-[\w.-]+)',  # C single-line (C99+)
            r'/\*[\s\S]*?MSL:\s*(REQ-[\w.-]+)[\s\S]*?\*/',  # C multi-line
        ],
        '.cpp': [
            r'//\s*MSL:\s*(REQ-[\w.-]+)',  # C++ single-line
            r'/\*[\s\S]*?MSL:\s*(REQ-[\w.-]+)[\s\S]*?\*/',  # C++ multi-line
        ],
        '.cs': [
            r'//\s*MSL:\s*(REQ-[\w.-]+)',  # C# single-line
            r'/\*[\s\S]*?MSL:\s*(REQ-[\w.-]+)[\s\S]*?\*/',  # C# multi-line
            r'///\s*MSL:\s*(REQ-[\w.-]+)',  # C# XML doc
        ],
        '.go': [
            r'//\s*MSL:\s*(REQ-[\w.-]+)',  # Go single-line
            r'/\*[\s\S]*?MSL:\s*(REQ-[\w.-]+)[\s\S]*?\*/',  # Go multi-line
        ],
        '.rs': [
            r'//\s*MSL:\s*(REQ-[\w.-]+)',  # Rust single-line
            r'///\s*MSL:\s*(REQ-[\w.-]+)',  # Rust doc comment
            r'/\*[\s\S]*?MSL:\s*(REQ-[\w.-]+)[\s\S]*?\*/',  # Rust multi-line
        ],
        '.rb': [
            r'#\s*MSL:\s*(REQ-[\w.-]+)',  # Ruby single-line
        ],
        '.php': [
            r'//\s*MSL:\s*(REQ-[\w.-]+)',  # PHP single-line
            r'#\s*MSL:\s*(REQ-[\w.-]+)',  # PHP single-line alt
            r'/\*[\s\S]*?MSL:\s*(REQ-[\w.-]+)[\s\S]*?\*/',  # PHP multi-line
        ],
        '.sh': [
            r'#\s*MSL:\s*(REQ-[\w.-]+)',  # Shell single-line
        ],
    }
    
    # Alternative reference formats
    ALT_PATTERNS = [
        r'@implements\s+(REQ-[\w.-]+)',  # @implements annotation
        r'@requirement\s+(REQ-[\w.-]+)',  # @requirement annotation
        r'\[MSL:\s*(REQ-[\w.-]+)\]',  # [MSL: REQ-XXX] format
        r'<MSL>\s*(REQ-[\w.-]+)\s*</MSL>',  # XML-style tag
    ]
    
    def __init__(self, project_root: str = "."):
        """Initialize code scanner with project root."""
        self.project_root = Path(project_root)
        self.references = {}
    
    def scan_file(self, file_path: str) -> List[Dict[str, Any]]:
        """Scan a single file for MSL references."""
        references = []
        path = Path(file_path)
        
        if not path.exists():
            return references
        
        # Get file extension
        ext = path.suffix.lower()
        if ext not in self.COMMENT_PATTERNS:
            ext = self._guess_language(path)
        
        if ext not in self.COMMENT_PATTERNS:
            return references
        
        content = path.read_text(encoding='utf-8')
        lines = content.split('\n')
        
        # Apply language-specific patterns
        for pattern_str in self.COMMENT_PATTERNS[ext]:
            pattern = re.compile(pattern_str, re.MULTILINE)
            
            for match in pattern.finditer(content):
                req_id = match.group(1)
                # Find line number
                line_num = content[:match.start()].count('\n') + 1
                
                references.append({
                    'requirement_id': req_id,
                    'file': str(path.relative_to(self.project_root) if path.is_relative_to(self.project_root) else path),
                    'line': line_num,
                    'type': 'comment',
                    'context': self._get_context(lines, line_num - 1)
                })
        
        # Also check alternative patterns
        for pattern_str in self.ALT_PATTERNS:
            pattern = re.compile(pattern_str, re.MULTILINE)
            
            for match in pattern.finditer(content):
                req_id = match.group(1)
                line_num = content[:match.start()].count('\n') + 1
                
                # Check if this reference is already found
                if not any(r['line'] == line_num for r in references):
                    references.append({
                        'requirement_id': req_id,
                        'file': str(path.relative_to(self.project_root) if path.is_relative_to(self.project_root) else path),
                        'line': line_num,
                        'type': 'annotation',
                        'context': self._get_context(lines, line_num - 1)
                    })
        
        return references
    
    def scan_directory(self, directory: str, extensions: Optional[List[str]] = None) -> Dict[str, List[Dict[str, Any]]]:
        """Scan a directory recursively for MSL references."""
        dir_path = Path(directory)
        all_references = {}
        
        if not dir_path.exists():
            return all_references
        
        # Default to common source file extensions
        if not extensions:
            extensions = list(self.COMMENT_PATTERNS.keys())
        
        # Scan all matching files
        for ext in extensions:
            for file_path in dir_path.rglob(f'*{ext}'):
                # Skip common directories to ignore
                if any(part.startswith('.') or part in ['node_modules', '__pycache__', 'venv', 'build', 'dist'] 
                       for part in file_path.parts):
                    continue
                
                refs = self.scan_file(str(file_path))
                if refs:
                    file_key = str(file_path.relative_to(self.project_root) if file_path.is_relative_to(self.project_root) else file_path)
                    all_references[file_key] = refs
        
        return all_references
    
    def find_requirement_implementations(self, requirement_id: str, directory: str = ".") -> List[Dict[str, Any]]:
        """Find all code locations that implement a specific requirement."""
        all_refs = self.scan_directory(directory)
        implementations = []
        
        for file_path, refs in all_refs.items():
            for ref in refs:
                if ref['requirement_id'] == requirement_id:
                    implementations.append(ref)
        
        return implementations
    
    def generate_reverse_links(self, spec_file: str, code_directory: str = ".") -> Dict[str, List[str]]:
        """Generate reverse links from code to spec requirements."""
        from .parser import MSLParser
        
        # Parse spec file to get requirements
        parser = MSLParser()
        parsed = parser.parse_file(spec_file)
        requirements = parsed.get('requirements', [])
        
        # Build requirement ID map
        req_map = {}
        for req in requirements:
            if req.get('id'):
                req_map[req['id']] = {
                    'text': req.get('text', ''),
                    'implementations': []
                }
        
        # Scan code for references
        all_refs = self.scan_directory(code_directory)
        
        # Map code references back to requirements
        for file_path, refs in all_refs.items():
            for ref in refs:
                req_id = ref['requirement_id']
                if req_id in req_map:
                    req_map[req_id]['implementations'].append({
                        'file': ref['file'],
                        'line': ref['line'],
                        'type': ref['type']
                    })
        
        return req_map
    
    def _guess_language(self, path: Path) -> str:
        """Guess language from file content or shebang."""
        try:
            with open(path, 'r', encoding='utf-8') as f:
                first_line = f.readline().strip()
                
            # Check shebang
            if first_line.startswith('#!'):
                if 'python' in first_line:
                    return '.py'
                elif 'node' in first_line or 'nodejs' in first_line:
                    return '.js'
                elif 'sh' in first_line or 'bash' in first_line:
                    return '.sh'
                elif 'ruby' in first_line:
                    return '.rb'
        except:
            pass
        
        return ''
    
    def _get_context(self, lines: List[str], line_index: int, context_size: int = 2) -> str:
        """Get surrounding context for a reference."""
        start = max(0, line_index - context_size)
        end = min(len(lines), line_index + context_size + 1)
        
        context_lines = []
        for i in range(start, end):
            prefix = '>' if i == line_index else ' '
            context_lines.append(f"{prefix} {lines[i]}")
        
        return '\n'.join(context_lines)
    
    def verify_bidirectional_links(self, spec_file: str, code_directory: str = ".") -> Dict[str, Any]:
        """Verify bidirectional links between spec and code."""
        from .parser import MSLParser
        
        parser = MSLParser()
        parsed = parser.parse_file(spec_file)
        requirements = parsed.get('requirements', [])
        
        results = {
            'total_requirements': len(requirements),
            'linked_requirements': 0,
            'unlinked_requirements': [],
            'broken_links': [],
            'verified_links': []
        }
        
        # Check each requirement
        for req in requirements:
            req_id = req.get('id')
            if not req_id:
                continue
            
            code_links = req.get('code_links', [])
            implementations = self.find_requirement_implementations(req_id, code_directory)
            
            if code_links or implementations:
                results['linked_requirements'] += 1
                
                # Verify forward links (spec -> code)
                for link in code_links:
                    file_path = Path(link['file'])
                    if not file_path.exists():
                        # Try relative to project root
                        file_path = self.project_root / link['file']
                    
                    if file_path.exists():
                        results['verified_links'].append({
                            'requirement': req_id,
                            'file': link['file'],
                            'direction': link.get('direction', 'forward')
                        })
                    else:
                        results['broken_links'].append({
                            'requirement': req_id,
                            'file': link['file'],
                            'error': 'File not found'
                        })
            else:
                results['unlinked_requirements'].append(req_id)
        
        return results