# Kyverno - v1.16.1

**Release Name**: v1.16.1
**Published**: 2025-12-03T09:59:45Z
**Repository**: https://github.com/kyverno/kyverno

---

## What's Changed
* fix nil namespace initialization for cluster wide param resources (Cherry-pick #14327) by @kyverno-bot in https://github.com/kyverno/kyverno/pull/14328
* fix: dont register the http request type (Cherry-pick #14238) by @kyverno-bot in https://github.com/kyverno/kyverno/pull/14340
* fix: scale test k6 installation (cherry-pick #14338) by @realshuting in https://github.com/kyverno/kyverno/pull/14348
* fix: handle namespace match with namespaceSelector (Cherry-pick #14339) by @kyverno-bot in https://github.com/kyverno/kyverno/pull/14356
* feat: generate and copy crd to cli for namespaced validating policy and namespaced deleting policy (Cherry-pick #14316) by @kyverno-bot in https://github.com/kyverno/kyverno/pull/14357
* release v1.16.1-rc.1 by @realshuting in https://github.com/kyverno/kyverno/pull/14345
* fix(admissionpolicy): handle nil MatchConstraints (Cherry-pick #14350) by @kyverno-bot in https://github.com/kyverno/kyverno/pull/14394
* fix(controllers): duplicate error accumulation (Cherry-pick #14349) by @kyverno-bot in https://github.com/kyverno/kyverno/pull/14395
* fix(controllers): avoid cleanup on non-matching ns (Cherry-pick #14386) by @kyverno-bot in https://github.com/kyverno/kyverno/pull/14398
* supporting wildcards in resource namespace matching (Cherry-pick #14250) by @kyverno-bot in https://github.com/kyverno/kyverno/pull/14397
* fix: use namespaceObject in deletingpolicies (Cherry-pick #14381) by @kyverno-bot in https://github.com/kyverno/kyverno/pull/14422
* chore: add a new test that uses both context and values (Cherry-pick #14416) by @kyverno-bot in https://github.com/kyverno/kyverno/pull/14423
* release v1.16.0-rc.2 by @realshuting in https://github.com/kyverno/kyverno/pull/14428
* release v1.16.1 by @realshuting in https://github.com/kyverno/kyverno/pull/14435


**Full Changelog**: https://github.com/kyverno/kyverno/compare/v1.16.0...v1.16.1