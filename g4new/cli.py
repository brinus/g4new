import click

from g4new import __version__


@click.group()
@click.version_option(version=__version__)
def main() -> None:
    """Easiest way to get a fully working Geant4 project ready to run."""
