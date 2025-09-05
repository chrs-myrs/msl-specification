---
msl: L1
id: cleanup-tests-script
title: Test Cleanup Script Specification
status: active
---

# Test Cleanup Script [MSL]

## Overview

This specification defines the cleanup script that prepares existing test files for pytest migration by removing standalone execution code and print statements.

## Requirements

### File Processing

- REQ-CLEANUP-001: Script must process all test files in the tests/ directory
- REQ-CLEANUP-002: Script must identify and remove `if __name__ == "__main__"` blocks
- REQ-CLEANUP-003: Script must preserve all test functions and their logic
- REQ-CLEANUP-004: Script must maintain file structure and imports

### Content Cleanup

- REQ-CLEANUP-010: Script must remove print statements used for test status output
- REQ-CLEANUP-011: Script must identify print statements by presence of success indicators (✓, ✅, "test passed")
- REQ-CLEANUP-012: Script must remove divider lines used in manual test output
- REQ-CLEANUP-013: Script must add comment indicating tests are now run via pytest

### File Handling

- REQ-CLEANUP-020: Script must read and write files safely with proper encoding
- REQ-CLEANUP-021: Script must preserve line endings and indentation
- REQ-CLEANUP-022: Script must process specific test files: test_composite_markers.py, test_hierarchical_requirements.py, test_validation_config.py, test_code_links.py
- REQ-CLEANUP-023: Script must report which files were processed

### User Feedback

- REQ-CLEANUP-030: Script must print status for each file processed
- REQ-CLEANUP-031: Script must provide final summary message
- REQ-CLEANUP-032: Script must indicate next steps for running tests

## Non-Requirements

- Script does not need to backup files (version control handles this)
- Script does not need to validate Python syntax after cleanup
- Script does not need to be idempotent (one-time migration)