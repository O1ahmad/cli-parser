# Near Protocol - 2.10.1

**Release Name**: 2.10.1
**Published**: 2025-12-03T18:00:36Z
**Repository**: https://github.com/near/nearcore

---

```
CODE_COLOR: CODE_GREEN_MAINNET
RELEASE_VERSION: 2.10.1
PROTOCOL_UPGRADE: FALSE
DATABASE_UPGRADE: FALSE
SECURITY_UPGRADE: FALSE
```

This release addresses the following issues discovered in [2.10.0](https://github.com/near/nearcore/releases/tag/2.10.0):
- Bug in networking code resulting in decrease in chunk endorsements: fixed in #14739 
- Runtime issue resulting in transactions with duplicate nonces included as part of shard chunks: fixed in #14747

While this release is marked as CODE_GREEN, it contains important stability and reliability improvements for nodes during both binary and protocol upgrades. We strongly encourage all node operators to apply this patch.