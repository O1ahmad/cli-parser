# cert-manager - v1.20.0-alpha.0

**Release Name**: v1.20.0-alpha.0
**Published**: 2025-11-04T16:44:32Z
**Repository**: https://github.com/cert-manager/cert-manager

---

cert-manager is the easiest way to automatically manage certificates in Kubernetes and OpenShift clusters.

> ⚠️ This is a pre-release. For testing only!

## Changes since `v1.19.0`

### Feature

- Add built-in "Ready" status metrics for ClusterIssuer and Issuer resources. (#8188, @mikeluttikhuis)
- Add support for specifying `imagePullSecrets` in the `startupapicheck-job` Helm template to enable pulling images from private registries. (#8186, @mathieu-clnk)

### Bug or Regression

- Adds logs for cases when acme server returns us a fatal error in the order controller (#8199, @Peac36)
- BUGFIX: in case kind or group in the issuerRef of a Certificate was omitted, upgrading to 1.19.x incorrectly caused the certificate to be renewed (#8160, @inteon)
- Fix unregulated retries with the DigitalOcean DNS-01 solver (#8221, @wallrj-cyberark)
- Add full detailed DNS-01 errors to the events attached to the Challenge, for easier debugging (#8221, @wallrj-cyberark)
- Revert API defaults for issuer reference kind and group introduced in 0.19.0 (#8173, @erikgb)
- When Prometheus monitoring is enabled, the metrics label is now set to the intended value of `cert-manager`. Previously, it was set depending on various factors (namespace cert-manager is installed in and/or Helm release name). (#8162, @LiquidPL)