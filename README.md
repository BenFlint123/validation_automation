# mypackage

A Python library template — `uv` + Ruff + `src/` layout, packaged with
`hatchling` and ready for CI, pre-commit, and release.

> **Status:** Template scaffold. The package is currently a stub:
> `src/mypackage/` exposes `__version__` and nothing else. Replace the
> placeholder name and add your own modules to make this your own.

---

## Using this template

This repository is a generic scaffold. After copying it (fork, "Use this
template", or `git clone`) do the following before adding your own code:

1. **Pick a package name** (PEP 8: lowercase, ideally one word, e.g.
   `mylib`). Then global-replace `mypackage` with that name across the
   workspace, including:
   - the directory `src/mypackage/`
   - `pyproject.toml` (`name`, hatch packages/sdist `include`, ruff
     `known-first-party`, `--cov=…`, `coverage.run.source`, `mypy.files`,
     `bandit.targets`)
   - `tests/test_smoke.py` (3 imports)
   - `src/mypackage/__init__.py` (docstring + `version("…")`)
   - `.github/copilot-instructions.md`, `.github/instructions/*.md`
   - `.github/workflows/ci.yml` (bandit path)
   - `.github/CODEOWNERS`, `.github/ISSUE_TEMPLATE/*` comments/examples
   - `.vscode/launch.json`, `.vscode/settings.json` comments
   - `.pre-commit-config.yaml` (`files:` patterns, if any)
   - this README and `CONTRIBUTING.md`, `SECURITY.md`
2. **Set the project description, keywords, and classifiers** in
   `pyproject.toml`.
3. **Update the repository URL** in `pyproject.toml`
   (`[project.urls] Repository`) and in
   `.github/ISSUE_TEMPLATE/config.yml`.
4. **Review `LICENSE`** — currently BSD 3-Clause with `Copyright (c) 2026,
   Ben Flint`. Update the year and copyright holder if needed, or replace the
   licence file entirely.
5. **Review `.github/CODEOWNERS`** —
   Replace with your team's GitHub usernames.
6. **Reset `CHANGELOG.md`** entries as you cut releases (the template
   ships with an empty `## [Unreleased]` section).
7. Run `uv sync` to generate a fresh `uv.lock` (the template ships
   without one).

A quick verification that the rename is complete:

```powershell
git grep -i "mypackage"          # should match only the new name
```

---

## Quick start

This project uses [`uv`](https://docs.astral.sh/uv/) to manage the Python
toolchain, virtual environment and dependencies. You do **not** need a
system-wide Python 3.11 — `uv` will fetch one for you.

```powershell
# 1. Install uv (one-time, if you don't have it):
#    https://docs.astral.sh/uv/getting-started/installation/

# 2. Clone & enter the repo
git clone <your-repo-url>/mypackage.git
cd mypackage

# 3. Install Python 3.11 (managed by uv) and pin the project to it
uv python install 3.11
uv python pin 3.11

# 4. Create the venv and install the project + dev dependencies
uv venv
uv sync --all-groups

# 5. Install pre-commit hooks
uv run pre-commit install
uv run pre-commit install --hook-type pre-push
```

Verify the install:

```powershell
uv run python -c "import mypackage; print(mypackage.__version__)"
uv run pytest -q
```

## Layout

```
src/mypackage/                  # package root (stub)
├── __init__.py                 # exposes __version__
└── py.typed                    # PEP 561 marker
tests/                          # pytest suite
.github/workflows/ci.yml        # CI: pytest on the full matrix; ruff/mypy/bandit gated to Linux/3.12
.pre-commit-config.yaml         # ruff, bandit, nbstripout (commit) + pytest (push) + mypy (manual)
pyproject.toml                  # single source of truth for build, deps and tool config
.python-version                 # 3.11 (consumed by uv)
```

## Adding a new module

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Day-to-day commands

```powershell
uv run pytest                                            # run unit tests + coverage report (no threshold)
uv run ruff format .                                     # format
uv run ruff check . --fix                                # lint + autofix
uv run pre-commit run --all-files                        # all commit-stage hooks
uv run pre-commit run mypy --all-files --hook-stage manual  # type-check on demand
uv build                                                 # produce wheel + sdist in dist/
```

## Installation in another project

Once a release tag exists in your repo:

```powershell
pip install git+<your-repo-url>/mypackage.git@v0.1.0
```

Or, after `uv build`, install the produced wheel directly.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

BSD 3-Clause — see [LICENSE](LICENSE).
