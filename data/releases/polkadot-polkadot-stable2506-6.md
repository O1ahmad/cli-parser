# Polkadot - polkadot-stable2506-6

**Release Name**: Polkadot stable2506-6
**Published**: 2025-12-05T06:46:58Z
**Repository**: https://github.com/paritytech/polkadot-sdk

---


This release contains the changes from `polkadot-stable2506-5` to `polkadot-stable2506-6`.

ℹ️ **Please note:**

⚠️ This is a patch release for the stable version: `stable2506` and contains only patches and fixes to the crates (list
below). No binary or docker images will be provided for this release.

The tag corresponding to the current patch release `polkadot-stable2506-6` and matching the old pattern will be
available under [polkadot-v1.19.6](https://github.com/paritytech/polkadot-sdk/releases/tag/polkadot-v1.19.6).

The following crates were updated to the corresponding versions:

- cumulus-pallet-parachain-system@0.21.2


## Changelog

### Changelog for `Node Dev`

**ℹ️ These changes are relevant to:**  Those who build around the client side code. Alternative client builders, SMOLDOT, those who consume RPCs. These are people who are oblivious to the runtime changes. They only care about the meta-protocol, not the protocol itself.


#### [#10280]: Accept only one block in `validate_block` when upgrading a runtime
As the validation is running the entire time using the same validation code, we can not accept any other blocks after a runtime upgrade was applied.

## Rust compiler versions

This release was built and tested against the following versions of `rustc`.
Other versions may work.

- Rust Stable: `1.84.1`

