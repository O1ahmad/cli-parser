# Strimzi - 0.49.1

**Release Name**: 0.49.1
**Published**: 2025-12-05T13:26:17Z
**Repository**: https://github.com/strimzi/strimzi-kafka-operator

---

⚠️ **SECURITY: Strimzi 0.49.1 addresses [CVE-2025-66623](https://github.com/strimzi/strimzi-kafka-operator/security/advisories/GHSA-xrhh-hx36-485q). If you use Strimzi 0.47.0 or newer, we recommend upgrading to 0.49.1.**

⚠️ **IMPORTANT: Strimzi 0.49 introduces new API version `v1` to all Strimzi custom resources.**
* **Make sure to [Upgrade the CRDs](#upgrading-your-clusters) as part of the Strimzi upgrade as well (especially when using Helm).**
* **The old API versions (`v1alpha1`, `v1beta1`, and `v1beta2`) will continue to be supported until Strimzi 1.0.0 / 0.52.0.**
* **Before upgrading to Strimzi 0.49.0 or newer, make sure that you update your `KafkaUser` resources to [use the `.spec.authorization.acls[]operations` field instead of the deprecated `.spec.authorization.acls[]operation`](https://strimzi.io/docs/operators/0.49.1/deploying.html#con-api-conversion-v1-str).**
* **For more details about the migration to the `v1` API and CRD upgrades, see the [documentation](https://strimzi.io/docs/operators/0.49.1/deploying.html#assembly-api-conversion-str).**

----

## Main changes since 0.49.0

This release contains the following bug fixes and improvements:

* Fixes CVE-2025-66623
* Fixed TLS configuration in MirrorMaker 2 examples
* `v1` API Conversion Tool bug fixes
* Fixed incorrect default names for Strimzi Metrics Provider metrics
* Fixed Push secret handling when `UseConnectBuildWithBuildah` feature gate is enabled
* Documentation improvements

All changes can be found under the [0.49.1 milestone](https://github.com/strimzi/strimzi-kafka-operator/milestone/56).

### Upgrading from Strimzi 0.49.0

See the [documentation for upgrade instructions](https://strimzi.io/docs/operators/0.49.1/deploying.html#assembly-upgrade-str).

### Container images

The following container images are part of this release:

| Name | Image |
| ----------- | ----------- |
| Operators | `quay.io/strimzi/operator@sha256:f0cea0535f65bca8d9e503d62de27bd1327e18e8cee64a515f3e9d06506c5aad` |
| Apache Kafka 4.0.0 | `quay.io/strimzi/kafka@sha256:8f775ee53622bf68b791c405e40299baa3d845b98e282d1a9269f9466018e990` |
| Apache Kafka 4.0.1 | `quay.io/strimzi/kafka@sha256:d495d3b6c98d1ea22ed3bdf0d6d06d6cda1c5b35087c817e8cf807892b178520` |
| Apache Kafka 4.1.0 | `quay.io/strimzi/kafka@sha256:73799dcf5bc7d1bb19f500f345d8892a1f91cf0213e01d9b59d3a1a53cc80aca` |
| Apache Kafka 4.1.1 | `quay.io/strimzi/kafka@sha256:bfbee54f85beb3731cf41483befa39d8c5ebe5db002df6265c6ea95b6a156749` |
| Strimzi Bridge | `quay.io/strimzi/kafka-bridge@sha256:53034f64f0b672f10b5bacea1c7a25132f118df7fd5c9032c4dbf702ed93796a` |
| Kaniko executor | `quay.io/strimzi/kaniko-executor@sha256:a5088c14d7b8bf1d336669cba047b971bf3ece8969647dae2c1e3a07a7be0c5e` |
| Maven Builder | `quay.io/strimzi/maven-builder@sha256:b8831c2aad621b80dce38484fae353cc5226bfc4dffb0f4c9d8b8d86e0fb3933` |
| Buildah builder | `quay.io/strimzi/buildah@sha256:ba89470b45a49e5e09aaab91a5c3c03ecb14f9013d598bc14b3d756eb9a145b4` |