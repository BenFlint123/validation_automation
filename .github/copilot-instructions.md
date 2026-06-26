# mypackage — AI Coding Guide

Workspace-wide guidance. Path-scoped instructions live under
[`.github/instructions/`](./instructions/) and are loaded automatically when
you edit matching files.

## Project overview

`mypackage` is a Python library scaffolded from this template.

> **Status:** the library is in early scaffold. `src/mypackage/` is
> intentionally near-empty — only `__init__.py` (exposing `__version__`) and
> the `py.typed` marker. The public API has not been designed yet and will
> land in subsequent PRs.

## Stable conventions

These are locked in and worth defending:

- **`src/` layout, editable install via `uv`.** Imports are always
  `from mypackage...`, never `from src.mypackage...`. There is no
  `src/__init__.py`; `src/` is the layout root, not a package.
- **No `sys.path` manipulation** anywhere — `conftest.py`, modules, scripts.
  If imports fail, fix the install (`uv sync`), not the path.
- **`pyproject.toml` + `uv.lock` are the source of truth for dependencies.**
  No `requirements.txt`, no `setup.py`.
- **Python 3.11 minimum** (pinned via `.python-version`). CI also runs 3.12.

## Tooling

- **uv** — Python install, venv, dependency management.
- **Ruff** — sole linter and formatter.
- **pytest + pytest-cov** — tests. Coverage is *reported*, never *gated*.
- **mypy** — light (`strict = false`), runs on demand and in CI only.
- **bandit** — security lint on `src/`.
- **pre-commit** — commit stage: ruff/bandit/hygiene; push stage: pytest;
  manual stage: mypy.
- **hatchling** — build backend.

## Pull request conventions

Prefix PR titles with the type of change. Supported types:
`feat`, `fix`, `refactor`, `perf`, `test`, `docs`, `build`, `ci`, `deps`, `revert`.

Example: `feat: add Widget class`.

Link related issues in the PR body using `Closes #<n>` or `Relates to #<n>`.

## Common pitfalls (workspace-wide)

- ❌ `from src.mypackage...` → ✅ `from mypackage...`
- ❌ `sys.path.insert(...)` anywhere → ✅ rely on the editable install
- ❌ `python.analysis.extraPaths` in `.vscode/settings.json` → ✅ leave it minimal
- ❌ `requirements.txt` → ✅ `pyproject.toml` + `uv.lock`
- ❌ `pythonpath` in `[tool.pytest.ini_options]` → ✅ omit it
- ❌ `--cov-fail-under` in pytest addopts → ✅ coverage is reported, never gated

## Where to look for path-scoped guidance

| When editing… | See |
|---|---|
| `tests/**` | [tests.instructions.md](./instructions/tests.instructions.md) |
| `.github/workflows/**` | [workflows.instructions.md](./instructions/workflows.instructions.md) |
| `pyproject.toml` | [pyproject.instructions.md](./instructions/pyproject.instructions.md) |
