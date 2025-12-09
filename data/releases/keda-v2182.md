# KEDA - v2.18.2

**Release Name**: v2.18.2
**Published**: 2025-12-08T13:46:24Z
**Repository**: https://github.com/kedacore/keda

---

# We are happy to release KEDA v2.18.2 :rocket: 

### Fixes

- **General**: Fix HPA behavior not restored when paused-scale-in/out annotation is deleted without corresponding custom behavior ([#7291](https://github.com/kedacore/keda/pull/7291))
- **General**: Fix nil reference panic when transfer-hpa-ownership is set but no hpa name is provided ([#7254](https://github.com/kedacore/keda/issues/7254))
- **General**: Fix race condition in paused-replicas annotation causing ScaledObject to get stuck ([#7231](https://github.com/kedacore/keda/issues/7231))
- **General**: Fix ScaledObject controller error handling for requestScaleLoop ([#7273](https://github.com/kedacore/keda/pull/7273))
- **General**: Remove unnecessary scaledObjectMetricSpecs variable in HPA ([#7292](https://github.com/kedacore/keda/pull/7292))
- **General**: Use TriggerError when all ScaledJob triggers fail ([#7205](https://github.com/kedacore/keda/pull/7205))
- **ActiveMQ Scaler**: Correct parse error ActiveMQ ([#7245](https://github.com/kedacore/keda/pull/7245))
- **Datadog Scaler**: Fix metricUnavailableValue parameter not working ([#7238](https://github.com/kedacore/keda/issues/7238))

**Full Changelog**: https://github.com/kedacore/keda/compare/v2.18.1...v2.18.2