# Contributing to mypackage

## First-time setup

After cloning the repository:

```powershell
uv python install 3.11
uv python pin 3.11
uv venv
uv sync --all-groups
uv run pre-commit install
uv run pre-commit install --hook-type pre-push
```

- `uv` will fetch and manage Python 3.11 — no system install required.
- `uv sync --all-groups` installs the project (editable) plus the `dev` dependency group, creating `.venv/` and `uv.lock`.
- The two `pre-commit install` commands register the git hooks: lint/format/security on commit, full test suite on push.

## Adding a new module

The public API for this package has not been designed yet — the scaffold
intentionally ships only `__version__`. The first PR that adds real code is
also the PR that decides the public contract (module layout, naming, return
conventions).

When that PR lands, it should also update this section with the agreed
conventions.

Until then, contributors adding the first module should:

1. Open a design discussion (issue or draft PR) before writing the
   implementation, so reviewers can weigh in on the contract shape.
2. Mirror the chosen `src/mypackage/...` layout under `tests/...`.
3. Run `uv run pytest` and `uv run pre-commit run --all-files` before
   opening the PR.

## Pre-commit hooks

| Stage | Hook | What it does |
|-------|------|--------------|
| `pre-commit` | `check-case-conflict` | Catches case-insensitive filename conflicts |
| `pre-commit` | `check-merge-conflict` | Blocks accidental merge conflict markers |
| `pre-commit` | `end-of-file-fixer` | Ensures files end with a newline |
| `pre-commit` | `trailing-whitespace` | Strips trailing whitespace |
| `pre-commit` | `check-toml` / `check-yaml` / `check-json` | Validates config file syntax |
| `pre-commit` | `nbstripout` | Strips notebook outputs before commit |
| `pre-commit` | `ruff format` | Formats Python code |
| `pre-commit` | `ruff check` | Lints and auto-fixes Python code |
| `pre-commit` | `bandit` | Security linting on `src/mypackage` |
| `pre-push`   | `pytest` | Runs the full test suite (with coverage report; no threshold) |
| `manual`     | `mypy` | Light static type check — opt in: `uv run pre-commit run mypy --all-files --hook-stage manual` |

Run all commit-stage hooks manually at any time:

```powershell
uv run pre-commit run --all-files
```

## Code quality

Before submitting a PR, ensure the following pass locally:

```powershell
uv run ruff format .
uv run ruff check . --fix
uv run pytest
```

CI runs pytest on every matrix entry (Linux/3.11, Linux/3.12, Windows/3.12) and runs ruff, mypy and bandit once on the Linux/3.12 entry against every PR.

## Branch protection

The following branches are protected and cannot be pushed to directly. All changes land via pull request.

| Branch    | Purpose                                              |
|-----------|------------------------------------------------------|
| `master`  | Production / released code                           |
| `develop` | Integration branch for in-progress work              |
| `release` | Release candidates being prepared for `master`       |

### Required to merge

A PR targeting any protected branch must satisfy **all** of the following before the merge button activates:

- ✅ **CI passes** — every required status check from `.github/workflows/ci.yml` is green. Pytest runs on the full matrix (Linux/3.11, Linux/3.12, Windows/3.12); ruff format, ruff lint, mypy and bandit are gated to a single matrix entry (Linux/3.12) since their result is independent of OS and Python version.
- ✅ **CodeQL scan passes** — no new "error"-severity alerts introduced by the PR. Configured via GitHub's default code-scanning setup.
- ✅ **Copilot code review** — the automated Copilot review must complete (and any blocking comments resolved).
- ✅ **At least one Code Owner approval** — see [`.github/CODEOWNERS`](.github/CODEOWNERS).
- ✅ **Conversations resolved** — all PR review threads marked resolved.
- ✅ **Branch up to date with target** — rebase or merge the target branch in if it has moved.
- ✅ **Linear history** — squash- or rebase-merge only; no merge commits on protected branches.

### Other protections in force

- Force-push is **disabled** on protected branches.
- Branch deletion is **disabled** on protected branches.

> If any of the above is incorrect for your branch, check **Settings → Branches → Branch protection rules** in the GitHub UI for the authoritative configuration.

## Pull request conventions

Prefix PR titles with the type of change. Supported types:

- `feat` — new feature
- `fix` — bug fix
- `refactor` — code change that is neither a fix nor a feature
- `perf` — performance improvement
- `test` — adding or updating tests
- `docs` — documentation only
- `build` / `ci` — build system or CI/CD changes
- `deps` — dependency updates
- `revert` — reverts a previous commit

Example: `feat: add Widget class`

Link related issues in the PR description using `Closes #<issue>` or `Relates to #<issue>`.

## Releasing

Releases are currently **manual**. To cut a release:

1. Bump `version` in `pyproject.toml` (single source of truth — `__version__`
   is read from installed package metadata, no second literal to update).
2. Move the `[Unreleased]` entries in [CHANGELOG.md](CHANGELOG.md) under a new
   `[X.Y.Z]` heading with today's date and add a fresh empty `[Unreleased]`
   section.
3. Open a PR, get it merged to `master`.
4. Tag the merge commit: `git tag vX.Y.Z && git push origin vX.Y.Z`.
5. Build artefacts: `uv build` (produces `dist/*.whl` and `dist/*.tar.gz`).
6. Create a GitHub Release from the tag, paste the changelog section into the
   release notes, and attach the contents of `dist/`.

Automated release workflow (tag-triggered build + publish) will be added before
the first `1.0` release, once the publish target (public PyPI vs. internal
index) is decided.

## Common pitfalls

- ❌ Importing your code as `from src.mypackage...` → ✅ Always `from mypackage...`. The `src/` folder is the project layout root, **not** an importable package.
- ❌ Adding `sys.path` manipulation to `conftest.py` or any module → ✅ Rely on the editable install from `uv sync`. If imports fail, fix the install, not the path.
- ❌ Adding `python.analysis.extraPaths` to `.vscode/settings.json` → ✅ Leave it out; it masks packaging bugs.
- ❌ Creating `requirements.txt` → ✅ `pyproject.toml` and `uv.lock` are the source of truth. Use `uv export -o requirements.txt` if a flat list is ever needed.
