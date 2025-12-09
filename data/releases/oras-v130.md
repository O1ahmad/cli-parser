# ORAS - v1.3.0

**Release Name**: v1.3.0
**Published**: 2025-09-08T04:55:08Z
**Repository**: https://github.com/oras-project/oras

---

## New Features

### Stable
* `oras` is compliant with OCI [distribution-spec v1.1.1](https://github.com/opencontainers/distribution-spec/releases/tag/v1.1.1)
* Show OS and architecture in `oras version`
* Add alias `oras manifest get` for `oras manifest fetch`

### Preview

* Improve tree view in `oras discover`
  * Display annotations by default
  * Colorize tree view 🌈

### Experimental

* Introduce [portable backup and restore of OCI artifacts, images, and repositories](https://oras.land/docs/how_to_guides/backup-restore/)
  * `oras backup`: New command to back up artifacts from remote registries into local OCI image layouts, either as directories or tar archives.
  * `oras restore`: New command to restore artifacts from local OCI image layouts (directories or tar archives) back to remote registries.
* Introduce [multi-arch image/artifact management](https://oras.land/docs/how_to_guides/multiarch/)
  * Add the `oras manifest index` command set to manage OCI image index manifests
    * `oras manifest index create` to create a new index from existing manifests
    * `oras manifest index update` to update an existing index manifest
  * Add `--artifact-platform` to `oras push` to push artifacts with platform information
  * Add `--format` to `oras repo ls` and `oras repo tags` with `text`, `json`, and `go-template` options
  * Support fully qualified references for OCI image layout via `--oci-layout-path`
* Refine the `oras discover` output for the `json` and `go-template` formats
  * **BREAKING CHANGE**: Rename the `manifests` field to `referrers`
  * Add subject manifest details to the `json` output
* `oras discover` now displays referrers recursively by default; the maximum recursion depth can be controlled via the `--depth` flag

## Feature Promotions
* Promote the following commands and flags from `Preview` to `Stable`:
  * `oras attach`
  * `oras attach --platform`
  * `oras pull --include-subject`
* Promote `oras resolve` from `Experimental` to `Preview`

## Deprecations

### Stable
* Deprecate the `-v`, `--verbose` flag (verbose output is now enabled by default)

### Preview
* **BREAKING CHANGE** Remove the global `--no-tty` flag
  * `--no-tty` remains available on individual TTY-capable commands

### Experimental
* Deprecate the `table` option of the `--format` flag in `oras discover`

## Bug Fixes
* Fix #1436: `oras tag` creates referrers tags unexpectedly
* Fix #1442: invalid progress bar shown for empty layers
* Fix #1494: invalid reference in the formatted output of `oras pull`
* Fix #1593: unable to download an artifact twice if it contains symbolic links
* Fix #1599: Auth token scope not correctly added when using `--debug` or `--no-tty` with `oras push`
* Fix #1623: Should show `KB` instead of `kB` in the progress bar
* Fix #1728: `oras cp` now correctly copies the root index when the index has no referrers
* Fix #1795, #1825: redundant blank lines in terminal output

## Other Changes
* Add support for the `loong64` architecture
* Upgrade to Go `1.25.0`
* Enhance UX:
  * Improve [diagnostic experience](https://github.com/oras-project/oras/blob/v1.3.0-beta.1/docs/proposals/diagnose-experience.md) through `--debug` logs
  * Improve error messages
* Improve documentation
* Optimize code structure
* Update dependencies
* Minor security enhancements

## New Contributors
* @bcho made their first contribution in https://github.com/oras-project/oras/pull/1408
* @njucjc made their first contribution in https://github.com/oras-project/oras/pull/1435
* @nmiyake made their first contribution in https://github.com/oras-project/oras/pull/1477
* @mauriciovasquezbernal made their first contribution in https://github.com/oras-project/oras/pull/1507
* @Horiodino made their first contribution in https://github.com/oras-project/oras/pull/1607
* @chrisguitarguy made their first contribution in https://github.com/oras-project/oras/pull/1658
* @kysucix made their first contribution in https://github.com/oras-project/oras/pull/1671
* @RohanMishra315 made their first contribution in https://github.com/oras-project/oras/pull/1650
* @apparentlymart made their first contribution in https://github.com/oras-project/oras/pull/1696
* @Copilot made their first contribution in https://github.com/oras-project/oras/pull/1755
* @tanyabhatnagar made their first contribution in https://github.com/oras-project/oras/pull/1761
* @amazingfate made their first contribution in https://github.com/oras-project/oras/pull/1787

**Full Changelog**: https://github.com/oras-project/oras/compare/v1.2.0...v1.3.0

## What's Changed Since RC.2

* bump: tag and release ORAS CLI v1.3.0-rc.2 by @Wwwsylvia in https://github.com/oras-project/oras/pull/1834
* build(deps): bump github.com/onsi/ginkgo/v2 from 2.25.1 to 2.25.2 in /test/e2e by @dependabot[bot] in https://github.com/oras-project/oras/pull/1836
* build(deps): bump github.com/spf13/cobra from 1.9.1 to 1.10.1 by @dependabot[bot] in https://github.com/oras-project/oras/pull/1837


**Full Changelog**: https://github.com/oras-project/oras/compare/v1.3.0-rc.2...v1.3.0

## Notes

This release was signed with `3E94 D52A FA46 5877 CAEA 79F1 E805 2EA1 7ECB 9A6C` (@Wwwsylvia's GPG key) which can be found [here](https://github.com/Wwwsylvia.gpg).