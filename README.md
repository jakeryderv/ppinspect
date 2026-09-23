# ppinspect

Inspect, validate, lint, and understand `pyproject.toml` with version-aware
analysis and editor tooling — the intended purpose of this project.

**Version 0.1.0 is a development stub.** The package is importable, but no
inspection, validation, linting, editor integration, or command-line interface
is implemented yet. It has no runtime dependencies.

## Development

Requires Python 3.11+ and [uv](https://docs.astral.sh/uv/getting-started/installation/).
CI uses uv 0.12.18. The development interpreter is set to Python 3.11 in
`.python-version`.

```sh
git clone https://github.com/jakeryderv/ppinspect.git
cd ppinspect
uv sync --locked
```

### Validation and build

There is no functional API to test yet. Validate the lockfile, import, and
installed version, then build the wheel and source distribution:

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

Generated artifacts are in `dist/` and must not be committed. Inspect both
archives and their metadata before release; they should contain the stub,
MIT license, and accurate package description, not local state or credentials.

## Publishing

The production PyPI target is [`ppinspect`](https://pypi.org/project/ppinspect/).
[The release workflow](.github/workflows/publish.yml) uses PyPI Trusted Publishing
with this identity:

- GitHub repository: [`jakeryderv/ppinspect`](https://github.com/jakeryderv/ppinspect)
- Workflow filename: `publish.yml`
- GitHub environment: `pypi`

Pushing the exact tag `v0.1.0` triggers the initial release. The workflow checks
that the tag matches the package version, validates the lockfile and import,
builds distributions with `uv build --no-sources`, checks metadata with
`uvx --from twine==7.0.0 twine check --strict dist/*`, and independently installs
and imports both the wheel and source distribution before uploading artifacts.

A separate job publishes those same artifacts using
`uv publish --trusted-publishing always` and GitHub OIDC, without a stored PyPI
token. It uses the `pypi` environment and respects its configured protections;
an environment name alone does not require approval. There is no manual trigger
or trigger for other tags. Review the workflow before enabling future releases.

Check the Actions run and PyPI project to confirm publication. Publishing a stub
does not guarantee ownership or permanent reservation of a PyPI project name.

## License

[MIT](LICENSE), copyright 2026 Jake Van Slyke.
