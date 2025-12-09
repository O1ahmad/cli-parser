# Capsule - v0.12.0

**Release Name**: v0.12.0
**Published**: 2025-12-05T14:36:58Z
**Repository**: https://github.com/projectcapsule/capsule

---

## Changelog
### ✨ New Features
* 584d372521a9a639b12a5093a2f62d6b4c0f8a05: feat(config): add combined users property as successor for usergroups (#1767) (@oliverbaehler)
* 7e7d9d02c65764f349bc4e71bd6f85f27efc96e6: feat(config): administrators get delete privileges for tenant namespaces (#1749) (@oliverbaehler)
* 581a8fe60e5a8a4c2861c32dd9854e1c2461777f: feat(controller): administration persona (#1739) (@oliverbaehler)
* dd39e1a6d5ede6523f7e68e15fe919cdad23a5a0: feat(dra): support dra device classes (#1759) (@Svarrogh1337)
* 5899e6d9a151478f7139ed54032cfb7d803341c3: feat(tenant): add available classes as status fields (#1751) (@oliverbaehler)
* d812a0c7221baf61aec4ceea613ba094045e2820: feat(tenant): add dedicated tenantowner crd (#1764) (@oliverbaehler)
* 6e8405d5f01f3cd5b618533d6a4710ad5e8567c1: feat: refactor core webhooks (#1756) (@oliverbaehler)
### 🐛 Bug fixes
* a270d6797a1009932054e3ee844b526020ade1fe: fix(admission): consistently inspect ownerreferences for namespace validations (#1758) (@oliverbaehler)
### 🛠 Dependency updates
* 866c69ffc322f0cff604601f314ef9b79673eae8: fix(deps): update module github.com/onsi/ginkgo/v2 to v2.27.2 (#1725) (@renovate[bot])
* 550f3cc074a2cbb5c5f6a708d1c6e17927efa05e: fix(deps): update module go.uber.org/zap to v1.27.1 (#1748) (@renovate[bot])
* 92d73ae7c9f6577b4991da01807de1b989acd396: fix(deps): update module golang.org/x/sync to v0.18.0 (#1734) (@renovate[bot])
* 9e73320e040b96d63dc3e0ac086d1c6fd0963e81: fix(deps): update module sigs.k8s.io/cluster-api to v1.11.3 (#1732) (@renovate[bot])
* 3c5708a37f7455b5cfb760324d6d0838e4edd974: fix(deps): update module sigs.k8s.io/controller-runtime to v0.22.4 (#1731) (@renovate[bot])
* 007cea96f4984fcfc81541e626d8a88e07824aff: fix(deps): update module sigs.k8s.io/gateway-api to v1.4.1 (#1770) (@renovate[bot])

**Full Changelog**: https://github.com/projectcapsule/capsule/compare/v0.11.1...v0.12.0

[Check out what's new in this release](https://projectcapsule.dev/docs/whats-new/)

**Docker Images**
- `ghcr.io/projectcapsule/capsule:0.12.0`
- `ghcr.io/projectcapsule/capsule:latest`

**Helm Chart**
View this release on [Artifact Hub](https://artifacthub.io/packages/helm/projectcapsule/capsule/0.12.0) or use the OCI helm chart:

- `ghcr.io/projectcapsule/charts/capsule:0.12.0`

[Review the Major Changes section first before upgrading to a new version](https://artifacthub.io/packages/helm/projectcapsule/capsule/0.12.0#major-changes)

> [!IMPORTANT]
> **Kubernetes compatibility**
>
> Note that the Capsule project offers support only for the latest minor version of Kubernetes.
> Backwards compatibility with older versions of Kubernetes and OpenShift is [offered by vendors](https://projectcapsule.dev/support/).
>
> | Kubernetes version | Minimum required |
> |--------------------|------------------|
> | `v1.34`            | `>= 1.34.0`      |


Thanks to all the contributors! 🚀 🦄

