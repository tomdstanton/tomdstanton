# justfile for tomdstanton

set shell := ["bash", "-uc"]

# Print available commands
default:
    @just --list

# Sync python dependencies and create the virtual environment using `uv`
sync:
    uv sync

# Installs everything needed to build the static site
install: clean
    uv venv
    uv pip install zensical

# Builds the static site
build: install
    cp README.md docs/index.md
    uv run zensical build

# Build and serve the documentation locally
serve: install
    cp README.md docs/index.md
    uv run zensical serve

# Clean build artifacts
clean:
    rm -rf .venv
    rm -rf site
    rm -f docs/index.md
    find . -type d -name "__pycache__" -exec rm -rf {} +
