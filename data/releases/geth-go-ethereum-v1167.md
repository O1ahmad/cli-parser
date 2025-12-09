# Geth (go-ethereum) - v1.16.7

**Release Name**: Ballistic Drift Stabilizer (v1.16.7)
**Published**: 2025-11-04T12:28:55Z
**Repository**: https://github.com/ethereum/go-ethereum

---

<!-- Ballistic Drift Stabilizer (v1.16.7) -->

This is a re-roll of v1.16.6, including an important fix in the KZG cryptography library.

**This release enables the Fusaka hardfork on Ethereum mainnet**.

The Fusaka fork is scheduled to occur at `2025-12-03 21:49:11 UTC`.
Please upgrade your node to v1.16.7 in time for the fork.

This release also enables two blob-parameter-only (BPO) upgrades.
These upgrades change protocol parameters to increase the available blob capacity.

- BPO1 on`2025-12-09`
- BPO2 on `2026-01-07`

### Fusaka

* Set mainnet timestamps for Osaka ([#33063](https://github.com/ethereum/go-ethereum/pull/33063))
* Enable Fusaka for `geth --dev` mode ([#32917](https://github.com/ethereum/go-ethereum/pull/32917))

### RPC

* Add `eth_sendRawTransactionSync` which waits until either a timeout or the transaction is mined. This feature is mostly useful on L2s with lower blocktimes. ([#32830](https://github.com/ethereum/go-ethereum/pull/32830), [#32930](https://github.com/ethereum/go-ethereum/pull/32930), [#32929](https://github.com/ethereum/go-ethereum/pull/32929/))
* Add support for `eth_simulateV1` in ethclient ([#32856](https://github.com/ethereum/go-ethereum/pull/32856))
* Fix for an issue that might crash `debug_traceCall` ([#33015](https://github.com/ethereum/go-ethereum/pull/33015))
* Fix for an issuer where local transactions were not persisted to the journal ([#32921](https://github.com/ethereum/go-ethereum/pull/32921))

### Core

* Fix for a cryptographic [vulnerability in c-kzg-4844](https://github.com/ethereum/c-kzg-4844/pull/607). This is only exploitable post-Fusaka. ([#33093](https://github.com/ethereum/go-ethereum/pull/33093))
* Add `geth --genesis` flag as an alternative to running `geth init genesis.json` ([#32844](https://github.com/ethereum/go-ethereum/pull/32844))
* Fix for receipt insertion during ERA file import. ([#32934](https://github.com/ethereum/go-ethereum/pull/32934))
* Work on getting the trie node history in order to serve historical `eth_getProof` request with the new path-based archive node. ([#32907](https://github.com/ethereum/go-ethereum/pull/32907), [#32914](https://github.com/ethereum/go-ethereum/pull/32914), [#32937](https://github.com/ethereum/go-ethereum/pull/32937))
* Further work on cmd/keeper, our guest program for zkVMs ([#32816](https://github.com/ethereum/go-ethereum/pull/32816))
* Various optimizations ([#32971](https://github.com/ethereum/go-ethereum/pull/32971), [#32916](https://github.com/ethereum/go-ethereum/pull/32916), [#32965](https://github.com/ethereum/go-ethereum/pull/32965), [#32946](https://github.com/ethereum/go-ethereum/pull/32946))

### Networking

* New metrics for tracking slow peers ([#32964](https://github.com/ethereum/go-ethereum/pull/32964))
* Fix for an issue where disconnected peers were not removed in txFetcher ([#32947](https://github.com/ethereum/go-ethereum/pull/32947))

---

For a full rundown of the changes please consult the Geth [1.16.6](https://github.com/ethereum/go-ethereum/milestone/195?closed=1) and [1.16.7](https://github.com/ethereum/go-ethereum/milestone/195?closed=1) release milestones.

As with all our previous releases, you can find the:

- Pre-built binaries for all platforms on our [downloads page](https://geth.ethereum.org/downloads/).
- Docker images published under [`ethereum/client-go`](https://hub.docker.com/r/ethereum/client-go) (use "stable" tag).
- Ubuntu packages in our [Launchpad PPA repository](https://launchpad.net/~ethereum/+archive/ubuntu/ethereum).
- macOS packages in our [Homebrew Tap repository](https://github.com/ethereum/homebrew-ethereum).
