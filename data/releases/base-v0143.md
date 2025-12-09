# Base - v0.14.3

**Release Name**: v0.14.3
**Published**: 2025-11-24T18:18:45Z
**Repository**: https://github.com/base-org/node

---

### ❗ Mandatory update for Base Mainnet nodes to support the Jovian upgrade on December 2nd.
Operators of Base Mainnet nodes must upgrade to this release _before_ December 2nd at UTC 16:00:01 UTC (unix timestamp 1764691201). 

### ⚠️ Breaking Changes (same as `v0.14.1`)

Similar to `v0.14.1` which was a mandatory upgrade for Base Sepolia node operators, this release also contains the following change and will be applied to mainnet node operators now as well.

### **`op-reth` Binary Removed, Consolidated into `base-reth-node`**

The separate `op-reth` binary has been **removed** and is no longer available.

All functionality previously provided by `op-reth` has been **consolidated** into the existing **`base-reth-node`** binary.

* **Impact:** If your deployment or scripts explicitly called the `op-reth` binary, you must update them to call **`base-reth-node`** instead.
* **Parameters & Operation:** The `base-reth-node` binary is designed to be **identical** in its command-line parameters and operational behavior to the removed `op-reth`. No parameter changes should be necessary other than the binary name itself.
* **Reasoning:** This consolidation allows us to more easily introduce and manage Base-specific features within a single, unified client binary.

## What's Changed
* chore: updated node-reth, reth by @github-actions[bot] in https://github.com/base/node/pull/661


**Full Changelog**: https://github.com/base/node/compare/v0.14.2...v0.14.3