import click


@click.group()
@click.version_option(package_name="g4new", prog_name="g4new")
def main() -> None:
    """Easiest way to get a fully working Geant4 project ready to run."""
