# Contributing to ppinspect

ppinspect is at the development-stub stage. Start with the
[project vision](docs/vision.md) for its intended scope; planned features are not
yet implemented.

## Proposing changes

For substantial features or design changes, open an
[issue](https://github.com/jakeryderv/ppinspect/issues) to discuss the problem and
approach before implementation. Small documentation fixes can go straight to a
pull request.

Keep changes focused, describe what changed and why, and include the checks you
ran in your pull request. Add meaningful tests when introducing executable
behavior, and keep documentation clear about what exists versus what is planned.
The planned top-level command is `ppinspect`; there is no CLI yet.

## Development setup

Requires Python 3.11+ and [uv](https://docs.astral.sh/uv/getting-started/installation/).
The publishing workflow uses uv 0.12.18. The development interpreter is set to
Python 3.11 in `.python-version`.

```sh
git clone https://github.com/jakeryderv/ppinspect.git
cd ppinspect
uv sync --locked
```

The package source lives in `src/ppinspect/`.

## Validation and build

There is no functional API or test suite yet. From the repository root, validate
the lockfile, import, and installed version, then build the wheel and source
distribution:

```sh
uv lock --check
uv run --locked python -c 'import ppinspect; from importlib.metadata import version; assert version("ppinspect") == "0.1.0"'
uv build
```

To smoke-test the built wheel in a separate environment without importing the
source checkout (POSIX shell):

```sh
check_dir=$(mktemp -d)
uv venv --python 3.11 "$check_dir/venv"
uv pip install --python "$check_dir/venv/bin/python" --no-deps dist/ppinspect-0.1.0-py3-none-any.whl
"$check_dir/venv/bin/python" -I -c 'import ppinspect; from importlib.metadata import version; assert version("ppinspect") == "0.1.0"; print(ppinspect.__file__)'
rm -rf "$check_dir"
```

These examples target the current version, `0.1.0`. Update version-specific
checks and artifact paths when the package version changes.

Generated artifacts are in `dist/` and must not be committed. Keep virtual
environments, credentials, and local agent state out of commits as well.

The current publishing workflow validates release artifacts; it does not run on
ordinary pushes or pull requests. Run the checks above locally for your changes.
See the [publishing guide](docs/publishing.md) for release-specific validation
and trusted-publisher configuration.
