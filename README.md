# ppinspect

Version-aware analysis and editor tooling for `pyproject.toml`.

Python project configuration brings together packaging standards and settings for
tools that evolve independently. ppinspect aims to help you understand whether
that configuration is valid for the versions your project actually uses.

## Planned capabilities

- Validate Python/PyPA sections and tool-specific configuration.
- Detect unknown settings, deprecated options, and conflicting configuration
  with useful diagnostics and suggested fixes.
- Provide formatting, a `ppinspect` CLI, and language-server features such as
  completion, hover documentation, and quick fixes.

ppinspect is intended to complement tools like uv, Ruff, and ty—not replace
package management, Python source linting, or type checking.

## Current status

**[Version 0.1.0](https://pypi.org/project/ppinspect/0.1.0/) is a development
stub.** The package is importable and has no runtime dependencies, but the
capabilities above—including the CLI—are not implemented yet.

## Learn more and contribute

- [Project vision](https://github.com/jakeryderv/ppinspect/blob/main/docs/vision.md):
  intended capabilities, inspiration, and scope.
- [Contributing](https://github.com/jakeryderv/ppinspect/blob/main/CONTRIBUTING.md):
  development setup, validation, and proposing changes.
- [Publishing guide](https://github.com/jakeryderv/ppinspect/blob/main/docs/publishing.md):
  maintainer release instructions and current automation limits.

## License

[MIT](https://github.com/jakeryderv/ppinspect/blob/main/LICENSE), copyright 2026
Jake Van Slyke.
