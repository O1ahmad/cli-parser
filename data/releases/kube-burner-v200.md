# Kube-burner - v2.0.0

**Release Name**: v2.0.0
**Published**: 2025-12-05T15:34:45Z
**Repository**: https://github.com/kube-burner/kube-burner

---

## 🎉 Major Release

This is a major version release of kube-burner with significant improvements and new features. This release includes breaking changes as we transition to v2.

## ✨ New Features & Enhancements

- **kube-burner V2**: Major version upgrade with improved architecture and performance ([#1033](https://github.com/kube-burner/kube-burner/pull/1033))
- **Node processes pprof colection**: Implement pprof collection for Node Processes (Kubelet and CRIO) ([#1045](https://github.com/kube-burner/kube-burner/pull/1045))
- **Configuration Override**: Add support for `--set` flag to override configuration base yaml values ([#1047](https://github.com/kube-burner/kube-burner/pull/1047))
- **Enhanced Latency Tracking**: Get pod scheduling and containersStarted latency timestamps from events ([#1029](https://github.com/kube-burner/kube-burner/pull/1029))

## 🚨 Breaking Changes

- **Resource Level Churning**: Enhanced churning capabilities at the resource level ([#987](https://github.com/kube-burner/kube-burner/pull/987))
-  **Standardized Labels**: Standardize kube-burner labels across the project ([#1022](https://github.com/kube-burner/kube-burner/pull/1022))
- **Cleanup**: Remove deprecated `gcTimeout` parameter ([#1027](https://github.com/kube-burner/kube-burner/pull/1027))

## 🔧 Improvements & Optimizations

- **Namespace Tracking**: Add map to jobExecutor struct to track namespaces creation ([#1028](https://github.com/kube-burner/kube-burner/pull/1028))
- **Object Verification**: Run object verification in churning iterations ([#1043](https://github.com/kube-burner/kube-burner/pull/1043))
  - Print delete log messages only when something is going to be deleted ([#1053](https://github.com/kube-burner/kube-burner/pull/1053))
  - Reduce GVR logging for cleaner output ([#1051](https://github.com/kube-burner/kube-burner/pull/1051))
  - Add space for service latency log to play nicer with double-click selection ([#1050](https://github.com/kube-burner/kube-burner/pull/1050))
- **Improved measurements logging**: Add units to measurements report for better clarity ([#1030](https://github.com/kube-burner/kube-burner/pull/1030))


## 🐛 Bug Fixes

- **Churning Fix**: Set deleted namespaces from churning to false and fix patch syntax ([#1037](https://github.com/kube-burner/kube-burner/pull/1037))

## 📚 Documentation

- **Churning Documentation**: Document churnMetric field in churning configuration ([#1046](https://github.com/kube-burner/kube-burner/pull/1046))

## 🧪 Testing

- **Test Optimization**: Use a smaller disk for DataVolume latency test ([#1034](https://github.com/kube-burner/kube-burner/pull/1034))
- **Performance**: Parallel CI testing implementation ([#1039](https://github.com/kube-burner/kube-burner/pull/1039))
- **Test Stability**: Fix flaky test by checking command return code rather than value ([#1032](https://github.com/kube-burner/kube-burner/pull/1032))
- **Refactoring**: Shift to `verify_object_count` function ([#1040](https://github.com/kube-burner/kube-burner/pull/1040))

## 🔄 Dependencies

- **GitHub Actions**: Bump actions/checkout from 5 to 6 ([#1049](https://github.com/kube-burner/kube-burner/pull/1049))
- **Dependencies**: Update go-commons dependency ([#1031](https://github.com/kube-burner/kube-burner/pull/1031))

## 👥 Contributors

Thanks to all the contributors who made this release possible:

- **Raúl Sevilla** - Multiple contributions
- **Sai Sanjay** - pprof integration and configuration enhancements
- **vishnuchalla** - Timeout handling improvements
- **Andrew Collins** - Logging and user experience improvements
- **Ygal Blum** - Testing optimizations
- **dependabot[bot]** - Dependency updates


---
