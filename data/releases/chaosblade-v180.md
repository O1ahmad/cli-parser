# Chaosblade - v1.8.0

**Release Name**: v1.8.0
**Published**: 2025-10-20T03:41:49Z
**Repository**: https://github.com/chaosblade-io/chaosblade

---

## What's Changed
### chaosblade
* fix: duplicate column name pid by @xcaspar in https://github.com/chaosblade-io/chaosblade/pull/1186
* feat: Supports accessing the cluster through kubectl-proxy by @xcaspar in https://github.com/chaosblade-io/chaosblade/pull/1185
* feat: Support specifying chaosblade data file path by @xcaspar in https://github.com/chaosblade-io/chaosblade/pull/1189
* chore: upgrade to go 1.25 and fix vet&test issues by @spencercjh in https://github.com/chaosblade-io/chaosblade/pull/1215
* chore: add scripts and Makefile targets to verify and reformat go codes by @spencercjh in https://github.com/chaosblade-io/chaosblade/pull/1217
* chore: update and reformat MAINTAINERS.md by @spencercjh in https://github.com/chaosblade-io/chaosblade/pull/1219
* [Snyk] Security upgrade alpine from 3.13.7 to 3.22.2 by @xcaspar in https://github.com/chaosblade-io/chaosblade/pull/1225
* build(deps): bump golang.org/x/crypto from 0.1.0 to 0.35.0 by @dependabot[bot] in https://github.com/chaosblade-io/chaosblade/pull/1152
* build(deps): bump golang.org/x/oauth2 from 0.0.0-20200107190931-bf48bf16ab8d to 0.27.0 by @dependabot[bot] in https://github.com/chaosblade-io/chaosblade/pull/1153
* build(deps): bump golang.org/x/net from 0.1.0 to 0.38.0 by @dependabot[bot] in https://github.com/chaosblade-io/chaosblade/pull/1151
* chore: update version to v1.8.0 by @xcaspar in https://github.com/chaosblade-io/chaosblade/pull/1227

### chaosblade-exec-jvm
* chore: add maven plugin to verify and reformat Java codes by @spencercjh in https://github.com/chaosblade-io/chaosblade-exec-jvm/pull/350
* fix: Fixed the issue that the coexistence of CPU and other JVM scenar… by @xcaspar in https://github.com/chaosblade-io/chaosblade-exec-jvm/pull/351
* chore(deps): bump org.elasticsearch:elasticsearch from 7.17.23 to 8.18.8 in /chaosblade-exec-plugin/chaosblade-exec-plugin-elasticsearch by @dependabot[bot] in https://github.com/chaosblade-io/chaosblade-exec-jvm/pull/352
* feat: update sandbox version built from sandbox develop-for-20230129 … by @xcaspar in https://github.com/chaosblade-io/chaosblade-exec-jvm/pull/353
* chore: update version from 1.7.5 to 1.8.0 by @xcaspar in https://github.com/chaosblade-io/chaosblade-exec-jvm/pull/354
* chore(deps): bump com.fasterxml.jackson.core:jackson-core from 2.12.7 to 2.15.0 by @dependabot[bot] in https://github.com/chaosblade-io/chaosblade-exec-jvm/pull/346

### chaosblade-exec-os
* feat: Introduce `replace` flag to `network dns` for domain name conflict resolution by @spencercjh in https://github.com/chaosblade-io/chaosblade-exec-os/pull/191
* fix: actually support Windows by @spencercjh in https://github.com/chaosblade-io/chaosblade-exec-os/pull/195
* chore: upgrade to go 1.25 and fix go vet issues by @spencercjh in https://github.com/chaosblade-io/chaosblade-exec-os/pull/194
* fix: network loss 100% exclude-port and exclude-ip not take effect by @chaoyuanning in https://github.com/chaosblade-io/chaosblade-exec-os/pull/193
* fix: blade create file append date output by @chaoyuanning in https://github.com/chaosblade-io/chaosblade-exec-os/pull/190
* chore: add scripts and Makefile targets to verify and reformat go codes by @spencercjh in https://github.com/chaosblade-io/chaosblade-exec-os/pull/196
* Fix: fix the cmd args info for chaosblade-exec-os by @zhangxuan321 in https://github.com/chaosblade-io/chaosblade-exec-os/pull/197
* add feature file load by @arthur657834 in https://github.com/chaosblade-io/chaosblade-exec-os/pull/199
* fix: properly handle CPU occupy Percentage When CPU Quota is Less Than 1 by @spencercjh in https://github.com/chaosblade-io/chaosblade-exec-os/pull/200
* fix: ensure effective CPU percent does not exceed 100% by @spencercjh in https://github.com/chaosblade-io/chaosblade-exec-os/pull/201
* fix: typos in `pkg/automaxprocs`; add more comments by @spencercjh in https://github.com/chaosblade-io/chaosblade-exec-os/pull/202

### chaosblade-exec-cri
* chore: upgrade go to 1.25 and fix go vet issues by @spencercjh in https://github.com/chaosblade-io/chaosblade-exec-cri/pull/28
* chore: add scripts and Makefile targets to verify and reformat go codes by @spencercjh in https://github.com/chaosblade-io/chaosblade-exec-cri/pull/29

### chaosblade-operator
* feat: filter out terminating pods from the pod list to inject exps by @spencercjh in https://github.com/chaosblade-io/chaosblade-operator/pull/262
* fix: unify biz to destroy network exp by @spencercjh in https://github.com/chaosblade-io/chaosblade-operator/pull/263
* chore: upgrade to go 1.25 and fix go vet issues by @spencercjh in https://github.com/chaosblade-io/chaosblade-operator/pull/264
* chore: add scripts and Makefile targets to verify and reformat go codes by @spencercjh in https://github.com/chaosblade-io/chaosblade-operator/pull/265

## New Contributors
* @dependabot[bot] made their first contribution in https://github.com/chaosblade-io/chaosblade/pull/1152
* @spencercjh made their first contribution in https://github.com/chaosblade-io/chaosblade-exec-jvm/pull/350
* @chaoyuanning made their first contribution in https://github.com/chaosblade-io/chaosblade-exec-os/pull/193
* @zhangxuan321 made their first contribution in https://github.com/chaosblade-io/chaosblade-exec-os/pull/197


### 📦 Downloads
Choose the appropriate package for your platform:

**Full Package (All Components):**
- **Linux AMD64**: `chaosblade-1.8.0-linux_amd64.tar.gz` - For 64-bit Linux systems
- **Linux ARM64**: `chaosblade-1.8.0-linux_arm64.tar.gz` - For ARM64 Linux systems
- **Darwin AMD64**: `chaosblade-1.8.0-darwin_amd64.tar.gz` - For Intel-based macOS
- **Darwin ARM64**: `chaosblade-1.8.0-darwin_arm64.tar.gz` - For Apple Silicon macOS

**Docker Images:**
- **Linux AMD64**:
    `ghcr.io/chaosblade-io/chaosblade-tool:1.8.0`
    `ghcr.io/chaosblade-io/chaosblade-operator:1.8.0`
- **Linux ARM64**:
    `ghcr.io/chaosblade-io/chaosblade-tool-arm64:1.8.0`
    `ghcr.io/chaosblade-io/chaosblade-operator-arm64:1.8.0`

### 🌐 OSS Download Links
Alternative download links from Alibaba Cloud OSS:

**Full Package (All Components):**
- [chaosblade-1.8.0-linux_amd64.tar.gz](https://chaosblade.oss-cn-hangzhou.aliyuncs.com/agent/github/1.8.0/chaosblade-1.8.0-linux_amd64.tar.gz)
- [chaosblade-1.8.0-linux_arm64.tar.gz](https://chaosblade.oss-cn-hangzhou.aliyuncs.com/agent/github/1.8.0/chaosblade-1.8.0-linux_arm64.tar.gz)
- [chaosblade-1.8.0-darwin_amd64.tar.gz](https://chaosblade.oss-cn-hangzhou.aliyuncs.com/agent/github/1.8.0/chaosblade-1.8.0-darwin_amd64.tar.gz)
- [chaosblade-1.8.0-darwin_arm64.tar.gz](https://chaosblade.oss-cn-hangzhou.aliyuncs.com/agent/github/1.8.0/chaosblade-1.8.0-darwin_arm64.tar.gz)
- [checksums.txt](https://chaosblade.oss-cn-hangzhou.aliyuncs.com/agent/github/1.8.0/checksums.txt) - SHA256 checksums

### 🔧 Installation

**From Package:**
```bash
# Extract and install
tar -xzf chaosblade-1.8.0-[platform].tar.gz
cd chaosblade-1.8.0-[platform]

# Verify installation
blade version
```

### For Kubernetes
#### Install
```
helm repo add chaosblade-io https://chaosblade-io.github.io/charts
helm install chaosblade chaosblade-io/chaosblade-operator --namespace chaosblade
```
Default image repository is `ghcr.io/chaosblade-io/chaosblade-tool` and  `ghcr.io/chaosblade-io/chaosblade-operator`, you can append `--set blade.repository` or `--set operator.repository` flag to change the image repository. For examples:
```
helm install chaosblade-operator chaosblade-io/chaosblade-operator --namespace chaosblade --set blade.repository=chaosbladeio/chaosblade-tool,operator.repository=chaosbladeio/chaosblade-operator
```
#### Uninstall
```
helm uninstall chaosblade-operator --namespace chaosblade
```


**Full Changelog**: https://github.com/chaosblade-io/chaosblade/compare/v1.7.5...v1.8.0