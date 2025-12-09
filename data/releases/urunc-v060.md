# urunc - v0.6.0

**Release Name**: v0.6.0
**Published**: 2025-07-04T13:49:24Z
**Repository**: https://github.com/urunc-dev/urunc

---

## What's Changed

### New features

* Add support for mewz unikernels
* Add support for cli options at the runtime
* Add support for environment variables, by passing the environment variables of the container in the unikernel
* Add support for existing containers, by booting a minimal Linux VM
* Add support for the creation and chroot to a new rootfs for monitor execution
* Add support for mounting volumes in the container's rootfs
* Add support for using the container;s rootfs as the rootfs of the guest through 9pfs shared-fs.

### Breaking changes

* Replace `useDMBlock` annotation with `mountRootfs`.

### Internals

* Improve logging and error handling
* Update Unikraft cli handling to replicate kraftkit's behavior

### CI/CD

* Add workflow to publish docs automatically
* Migrate to GH runners for all CI actions
* fix invocation and update urunc-deploy building action
* Improve CI, by removing hardcoded repo values, running workflows in the correct context and removing org secret dependencies

### Misc

* Add security policy
* Give a new look in urunc's documentation, with the new logo, colors, footer, and easier copying of commands
* Uodate knative tutorial
* Add project governance
* Fix typos and update urunc documentation
* Update README with new info about urunc's community, Slack channel, roadmap and OpenSSF badge.

**Full Changelog**: https://github.com/urunc-dev/urunc/compare/v0.5.0...v0.6.0