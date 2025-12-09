# Prysm - v7.0.1

**Release Name**: v7.0.1
**Published**: 2025-12-08T20:09:29Z
**Repository**: https://github.com/prysmaticlabs/prysm

---

## [v7.0.1](https://github.com/prysmaticlabs/prysm/compare/v7.0.0...v7.0.1) - 2025-12-08

This patch release contains 4 cherry-picked changes to address the mainnet attestation processing issue from 2025-12-04. Operators are encouraged to update to this release as soon as practical. As of this release, the feature flag `--disable-last-epoch-targets` has been deprecated and can be safely removed from your node configuration. 

A post mortem doc with full details is expected to be published later this week.

### Changed

- Move the "Not enough connected peers" (for a given subnet) from WARN to DEBUG. [[PR]](https://github.com/prysmaticlabs/prysm/pull/16087)
- Use dependent root instead of target when possible. [[PR]](https://github.com/prysmaticlabs/prysm/pull/15996)
- Introduced flag `--ignore-unviable-attestations` (replaces and deprecates `--disable-last-epoch-targets`) to drop attestations whose target state is not viable; default remains to process them unless explicitly enabled. [[PR]](https://github.com/prysmaticlabs/prysm/pull/16094)

### Fixed

- Use head state to validate attestations for old blocks if they are compatible. [[PR]](https://github.com/prysmaticlabs/prysm/pull/16095)