# Envoy - v1.36.3

**Release Name**: v1.36.3
**Published**: 2025-12-04T14:37:21Z
**Repository**: https://github.com/envoyproxy/envoy

---

**Summary of changes**:

* Security fixes:
  - [CVE-2025-64527](https://github.com/envoyproxy/envoy/security/advisories/GHSA-mp85-7mrq-r866): Envoy crashes when JWT authentication is configured with the remote JWKS fetching
  - [CVE-2025-66220](https://github.com/envoyproxy/envoy/security/advisories/GHSA-rwjg-c3h2-f57p): TLS certificate matcher for `match_typed_subject_alt_names` may incorrectly treat certificates containing an embedded null byte
  - [CVE-2025-64763](https://github.com/envoyproxy/envoy/security/advisories/GHSA-rj35-4m94-77jh): Potential request smuggling from early data after the CONNECT upgrade

**Docker images**:
    https://hub.docker.com/r/envoyproxy/envoy/tags?page=1&name=v1.36.3
**Docs**:
    https://www.envoyproxy.io/docs/envoy/v1.36.3/
**Release notes**:
    https://www.envoyproxy.io/docs/envoy/v1.36.3/version_history/v1.36/v1.36.3
**Full changelog**:
    https://github.com/envoyproxy/envoy/compare/v1.36.2...v1.36.3

Signed-off-by: Ryan Northey <ryan@synca.io>
Signed-off-by: Boteng Yao <boteng@google.com>