#!/bin/bash

VENV_DIR=".venv"

function setup_venv() {
    if [ ! -d "$VENV_DIR" ]; then
        echo "Creating virtual environment..."
        python3 -m venv "$VENV_DIR"
        echo "Virtual environment created at $VENV_DIR."
    fi

    echo "Activating virtual environment..."
    source "$VENV_DIR/bin/activate"
    echo "Installing dependencies..."
    pip install --upgrade pip
    pip install flake8 pytest pytest-cov black isort
}

function clean() {
    echo "Cleaning up virtual environment and temporary files..."
    if [ -d "$VENV_DIR" ]; then
        rm -rf "$VENV_DIR"
        echo "Removed virtual environment directory: $VENV_DIR"
    fi

    find . -type d -name "__pycache__" -exec rm -rf {} +
    find . -type d -name "*.egg-info" -exec rm -rf {} +
    find . -type f -name "*.pyc" -delete
    find . -type d -name ".pytest_cache" -exec rm -rf {} +

    echo "Cleanup completed!"
}

function lint() {
    echo "Running linting with flake8..."
    flake8 src --max-line-length=88
    FL_STATUS=$?

    if [ $FL_STATUS -eq 0 ]; then
        echo "Linting passed successfully! No issues found in the code."
    else
        echo "Linting failed with exit code $FL_STATUS. Please fix the issues above." >&2
        exit $FL_STATUS
    fi
}

function test() {
    echo "Running tests with pytest..."
    pytest tests --cov=src
    PYTEST_STATUS=$?

    if [ $PYTEST_STATUS -eq 0 ]; then
        echo "All tests passed successfully!"
    else
        echo "Some tests failed with exit code $PYTEST_STATUS. Please review the output above." >&2
        exit $PYTEST_STATUS
    fi
}

function format() {
    echo "Running formatting with black and isort..."
    black src tests
    isort src tests
    echo "Formatting completed!"
}

case "$1" in
setup)
    setup_venv
    ;;
lint)
    setup_venv
    lint
    clean
    ;;
test)
    setup_venv
    test
    clean
    ;;
format)
    setup_venv
    format
    clean
    ;;
clean)
    clean
    ;;
*)
    echo "Usage: $0 {setup|lint|test|format|clean}"
    exit 1
    ;;
esac
