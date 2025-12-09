# Distribution - v3.0.0

**Release Name**: v3.0.0
**Published**: 2025-04-03T06:25:36Z
**Repository**: https://github.com/distribution/distribution

---

Welcome to the `v3.0.0` release of registry!

This is the first v3 stable release since [`v2.8.3`](https://github.com/distribution/distribution/releases/tag/v2.8.3) which is a culmination of years of hard work of the container community and registry maintainers!

If you are upgrading from `v2.x` and have never used any of the release candidates, please familiarise yourselves with the `v2.x` deprecations properly.

## Deprecations
* oss and swift storage drivers are no longer supported
* [`docker/libtrust`](https://github.com/docker/libtrust) has been replaced with [`go-jose/go-jose`](https://github.com/go-jose/go-jose) in https://github.com/distribution/distribution/pull/4096
* `client` is no longer supported as a standalone package in https://github.com/distribution/distribution/pull/4126
* the default configuration path has changed to `/etc/distribution/config.yml`
* `ManifestBuilder` interface in [3886](https://github.com/distribution/distribution/pull/3886)
* `manifest.Versioned` has been deprecated in favor of `oci.Versioned` in [3887](https://github.com/distribution/distribution/pull/3887)
* `reference` package has been moved to [github.com/distribution/reference](github.com/distribution/reference) in https://github.com/distribution/distribution/pull/4063

## Changes since the last release candidate

### Changes
<details><summary>7 commits</summary>
<p>
  * [`2e63da99`](https://github.com/distribution/distribution/commit/2e63da99776be71a17be3f79f60e4c3f485b87e1) Fix golangci-lint config (#4612)
  * [`fd14cf19`](https://github.com/distribution/distribution/commit/fd14cf193339eb2300828363560884f4ccbadba3) Vrify the linter config first before running it
  * [`3a33ba12`](https://github.com/distribution/distribution/commit/3a33ba12ad9a436792c1e89a3732f8600940f6e6) Fix golangci-lint config
  * [`75f32197`](https://github.com/distribution/distribution/commit/75f32197b6f180518d17210195ae0d3eb3885ce5) Bump Azure deps (#4611)
  * [`52f0f6c4`](https://github.com/distribution/distribution/commit/52f0f6c45d5397ebff48778b7c5c8b1dec89e572) Bump Azure deps
  * [`ef21149b`](https://github.com/distribution/distribution/commit/ef21149b4999ac0be22fe292640491b55cac9d9b) build(deps): bump github.com/golang-jwt/jwt/v5 from 5.2.1 to 5.2.2 in the go_modules group across 1 directory (#4608)
  * [`05b308bc`](https://github.com/distribution/distribution/commit/05b308bc42519068f6157747301f5e68ef01b9af) build(deps): bump github.com/golang-jwt/jwt/v5
</p>
</details>

Previous release can be found at [v3.0.0-rc.4](https://github.com/distribution/distribution/releases/tag/v3.0.0-rc.4)