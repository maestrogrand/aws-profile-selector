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

function release() {
    if [[ -z "${GITHUB_TOKEN}" || -z "${GITHUB_REPO}" ]]; then
        echo "Error: GITHUB_TOKEN and GITHUB_REPO environment variables must be set."
        exit 1
    fi

    VERSION_LINE=$(grep '__version__' src/version.py)
    VERSION=$(echo $VERSION_LINE | sed -E "s/__version__ = \"(.*)\"/\1/")
    echo "Current version: $VERSION"
    IFS='.' read -ra VERSION_PARTS <<<"$VERSION"

    MAJOR=${VERSION_PARTS[0]}
    MINOR=${VERSION_PARTS[1]}
    PATCH=${VERSION_PARTS[2]}

    PS3='Enter which part to increment (1 for MAJOR, 2 for MINOR, 3 for PATCH): '
    options=("MAJOR" "MINOR" "PATCH")
    select opt in "${options[@]}"; do
        case $REPLY in
        1)
            echo "Incrementing MAJOR version from $VERSION"
            MAJOR=$((MAJOR + 1))
            MINOR=0
            PATCH=0
            break
            ;;
        2)
            echo "Incrementing MINOR version from $VERSION"
            MINOR=$((MINOR + 1))
            PATCH=0
            break
            ;;
        3)
            echo "Incrementing PATCH version from $VERSION"
            PATCH=$((PATCH + 1))
            break
            ;;
        *)
            echo "Invalid option. Please select 1, 2, or 3."
            ;;
        esac
    done

    NEW_VERSION="$MAJOR.$MINOR.$PATCH"
    echo "New version: $NEW_VERSION"

    # Update version in src/version.py
    sed -i '' -e "s/__version__ = \".*\"/__version__ = \"$NEW_VERSION\"/" src/version.py
    echo "Updated version in src/version.py"

    # Commit and push changes
    echo "Enter commit message:"
    read commit_message
    git add .
    git commit -m "$commit_message"
    git push origin $(git rev-parse --abbrev-ref HEAD)

    echo "Version $NEW_VERSION released and changes pushed!"

    # Create GitHub release
    echo "Creating GitHub release..."
    echo "Enter release notes. Finish input with CTRL+D:"
    release_notes=$(cat)

    curl -X POST \
        -H "Authorization: token ${GITHUB_TOKEN}" \
        -H "Accept: application/vnd.github.v3+json" \
        https://api.github.com/repos/${GITHUB_REPO}/releases \
        -d "{
            \"tag_name\": \"$NEW_VERSION\",
            \"name\": \"Release $NEW_VERSION\",
            \"body\": \"$(echo "$release_notes" | sed ':a;N;$!ba;s/\n/\\n/g')\",
            \"draft\": false,
            \"prerelease\": false
        }"

    echo "GitHub release created for version $NEW_VERSION!"
}

case "$1" in
setup)
    setup_venv
    ;;
clean)
    clean
    ;;
release)
    release
    ;;
*)
    echo "Usage: $0 {setup|clean|release}"
    exit 1
    ;;
esac
