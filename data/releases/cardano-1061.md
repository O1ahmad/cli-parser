# Cardano - 10.6.1

**Release Name**: 10.6.1
**Published**: 2025-12-02T10:01:42Z
**Repository**: https://github.com/IntersectMBO/cardano-node

---

*IMPORTANT* If you're building from source you *must* upgrade to [libblst 0.3.14](https://github.com/supranational/blst/releases/tag/v0.3.14).

** This version includes the hot fix in cardano-crypto-class addressing an issue with hash sizes**

# Technical Specification

<details open>
  <summary>Minimum System Requirements</summary>

- An Intel or AMD x86 processor with two or more cores, at 1.6GHz or faster (2GHz or faster for a stake pool or relay)
- Or, for MacOS, an Apple Silicon (M1, M2, M3 or M4) processor
- 24GB of RAM when running with the `InMemory` backend, 8GB when running with the `OnDisk` backend (pending confirmation)
- 300GB of free storage (350GB recommended for future growth)

</details>

<details>
  <summary>Platforms</summary>

- Linux 64-bit (Ubuntu 20.04 LTS, 22.04 LTS, 24.04 LTS, 26.04 LTS; Mint 20, 21, 21.1, 21.2, 21.3, 22, 22.1, 22.2; Debian 11, 12, 13)
- Windows 64-bit (10, 11)
- MacOS 10.15, 11 (Big Sur), 12 (Monterey), 13 (Ventura), 14 (Sonoma), 15 (Sequoia), 26 (Tahoe)

</details>

<details open>
  <summary>GHC/Cabal supported versions</summary>

- GHC 9.6
- Cabal 3.8/3.12

</details>

<details>
  <summary>Supported roles</summary>

Platform | Block Production | Relay           | Client (Desktop)
-------- | :--------------: | :-------------: | :--------------:
Linux    | :green_circle:   | :green_circle:  | :green_circle:
Windows  | :red_square:     | :red_square:    | :green_circle:
MacOS    | :red_square:     | :red_square:    | :green_circle:

</details>

<details open>
  <summary>Downloads</summary>

- [Pre-release configuration files](https://book.play.dev.cardano.org/advanced.html)
- Docker Images: [cardano-node](https://github.com/orgs/IntersectMBO/packages/container/cardano-node/591034516?tag=10.6.1), [cardano-tracer](https://github.com/IntersectMBO/cardano-node/pkgs/container/cardano-tracer/591034882?tag=10.6.1), [cardano-submit-api](https://github.com/IntersectMBO/cardano-node/pkgs/container/cardano-submit-api/591034693?tag=10.6.1)

</details>

# Documentation

- [Cardano Node documentation](https://docs.cardano.org/cardano-components/cardano-node)
  - For details about changes to configuration for `UTxO-HD` please refer to the [Consensus docs on UTxO-HD](https://ouroboros-consensus.cardano.intersectmbo.org/docs/references/miscellaneous/utxo-hd/)
  - The [getting started guide](https://developers.cardano.org/docs/get-started/) may also be helpful for general queries.
  - Networking options and related changes are listed on the [P2P section](https://developers.cardano.org/docs/operate-a-stake-pool/node-operations/topology)
- [Cardano CLI](https://github.com/IntersectMBO/cardano-cli/tree/cardano-cli-10.8.0.0)
- Internal API docs for [ledger](https://cardano-ledger.cardano.intersectmbo.org/), [consensus](https://ouroboros-consensus.cardano.intersectmbo.org/haddocks/) and [network](https://ouroboros-network.cardano.intersectmbo.org/)
- [Compatibility matrix](https://docs.cardano.org/developer-resources/release-notes/comp-matrix)

# Sign-off

<!-- Signatures of people responsible for the release -->
Role                                     | Approval
---------------------------------------- | :------------:
Technical Steering Committee (Intersect) |  :green_circle:
Product Committee (Intersect)            |  🟢 
Test Engineer                            |  N/A 
Performance Engineer                     |  :green_circle:
Site Reliability Engineer                | N/A
Release Engineer                         |   :green_circle:

<details>
  <summary>Legend</summary>

  * :green_circle: - signed / agreed / supported
  * :red_square: - not agreed / unsupported

</details>