#!/usr/bin/env python3
"""Test composite markers parsing and validation."""

import pytest


@pytest.mark.parser
def test_simple_composite_markers(msl_parser):
    """Test parsing simple composite markers."""
    parser = msl_parser
    
    content = """# Test Spec
## Requirements
- REQ-001: [!|security|@team-security] Critical security fix
- REQ-002: [blocked|external|vendor:acme] Third-party dependency
- REQ-003: [mvp|tested|deployed] Core feature
"""
    
    parsed = parser.parse_content(content)
    reqs = parsed["requirements"]
    
    # Test first requirement
    assert reqs[0]["priority"] == "critical"
    assert "security" in reqs[0]["categories"]
    assert reqs[0]["assignee"] == "team-security"
    
    # Test second requirement  
    assert reqs[1]["status"] == "blocked"
    assert reqs[1]["markers"]["external"] == True
    assert reqs[1]["markers"]["vendor"] == "acme"
    
    # Test third requirement
    assert reqs[2]["markers"]["mvp"] == True
    assert reqs[2]["markers"]["tested"] == True
    assert reqs[2]["markers"]["deployed"] == True


def test_metrics_markers(msl_parser):
    """Test parsing metrics in composite markers."""
    parser = msl_parser
    
    content = """# Test Spec
## Requirements
- REQ-001: [stage:implementation|progress:60%] Core module
- REQ-002: [stage:testing|coverage:85%|confidence:high] Validation
- REQ-003: [estimate:5d|actual:7d|variance:+2d] Complex task
"""
    
    parsed = parser.parse_content(content)
    reqs = parsed["requirements"]
    
    # Test progress tracking
    assert reqs[0]["markers"]["stage"] == "implementation"
    assert reqs[0]["metrics"]["progress"] == "60%"
    
    # Test coverage and confidence
    assert reqs[1]["markers"]["stage"] == "testing"
    assert reqs[1]["metrics"]["coverage"] == "85%"
    assert reqs[1]["metrics"]["confidence"] == "high"
    
    # Test estimates
    assert reqs[2]["metrics"]["estimate"] == "5d"
    assert reqs[2]["metrics"]["actual"] == "7d"
    assert reqs[2]["metrics"]["variance"] == "+2d"
    


def test_priority_status_combinations(msl_parser):
    """Test various priority and status combinations."""
    parser = msl_parser
    
    content = """# Test Spec
## Requirements
- REQ-001: [!!|blocked] Urgent but blocked
- REQ-002: [~|review] Low priority in review
- REQ-003: [!|testing|sprint:15] Critical in testing
"""
    
    parsed = parser.parse_content(content)
    reqs = parsed["requirements"]
    
    assert reqs[0]["priority"] == "urgent"
    assert reqs[0]["status"] == "blocked"
    
    assert reqs[1]["priority"] == "low"
    assert reqs[1]["status"] == "review"
    
    assert reqs[2]["priority"] == "critical"
    assert reqs[2]["status"] == "testing"
    assert reqs[2]["markers"]["sprint"] == "15"
    


def test_dependency_markers(msl_parser):
    """Test dependency relationship markers."""
    parser = msl_parser
    
    content = """# Test Spec
## Requirements
- REQ-001: Core authentication
- REQ-002: [depends:REQ-001] User profiles
- REQ-003: [blocks:REQ-004,REQ-005] Database migration
- REQ-004: [after:REQ-003|parallel:REQ-005] UI component
"""
    
    parsed = parser.parse_content(content)
    reqs = parsed["requirements"]
    
    # Debug: print what we actually got
    # print("REQ-002 markers:", reqs[1].get("markers", {}))
    
    assert "depends" in reqs[1]["markers"] and reqs[1]["markers"]["depends"] == "REQ-001"
    assert "blocks" in reqs[2]["markers"] and reqs[2]["markers"]["blocks"] == "REQ-004,REQ-005"
    assert "after" in reqs[3]["markers"] and reqs[3]["markers"]["after"] == "REQ-003"
    assert "parallel" in reqs[3]["markers"] and reqs[3]["markers"]["parallel"] == "REQ-005"
    


def test_validation_of_composite_markers(msl_parser, msl_validator):
    """Test validation rules for composite markers."""
    parser = msl_parser
    from lib.validator import MSLValidator
    validator = MSLValidator(strict=True)
    
    content = """# Test Spec
## Requirements
- REQ-001: [progress:150%] Invalid progress
- REQ-002: [coverage:85%] Valid coverage
- REQ-003: [confidence:unknown] Invalid confidence
- REQ-004: [stage:planning] Invalid stage
- REQ-005: [gap:unknown] Invalid gap type
"""
    
    parsed = parser.parse_content(content)
    issues = validator.validate(parsed)
    
    # Check for expected validation issues
    issue_messages = [issue.message for issue in issues]
    
    assert any("should be between 0-100%" in msg for msg in issue_messages)
    assert any("Invalid confidence" in msg for msg in issue_messages)
    assert any("Invalid stage" in msg for msg in issue_messages)
    assert any("Invalid gap type" in msg for msg in issue_messages)
    


def test_backward_compatibility(msl_parser):
    """Test that simple markers still work."""
    parser = msl_parser
    
    content = """# Test Spec
## Requirements
- REQ-001: [!] Critical requirement
- REQ-002: [x] Completed requirement
- REQ-003: [@alice] Assigned requirement
- REQ-004: Normal requirement without markers
"""
    
    parsed = parser.parse_content(content)
    reqs = parsed["requirements"]
    
    assert reqs[0]["priority"] == "critical"
    assert reqs[1]["status"] == "complete"
    assert reqs[2]["assignee"] == "alice"
    assert reqs[3]["priority"] == "medium"  # default
    


def test_complex_real_world_example(msl_parser):
    """Test a complex real-world scenario."""
    parser = msl_parser
    
    content = """# Payment System
## Requirements
- REQ-001: [!|security|stage:implementation|progress:75%] Payment encryption
- REQ-002: [mvp|depends:REQ-001|estimate:3d|@team-backend] Payment processing
- REQ-003: [stage:testing|coverage:92%|sprint:15|milestone:v1.0] Integration tests
- REQ-004: [blocked|external|vendor:stripe|eta:2025-Q1] Stripe webhook integration
- REQ-005: [gap:doc|review:pending|@alice] API documentation
"""
    
    parsed = parser.parse_content(content)
    reqs = parsed["requirements"]
    
    # Payment encryption
    assert reqs[0]["priority"] == "critical"
    assert "security" in reqs[0]["categories"]
    assert reqs[0]["markers"]["stage"] == "implementation"
    assert reqs[0]["metrics"]["progress"] == "75%"
    
    # Payment processing
    assert reqs[1]["markers"]["mvp"] == True
    assert reqs[1]["markers"]["depends"] == "REQ-001"
    assert reqs[1]["metrics"]["estimate"] == "3d"
    assert reqs[1]["assignee"] == "team-backend"
    
    # Integration tests
    assert reqs[2]["markers"]["stage"] == "testing"
    assert reqs[2]["metrics"]["coverage"] == "92%"
    assert reqs[2]["markers"]["sprint"] == "15"
    assert reqs[2]["markers"]["milestone"] == "v1.0"
    
    # Stripe webhook
    assert reqs[3]["status"] == "blocked"
    assert reqs[3]["markers"]["external"] == True
    assert reqs[3]["markers"]["vendor"] == "stripe"
    assert reqs[3]["markers"]["eta"] == "2025-Q1"
    
    # API documentation
    assert reqs[4]["markers"]["gap"] == "doc"
    assert reqs[4]["markers"]["review"] == "pending"
    assert reqs[4]["assignee"] == "alice"
    


# Tests are now run via pytest - no main block needed