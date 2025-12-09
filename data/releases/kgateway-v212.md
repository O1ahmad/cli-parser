# Kgateway - v2.1.2

**Release Name**: v2.1.2
**Published**: 2025-12-06T16:38:35Z
**Repository**: https://github.com/kgateway-dev/kgateway

---


🎉 Welcome to the v2.1.2 release of the kgateway project!
---



## Installation

The kgateway project is available as a Helm chart and docker images.

### Helm Charts

The Helm chart is available at cr.kgateway.dev/kgateway-dev/charts/kgateway.

### Docker Images

The docker images are available at:

- cr.kgateway.dev/kgateway-dev/kgateway:v2.1.2
- cr.kgateway.dev/kgateway-dev/sds:v2.1.2
- cr.kgateway.dev/kgateway-dev/envoy-wrapper:v2.1.2

## Quickstart

Try installing this release:
```
helm install kgateway-crds oci://cr.kgateway.dev/kgateway-dev/charts/kgateway-crds --version v2.1.2 --namespace kgateway-system --create-namespace
helm install kgateway oci://cr.kgateway.dev/kgateway-dev/charts/kgateway --version v2.1.2 --namespace kgateway-system --create-namespace
```

For detailed installation instructions and next steps, please visit our [quickstart guide](https://kgateway.dev/docs/quickstart/).

