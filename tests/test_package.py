"""Smoke tests for the installed development package, not its planned features."""

import tomllib
from importlib.metadata import distribution
from importlib.resources import files
from pathlib import Path

import ppinspect


def test_installed_metadata_matches_project() -> None:
    project_file = Path(__file__).resolve().parents[1] / "pyproject.toml"
    with project_file.open("rb") as stream:
        project = tomllib.load(stream)["project"]

    installed = distribution("ppinspect")
    assert installed.metadata["Name"] == project["name"]
    assert installed.version == project["version"]
    assert installed.metadata["Requires-Python"] == project["requires-python"]


def test_package_includes_typing_marker() -> None:
    assert files(ppinspect).joinpath("py.typed").is_file()
