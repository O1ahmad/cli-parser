# Container Network Interface (CNI) - v1.3.0

**Release Name**: v1.3.0
**Published**: 2025-04-07T15:40:01Z
**Repository**: https://github.com/containernetworking/cni

---

## What's Changed
* RFC - Support safe subdirectory-based plugin conf loading by @bleggett in https://github.com/containernetworking/cni/pull/1052

This adds a new config flag `loadPluginsFromFolde`r - if present, for a given named network bar, plugin configuration objects will be loaded from `<path-to-bar-network-config-file>/bar/xxx.conf`. This may be useful for vendors providing chained plugins: you can add your plugin to a chain without needing to edit the file in-place.

## New Contributors
* @bleggett made their first contribution in https://github.com/containernetworking/cni/pull/1052

**Full Changelog**: https://github.com/containernetworking/cni/compare/v1.2.3...v1.3.0