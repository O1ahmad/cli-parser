# Benthos - v4.72.0

**Release Name**: v4.72.0
**Published**: 2025-11-28T13:08:27Z
**Repository**: https://github.com/benthosdev/benthos

---

For installation instructions check out the [getting started guide](https://docs.redpanda.com/redpanda-connect/guides/getting_started).

### Added

- Added Redpanda Cloud service account authentication to all redpanda/kafka based components (@rockwotj)
- `mysql_cdc`: Support for chained or unchained IAM authentication (@josephwoodward)
- `postgresql_cdc`: Support for chained IAM authentication (@josephwoodward)
- `redpanda_migrator`: Add client timeout config for schema registry client (@josephwoodward)

### Fixed

- `schema_registry_decode`: Fix serde protobuf race condition in processor (@rockwotj)

The full change log can be [found here](https://github.com/redpanda-data/connect/blob/main/CHANGELOG.md).

