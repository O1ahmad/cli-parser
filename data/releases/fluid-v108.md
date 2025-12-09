# Fluid - v1.0.8

**Release Name**: v1.0.8
**Published**: 2025-10-31T04:05:14Z
**Repository**: https://github.com/fluid-cloudnative/fluid

---

## New Features
1. **Support for Native Sidecar Mode**  
   In FUSE Sidecar deployments, the Kubernetes Native Sidecar injection scheme can be enabled to resolve lifecycle management, startup sequencing, and resource isolation limitations of traditional Sidecars.  
2. **Fluid Dashboard KubeSphere Extension**
  Adds Web dashboard for Fluid, including dataset, runtime, and dataload management.
3. **Open ThinRuntime PodMetadata Configuration**  
   Supports dynamic configuration of PodMetadata (e.g., labels/annotations) for FUSE Pods, enhancing deployment flexibility.  
4. **Support for Additional Storage Client Types**  
   Adds 3FS and Curvine storage support through ThinRuntime, extending distributed storage ecosystem compatibility.  



## Enhancements
1. **Optimized Node Scheduling Synchronization**  
   Provides configuration options to disable unnecessary node scheduling synchronization, significantly improving cache engine scheduling efficiency.  
2. **Adjusted ThinRuntime Controller Rate Limiting**  
   Sets default Reconcile RateLimit to 0, accelerating resource update response times.  
3. **Mount Point Detection Reliability Reinforcement**  
   Optimizes redirection mechanisms in postStart scripts, eliminating intermittent mount status check failures.  
4. **Optimized Control-Plane Least Privilege**  
   Tightens RBAC permissions for core Controllers' ServiceAccounts, removing redundant authorizations.  
6. **FUSE Container Privilege Reduction**  
   Removes non-essential administrative privileges to reduce security attack surfaces.  

## Bug Fixes
- Trimmed CRD descriptions to avoid Helm release storage size limits.
- Fixed template injection vulnerabilities and updated dependencies in the dashboard extension.
- Upgraded Kubernetes client to **v1.29.15** for improved compatibility.
- Added comprehensive unit tests for FUSE sidecar mutators and utility functions.
- Refactored internal logic for better modularity and maintainability (e.g., `SyncScheduleInfoToCacheNodes`, sidecar mutators).
- Bumped key dependencies, including gRPC, Gomega, Cobra, and CodeQL.
- Added documentation for dashboard usage and Curvine integration guidance.
- Improved CI/CD pipeline reliability with pinned dependencies and enhanced debugging info.


## What's Changed
* Update Makefile/Chart to v1.0.8 by @RongGu in https://github.com/fluid-cloudnative/fluid/pull/5249
* optim: trim descriptions in fluid crds to avoid touching size limit in helm release storage by @TrafalgarZZZ in https://github.com/fluid-cloudnative/fluid/pull/5251
* fix(security): Service account permissions should be restricted. Add sample file samples/juicefs/read_job.yaml. by @JiGuoDing in https://github.com/fluid-cloudnative/fluid/pull/5242
* refactor function SyncScheduleInfoToCacheNodes and add unit tests for util dataset functions  by @TrafalgarZZZ in https://github.com/fluid-cloudnative/fluid/pull/5220
* refactor(utils): remove unused code and re-organize some code structure by @TrafalgarZZZ in https://github.com/fluid-cloudnative/fluid/pull/5223
* feat: add guidance on integrating thin-runtime with Curvine by @jlon in https://github.com/fluid-cloudnative/fluid/pull/5245
* add unit tests for default and unprivileged fuse sidecar mutators by @TrafalgarZZZ in https://github.com/fluid-cloudnative/fluid/pull/5246
* feat(dashboard-ks-extension): migrate base project structure and configs by @zmrlft in https://github.com/fluid-cloudnative/fluid/pull/5248
* Fix sa restriction in samples by @Pikabooboo in https://github.com/fluid-cloudnative/fluid/pull/5260
* chore: update ossfs dynamic mount example by @TrafalgarZZZ in https://github.com/fluid-cloudnative/fluid/pull/5259
* build(deps-dev): bump http-proxy-middleware from 1.3.1 to 2.0.9 in /dashboard/fluid-ks-extension by @dependabot[bot] in https://github.com/fluid-cloudnative/fluid/pull/5257
* update kubernetes to v1.29.15 by @cheyang in https://github.com/fluid-cloudnative/fluid/pull/5253
* fix(security): Storage & Memory limits should be enforced in test/gha-e2e/jindo/job.yaml. Add a sample file samples/jindo/job.yaml. by @JiGuoDing in https://github.com/fluid-cloudnative/fluid/pull/5261
* build(deps): bump google.golang.org/grpc from 1.70.0 to 1.75.1 by @dependabot[bot] in https://github.com/fluid-cloudnative/fluid/pull/5227
* feat(dashboard-ks-extension): migrate framework entry and utilities by @zmrlft in https://github.com/fluid-cloudnative/fluid/pull/5250
* build(deps-dev): bump webpack-dev-server from 4.15.2 to 5.2.1 in /dashboard/fluid-ks-extension by @dependabot[bot] in https://github.com/fluid-cloudnative/fluid/pull/5256
* build(deps): bump github/codeql-action from 3.30.1 to 3.30.5 by @dependabot[bot] in https://github.com/fluid-cloudnative/fluid/pull/5262
* build(deps): bump github.com/onsi/gomega from 1.36.2 to 1.38.2 by @dependabot[bot] in https://github.com/fluid-cloudnative/fluid/pull/5263
* add pinned dependency for code coverage by @RongGu in https://github.com/fluid-cloudnative/fluid/pull/5264
* feat(dashboard-ks-extension): migrate dataset-related pages and logic by @zmrlft in https://github.com/fluid-cloudnative/fluid/pull/5252
* feat(dashboard-ks-extension): migrate runtime-related pages and logic by @zmrlft in https://github.com/fluid-cloudnative/fluid/pull/5254
* build(deps): bump github.com/spf13/cobra from 1.9.1 to 1.10.1 by @dependabot[bot] in https://github.com/fluid-cloudnative/fluid/pull/5265
* fix(dashboard-ks-extension): resolve ejs template injection vulnerabi… by @zmrlft in https://github.com/fluid-cloudnative/fluid/pull/5266
* Fix/dashboard ks extension dependency security vulnerabilities by @zmrlft in https://github.com/fluid-cloudnative/fluid/pull/5268
* Build docker images for  v1.0.8 alpha version by @RongGu in https://github.com/fluid-cloudnative/fluid/pull/5267
* fix(dashboard-ks-extension): update version to resolve path-to-regexp… by @zmrlft in https://github.com/fluid-cloudnative/fluid/pull/5272
* build(deps): bump ossf/scorecard-action from 2.4.2 to 2.4.3 by @dependabot[bot] in https://github.com/fluid-cloudnative/fluid/pull/5271
* build(deps): bump github.com/onsi/ginkgo/v2 from 2.25.1 to 2.26.0 by @dependabot[bot] in https://github.com/fluid-cloudnative/fluid/pull/5269
* feat(dashboard-ks-extension): migrate dataload-related pages and logic by @zmrlft in https://github.com/fluid-cloudnative/fluid/pull/5255
* docs: add a new "dashboard" section in the document by @zmrlft in https://github.com/fluid-cloudnative/fluid/pull/5258
* build(deps): bump github/codeql-action from 3.30.5 to 3.30.6 by @dependabot[bot] in https://github.com/fluid-cloudnative/fluid/pull/5270
* enhance: set default syncRetryRateLimitDuration to 0s for thinruntime controller by @TrafalgarZZZ in https://github.com/fluid-cloudnative/fluid/pull/5277
* Build docker image for supporting k8s 1.29.15 by @RongGu in https://github.com/fluid-cloudnative/fluid/pull/5278
* feat: thinruntime support pod metadata by @TrafalgarZZZ in https://github.com/fluid-cloudnative/fluid/pull/5276
* build(deps): bump github/codeql-action from 3.30.6 to 4.30.8 by @dependabot[bot] in https://github.com/fluid-cloudnative/fluid/pull/5279
* disable token mount in all samples by @Pikabooboo in https://github.com/fluid-cloudnative/fluid/pull/5281
* feat: skip syncing schedule info for specified nodes by @TrafalgarZZZ in https://github.com/fluid-cloudnative/fluid/pull/5285
* Add 3fs addon samples by @Pikabooboo in https://github.com/fluid-cloudnative/fluid/pull/5282
* Add debug info for check_control_plane_status by @cheyang in https://github.com/fluid-cloudnative/fluid/pull/5286
* refactor(dashboard): remove dashboard directory by @zmrlft in https://github.com/fluid-cloudnative/fluid/pull/5290
* Build docker images for skipping syncing schedule info for specified … by @cheyang in https://github.com/fluid-cloudnative/fluid/pull/5287
* ehance: remove redundant SYS_ADMIN capability from runtime engines by @TrafalgarZZZ in https://github.com/fluid-cloudnative/fluid/pull/5289
* build(deps): bump github/codeql-action from 4.30.8 to 4.30.9 by @dependabot[bot] in https://github.com/fluid-cloudnative/fluid/pull/5288
* Bump csi image version to v.2.14.0 by @Pikabooboo in https://github.com/fluid-cloudnative/fluid/pull/5292
* refactor: make fuse sidecar mutators function-level composable  by @TrafalgarZZZ in https://github.com/fluid-cloudnative/fluid/pull/5293
* Build docker images for native sidecar feature by @RongGu in https://github.com/fluid-cloudnative/fluid/pull/5296
* feat(injector): add support for native sidecar injection by @TrafalgarZZZ in https://github.com/fluid-cloudnative/fluid/pull/5295
* Fix: support retries for redirecting check-mount script execution res… by @Syspretor in https://github.com/fluid-cloudnative/fluid/pull/5297
* Build docker images for enabling retries config for checking-mount by @RongGu in https://github.com/fluid-cloudnative/fluid/pull/5301
* refactor(helm): extract syncScheduleInfoNodeExcludeSelector env into helper template by @TrafalgarZZZ in https://github.com/fluid-cloudnative/fluid/pull/5300
* Build docker images for v1.0.8 by @RongGu in https://github.com/fluid-cloudnative/fluid/pull/5302
* Update CHANGELOG.md for version 1.0.8 by @RongGu in https://github.com/fluid-cloudnative/fluid/pull/5303

## New Contributors
* @jlon made their first contribution in https://github.com/fluid-cloudnative/fluid/pull/5245
* @zmrlft made their first contribution in https://github.com/fluid-cloudnative/fluid/pull/5248

**Full Changelog**: https://github.com/fluid-cloudnative/fluid/compare/v1.0.7...v1.0.8