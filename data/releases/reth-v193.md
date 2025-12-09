# Reth - v1.9.3

**Release Name**: Reth v1.9.3
**Published**: 2025-11-18T15:39:24Z
**Repository**: https://github.com/paradigmxyz/reth

---

![image](https://raw.githubusercontent.com/paradigmxyz/reth/main/assets/reth-prod.png)

This is on opstack patch release on top of [v1.9.2](https://github.com/paradigmxyz/reth/releases/tag/v1.9.2) that contains fix for rollup boost that includes the new jovian fields in the payload id (https://github.com/paradigmxyz/reth/pull/19726)
Also updates the superchan registry with updated timestamps for jovian and isthmus (e.g. worldchain isthmus: https://github.com/ethereum-optimism/superchain-registry/pull/1149)
This release is recommended for opstack sepolia where jovian activates Wed 19 Nov 2025 16:00:01 UTC

For fusaka support info see also [v1.9.0](https://github.com/paradigmxyz/reth/releases/tag/v1.9.1)

## Summary

Add a summary, including:

- Critical bug fixes
- New features
- Any breaking changes (and what to expect)

## Update Priority

This table provides priorities for which classes of users should update particular components.

| User Class           | Priority        |
|----------------------|-----------------|
| Payload Builders     | low |
| Non-Payload Builders | low    |

*See [Update Priorities](https://reth.rs/installation/priorities) for more information about this table.*

## All Changes

- chore: bump version v1.9.3 (#19831)
- chore(op-reth/scr): update superchain-registry (#19806)
- fix: add minbasefee for jovian attributes (#19726)

## Binaries

[See pre-built binaries documentation.](https://reth.rs/installation/binaries)

The binaries are signed with the PGP key: `50FB 7CC5 5B2E 8AFA 59FE 03B7 AA5E D56A 7FBF 253E`

### Reth

| System | Architecture | Binary | PGP Signature |
|:---:|:---:|:---:|:---|
| <img src="https://www.svgrepo.com/download/473700/linux.svg" width="50"/> | x86_64 | [reth-v1.9.3-x86_64-unknown-linux-gnu.tar.gz](https://github.com/paradigmxyz/reth/releases/download/v1.9.3/reth-v1.9.3-x86_64-unknown-linux-gnu.tar.gz) | [PGP Signature](https://github.com/paradigmxyz/reth/releases/download/v1.9.3/reth-v1.9.3-x86_64-unknown-linux-gnu.tar.gz.asc) |
| <img src="https://www.svgrepo.com/download/473700/linux.svg" width="50"/> | aarch64 | [reth-v1.9.3-aarch64-unknown-linux-gnu.tar.gz](https://github.com/paradigmxyz/reth/releases/download/v1.9.3/reth-v1.9.3-aarch64-unknown-linux-gnu.tar.gz) | [PGP Signature](https://github.com/paradigmxyz/reth/releases/download/v1.9.3/reth-v1.9.3-aarch64-unknown-linux-gnu.tar.gz.asc) |
| <img src="https://www.svgrepo.com/download/513083/windows-174.svg" width="50"/> | x86_64 | [reth-v1.9.3-x86_64-pc-windows-gnu.tar.gz](https://github.com/paradigmxyz/reth/releases/download/v1.9.3/reth-v1.9.3-x86_64-pc-windows-gnu.tar.gz) | [PGP Signature](https://github.com/paradigmxyz/reth/releases/download/v1.9.3/reth-v1.9.3-x86_64-pc-windows-gnu.tar.gz.asc) |
| <img src="https://www.svgrepo.com/download/511330/apple-173.svg" width="50"/> | x86_64 | [reth-v1.9.3-x86_64-apple-darwin.tar.gz](https://github.com/paradigmxyz/reth/releases/download/v1.9.3/reth-v1.9.3-x86_64-apple-darwin.tar.gz) | [PGP Signature](https://github.com/paradigmxyz/reth/releases/download/v1.9.3/reth-v1.9.3-x86_64-apple-darwin.tar.gz.asc) |
| <img src="https://www.svgrepo.com/download/511330/apple-173.svg" width="50"/> | aarch64 | [reth-v1.9.3-aarch64-apple-darwin.tar.gz](https://github.com/paradigmxyz/reth/releases/download/v1.9.3/reth-v1.9.3-aarch64-apple-darwin.tar.gz) | [PGP Signature](https://github.com/paradigmxyz/reth/releases/download/v1.9.3/reth-v1.9.3-aarch64-apple-darwin.tar.gz.asc) |
| <img src="https://www.svgrepo.com/download/473589/docker.svg" width="50"/> | Docker | [paradigmxyz/reth](https://ghcr.io/paradigmxyz/reth) | - |

### OP-Reth

| System | Architecture | Binary | PGP Signature |
|:---:|:---:|:---:|:---|
| <img src="https://www.svgrepo.com/download/473700/linux.svg" width="50"/> | x86_64 | [op-reth-v1.9.3-x86_64-unknown-linux-gnu.tar.gz](https://github.com/paradigmxyz/reth/releases/download/v1.9.3/op-reth-v1.9.3-x86_64-unknown-linux-gnu.tar.gz) | [PGP Signature](https://github.com/paradigmxyz/reth/releases/download/v1.9.3/op-reth-v1.9.3-x86_64-unknown-linux-gnu.tar.gz.asc) |
| <img src="https://www.svgrepo.com/download/473700/linux.svg" width="50"/> | aarch64 | [op-reth-v1.9.3-aarch64-unknown-linux-gnu.tar.gz](https://github.com/paradigmxyz/reth/releases/download/v1.9.3/op-reth-v1.9.3-aarch64-unknown-linux-gnu.tar.gz) | [PGP Signature](https://github.com/paradigmxyz/reth/releases/download/v1.9.3/op-reth-v1.9.3-aarch64-unknown-linux-gnu.tar.gz.asc) |
| <img src="https://www.svgrepo.com/download/513083/windows-174.svg" width="50"/> | x86_64 | [op-reth-v1.9.3-x86_64-pc-windows-gnu.tar.gz](https://github.com/paradigmxyz/reth/releases/download/v1.9.3/op-reth-v1.9.3-x86_64-pc-windows-gnu.tar.gz) | [PGP Signature](https://github.com/paradigmxyz/reth/releases/download/v1.9.3/op-reth-v1.9.3-x86_64-pc-windows-gnu.tar.gz.asc) |
| <img src="https://www.svgrepo.com/download/511330/apple-173.svg" width="50"/> | x86_64 | [op-reth-v1.9.3-x86_64-apple-darwin.tar.gz](https://github.com/paradigmxyz/reth/releases/download/v1.9.3/op-reth-v1.9.3-x86_64-apple-darwin.tar.gz) | [PGP Signature](https://github.com/paradigmxyz/reth/releases/download/v1.9.3/op-reth-v1.9.3-x86_64-apple-darwin.tar.gz.asc) |
| <img src="https://www.svgrepo.com/download/511330/apple-173.svg" width="50"/> | aarch64 | [op-reth-v1.9.3-aarch64-apple-darwin.tar.gz](https://github.com/paradigmxyz/reth/releases/download/v1.9.3/op-reth-v1.9.3-aarch64-apple-darwin.tar.gz) | [PGP Signature](https://github.com/paradigmxyz/reth/releases/download/v1.9.3/op-reth-v1.9.3-aarch64-apple-darwin.tar.gz.asc) |
| <img src="https://www.svgrepo.com/download/473589/docker.svg" width="50"/> | Docker | [paradigmxyz/op-reth](https://ghcr.io/paradigmxyz/op-reth) | - |

**Full Changelog**: https://github.com/paradigmxyz/reth/compare/v1.9.2...v1.9.3