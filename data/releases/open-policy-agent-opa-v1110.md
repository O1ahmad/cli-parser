# Open Policy Agent (OPA) - v1.11.0

**Release Name**: v1.11.0
**Published**: 2025-11-26T13:24:07Z
**Repository**: https://github.com/open-policy-agent/opa

---

This release contains a mix of new features, performance improvements, and bugfixes. Notably:

- More efficient connection management in the `http.send` built-in function
- More performant loading of large bundles containing multiple Rego files

### Immutable Releases

Starting with this release, OPA releases are [immutable](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/immutable-releases) for increased security.

### Runtime, SDK, Tooling

- v1/ast: Fix Call parsing Text attribute including an extra character ([#7989](https://github.com/open-policy-agent/opa/issues/7989)) authored by @schmitd
- ast: Export built-in deprecated field ([#7912](https://github.com/open-policy-agent/opa/issues/7912)) authored by @colinjlacy
- ast: Intern common var values + some parser improvements ([#8028](https://github.com/open-policy-agent/opa/pull/8028)) authored by @anderseknert
- ast: Support custom builtins in CompileModulesWithOpt ([#8061](https://github.com/open-policy-agent/opa/issues/5580)) authored by @sspaink
- bundle: Concurrent Rego parsing in bundle loader ([#8067](https://github.com/open-policy-agent/opa/pull/8067)) authored by @anderseknert
- cmd: Support `--ignore` in `eval` cmd when using bundle flag (`--bundle`) ([#8062](https://github.com/open-policy-agent/opa/pull/8048)) authored by @sspaink
- storage/inmem: Allow passing triggers (AST) data without conversion ([#7958](https://github.com/open-policy-agent/opa/issues/7958)) authored by @anderseknert

### Compiler, Topdown and Rego

- topdown: Avoid unnecessary use of custom `http.Transport` in `http.send` built-in ([#7927](https://github.com/open-policy-agent/opa/pull/7927)) authored by @sykesm
- topdown: New custom SemVer implementation ([#8010](https://github.com/open-policy-agent/opa/pull/8010)) authored by @anderseknert
- topdown: Use `sync.Pool` for eval func objects ([#8054](https://github.com/open-policy-agent/opa/pull/8054)) authored by @anderseknert

### Docs, Website, Ecosystem

- docs: Add example for Compile API's table mapping ([#8017](https://github.com/open-policy-agent/opa/pull/8017)) authored by @srenatus
- docs: Address pages with similar titles ([#8046](https://github.com/open-policy-agent/opa/pull/8046)) authored by @charlieegan3
- docs: Address some broken links ([#8022](https://github.com/open-policy-agent/opa/pull/8022)) authored by @charlieegan3
- docs: Bump glob dep (CVE-2025-64756) ([#8056](https://github.com/open-policy-agent/opa/pull/8056)) authored by @srenatus
- docs: Improve ground value and assignment docs ([#8047](https://github.com/open-policy-agent/opa/pull/8047)) authored by @charlieegan3
- docs: Make iteration content flow better ([#8064](https://github.com/open-policy-agent/opa/pull/8064)) authored by @charlieegan3
- docs: Note package repos are community maintained ([#8053](https://github.com/open-policy-agent/opa/pull/8053)) authored by @charlieegan3
- docs: Update terraform guide with notes about plan ([#8043](https://github.com/open-policy-agent/opa/pull/8043)) authored by @charlieegan3
- docs: Update the archive to have an edge link ([#8011](https://github.com/open-policy-agent/opa/pull/8011)) authored by @charlieegan3
- docs: Update the policy language intro ([#8050](https://github.com/open-policy-agent/opa/pull/8050)) authored by @charlieegan3
- docs/ocp: Datasource example uses wrong AWS S3 URL ([#8039](https://github.com/open-policy-agent/opa/pull/8039)) authored by @SuchSkill
- docs/regal: Replicate sidebar fixes ([#8036](https://github.com/open-policy-agent/opa/pull/8036)) authored by @charlieegan3
- website: Various fixes and improvements by @charlieegan3

### Miscellaneous

- Bump golangci-lint, more gocritic linters ([#8052](https://github.com/open-policy-agent/opa/pull/8052)) authored by @anderseknert
- Tidy up and unify sync pool handling ([#8068](https://github.com/open-policy-agent/opa/pull/8068)) authored by @anderseknert
- builtins: Add `StringOperandByteSlice` helper ([#8048](https://github.com/open-policy-agent/opa/pull/8048)) authored by @anderseknert
- test: Add test cases for consistent cache behavior ([#8015](https://github.com/open-policy-agent/opa/pull/8015)) authored by @DFrenkel
- util/performance: Remove math.Log10, remove unused KeysCount ([#8041](https://github.com/open-policy-agent/opa/pull/8041)) authored by @srenatus
- workflow: Add `Benchmarks` workflow ([#8072](https://github.com/open-policy-agent/opa/pull/8072)) authored by @srenatus
- workflows/pull-request: Update macos versions ([#8030](https://github.com/open-policy-agent/opa/pull/8030)) authored by @srenatus
- Dependency updates; notably:
  - build: golang 1.25.3 -> 1.25.4 ([#8051](https://github.com/open-policy-agent/opa/pull/8051)) authored by @srenatus
  - build(deps): Bump github.com/bytecodealliance/wasmtime-go from v37.0.0 to v39.0.1 ([#8075](https://github.com/open-policy-agent/opa/pull/8075)) authored by @srenatus
  - build(deps): Bump github.com/containerd/containerd/v2 from 2.1.4 to 2.2.0
  - build(deps): Bump github.com/huandu/go-sqlbuilder from 1.37.0 to 1.38.1
  - build(deps): Bump github.com/lestrrat-go/jwx/v3 from 3.0.11 to 3.0.12
  - build(deps): Bump github.com/vektah/gqlparser/v2 from 2.5.30 to 2.5.31 ([#8027](https://github.com/open-policy-agent/opa/pull/8027)) authored by @johanfylling
  - build(deps): Bump golang.org/x/crypto from 0.43.0 to 0.45.0
  - build(deps): Bump golang.org/x/net from 0.44.0 to 0.45.0
  - build(deps): Bump golang.org/x/time from 0.13.0 to 0.14.0
  - build(deps): Bump google.golang.org/grpc from 1.75.1 to 1.76.0
  - build(deps): Bump google.golang.org/protobuf from 1.36.9 to 1.36.10

