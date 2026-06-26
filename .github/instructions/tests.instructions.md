---
applyTo: 'tests/**'
---

# Pytest suite — guidance

Unit and integration tests for `mypackage`. Mirrors the `src/` layout.

## Conventions

- File names: `test_*.py`. Function names: `test_*`. Class names: `Test*`.
- Place each test next to its mirror in `src/`. A test for
  `src/mypackage/foo/bar.py` lives at `tests/foo/test_bar.py`.
- Use `pytest.fixture` for setup; avoid module-level state.
- Use `pytest.parametrize` for table-driven cases — it gives better failure
  messages than a `for` loop with `assert`.
- For expected exceptions use `pytest.raises(...)`, not bare
  `try/except` + `assert False`.

## What's already configured

- `pytest --cov=mypackage` runs automatically (see `pyproject.toml`).
  Don't pass `--cov` manually unless you're scoping to a single subpath.
- `--strict-markers` and `--strict-config` are on. New custom markers
  must be registered in `pyproject.toml` under
  `[tool.pytest.ini_options].markers`.
- `--import-mode=importlib` — the test discovery mechanism. Don't change
  this without checking the import-side-effect implications.

## Hard rules

- **No `sys.path` manipulation in `conftest.py` or anywhere else.**
  The editable install (`uv sync`) puts `mypackage` on the import path.
  If imports fail, fix the install, not the path.
- **No `pythonpath` key in `[tool.pytest.ini_options]`.** Same reason.
- Tests should run on a fresh checkout after `uv sync` with **no other
  setup**. If you need fixtures from disk, put them under `tests/` and
  load them via `pathlib.Path(__file__).parent / "fixtures" / ...`.

## Things ruff is configured to be lenient about here

The `tests/**/*.py` per-file-ignore in `pyproject.toml` disables `ARG`
(unused args, common in pytest fixtures) and `SIM` (over-eager
simplifications that hurt assertion readability). Don't add `# noqa`
comments for these — they're already allowed.
