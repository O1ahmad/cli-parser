# Crossplane - v2.1.3

**Release Name**: v2.1.3
**Published**: 2025-12-02T04:01:23Z
**Repository**: https://github.com/crossplane/crossplane

---

This release resolves https://github.com/crossplane/crossplane/issues/6761 - issues when upgrading providers that manifest with errors like these:

> cannot establish control of object: addresses.compute.gcp.upbound.io is already controlled by ProviderRevision provider-gcp-compute-a41e4ba551fc (UID 58db5dee-38e7-40f9-9d31-669bb25a688e)

## What's Changed
* [Backport release-2.1] Use server-side apply for MRD controller by @negz in https://github.com/crossplane/crossplane/pull/6952


**Full Changelog**: https://github.com/crossplane/crossplane/compare/v2.1.2...v2.1.3