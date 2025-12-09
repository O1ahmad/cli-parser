# Certbot - v5.2.1

**Release Name**: Certbot 5.2.1
**Published**: 2025-12-03T20:33:04Z
**Repository**: https://github.com/certbot/certbot

---

### Added

- Support for Python 3.14 was added.
  ([#10477](https://github.com/certbot/certbot/issues/10477))

### Changed

- While nothing significant should have changed from the user's perspective,
  we've been doing a lot of internal refactoring in preparation for soon adding
  support for IP address certificates to Certbot.
  ([#10468](https://github.com/certbot/certbot/issues/10468),
  [#10478](https://github.com/certbot/certbot/issues/10478))

### Fixed

- Removed `vhost_combined` and `vhost_common` log formats from included Apache
  configuration file. ([#9769](https://github.com/certbot/certbot/issues/9769))
- Due to a mistake on our end playing with GitHub's new [immutable
  releases](https://github.blog/changelog/2025-10-28-immutable-releases-are-now-generally-available/)
  feature that prevented our CI from uploading additional release assets,
  Certbot 5.2.0 was not and will not be uploaded to most platforms. Instead,
  that version number will be skipped and we'll go straight to 5.2.1.
  ([#10501](https://github.com/certbot/certbot/issues/10501))


