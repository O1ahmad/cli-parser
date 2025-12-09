# Ganache - v7.9.0

**Release Name**: v7.9.0
**Published**: 2023-07-06T01:26:55Z
**Repository**: https://github.com/trufflesuite/ganache

---

<a id="user-content-v7.9.0-top"></a>

<h4>
  <p align="center">
		<code>&nbsp;<a href="#user-content-v7.9.0-new-features">New&nbsp;Features</a>&nbsp;</code>
<img height="36" width="0" src="https://raw.githubusercontent.com/davidmurdoch/px/master/1px.gif">
		<code>&nbsp;<a href="#user-content-v7.9.0-fixes">Fixes</a>&nbsp;</code>
<img height="36" width="0" src="https://raw.githubusercontent.com/davidmurdoch/px/master/1px.gif">
		<code>&nbsp;<a href="#user-content-v7.9.0-miscellaneous">Miscellaneous</a>&nbsp;</code>
<img height="36" width="0" src="https://raw.githubusercontent.com/davidmurdoch/px/master/1px.gif">
		<code>&nbsp;<a href="#user-content-v7.9.0-changelog">Changelog</a>&nbsp;</code>
  <img height="36" width="0" src="https://raw.githubusercontent.com/davidmurdoch/px/master/1px.gif">
		<code>&nbsp;<a href="#user-content-v7.9.0-known-issues">Known&nbsp;Issues</a>&nbsp;</code>
  <img height="36" width="0" src="https://raw.githubusercontent.com/davidmurdoch/px/master/1px.gif">
		<code>&nbsp;<a href="#user-content-v7.9.0-future-plans">Future&nbsp;Plans</a>&nbsp;</code>
  <img height="36" width="0" src="https://raw.githubusercontent.com/davidmurdoch/px/master/1px.gif">
  </p>
</h4>

---

Presenting the latest version of Ganache! This release brings a couple of important bug fixes and one new feature: the ability to specify a file path for Ganache to write logs to – handy when using detach mode, where the logs are not (yet) available.

If you have some time, we encourage you to browse our [issues](https://github.com/trufflesuite/ganache/issues) to find anything you'd like implemented/fixed sooner. Give them a +1 and we'll use this community feedback to help prioritize what we work on! Or better yet, [open a new issue](https://github.com/trufflesuite/ganache/issues/new) or [open a PR](https://github.com/trufflesuite/ganache/compare) to fix an existing issue.

We've changed 59 files across 14 merged pull requests, tallying 2485 additions and 563 deletions, since our last release.

<a id="user-content-v7.9.0-new-features" ></a>

---

# <p align="center"><a href="#user-content-v7.9.0-new-features"><img alt="New Features" width="auto" src="https://raw.githubusercontent.com/trufflesuite/ganache/release-notes-assets/title-images/new-features.svg"></a></p>

- [feat: add hardfork to cli output (#4343)](#user-content-v7.9.0-new-features-0)
- [feat: allow logs to be written to a file by providing the `--logging.file` argument (#4195)](#user-content-v7.9.0-new-features-1)

---

### <a id="user-content-v7.9.0-new-features-0"></a>feat: add hardfork to cli output (#4343)

Ganache now outputs the hardfork to the console along with the rest of the startup information:

```
Chain
==================
Hardfork: shanghai
Id:       1337
```

<p align="right"><sup><a href="#user-content-v7.9.0-new-features">back to new features</a></sup></p>

### <a id="user-content-v7.9.0-new-features-1"></a>feat: allow logs to be written to a file by providing the `--logging.file` argument (#4195)

Introducing the ability to specify a log file for Ganache to write its logs to. No more sifting through endless terminal output to find that one critical message you need. Just provide a path to your desired log file with `ganache --logging.file <path-to-log-file>`, and you're all set! Now you can sit back, relax, and let Ganache do the heavy lifting while you focus on building awesome applications.

<p align="right"><sup><a href="#user-content-v7.9.0-new-features">back to new features</a></sup></p>

<p align="right"><sup><a href="#user-content-v7.9.0-top">back to top</a></sup></p>

<a id="user-content-v7.9.0-fixes" ></a>

---

# <p align="center"><a href="#user-content-v7.9.0-fixes"><img alt="Fixes" width="auto" src="https://raw.githubusercontent.com/trufflesuite/ganache/release-notes-assets/title-images/fixes.svg"></a></p>

- [fix: show a helpful message when `ganache instances` is executed without a subcommand (#4368)](#user-content-v7.9.0-fixes-0)
- [fix: resolve hardfork for blocks by blocknumber and timestamp (#4455)](#user-content-v7.9.0-fixes-1)
- [fix: add support for `mergeForkIdTransition` (#4463)](#user-content-v7.9.0-fixes-2)
- [fix: ensure clique-signer for PoA networks (#4465)](#user-content-v7.9.0-fixes-3)

---

### <a id="user-content-v7.9.0-fixes-0"></a>fix: show a helpful message when `ganache instances` is executed without a subcommand (#4368)

When `ganache instances` is executed, a subcommand must be provided.
Previously an unhelpful error was thrown, with this fix we output a simple error message, followed by the the help text for `ganache instances`.

```terminal
$ ganache instances
ganache instances requires a subcommand:

ganache instances

Manage instances of Ganache running in detached mode.
(Ganache can be run in detached mode by providing the --detach flag)

Commands:
  ganache instances list         List instances running in detached mode
  ganache instances stop <name>  Stop the instance specified by <name>

Options:
  -?, --help  Show help                                                                           [boolean]
```

fixes: #4360

<p align="right"><sup><a href="#user-content-v7.9.0-fixes">back to fixes</a></sup></p>

### <a id="user-content-v7.9.0-fixes-1"></a>fix: resolve hardfork for blocks by blocknumber and timestamp (#4455)

Starting with Shanghai, hardforks are determined by timestamp, rather than block number. When resolving the hardfork to use for a given block, we now consider the blocknumber and the timestamp.<br/>
fixes: #4450 (in that the correct hardfork is now resolved, which is not `mergeForkIdTransition`)

See #4463

<p align="right"><sup><a href="#user-content-v7.9.0-fixes">back to fixes</a></sup></p>

### <a id="user-content-v7.9.0-fixes-2"></a>fix: add support for `mergeForkIdTransition` (#4463)

Add internal support for `mergeForkIdTransition` "hardfork", which is presently live only on Sepolia, but assumedly will eventually happen on other networks.<br/>
This doesn't add any functionality, but fixes: #4450 for transactions happening on `mergeForkIdTransition` hardfork.

See #4455

<p align="right"><sup><a href="#user-content-v7.9.0-fixes">back to fixes</a></sup></p>

### <a id="user-content-v7.9.0-fixes-3"></a>fix: ensure clique-signer for PoA networks (#4465)

Fixes #4359

<p align="right"><sup><a href="#user-content-v7.9.0-fixes">back to fixes</a></sup></p>

<p align="right"><sup><a href="#user-content-v7.9.0-top">back to top</a></sup></p>

<a id="user-content-v7.9.0-miscellaneous" ></a>

---

# <p align="center"><a href="#user-content-v7.9.0-miscellaneous"><img alt="Miscellaneous" width="auto" src="https://raw.githubusercontent.com/trufflesuite/ganache/release-notes-assets/title-images/miscellaneous.svg"></a></p>

- [docs: update contributing guide for linux (#4358)](#user-content-v7.9.0-miscellaneous-0)
- [chore: use `localhost` as hostname for `docs.preview` dev command (#4357)](#user-content-v7.9.0-miscellaneous-1)
- [test: ensure tests that are skipped in development are run in CI (#4353)](#user-content-v7.9.0-miscellaneous-2)
- [docs: complete macOS node-gyp troubleshooting steps in CONTRIBUTING.md (#4036)](#user-content-v7.9.0-miscellaneous-3)
- [perf: optimize account init logging (#4318)](#user-content-v7.9.0-miscellaneous-4)
- [docs: make light-mode links slightly darker to meet WCAG 2 Level AA contrast goals (#4383)](#user-content-v7.9.0-miscellaneous-5)
- [perf: optimize options normalization (#4317)](#user-content-v7.9.0-miscellaneous-6)
- [docs: preloads docs assets (#4384)](#user-content-v7.9.0-miscellaneous-7)

---

### <a id="user-content-v7.9.0-miscellaneous-0"></a>docs: update contributing guide for linux (#4358)

Python 2.7 is no longer a requirement to build ganache, but `make` is.

<p align="right"><sup><a href="#user-content-v7.9.0-miscellaneous">back to miscellaneous</a></sup></p>

### <a id="user-content-v7.9.0-miscellaneous-1"></a>chore: use `localhost` as hostname for `docs.preview` dev command (#4357)

This is just to make ganache development from WSL easier.

<p align="right"><sup><a href="#user-content-v7.9.0-miscellaneous">back to miscellaneous</a></sup></p>

### <a id="user-content-v7.9.0-miscellaneous-2"></a>test: ensure tests that are skipped in development are run in CI (#4353)

Previously, tests that depend on an INFURA_KEY would be skipped if it were not provided. After this change these tests will fail in CI if no INFURA_KEY is provided.<br/>
Additionally, a test which was previously skipped is now run on Windows and Linux agents in Github Actions only. (` > server > listens on given interface only`)

<p align="right"><sup><a href="#user-content-v7.9.0-miscellaneous">back to miscellaneous</a></sup></p>

### <a id="user-content-v7.9.0-miscellaneous-3"></a>docs: complete macOS node-gyp troubleshooting steps in CONTRIBUTING.md (#4036)

Does what it says on the tin.

<p align="right"><sup><a href="#user-content-v7.9.0-miscellaneous">back to miscellaneous</a></sup></p>

### <a id="user-content-v7.9.0-miscellaneous-4"></a>perf: optimize account init logging (#4318)

Minor performance improvement on startup.

<p align="right"><sup><a href="#user-content-v7.9.0-miscellaneous">back to miscellaneous</a></sup></p>

### <a id="user-content-v7.9.0-miscellaneous-5"></a>docs: make light-mode links slightly darker to meet WCAG 2 Level AA contrast goals (#4383)

Changes the contrast on links on ganache.dev in light mode.

<p align="right"><sup><a href="#user-content-v7.9.0-miscellaneous">back to miscellaneous</a></sup></p>

### <a id="user-content-v7.9.0-miscellaneous-6"></a>perf: optimize options normalization (#4317)

Minor performance improvement on start up.

<p align="right"><sup><a href="#user-content-v7.9.0-miscellaneous">back to miscellaneous</a></sup></p>

### <a id="user-content-v7.9.0-miscellaneous-7"></a>docs: preloads docs assets (#4384)

Reduces page load time on ganache.dev by initiating downloads of assets that will get loaded from other CSS and JS files later.

<p align="right"><sup><a href="#user-content-v7.9.0-miscellaneous">back to miscellaneous</a></sup></p>

<p align="right"><sup><a href="#user-content-v7.9.0-top">back to top</a></sup></p>

<a id="user-content-v7.9.0-changelog" ></a>

---

# <p align="center"><a href="#user-content-v7.9.0-changelog"><img alt="Changelog" width="auto" src="https://raw.githubusercontent.com/trufflesuite/ganache/release-notes-assets/title-images/changelog.svg"></a></p>

- #4358 docs: update contributing guide for linux (@davidmurdoch)
- #4357 chore: use `localhost` as hostname for `docs.preview` dev command (@davidmurdoch)
- #4353 test: ensure tests that are skipped in development are run in CI (@jeffsmale90)
- #4343 feat: add hardfork to cli output (@davidmurdoch)
- #4368 fix: show a helpful message when `ganache instances` is executed without a subcommand (@jeffsmale90)
- #4036 docs: complete macOS node-gyp troubleshooting steps in CONTRIBUTING.md (@OnlyOneJMJQ)
- #4318 perf: optimize account init logging (@davidmurdoch)
- #4383 docs: make light-mode links slightly darker to meet WCAG 2 Level AA contrast goals (@davidmurdoch)
- #4317 perf: optimize options normalization (@davidmurdoch)
- #4195 feat: allow logs to be written to a file by providing the `--logging.file` argument (@jeffsmale90)
- #4455 fix: resolve hardfork for blocks by blocknumber and timestamp (@jeffsmale90)
- #4463 fix: add support for `mergeForkIdTransition` (@jeffsmale90)
- #4465 fix: ensure clique-signer for PoA networks (@davidmurdoch)
- #4384 docs: preloads docs assets (@davidmurdoch)

<p align="right"><sup><a href="#user-content-v7.9.0-top">back to top</a></sup></p>

<a id="user-content-v7.9.0-known-issues" ></a>

---

# <p align="center"><a href="#user-content-v7.9.0-known-issues"><img alt="Known Issues" width="auto" src="https://raw.githubusercontent.com/trufflesuite/ganache/release-notes-assets/title-images/known-issues.svg"></a></p>

### Top Priority:

- interactive documentation's `debug_storageRangeAt` doesn't work ([#3203](https://github.com/trufflesuite/ganache/issues/3203))
- Add `eth_createAccessList` RPC method ([#1056](https://github.com/trufflesuite/ganache/issues/1056))

### Coming Soon™:

- Implications failed: fork.headers -> url ([#2627](https://github.com/trufflesuite/ganache/issues/2627))
- In Geth chain-mode, logic to accept/reject transactions based on gas price/limit should match Geth ([#2176](https://github.com/trufflesuite/ganache/issues/2176))
- `evm_mine` and `miner_start` don't respect --mode.instamine=eager ([#2029](https://github.com/trufflesuite/ganache/issues/2029))
- `evm_setAccount*` is race-conditiony ([#1646](https://github.com/trufflesuite/ganache/issues/1646))
- `@ganache/filecoin@alpha` doesn't work with `ganache@alpha` ([#1150](https://github.com/trufflesuite/ganache/issues/1150))
- Launching ganache with fork is throwing revert errors when communicating with 3rd party contracts ([#956](https://github.com/trufflesuite/ganache/issues/956))
- Build a real pending block! ([#772](https://github.com/trufflesuite/ganache/issues/772))
- VM Exception when interfacing with Kyber contract ([#606](https://github.com/trufflesuite/ganache/issues/606))
- After calling `evm_mine`, `eth_getLogs` returns same logs for all blocks ([#533](https://github.com/trufflesuite/ganache/issues/533))
- personal_unlockAccount works with any password ([#165](https://github.com/trufflesuite/ganache/issues/165))
- --db Option Requires Same Mnemonic and Network ID ([#1030](https://github.com/trufflesuite/ganache/issues/1030))

<p align="right"><sup><a href="#user-content-v7.9.0-top">back to top</a></sup></p>


---

# <p align="center"><a href="#user-content-v7.9.0-future-plans"><img alt="Future Plans" width="auto" src="https://raw.githubusercontent.com/trufflesuite/ganache/release-notes-assets/title-images/future-plans.svg"></a></p>

### Top Priority:

- Accept a genesis.json file ([#1042](https://github.com/trufflesuite/ganache/issues/1042))

### Coming Soon™:

- Switch to esbuild to make build times faster/reasonable ([#1555](https://github.com/trufflesuite/ganache/issues/1555))
- fork specific block & specific index ([#952](https://github.com/trufflesuite/ganache/issues/952))
- Allow to sync forked chain to the latest block ([#643](https://github.com/trufflesuite/ganache/issues/643))
- Implement a streaming trace capability ([#381](https://github.com/trufflesuite/ganache/issues/381))
- Improve log performance when forking ([#145](https://github.com/trufflesuite/ganache/issues/145))
- Log contract events ([#45](https://github.com/trufflesuite/ganache/issues/45))

<p align="right"><sup><a href="#user-content-v7.9.0-top">back to top</a></sup></p>

[Open new issues](https://github.com/trufflesuite/ganache/issues/new?milestone=7.0.0) to influence what we gets implemented and prioritized.

---

<p align="center">
  💖 The Truffle Team
</p>
