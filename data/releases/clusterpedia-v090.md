# Clusterpedia - v0.9.0

**Release Name**: Clusterpedia v0.9.0
**Published**: 2025-07-07T07:49:39Z
**Repository**: https://github.com/clusterpedia-io/clusterpedia

---

# Notable Changes since v0.8.0

## Global Features

### Associated Storage and Querying of Resource-Specific Events
The related PRs: (@Iceber, https://github.com/clusterpedia-io/clusterpedia/pull/783, https://github.com/clusterpedia-io/clusterpedia/pull/785, https://github.com/clusterpedia-io/clusterpedia/pull/786, https://github.com/clusterpedia-io/clusterpedia/pull/788, https://github.com/clusterpedia-io/clusterpedia/pull/787)

This feature implements the basic functionality for storing and retrieving event associations. It will be continuously iterated on based on user needs in the future.
```
apiVersion: cluster.clusterpedia.io/v1alpha2
kind: PediaCluster
metadata:
  name: cluster-example
spec:
  kubeconfig: "**base64**"
  syncResources:
    - group: ""
      resources:
      - "*"
      eventsInvolvedResources:
      - "pods"
      - "nodes"
```
Use `spec.syncResources.[].eventsInvolvedResources` to specify the resources whose events need to be synchronized.
**Note**: If `eventsInvolvedResources` includes resources that have already been synchronized, you'll need to restart the clustersynchro-manager. This behavior will be optimized in the future based on user needs.

#### Get Events
Use the search label `search.clusterpedia.io/inject-events=true` to request that the returned data includes events.
The events will be injected into the `shadow.clusterpedia.io/events` annotation.
> Note: The events are not currently sorted. Event filtering and sorting may be added in the future.
```bash
$ kubectl --cluster kpanda-global -n kpanda-system get po -l "search.clusterpedia.io/inject-events=true" -o yaml
...
- apiVersion: v1
  kind: Pod
  metadata:
    annotations:
      shadow.clusterpedia.io/cluster-name: kpanda-global
      shadow.clusterpedia.io/events: '[{"kind":"Event","apiVersion":"v1","metadata":{"name":"kpanda-clusterpedia-controller-manager-67758bb46d-mpl49.1843f13522e37ad9","namespace":"kpanda-system","uid":"2220a44a-5414-4698-bc89-16ae411f5dc1","resourceVersion":"23444068","creationTimestamp":"2025-06-23T01:49:12Z"},"involvedObject":{"kind":"Pod","namespace":"kpanda-system","name":"kpanda-clusterpedia-controller-manager-67758bb46d-mpl49","uid":"1918b3fb-cf36-4a2f-8f35-2e105210c38c","apiVersion":"v1","resourceVersion":"7019","fieldPath":"spec.containers{kpanda-clusterpedia-controller-manager}"},"reason":"Created","message":"Created container: kpanda-clusterpedia-controller-manager","source":{"component":"kubelet","host":"g-master68"},"firstTimestamp":"2025-05-29T08:11:30Z","lastTimestamp":"2025-06-23T02:57:05Z","count":393,"type":"Normal","eventTime":null,"reportingComponent":"kubelet","reportingInstance":"g-master68"},{"kind":"Event","apiVersion":"v1","metadata":{"name":"kpanda-clusterpedia-controller-manager-67758bb46d-mpl49.1843f215c90791e6","namespace":"kpanda-system","uid":"3e1417e9-68df-4b2a-947e-f8a37178429b","resourceVersion":"23444060","creationTimestamp":"2025-06-23T01:49:12Z"},"involvedObject":{"kind":"Pod","namespace":"kpanda-system","name":"kpanda-clusterpedia-controller-manager-67758bb46d-mpl49","uid":"1918b3fb-cf36-4a2f-8f35-2e105210c38c","apiVersion":"v1","resourceVersion":"7019","fieldPath":"spec.containers{kpanda-clusterpedia-controller-manager}"},"reason":"Pulled","message":"Container ....'
...
```
#### Historical Events and Cleanup Policy
Associated stored events will not be deleted when the corresponding events in the cluster are cleaned up. This means historical events will be retained permanently until the related resource itself is deleted.

### Get Cluster Authentication Info from Secrets
The related PRs: (@Iceber @scydas, https://github.com/clusterpedia-io/clusterpedia/pull/753, https://github.com/clusterpedia-io/clusterpedia/pull/747)

You need to enable the feature gate `--feature-gates=ClusterAuthenticationFromSecret=true` for both clusterpedia-apiserver and clustersynchro-manager.

Then, configure the PediaCluster and its corresponding authentication Secrets.
```yaml
apiVersion: cluster.clusterpedia.io/v1alpha2
kind: PediaCluster
metadata:
  name: cluster-example
spec:
  apiserver: "https://cluster-example.io:8080"
  authenticationFrom:
    kubeconfig:
      name: "cluster-example-auth-kubeconfig"
      key: "kubeconfig"
    ca:
      name: "cluster-example-auth"
      key: "ca.crt"
    cert:
      name: "cluster-example-auth"
      key: "client.crt"
    key:
      name: "cluster-example-auth"
      key: "client.key"
    token:
      name: "cluster-example-auth"
      key: "token"
  syncResources:
    - group: ""
      resources:
      - "*"
---
apiVersion: v1
data:
  ca.crt: LS0tLS1...base64
  client.crt: LS0tLS1...base64
  client.key: LS0tLS1...base64
kind: Secret
metadata:
  name: cluster-example-cert
  namespace: clusterpedia-system
type: Opaque
```
Note: You don’t need to configure every field in `spec.authenticationFrom`. Just provide a valid combination, such as: 1. Only kubeconfig 2. ca + cert + key 3. ca + token

Authentication Priority:
1. spec.kubeconfig > spec.cert & spec.key&spec.token > spec.authenticationFrom
2. spec.authenticationFrom: .kubeconfig > .cert & .key & .token

>   The namespace of the cluster authentication secrets must match the namespace where the Clusterpedia components are deployed.

## Clusterpedia Apiserver
* apiserver: remove admission middleware (@Iceber, https://github.com/clusterpedia-io/clusterpedia/pull/674)

### Request Forwarding
In this version, Clusterpedia supports request forwarding to member clusters. This feature is divided into two categories:
1. Proxy specific subresource requests
2. Pass through all requests directly

Stricter authentication configurations have also been introduced for this feature.

To enable it, you need to turn on the `AllowProxyRequestToClusters` feature gate and set the appropriate flags in the Clusterpedia API server.
```bash
$ ./bin/apiserver --help
Resource server flags:

      --allow-forward-unsync-resource-request
                Allow forwarding requests for unsynchronized resource types.By default, only requests for resource types configured in PediaCluster can be forwarded.
      --allow-pediacluster-config-for-proxy-request
                Allow proxy requests to use the cluster configuration from PediaCluster when authentication information cannot be got from the header.
      --allowed-proxy-subresources strings
                List of subresources that support proxying requests to the specified cluster, formatted as '[resource/subresource],[subresource],...'. Supported proxy subresources include
                "services/proxy,pods/proxy,pods/log,pods/exec,pods/attach,pods/portfowrd,nodes/proxy".
      --enable-proxy-path-for-forward-request
                Add a '/proxy' path in the API to proxy any request.
```

#### Proxying Subresource Requests
The related PRs: (@Iceber @scydas, https://github.com/clusterpedia-io/clusterpedia/pull/715, https://github.com/clusterpedia-io/clusterpedia/pull/717, https://github.com/clusterpedia-io/clusterpedia/pull/723 , https://github.com/clusterpedia-io/clusterpedia/pull/719)

Enable this by setting the `--allowed-proxy-subresources` flag in the Clusterpedia API server.
```bash
$ # Enable the proxy subresources for all resources and the exec subresources of the pods.
$ ./bin/apiserver --allowed-proxy-subresources "pods/exec,proxy"
```
Currently supported subresource requests include:
* pods/log
* pods/exec
* pods/attach
* pods/portfowrd
* pods/proxy
* nodes/proxy
* services/proxy

The usage is consistent with native Kubernetes behavior. You can use kubectl to make calls. For example:
```bash
$ kubectl --cluster cluster-example logs nginx
$ kubectl --cluster cluster-example exec -ti nginx bash
```

#### Request Forwarding
The related PRs: (@Iceber @scydas, https://github.com/clusterpedia-io/clusterpedia/pull/716, https://github.com/clusterpedia-io/clusterpedia/pull/741, https://github.com/clusterpedia-io/clusterpedia/pull/748,https://github.com/clusterpedia-io/clusterpedia/pull/750, https://github.com/clusterpedia-io/clusterpedia/pull/752)

Clusterpedia supports three ways to forward requests directly to member clusters:
1. Enable the `--enable-proxy-path-for-forward-request` flag. The API server will support proxy-style paths like:
*/apis/clusterpedia.io/v1beta1/resources/clusters/<cluster>/proxy/<forward path>*
2. Use the HTTP header: `X-CLUSTERPEDIA-FORWARD: true`
3. For list requests, use the search label —— `search.clusterpedia.io/forward` to enable forwarding.

```yaml
# kubeconfig
- cluster:
    insecure-skip-tls-verify: true
    server: https://127.0.0.1:8443/apis/clusterpedia.io/v1beta1/resources/clusters/cluster-example/
  name: cluster-example
- cluster:
    insecure-skip-tls-verify: true
    server: https://127.0.0.1:8443/apis/clusterpedia.io/v1beta1/resources/clusters/cluster-example/proxy
  name: cluster-example-proxy
```
```bash
$ kubectl --cluster cluster-example-proxy get po -A

$ kubectl --cluster cluster-example get po -l search.clusterpedia.io/forward=true

$ curl -v -k --cert-type P12 --cert client.p12:password  -H "X-CLUSTERPEDIA-FORWARD: true" "https://localhost:8443/apis/clusterpedia.io/v1beta1/resources/clusters/cluster-example/api/v1/namespaces/clusterpedia-system/pods"
```
You can enable a more relaxed mode by setting the `--allow-forward-unsync-resource-request` flag to allow forwarding requests for unsynchronized resources.

#### Authentication for Proxy Requests
* apiserver: set proxy auth info via request header (@Iceber, https://github.com/clusterpedia-io/clusterpedia/pull/727)

By default, proxy requests require authentication headers to be passed in the request for the target cluster. These headers include the necessary credentials.
1. X-Clusterpedia-Proxy-CA
2. X-Clusterpedia-Proxy-Token
3. X-Clusterpedia-Proxy-Client-Cert
4. X-Clusterpedia-Proxy-Client-Key

Alternatively, you can enable `--allow-pediacluster-config-for-proxy-request` to reuse the authentication config defined in the PediaCluster.

### Observability
* fix otel trace handler WithTracing (@KubeKyrie, https://github.com/clusterpedia-io/clusterpedia/pull/638)
* feat: add pprof router (@jiuker, https://github.com/clusterpedia-io/clusterpedia/pull/646)
* New flags have been added for metrics (@scydas, https://github.com/clusterpedia-io/clusterpedia/pull/696)
```bash
$ ./bin/apiserver --help
...
Metrics flags:

      --allow-metric-labels stringToString
                The map from metric-label to value allow-list of this label. The key's format is <MetricName>,<LabelName>. The value's format is <allowed_value>,<allowed_value>...e.g.
                metric1,label1='v1,v2,v3', metric1,label2='v1,v2,v3' metric2,label1='v1,v2,v3'. (default [])
      --allow-metric-labels-manifest string
                The path to the manifest file that contains the allow-list mapping. The format of the file is the same as the flag --allow-metric-labels. Note that the flag --allow-metric-labels will
                override the manifest file.
      --disabled-metrics strings
                This flag provides an escape hatch for misbehaving metrics. You must provide the fully qualified metric name in order to disable it. Disclaimer: disabling metrics is higher in precedence
                than showing hidden metrics.
      --show-hidden-metrics-for-version string
                The previous version for which you want to show hidden metrics. Only the previous minor version is meaningful, other values will not be allowed. The format is <major>.<minor>, e.g.:
                '1.16'. The purpose of this format is make sure you have the opportunity to notice if the next release hides additional metrics, rather than being surprised when they are permanently
                removed in the release after that.
...
```

* Metrics now include build info for both Clusterpedia API server and Kubernetes (@Iceber, https://github.com/clusterpedia-io/clusterpedia/pull/695, https://github.com/clusterpedia-io/clusterpedia/pull/694)
```
# HELP clusterpedia_build_info [ALPHA] A metric with a constant '1' value labeled by git version, git commit, git tree state, build date, Go version, and compiler from which Clusterpedia was built, and platform on which it is running.
# TYPE clusterpedia_build_info gauge
clusterpedia_build_info{build_date="2025-06-17T07:06:13Z",compiler="gc",git_commit="ee85edb72c541ece9e0b2d7da54c0f442e9a1536",git_tree_state="clean",git_version="v0.9.0-beta.0",go_version="go1.23.10",platform="linux/arm64"} 1
# HELP kubernetes_build_info [ALPHA] A metric with a constant '1' value labeled by major, minor, git version, git commit, git tree state, build date, Go version, and compiler from which Kubernetes was built, and platform on which it is running.
# TYPE kubernetes_build_info gauge
kubernetes_build_info{build_date="2025-06-17T07:06:13Z",compiler="gc",git_commit="ee85edb72c541ece9e0b2d7da54c0f442e9a1536",git_tree_state="clean",git_version="v1.31.2",go_version="go1.23.10",major="1",minor="31",platform="linux/arm64"} 1
```

### Other
* fix the version order of 'discovery.k8s.io' (@Iceber, https://github.com/clusterpedia-io/clusterpedia/pull/659)
* kubeapiserver: allow using the storage version in request handling (@Iceber, https://github.com/clusterpedia-io/clusterpedia/pull/771)
* install storagemigration group to LegacyResourceScheme (@Iceber, https://github.com/clusterpedia-io/clusterpedia/pull/672)

## Cluster Storage Layer
### Internal Storage Observability
* Metrics support added for gorm and database connections (@Iceber @scydas, https://github.com/clusterpedia-io/clusterpedia/pull/711, https://github.com/clusterpedia-io/clusterpedia/pull/712, https://github.com/clusterpedia-io/clusterpedia/pull/713)

Metrics with prefix **storage_dbstats** are now available.
```
 HELP storage_dbstats_idle The number of idle connections.
# TYPE storage_dbstats_idle gauge
 storage_dbstats_idle{db_name="clusterpedia"} 1
# HELP storage_dbstats_in_use The number of connections currently in use.
# TYPE storage_dbstats_in_use gauge
 storage_dbstats_in_use{db_name="clusterpedia"} 0
# HELP storage_dbstats_max_idle_closed The total number of connections closed due to SetMaxIdleConns.
# TYPE storage_dbstats_max_idle_closed gauge
 storage_dbstats_max_idle_closed{db_name="clusterpedia"} 0
# HELP storage_dbstats_max_idletime_closed The total number of connections closed due to SetConnMaxIdleTime.
# TYPE storage_dbstats_max_idletime_closed gauge
...
```

* internalstorage: add trace (@scydas, https://github.com/clusterpedia-io/clusterpedia/pull/714)

### Other
* A shutdown function has been added to the storage factory to allow manual release of the connection pool (@learner0810 @scydas, https://github.com/clusterpedia-io/clusterpedia/pull/724, https://github.com/clusterpedia-io/clusterpedia/pull/749)
* support for storage to implement custom resource synchro (@Iceber, https://github.com/clusterpedia-io/clusterpedia/pull/677)

#### Memory Storage
* support cluster filter when use memory storage (@huiwq1990, https://github.com/clusterpedia-io/clusterpedia/pull/649)
* memorystorage: fix deleting cluster info when cleaning a resource (@Iceber, https://github.com/clusterpedia-io/clusterpedia/pull/706)

## Clustersynchro Manager
* clustersynchro: add initial list phase (@Iceber, https://github.com/clusterpedia-io/clusterpedia/pull/791)

If a resource is in the `status.resources[].initialListPhase` state, it means that the cluster data in Clusterpedia Storage is still being initialized and not yet consistent with the source cluster.

* clustersynchro: add resource synchro metrics (@Iceber, https://github.com/clusterpedia-io/clusterpedia/pull/718)

## Dependency Upgrades
* Go version upgraded from 1.21.5 to 1.23.10 (@Iceber @dependabot, https://github.com/clusterpedia-io/clusterpedia/pull/640, https://github.com/clusterpedia-io/clusterpedia/pull/689, https://github.com/clusterpedia-io/clusterpedia/pull/697, https://github.com/clusterpedia-io/clusterpedia/pull/701, https://github.com/clusterpedia-io/clusterpedia/pull/702, https://github.com/clusterpedia-io/clusterpedia/pull/722, https://github.com/clusterpedia-io/clusterpedia/pull/725, https://github.com/clusterpedia-io/clusterpedia/pull/793)
* Alpine base image upgraded from 3.18.5 to 3.21.3 (@Iceber @dependabot, https://github.com/clusterpedia-io/clusterpedia/pull/688, https://github.com/clusterpedia-io/clusterpedia/pull/698, https://github.com/clusterpedia-io/clusterpedia/pull/720, https://github.com/clusterpedia-io/clusterpedia/pull/721, https://github.com/clusterpedia-io/clusterpedia/pull/728
* gorm.io dependencies upgrade (@Iceber, https://github.com/clusterpedia-io/clusterpedia/pull/767, https://github.com/clusterpedia-io/clusterpedia/pull/768, https://github.com/clusterpedia-io/clusterpedia/pull/769, https://github.com/clusterpedia-io/clusterpedia/pull/772, https://github.com/clusterpedia-io/clusterpedia/pull/793)

|dependency|old version| new version|
|----------|-----------|------------|
|gorm.io/gorm|v1.24.1|1.30.0
|gorm.io/driver/mysql|v1.4.4|v1.6.0
|gorm.io/driver/postgres|v1.4.5|v1.6.0
|gorm.io/driver/sqlite|v1.4.4|v1.6.0
|gorm.io/datatypes|v1.0.7|v1.2.5
|github.com/jackc/pgx|v4.17.2|v5.7.5
|github.com/go-sql-driver/mysql|v1.6.0|v1.9.3

* Kubernetes version upgraded from v1.30.2 to v1.31.2 (@Iceber, https://github.com/clusterpedia-io/clusterpedia/pull/668, https://github.com/clusterpedia-io/clusterpedia/pull/691, https://github.com/clusterpedia-io/clusterpedia/pull/704)

## Contributers
Thanks everyone who contributed to this release!

The following users (sort alphabetically) are those who committed much in this release. Thank you!
* @dependabot
* @googs1025
* @huiwq1990
* @Iceber
* @jiuker
* @KubeKyrie
* @learner0810
* @mayur-tolexo
* @pacoxu
* @scydas
* @wzshiming