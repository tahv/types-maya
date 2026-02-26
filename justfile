[private]
default:
    @just --list

# Sync development requirements
sync:
    uv sync

# Open project in neovim
nvim *args:
    uv run -- nvim {{ args }}

# Run ruff
ruff *files:
    uvx ruff check --output-format concise {{ files }}

# Run ty
ty *files:
    uvx ty check --output-format concise {{ files }}

# Dry run formatter and output the diffs
fmt:
    uvx ruff format --diff

# Perform type-checking with `mypy`
mypy:
    uv run -m mypy

# Perform type-checking with `pyright`
pyright:
    uv run -m pyright

build:
    uv build

# Calculate stub completion of a file based on `Incomplete` uses
[unix]
completion file:
    #!/usr/bin/env sh
    IMPLEMENTED=$(rg ^class --count {{ file }})
    INCOMPLETE=$(rg "^[^\s]+\: Incomplete$" --count {{ file }})
    echo "scale=2; 100 * $IMPLEMENTED / ($IMPLEMENTED + $INCOMPLETE)" | bc

image-name := "maya-stubs"

[private]
docker-build:
    docker build --platform linux/amd64 -t {{ image-name }} .

# Run an interactive docker container
interactive: docker-build
    docker run -it --rm {{ image-name }}

