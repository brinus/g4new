# Boilerplate Setup — Design Spec

**Date:** 2026-06-29
**Project:** g4new

## Goal

Set up the full Python project boilerplate for `g4new`, a CLI scaffolding tool that generates Geant4 C++/CMake project structures. The toolchain mirrors the `quantalyst` repo.

## Repository Structure

```
g4new/
├── pyproject.toml
├── .pre-commit-config.yaml
├── mkdocs.yml
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── publish.yml
├── docs/
│   └── index.md
├── g4new/
│   ├── __init__.py
│   └── cli.py
└── tests/
    └── __init__.py
```

The installed CLI command is `g4new`, entrypoint `g4new.cli:main`.

## `pyproject.toml`

- Build backend: `setuptools` + `setuptools-scm` (version from git tags)
- Package name: `g4new`, published to PyPI
- Python: `>=3.12`, classifiers for 3.12 / 3.13 / 3.14
- Runtime dependency: `click>=8.0`
- Dev extras: `pytest`, `pytest-cov`, `pre-commit`, `ruff`, `pyright`, `mkdocs-material`, `build`
- Ruff: target `py312`, line-length 88, rules `E F I UP B SIM`
- Pyright: `py312`, `standard` mode
- Pytest: `testpaths = ["tests"]`, `--tb=short`

## Pre-commit

Identical to quantalyst:
- `ruff` (lint + fix) and `ruff-format` via `astral-sh/ruff-pre-commit`
- `trailing-whitespace`, `end-of-file-fixer`, `check-yaml`, `check-toml`, `check-merge-conflict` via `pre-commit-hooks`

## GitHub Actions

**`ci.yml`** (on push and PR):
- `lint` job: ruff check + format check on Python 3.12
- `test` job: matrix over 3.12 / 3.13 / 3.14, runs `pytest --cov=g4new --cov-report=term-missing`
- Both jobs use `fetch-depth: 0` for setuptools-scm compatibility

**`publish.yml`** (on tag `v*`):
- Builds with `python -m build`
- Uploads to PyPI via `twine` using `PYPI_API_TOKEN` secret

## Docs

- MkDocs Material theme with `navigation.instant`, `navigation.top`, `search.suggest`
- `repo_url` points to `https://github.com/brinus/g4new`
- Minimal `docs/index.md` with install + quick-start snippet
