# Publishing ppinspect

This guide is for maintainers. For development setup and local build/import
checks, see [Contributing](../CONTRIBUTING.md).

## Current release automation

The production PyPI target is [`ppinspect`](https://pypi.org/project/ppinspect/).
[The release workflow](../.github/workflows/publish.yml) uses PyPI Trusted
Publishing with this identity:

- GitHub repository: [`jakeryderv/ppinspect`](https://github.com/jakeryderv/ppinspect)
- Workflow filename: `publish.yml`
- GitHub environment: `pypi`

Publication is **tag-driven**, not GitHub Release–driven. Pushing the exact tag
`v0.1.0` triggers the initial-release workflow. Tags must be created and pushed
manually; the workflow does not create tags or GitHub Releases. Creating a GitHub
Release is not required for publication.

The workflow:

1. Checks that the tag matches the package version and validates the lockfile
   and package import.
2. Builds distributions with `uv build --no-sources`.
3. Checks metadata with `uvx --from twine==7.0.0 twine check --strict dist/*`.
4. Independently installs and imports both the wheel and source distribution.
5. Transfers the validated artifacts to a separate publishing job.
6. Publishes those same artifacts using `uv publish --trusted-publishing always`
   and GitHub OIDC, without a stored PyPI token.

Only the publishing job has `id-token: write`. It uses the `pypi` environment and
respects its configured protections; an environment name alone does not require
approval.

## Before another release

**Version 0.1.0 is already published.** The current workflow accepts only
`v0.1.0`: it has no manual trigger and does not accept other tags. Its publish-job
condition and import assertions are also specific to that initial version.
Do not reuse or move the published tag to release new content.

Before publishing a new version:

- Update the package version and lockfile, and keep the README's status accurate.
- Review and update the workflow's tag trigger, publish-job condition, and
  version-specific assertions. Keep the tag/package-version consistency check.
- Update version-specific examples in [Contributing](../CONTRIBUTING.md).
- Run the documented local checks and the release-specific build, metadata, and
  artifact-install checks above. Inspect both archives and their metadata: they
  should contain the intended package, MIT license, and accurate description,
  not local state or credentials. Do not publish stale artifacts from `dist/`.
- Commit and push the reviewed release changes, then create and push the matching
  version tag once the workflow supports it.

A GitHub Release can optionally provide release notes; it is not a publishing
prerequisite.

## Verify publication

Check the [Actions run](https://github.com/jakeryderv/ppinspect/actions) and the
[PyPI project](https://pypi.org/project/ppinspect/) to confirm publication. Verify
that the expected version and both distribution files are present, and test an
installation from production PyPI in an isolated environment.

If an upload's outcome is unclear, inspect PyPI before retrying. Published
versions cannot be overwritten with different artifacts.

Publishing a stub does not guarantee ownership or permanent reservation of a
PyPI project name.
