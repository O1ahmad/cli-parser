# Inclavare Containers - v0.6.4

**Release Name**: Inclavare Containers 0.6.4 release
**Published**: 2021-11-30T11:19:55Z
**Repository**: https://github.com/inclavare-containers/inclavare-containers

---

The new features of this release all revolve around RATS-TLS:
- Support TDX attestation in RATS-TLS.
- Compatible with OpenSSL 1.0.x version.

Other updates include:
- Verdictd and [attestation-agent](https://github.com/confidential-containers/attestation-agent) support to obtain keys to decrypt encrypted container images with TDX attestation based on RATS-TLS.
- Update SGX software stack from 2.13 to 2.14.
- Fix CVE vulnerabilities in shim-rune: CVE-2021-41103, CVE-2021-30465, GHSA-77vh-xpmg-72qh and GHSA-77vh-xpmg-72qh.
- CI/CD adds integration tests for RATS-TLS and EAA components.
- Each component has its own version number right now, therefore each component will control its own release rhythm.