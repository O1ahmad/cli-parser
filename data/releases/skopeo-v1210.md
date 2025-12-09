# Skopeo - v1.21.0

**Release Name**: v1.21.0
**Published**: 2025-12-03T18:33:46Z
**Repository**: https://github.com/containers/skopeo

---

- New support for creating "simple signing" signatures using Sequoia-PGP, dependent on a build tag that enables it
- New option `skopeo copy --force-compression-format`
- New option `--user-agent-prefix`
- TLS options on the command line of `skopeo sync` take precedence over options in YAML

This is intended to match dependencies of Podman 5.7 as closely as possible.
