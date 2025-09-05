"""MSL Validation Configuration System."""

import os
import re
import json
import yaml
from pathlib import Path
from typing import Dict, Any, List, Optional, Callable
from dataclasses import dataclass, field


@dataclass
class ValidationConfig:
    """Configuration for MSL validation."""
    
    # ID Format Rules
    require_ids: bool = False
    id_format: str = r"^REQ-\d+(?:\.\d+)*$"
    id_sequence_check: bool = False
    
    # Content Rules
    require_markers: List[str] = field(default_factory=list)
    forbid_markers: List[str] = field(default_factory=list)
    max_depth: int = 4
    min_requirements: int = 0
    max_requirements: int = 1000
    
    # Link Validation
    require_code_links: bool = False
    validate_file_paths: bool = True
    check_dead_links: bool = False
    
    # Review Rules
    require_review: List[str] = field(default_factory=list)
    review_timeout_days: int = 7
    
    # Custom Validators
    custom_validators: List[str] = field(default_factory=list)
    
    # Severity Overrides
    severity_overrides: Dict[str, str] = field(default_factory=dict)
    
    # Strict Mode
    strict: bool = False
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ValidationConfig':
        """Create config from dictionary."""
        # Filter out unknown fields
        valid_fields = {f.name for f in cls.__dataclass_fields__.values()}
        filtered_data = {k: v for k, v in data.items() if k in valid_fields}
        return cls(**filtered_data)
    
    @classmethod
    def from_yaml(cls, yaml_content: str) -> 'ValidationConfig':
        """Create config from YAML string."""
        data = yaml.safe_load(yaml_content) or {}
        validation_section = data.get('validation', data)
        return cls.from_dict(validation_section)
    
    @classmethod
    def from_file(cls, file_path: str) -> 'ValidationConfig':
        """Load config from file (.mslrc or frontmatter)."""
        path = Path(file_path)
        if not path.exists():
            return cls()
            
        content = path.read_text(encoding='utf-8')
        
        # Try to parse as YAML
        try:
            return cls.from_yaml(content)
        except yaml.YAMLError:
            # If not valid YAML, return default config
            return cls()
    
    @classmethod
    def find_config(cls, start_path: str = ".") -> 'ValidationConfig':
        """Find and load .mslrc configuration file."""
        current_path = Path(start_path).resolve()
        
        # Search for .mslrc in current and parent directories
        while current_path != current_path.parent:
            config_file = current_path / ".mslrc"
            if config_file.exists():
                return cls.from_file(str(config_file))
            
            # Also check for .mslrc.yaml or .mslrc.yml
            for ext in ['.yaml', '.yml']:
                config_file = current_path / f".mslrc{ext}"
                if config_file.exists():
                    return cls.from_file(str(config_file))
            
            current_path = current_path.parent
        
        # Check home directory
        home_config = Path.home() / ".mslrc"
        if home_config.exists():
            return cls.from_file(str(home_config))
        
        # Return default config
        return cls()
    
    def merge(self, other: 'ValidationConfig') -> 'ValidationConfig':
        """Merge another config into this one (other takes precedence)."""
        result = ValidationConfig()
        
        # Copy all fields from self
        for field_name in self.__dataclass_fields__:
            setattr(result, field_name, getattr(self, field_name))
        
        # Override with non-default values from other
        for field_name in other.__dataclass_fields__:
            other_value = getattr(other, field_name)
            default_value = self.__dataclass_fields__[field_name].default
            
            # Check if it's a factory default
            if self.__dataclass_fields__[field_name].default_factory != field:
                default_value = self.__dataclass_fields__[field_name].default_factory()
            
            # Override if not default
            if other_value != default_value:
                setattr(result, field_name, other_value)
        
        return result


class CustomValidators:
    """Registry for custom validation functions."""
    
    _validators: Dict[str, Callable] = {}
    
    @classmethod
    def register(cls, name: str):
        """Decorator to register a custom validator."""
        def decorator(func: Callable):
            cls._validators[name] = func
            return func
        return decorator
    
    @classmethod
    def get(cls, name: str) -> Optional[Callable]:
        """Get a custom validator by name."""
        return cls._validators.get(name)
    
    @classmethod
    def list_validators(cls) -> List[str]:
        """List all registered validator names."""
        return list(cls._validators.keys())


# Built-in custom validators

@CustomValidators.register("security_keywords_check")
def check_security_keywords(requirement: Dict[str, Any]) -> Optional[str]:
    """Check for security-related keywords requiring special attention."""
    security_keywords = [
        'password', 'encryption', 'authentication', 'authorization',
        'token', 'key', 'secret', 'credential', 'certificate',
        'vulnerability', 'exploit', 'injection', 'xss', 'csrf'
    ]
    
    text = requirement.get('text', '').lower()
    found_keywords = [kw for kw in security_keywords if kw in text]
    
    if found_keywords and 'security' not in requirement.get('categories', []):
        return f"Security keywords found ({', '.join(found_keywords)}) but requirement not marked with [security] category"
    
    return None


@CustomValidators.register("api_consistency_check")
def check_api_consistency(requirement: Dict[str, Any]) -> Optional[str]:
    """Check API requirements follow RESTful conventions."""
    text = requirement.get('text', '')
    
    # Check for REST verbs
    rest_verbs = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    api_patterns = [
        (r'endpoint', 'Endpoint requirements should specify HTTP method'),
        (r'API', 'API requirements should follow RESTful conventions'),
    ]
    
    for pattern, message in api_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            has_verb = any(verb in text for verb in rest_verbs)
            if not has_verb:
                return message
    
    return None


@CustomValidators.register("performance_requirements_check")
def check_performance_requirements(requirement: Dict[str, Any]) -> Optional[str]:
    """Check performance requirements have measurable criteria."""
    text = requirement.get('text', '').lower()
    
    performance_keywords = ['performance', 'response time', 'latency', 'throughput', 'load']
    has_performance = any(kw in text for kw in performance_keywords)
    
    if has_performance:
        # Check for measurable criteria - use regex for numeric patterns
        import re
        numeric_patterns = [
            r'\d+\s*ms', r'\d+\s*seconds?', r'\d+\s*req', r'\d+\s*%'
        ]
        text_patterns = [
            'less than', 'more than', 'at least', 'maximum', 'minimum'
        ]
        
        has_metrics = any(re.search(pattern, text) for pattern in numeric_patterns)
        has_metrics = has_metrics or any(pattern in text for pattern in text_patterns)
        
        if not has_metrics:
            return "Performance requirement lacks measurable criteria"
    
    return None


@CustomValidators.register("testability_check")
def check_testability(requirement: Dict[str, Any]) -> Optional[str]:
    """Check requirement is testable with clear pass/fail criteria."""
    text = requirement.get('text', '').lower()
    
    # Vague words that indicate poor testability
    vague_words = [
        'should', 'might', 'could', 'possibly', 'maybe',
        'appropriate', 'adequate', 'sufficient', 'reasonable',
        'user-friendly', 'intuitive', 'easy', 'simple'
    ]
    
    found_vague = [word for word in vague_words if word in text]
    
    if found_vague:
        return f"Requirement contains vague terms that reduce testability: {', '.join(found_vague)}"
    
    return None