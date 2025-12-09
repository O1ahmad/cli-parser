# Tetragon - v1.6.0

**Release Name**: v1.6.0
**Published**: 2025-10-23T10:53:08Z
**Repository**: https://github.com/cilium/tetragon

---

# Changes from v1.5.0 to v1.6.0

**All contributions** - total: 362 commits, prs: 187 pr commits: 362
**Excluding cilium-renovate[bot]** - total: 288 commits, prs: 114 pr commits: 288

## Upgrade notes

Read the upgrade notes carefully before upgrading Tetragon.
Depending on your setup, changes listed here might require a manual intervention.

### Helm Values

* The `tetragonOperator.securityContext` field has been deprecated in favor of `tetragonOperator.containerSecurityContext` for clarity. The old field is still supported for backward compatibility but might be removed in a future release. Users should migrate their configurations to use the new field.

* The Tetragon Operator now defaults to running as a non-root user (UID 65532) for improved security. A new `tetragonOperator.runAsRoot` option has been added to override this behavior and run as root when needed. Set `tetragonOperator.runAsRoot: true` to maintain the previous root-based behavior if required.

## Changelog

### Bugfixes

* Fix bug in process modeling where long executable filenames may cause command-line argument capture corruption. (https://github.com/cilium/tetragon/pull/3972) by @acamatcisco
* helm: Quote tetragon.processAncestors.enabled (https://github.com/cilium/tetragon/pull/4013) by @michi-covalent
* selectors: Ignore empty matchBinaries (https://github.com/cilium/tetragon/pull/4022) by @tpapagian
* pkg/cgroups/fsscan: fix incorrect path returned (https://github.com/cilium/tetragon/pull/4117) by @mtardy
* pkg/crdutils: fix standalone custom resources validation (https://github.com/cilium/tetragon/pull/4140) by @mtardy
* selectors: fix off by one bounds check (https://github.com/cilium/tetragon/pull/4170) by @andrewstrohman

### Minor Changes

* option: Remove deprecated enable-process-ancestors boolean flags (https://github.com/cilium/tetragon/pull/3955) by @t0x01
* tetragon: Enable TestTracepointLoadFormat on 6.1 and bpf-next (https://github.com/cilium/tetragon/pull/3978) by @olsajiri
* More robust process argument parsing logic. (https://github.com/cilium/tetragon/pull/3974) by @acamatcisco
* tetragon: Add usdt sensor (https://github.com/cilium/tetragon/pull/3943) by @olsajiri
* tetragon: Change generic usdt op number (https://github.com/cilium/tetragon/pull/4000) by @olsajiri
* k8s: Enable k8s control plane for non-k8s deployment (https://github.com/cilium/tetragon/pull/4011) by @sayboras
* tetragon: assorted fixes (https://github.com/cilium/tetragon/pull/4023) by @olsajiri
* fix: reject NotifyEnforcer kprobe action without an Enforcer (https://github.com/cilium/tetragon/pull/4008) by @dwindsor
* tetragon: Make TestUsdtArgs amd64 only (https://github.com/cilium/tetragon/pull/4047) by @olsajiri
* fix: detectUprobeRefCtrOffsetOnce init logic (https://github.com/cilium/tetragon/pull/4036) by @zeyuwzy
* bpf: turn environment configuration storage into a BPF ARRAY storage (https://github.com/cilium/tetragon/pull/4035) by @tixxdz
* new(tetra/getevents): allow to filter events by container name regex. (https://github.com/cilium/tetragon/pull/4051) by @FedeDP
* assorted fixes (https://github.com/cilium/tetragon/pull/4053) by @olsajiri
* api: Add pod uid field for k8s Pod (https://github.com/cilium/tetragon/pull/4069) by @sayboras
* k8s: Reduce RBAC permission for non-k8s deployment (https://github.com/cilium/tetragon/pull/4060) by @sayboras
* tetragon: support for current task data (https://github.com/cilium/tetragon/pull/4064) by @olsajiri
* tetragon: add usdt action support (https://github.com/cilium/tetragon/pull/4078) by @olsajiri
* tracingpolicy: add counters about actions performed for every policy (https://github.com/cilium/tetragon/pull/4074) by @kkourt
* helm: run the Tetragon operator as non-root by default (https://github.com/cilium/tetragon/pull/3909) by @calghar
* tetra: add "probe config" command to check kernel configuration. (https://github.com/cilium/tetragon/pull/4020) by @zeyuwzy
* tetragon: allow to parse usdt sib argument (https://github.com/cilium/tetragon/pull/4095) by @olsajiri
* tetragon: Fix TestControllerSuite flake panic (https://github.com/cilium/tetragon/pull/4110) by @olsajiri
* tetragon: Fix struct perf_event_info_type layout (https://github.com/cilium/tetragon/pull/4126) by @olsajiri
* kprobe: Add support for bpf_prog argument (https://github.com/cilium/tetragon/pull/4124) by @tpapagian
* tetragon: add range filter (https://github.com/cilium/tetragon/pull/4109) by @olsajiri
* tetragon: Fix k8s validation of ArgSelector fields (https://github.com/cilium/tetragon/pull/4143) by @olsajiri
* Adds support for bpf ring buffer and sets that as the default from kernels v5.11 onwards. (https://github.com/cilium/tetragon/pull/4075) by @kevsecurity
* k8s: Add retry support for ControllerManager (https://github.com/cilium/tetragon/pull/4135) by @shpalani
* feat: add nameOverride support for tetragon-rthooks (https://github.com/cilium/tetragon/pull/4134) by @EfratRub
* tetragon: remove unused execve event flags bits (https://github.com/cilium/tetragon/pull/4138) by @olsajiri
* fix: Controller manager retry logic (https://github.com/cilium/tetragon/pull/4153) by @shpalani
* tetragon: add support for usdt set action (https://github.com/cilium/tetragon/pull/4005) by @olsajiri
* tetragon: assorted fixes (https://github.com/cilium/tetragon/pull/4155) by @olsajiri
* Helm chart: add support for export.stdout.envFromSecrets to inject environment variables from Kubernetes secrets (https://github.com/cilium/tetragon/pull/4025) by @Bagautdino
* tetragon: uprobe fixes (https://github.com/cilium/tetragon/pull/4172) by @olsajiri
* Dockerfile.clang: upgrade to clang-20 (https://github.com/cilium/tetragon/pull/4196) by @olsajiri
* tetragon: assorted fixes (https://github.com/cilium/tetragon/pull/4131) by @olsajiri
* policies: support for resolve: in USDT policies (https://github.com/cilium/tetragon/pull/4198) by @kkourt
* tetragon: add uprobe override action (https://github.com/cilium/tetragon/pull/4173) by @olsajiri
* tetragon: Add missing switch break to do_action (https://github.com/cilium/tetragon/pull/4218) by @olsajiri

### CI Changes

* renovate: Remove manual step for cilium/cilium dep (https://github.com/cilium/tetragon/pull/3966) by @sayboras
* ci: Re-enable label checker in ARM (https://github.com/cilium/tetragon/pull/3968) by @sayboras
* fix: Resolve error message typo in TestHelperMain(). (https://github.com/cilium/tetragon/pull/3975) by @acamatcisco
* pin alexellis/arkade-get github action by hash (https://github.com/cilium/tetragon/pull/3986) by @datosh
* renovate: sync helm chart version/appVersion update with image tag (https://github.com/cilium/tetragon/pull/4027) by @alero-awani
* chore(ci): always use `actions/setup-go` after repo clone. (https://github.com/cilium/tetragon/pull/4054) by @FedeDP
* Makefile alias for docs generation and renovate config update (https://github.com/cilium/tetragon/pull/4112) by @mtardy
* Makefile: add checkpatch target (https://github.com/cilium/tetragon/pull/4125) by @mtardy
* Fix flaky downloads of eBPF for Windows deps (https://github.com/cilium/tetragon/pull/4128) by @ygvalent
* ci: always upload Go test artifacts for easier debugging (https://github.com/cilium/tetragon/pull/4133) by @AritraDey-Dev
* check-links: fix the periodic check issue creation (https://github.com/cilium/tetragon/pull/4183) by @mtardy
* vmtests: add kernel 6.12 to test matrix (https://github.com/cilium/tetragon/pull/4235) by @AritraDey-Dev

### Documentation changes

* Update tetragon enteprise URL (https://github.com/cilium/tetragon/pull/3954) by @saintdle
* Fix a typo in kubectl in the runtime hook documentation (https://github.com/cilium/tetragon/pull/3957) by @uhlhosting
* docs: improve path retrieval limits formatting (https://github.com/cilium/tetragon/pull/3989) by @UtkarshSiddhpura
* docs: Fix swapped event filters descriptions (https://github.com/cilium/tetragon/pull/4003) by @t0x01
* docs: fix the yaml indent in selector semantics (https://github.com/cilium/tetragon/pull/4094) by @kemingy
* Adds Tracing Policy API reference documentation (https://github.com/cilium/tetragon/pull/4059) by @bschaatsbergen
* doc: add contribution ladder section (https://github.com/cilium/tetragon/pull/4123) by @paularah
* Chore: Add KubeCon NA 2025 to Announcement banner (https://github.com/cilium/tetragon/pull/4142) by @thisisobate
* docs: fix broken link in docs detected by the periodic check (https://github.com/cilium/tetragon/pull/4181) by @mtardy
* ARM64 users: Tetragon may run on v4.19/v5.4 kernels with limited functionality; use v5.10 or later. (https://github.com/cilium/tetragon/pull/4206) by @AritraDey-Dev
* Documentation Fix: Correct followChildren Example (https://github.com/cilium/tetragon/pull/4232) by @ossie-git

### Dependency updates

* chore(deps): update module github.com/docker/docker to v28.3.3+incompatible [security] (main) (https://github.com/cilium/tetragon/pull/3958) by @cilium-renovate[bot]
* chore(deps): update renovatebot/github-action action to v43 (main) (https://github.com/cilium/tetragon/pull/3965) by @cilium-renovate[bot]
* chore(deps): update module github.com/cilium/cilium to v1.18.0 (main) (https://github.com/cilium/tetragon/pull/3964) by @cilium-renovate[bot]
* chore(deps): update all github action dependencies (main) (https://github.com/cilium/tetragon/pull/3963) by @cilium-renovate[bot]
* chore(deps): update all lvh-images main (main) (patch) (https://github.com/cilium/tetragon/pull/3970) by @cilium-renovate[bot]
* chore(deps): update dependency cilium/cilium-cli to v0.18.6 (main) (https://github.com/cilium/tetragon/pull/3976) by @cilium-renovate[bot]
* fix(deps): update module github.com/prometheus/client_golang to v1.23.0 (main) (https://github.com/cilium/tetragon/pull/3977) by @cilium-renovate[bot]
* chore(deps): update all lvh-images main (main) (patch) (https://github.com/cilium/tetragon/pull/3981) by @cilium-renovate[bot]
* chore(deps): update docker.io/golangci/golangci-lint docker tag to v2.3.1 (main) (https://github.com/cilium/tetragon/pull/3982) by @cilium-renovate[bot]
* chore(deps): update go to v1.24.6 (main) (patch) (https://github.com/cilium/tetragon/pull/3990) by @cilium-renovate[bot]
* chore(deps): update all lvh-images main (main) (patch) (https://github.com/cilium/tetragon/pull/3995) by @cilium-renovate[bot]
* fix(deps): update module google.golang.org/protobuf to v1.36.7 (main) (https://github.com/cilium/tetragon/pull/3997) by @cilium-renovate[bot]
* fix(deps): update all go dependencies main (main) (minor) (https://github.com/cilium/tetragon/pull/3999) by @cilium-renovate[bot]
* chore(deps): update all lvh-images main (main) (patch) (https://github.com/cilium/tetragon/pull/4002) by @cilium-renovate[bot]
* chore(deps): update docker.io/golangci/golangci-lint docker tag to v2.4.0 (main) (https://github.com/cilium/tetragon/pull/4010) by @cilium-renovate[bot]
* chore(deps): update go to v1.25.0 (main) (minor) (https://github.com/cilium/tetragon/pull/4009) by @cilium-renovate[bot]
* chore(deps): update all lvh-images main (main) (patch) (https://github.com/cilium/tetragon/pull/4014) by @cilium-renovate[bot]
* chore(deps): update dependency helm/helm to v3.18.5 (main) (https://github.com/cilium/tetragon/pull/4015) by @cilium-renovate[bot]
* fix(deps): update kubernetes packages to v0.33.4 (main) (patch) (https://github.com/cilium/tetragon/pull/4018) by @cilium-renovate[bot]
* chore(deps): update dependency kubernetes/kubernetes to v1.33.4 (main) (https://github.com/cilium/tetragon/pull/4017) by @cilium-renovate[bot]
* chore(deps): update docker.io/alpine/helm docker tag to v3.18.5 (main) (https://github.com/cilium/tetragon/pull/4021) by @cilium-renovate[bot]
* chore(deps): update dependency helm/helm to v3.18.6 (main) (https://github.com/cilium/tetragon/pull/4030) by @cilium-renovate[bot]
* fix(deps): update module google.golang.org/protobuf to v1.36.8 (main) (https://github.com/cilium/tetragon/pull/4031) by @cilium-renovate[bot]
* fix(deps): update module google.golang.org/grpc to v1.75.0 (main) (https://github.com/cilium/tetragon/pull/4033) by @cilium-renovate[bot]
* chore(deps): update all lvh-images main (main) (patch) (https://github.com/cilium/tetragon/pull/4037) by @cilium-renovate[bot]
* fix(deps): update module github.com/stretchr/testify to v1.11.0 (main) (https://github.com/cilium/tetragon/pull/4040) by @cilium-renovate[bot]
* chore(deps): update docker.io/alpine/helm docker tag to v3.18.6 (main) (https://github.com/cilium/tetragon/pull/4038) by @cilium-renovate[bot]
* chore(deps): update actions/download-artifact action to v5 (main) (https://github.com/cilium/tetragon/pull/4044) by @cilium-renovate[bot]
* chore(deps): update actions/upload-pages-artifact action to v4 (main) (https://github.com/cilium/tetragon/pull/4045) by @cilium-renovate[bot]
* chore(deps): update dependency kubernetes/kubernetes to v1.34.0 (main) (https://github.com/cilium/tetragon/pull/4062) by @cilium-renovate[bot]
* chore(deps): update kindest/node docker tag to v1.34.0 (main) (https://github.com/cilium/tetragon/pull/4063) by @cilium-renovate[bot]
* chore(deps): update dependency kubernetes-sigs/kind to v0.30.0 (main) (https://github.com/cilium/tetragon/pull/4065) by @cilium-renovate[bot]
* chore(deps): update actions/checkout action to v5 (main) (https://github.com/cilium/tetragon/pull/4043) by @cilium-renovate[bot]
* fix(deps): update all rthook go dependencies main (main) (patch) (https://github.com/cilium/tetragon/pull/4061) by @cilium-renovate[bot]
* chore(deps): update all github action dependencies (main) (https://github.com/cilium/tetragon/pull/4042) by @cilium-renovate[bot]
* fix(deps): update module github.com/stretchr/testify to v1.11.1 (main) (https://github.com/cilium/tetragon/pull/4068) by @cilium-renovate[bot]
* chore(deps): update all lvh-images main (main) (patch) (https://github.com/cilium/tetragon/pull/4066) by @cilium-renovate[bot]
* fix(deps): update module github.com/containerd/nri to v0.10.0 (main) (https://github.com/cilium/tetragon/pull/4032) by @cilium-renovate[bot]
* fix(deps): update module github.com/spf13/pflag to v1.0.9 (main) (https://github.com/cilium/tetragon/pull/4072) by @cilium-renovate[bot]
* chore(deps): update all lvh-images main (main) (patch) (https://github.com/cilium/tetragon/pull/4071) by @cilium-renovate[bot]
* fix(deps): update module github.com/spf13/cobra to v1.10.1 (main) (https://github.com/cilium/tetragon/pull/4073) by @cilium-renovate[bot]
* chore(deps): update all lvh-images main (main) (patch) (https://github.com/cilium/tetragon/pull/4083) by @cilium-renovate[bot]
* chore(deps): update go to v1.25.1 (main) (patch) (https://github.com/cilium/tetragon/pull/4084) by @cilium-renovate[bot]
* fix(deps): update all rthook go dependencies main (main) (patch) (https://github.com/cilium/tetragon/pull/4086) by @cilium-renovate[bot]
* fix(deps): update all go dependencies main (main) (minor) (https://github.com/cilium/tetragon/pull/4091) by @cilium-renovate[bot]
* fix(deps): update module golang.org/x/sync to v0.17.0 (main) (https://github.com/cilium/tetragon/pull/4092) by @cilium-renovate[bot]
* fix(deps): update all go dependencies main (main) (patch) (https://github.com/cilium/tetragon/pull/4085) by @cilium-renovate[bot]
* fix(deps): update module github.com/spf13/viper to v1.21.0 (main) (https://github.com/cilium/tetragon/pull/4096) by @cilium-renovate[bot]
* chore(deps): update docker.io/mikefarah/yq docker tag to v4.47.2 (main) (https://github.com/cilium/tetragon/pull/4097) by @cilium-renovate[bot]
* chore(deps): update dependency helm/helm to v3.19.0 (main) (https://github.com/cilium/tetragon/pull/4105) by @cilium-renovate[bot]
* chore(deps): update dependency kubernetes/kubernetes to v1.34.1 (main) (https://github.com/cilium/tetragon/pull/4100) by @cilium-renovate[bot]
* chore(deps): update all lvh-images main (main) (patch) (https://github.com/cilium/tetragon/pull/4099) by @cilium-renovate[bot]
* fix(deps): update all api go dependencies main (main) (patch) (https://github.com/cilium/tetragon/pull/4101) by @cilium-renovate[bot]
* chore(deps): update docker.io/alpine/helm docker tag to v3.19.0 (main) (https://github.com/cilium/tetragon/pull/4111) by @cilium-renovate[bot]
* fix(deps): update kubernetes packages to v0.33.5 (main) (patch) (https://github.com/cilium/tetragon/pull/4103) by @cilium-renovate[bot]
* chore(deps): update all lvh-images main (main) (patch) (https://github.com/cilium/tetragon/pull/4121) by @cilium-renovate[bot]
* chore(deps): update docker.io/golangci/golangci-lint docker tag to v2.5.0 (main) (https://github.com/cilium/tetragon/pull/4122) by @cilium-renovate[bot]
* chore(deps): update all lvh-images main (main) (patch) (https://github.com/cilium/tetragon/pull/4129) by @cilium-renovate[bot]
* fix(deps): update module google.golang.org/protobuf to v1.36.10 (main) (https://github.com/cilium/tetragon/pull/4144) by @cilium-renovate[bot]
* fix(deps): update module google.golang.org/grpc to v1.76.0 (main) (https://github.com/cilium/tetragon/pull/4148) by @cilium-renovate[bot]
* chore(deps): update dependency kubernetes-sigs/bom to v0.7.1 (main) (https://github.com/cilium/tetragon/pull/4130) by @cilium-renovate[bot]
* chore(deps): update all lvh-images main (main) (patch) (https://github.com/cilium/tetragon/pull/4137) by @cilium-renovate[bot]
* chore(deps): update go to v1.25.2 (main) (patch) (https://github.com/cilium/tetragon/pull/4160) by @cilium-renovate[bot]
* fix(deps): update all go dependencies main (main) (minor) (https://github.com/cilium/tetragon/pull/4162) by @cilium-renovate[bot]
* chore(deps): update all lvh-images main (main) (patch) (https://github.com/cilium/tetragon/pull/4163) by @cilium-renovate[bot]
* chore(deps): update docker.io/python docker tag to v3.14 (main) (https://github.com/cilium/tetragon/pull/4161) by @cilium-renovate[bot]
* chore(deps): update docker.io/library/alpine docker tag to v3.22.2 (main) (https://github.com/cilium/tetragon/pull/4159) by @cilium-renovate[bot]
* chore(deps): update docker.io/mikefarah/yq docker tag to v4.48.1 (main) (https://github.com/cilium/tetragon/pull/4175) by @cilium-renovate[bot]
* chore(deps): update all github action dependencies to v6 (main) (major) (https://github.com/cilium/tetragon/pull/4177) by @cilium-renovate[bot]
* chore(deps): update actions/setup-node action to v5 (main) (https://github.com/cilium/tetragon/pull/4182) by @cilium-renovate[bot]
* chore(deps): update go to v1.25.3 (main) (patch) (https://github.com/cilium/tetragon/pull/4187) by @cilium-renovate[bot]
* fix(deps): update module github.com/cilium/little-vm-helper to v0.0.27 (main) (https://github.com/cilium/tetragon/pull/4197) by @cilium-renovate[bot]
* fix(deps): update module github.com/prometheus/common to v0.67.1 (main) (https://github.com/cilium/tetragon/pull/4224) by @cilium-renovate[bot]
* fix(deps): update module github.com/prometheus/procfs to v0.18.0 (main) (https://github.com/cilium/tetragon/pull/4237) by @cilium-renovate[bot]

### Misc Changes

* Prepare for v1.5.0 release (https://github.com/cilium/tetragon/pull/3950) by @tpapagian
* Starting v1.6 development (https://github.com/cilium/tetragon/pull/3951) by @tpapagian
* Restore upgrade notes in v1.5.0.md (https://github.com/cilium/tetragon/pull/3953) by @tpapagian
* bpf: remove unused func UpdateElementFromPointers (https://github.com/cilium/tetragon/pull/3952) by @tklauser
* fix: Refactor SIZEOF_EVENT constant to not be a hard-coded value. (https://github.com/cilium/tetragon/pull/3956) by @acamatcisco
* rthooks: Log container ID as a key-value pair (https://github.com/cilium/tetragon/pull/3962) by @michi-covalent
* Update release template (https://github.com/cilium/tetragon/pull/3973) by @tpapagian
* lint: Ignore error check for cgroups.DiscoverSubSysIds call (https://github.com/cilium/tetragon/pull/3969) by @sayboras
* deps: remove direct gopkg.in/yaml.v2 dep (https://github.com/cilium/tetragon/pull/3984) by @mtardy
* fix: Remove unused constants from bpf/lib/process.h (https://github.com/cilium/tetragon/pull/3979) by @acamatcisco
* e2e: Remove Cilium related flags (https://github.com/cilium/tetragon/pull/3987) by @sayboras
* USDT ancestors support (https://github.com/cilium/tetragon/pull/3994) by @t0x01
* pkg/cgroups/fsscan: add FindPodPath (https://github.com/cilium/tetragon/pull/3988) by @mtardy
* contrib: Remove Vagrantfile and related docs (https://github.com/cilium/tetragon/pull/4004) by @sayboras
* chore: Update goimport config with local-prefixes for consistency (https://github.com/cilium/tetragon/pull/4001) by @sayboras
* helm: Add 'containers.extra' helper function (https://github.com/cilium/tetragon/pull/4029) by @michi-covalent
* renovate: Allow go 1.24 for v1.3 branch (https://github.com/cilium/tetragon/pull/4019) by @sayboras
* linters/staticcheck: fix underscore in names (https://github.com/cilium/tetragon/pull/3983) by @mtardy
* helm: Add a Role for tetragon service account (https://github.com/cilium/tetragon/pull/4055) by @michi-covalent
* Optimize Kprobe Rate Limit Test Performance (https://github.com/cilium/tetragon/pull/3948) by @AritraDey-Dev
* pkg/sensors: initialize RewriteConstant map in builder (https://github.com/cilium/tetragon/pull/4080) by @mtardy
* new(cmd/tetra,pkg/bugtool): allow to extend bugtool with custom commands and grpc calls. (https://github.com/cilium/tetragon/pull/4079) by @FedeDP
* FindProgramFileUnderLocations: error logging (https://github.com/cilium/tetragon/pull/4106) by @kkourt
* policy_stats: use the map only for policy sensors (https://github.com/cilium/tetragon/pull/4107) by @kkourt
* k8s: Add alias for getting k8s config (https://github.com/cilium/tetragon/pull/4116) by @sayboras
* bpf: additional errmetrics (https://github.com/cilium/tetragon/pull/4120) by @FedeDP
* chore(bpf, pkg/errmetrics): some probe_read() bpf errmetrics (https://github.com/cilium/tetragon/pull/4132) by @FedeDP
* policies: only warn once for stats and mode (https://github.com/cilium/tetragon/pull/4136) by @kkourt
* pkg/errmetrics: expose error metrics via Prometheus metrics (https://github.com/cilium/tetragon/pull/4127) by @mtardy
* k8s: Avoid hard coded CRD.spec.group (https://github.com/cilium/tetragon/pull/4150) by @sayboras
* fix: always close the bpf link in `detectKprobeMulti` before returning (https://github.com/cilium/tetragon/pull/4151) by @Andreagit97
* observer: deal with empty data in HandlePerfData (https://github.com/cilium/tetragon/pull/4200) by @kkourt
* tetragon: assorted fixes (https://github.com/cilium/tetragon/pull/4207) by @olsajiri
* tetragon: testutils service both perf and bpf ring (https://github.com/cilium/tetragon/pull/4147) by @kevsecurity
* cleanup: remove old build constraint syntax (https://github.com/cilium/tetragon/pull/4216) by @mtardy
* pkg/asm: fuzz Assignment func parsing strings (https://github.com/cilium/tetragon/pull/4209) by @mtardy
* new(tests/e2e): add a metrics checker on e2e tests. (https://github.com/cilium/tetragon/pull/4098) by @FedeDP
* fix(bpf/process): fix some missing `break` statements. (https://github.com/cilium/tetragon/pull/4219) by @FedeDP
* fix(bpf): force explicit switch case fallthrough (https://github.com/cilium/tetragon/pull/4223) by @FedeDP
* Prepare for v1.6.0-rc.1 release (https://github.com/cilium/tetragon/pull/4229) by @mtardy
* tetragon: check event length in test ring handler (https://github.com/cilium/tetragon/pull/4231) by @kevsecurity
* fix(pkg/sensors): account for sleepableOffloadMap in multi uprobe (https://github.com/cilium/tetragon/pull/4226) by @FedeDP
* fix(pkg/sensors): use correct name for multiUprobePinPath (https://github.com/cilium/tetragon/pull/4225) by @FedeDP
* Prepare for v1.6.0 release (https://github.com/cilium/tetragon/pull/4238) by @mtardy