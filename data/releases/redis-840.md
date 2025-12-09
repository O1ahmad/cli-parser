# Redis - 8.4.0

**Release Name**: 8.4.0
**Published**: 2025-11-18T15:06:37Z
**Repository**: https://github.com/redis/redis

---

This is the General Availability release of Redis 8.4 in Redis Open Source.

### Major changes compared to 8.2

- [DIGEST](https://redis.io/docs/latest/commands/digest/), [DELEX](https://redis.io/docs/latest/commands/delex/); [SET](https://redis.io/docs/latest/commands/set/) extensions - atomic compare-and-set and compare-and-delete for string keys
- [MSETEX](https://redis.io/docs/latest/commands/msetex/) - atomically set multiple string keys and update their expiration
- [XREADGROUP](https://redis.io/docs/latest/commands/xreadgroup/) - new `CLAIM` option for reading both idle pending and incoming stream entries
- [CLUSTER MIGRATION](https://redis.io/docs/latest/commands/cluster-migration/) - atomic slot migration
- [CLUSTER SLOT-STATS](https://redis.io/docs/latest/commands/cluster-slot-stats/) - per-slot usage metrics: key count, CPU time, and network I/O
- Redis query engine: [FT.HYBRID](https://redis.io/docs/latest/commands/ft.hybrid/) - hybrid search and fused scoring
- Redis query engine: I/O threading with performance boost for search and query commands (`FT.*`) 
- I/O threading: substantial throughput increase (e.g. >30% for caching use cases (10% `SET`, 90% `GET`), 4 cores)
- JSON: substantial memory reduction for homogenous arrays (up to 92%)

### Binary distributions

- Alpine and Debian Docker images - https://hub.docker.com/_/redis
- Install using snap - see https://github.com/redis/redis-snap
- Install using brew - see https://github.com/redis/homebrew-redis
- Install using RPM - see https://github.com/redis/redis-rpm
- Install using Debian APT - see https://github.com/redis/redis-debian


### Operating systems we test Redis 8.4 on

- Ubuntu 22.04 (Jammy Jellyfish), 24.04 (Noble Numbat)
- Rocky Linux 8.10, 9.5
- AlmaLinux 8.10, 9.5
- Debian 12 (Bookworm), Debian 13 (Trixie)
- macOS 13 (Ventura), 14 (Sonoma), 15 (Sequoia)

### Bug fixes (compared to 8.4-RC1)

- #14524 `XREADGROUP CLAIM` returns strings instead of integers
- #14529 Add variable key-spec flags to `SET IF*` and `DELEX`
- [#P928](https://github.com/RedisBloom/RedisBloom/pull/928) Potential memory leak (MOD-11484)
- [#T1801](https://github.com/RedisTimeSeries/RedisTimeSeries/pull/1801), [#T1805](https://github.com/RedisTimeSeries/RedisTimeSeries/pull/1805) macOS build failures (MOD-12293)
- [#J1438](https://github.com/RedisJSON/RedisJSON/pull/1438) `JSON.NUMINCRBY` - wrong result on integer array with non-integer increment (MOD-12282)
- [#J1437](https://github.com/RedisJSON/RedisJSON/pull/1437) Thread safety issue related to ASM and shared strings (MOD-12013)


### Performance and resource utilization improvements (compared to 8.4-RC1)

- #14480, #14516 Optimize `XREADGROUP`

### known bugs and limitations

- When executing `FT.SEARCH`, `FT.AGGREGATE`, `FT.CURSOR`, `FT.HYBRID`, `TS.MGET`, `TS.MRANGE`, `TS.MREVRANGE`, and `TS.QUERYINDEX` while an atomic slot migration process is in progress, the results may be partial or contain duplicates
- `FT.PROFILE`, `FT.EXPLAIN`, and `FT.EXPLACINCLI` do not contain the `FT.HYBRID` option
- Metrics from `FT.HYBRID` command are not displayed on `FT.INFO` and `INFO`
- `FT.HYBRID`: the `EXPLAINSCORE`, `SHARD_K_RATIO`, `YIELD_DISTANCE_AS`, and `WITHCURSOR` options are not supported
- `FT.HYBRID`: post-filtering (after `COMBINE` step) using `FILTER` is not supported
- `FT.HYBRID`: the default response format considers only `key_id` and `score`. This may change for delivering the entire document content
