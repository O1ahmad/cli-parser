# bootc - v1.11.0

**Release Name**: Release v1.11.0
**Published**: 2025-12-05T18:25:45Z
**Repository**: https://github.com/bootc-dev/bootc

---

## bootc 1.11.0

### Changes

## What's Changed

### Installation & Factory Reset

There's a new experimental factory reset flow, we're looking for feedback on it!

* Initial factory reset code by @ckyrouac in https://github.com/bootc-dev/bootc/pull/1588
* docs: Add docs for install reset to experimental section by @ckyrouac in https://github.com/bootc-dev/bootc/pull/1717
* install: Expand on root_mount_spec option by @cgwalters in https://github.com/bootc-dev/bootc/pull/1765
* install: Fix DPS support by @cgwalters in https://github.com/bootc-dev/bootc/pull/1772
* install: Detect bootloader from target image instead of host by @cgwalters in https://github.com/bootc-dev/bootc/pull/1785
* docs: Document finding deployments in install-to-existing-root by @cgwalters in https://github.com/bootc-dev/bootc/pull/1798
* cli: add `install print-configuration --all` by @mvo5 in https://github.com/bootc-dev/bootc/pull/1820

### Composefs

A lot of progress continues on composefs!

* Make update and switch operations idempotent by @Johan-Liebert1 in https://github.com/bootc-dev/bootc/pull/1797
* docs: Add experimental-composefs by @cgwalters in https://github.com/bootc-dev/bootc/pull/1706
* Composefs deleting deployment by @Johan-Liebert1 in https://github.com/bootc-dev/bootc/pull/1685
* lib: Remove composefs-backend feature gate by @cgwalters in https://github.com/bootc-dev/bootc/pull/1708
* Various composefs changes by @Johan-Liebert1 in https://github.com/bootc-dev/bootc/pull/1715
* System reinstall composefs by @Johan-Liebert1 in https://github.com/bootc-dev/bootc/pull/1726
* composefs: Refactoring to use storage by @cgwalters in https://github.com/bootc-dev/bootc/pull/1718
* cfs: Add --write-dumpfile-to by @cgwalters in https://github.com/bootc-dev/bootc/pull/1738
* Two minor composefs patches by @cgwalters in https://github.com/bootc-dev/bootc/pull/1742
* initramfs: Mount /sysroot readonly for composefs by default by @cgwalters in https://github.com/bootc-dev/bootc/pull/1769
* composefs/bls: Properly reuse kernel + initrd duplicates by @Johan-Liebert1 in https://github.com/bootc-dev/bootc/pull/1796
* composefs/boot: Fix sd-boot order on update by @Johan-Liebert1 in https://github.com/bootc-dev/bootc/pull/1779

### Kernel Arguments & Command Line
* prep work / enhancements to kernel_cmdline by @jeckersb in https://github.com/bootc-dev/bootc/pull/1723
* kernel_cmdline: More prep work for bootc_kargs integration by @jeckersb in https://github.com/bootc-dev/bootc/pull/1729
* kernel_cmdline: Fix parsing/equivalence of "outside" quoted args by @jeckersb in https://github.com/bootc-dev/bootc/pull/1739
* Switch bootc_kargs to use kernel_cmdline for parsing by @jeckersb in https://github.com/bootc-dev/bootc/pull/1724
* kernel_cmdline: Simplify Display impl for utf8::Parameter by @jeckersb in https://github.com/bootc-dev/bootc/pull/1749
* More kargs improvements and hoisting parsing into clap by @jeckersb in https://github.com/bootc-dev/bootc/pull/1761
* Get kargs from usr/lib/bootc/kargs.d by @Johan-Liebert1 in https://github.com/bootc-dev/bootc/pull/1783

### Features
* --transport docker-daemon support by @ericcurtin in https://github.com/bootc-dev/bootc/pull/1776

### Bug Fixes

* Soft reboot: Detect SELinux policy deltas by @gursewak1997 in https://github.com/bootc-dev/bootc/pull/1768
* blockdev: add `bootable` property to find ESP partition by @HuijingHei in https://github.com/bootc-dev/bootc/pull/1736
* store: Preserve /sysroot readonly for read-only operations by @cgwalters in https://github.com/bootc-dev/bootc/pull/1753
* cli: Hide config-diff and delete-deployment by @cgwalters in https://github.com/bootc-dev/bootc/pull/1758
* Add '--remove-destination' option to cp command by @TGNThump in https://github.com/bootc-dev/bootc/pull/1764
* Fix var-tmpfiles lint to check /etc/tmpfiles.d in addition to /usr/lib/tmpfiles.d by @gursewak1997 in https://github.com/bootc-dev/bootc/pull/1763
* blockdev: find `esp` based on `MBR` or `GPT` by @HuijingHei in https://github.com/bootc-dev/bootc/pull/1773
* core: Fix usroverlay regression by @cgwalters in https://github.com/bootc-dev/bootc/pull/1784
* cli: Fix rhsm feature propagation and manpage build order by @cgwalters in https://github.com/bootc-dev/bootc/pull/1807
* Minor fixes by @Johan-Liebert1 in https://github.com/bootc-dev/bootc/pull/1811

### Internal cleanups

* Fix one remaining instance of 114800 baud rate by @jeckersb in https://github.com/bootc-dev/bootc/pull/1822
* Fix undefined BOOTC_buildroot_base in build-sealed script by @shi2wei3 in https://github.com/bootc-dev/bootc/pull/1815
* Fix deprecation warning for rustix::thread::Capability by @jeckersb in https://github.com/bootc-dev/bootc/pull/1750
* xtask: Fix deprecation warnings with rand 0.9 by @jeckersb in https://github.com/bootc-dev/bootc/pull/1766

### Testing & CI
* packit: Update jobs to target newly-released fedora-43 by @jeckersb in https://github.com/bootc-dev/bootc/pull/1709
* ci: Just use one job for build + test by @cgwalters in https://github.com/bootc-dev/bootc/pull/1716
* tests: Use systemd-i128 over uuidgen by @cgwalters in https://github.com/bootc-dev/bootc/pull/1721
* test: Fix OSCI gating failure by @henrywang in https://github.com/bootc-dev/bootc/pull/1730
* Switch over qemu tests to use bcvk by @cgwalters in https://github.com/bootc-dev/bootc/pull/1733
* ci: Add a required-checks context by @cgwalters in https://github.com/bootc-dev/bootc/pull/1744
* ci: Push built images to ghcr.io by @cgwalters in https://github.com/bootc-dev/bootc/pull/1745
* test: Fix factory reset test failure on CS10 by @henrywang in https://github.com/bootc-dev/bootc/pull/1759
* Various tmt + testing improvements by @cgwalters in https://github.com/bootc-dev/bootc/pull/1790
* test: Add more distros for composefs test by @henrywang in https://github.com/bootc-dev/bootc/pull/1810
* ci: Split image publishing, unify variant testing by @cgwalters in https://github.com/bootc-dev/bootc/pull/1829

### Build System
* build-sys: Run most parts with `--network=none` by @cgwalters in https://github.com/bootc-dev/bootc/pull/1725
* build-sys: Reinstall fedora-bootc-destructive-cleanup script by @cgwalters in https://github.com/bootc-dev/bootc/pull/1754
* Dockerfile: Use rpmbuild by @cgwalters in https://github.com/bootc-dev/bootc/pull/1775
* build-sys: Inject hvc0 by default by @cgwalters in https://github.com/bootc-dev/bootc/pull/1786
* Justfile: Bring back build-sealed target by @jeckersb in https://github.com/bootc-dev/bootc/pull/1787
* Justfile: Two minor tweaks by @cgwalters in https://github.com/bootc-dev/bootc/pull/1746

### Documentation
* Elaborate more on Justfile vs Makefile vs GHA by @cgwalters in https://github.com/bootc-dev/bootc/pull/1719
* docs: fix symlink command by @miabbott in https://github.com/bootc-dev/bootc/pull/1747
* docs: Add a packaging-and-integration guide by @cgwalters in https://github.com/bootc-dev/bootc/pull/1782
* docs: Add a man page for bootc-root-setup by @cgwalters in https://github.com/bootc-dev/bootc/pull/1767

### Dependencies
* rust: cargo update by @cgwalters in https://github.com/bootc-dev/bootc/pull/1743
* fix(deps): update rust by @bootc-bot[bot] in https://github.com/bootc-dev/bootc/pull/1740
* chore(deps): update actions/checkout action to v6 by @bootc-bot[bot] in https://github.com/bootc-dev/bootc/pull/1792
* chore(deps): update github actions by @bootc-bot[bot] in https://github.com/bootc-dev/bootc/pull/1823

### Automation
* Sync common files from infra repository by @bootc-bot[bot] in https://github.com/bootc-dev/bootc/pull/1720
* Sync common files from infra repository by @bootc-bot[bot] in https://github.com/bootc-dev/bootc/pull/1821
* Release 1.11.0 by @bootc-bot[bot] in https://github.com/bootc-dev/bootc/pull/1774


## New Contributors
* @HuijingHei made their first contribution in https://github.com/bootc-dev/bootc/pull/1736
* @TGNThump made their first contribution in https://github.com/bootc-dev/bootc/pull/1764
* @shi2wei3 made their first contribution in https://github.com/bootc-dev/bootc/pull/1815

**Full Changelog**: https://github.com/bootc-dev/bootc/compare/v1.10.0...v1.11.0

### Assets

- `bootc-1.11.0-vendor.tar.zstd` - Vendored dependencies archive
- `bootc-1.11.0.tar.zstd` - Source archive
