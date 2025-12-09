# hami - v2.7.1

**Release Name**: v2.7.1
**Published**: 2025-11-07T06:41:45Z
**Repository**: https://github.com/Project-HAMi/HAMi

---

<!-- Release notes generated using configuration in .github/release.yml at v2.7.1 -->

## What's Changed
### 🐛 Bug Fixes

Major:

**Update HAMi-core to fix vllm-related issues: #1381 # 1461 by @archlitchi in https://github.com/Project-HAMi/HAMi/pull/1478**
**Fix: Calculation error for quotas by @luohua13 in https://github.com/Project-HAMi/HAMi/pull/1400**

Others
* Fix release CI by @archlitchi in https://github.com/Project-HAMi/HAMi/pull/1373
* Fix: failed clusterrolebinding when change release name or chart name by @FouoF in https://github.com/Project-HAMi/HAMi/pull/1380
* fix: e2e ginkgo version mismatch by @FouoF in https://github.com/Project-HAMi/HAMi/pull/1391
* fix: check pod nil in `ReleaseNodeLock` by @DSFans2014 in https://github.com/Project-HAMi/HAMi/pull/1372
* fix: upgrade nvidia-mig-parted to v0.12.2 to solve security issues by @Shouren in https://github.com/Project-HAMi/HAMi/pull/1388
* fix: scheduler flaky test by @FouoF in https://github.com/Project-HAMi/HAMi/pull/1402
* Fix: After removing the device plugin from the gpu node, it can still… by @luohua13 in https://github.com/Project-HAMi/HAMi/pull/1456
* Fix concurrent map iteration and map write fatal error. by @litaixun in https://github.com/Project-HAMi/HAMi/pull/1452
* fix: fix typos by @DSFans2014 in https://github.com/Project-HAMi/HAMi/pull/1434
* Fix CI error of the PR #1470, #1326, #1033 by @archlitchi in https://github.com/Project-HAMi/HAMi/pull/1473
* Fix concurrent map read write fatal error. by @litaixun in https://github.com/Project-HAMi/HAMi/pull/1476
* add podInfos in DeviceUsage to enhance scheduling decision by @Kyrie336 in https://github.com/Project-HAMi/HAMi/pull/1362
* Update device-numa acquisition logic by @archlitchi in https://github.com/Project-HAMi/HAMi/pull/1403
* Improved support for iluvatar GPUs by @qiangwei1983 in https://github.com/Project-HAMi/HAMi/pull/1399
* Improve: Replace `StrategicMergePatchType` by `MergePatchType` by @luohua13 in https://github.com/Project-HAMi/HAMi/pull/1431
* optimize schedule failure event by @Kyrie336 in https://github.com/Project-HAMi/HAMi/pull/1444
* Release v2.7.1 by @archlitchi in https://github.com/Project-HAMi/HAMi/pull/1480

## New Contributors
* @luohua13 made their first contribution in https://github.com/Project-HAMi/HAMi/pull/1400
* @qiangwei1983 made their first contribution in https://github.com/Project-HAMi/HAMi/pull/1399
* @eltociear made their first contribution in https://github.com/Project-HAMi/HAMi/pull/1412
* @daixiang0 made their first contribution in https://github.com/Project-HAMi/HAMi/pull/1465
* @zhegemingzimeibanquan made their first contribution in https://github.com/Project-HAMi/HAMi/pull/1419

**Full Changelog**: https://github.com/Project-HAMi/HAMi/compare/v2.7.0...v2.7.1