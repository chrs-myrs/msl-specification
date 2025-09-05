#!/usr/bin/env python3
"""Clean up test files for pytest migration."""

import re
from pathlib import Path


def cleanup_test_file(filepath):
    """Remove print statements and main blocks from test file."""
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    new_lines = []
    skip_main_block = False
    
    for i, line in enumerate(lines):
        # Skip main block
        if 'if __name__ == "__main__":' in line:
            skip_main_block = True
            new_lines.append("# Tests are now run via pytest - no main block needed\n")
            continue
        
        if skip_main_block:
            # Keep skipping until we find a non-indented line
            if line.strip() and not line.startswith(' ') and not line.startswith('\t'):
                skip_main_block = False
            else:
                continue
        
        # Remove print statements about test passing
        if 'print(' in line and ('✓' in line or '✅' in line or 'test passed' in line.lower() or '=' * 10 in line):
            continue
        
        # Keep the line
        new_lines.append(line)
    
    # Write back
    with open(filepath, 'w') as f:
        f.writelines(new_lines)
    
    print(f"Cleaned up {filepath.name}")


def main():
    """Clean up all test files."""
    test_dir = Path(__file__).parent.parent / 'tests'
    
    test_files = [
        'test_composite_markers.py',
        'test_hierarchical_requirements.py', 
        'test_validation_config.py',
        'test_code_links.py'
    ]
    
    for test_file in test_files:
        filepath = test_dir / test_file
        if filepath.exists():
            cleanup_test_file(filepath)
    
    print("\nAll test files cleaned up for pytest!")
    print("You can now run: pytest")


if __name__ == "__main__":
    main()