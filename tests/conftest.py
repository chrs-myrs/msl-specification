"""Pytest configuration and shared fixtures for MSL tests."""

import sys
import os
import tempfile
import shutil
from pathlib import Path
import pytest

# Add tools directory to path so tests can import MSL modules
sys.path.insert(0, str(Path(__file__).parent.parent / 'tools'))


@pytest.fixture
def msl_parser():
    """Provide an MSL parser instance."""
    from lib.parser import MSLParser
    return MSLParser()


@pytest.fixture
def msl_validator():
    """Provide an MSL validator instance."""
    from lib.validator import MSLValidator
    return MSLValidator()


@pytest.fixture
def temp_dir():
    """Create a temporary directory for test files."""
    temp_path = tempfile.mkdtemp()
    yield Path(temp_path)
    # Cleanup after test
    shutil.rmtree(temp_path, ignore_errors=True)


@pytest.fixture
def sample_msl_content():
    """Provide sample MSL content for testing."""
    return """---
msl: L1
id: test-spec
---

# Test Specification [MSL]

## Requirements

- REQ-001: Basic requirement
- REQ-002: [!] High priority requirement
- REQ-003: [@alice] Assigned requirement
"""


@pytest.fixture
def code_scanner():
    """Provide a code scanner instance."""
    from lib.code_scanner import CodeScanner
    return CodeScanner()


# Pytest configuration
def pytest_configure(config):
    """Configure custom pytest markers."""
    config.addinivalue_line(
        "markers", "unit: Unit tests for individual functions"
    )
    config.addinivalue_line(
        "markers", "integration: Integration tests for components"
    )
    config.addinivalue_line(
        "markers", "parser: Parser-specific tests"
    )
    config.addinivalue_line(
        "markers", "validator: Validator-specific tests"
    )