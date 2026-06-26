---
applyTo: 'pyproject.toml'
---

# pyproject.toml — guidance

This file is the **single source of truth** for build, dependencies, and
tool configuration. Don't split things into separate config files
(`.flake8`, `mypy.ini`, `pytest.ini`, `setup.cfg`) — keep them all here.

## Dependencies

- **Runtime deps** go in `[project].dependencies`. Keep this list as
  **short as honestly possible**; every transitive dependency is a
  supply-chain surface and a future security alert.
- **Dev/test/docs deps** go in `[dependency-groups]` (uv-native). Install
  with `uv sync --all-groups` or scoped to a group with `uv sync --group dev`.
- Use lower bounds (`>=X.Y`), not exact pins, in this file. The exact
  resolution lives in `uv.lock` — that's what's installed reproducibly.
- **No `requirements.txt`.** If a downstream consumer asks for one, generate
  it on the fly with `uv export -o requirements.txt`.

## Tool configuration

- `[tool.ruff]` — `target-version = "py311"`, `line-length = 88`.
  Per-file-ignores already cover `tests/**` (allow ARG/SIM) and
  `__init__.py` (allow F401 for re-exports).
- `[tool.pytest.ini_options]` — **no `pythonpath` key**. The editable
  install handles imports. Adding pythonpath here would mask packaging
  bugs.
- `[tool.coverage.run]` — `branch = true`. **Don't add `--cov-fail-under`**
  to either pytest addopts or coverage config — coverage is reported, not
  gated, by deliberate choice.
- `[tool.mypy]` — `strict = false`. Strictness is intentionally light so
  contributors aren't blocked on incremental typing work. Don't tighten
  this without a team conversation.

## Build

- Build backend is `hatchling`. Wheel target packages `src/mypackage`;
  sdist includes the source, tests, README, LICENSE, CONTRIBUTING.
- The `py.typed` marker file in `src/mypackage/` ships automatically
  via the wheel target — don't add an explicit include for it.

## Version bumps

- Bump `[project].version` here only. `__version__` is read at runtime from
  installed package metadata via `importlib.metadata.version("mypackage")`,
  so there is no second literal to keep in sync.
- Also roll `CHANGELOG.md` in the same PR: move `[Unreleased]` entries under
  a new `[X.Y.Z]` heading.
- Follow SemVer: pre-1.0 means breaking changes are allowed in minor bumps.
