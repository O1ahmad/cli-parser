# Keylime - v7.13.0

**Release Name**: v7.13.0
**Published**: 2025-09-15T08:54:59Z
**Repository**: https://github.com/keylime/keylime

---

## What's Changed
### New features and significant changes
* Extend meta_data field in verifierdb by @Isaac-Matthews in https://github.com/keylime/keylime/pull/1750
* Initial version of verify evidence enhancement by @mpeters in https://github.com/keylime/keylime/pull/1753
* Add 2.5 templates including Push Model agent changes by @sarroutbi in https://github.com/keylime/keylime/pull/1783
* Remove unnecessary configuration values by @sarroutbi in https://github.com/keylime/keylime/pull/1792
### Bugfixes and improvements
* Remove excessive logging on exception by @kaifeng in https://github.com/keylime/keylime/pull/1735
* registrar: Log API versions during startup by @ansasaki in https://github.com/keylime/keylime/pull/1741
* tpm_util: fix quote signature extraction for ECDSA by @THS-on in https://github.com/keylime/keylime/pull/1746
* Fix pylint invalid name warnings (C0103) by @msafarik in https://github.com/keylime/keylime/pull/1758
* Fix create_runtime_policy in python < 3.12 by @mpeters in https://github.com/keylime/keylime/pull/1765
* templates: duplicate str_to_version() in the adjust script by @sergio-correia in https://github.com/keylime/keylime/pull/1768
* docker: Remove tpm2-tools compilation from base image by @ansasaki in https://github.com/keylime/keylime/pull/1767
* tenant: Add --push-model option to avoid requests to agents by @sarroutbi in https://github.com/keylime/keylime/pull/1770
* fix: Use `fork` as `multiprocessing` start method by @kkaarreell in https://github.com/keylime/keylime/pull/1773
* verifier: Gracefully shutdown webhook workers during signal handling by @ansasaki in https://github.com/keylime/keylime/pull/1784
* fix: Resolve database connection leaks causing QueuePool limit errors by @ansasaki in https://github.com/keylime/keylime/pull/1782
* Misc fixes by @sergio-correia in https://github.com/keylime/keylime/pull/1785
* mb: support vendor_db as logged by newer shim versions by @sergio-correia in https://github.com/keylime/keylime/pull/1791
* mba: normalize vendor_db in EV_EFI_VARIABLE_AUTHORITY events by @sergio-correia in https://github.com/keylime/keylime/pull/1793
* models: Do not re-encode certificate stored in DB by @ansasaki in https://github.com/keylime/keylime/pull/1794
* policy/sign: use print() when writing to /dev/stdout by @sergio-correia in https://github.com/keylime/keylime/pull/1795
* registrar: Do not store corrupted certificate in the DB by @ansasaki in https://github.com/keylime/keylime/pull/1798
### Base image updates
* [Automatic] Update Keylime base image (2025-03-10) by @github-actions[bot] in https://github.com/keylime/keylime/pull/1745
* [Automatic] Update Keylime base image (2025-04-01) by @github-actions[bot] in https://github.com/keylime/keylime/pull/1752
* [Automatic] Update Keylime base image (2025-04-04) by @github-actions[bot] in https://github.com/keylime/keylime/pull/1755
* [Automatic] Update Keylime base image (2025-05-02) by @github-actions[bot] in https://github.com/keylime/keylime/pull/1757
* [Automatic] Update Keylime base image (2025-06-02) by @github-actions[bot] in https://github.com/keylime/keylime/pull/1763
* [Automatic] Update Keylime base image (2025-06-04) by @github-actions[bot] in https://github.com/keylime/keylime/pull/1769
* [Automatic] Update Keylime base image (2025-07-01) by @github-actions[bot] in https://github.com/keylime/keylime/pull/1776
* [Automatic] Update Keylime base image (2025-08-01) by @github-actions[bot] in https://github.com/keylime/keylime/pull/1787
* [Automatic] Update Keylime base image (2025-09-01) by @github-actions[bot] in https://github.com/keylime/keylime/pull/1796
### Documentation improvements
* docs: add GitHub PR template with documentation reminders by @Yizhi-W in https://github.com/keylime/keylime/pull/1748
* docs: migrate issue templates to GitHub's new directory structure by @Yizhi-W in https://github.com/keylime/keylime/pull/1751
* Docs: expand security/threat model page by @stringlytyped in https://github.com/keylime/keylime/pull/1704
* Manpage for keylime_tenant binary by @msafarik in https://github.com/keylime/keylime/pull/1786
* Fix minor typo (exponantial->exponential) by @sarroutbi in https://github.com/keylime/keylime/pull/1780
### Testing/CI
* scripts: Fix coverage information downloading script by @ansasaki in https://github.com/keylime/keylime/pull/1738
* tests: change test_mba_parsing to not need keylime installed by @sergio-correia in https://github.com/keylime/keylime/pull/1736
* lint: Fix mypy warnings by @ansasaki in https://github.com/keylime/keylime/pull/1742
* packit: Add compatibility/api_version_compatibility test by @ansasaki in https://github.com/keylime/keylime/pull/1744
* CI: Enable CONTAINER_ENGINE to allow alternative container engines by @sarroutbi in https://github.com/keylime/keylime/pull/1771
* CI: Enable test add-agent-with-malformed-ek-cert by @kkaarreell in https://github.com/keylime/keylime/pull/1797
### Other
* Bump version to 7.13.0 by @ansasaki in https://github.com/keylime/keylime/pull/1801

## New Contributors
* @Yizhi-W made their first contribution in https://github.com/keylime/keylime/pull/1748
* @msafarik made their first contribution in https://github.com/keylime/keylime/pull/1758

**Full Changelog**: https://github.com/keylime/keylime/compare/v7.12.1...v7.13.0