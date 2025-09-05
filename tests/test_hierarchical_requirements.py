#!/usr/bin/env python3
"""Test hierarchical requirements parsing and validation."""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'tools'))

from lib.parser import MSLParser
from lib.validator import MSLValidator, ValidationIssue


def test_basic_hierarchy():
    """Test parsing basic hierarchical requirements."""
    parser = MSLParser()
    
    content = """# Test Spec
## Requirements
- REQ-001: Authentication system
  - REQ-001.1: Login with email/password
  - REQ-001.2: OAuth integration
    - REQ-001.2.1: Google OAuth
    - REQ-001.2.2: GitHub OAuth
  - REQ-001.3: Session management
"""
    
    parsed = parser.parse_content(content)
    reqs = parsed["requirements"]
    
    # Check top-level requirement
    assert len(reqs) == 1
    assert reqs[0]["id"] == "REQ-001"
    assert reqs[0]["text"] == "Authentication system"
    assert len(reqs[0]["children"]) == 3
    
    # Check first-level children
    children = reqs[0]["children"]
    assert children[0]["id"] == "REQ-001.1"
    assert children[0]["text"] == "Login with email/password"
    assert children[1]["id"] == "REQ-001.2"
    assert children[1]["text"] == "OAuth integration"
    assert len(children[1]["children"]) == 2
    
    # Check second-level children
    oauth_children = children[1]["children"]
    assert oauth_children[0]["id"] == "REQ-001.2.1"
    assert oauth_children[0]["text"] == "Google OAuth"
    assert oauth_children[1]["id"] == "REQ-001.2.2"
    assert oauth_children[1]["text"] == "GitHub OAuth"
    


def test_auto_generated_ids():
    """Test automatic ID generation for sub-requirements."""
    parser = MSLParser()
    
    content = """# Test Spec
## Requirements
- REQ-001: Parent requirement
  - Sub-requirement without ID
  - Another sub-requirement
    - Nested sub-requirement
"""
    
    parsed = parser.parse_content(content)
    reqs = parsed["requirements"]
    
    # Check auto-generated IDs
    assert reqs[0]["children"][0]["id"] == "REQ-001.1"
    assert reqs[0]["children"][1]["id"] == "REQ-001.2"
    assert reqs[0]["children"][1]["children"][0]["id"] == "REQ-001.2.1"
    


def test_mixed_hierarchy():
    """Test mixed hierarchical and flat requirements."""
    parser = MSLParser()
    
    content = """# Test Spec
## Requirements
- REQ-001: First parent
  - REQ-001.1: First child
  - REQ-001.2: Second child
- REQ-002: Second parent (flat)
- REQ-003: Third parent
  - REQ-003.1: Child of third
    - REQ-003.1.1: Grandchild
"""
    
    parsed = parser.parse_content(content)
    reqs = parsed["requirements"]
    
    # Should have 3 top-level requirements
    assert len(reqs) == 3
    assert reqs[0]["id"] == "REQ-001"
    assert len(reqs[0]["children"]) == 2
    assert reqs[1]["id"] == "REQ-002"
    assert len(reqs[1]["children"]) == 0
    assert reqs[2]["id"] == "REQ-003"
    assert len(reqs[2]["children"]) == 1
    assert len(reqs[2]["children"][0]["children"]) == 1
    


def test_hierarchy_with_markers():
    """Test hierarchical requirements with composite markers."""
    parser = MSLParser()
    
    content = """# Test Spec
## Requirements
- REQ-001: [!|security] Authentication system
  - REQ-001.1: [stage:implementation|progress:60%] Login module
  - REQ-001.2: [blocked|depends:REQ-001.1] OAuth integration
    - REQ-001.2.1: [@team-backend] Google OAuth
    - REQ-001.2.2: [gap:test] GitHub OAuth
"""
    
    parsed = parser.parse_content(content)
    reqs = parsed["requirements"]
    
    # Check markers are preserved in hierarchy
    assert reqs[0]["priority"] == "critical"
    assert "security" in reqs[0]["categories"]
    
    assert reqs[0]["children"][0]["markers"]["stage"] == "implementation"
    assert reqs[0]["children"][0]["metrics"]["progress"] == "60%"
    
    assert reqs[0]["children"][1]["status"] == "blocked"
    assert reqs[0]["children"][1]["markers"]["depends"] == "REQ-001.1"
    
    assert reqs[0]["children"][1]["children"][0]["assignee"] == "team-backend"
    assert reqs[0]["children"][1]["children"][1]["markers"]["gap"] == "test"
    


def test_depth_validation():
    """Test validation of hierarchy depth limits."""
    parser = MSLParser()
    validator = MSLValidator(strict=True)
    
    content = """# Test Spec
## Requirements
- REQ-001: Level 0
  - REQ-001.1: Level 1
    - REQ-001.1.1: Level 2
      - REQ-001.1.1.1: Level 3
        - REQ-001.1.1.1.1: Level 4 (too deep)
          - REQ-001.1.1.1.1.1: Level 5 (way too deep)
"""
    
    parsed = parser.parse_content(content)
    issues = validator.validate(parsed)
    
    # Should have warnings about depth
    depth_warnings = [i for i in issues if "depth" in i.message.lower()]
    assert len(depth_warnings) > 0
    


def test_id_consistency_validation():
    """Test validation of parent-child ID consistency."""
    parser = MSLParser()
    validator = MSLValidator(strict=True)
    
    content = """# Test Spec
## Requirements
- REQ-001: Parent
  - REQ-002.1: Wrong parent ID prefix
  - REQ-001.1: Correct child
  - REQ-001.1: Duplicate child ID
"""
    
    parsed = parser.parse_content(content)
    issues = validator.validate(parsed)
    
    # Should have warnings about ID consistency
    issue_messages = [i.message for i in issues]
    assert any("doesn't follow parent ID pattern" in msg for msg in issue_messages)
    assert any("Duplicate" in msg for msg in issue_messages)
    


def test_indentation_parsing():
    """Test correct parsing of indentation levels."""
    parser = MSLParser()
    
    # Using explicit spaces for clarity
    content = """# Test Spec
## Requirements
- REQ-001: No indent (depth 0)
  - REQ-001.1: Two spaces (depth 1)
    - REQ-001.1.1: Four spaces (depth 2)
      - REQ-001.1.1.1: Six spaces (depth 3)
  - REQ-001.2: Back to two spaces (depth 1)
- REQ-002: Back to no indent (depth 0)
"""
    
    parsed = parser.parse_content(content)
    reqs = parsed["requirements"]
    
    # Check depths are correctly parsed
    assert reqs[0]["depth"] == 0
    assert reqs[0]["children"][0]["depth"] == 1
    assert reqs[0]["children"][0]["children"][0]["depth"] == 2
    assert reqs[0]["children"][0]["children"][0]["children"][0]["depth"] == 3
    assert reqs[0]["children"][1]["depth"] == 1
    assert reqs[1]["depth"] == 0
    


def test_complex_real_world_hierarchy():
    """Test a complex real-world hierarchical specification."""
    parser = MSLParser()
    
    content = """# E-Commerce System
## Requirements
- REQ-001: [!|mvp] User Management System
  - REQ-001.1: [stage:implementation|progress:80%] User Registration
    - REQ-001.1.1: Email validation
    - REQ-001.1.2: Password strength requirements
    - REQ-001.1.3: CAPTCHA integration
  - REQ-001.2: [stage:testing|coverage:75%] User Authentication
    - REQ-001.2.1: [@backend] JWT token generation
    - REQ-001.2.2: [@backend] Session management
    - REQ-001.2.3: [@frontend] Remember me functionality
  - REQ-001.3: [gap:doc] User Profile Management
    - REQ-001.3.1: Profile editing
    - REQ-001.3.2: Avatar upload
    - REQ-001.3.3: Privacy settings

- REQ-002: [!|performance] Product Catalog
  - REQ-002.1: Product Search
    - REQ-002.1.1: [estimate:3d] Full-text search
    - REQ-002.1.2: [estimate:2d] Filter by category
    - REQ-002.1.3: [estimate:1d] Sort by price/rating
  - REQ-002.2: [depends:REQ-002.1] Product Display
    - REQ-002.2.1: Image gallery
    - REQ-002.2.2: Product specifications
    - REQ-002.2.3: Customer reviews

- REQ-003: [blocked|external|vendor:stripe] Payment Processing
  - REQ-003.1: [stage:design] Cart Management
  - REQ-003.2: [stage:design] Checkout Flow
  - REQ-003.3: [gap:implementation] Order Confirmation
"""
    
    parsed = parser.parse_content(content)
    reqs = parsed["requirements"]
    
    # Verify structure
    assert len(reqs) == 3
    assert reqs[0]["id"] == "REQ-001"
    assert len(reqs[0]["children"]) == 3
    assert len(reqs[0]["children"][0]["children"]) == 3
    assert len(reqs[0]["children"][1]["children"]) == 3
    assert len(reqs[0]["children"][2]["children"]) == 3
    
    assert reqs[1]["id"] == "REQ-002"
    assert len(reqs[1]["children"]) == 2
    assert len(reqs[1]["children"][0]["children"]) == 3
    assert len(reqs[1]["children"][1]["children"]) == 3
    
    assert reqs[2]["id"] == "REQ-003"
    assert len(reqs[2]["children"]) == 3
    
    # Verify markers are preserved
    assert reqs[0]["priority"] == "critical"
    assert "mvp" in reqs[0]["markers"]
    assert reqs[0]["children"][0]["metrics"]["progress"] == "80%"
    assert reqs[2]["status"] == "blocked"
    assert reqs[2]["markers"]["vendor"] == "stripe"
    


def test_flat_list_still_works():
    """Test that flat requirement lists still work correctly."""
    parser = MSLParser()
    
    content = """# Test Spec
## Requirements
- REQ-001: First requirement
- REQ-002: Second requirement
- REQ-003: Third requirement
- REQ-004: [!] Fourth requirement with marker
"""
    
    parsed = parser.parse_content(content)
    reqs = parsed["requirements"]
    
    # All should be top-level
    assert len(reqs) == 4
    for req in reqs:
        assert req["depth"] == 0
        assert len(req["children"]) == 0
    
    assert reqs[3]["priority"] == "critical"
    


# Tests are now run via pytest - no main block needed
