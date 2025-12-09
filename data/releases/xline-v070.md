# Xline - v0.7.0

**Release Name**: Release v0.7.0
**Published**: 2024-08-26T11:11:20Z
**Repository**: https://github.com/xline-kv/Xline

---

## :star: New Features

- [Feature]CURP WAL (Write-Ahead-Log) implementation：We designed a Write-Ahead-Log to persist log entries for curp.
- [Feature]Deduplication：Implements command deduplication using the exactly-once semantics from the [RIFL](https://web.stanford.edu/~ouster/cgi-bin/papers/rifl.pdf) paper.
- [Feature]: Snapshot Restore [#630](https://github.com/xline-kv/Xline/actions/runs/10570897780/job/29286109247#step:4:31)](https://github.com/xline-kv/Xline/issues/630)
- [Feature]: Interface of maintenance server [#543](https://github.com/xline-kv/Xline/issues/543)
- [Feature]: Support run with tls [#[32](https://github.com/xline-kv/Xline/actions/runs/10570897780/job/29286109247#step:4:33)8](https://github.com/xline-kv/Xline/issues/328)

## :hammer_and_wrench: Refactor

- [Refactor]: Add a session structure to renew lock lease automatically  [#684](https://github.com/xline-kv/Xline/issues/684)
- [Refactor]: startup process [#629](https://github.com/xline-kv/Xline/issues/629)
- [Refactor]: Refactor the GC of speculative pool [#439](https://github.com/xline-kv/Xline/issues/439)
- [Refactor]:New command execution logic: We removed the cmd workers and related command execution logic. Now Xline will use serial execution (with batch) to prevent lock contention.
- [Refactor]: Garbage Collection: We refactored the garbage collection logic based on the dedup implementation.
- [Refactor]:Client Propose Optimization:  We refactored the curp client to use gRPC stream to send a propose to the cluster. This reduces the load of the gRPC server and improves the overall performance.
- [Refactor]: Conflict Detection:  We removed the conflict checked mpmc. Now Xline will use the conflict pools (speculative pool and uncommitted pool) to detect command conflicts.
- [Refactor]: Read Index: We implemented the Read Index mechanism from the Raft paper for read-only commands. Replacing the previous Read State implementation.
- [Refactor]: xline-client Refactor: We switched to a more intuitive user interface for the xline-client crate.
- [Refactor]: Various performance optimizations

## :beetle: Bug Fixes

- [Bug]: Implement ReadIndex [#870](https://github.com/xline-kv/Xline/issues/870)
- [etcdapi] [Bug]: Repeated revision [#848](https://github.com/xline-kv/Xline/issues/848)
- [Bug]: The test case curp::it server::shutdown_rpc_should_shutdown_the_cluster failed [#774](https://github.com/xline-kv/Xline/issues/774)
- [Bug]: Xline will loss event when using watch feature [#677](https://github.com/xline-kv/Xline/issues/677)
- [Bug]: The xlinectl won't renew the lease of the lock key [#664](https://github.com/xline-kv/Xline/issues/664)
- [Bug]: Failed to add a new member node4 to a three-nodes xline cluster [#661](https://github.com/xline-kv/Xline/issues/661)
- [Refactor]: read-only command during revision generation [#502](https://github.com/xline-kv/Xline/issues/502)
- [Bug]: Read different values in execute during read state [#501](https://github.com/xline-kv/Xline/issues/501)
- [Bug]: sync txn request does not execute in the order of child request [#498](https://github.com/xline-kv/Xline/issues/498)
- [Bug]: Read State [#497](https://github.com/xline-kv/Xline/issues/497)
- [Bug]: revision generation [#491](https://github.com/xline-kv/Xline/issues/491), [#848](https://github.com/xline-kv/Xline/issues/848)
- [Bug]: requests in a single txn do not execute in sequence [#471](https://github.com/xline-kv/Xline/issues/471)
- [Bug]: batch_index in raw_curp will overflow eventually [#368](https://github.com/xline-kv/Xline/issues/368)
- [Bug]: Fix GC may break the CURP durability [#159](https://github.com/xline-kv/Xline/issues/159)

## :writing_hand: Known Issues
During benchmark if the cluster is under high load, the cluster may sometimes not be able to make progress due to deduplication mechanism.

## :boom: Breaking Changes
- etcd compative APIs will now use 2-RTTs operations to prevent revision generation issues.

## :heart: Contributors

We'd like to thank all the contributors who worked on this release!

- [@themanforfree](https://github.com/themanforfree)
- [@iGxnon](https://github.com/iGxnon)
- [@Phoenix500526](https://github.com/Phoenix500526)
- [@bsbds](https://github.com/bsbds)