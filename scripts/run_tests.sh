#!/bin/bash
# MSL Test Runner Script

echo "MSL Test Suite"
echo "=============="

# Check if pytest is installed
if ! command -v pytest &> /dev/null; then
    echo "❌ pytest is not installed"
    echo "Please install: pip install -r requirements-dev.txt"
    exit 1
fi

# Run pytest with appropriate options
echo "Running tests..."
echo ""

# Run tests with summary output
pytest tests/ \
    -v \
    --tb=short \
    --color=yes \
    -q

# Capture exit code
TEST_RESULT=$?

echo ""
echo "=============="

if [ $TEST_RESULT -eq 0 ]; then
    echo "✅ All tests passed!"
else
    echo "❌ Some tests failed"
    echo "Run 'pytest tests/ -v' for more details"
fi

exit $TEST_RESULT