"""validation_automation — a library for the automation of model validation tests."""

from importlib.metadata import PackageNotFoundError, version


try:
    __version__ = version("validation_automation")
except PackageNotFoundError:  # pragma: no cover — only hit if not installed
    __version__ = "0.0.0+unknown"

__all__ = ["__version__"]
