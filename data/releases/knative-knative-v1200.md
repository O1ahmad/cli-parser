# Knative - knative-v1.20.0

**Release Name**: v1.20.0
**Published**: 2025-10-29T10:19:44Z
**Repository**: https://github.com/knative/serving

---

## 🚨 Breaking or Notable Changes

#### Metrics and Tracing

In v1.19 we've dropped support for OpenCensus (which has been deprecated for a while) in favour of OpenTelemetry. This is a breaking change and details are documented here in the [design document](https://docs.google.com/document/d/1QQ_ubc0RjeZbRHdN4rQR85Z7RZfTSjz4GoKsE0dZ2Z0/edit?pli=1&tab=t.0#heading=h.n8a530nnrb=). and the website (https://knative.dev/docs/serving/observability/metrics/collecting-metrics/)

#### Secure Pod Defaults  (#16042, @nader-ziada)

We've introduce `secure-pod-defaults` in an earlier release but this release includes a new setting `AllowRootBounded` that offers a better security posture for your workloads but balances the compatibility with images that require/expect you to run as root. 

For `v1.20` release the `secure-pod-defaults` default will remain `disabled` but in a future release (most likely `v1.21`) we will switch this default to `AllowRootBounded`. 

_If you're unsure whether your workloads will support this new setting you should explicitly set this option to `disabled` prior to upgrading to `v1.21`._

For more information see the [documentation](https://knative.dev/development/serving/configuration/secure-pod-defaults/) and reach out if you foresee issues in your testing.

## 💫 New Features & Changes

* Create a new value for `secure-pod-defaults`: `AllowRootBounded`
    - when AllowRootBounded, defaults SeccompProfile and Capabilities if nil
    - when enabled sets RunAsNonRoot to true if not already specified (#16042, @nader-ziada)
* Made it possible to configure the `httputil.ReverseProxy` or add `http.Handler`s to queue-proxy in out-of-tree builds. (#16097, @mbaynton)
* Podspec-dryrun feature flag has been removed. Dry run validation will now occur when a user opts into it using `kubectl apply --dry-run=server` (#16008, @Alexander-Kita)
* Add distinct logging for timeout types  by @thiagomedina in https://github.com/knative/serving/pull/16109
* drop unnecessary 'kn.activator.proxy' metric/span attribute by @dprotaso in https://github.com/knative/serving/pull/16045
* bump Istio to v1.27 and Contour to v1.33 by @dprotaso in https://github.com/knative/serving/pull/16099
* Keep queue-proxy admin server on HTTP for PreStop hooks by @Fedosin in https://github.com/knative/serving/pull/16163


### 🐞Bug Fixes
* Fix min-scale transition by @dprotaso in https://github.com/knative/serving/pull/16094      
* Add initialize conditions to MakePA to avoid potential race conditions by @nader-ziada in https://github.com/knative/serving/pull/16037
* For orphaned certificates if we have an issue listing just log the error by @dprotaso in https://github.com/knative/serving/pull/16096
* Fix queue proxy user metrics port by @dprotaso in https://github.com/knative/serving/pull/16018
* drop unused metrics domain env var by @dprotaso in https://github.com/knative/serving/pull/16019
* fix otelhttp setup in activator by @dprotaso in https://github.com/knative/serving/pull/16044
* Drop probe tracing in queue-proxy by @dprotaso in https://github.com/knative/serving/pull/16048
* Adjust queue proxy metric attributes by @dprotaso in https://github.com/knative/serving/pull/16049
* Serving Metric Tweaks by @dprotaso in https://github.com/knative/serving/pull/16062
* Fix: PodAutoscaler not reconciled due to missing class annotation by @nader-ziada in https://github.com/knative/serving/pull/16141


## New Contributors
* @Alexander-Kita made their first contribution in https://github.com/knative/serving/pull/16008
* @mbaynton made their first contribution in https://github.com/knative/serving/pull/16097
* @thiagomedina made their first contribution in https://github.com/knative/serving/pull/16109
* @ali-a-a made their first contribution in https://github.com/knative/serving/pull/16201

## Dependencies

<details>
<summary>Added</summary>

- github.com/prometheus/otlptranslator: [v1.0.0](https://github.com/prometheus/otlptranslator/tree/v1.0.0)
- golang.org/x/tools/go/expect: v0.1.1-deprecated
- golang.org/x/tools/go/packages/packagestest: v0.1.1-deprecated

</details>

<details>
<summary>Changed</summary>

- cel.dev/expr: v0.23.0 → v0.24.0
- cloud.google.com/go/compute/metadata: v0.6.0 → v0.7.0
- github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp: [v1.27.0 → v1.29.0](https://github.com/GoogleCloudPlatform/opentelemetry-operations-go/compare/detectors/gcp/v1.27.0...detectors/gcp/v1.29.0)
- github.com/cenkalti/backoff/v5: [v5.0.2 → v5.0.3](https://github.com/cenkalti/backoff/compare/v5.0.2...v5.0.3)
- github.com/census-instrumentation/opencensus-proto: [v0.4.1 → v0.2.1](https://github.com/census-instrumentation/opencensus-proto/compare/v0.4.1...v0.2.1)
- github.com/cncf/xds/go: [ae57f3c → 2ac532f](https://github.com/cncf/xds/compare/ae57f3c...2ac532f)
- github.com/go-jose/go-jose/v4: [v4.0.5 → v4.1.1](https://github.com/go-jose/go-jose/compare/v4.0.5...v4.1.1)
- github.com/golang/glog: [v1.2.4 → v1.2.5](https://github.com/golang/glog/compare/v1.2.4...v1.2.5)
- github.com/grpc-ecosystem/grpc-gateway/v2: [v2.27.1 → v2.27.2](https://github.com/grpc-ecosystem/grpc-gateway/compare/v2.27.1...v2.27.2)
- github.com/prometheus/client_golang: [v1.22.0 → v1.23.2](https://github.com/prometheus/client_golang/compare/v1.22.0...v1.23.2)
- github.com/prometheus/common: [v0.65.0 → v0.66.1](https://github.com/prometheus/common/compare/v0.65.0...v0.66.1)
- github.com/prometheus/procfs: [v0.16.1 → v0.17.0](https://github.com/prometheus/procfs/compare/v0.16.1...v0.17.0)
- github.com/spf13/pflag: [v1.0.6 → v1.0.10](https://github.com/spf13/pflag/compare/v1.0.6...v1.0.10)
- github.com/stretchr/testify: [v1.10.0 → v1.11.1](https://github.com/stretchr/testify/compare/v1.10.0...v1.11.1)
- go.opentelemetry.io/contrib/detectors/gcp: v1.35.0 → v1.36.0
- go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp: v0.62.0 → v0.63.0
- go.opentelemetry.io/contrib/instrumentation/runtime: v0.62.0 → v0.63.0
- go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetricgrpc: v1.37.0 → v1.38.0
- go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetrichttp: v1.37.0 → v1.38.0
- go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc: v1.37.0 → v1.38.0
- go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp: v1.37.0 → v1.38.0
- go.opentelemetry.io/otel/exporters/otlp/otlptrace: v1.37.0 → v1.38.0
- go.opentelemetry.io/otel/exporters/prometheus: v0.59.0 → v0.60.0
- go.opentelemetry.io/otel/exporters/stdout/stdouttrace: v1.37.0 → v1.38.0
- go.opentelemetry.io/otel/metric: v1.37.0 → v1.38.0
- go.opentelemetry.io/otel/sdk/metric: v1.37.0 → v1.38.0
- go.opentelemetry.io/otel/sdk: v1.37.0 → v1.38.0
- go.opentelemetry.io/otel/trace: v1.37.0 → v1.38.0
- go.opentelemetry.io/otel: v1.37.0 → v1.38.0
- go.opentelemetry.io/proto/otlp: v1.7.0 → v1.7.1
- go.yaml.in/yaml/v3: v3.0.3 → v3.0.4
- golang.org/x/crypto: v0.39.0 → v0.43.0
- golang.org/x/mod: v0.25.0 → v0.29.0
- golang.org/x/net: v0.41.0 → v0.46.0
- golang.org/x/sync: v0.15.0 → v0.17.0
- golang.org/x/sys: v0.33.0 → v0.37.0
- golang.org/x/telemetry: bda5523 → 078029d
- golang.org/x/term: v0.32.0 → v0.36.0
- golang.org/x/text: v0.26.0 → v0.30.0
- golang.org/x/tools: v0.34.0 → v0.38.0
- gonum.org/v1/gonum: 3f7ecaa → v0.16.0
- google.golang.org/genproto/googleapis/api: 513f239 → c5933d9
- google.golang.org/genproto/googleapis/rpc: 513f239 → c5933d9
- google.golang.org/grpc: v1.73.0 → v1.75.0
- google.golang.org/protobuf: v1.36.6 → v1.36.8
- k8s.io/api: v0.33.1 → v0.33.5
- k8s.io/apiextensions-apiserver: v0.33.1 → v0.33.5
- k8s.io/apimachinery: v0.33.1 → v0.33.5
- k8s.io/apiserver: v0.33.1 → v0.33.5
- k8s.io/client-go: v0.33.1 → v0.33.5
- k8s.io/code-generator: v0.33.1 → v0.33.5
- k8s.io/component-base: v0.33.1 → v0.33.5
- k8s.io/kms: v0.33.1 → v0.33.5
- knative.dev/caching: fd36b19 → 09d3ca0
- knative.dev/hack: 70d4b00 → 4fae780
- knative.dev/networking: edb1a4a → 0bde191
- knative.dev/pkg: 19d3cc2 → 7bf6feb
- sigs.k8s.io/yaml: v1.5.0 → v1.6.0

</details>

<details>

<summary>Removed</summary>

- contrib.go.opencensus.io/exporter/ocagent: 05415f1
- contrib.go.opencensus.io/exporter/prometheus: v0.4.2
- contrib.go.opencensus.io/exporter/zipkin: v0.1.2
- github.com/go-kit/log: [v0.2.1](https://github.com/go-kit/log/tree/v0.2.1)
- github.com/go-logfmt/logfmt: [v0.5.1](https://github.com/go-logfmt/logfmt/tree/v0.5.1)
- github.com/openzipkin/zipkin-go: [v0.4.3](https://github.com/openzipkin/zipkin-go/tree/v0.4.3)
- github.com/prometheus/statsd_exporter: [v0.22.7](https://github.com/prometheus/statsd_exporter/tree/v0.22.7)

</details>



**Full Changelog**: https://github.com/knative/serving/compare/knative-v1.19.0...knative-v1.20.0