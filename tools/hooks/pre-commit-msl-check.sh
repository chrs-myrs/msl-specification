#!/bin/bash
# Pre-commit hook script to validate MSL documents

# Function to check if a file is an MSL document
is_msl_doc() {
    local file="$1"
    
    # Check for YAML frontmatter with msl field
    if head -n 20 "$file" | grep -q "^msl:"; then
        return 0
    fi
    
    # Check for [MSL] marker in title
    if head -n 10 "$file" | grep -q "\[MSL\]"; then
        return 0
    fi
    
    # Check if it's in specs directory (likely MSL)
    if [[ "$file" == specs/*.md ]] || [[ "$file" == specs/**/*.md ]]; then
        return 0
    fi
    
    return 1
}

# Exit codes
SUCCESS=0
FAILURE=1

# Track if any MSL files failed
any_failures=0

# Process all staged .md files
for file in "$@"; do
    # Skip if not an MSL document
    if ! is_msl_doc "$file"; then
        continue
    fi
    
    echo "Validating MSL specification: $file"
    
    # Run the linter
    if ! ./tools/cli/msl-lint "$file"; then
        echo "❌ MSL validation failed for: $file"
        any_failures=1
    else
        echo "✅ MSL validation passed for: $file"
    fi
done

exit $any_failures