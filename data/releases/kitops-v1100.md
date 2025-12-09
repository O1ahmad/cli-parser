# KitOps - v1.10.0

**Release Name**: Release v1.10.0
**Published**: 2025-11-07T19:06:56Z
**Repository**: https://github.com/kitops-ml/kitops

---


Welcome to the v1.10.0 release of Kit! With this release, we're proud to announce initial support for CNCF ModelPack artifacts in the Kit CLI. 

## New Features

### CNCF ModelPack support

We've added support for the [CNCF model-spec](https://github.com/modelpack/model-spec) in the Kit CLI. For most use cases, this should mean that Kit is able to work with ModelPack artifacts in the same way it handles ModelKits, allowing you to push, pull, and unpack artifacts that conform to the ModelPack specification.

To create new ModelPack artifacts, the `kit pack` command now supports the `--use-model-pack` flag. If specified, instead of creating a ModelKit OCI artifact, Kit will create an OCI artifact in the model-spec format. Once created, these artifacts should be handled by the Kit CLI transparently, with no additional changes to usage, though additional tools that rely on ModelKit media types may have issues processing ModelPack artifacts.

For more detail, see the PR that added support: https://github.com/kitops-ml/kitops/pull/1000

## Documentation updates

* Adding Security page by @bmicklea in https://github.com/kitops-ml/kitops/pull/1001
* Create INSTALL.md by @bmicklea in https://github.com/kitops-ml/kitops/pull/1008


## Bug Fixes

* Handle missing tag in ModelKit references per command by @amisevsk in https://github.com/kitops-ml/kitops/pull/1003

**Full Changelog**: https://github.com/kitops-ml/kitops/compare/v1.9.0...v1.10.0