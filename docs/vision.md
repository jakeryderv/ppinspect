## `ppinspect`: pyproject.toml Analyzer / Language Server

### Idea

Build a developer tool that **validates, lints, formats, and provides editor intelligence for `pyproject.toml`**, understanding both official Python standards and tool-specific configuration.

Think:

> **Ruff/ty-style developer experience, but for `pyproject.toml` itself.**

### Why / Inspiration

Modern Python increasingly centralizes configuration in `pyproject.toml`, but the file combines multiple independently evolving specifications:

```text
pyproject.toml
├── Python/PyPA standards
│   ├── [project]
│   ├── [build-system]
│   └── [dependency-groups]
│
└── Tool-specific configuration
    ├── [tool.uv]
    ├── [tool.ruff]
    ├── [tool.ty]
    ├── [tool.pytest]
    └── ...
```

Knowing whether a configuration is valid often requires consulting multiple documentation sites and accounting for **different tool versions**.

The inspiration is the experience provided by tools like Ruff and ty: fast diagnostics, useful errors, autofixes, and strong editor integration.

### Core functionality

The tool would:

* Parse and validate TOML syntax.
* Validate standardized Python/PyPA sections.
* Validate `[tool.*]` sections against tool-specific schemas.
* Detect the project's actual/locked tool versions when possible.
* Perform **version-aware validation**.
* Detect unknown/misspelled settings and suggest corrections.
* Validate types, enums, required properties, and incompatible settings.
* Lint redundant, deprecated, suspicious, or conflicting configuration.
* Format `pyproject.toml` consistently.
* Provide an LSP for autocomplete, hover documentation, diagnostics, and quick fixes.
* Expose a CLI suitable for local development and CI.

Example:

```text
$ pyproject check

tool.ruff.line-lenght
                 ^^^^^
Unknown setting `line-lenght`.
Did you mean `line-length`?

Configured Ruff: 0.x
```

### In scope

```text
✓ TOML parsing
✓ formatting
✓ Python/PyPA schema validation
✓ [tool.*] schema validation
✓ version-aware configuration
✓ configuration linting
✓ deprecation detection
✓ helpful diagnostics/autofixes
✓ CLI
✓ language server / editor integration
✓ CI usage
```

### Out of scope

```text
✗ Python source linting → Ruff
✗ Python type checking → ty/Pyright
✗ dependency resolution → uv/pip
✗ environment management → uv
✗ package building/publishing → uv/build tools
✗ replacing the tools being configured
```

The goal is specifically to become the **static analyzer and language tooling for `pyproject.toml`**, complementing tools like uv, Ruff, and ty rather than replacing them.

