# Arbitrum - v3.9.4-rc.2

**Release Name**: Arbitrum Nitro v3.9.4-rc.2
**Published**: 2025-12-04T22:22:47Z
**Repository**: https://github.com/OffchainLabs/nitro

---

Nitro `v3.9.4` is an optional release, only minor updates on top of `v3.9.3`.

This release is available as a Docker Image on Docker Hub at offchainlabs/nitro-node:v3.9.4-rc.2-7f582c3
This Docker image specifies default flags in its entrypoint which should be replicated if you're overriding the entrypoint: /usr/local/bin/nitro --validation.wasm.allowed-wasm-module-roots /home/user/nitro-legacy/machines,/home/user/target/machines

Important for any chains still on ArbOS40: If you're running a validator without a split validation server (this will be true of most validators), you should instead use the image offchainlabs/nitro-node:v3.9.4-rc.2-7f582c3-validator which has the extra script /usr/local/bin/split-val-entry.sh as the entrypoint (no need to override the default entrypoint).

## Configuration Changes
* `--node.batch-poster.data-poster.enable-cell-proofs` has been removed
* `--parent-chain.blob-client.use-legacy-endpoint` has been removed

## What's Changed
Fix to store blobs locally post fusaka, and add disk reader that can use locally stored blobs.  Also, remove legacy blob functionality that is no longer needed now that Fusaka is live.

## User-facing Changes
* Remove legacy blob support, store blobs locally: https://github.com/OffchainLabs/nitro/pull/4113


**Full Changelog**: https://github.com/OffchainLabs/nitro/compare/v3.9.4-rc.1...v3.9.4-rc.2