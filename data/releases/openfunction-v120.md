# OpenFunction - v1.2.0

**Release Name**: v1.2.0
**Published**: 2023-09-22T10:06:14Z
**Repository**: https://github.com/OpenFunction/OpenFunction

---

# What's Changed

### OpenFunction

#### Features

- Integrating KEDA http-addon [OpenFunction#483](https://github.com/OpenFunction/OpenFunction/pull/483)

#### Enhancement

- Add envs for skywalking when enable skywalking tracing [OpenFunction#481](https://github.com/OpenFunction/OpenFunction/pull/481)
- Upgrade KEDA to v2.10.1, HPA(autoscaling) api version to v2, improve stability and compatibility [OpenFunction#476](https://github.com/OpenFunction/OpenFunction/pull/476)
- Support to record events when Function， Builder, and Serving status change [OpenFunction#470](https://github.com/OpenFunction/OpenFunction/pull/470)
- Support for recording build time [OpenFunction#468](https://github.com/OpenFunction/OpenFunction/pull/468)

#### BUGFIX

- Adjust CI process, fix some minor issues [OpenFunction#496](https://github.com/OpenFunction/OpenFunction/pull/496)
- Fix a bug in keda http-addon runtime [OpenFunction#491](https://github.com/OpenFunction/OpenFunction/pull/491)
- Revert the change of [#486], because it caused the service to not work properly [OpenFunction#493](https://github.com/OpenFunction/OpenFunction/pull/493)

### charts

#### Component Upgrade

- Upgrade keda from v2.8.1 to v2.11.2
- Upgrade dapr from v1.8.3 to v1.11.3
- Upgrade contour from v1.21.1 to v1.23.3

**Full Changelog**: https://github.com/OpenFunction/OpenFunction/compare/v1.1.1...v1.2.0