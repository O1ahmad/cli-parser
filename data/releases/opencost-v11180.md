# OpenCost - v1.118.0

**Release Name**: v1.118.0
**Published**: 2025-10-23T20:07:34Z
**Repository**: https://github.com/opencost/opencost

---

## What's Changed
* bump dependencies by @mittal-ishaan in https://github.com/opencost/opencost/pull/3382
* Refactor ComputeCostData and add unit tests by @sneaxhuh in https://github.com/opencost/opencost/pull/3295
* feat: Implement OpenCost Data Model v2 protobuf architecture by @spa-raj in https://github.com/opencost/opencost/pull/3369
* Implement missing Window methods and tests by @sneaxhuh in https://github.com/opencost/opencost/pull/3305
* fix window to be inclusive by @ameijer in https://github.com/opencost/opencost/pull/3395
* update log when unable to find pricing key for node by @nickcurie in https://github.com/opencost/opencost/pull/3396
* Fix idleByNode parameter ignored in allocation API by @rbtkess in https://github.com/opencost/opencost/pull/3402
* fix: Apply allocation filters before aggregation to ensure AND operator order independence by @spa-raj in https://github.com/opencost/opencost/pull/3394
* Enforce secure TLS MinVersion across all configurations by @fromsaurav in https://github.com/opencost/opencost/pull/3309
* fix(csvprovider): convert ProviderID to lowercase for pv by @jumana-s in https://github.com/opencost/opencost/pull/3361
* Fix providerID set to node name in idle allocations by @rbtkess in https://github.com/opencost/opencost/pull/3403
* security: update to Go 1.24-alpine3.20 to fix critical vulnerabilities by @brian-olson in https://github.com/opencost/opencost/pull/3367
* Kcm-4679: K8s version information in cluster info meta provider  by @avrodrigues5 in https://github.com/opencost/opencost/pull/3398
* Improve heuristics to get Azure node prices from Retail Prices API by @joao-pimentel-randoli in https://github.com/opencost/opencost/pull/3230
* test(athena): Improve AWS Athena integration test coverage by @sneaxhuh in https://github.com/opencost/opencost/pull/3314
* initial golangci-lint workflow by @HMetcalfeW in https://github.com/opencost/opencost/pull/3410
* rev golangci-lint version by @HMetcalfeW in https://github.com/opencost/opencost/pull/3411
* Add AppVersion to pkg/version by @kaelanspatel in https://github.com/opencost/opencost/pull/3412
* move cliff to maintainer emeritus by @ameijer in https://github.com/opencost/opencost/pull/3409
* Remove requirement for SpecProviderID for node stats by @mbolt35 in https://github.com/opencost/opencost/pull/3418
* chores: Optimize Dockerfile with cross-compilation by @motoki317 in https://github.com/opencost/opencost/pull/3351
* fix: Bearer token capitalization in Authorization header to comply with RFC 6750 by @spa-raj in https://github.com/opencost/opencost/pull/3417
* feat: add MCP server for OpenCost allocation and asset queries by @sneaxhuh in https://github.com/opencost/opencost/pull/3386

## New Contributors
* @rbtkess made their first contribution in https://github.com/opencost/opencost/pull/3402
* @fromsaurav made their first contribution in https://github.com/opencost/opencost/pull/3309
* @jumana-s made their first contribution in https://github.com/opencost/opencost/pull/3361
* @brian-olson made their first contribution in https://github.com/opencost/opencost/pull/3367
* @joao-pimentel-randoli made their first contribution in https://github.com/opencost/opencost/pull/3230
* @motoki317 made their first contribution in https://github.com/opencost/opencost/pull/3351

**Full Changelog**: https://github.com/opencost/opencost/compare/v1.117.6...v1.118.0