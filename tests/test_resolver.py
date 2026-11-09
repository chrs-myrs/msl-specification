"""Tests for locating parents during inheritance resolution (msl-tools REQ-504, REQ-506, REQ-507)."""

import pytest

from lib.resolver import MSLResolver


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


PARENT = """---
msl: L1
id: base-spec
---

# Base [MSL]

## Requirements

- REQ-001: Parent requirement
"""

CHILD = """---
msl: L1
id: child-spec
extends: base-spec
---

# Child [MSL]

## Requirements

- REQ-002: [NEW] Child requirement
"""


def requirement_ids(spec):
    return {req.get("id") for req in spec.get("requirements", [])}


def test_parent_found_by_frontmatter_id_in_nested_folder(temp_dir):
    write(temp_dir / "specs" / "interfaces" / "renamed-base.spec.md", PARENT)
    write(temp_dir / "specs" / "features" / "child.spec.md", CHILD)

    resolved = MSLResolver(str(temp_dir)).resolve("child-spec")

    assert {"REQ-001", "REQ-002"} <= requirement_ids(resolved)


def test_frontmatter_id_wins_over_file_name(temp_dir):
    # A pointer left at the old path shares the id's file name but declares no id
    write(temp_dir / "specs" / "base-spec.md", "# Base (moved)\n\nSee interfaces/.\n")
    write(temp_dir / "specs" / "interfaces" / "base-spec.spec.md", PARENT)
    write(temp_dir / "specs" / "features" / "child.spec.md", CHILD)

    resolved = MSLResolver(str(temp_dir)).resolve("child-spec")

    assert "REQ-001" in requirement_ids(resolved)


def test_parent_without_frontmatter_found_by_file_name(temp_dir):
    write(temp_dir / "specs" / "base-spec.spec.md", "# Base [MSL]\n\n## Requirements\n\n- REQ-001: Parent requirement\n")
    write(temp_dir / "specs" / "features" / "child.spec.md", CHILD)

    resolved = MSLResolver(str(temp_dir)).resolve("child-spec")

    assert "REQ-001" in requirement_ids(resolved)


def test_missing_parent_names_the_id(temp_dir):
    write(temp_dir / "specs" / "features" / "child.spec.md", CHILD)

    with pytest.raises(FileNotFoundError, match="base-spec"):
        MSLResolver(str(temp_dir)).resolve("child-spec")
