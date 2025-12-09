# Cadence Workflow - v1.3.7-prerelease23

**Release Name**: v1.3.7-prerelease23
**Published**: 2025-12-08T22:50:32Z
**Repository**: https://github.com/cadence-workflow/cadence

---

## What's Changed
* chore(shard-distirbutor): extend info to debug assignment conflicts by @eleonoradgr in https://github.com/cadence-workflow/cadence/pull/7506
* feat(shard-distributor): Add ping verification to ephemeral shard creator by @jakobht in https://github.com/cadence-workflow/cadence/pull/7496
* fix(shard-distributor): add context timeout into the shard rebalancing loop by @arzonus in https://github.com/cadence-workflow/cadence/pull/7514
* chore(shard-distributor): increase observability of the leader election and the leader processor by @arzonus in https://github.com/cadence-workflow/cadence/pull/7515
* fix(shard-distributor): remove storing AssignedState.ModRevision to etcd by @arzonus in https://github.com/cadence-workflow/cadence/pull/7516
* chore: change logger to warn for nil mutable state in executeDeleteHistoryEventTask by @fimanishi in https://github.com/cadence-workflow/cadence/pull/7509
* feat(docker): add docker-compose configuration for OpenSearch by @Bueller87 in https://github.com/cadence-workflow/cadence/pull/7510


**Full Changelog**: https://github.com/cadence-workflow/cadence/compare/v1.3.7-prerelease21...v1.3.7-prerelease23