# Piraeus Datastore - v2.10.2

**Release Name**: v2.10.2
**Published**: 2025-11-27T12:33:57Z
**Repository**: https://github.com/piraeusdatastore/piraeus-operator

---

This release updates the DRBD version to 9.2.16, along with an update to LINSTOR CSI to fix issues with the new `fsck` behaviour.

We also added configurable timeouts for the [new evacuation process](https://piraeus.io/docs/stable/explanation/deletion-policies/). 

Finally, we fixed an issue where the CSI Driver would report SELinux capabilities, but the `mount` command stripped them because it saw SELinux as disabled.

---

### Added

- Configurable timeouts for how long the Operator waits for volume to (re-)attach during evacuation.

### Fixed

- Ensure `mount` commands pass along SELinux options by mounting SELinux directories.

### Changed

- Updated images:
    * DRBD 9.2.16
    * LINSTOR CSI 1.10.3
    * Latest CSI sidecars

