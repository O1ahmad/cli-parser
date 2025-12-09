# Hardhat - hardhat@3.0.16

**Release Name**: Hardhat v3.0.16
**Published**: 2025-11-27T18:30:06Z
**Repository**: https://github.com/NomicFoundation/hardhat

---

This release adds support for the [Fusaka hardfork](https://forkcast.org/upgrade/fusaka).

### Changes

- 478ee07: Bumped EDR version to [`0.12.0-next.16`](https://www.npmjs.com/package/@nomicfoundation/edr/v/0.12.0-next.16)
  - Added support for Osaka hardfork
  - Added full support for OP stack Isthmus hardfork
- 806ee5a: Fixed an issue caused by networks that don't implement `eth_feeHistory` correctly (https://github.com/NomicFoundation/hardhat/pull/7678)
- f4b7f7e: Fix: use user config provided value for `defaultChainType` ([#7700](https://github.com/NomicFoundation/hardhat/issues/7700))
- 6b2ed9a: Add ability for task options to be hidden from the CLI ([#7426](https://github.com/NomicFoundation/hardhat/issues/7426))
- 6d10d05: Update `hardfork` validation and resolution to use `defaultChainType` when `chainType` is undefined ([#7700](https://github.com/NomicFoundation/hardhat/issues/7700))

---
> 💡 **The Nomic Foundation is hiring! Check [our open positions](https://www.nomic.foundation/jobs).**
---