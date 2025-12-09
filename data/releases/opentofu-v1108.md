# OpenTofu - v1.10.8

**Release Name**: v1.10.8
**Published**: 2025-12-08T19:49:22Z
**Repository**: https://github.com/opentofu/opentofu

---

SECURITY ADVISORIES:

This release contains fixes for some security advisories related to previous releases in this series.

- Incorrect handling of excluded subdomain constraint in conjunction with TLS certificates containing wildcard SANs

    This release incorporates the upstream fixes for [GO-2025-4175](https://pkg.go.dev/vuln/GO-2025-4175).

- Excessive CPU usage when reporting error about crafted TLS certificate with many hostnames

    This release incorporates the upstream fixes for [GO-2025-4155](https://pkg.go.dev/vuln/GO-2025-4155).


**Full Changelog**: https://github.com/opentofu/opentofu/compare/v1.10.7...v1.10.8

