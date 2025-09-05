#!/usr/bin/env python3
"""Test bidirectional code links functionality."""

import sys
import os
import tempfile
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'tools'))

from lib.parser import MSLParser
from lib.validator import MSLValidator
from lib.code_scanner import CodeScanner


def test_parse_bidirectional_links():
    """Test parsing of bidirectional code link markers."""
    parser = MSLParser()
    
    content = """# Test Spec
## Requirements
- REQ-001: [↔ src/auth.js:45-67] Authentication implementation
- REQ-002: [<-> lib/validator.py:100] Validation logic
- REQ-003: [→ app/main.java:25] Forward link only
- REQ-004: [-> tests/test.js] Forward link alt syntax
- REQ-005: [← config.yaml:10-20] Backward link only
- REQ-006: [<- deploy.sh:5] Backward link alt syntax
"""
    
    parsed = parser.parse_content(content)
    reqs = parsed['requirements']
    
    # Test bidirectional link parsing
    assert 'code_links' in reqs[0]
    assert reqs[0]['code_links'][0]['file'] == 'src/auth.js'
    assert reqs[0]['code_links'][0]['start_line'] == '45'
    assert reqs[0]['code_links'][0]['end_line'] == '67'
    assert reqs[0]['code_links'][0]['direction'] == 'bidirectional'
    
    # Test alt bidirectional syntax
    assert reqs[1]['code_links'][0]['file'] == 'lib/validator.py'
    assert reqs[1]['code_links'][0]['line'] == '100'
    assert reqs[1]['code_links'][0]['direction'] == 'bidirectional'
    
    # Test forward link
    assert reqs[2]['code_links'][0]['file'] == 'app/main.java'
    assert reqs[2]['code_links'][0]['line'] == '25'
    assert reqs[2]['code_links'][0]['direction'] == 'forward'
    
    # Test forward alt syntax
    assert reqs[3]['code_links'][0]['file'] == 'tests/test.js'
    assert reqs[3]['code_links'][0]['direction'] == 'forward'
    
    # Test backward link
    assert reqs[4]['code_links'][0]['file'] == 'config.yaml'
    assert reqs[4]['code_links'][0]['start_line'] == '10'
    assert reqs[4]['code_links'][0]['end_line'] == '20'
    assert reqs[4]['code_links'][0]['direction'] == 'backward'
    
    # Test backward alt syntax
    assert reqs[5]['code_links'][0]['file'] == 'deploy.sh'
    assert reqs[5]['code_links'][0]['line'] == '5'
    assert reqs[5]['code_links'][0]['direction'] == 'backward'
    
    print("✓ Parse bidirectional links test passed")


def test_composite_markers_with_code_links():
    """Test combining code links with other composite markers."""
    parser = MSLParser()
    
    content = """# Test Spec
## Requirements
- REQ-001: [!|security|↔ auth/login.py:50-100] Secure login implementation
- REQ-002: [stage:implementation|progress:75%|→ src/api.js] API in progress
- REQ-003: [@alice|← tests/integration.py:200|gap:doc] Needs documentation
"""
    
    parsed = parser.parse_content(content)
    reqs = parsed['requirements']
    
    # First requirement: priority + security + code link
    assert reqs[0]['priority'] == 'critical'  # '!' means critical priority
    assert 'security' in reqs[0]['categories']
    assert reqs[0]['code_links'][0]['file'] == 'auth/login.py'
    assert reqs[0]['code_links'][0]['direction'] == 'bidirectional'
    
    # Second requirement: stage + progress + code link
    assert reqs[1]['markers']['stage'] == 'implementation'
    assert reqs[1]['metrics']['progress'] == '75%'
    assert reqs[1]['code_links'][0]['file'] == 'src/api.js'
    assert reqs[1]['code_links'][0]['direction'] == 'forward'
    
    # Third requirement: assignee + code link + gap
    assert reqs[2]['assignee'] == 'alice'
    assert reqs[2]['code_links'][0]['file'] == 'tests/integration.py'
    assert reqs[2]['code_links'][0]['direction'] == 'backward'
    assert reqs[2]['markers']['gap'] == 'doc'
    
    print("✓ Composite markers with code links test passed")


def test_code_link_validation():
    """Test validation of code links."""
    parser = MSLParser()
    validator = MSLValidator()
    
    content = """# Test Spec
## Requirements
- REQ-001: [↔ src/auth.js:45-67] Valid range link
- REQ-002: [→ lib/test.py:abc] Invalid line number
- REQ-003: [← config.yaml:100-50] Invalid range (end before start)
- REQ-004: [↔] Missing file path
- REQ-005: [→ :25] Missing file name
"""
    
    parsed = parser.parse_content(content)
    issues = validator.validate(parsed)
    
    # Check for expected validation issues
    issue_messages = [issue.message for issue in issues]
    
    assert any("Invalid line number" in msg for msg in issue_messages)
    assert any("End line before start" in msg for msg in issue_messages)
    assert any("Empty file path" in msg for msg in issue_messages)
    
    print("✓ Code link validation test passed")


def test_code_scanner_python():
    """Test scanning Python files for MSL references."""
    scanner = CodeScanner()
    
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a test Python file
        test_file = Path(tmpdir) / "test.py"
        test_file.write_text("""
# MSL: REQ-001
def authenticate(username, password):
    '''
    Authenticate user
    MSL: REQ-002
    '''
    pass

# @implements REQ-003
def validate_input(data):
    # [MSL: REQ-004]
    return True
""")
        
        refs = scanner.scan_file(str(test_file))
        
        assert len(refs) == 4
        assert refs[0]['requirement_id'] == 'REQ-001'
        assert refs[0]['line'] == 2
        assert refs[1]['requirement_id'] == 'REQ-002'
        assert refs[2]['requirement_id'] == 'REQ-003'
        assert refs[3]['requirement_id'] == 'REQ-004'
    
    print("✓ Code scanner Python test passed")


def test_code_scanner_javascript():
    """Test scanning JavaScript files for MSL references."""
    scanner = CodeScanner()
    
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a test JavaScript file
        test_file = Path(tmpdir) / "test.js"
        test_file.write_text("""
// MSL: REQ-101
function login(email, password) {
    /* 
     * Authentication logic
     * MSL: REQ-102
     */
    return true;
}

// @requirement REQ-103
const validate = (input) => {
    // [MSL: REQ-104]
    return input.length > 0;
};
""")
        
        refs = scanner.scan_file(str(test_file))
        
        assert len(refs) == 4
        assert refs[0]['requirement_id'] == 'REQ-101'
        assert refs[1]['requirement_id'] == 'REQ-102'
        assert refs[2]['requirement_id'] == 'REQ-103'
        assert refs[3]['requirement_id'] == 'REQ-104'
    
    print("✓ Code scanner JavaScript test passed")


def test_reverse_link_generation():
    """Test generating reverse links from code to spec."""
    scanner = CodeScanner()
    
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        
        # Create spec file
        spec_file = tmpdir / "spec.md"
        spec_file.write_text("""# Auth Spec
## Requirements
- REQ-001: User authentication
- REQ-002: Password validation
- REQ-003: Session management
""")
        
        # Create code files with references
        src_dir = tmpdir / "src"
        src_dir.mkdir()
        
        (src_dir / "auth.py").write_text("""
# MSL: REQ-001
def authenticate(user, password):
    # MSL: REQ-002
    if validate_password(password):
        return create_session(user)
    return None

# MSL: REQ-003
def create_session(user):
    return {"user": user, "token": "abc123"}
""")
        
        (src_dir / "validator.py").write_text("""
# MSL: REQ-002
def validate_password(password):
    return len(password) >= 8
""")
        
        # Generate reverse links
        reverse_links = scanner.generate_reverse_links(str(spec_file), str(tmpdir))
        
        assert 'REQ-001' in reverse_links
        assert 'REQ-002' in reverse_links
        assert 'REQ-003' in reverse_links
        
        assert len(reverse_links['REQ-001']['implementations']) == 1
        assert len(reverse_links['REQ-002']['implementations']) == 2  # Referenced in two files
        assert len(reverse_links['REQ-003']['implementations']) == 1
    
    print("✓ Reverse link generation test passed")


def test_bidirectional_verification():
    """Test verification of bidirectional links."""
    parser = MSLParser()
    scanner = CodeScanner()
    
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        
        # Create code file
        src_dir = tmpdir / "src"
        src_dir.mkdir()
        (src_dir / "auth.py").write_text("""
# MSL: REQ-001
def login():
    pass

# MSL: REQ-002
def logout():
    pass
""")
        
        # Create spec with links
        spec_file = tmpdir / "spec.md"
        spec_file.write_text("""# Auth Spec
## Requirements
- REQ-001: [↔ src/auth.py:2] Login function
- REQ-002: [→ src/auth.py:6] Logout function
- REQ-003: Unlinked requirement
- REQ-004: [← src/missing.py] Broken link
""")
        
        # Change to temp directory for relative path resolution
        original_cwd = os.getcwd()
        os.chdir(tmpdir)
        
        try:
            # Verify links
            results = scanner.verify_bidirectional_links(str(spec_file), str(tmpdir))
            
            assert results['total_requirements'] == 4
            assert results['linked_requirements'] == 3
            assert 'REQ-003' in results['unlinked_requirements']
            assert len(results['broken_links']) == 1
            assert results['broken_links'][0]['requirement'] == 'REQ-004'
        finally:
            os.chdir(original_cwd)
    
    print("✓ Bidirectional verification test passed")


def test_hierarchical_requirements_with_code_links():
    """Test code links in hierarchical requirements."""
    parser = MSLParser()
    
    content = """# Test Spec
## Requirements
- REQ-001: [↔ src/auth.py] Authentication system
  - REQ-001.1: [→ src/auth.py:10-30] Login function
  - REQ-001.2: [→ src/auth.py:35-50] Logout function
    - REQ-001.2.1: [← tests/auth_test.py:100] Session cleanup
"""
    
    parsed = parser.parse_content(content)
    reqs = parsed['requirements']
    
    # Parent has general link to file
    assert reqs[0]['code_links'][0]['file'] == 'src/auth.py'
    assert 'line' not in reqs[0]['code_links'][0]
    
    # Children have specific line ranges
    children = reqs[0]['children']
    assert children[0]['code_links'][0]['start_line'] == '10'
    assert children[0]['code_links'][0]['end_line'] == '30'
    
    assert children[1]['code_links'][0]['start_line'] == '35'
    assert children[1]['code_links'][0]['end_line'] == '50'
    
    # Grandchild has backward link
    grandchild = children[1]['children'][0]
    assert grandchild['code_links'][0]['file'] == 'tests/auth_test.py'
    assert grandchild['code_links'][0]['direction'] == 'backward'
    
    print("✓ Hierarchical requirements with code links test passed")


if __name__ == "__main__":
    print("Running code links tests...")
    print("=" * 50)
    
    test_parse_bidirectional_links()
    test_composite_markers_with_code_links()
    test_code_link_validation()
    test_code_scanner_python()
    test_code_scanner_javascript()
    test_reverse_link_generation()
    test_bidirectional_verification()
    test_hierarchical_requirements_with_code_links()
    
    print("=" * 50)
    print("✅ All code links tests passed!")