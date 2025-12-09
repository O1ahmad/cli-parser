# Sui - devnet-v1.62.0

**Release Name**: devnet-v1.62.0
**Published**: 2025-12-08T20:41:05Z
**Repository**: https://github.com/MystenLabs/sui

---

## Protocol
#### Sui Protocol Version in this release: `104`

https://github.com/MystenLabs/sui/pull/24239: 104 - update CoinMetadata post updates in Coin in 103

## Nodes (Validators and Full nodes)
https://github.com/MystenLabs/sui/pull/24420: Disable using Quorum Driver for transaction submission. Setting `TRANSACTION_DRIVER` env var is now a no-op.

## JSON-RPC

https://github.com/MystenLabs/sui/pull/23737: This PR, in tandem with [https://github.com/MystenLabs/sui/pull/24192](https://github.com/MystenLabs/sui/pull/24192), unifies how indexers determine their ingestion starting point and introduce watermark-gated backfill tasks.

1. `--skip-watermark` is removed, and the previous ability to bypass
watermark safety checks for concurrent pipelines is no longer supported.
2. `--first-checkpoint` no longer forces the indexer to start ingesting
from the configured checkpoint. The indexer now always determines its
starting ingestion point as the minimum next checkpoint across all
pipelines to resume processing from. From this release,
`--first-checkpoint` now only applies to pipelines that do not yet have
a committer watermark. These pipelines will resume processing from the
configured value. Pipelines with existing watermarks will always resume
processing from their own next checkpoint.
3. A new mechanism, watermark tasks, allows operators to run the same
pipelines on multiple indexer instances for historical backfilling. Two
new flags, `--task` and `--reader-interval-ms`, enable this mechanism.
These flags create a tasked indexer whose pipelines commit checkpoint
data as long as the checkpoint is not below the `reader_lo` watermark of
their corresponding main pipelines. The indexer controls how frequently
these tasked pipelines poll the main pipelines' watermarks
per `--reader-interval-ms`.

Migration guidance:  
1. If you use `--first-checkpoint` only for _initial_ ingestion of a
fresh pipeline, no further action is needed.
2. If you previously used `--first-checkpoint` and
optionally `--skip-watermark` to backfill existing tables, you can
achieve the same workflow by starting a new indexer instance with a
configured `--task`, `--reader-interval-ms`, and `--first-checkpoint`.
3. Like `--skip-watermark`, `--task` cannot be used to run sequential
pipelines.

## GraphQL

https://github.com/MystenLabs/sui/pull/24319: Fixes a bug where the transaction payloads that were part of `simulateTransaction` calls were incorrectly classified as part of the query payload (and therefore subject to a lower payload size limit).

https://github.com/MystenLabs/sui/pull/23928: Removed `events` field from `SimulationResult`. Events are now only accessible via `effects.events()` to eliminate redundancy.

https://github.com/MystenLabs/sui/pull/23929: Returns `null` for simulated/executed transactions timestamp as they are not included in a checkpoint.

https://github.com/MystenLabs/sui/pull/24486: Validate types and fields passed into AvailableRange queries.

## CLI

https://github.com/MystenLabs/sui/pull/24367:
- Refactored `sui validator` commands to use a shared
[TxProcessingArgs](cci:2://file:///Users/jnaulty/github/mystenlabs/sui/crates/sui/src/client_commands.rs:693:0-721:1)
struct for transaction arguments, improving consistency with `sui
client`. Updated `serialize_unsigned_transaction` help text to provide
clearer instructions for offline signing.

---
#### Full Log: https://github.com/MystenLabs/sui/commits/devnet-v1.62.0
