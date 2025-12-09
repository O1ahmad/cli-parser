# Infracost - v0.10.43

**Release Name**: v0.10.43
**Published**: 2025-12-03T11:22:38Z
**Repository**: https://github.com/infracost/infracost

---

This release brings support for new AWS regions and OpenTofu extensions, improvements to Docker performance, and several important bug fixes. Special thanks to new contributors @shikharawasthi and @karamaru-alpha! 👏

### ✨ New Features

* Added support for new AWS regions: `ap-east-2`, `ap-southeast-6`, `ap-southeast-7`, and `mx-central-1` by @aliscott in [https://github.com/infracost/infracost/pull/3446](https://github.com/infracost/infracost/pull/3446) and [https://github.com/infracost/infracost/pull/3459](https://github.com/infracost/infracost/pull/3459).
* Added support for OpenTofu extensions by @liamg in [https://github.com/infracost/infracost/pull/3474](https://github.com/infracost/infracost/pull/3474).

### 🐛 Fixes

* Fixed AWS EC2 bare metal instance cost calculations by @shikharawasthi in [https://github.com/infracost/infracost/pull/3471](https://github.com/infracost/infracost/pull/3471).
* Fixed Azure Cognitive Account lookups by @aliscott in [https://github.com/infracost/infracost/pull/3444](https://github.com/infracost/infracost/pull/3444).
* Fixed nil pointer issues in Azure VM Scale Sets and diff output by @aliscott and @liamg.
* Prevented panics during truncation and improved GitHub comment handling by @tim775.
* Ensured `PastBreakdown` is non-nil in outputs by @bazaah in [https://github.com/infracost/infracost/pull/3426](https://github.com/infracost/infracost/pull/3426).

### 🚀 Performance

* Optimized Docker images by reducing layers, removing unused files, and shrinking cache usage by @karamaru-alpha in [https://github.com/infracost/infracost/pull/3479](https://github.com/infracost/infracost/pull/3479), [https://github.com/infracost/infracost/pull/3480](https://github.com/infracost/infracost/pull/3480), [https://github.com/infracost/infracost/pull/3481](https://github.com/infracost/infracost/pull/3481), [https://github.com/infracost/infracost/pull/3485](https://github.com/infracost/infracost/pull/3485)

### 🧰 Maintenance

* Upgraded Go to v1.25.4 for latest security patches by @aliscott in [https://github.com/infracost/infracost/pull/3482](https://github.com/infracost/infracost/pull/3482).
* Updated internal dependencies (`go-getter`, `golang.org/x/*`, etc.).

**Full Changelog**: [https://github.com/infracost/infracost/compare/v0.10.42...v0.10.43](https://github.com/infracost/infracost/compare/v0.10.42...v0.10.43)