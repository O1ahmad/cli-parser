# Inspektor Gadget - v0.47.0

**Release Name**: Release v0.47.0
**Published**: 2025-12-01T08:13:10Z
**Repository**: https://github.com/inspektor-gadget/inspektor-gadget

---

Highlights of this release are:

* trace_open: add file path after symlink resolution by @alban in https://github.com/inspektor-gadget/inspektor-gadget/pull/5066
* tree-wide: add more metadata to parameters by @flyth in https://github.com/inspektor-gadget/inspektor-gadget/pull/5082
* feat: added ig image verify command by @ask-elad in https://github.com/inspektor-gadget/inspektor-gadget/pull/5010
* pkg: signature: Add support for cosign bundle format by @eiffel-fl in https://github.com/inspektor-gadget/inspektor-gadget/pull/5086

### Breaking change:
* op/otel-metrics: Change default metricname to FullName by @burak-ok in https://github.com/inspektor-gadget/inspektor-gadget/pull/4870

### General Improvements

* op/otel-metrics: Add metricname annotation by @burak-ok in https://github.com/inspektor-gadget/inspektor-gadget/pull/4870
* Artifact Hub: Update gadgets version to v0.46.0 by @github-actions[bot] in https://github.com/inspektor-gadget/inspektor-gadget/pull/5040
* feature(cli): allow “-f -” to apply gadget manifest from stdin by @ask-elad in https://github.com/inspektor-gadget/inspektor-gadget/pull/5035
* added new function to recursively call GetAuthConfig by @ask-elad in https://github.com/inspektor-gadget/inspektor-gadget/pull/5065
* op/sort: Append the fields when same DS is specified by @burak-ok in https://github.com/inspektor-gadget/inspektor-gadget/pull/4784

### Security Improvements

* vex: Fix PURL for trivy by @burak-ok in https://github.com/inspektor-gadget/inspektor-gadget/pull/5024
* pkg: oci: Add nil check for Verifier in VerifyGadgetImage(). by @eiffel-fl in https://github.com/inspektor-gadget/inspektor-gadget/pull/5074
* pkg: signature: Add new signature-format package for cosign. by @eiffel-fl in https://github.com/inspektor-gadget/inspektor-gadget/pull/5056
* pkg: oci: Pull gadget signature if verification failed. by @eiffel-fl in https://github.com/inspektor-gadget/inspektor-gadget/pull/5105

### Bug Fixes

* fixed /test/integration/trace_tcpretrans_test.go to allow 1.0.0.1 as well as 1.1.1.1 by @ask-elad in https://github.com/inspektor-gadget/inspektor-gadget/pull/5052
* dead container made independent of name by @ask-elad in https://github.com/inspektor-gadget/inspektor-gadget/pull/5088

### Documentation Improvements

* docs/tcpdump: Add kubectl-gadget section by @mqasimsarfraz in https://github.com/inspektor-gadget/inspektor-gadget/pull/5015

### Testing and Continue Integration

* makefile/gadgets: Support testing for local registry by @mqasimsarfraz in https://github.com/inspektor-gadget/inspektor-gadget/pull/5021
* Testing: Wait for the Pod to be created before kubectl wait by @burak-ok in https://github.com/inspektor-gadget/inspektor-gadget/pull/5048
* Validate parent TID belongs to same process in test by @matthyx in https://github.com/inspektor-gadget/inspektor-gadget/pull/5069

## New Contributors
* @ask-elad made their first contribution in https://github.com/inspektor-gadget/inspektor-gadget/pull/5035

**Full Changelog**: https://github.com/inspektor-gadget/inspektor-gadget/compare/v0.46.0...v0.47.0