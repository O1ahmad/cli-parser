# SPIRE - v1.13.3

**Release Name**: v1.13.3
**Published**: 2025-10-23T13:05:05Z
**Repository**: https://github.com/spiffe/spire

---

### Added

- X.509 CA metric with absolute expiration time in addition to TTL-based metric (#6303)
- `spire-agent` configuration to source join tokens from files to support integration with third-party credential providers (#6330)
- Capability to filter on caller path in `spire-server` Rego authorization policies (#6320)

### Changed

- `spire-server` will use the SHA-256 algorithm for X.509-SVID Subject Key Identifiers when the `GODEBUG` environment variable contains `fips140=only` (#6294)
- Attested node entries are now purged at a fixed interval with jitter (#6315)
- `oidc-discovery-provider` now fails to initialize when started with unrecognized arguments (#6297)

### Fixed

- Documentation fixes (#6309, #6323, #6377)