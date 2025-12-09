# Loki - operator/v0.9.0

**Release Name**: operator: v0.9.0
**Published**: 2025-12-04T15:55:22Z
**Repository**: https://github.com/grafana/loki

---

## [0.9.0](https://github.com/grafana/loki/compare/operator/v0.8.0...operator/v0.9.0) (2025-12-04)


### ⚠ BREAKING CHANGES

* **operator:** consolidate image build workflows and improve documentation ([#19395](https://github.com/grafana/loki/issues/19395))

### Features

* **operator:** Add alert LokiIngesterFlushFailureRateCritical ([#18698](https://github.com/grafana/loki/issues/18698)) ([66ebc5a](https://github.com/grafana/loki/commit/66ebc5a184cf1d54b1e41b14b2a76f6601156405))
* **operator:** Add warning alert for when LokiStack is not getting ready ([#19258](https://github.com/grafana/loki/issues/19258)) ([c47fe46](https://github.com/grafana/loki/commit/c47fe465ffeebda3f4f8d84e2aff46dac3a2b878))
* **operator:** deploy network policies with LokiStack ([#19099](https://github.com/grafana/loki/issues/19099)) ([6e6f61f](https://github.com/grafana/loki/commit/6e6f61ff9bd88bfd7e7914de48c7d14aecf7748e))
* **operator:** s3 validation reject endpoints that contain a URL path ([#19356](https://github.com/grafana/loki/issues/19356)) ([f6ef4d8](https://github.com/grafana/loki/commit/f6ef4d89fd3e6dc43dcee2ef62f2d4ecf77a4d0f))
* **operator:** Update Loki operand to v3.5.4 ([#19122](https://github.com/grafana/loki/issues/19122)) ([155972e](https://github.com/grafana/loki/commit/155972ec256501af88147c9d4da2382a0bdc2ed2))
* **operator:** Update Loki operand to v3.5.5 ([#19187](https://github.com/grafana/loki/issues/19187)) ([743929b](https://github.com/grafana/loki/commit/743929bf5537b701bb4c86203c79fa08eb68ad08))


### Bug Fixes

* **operator:** updated AlertingRule sample to make it comply with the validation we apply ([#18671](https://github.com/grafana/loki/issues/18671)) ([8e6c018](https://github.com/grafana/loki/commit/8e6c018665ae8cc692083649042ab991d472ce15))
* **operator:** upgrade OPA policy syntax for v1+ ([#18795](https://github.com/grafana/loki/issues/18795)) ([610f43e](https://github.com/grafana/loki/commit/610f43eb678cdcd537b8dcc19cfd0550c092b371))
* **operator:** Do not deploy NetworkPolicies automatically on OCP 4.20 ([#19680](https://github.com/grafana/loki/issues/19680)) ([8df33ff](https://github.com/grafana/loki/commit/8df33ff659d53d17b68fb894879587b330e63607))
* **operator:** Return quickstart script to working condition and improve rootless usage ([#19960](https://github.com/grafana/loki/issues/19960)) ([397da27](https://github.com/grafana/loki/commit/397da277753d771d8c1492dd3f4db4b208b3532d))


### Code Refactoring

* **operator:** consolidate image build workflows and improve documentation ([#19395](https://github.com/grafana/loki/issues/19395)) ([292a31e](https://github.com/grafana/loki/commit/292a31e56a36a2e2fef6afe765dbe5b0a2f8f13f))