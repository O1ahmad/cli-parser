# Hyperlight - dev-latest

**Release Name**: Latest prerelease from main branch
**Published**: 2025-12-08T18:52:27Z
**Repository**: https://github.com/hyperlight-dev/hyperlight

---

## What's Changed

### Removed
* Remove outdated `is_supported_platform` (use `is_hypervisor_present` instead) and unused `ExtraAllowedSyscall` by @ludfjig in https://github.com/hyperlight-dev/hyperlight/pull/1062


### Full Changelog (excl. dependencies)
* Organize benchmarks and introduce 'size' dimension by @ludfjig in https://github.com/hyperlight-dev/hyperlight/pull/1007
* Simplify cancellation by @ludfjig in https://github.com/hyperlight-dev/hyperlight/pull/1024
* Deduplicate mem mgr and host functions from hv drivers by @ludfjig in https://github.com/hyperlight-dev/hyperlight/pull/1013
* Move sregs to its own file by @ludfjig in https://github.com/hyperlight-dev/hyperlight/pull/1043
* Fix cross-compilation of Windows surrogate binary on Linux by @ludfjig in https://github.com/hyperlight-dev/hyperlight/pull/1045
* Add metric for erroneous vCPU kicks from stale cancellations by @Copilot in https://github.com/hyperlight-dev/hyperlight/pull/1034
* [trace-dump] Fix `MemFree` writing to file for `mem_profile` feature by @dblnz in https://github.com/hyperlight-dev/hyperlight/pull/1051
* Add TraceContext unit tests by @dblnz in https://github.com/hyperlight-dev/hyperlight/pull/1006
* Add anyhow-inspired error utilities by @jprendes in https://github.com/hyperlight-dev/hyperlight/pull/1052
* Remove old unused code by @ludfjig in https://github.com/hyperlight-dev/hyperlight/pull/1062
* Fix guest tracing deadlock when exception happens during tracing data serialization by @dblnz in https://github.com/hyperlight-dev/hyperlight/pull/1066
* Guest function improvements and macros by @jprendes in https://github.com/hyperlight-dev/hyperlight/pull/851
* Fix StackOverflow produced by guest logging by @dblnz in https://github.com/hyperlight-dev/hyperlight/pull/1067
* Update the interrupt handler for 16byte alignment by @jsturtevant in https://github.com/hyperlight-dev/hyperlight/pull/1037
* fix auto approve script by @simongdavies in https://github.com/hyperlight-dev/hyperlight/pull/1075
* Fix guest call to `halt` not dropping allocated trace data leading to memory leak  by @dblnz in https://github.com/hyperlight-dev/hyperlight/pull/1072
### Full Changelog (dependencies)
* Bump cc from 1.2.43 to 1.2.44 by @dependabot[bot] in https://github.com/hyperlight-dev/hyperlight/pull/1003
* Bump syn from 2.0.108 to 2.0.109 by @dependabot[bot] in https://github.com/hyperlight-dev/hyperlight/pull/1012
* Bump quote from 1.0.41 to 1.0.42 by @dependabot[bot] in https://github.com/hyperlight-dev/hyperlight/pull/1015
* Bump tracing-forest from 0.2.0 to 0.3.0 by @dependabot[bot] in https://github.com/hyperlight-dev/hyperlight/pull/1014
* Bump cc from 1.2.44 to 1.2.45 by @dependabot[bot] in https://github.com/hyperlight-dev/hyperlight/pull/1018
* Bump syn from 2.0.109 to 2.0.110 by @dependabot[bot] in https://github.com/hyperlight-dev/hyperlight/pull/1017
* Bump crate-ci/typos from 1.38.1 to 1.39.0 by @dependabot[bot] in https://github.com/hyperlight-dev/hyperlight/pull/1001
* Bump crate-ci/typos from 1.39.0 to 1.39.1 by @dependabot[bot] in https://github.com/hyperlight-dev/hyperlight/pull/1022
* Bump crate-ci/typos from 1.39.1 to 1.39.2 by @dependabot[bot] in https://github.com/hyperlight-dev/hyperlight/pull/1023
* Bump cc from 1.2.45 to 1.2.46 by @dependabot[bot] in https://github.com/hyperlight-dev/hyperlight/pull/1026
* Bump wasmparser from 0.240.0 to 0.241.2 by @dependabot[bot] in https://github.com/hyperlight-dev/hyperlight/pull/1025
* Bump actions/checkout from 5 to 6 by @dependabot[bot] in https://github.com/hyperlight-dev/hyperlight/pull/1035
* Bump signal-hook-registry from 1.4.6 to 1.4.7 by @dependabot[bot] in https://github.com/hyperlight-dev/hyperlight/pull/1040
* Bump syn from 2.0.110 to 2.0.111 by @dependabot[bot] in https://github.com/hyperlight-dev/hyperlight/pull/1038
* Bump cc from 1.2.46 to 1.2.47 by @dependabot[bot] in https://github.com/hyperlight-dev/hyperlight/pull/1039
* Remove unused dependencies by @simongdavies in https://github.com/hyperlight-dev/hyperlight/pull/1042
* Bump tracing-core from 0.1.34 to 0.1.35 by @dependabot[bot] in https://github.com/hyperlight-dev/hyperlight/pull/1050
* Bump crate-ci/typos from 1.39.2 to 1.40.0 by @dependabot[bot] in https://github.com/hyperlight-dev/hyperlight/pull/1048
* Bump wasmparser from 0.241.2 to 0.242.0 by @dependabot[bot] in https://github.com/hyperlight-dev/hyperlight/pull/1049
* Bump cc from 1.2.47 to 1.2.48 by @dependabot[bot] in https://github.com/hyperlight-dev/hyperlight/pull/1056
* Bump goblin from 0.10.3 to 0.10.4 by @dependabot[bot] in https://github.com/hyperlight-dev/hyperlight/pull/1054
* Bump metrics-util from 0.20.0 to 0.20.1 by @dependabot[bot] in https://github.com/hyperlight-dev/hyperlight/pull/1055
* Bump criterion from 0.7.0 to 0.8.0 by @dependabot[bot] in https://github.com/hyperlight-dev/hyperlight/pull/1059
* Bump tracing from 0.1.41 to 0.1.43 by @dependabot[bot] in https://github.com/hyperlight-dev/hyperlight/pull/1058
* Bump metrics from 0.24.2 to 0.24.3 by @dependabot[bot] in https://github.com/hyperlight-dev/hyperlight/pull/1057
* Bump uuid from 1.18.1 to 1.19.0 by @dependabot[bot] in https://github.com/hyperlight-dev/hyperlight/pull/1064
* Bump tracing-subscriber from 0.3.20 to 0.3.22 by @dependabot[bot] in https://github.com/hyperlight-dev/hyperlight/pull/1063
* Bump metrics-exporter-prometheus from 0.17.2 to 0.18.0 by @dependabot[bot] in https://github.com/hyperlight-dev/hyperlight/pull/1060
* Bump log from 0.4.28 to 0.4.29 by @dependabot[bot] in https://github.com/hyperlight-dev/hyperlight/pull/1070
* Bump libc from 0.2.177 to 0.2.178 by @dependabot[bot] in https://github.com/hyperlight-dev/hyperlight/pull/1068
* Bump wasmparser from 0.242.0 to 0.243.0 by @dependabot[bot] in https://github.com/hyperlight-dev/hyperlight/pull/1069
* Bump linkme from 0.3.33 to 0.3.35 by @dependabot[bot] in https://github.com/hyperlight-dev/hyperlight/pull/1073
* Bump metrics-exporter-prometheus from 0.18.0 to 0.18.1 by @dependabot[bot] in https://github.com/hyperlight-dev/hyperlight/pull/1080
* Bump cc from 1.2.48 to 1.2.49 by @dependabot[bot] in https://github.com/hyperlight-dev/hyperlight/pull/1081
* Bump criterion from 0.8.0 to 0.8.1 by @dependabot[bot] in https://github.com/hyperlight-dev/hyperlight/pull/1079


**Full Changelog**: https://github.com/hyperlight-dev/hyperlight/compare/v0.11.0...dev-latest
