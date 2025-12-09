# CloudNativePG - v1.28.0-rc2

**Release Name**: v1.28.0-rc2
**Published**: 2025-11-28T16:55:36Z
**Repository**: https://github.com/cloudnative-pg/cloudnative-pg

---

**Release date:** Nov 28, 2025

### Enhancements:

  - Improved network failure detection for replica instances by setting the default `tcp_user_timeout` to 5 seconds. This change helps replicas detect and recover from silent network drops more quickly. Previously, replicas could wait up to 127 seconds before detecting such failures; with the new timeout, they reconnect to the primary within 5 seconds. To preserve the previous behavior, set `STANDBY_TCP_USER_TIMEOUT` to `0` in the operator configuration. ([\#9317](https://github.com/cloudnative-pg/cloudnative-pg/pull/9317))

  - Enhanced cluster restore to wait for all init containers to complete before starting the restore process. This ensures that backup tools running in init containers finish preparing the data before the restore begins. The implementation correctly handles Kubernetes init container sidecars by ignoring those with `RestartPolicy=Always`. ([\#9026](https://github.com/cloudnative-pg/cloudnative-pg/pull/9026))

<!-- 1.27 1.26 1.25 -->

  - Added the `PGBOUNCER_IMAGE_NAME` operator configuration parameter to allow overriding the default PgBouncer image. This is useful for air-gapped environments or when using internal registries. ([\#9232](https://github.com/cloudnative-pg/cloudnative-pg/pull/9232))

  - `cnpg` plugin:
    
      <!-- 1.27 -->

      - Added a `--timeout` flag to the `kubectl cnpg status` command for configuring the timeout for filesystem operations such as calculating cluster size. The default remains 10 seconds but can be adjusted for large clusters where operations may take longer. ([\#9201](https://github.com/cloudnative-pg/cloudnative-pg/pull/9201))

### Fixes:

<!-- 1.27 -->

  - Improved resilience of all probe types (liveness, readiness, and startup) to transient Kubernetes API server connectivity issues. Probes now use a caching mechanism that falls back to cached cluster definitions during brief network interruptions, preventing unnecessary pod restarts and probe failures. ([\#9148](https://github.com/cloudnative-pg/cloudnative-pg/pull/9148))

<!-- 1.27 1.26 1.25 -->

  - Fixed the `CheckEmptyWalArchive` safeguard to run correctly when restoring from a volume snapshot using CNPG-I backup/WAL plugins (e.g., `plugin-barman-cloud`). Previously, this check was skipped for plugin-based implementations. ([\#9306](https://github.com/cloudnative-pg/cloudnative-pg/pull/9306))

<!-- 1.27 -->

  - Improved error reporting when ImageCatalog retrieval fails. The operator now emits a Warning event and logs errors for all failure types, not just `NotFound` errors, improving visibility into configuration issues. ([\#9266](https://github.com/cloudnative-pg/cloudnative-pg/pull/9266))

<!-- 1.27 1.26 1.25 -->

  - Fixed TLS certificate verification issues when connecting to CNPG-I plugins by adding the `cnpg.io/pluginServerName` annotation. This allows customizing the DNS name used for certificate verification in environments where the plugin's certificate uses a different DNS name than the Service name. ([\#9222](https://github.com/cloudnative-pg/cloudnative-pg/pull/9222))

<!-- 1.27 1.26 1.25 -->

  - Fixed an issue where the instance manager controller could fail to restart after an error, reporting a "controller already exists" message. The controller now uses `SkipNameValidation` for subsequent initialization attempts. Contributed by @mateusoliveira43. ([\#9123](https://github.com/cloudnative-pg/cloudnative-pg/pull/9123))

<!-- 1.27 1.26 1.25 -->

  - Fixed incorrect WAL restore path handling in plugins when the destination path is absolute, preventing path duplication issues. Contributed by @Endevir. ([\#9093](https://github.com/cloudnative-pg/cloudnative-pg/pull/9093))

