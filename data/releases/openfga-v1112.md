# OpenFGA - v1.11.2

**Release Name**: v1.11.2
**Published**: 2025-12-04T17:23:09Z
**Repository**: https://github.com/openfga/openfga

---

## What's Changed
### Fixed
- Fixed an issue with the `InMemoryCacheController` (the default cache controller when enabled) where cached Check responses were not invalidated after a write to the store. Previously, invalidation only occurred if multiple Checks were triggered in rapid succession after a write. [#2811](https://github.com/openfga/openfga/pull/2811)
- Update toolchain go version to 1.25.5 to address [CVE-2025-61729](https://pkg.go.dev/vuln/GO-2025-4155) in the go std lib.

## New Contributors
* @saad-h1 made their first contribution in https://github.com/openfga/openfga/pull/2811
* @step-security-bot made their first contribution in https://github.com/openfga/openfga/pull/2830

**Full Changelog**: https://github.com/openfga/openfga/compare/v1.11.1...v1.11.2

