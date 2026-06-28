from click.testing import CliRunner

from g4new.cli import main


def test_help_exits_zero():
    runner = CliRunner()
    result = runner.invoke(main, ["--help"])
    assert result.exit_code == 0


def test_help_mentions_geant4():
    runner = CliRunner()
    result = runner.invoke(main, ["--help"])
    assert "Geant4" in result.output


def test_version_exits_zero():
    runner = CliRunner()
    result = runner.invoke(main, ["--version"])
    assert result.exit_code == 0
