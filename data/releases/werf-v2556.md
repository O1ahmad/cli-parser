# werf - v2.55.6

**Release Name**: v2.55.6 [alpha]
**Published**: 2025-12-08T10:30:07Z
**Repository**: https://github.com/werf/werf

---

## Changelog


### Bug Fixes

* **build, import:** should not resolve symlinks ([c28127a](https://github.com/werf/werf/commit/c28127a095e6153ca8d295cb0165d96441ff3e24))
* **deploy:** hooks cleaned up too early ([42c57b4](https://github.com/werf/werf/commit/42c57b4e077d7b0b02f64f0b194155856248a2af))

## Installation

To install `werf` we strongly recommend following [these instructions](https://werf.io/getting_started/).

Alternatively, you can download `werf` binaries from here:
* [Linux amd64](https://tuf.werf.io/targets/releases/2.55.6/linux-amd64/bin/werf) ([PGP signature](https://tuf.werf.io/targets/signatures/2.55.6/linux-amd64/bin/werf.sig))
* [Linux arm64](https://tuf.werf.io/targets/releases/2.55.6/linux-arm64/bin/werf) ([PGP signature](https://tuf.werf.io/targets/signatures/2.55.6/linux-arm64/bin/werf.sig))
* [macOS amd64](https://tuf.werf.io/targets/releases/2.55.6/darwin-amd64/bin/werf) ([PGP signature](https://tuf.werf.io/targets/signatures/2.55.6/darwin-amd64/bin/werf.sig))
* [macOS arm64](https://tuf.werf.io/targets/releases/2.55.6/darwin-arm64/bin/werf) ([PGP signature](https://tuf.werf.io/targets/signatures/2.55.6/darwin-arm64/bin/werf.sig))
* [Windows amd64](https://tuf.werf.io/targets/releases/2.55.6/windows-amd64/bin/werf.exe) ([PGP signature](https://tuf.werf.io/targets/signatures/2.55.6/windows-amd64/bin/werf.exe.sig))

These binaries were signed with PGP and could be verified with the [werf PGP public key](https://werf.io/werf.asc). For example, `werf` binary can be downloaded and verified with `gpg` on Linux with these commands:
```shell
curl -sSLO "https://tuf.werf.io/targets/releases/2.55.6/linux-amd64/bin/werf" -O "https://tuf.werf.io/targets/signatures/2.55.6/linux-amd64/bin/werf.sig"
curl -sSL https://werf.io/werf.asc | gpg --import
gpg --verify werf.sig werf
```
