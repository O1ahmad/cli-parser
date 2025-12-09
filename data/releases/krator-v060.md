# Krator - v0.6.0

**Release Name**: v0.6.0
**Published**: 2021-11-23T00:13:31Z
**Repository**: https://github.com/krator-rs/krator

---

* Fixed a race condition which caused object tasks to get stuck right after the state machine completed. For more info see #4.
* Rust 2021 Edition
* Increment `kube` to version 0.64.
* Bump `tokio` to 1.14 to address RUSTSEC-2021-0124.