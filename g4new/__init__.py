from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("g4new")
except PackageNotFoundError:
    __version__ = "0.0.0+dev"
