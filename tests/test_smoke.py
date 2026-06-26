"""Smoke tests — packaging only.

These deliberately make **no claims about the public API or registry shape**.
They exist to prove the package installs cleanly via `uv sync` and that the
`src/` layout is wired correctly. Real behavioural tests should live next to
the real code that introduces those behaviours.
"""

from __future__ import annotations

import sys


def test_package_imports():
    import mypackage  # noqa: F401


def test_package_has_version():
    import mypackage

    assert isinstance(mypackage.__version__, str)
    assert mypackage.__version__  # non-empty


def test_src_is_not_on_sys_modules():
    """`src/` must not be importable as a package — it is just the layout root."""
    import mypackage  # noqa: F401  (force import)

    assert "src" not in sys.modules
