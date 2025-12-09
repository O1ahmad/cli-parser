# containerd - v2.2.0

**Release Name**: containerd 2.2.0
**Published**: 2025-11-06T01:34:14Z
**Repository**: https://github.com/containerd/containerd

---

Welcome to the v2.2.0 release of containerd!

The second minor release of containerd 2.x focuses on continued stability alongside
new features and improvements. This is the second time-based released for containerd.

### Highlights

* **Add mount manager** ([#12063](https://github.com/containerd/containerd/pull/12063))

  The mount manager is a new service that provides lifecycle management for filesystem mounts
  to support more advanced use cases, such as:
  * **Device formatting** to create formatted filesystems (xfs, ext4) on-demand
  * **Mount activation** to prepare devices such as loopbacks or network fileystems
  * **Mount transformation** to allow mount arguments to be filled in dynamically from previous mounts
  * **Garbage collection** of mounts to ensure temporary mounts are never leaked
* **Add conf.d include in the default config** ([#12323](https://github.com/containerd/containerd/pull/12323))
* **Add support for back references in the garbage collector** ([#12025](https://github.com/containerd/containerd/pull/12025))

#### Container Runtime Interface (CRI)

* **Pod Sandbox Metrics** ([#10691](https://github.com/containerd/containerd/pull/10691))

  Full implementation of Kubernetes CRI pod-level metrics API
  * **ListPodSandboxMetrics**: Query metrics for  running pods/sandboxes
  * **ListMetricsDescriptors**: Discover available metrics and their descriptions
* **Support image volume mount subpath** ([#11578](https://github.com/containerd/containerd/pull/11578))

#### Go client

* **Update pkg/oci to use fs.FS interface and os.OpenRoot** ([#12245](https://github.com/containerd/containerd/pull/12245))

#### Image Distribution

* **Parallel Unpack**  ([#12332](https://github.com/containerd/containerd/pull/12332))

  Adds support for unpacking layers in parallel during pull operations. This feature is supported with overlayfs and EROFS snapshotters.
* **OCI Referrers Support** ([#12309](https://github.com/containerd/containerd/pull/12309))

  Adds new referrers fetcher to remote registry interface using the [new referrers endpoint added in OCI distribution-spec 1.1](https://github.com/opencontainers/distribution-spec/blob/v1.1.0/spec.md#listing-referrers)
* **Tar unpack progress through transfer service** ([#11921](https://github.com/containerd/containerd/pull/11921))

#### Image Storage

* **EROFS enhancements using mount manager** ([#12333](https://github.com/containerd/containerd/pull/12333))

  Improvements to EROFS snapshotter using the new mount manager service
  * **Quota Support**: Support for sized block devices as the upper layer for overlayfs
  * **Mount Lifecycle**: Loopback setup, block device creation, and overlayfs argument formatting is moved to the
     mount  manager to be performed on-demand or within the runtime.
  * **Mount handler**: To allow optimization of EROFS mount types based on the current system
  * **macOS Support**: EROFS snapshotter can now be used on Darwin to natively allow image pulls
  * **Tar index mode**: Efficiently generate EROFS metadata backed by original tar content ([#11919](https://github.com/containerd/containerd/pull/11919))
* **Add snapshotter and differ for block CIMs** ([#12050](https://github.com/containerd/containerd/pull/12050))

#### Node Resource Interface (NRI)

* **Enable otel traces in NRI** ([#12082](https://github.com/containerd/containerd/pull/12082))
* **Add WASM plugin support** ([containerd/nri#121](https://github.com/containerd/nri/pull/121))

#### Runtime

* **Improve shim load time after restart by loading in parallel** ([#12142](https://github.com/containerd/containerd/pull/12142))
* **Fix pidfd leak in UnshareAfterEnterUserns** ([#12167](https://github.com/containerd/containerd/pull/12167))

#### Deprecations

* **Deprecate cgroup v1** ([#12445](https://github.com/containerd/containerd/pull/12445))
* **Postpone v2.2 deprecation items to v2.3** ([#12417](https://github.com/containerd/containerd/pull/12417))

Please try out the release binaries and report any issues at
https://github.com/containerd/containerd/issues.

### Contributors

* Derek McGowan
* Phil Estes
* Akihiro Suda
* Maksym Pavlenko
* Wei Fu
* Krisztian Litkey
* Mike Brown
* Akhil Mohan
* Markus Lehtonen
* Samuel Karp
* Sebastiaan van Stijn
* ningmingxiao
* Austin Vazquez
* yashsingh74
* Gao Xiang
* Kirtana Ashok
* Jin Dong
* Chris Henzie
* Aadhar Agarwal
* Etienne Champetier
* Henry Wang
* Rodrigo Campos
* Sascha Grunert
* Aleksa Sarai
* Eric Mountain
* Keith Mattix II
* Paweł Gronowski
* Tõnis Tiigi
* Adrien Delorme
* Apurv Barve
* Enji Cooper
* Kohei Tokunaga
* Max Jonas Werner
* Rehan Khan
* Yang Yang
* jinda.ljd
* jokemanfire
* Amit Barve
* Andrew Halaney
* Antonio Ojea
* Brian Goff
* Carlos Eduardo Arango Gutierrez
* Chenyang Yan
* Dawei Wei
* Divya Rani
* Evan Anderson
* Fabiano Fidêncio
* Iceber Gu
* Jared Ledvina
* Jonathan Perkin
* Jose Fernandez
* Karl Baumgartner
* Michael Weibel
* Osama Abdelkader
* Radostin Stoyanov
* Ruidong Cao
* Sameer
* Sergey Kanzhelev
* Swagat Bora
* Sylvain MOUQUET
* Tom Wieczorek
* Tycho Andersen
* Wuyue (Tony) Sun
* suranmiao
* tanhuaan
* wheat2018
* zounengren

### Dependency Changes

* **dario.cat/mergo**                                                    v1.0.1 -> v1.0.2
* **github.com/Microsoft/hcsshim**                                       v0.13.0-rc.3 -> v0.14.0-rc.1
* **github.com/StackExchange/wmi**                                       cbe66965904d **_new_**
* **github.com/checkpoint-restore/checkpointctl**                        v1.3.0 -> v1.4.0
* **github.com/containerd/cgroups/v3**                                   v3.0.5 -> v3.1.0
* **github.com/containerd/console**                                      v1.0.4 -> v1.0.5
* **github.com/containerd/containerd/api**                               v1.9.0 -> v1.10.0
* **github.com/containerd/go-cni**                                       v1.1.12 -> v1.1.13
* **github.com/containerd/nri**                                          v0.8.0 -> v0.10.0
* **github.com/containerd/platforms**                                    v1.0.0-rc.1 -> v1.0.0-rc.2
* **github.com/containernetworking/plugins**                             v1.7.1 -> v1.8.0
* **github.com/coreos/go-systemd/v22**                                   v22.5.0 -> v22.6.0
* **github.com/cpuguy83/go-md2man/v2**                                   v2.0.5 -> v2.0.7
* **github.com/emicklei/go-restful/v3**                                  v3.11.0 -> v3.13.0
* **github.com/fxamacker/cbor/v2**                                       v2.7.0 -> v2.9.0
* **github.com/go-jose/go-jose/v4**                                      v4.0.5 -> v4.1.2
* **github.com/go-logr/logr**                                            v1.4.2 -> v1.4.3
* **github.com/go-ole/go-ole**                                           v1.2.6 **_new_**
* **github.com/golang/groupcache**                                       41bb18bfe9da -> 2c02b8208cf8
* **github.com/google/certtostore**                                      v1.0.6 **_new_**
* **github.com/google/deck**                                             105ad94aa8ae **_new_**
* **github.com/gorilla/websocket**                                       v1.5.0 -> e064f32e3674
* **github.com/grpc-ecosystem/go-grpc-middleware/providers/prometheus**  v1.0.1 -> v1.1.0
* **github.com/hashicorp/errwrap**                                       v1.1.0 **_new_**
* **github.com/intel/goresctrl**                                         v0.8.0 -> v0.10.0
* **github.com/klauspost/compress**                                      v1.18.0 -> v1.18.1
* **github.com/knqyf263/go-plugin**                                      v0.9.0 **_new_**
* **github.com/moby/sys/capability**                                     v0.4.0 **_new_**
* **github.com/modern-go/reflect2**                                      v1.0.2 -> 35a7c28c31ee
* **github.com/opencontainers/runtime-tools**                            2e043c6bd626 -> 0ea5ed0382a2
* **github.com/prometheus/client_golang**                                v1.22.0 -> v1.23.2
* **github.com/prometheus/client_model**                                 v0.6.1 -> v0.6.2
* **github.com/prometheus/common**                                       v0.62.0 -> v0.66.1
* **github.com/prometheus/procfs**                                       v0.15.1 -> v0.16.1
* **github.com/stretchr/testify**                                        v1.10.0 -> v1.11.1
* **github.com/tchap/go-patricia/v2**                                    v2.3.2 -> v2.3.3
* **github.com/tetratelabs/wazero**                                      v1.9.0 **_new_**
* **github.com/urfave/cli/v2**                                           v2.27.6 -> v2.27.7
* **github.com/vishvananda/netlink**                                     0e7078ed04c8 -> v1.3.1
* **go.etcd.io/bbolt**                                                   v1.4.0 -> v1.4.3
* **go.opentelemetry.io/otel**                                           v1.35.0 -> v1.37.0
* **go.opentelemetry.io/otel/metric**                                    v1.35.0 -> v1.37.0
* **go.opentelemetry.io/otel/sdk**                                       v1.35.0 -> v1.37.0
* **go.opentelemetry.io/otel/trace**                                     v1.35.0 -> v1.37.0
* **go.uber.org/goleak**                                                 v1.3.0 **_new_**
* **go.yaml.in/yaml/v2**                                                 v2.4.2 **_new_**
* **golang.org/x/crypto**                                                v0.36.0 -> v0.41.0
* **golang.org/x/mod**                                                   v0.24.0 -> v0.29.0
* **golang.org/x/net**                                                   v0.38.0 -> v0.43.0
* **golang.org/x/oauth2**                                                v0.27.0 -> v0.30.0
* **golang.org/x/sync**                                                  v0.14.0 -> v0.17.0
* **golang.org/x/sys**                                                   v0.33.0 -> v0.37.0
* **golang.org/x/term**                                                  v0.30.0 -> v0.34.0
* **golang.org/x/text**                                                  v0.23.0 -> v0.28.0
* **golang.org/x/time**                                                  v0.7.0 -> v0.14.0
* **google.golang.org/genproto/googleapis/api**                          56aae31c358a -> a7a43d27e69b
* **google.golang.org/genproto/googleapis/rpc**                          56aae31c358a -> a7a43d27e69b
* **google.golang.org/grpc**                                             v1.72.0 -> v1.76.0
* **google.golang.org/protobuf**                                         v1.36.6 -> v1.36.10
* **k8s.io/api**                                                         v0.32.3 -> v0.34.1
* **k8s.io/apimachinery**                                                v0.32.3 -> v0.34.1
* **k8s.io/client-go**                                                   v0.32.3 -> v0.34.1
* **k8s.io/cri-api**                                                     v0.32.3 -> v0.34.1
* **k8s.io/utils**                                                       3ea5e8cea738 -> 4c0f3b243397
* **sigs.k8s.io/json**                                                   9aa6b5e7a4b3 -> cfa47c3a1cc8
* **sigs.k8s.io/randfill**                                               v1.0.0 **_new_**
* **sigs.k8s.io/structured-merge-diff/v6**                               v6.3.0 **_new_**
* **sigs.k8s.io/yaml**                                                   v1.4.0 -> v1.6.0

Previous release can be found at [v2.1.0](https://github.com/containerd/containerd/releases/tag/v2.1.0)
### Which file should I download?
* `containerd-<VERSION>-<OS>-<ARCH>.tar.gz`:         ✅Recommended. Dynamically linked with glibc 2.35 (Ubuntu 22.04).
* `containerd-static-<VERSION>-<OS>-<ARCH>.tar.gz`:  Statically linked. Expected to be used on Linux distributions that do not use glibc >= 2.35. Not position-independent.

In addition to containerd, typically you will have to install [runc](https://github.com/opencontainers/runc/releases)
and [CNI plugins](https://github.com/containernetworking/plugins/releases) from their official sites too.

See also the [Getting Started](https://github.com/containerd/containerd/blob/main/docs/getting-started.md) documentation.
