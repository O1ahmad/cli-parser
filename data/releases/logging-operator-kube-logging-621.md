# Logging Operator (Kube Logging) - 6.2.1

**Release Name**: 6.2.1
**Published**: 2025-11-27T10:02:25Z
**Repository**: https://github.com/kube-logging/logging-operator

---

## What's Changed

### New or updated images
| component | image |
| - | - |
| operator |`ghcr.io/kube-logging/logging-operator:6.2.1` |
| fluentd | `ghcr.io/kube-logging/logging-operator/fluentd:6.2.1-full` |
| syslog-ng-reloader | `ghcr.io/kube-logging/logging-operator/syslog-ng-reloader:6.2.1` |
| config-reloader | `ghcr.io/kube-logging/logging-operator/config-reloader:6.2.1` |
| fluentd-drain-watch | `gghcr.io/kube-logging/logging-operator/fluentd-drain-watch:6.2.1` |
| buffer-volume-metrics | `ghcr.io/kube-logging/logging-operator/node-exporter:6.2.1` |

### Install with helm

```bash
helm install logging-operator oci://ghcr.io/kube-logging/helm-charts/logging-operator --version=6.2.1
```

### Dependency and image updates
* chore(deps): update all dependencies by @renovate[bot] in https://github.com/kube-logging/logging-operator/pull/2144
### Bug fixes
* fix: align metrics service names and reuse object metadata by @aslafy-z in https://github.com/kube-logging/logging-operator/pull/2147
* fix: apply ServiceMonitor default values only when metrics are enabled by @aslafy-z in https://github.com/kube-logging/logging-operator/pull/2146


**Full Changelog**: https://github.com/kube-logging/logging-operator/compare/6.2.0...6.2.1