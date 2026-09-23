# ppinspect

> [!IMPORTANT]
> **ppinspect has moved to [pyprojx](https://github.com/jakeryderv/pyprojx).**
> This repository is archived and will not receive further updates.

Version-aware intelligence for `pyproject.toml`—check, explain, and safely evolve
your Python configuration.

Python project configuration brings together packaging standards and settings for
tools that evolve independently. ppinspect aims to help you understand and safely
maintain that configuration for the versions your project actually uses, with
analysis as the foundation for useful explanations and reviewable improvements.

## Planned capabilities

- Validate Python/PyPA sections and tool-specific configuration.
- Explain configuration issues, including unknown settings, deprecated options,
  and conflicts, with useful diagnostics and suggested fixes.
- Provide formatting, a `ppinspect` CLI, and language-server features such as
  completion, hover documentation, and quick fixes.

Guided editing, configuration migrations, and generation are possible future
directions built on that foundation—not committed features or current capabilities.

The focus is `pyproject.toml`, not general project management. ppinspect is intended
to complement tools like uv, Ruff, and ty—not replace package management, Python
source linting, or type checking.

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
