# justfile for tomdstanton

set shell := ["bash", "-uc"]

# Print available commands
default:
    @just --list


install:
    uv venv
    uv pip install zensical

build: install
    cp README.md docs/index.md
    uv run zensical build


# Clean build artifacts
clean:
    cargo clean
    rm -rf .venv
    rm -f rammappy.so
    rm -rf rammappy
    rm -rf target/wheels
    rm -rf site
    rm -f docs/index.md docs/contributing.md
    find . -type d -name "__pycache__" -exec rm -rf {} +
