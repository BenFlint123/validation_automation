"""mypackage — short description of your package.

Replace this docstring (and the package name `mypackage` throughout the
repository) with details for the library you are building from this template.
"""

from importlib.metadata import PackageNotFoundError, version


try:
    __version__ = version("mypackage")
except PackageNotFoundError:  # pragma: no cover — only hit if not installed
    __version__ = "0.0.0+unknown"

__all__ = ["__version__"]
