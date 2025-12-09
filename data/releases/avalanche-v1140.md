# Avalanche - v1.14.0

**Release Name**: Granite - Improving ICM and Dynamic Block Times
**Published**: 2025-11-05T20:05:50Z
**Repository**: https://github.com/ava-labs/avalanchego

---

This release schedules the activation of the following Avalanche Community Proposals (ACPs):
- [ACP-181](https://github.com/avalanche-foundation/ACPs/blob/main/ACPs/181-p-chain-epoched-views/README.md) P-Chain Epoched Views
- [ACP-204](https://github.com/avalanche-foundation/ACPs/blob/main/ACPs/204-precompile-secp256r1/README.md) Precompile for secp256r1 Curve Support
- [ACP-226](https://github.com/avalanche-foundation/ACPs/blob/main/ACPs/226-dynamic-minimum-block-times/README.md) Dynamic Minimum Block Times

The ACPs in this upgrade go into effect at 11 AM ET (4 PM UTC) on Wednesday, November 19th, 2025 on Mainnet.

**All Mainnet nodes must upgrade before 11 AM ET, November 19th 2025.**

The plugin version is updated to `44`; all plugins must update to be compatible.

## LibEVM Hook Registration

This release includes changes for how EVM modifications are registered with libevm. For consumers of avalanchego as a library, manual registration of libevm callbacks is now required.

## APIs

- Added support for specifying multiple `Avalanche-Api-Route` headers for more complex routing.
- Added proposervm gRPC, connectrpc, and jsonrpc APIs for `GetProposedHeight` and `GetCurrentEpoch`.
  - The gRPC and connectrpc APIs are routed by adding a second `Avalanche-Api-Route` header with the value `proposervm`.
  - The jsonrpc APIs are added to all chains with the base endpoint `/proposervm`.
- Added platformvm `platform.GetAllValidatorsAt` API.

## Configs

- Changed default `proposerMinBlockDelay` for L1s (other than Primary Network) to 0.

## Fixes

- Improved bootstrapping ETA predictions.

## What's Changed

- Remove schedule trigger for w/ container job that evaluates to empty matrix by @aaronbuchwald in https://github.com/ava-labs/avalanchego/pull/4218
- chore: remove unzip mention by @RodrigoVillar in https://github.com/ava-labs/avalanchego/pull/4226
- refactor(load): simulator contract by @RodrigoVillar in https://github.com/ava-labs/avalanchego/pull/4181
- Remove firewood entry from PR triggers due to flakes by @aaronbuchwald in https://github.com/ava-labs/avalanchego/pull/4227
- Write grafana link to logs and github step summary by @aaronbuchwald in https://github.com/ava-labs/avalanchego/pull/4219
- Disambiguate source vs exec variable names in reexecute tasks by @aaronbuchwald in https://github.com/ava-labs/avalanchego/pull/4200
- Push benchmark re-execute results on master workflow dispatch by @aaronbuchwald in https://github.com/ava-labs/avalanchego/pull/4224
- Add newline to workflow dispatch by @aaronbuchwald in https://github.com/ava-labs/avalanchego/pull/4229
- Add back empty schedule entry for reexecute w/ container job by @aaronbuchwald in https://github.com/ava-labs/avalanchego/pull/4230
- Comment out schedule trigger for re-execution on w/container by @aaronbuchwald in https://github.com/ava-labs/avalanchego/pull/4234
- Add timeout parameter to C-Chain re-execution jobs by @aaronbuchwald in https://github.com/ava-labs/avalanchego/pull/4223
- feat: add parameters to disable metrics by @qusuyan in https://github.com/ava-labs/avalanchego/pull/4214
- feat(load): add firewood flag by @RodrigoVillar in https://github.com/ava-labs/avalanchego/pull/4235
- fix(load): totalSupply overflow by @RodrigoVillar in https://github.com/ava-labs/avalanchego/pull/4244
- Add runner name as metric label and benchmark name param by @aaronbuchwald in https://github.com/ava-labs/avalanchego/pull/4243
- fix(load): update nonce regardless of tx execution result by @RodrigoVillar in https://github.com/ava-labs/avalanchego/pull/4245
- Fix manual workflow quoted timeout minutes by @aaronbuchwald in https://github.com/ava-labs/avalanchego/pull/4250
- BlockDB Compression by @DracoLi in https://github.com/ava-labs/avalanchego/pull/4201
- Pass x/sync proofs as bytes by @alarso16 in https://github.com/ava-labs/avalanchego/pull/4246
- feat(load): parameterize worker count by @RodrigoVillar in https://github.com/ava-labs/avalanchego/pull/4248
- Add back schedule trigger to gh native by @aaronbuchwald in https://github.com/ava-labs/avalanchego/pull/4253
- Remove compare benchmark that uses gh action cache by @aaronbuchwald in https://github.com/ava-labs/avalanchego/pull/4252
- Delete gRPC client for MerkleDB by @alarso16 in https://github.com/ava-labs/avalanchego/pull/4251
- style(gas): rename to unit-agnostic duration by @alarso16 in https://github.com/ava-labs/avalanchego/pull/4258
- Fix testifylint config by @StephenButtolph in https://github.com/ava-labs/avalanchego/pull/4260
- Remove unnecessary field from MaybeBytes by @alarso16 in https://github.com/ava-labs/avalanchego/pull/4259
- fix: time remaining should use better estimates by @rkuris in https://github.com/ava-labs/avalanchego/pull/4196
- [tmpnet] Add optional stack traces to errors originating from tmpnet by @maru-ava in https://github.com/ava-labs/avalanchego/pull/4262
- [tmpnet] Use Api Node Instead of URI in CreateSubnets by @samliok in https://github.com/ava-labs/avalanchego/pull/4263
- [tmpnet] Upgrade prometheus agent version to avoid use of bitnami images by @maru-ava in https://github.com/ava-labs/avalanchego/pull/4269
- Add public network support to tmpnet by @felipemadero in https://github.com/ava-labs/avalanchego/pull/4267
- Remove proof details from x/sync by @alarso16 in https://github.com/ava-labs/avalanchego/pull/4247
- Don't unmarshal Stateless Block in XSVM by @samliok in https://github.com/ava-labs/avalanchego/pull/4279
- chore: fix some typos in comment by @joemicky in https://github.com/ava-labs/avalanchego/pull/4276
- Update config.md by @meaghanfitzgerald in https://github.com/ava-labs/avalanchego/pull/4278
- test(load): add firewood workflow by @RodrigoVillar in https://github.com/ava-labs/avalanchego/pull/4268
- chore: fix some function names by @zhoujiaweii in https://github.com/ava-labs/avalanchego/pull/4288
- test(reexecute/c): disable metrics collection by default by @RodrigoVillar in https://github.com/ava-labs/avalanchego/pull/4272
- uplift: Migrate ACP-176 Implementation by @ceyonur in https://github.com/ava-labs/avalanchego/pull/4291
- Handle ACP176 excess overflow during scaling by @StephenButtolph in https://github.com/ava-labs/avalanchego/pull/4294
- Implement ACP-226 Math by @ceyonur in https://github.com/ava-labs/avalanchego/pull/4289
- [monitoring] Clean up monitoring configuration in preparation for grafana cloud migration by @maru-ava in https://github.com/ava-labs/avalanchego/pull/4149
- Replace Coreth/ACP-176 package import  by @ceyonur in https://github.com/ava-labs/avalanchego/pull/4301
- Simplex Block Builder Component by @samliok in https://github.com/ava-labs/avalanchego/pull/4159
- ACP-226: add initial delay excess by @ceyonur in https://github.com/ava-labs/avalanchego/pull/4300
- ignore debug files in gitignore by @samliok in https://github.com/ava-labs/avalanchego/pull/4303
- Pass block tracker in deserialize block by @samliok in https://github.com/ava-labs/avalanchego/pull/4266
- Remove comment/fail on benchmark perf alerts by @aaronbuchwald in https://github.com/ava-labs/avalanchego/pull/4308
- Add HeightIndex interface to database by @DracoLi in https://github.com/ava-labs/avalanchego/pull/4133
- Upgrade to Go 1.24 by @alarso16 in https://github.com/ava-labs/avalanchego/pull/4304
- Move task args to cli instead of run_env by @aaronbuchwald in https://github.com/ava-labs/avalanchego/pull/4309
- Replace reflect.TypeOf with reflect.TypeFor by @StephenButtolph in https://github.com/ava-labs/avalanchego/pull/4311
- Consolidate scheduled runs by @aaronbuchwald in https://github.com/ava-labs/avalanchego/pull/4313
- Fix array type check in reflect codec by @StephenButtolph in https://github.com/ava-labs/avalanchego/pull/4312
- [tooling] Switch to go 1.24's `go tool` to manage CLI dependencies by @maru-ava in https://github.com/ava-labs/avalanchego/pull/4316
- Bump github.com/go-viper/mapstructure/v2 from 2.2.1 to 2.4.0 in /tools by @dependabot[bot] in https://github.com/ava-labs/avalanchego/pull/4319
- Fix waitForProposerWindow by @StephenButtolph in https://github.com/ava-labs/avalanchego/pull/4321
- Add test-unit-fast task by @StephenButtolph in https://github.com/ava-labs/avalanchego/pull/4323
- Granite ACP-176 by @alarso16 in https://github.com/ava-labs/avalanchego/pull/4336
- refactor(metervm): remove mockable clock by @RodrigoVillar in https://github.com/ava-labs/avalanchego/pull/4338
- Remove premature optimization in validator manager by @StephenButtolph in https://github.com/ava-labs/avalanchego/pull/4346
- Refactor Warp Verification Tests by @StephenButtolph in https://github.com/ava-labs/avalanchego/pull/4335
- Replace `mockable.MaxTime` with `upgrade.UnscheduledActivationTime` by @StephenButtolph in https://github.com/ava-labs/avalanchego/pull/4322
- fix(load): only modify non-reserved slots by @RodrigoVillar in https://github.com/ava-labs/avalanchego/pull/4283
- chore: fix a large number of spelling issues in comments by @letreturn in https://github.com/ava-labs/avalanchego/pull/4353
- Update daily re-execution benchmark by @aaronbuchwald in https://github.com/ava-labs/avalanchego/pull/4340
- Implement GetProposedHeight API in Proposervm by @geoff-vball in https://github.com/ava-labs/avalanchego/pull/4222
- Remove UptimeManager#IsConnected by @joshua-kim in https://github.com/ava-labs/avalanchego/pull/4333
- Set `activationTime` equal to `upgrade.InitiallyActiveTime` for `propservm` by @JonathanOppenheimer in https://github.com/ava-labs/avalanchego/pull/4351
- Support all validator set diffs by height by @geoff-vball in https://github.com/ava-labs/avalanchego/pull/4342
- Use `acp226.DelayExcess` rather than `uint64` by @StephenButtolph in https://github.com/ava-labs/avalanchego/pull/4358
- Add generics to x/sync by @alarso16 in https://github.com/ava-labs/avalanchego/pull/4275
- Improve C-Chain Re-Execution README by @aaronbuchwald in https://github.com/ava-labs/avalanchego/pull/4236
- Move canonical warp ordering to validators package by @StephenButtolph in https://github.com/ava-labs/avalanchego/pull/4363
- Move ginkgo tool usage to the main go.mod from tools/go.mod by @maru-ava in https://github.com/ava-labs/avalanchego/pull/4328
- Simplex ReplicationResponse.LatestRound Might Be Nil by @samliok in https://github.com/ava-labs/avalanchego/pull/4213
- feat: add in memory implementation of HeightIndex Database by @DracoLi in https://github.com/ava-labs/avalanchego/pull/4212
- Update prometheus params passed to run monitored tmpnet cmd by @aaronbuchwald in https://github.com/ava-labs/avalanchego/pull/4343
- [nix] Add package for official golang binaries by @maru-ava in https://github.com/ava-labs/avalanchego/pull/3824
- test only relevant packages for subnet-evm by @ceyonur in https://github.com/ava-labs/avalanchego/pull/4345
- feat(reexecution/c): add metervm metrics by @RodrigoVillar in https://github.com/ava-labs/avalanchego/pull/4369
- Update ledger dependencies to v1.1.0 by @felipemadero in https://github.com/ava-labs/avalanchego/pull/4347
- Revert #4333: "Remove UptimeManager#IsConnected" by @JonathanOppenheimer in https://github.com/ava-labs/avalanchego/pull/4379
- Bump github.com/go-viper/mapstructure/v2 from 2.3.0 to 2.4.0 by @dependabot[bot] in https://github.com/ava-labs/avalanchego/pull/4380
- Add warp accessors to `validators.State` by @StephenButtolph in https://github.com/ava-labs/avalanchego/pull/4373
- StatelessGraniteBlock types by @iansuvak in https://github.com/ava-labs/avalanchego/pull/4370
- Cache warp validator sets after Granite by @geoff-vball in https://github.com/ava-labs/avalanchego/pull/4170
- refactor(reexecution/c): rename  args by @RodrigoVillar in https://github.com/ava-labs/avalanchego/pull/4382
- feat(reexecution/c): print grafana link during local run by @RodrigoVillar in https://github.com/ava-labs/avalanchego/pull/4383
- [ci] Update run-monitored-tmpnet-cmd to not require tools/go.modfile by @maru-ava in https://github.com/ava-labs/avalanchego/pull/4384
- refactor: explicit libevm registration by @ARR4N in https://github.com/ava-labs/avalanchego/pull/4385
- fix: blockdb has block don't error if invalid block height by @DracoLi in https://github.com/ava-labs/avalanchego/pull/4354
- Refactor `initTestProposerVM` to take in `upgradetest.fork`  by @JonathanOppenheimer in https://github.com/ava-labs/avalanchego/pull/4371
- chore: update blockdb to use HeightIndex interface and errors in database pkg by @DracoLi in https://github.com/ava-labs/avalanchego/pull/4318
- Simplify waitForProposerWindow helper by @StephenButtolph in https://github.com/ava-labs/avalanchego/pull/4393
- Epoching ACP181 implementation by @geoff-vball in https://github.com/ava-labs/avalanchego/pull/4238
- fix(tests/e2e): register C-Chain `libevm` types by @ARR4N in https://github.com/ava-labs/avalanchego/pull/4399
- deps: bump go to version `1.24.8`  by @JonathanOppenheimer in https://github.com/ava-labs/avalanchego/pull/4403
- Remove duplicate header write by @StephenButtolph in https://github.com/ava-labs/avalanchego/pull/4408
- Add GetAllValidatorsAt endpoint by @geoff-vball in https://github.com/ava-labs/avalanchego/pull/4394
- Update coreth to v0.15.4-rc.4 by @StephenButtolph in https://github.com/ava-labs/avalanchego/pull/4414
- [nix] Extract Go derivation to nested flake for cross-repo reuse by @maru-ava in https://github.com/ava-labs/avalanchego/pull/4406
- chore(reexecution/c): revert metervm metrics changes by @RodrigoVillar in https://github.com/ava-labs/avalanchego/pull/4397
- Add network config to connect to all validators by @iansuvak in https://github.com/ava-labs/avalanchego/pull/4164
- Remove max contiguous height by @DracoLi in https://github.com/ava-labs/avalanchego/pull/4401
- Add initial EVM codeowners by @StephenButtolph in https://github.com/ava-labs/avalanchego/pull/4295
- change subnet proposervm delay default to 0 by @ceyonur in https://github.com/ava-labs/avalanchego/pull/4422
- feat(reexecute/c): decouple metrics server and collector by @RodrigoVillar in https://github.com/ava-labs/avalanchego/pull/4415
- chore: Fix TestGetStakingSigner for pre-release builds by @michaelkaplan13 in https://github.com/ava-labs/avalanchego/pull/4424
- Add SetPreferenceWithContext by @michaelkaplan13 in https://github.com/ava-labs/avalanchego/pull/4410
- Update go version to v1.24.9 by @StephenButtolph in https://github.com/ava-labs/avalanchego/pull/4428
- chore: fix the incorrect path in CONTRIBUTING.md by @withtimezone in https://github.com/ava-labs/avalanchego/pull/4421
- feat(sync/customrawdb): migrate customrawdb package from coreth by @powerslider in https://github.com/ava-labs/avalanchego/pull/4387
- uplift: (validators) - refactor uptime tracking from evm repos by @JonathanOppenheimer in https://github.com/ava-labs/avalanchego/pull/4166
- Remove unexpected workarounds of the prealloc linter by @StephenButtolph in https://github.com/ava-labs/avalanchego/pull/4431
- Skip prealloc linting in test files by @StephenButtolph in https://github.com/ava-labs/avalanchego/pull/4432
- uplift `database` package from evm repositories by @JonathanOppenheimer in https://github.com/ava-labs/avalanchego/pull/4331
- Add usetesting linter by @StephenButtolph in https://github.com/ava-labs/avalanchego/pull/4433
- feat: Add meterdb for heightindex database by @DracoLi in https://github.com/ava-labs/avalanchego/pull/4208
- Remove bool return from `uptimetracker.GetUptime`  by @JonathanOppenheimer in https://github.com/ava-labs/avalanchego/pull/4434
- Export uptimetracker error by @JonathanOppenheimer in https://github.com/ava-labs/avalanchego/pull/4436
- feat(reexecute/c): explicit metrics port by @RodrigoVillar in https://github.com/ava-labs/avalanchego/pull/4418
- Allow new nodes to sync delinquent L1s by @StephenButtolph in https://github.com/ava-labs/avalanchego/pull/4439
- Fix misleading comment on info.peers by @StephenButtolph in https://github.com/ava-labs/avalanchego/pull/4445
- Fix typos in config.md for clarity by @crStiv in https://github.com/ava-labs/avalanchego/pull/4449
- chore: Add EVM linters by @JonathanOppenheimer in https://github.com/ava-labs/avalanchego/pull/4444
- feat: Use the new ETA tracker for re-execution tests by @rkuris in https://github.com/ava-labs/avalanchego/pull/4352
- Bump github.com/consensys/gnark-crypto from 0.12.1 to 0.18.1 by @dependabot[bot] in https://github.com/ava-labs/avalanchego/pull/4440
- feat: `emulate` package for temporary `libevm` registration by @ARR4N in https://github.com/ava-labs/avalanchego/pull/4430
- Skip flaky tests by @StephenButtolph in https://github.com/ava-labs/avalanchego/pull/4456
- wallet: remove ledger support in favor of golang SDK implementation of ledger keychain by @felipemadero in https://github.com/ava-labs/avalanchego/pull/4413
- Implement RTT measurement by @yacovm in https://github.com/ava-labs/avalanchego/pull/4454
- docs: fix typos by @crStiv in https://github.com/ava-labs/avalanchego/pull/4455
- Update versions for v1.14.0 by @StephenButtolph in https://github.com/ava-labs/avalanchego/pull/4459

## New Contributors

- @qusuyan made their first contribution in https://github.com/ava-labs/avalanchego/pull/4214
- @joemicky made their first contribution in https://github.com/ava-labs/avalanchego/pull/4276
- @zhoujiaweii made their first contribution in https://github.com/ava-labs/avalanchego/pull/4288
- @letreturn made their first contribution in https://github.com/ava-labs/avalanchego/pull/4353
- @withtimezone made their first contribution in https://github.com/ava-labs/avalanchego/pull/4421

**Full Changelog**: https://github.com/ava-labs/avalanchego/compare/v1.13.5...v1.14.0