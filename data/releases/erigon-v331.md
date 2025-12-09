# Erigon - v3.3.1

**Release Name**: v3.3.1 - Rocky Romp
**Published**: 2025-12-07T03:34:21Z
**Repository**: https://github.com/erigontech/erigon

---


- We have new Docs and HelpCenter: https://docs.erigon.tech/
- Support of historical `eth_getProof` (https://github.com/erigontech/erigon/issues/12984). It requires
  `--prune.include-commitment-history` flag.


#### RPC
* rpc: fix txpool_content crash: unknown by @canepat in https://github.com/erigontech/erigon/pull/18120

#### CL
* Caplin: Simplified peer refreshing (#18123) by @domiwei in https://github.com/erigontech/erigon/pull/18152

#### TxPool
* txpool: remove double PopWorst() in pending pool overflow by @AskAlexSharov in https://github.com/erigontech/erigon/pull/18159

#### Sync
* Torrent client fixes by @anacrolix in https://github.com/erigontech/erigon/pull/18179


**Full Changelog**: https://github.com/erigontech/erigon/compare/v3.3.0...v3.3.1