# Lighthouse - v8.0.1

**Release Name**: BugAnne
**Published**: 2025-11-20T03:32:43Z
**Repository**: https://github.com/sigp/lighthouse

---

## Summary

This is a hotfix release addressing several bugs and performance issues discovered in v8.0.0.

Notable changes:
* From the Fulu fork, checkpoint blobs will no longer be downloaded from the checkpoint server and instead they will be fetched from p2p peers. The [getBlobSidcars](https://ethereum.github.io/beacon-APIs/?urls.primaryName=dev#/Beacon/getBlobSidecars) Beacon API is deprecated from Fulu and clients may drop support in future releases. (#8413, #8417)
* Prevent unnecessary state advances pre-Fulu. This improves beacon node performance prior to the Fulu fork. (#8388)
* Fix rare custody context initialization race condition that could cause panics. (#8391)

As a reminder,  all mainnet users **must upgrade** to either v8.0.0 or v8.0.1 prior to the Fulu fork at epoch 411,392 (**2025-12-03, 21:49 UTC**). You must also update your execution client (e.g. Geth, Nethermind, Erigon, Besu or Reth).

For users upgrading from v7.x.x, please see v8.0.0 release notes [here](https://github.com/sigp/lighthouse/releases/tag/v8.0.0).

## Update Priority

This table provides priorities for which classes of users should update particular components.

|User Class |Beacon Node  | Validator Client|
--- | --- | ---
|Staking Users| Medium | Low |
|Non-Staking Users| Low|---|

*See [Update Priorities](https://lighthouse-book.sigmaprime.io/installation_priorities.html) for more information about this table.*

## All Changes

- Release v8.0.1 (#8414)
- Reimport the checkpoint sync block (#8417)
- Fix md format (#8434)
- Compute missing_columns correctly (#8425)
- Fix custody context initialization race condition that caused panic (#8391)
- Do not require blobs from checkpoint servers from Fulu epochs. (#8413)
- Fix tracing span for execution payload verif (#8419)
- re-targeting of `remove-windows-ci` against `release-v8.0` (#8406)
- Prevent unnecessary state advances pre-Fulu (#8388)

## Binaries

[See pre-built binaries documentation.](https://lighthouse-book.sigmaprime.io/installation_binaries.html)

The binaries are signed with Sigma Prime's PGP key: `15E66D941F697E28F49381F426416DC3F30674B0`

| System | Architecture | Binary | PGP Signature |
|:---:|:---:|:---:|:---|
| <picture> <source media="(prefers-color-scheme: dark)" srcset="https://cdn.simpleicons.org/apple/white" > <source media="(prefers-color-scheme: light)" srcset="https://cdn.simpleicons.org/apple" ><img src="https://cdn.simpleicons.org/apple" width="32" alt="Apple logo">  </picture> | aarch64 | [lighthouse-v8.0.1-aarch64-apple-darwin.tar.gz](https://github.com/sigp/lighthouse/releases/download/v8.0.1/lighthouse-v8.0.1-aarch64-apple-darwin.tar.gz) | [PGP Signature](https://github.com/sigp/lighthouse/releases/download/v8.0.1/lighthouse-v8.0.1-aarch64-apple-darwin.tar.gz.asc) |
| <picture> <source media="(prefers-color-scheme: dark)" srcset="https://cdn.simpleicons.org/linux/white" > <source media="(prefers-color-scheme: light)" srcset="https://cdn.simpleicons.org/linux/black" ><img src="https://cdn.simpleicons.org/linux" width="32" alt="Linux logo"> </picture> | x86_64 | [lighthouse-v8.0.1-x86_64-unknown-linux-gnu.tar.gz](https://github.com/sigp/lighthouse/releases/download/v8.0.1/lighthouse-v8.0.1-x86_64-unknown-linux-gnu.tar.gz) | [PGP Signature](https://github.com/sigp/lighthouse/releases/download/v8.0.1/lighthouse-v8.0.1-x86_64-unknown-linux-gnu.tar.gz.asc) |
| <picture> <source media="(prefers-color-scheme: dark)" srcset="https://cdn.simpleicons.org/raspberrypi/white" > <source media="(prefers-color-scheme: light)" srcset="https://cdn.simpleicons.org/raspberrypi/black" > <img src="https://cdn.simpleicons.org/raspberrypi" width="32" alt="Raspberrypi logo"> </picture> | aarch64 | [lighthouse-v8.0.1-aarch64-unknown-linux-gnu.tar.gz](https://github.com/sigp/lighthouse/releases/download/v8.0.1/lighthouse-v8.0.1-aarch64-unknown-linux-gnu.tar.gz) | [PGP Signature](https://github.com/sigp/lighthouse/releases/download/v8.0.1/lighthouse-v8.0.1-aarch64-unknown-linux-gnu.tar.gz.asc) |
| | | | |
| **System** | **Option** | - | **Resource** |
| <picture> <source media="(prefers-color-scheme: dark)" srcset="https://cdn.simpleicons.org/docker/white" > <source media="(prefers-color-scheme: light)" srcset="https://cdn.simpleicons.org/docker/black" > <img src="https://cdn.simpleicons.org/docker/black" width="32" alt="Docker logo"></picture>  | Docker | [v8.0.1](https://hub.docker.com/r/sigp/lighthouse/tags?page=1&ordering=last_updated&name=v8.0.1) | [sigp/lighthouse](https://hub.docker.com/r/sigp/lighthouse) |
