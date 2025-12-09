# wasmCloud - v1.9.0

**Release Name**: v1.9.0
**Published**: 2025-08-13T20:00:33Z
**Repository**: https://github.com/wasmCloud/wasmCloud

---

<!-- Release notes generated using configuration in .github/release.yml at v1.9.0 -->

## What's Changed
### Breaking Changes 🛠
* feat(host)!: implement traits for extending host functionality by @brooksmtownsend in https://github.com/wasmCloud/wasmCloud/pull/4407
* fix(provider-kv-redis)!: search secrets first for default redis URL by @vados-cosmonic in https://github.com/wasmCloud/wasmCloud/pull/4473
* feat(kv-provider-redis): enable disabling default connection by @vados-cosmonic in https://github.com/wasmCloud/wasmCloud/pull/4475
* chore(wasmcloud)!: bump to 1.9 for release by @brooksmtownsend in https://github.com/wasmCloud/wasmCloud/pull/4689
### New Features 🎉
* fix(wash): dev manifest option by @vados-cosmonic in https://github.com/wasmCloud/wasmCloud/pull/4347
* feat(host): track active component instances by @brooksmtownsend in https://github.com/wasmCloud/wasmCloud/pull/4398
* feat(wash): allow setting link_config via wash dev overrides by @vados-cosmonic in https://github.com/wasmCloud/wasmCloud/pull/4356
* feat(nats): Add names to nats connections by @nitame in https://github.com/wasmCloud/wasmCloud/pull/4031
* feat(wash): add information when new version is available by @f4z3r in https://github.com/wasmCloud/wasmCloud/pull/4425
* feat(providers): improve http server error message by @vados-cosmonic in https://github.com/wasmCloud/wasmCloud/pull/4472
* feat(provider-kv-redis): support connection pooling by @vados-cosmonic in https://github.com/wasmCloud/wasmCloud/pull/4480
* replace use of `~/.wash` with XDG Base Directory Specification by @f4z3r in https://github.com/wasmCloud/wasmCloud/pull/4558
* feat(ci): Starts process of moving release pipelines away from Nix by @thomastaylor312 in https://github.com/wasmCloud/wasmCloud/pull/4622
* feat(ci): Add workflows for scanning links and validating example docs by @lachieh in https://github.com/wasmCloud/wasmCloud/pull/4632
* feat(wash): add dashboard option for dev by @Bilaltariq98 in https://github.com/wasmCloud/wasmCloud/pull/4623
* feat(sqldb-postgres): support connection pool sharing by @brooksmtownsend in https://github.com/wasmCloud/wasmCloud/pull/4606
* feat(host): Add per component memory limits by @Aditya1404Sal in https://github.com/wasmCloud/wasmCloud/pull/4451
* feat(http-client): Add internal HTTP client provider and improve http-client codebase organization  by @brooksmtownsend in https://github.com/wasmCloud/wasmCloud/pull/4540
* feat(wash): Add check in wash ui to confirm server responds with a 200 by @Aditya1404Sal in https://github.com/wasmCloud/wasmCloud/pull/4671
### Bug Fixes 🐞
* fix: remove azurecr.io publishing and references by @brooksmtownsend in https://github.com/wasmCloud/wasmCloud/pull/4409
* fix(examples): set default OTEL_EXPORTER_OTLP_ENDPOINT in docker-comp… by @bragern in https://github.com/wasmCloud/wasmCloud/pull/4464
* fix(otel): add default endpoints for OpenTelemetry collectors by @ossfellow in https://github.com/wasmCloud/wasmCloud/pull/4494
* fix(wash): use context during wash call by @vados-cosmonic in https://github.com/wasmCloud/wasmCloud/pull/4502
* build(nix): update dependencies by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4484
* fix(examples): full OTEL-stack in docker-compose-full.yml by @bragern in https://github.com/wasmCloud/wasmCloud/pull/4512
* fix(wash): windows build suffix by @vados-cosmonic in https://github.com/wasmCloud/wasmCloud/pull/4527
* fix(keyvalue-redis): use default config for connection manager by @brooksmtownsend in https://github.com/wasmCloud/wasmCloud/pull/4550
* fix: add wasm-tools to dev dependencies for `wash` by @f4z3r in https://github.com/wasmCloud/wasmCloud/pull/4557
* fix(wash): pass host key seed to infer host id rather than read from log by @f4z3r in https://github.com/wasmCloud/wasmCloud/pull/4568
* fix(host): start provider from file by CLI by @if0ne in https://github.com/wasmCloud/wasmCloud/pull/4646
* fix: use allow-latest for allow_latest, default registry config improvement by @brooksmtownsend in https://github.com/wasmCloud/wasmCloud/pull/4411
* fix(wasmbus): expect when we should've mapped by @brooksmtownsend in https://github.com/wasmCloud/wasmCloud/pull/4703
### Other Changes
* chore(deps): bump taiki-e/install-action from 2.49.49 to 2.50.0 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4386
* chore(deps): bump crossbeam-channel from 0.5.14 to 0.5.15 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4389
* chore(deps): update example (local.)wadm.yaml and readme files by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4387
* build(nix): update OCI image bases by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4390
* chore(deps): bump renovatebot/github-action from 41.0.20 to 41.0.21 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4385
* chore(deps): bump clap from 4.5.36 to 4.5.37 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4381
* chore(deps): bump exponential-backoff from 2.0.0 to 2.1.0 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4377
* build(nix): update OCI image bases by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4404
* chore(deps): bump golang.org/x/net from 0.36.0 to 0.38.0 in /examples/security/opa by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4384
* chore(ci): Remove language-specific rules from CODEOWNERS by @joonas in https://github.com/wasmCloud/wasmCloud/pull/4391
* chore(deps): bump docker/build-push-action from 6.15.0 to 6.16.0 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4402
* build(nix): update dependencies by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4382
* chore(deps): bump actions/download-artifact from 4.2.1 to 4.3.0 in the upload-download-artifact group by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4400
* chore: Updates all pinned deps by @thomastaylor312 in https://github.com/wasmCloud/wasmCloud/pull/4412
* chore(deps): bump renovatebot/github-action from 41.0.21 to 41.0.22 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4413
* chore(deps): bump github/codeql-action from 3.28.15 to 3.28.16 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4396
* chore(deps): bump taiki-e/install-action from 2.50.0 to 2.50.5 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4423
* chore(deps): bump actions/create-github-app-token from 2.0.2 to 2.0.5 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4424
* chore(deps): bump oras-project/setup-oras from 1.2.2 to 1.2.3 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4419
* chore(deps): bump actions/setup-python from 5.5.0 to 5.6.0 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4403
* chore(deps): bump wasm-encoder from 0.228.0 to 0.229.0 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4418
* chore(deps): bump github/codeql-action from 3.28.16 to 3.28.17 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4427
* chore(deps): bump taiki-e/install-action from 2.50.5 to 2.50.7 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4428
* chore(deps): bump actions/create-github-app-token from 2.0.5 to 2.0.6 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4429
* chore(deps): bump renovatebot/github-action from 41.0.22 to 42.0.1 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4430
* chore(deps): bump rand from 0.9.0 to 0.9.1 in /tests/components/rust by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4379
* chore(deps): bump clap-markdown from 0.1.4 to 0.1.5 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4431
* chore(deps): bump taiki-e/install-action from 2.50.7 to 2.50.8 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4432
* chore(deps): bump sha2 from 0.10.8 to 0.10.9 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4414
* chore(deps): bump DeterminateSystems/nix-installer-action from 16 to 17 in /.github/actions/install-nix by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4399
* chore(deps): bump taiki-e/install-action from 2.50.8 to 2.50.9 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4436
* build(nix): update OCI image bases by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4437
* chore(host): Reference wasmcloud_core::rpc helper methods consistently by @joonas in https://github.com/wasmCloud/wasmCloud/pull/4440
* chore(deps): bump taiki-e/install-action from 2.50.9 to 2.50.10 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4442
* chore(deps): bump actions/setup-go from 5.4.0 to 5.5.0 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4441
* build(nix): update OCI image bases by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4443
* chore(deps): bump docker_credential from 1.3.1 to 1.3.2 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4435
* chore(deps): bump clap_complete from 4.5.48 to 4.5.50 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4434
* chore(deps): bump renovatebot/github-action from 42.0.1 to 42.0.2 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4447
* build(nix): update OCI image bases by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4450
* chore: Address `cargo clippy` feedback by @joonas in https://github.com/wasmCloud/wasmCloud/pull/4453
* build(nix): update OCI image bases by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4454
* chore(wash): Address cargo clippy feedback by @joonas in https://github.com/wasmCloud/wasmCloud/pull/4456
* build(nix): update dependencies by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4457
* chore(deps): bump golang.org/x/net from 0.27.0 to 0.38.0 in /examples/golang/providers/custom-template by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4449
* chore(deps): bump webpki-roots from 0.26.9 to 1.0.0 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4433
* chore: Bump nats-server version to 2.11.3 by @joonas in https://github.com/wasmCloud/wasmCloud/pull/4452
* chore(deps): bump docker/build-push-action from 6.16.0 to 6.17.0 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4459
* build(nix): update dependencies by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4460
* chore(deps): bump github.com/open-policy-agent/opa from 0.68.0 to 1.4.0 in /examples/security/opa by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4448
* chore(deps): bump github/codeql-action from 3.28.17 to 3.28.18 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4463
* chore(deps): bump tower-http from 0.6.2 to 0.6.4 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4445
* chore(deps): bump taiki-e/install-action from 2.50.10 to 2.51.1 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4462
* build(nix): update dependencies by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4465
* chore(deps): bump DeterminateSystems/nix-installer-action from 16 to 17 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4401
* chore(deps): bump clap from 4.5.37 to 4.5.38 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4470
* chore(deps): bump taiki-e/install-action from 2.51.1 to 2.51.2 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4468
* build(nix): update dependencies by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4471
* chore(deps): bump tokio from 1.43.0 to 1.45.0 in /examples/rust/components/http-keyvalue-counter by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4466
* chore(deps): bump renovatebot/github-action from 42.0.2 to 42.0.3 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4469
* chore(deps): bump tokio from 1.43.0 to 1.45.0 in /examples/rust/components/http-hello-world by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4467
* chore(deps): bump tempfile from 3.19.1 to 3.20.0 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4446
* chore(deps): bump taiki-e/install-action from 2.51.2 to 2.51.3 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4478
* build(nix): update dependencies by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4479
* chore(deps): bump axum from 0.8.3 to 0.8.4 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4476
* chore(deps): bump tokio from 1.44.2 to 1.45.0 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4482
* build(nix): update OCI image bases by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4483
* chore(deps): bump hyper-util from 0.1.11 to 0.1.12 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4477
* chore(provider-kv-redis): release v0.30.0 by @vados-cosmonic in https://github.com/wasmCloud/wasmCloud/pull/4487
* chore(wash): update default host version to 1.8.0 by @vados-cosmonic in https://github.com/wasmCloud/wasmCloud/pull/4488
* Release wash by @github-actions[bot] in https://github.com/wasmCloud/wasmCloud/pull/4489
* chore(deps): bump taiki-e/install-action from 2.51.3 to 2.52.0 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4490
* build(nix): update OCI image bases by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4493
* build(nix): update OCI image bases by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4498
* chore(deps): bump renovatebot/github-action from 42.0.3 to 42.0.4 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4501
* chore(deps): bump aws-config from 1.6.2 to 1.6.3 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4491
* chore(release): bump versions by @vados-cosmonic in https://github.com/wasmCloud/wasmCloud/pull/4495
* chore(deps): bump uuid from 1.16.0 to 1.17.0 in /tests/components/rust by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4496
* chore(deps): bump taiki-e/install-action from 2.52.0 to 2.52.2 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4504
* chore(deps): bump wat from 1.229.0 to 1.232.0 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4505
* chore(deps): bump hyper-util from 0.1.12 to 0.1.13 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4506
* chore(wascap): bump version by @vados-cosmonic in https://github.com/wasmCloud/wasmCloud/pull/4507
* chore(secrets-types): bump version by @vados-cosmonic in https://github.com/wasmCloud/wasmCloud/pull/4508
* chore(deps): update versions to enable release by @vados-cosmonic in https://github.com/wasmCloud/wasmCloud/pull/4509
* Release wash by @github-actions[bot] in https://github.com/wasmCloud/wasmCloud/pull/4510
* Release wasmcloud-test-util by @github-actions[bot] in https://github.com/wasmCloud/wasmCloud/pull/4511
* chore(deps): bump tokio from 1.45.0 to 1.45.1 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4515
* Release wash by @github-actions[bot] in https://github.com/wasmCloud/wasmCloud/pull/4518
* build(nix): update OCI image bases by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4516
* chore(deps): bump docker/build-push-action from 6.17.0 to 6.18.0 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4503
* build(nix): update dependencies by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4520
* chore(deps): bump clap from 4.5.38 to 4.5.39 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4519
* chore(deps): bump taiki-e/install-action from 2.52.2 to 2.52.3 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4523
* chore(deps): bump ossf/scorecard-action from 2.4.1 to 2.4.2 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4524
* build(nix): update dependencies by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4526
* chore(deps): bump rustls from 0.22.4 to 0.23.26 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4458
* build(nix): update OCI image bases by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4525
* build(nix): update dependencies by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4528
* chore(deps): bump taiki-e/install-action from 2.52.3 to 2.52.6 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4541
* build(nix): update dependencies by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4529
* chore(deps): update ghcr.io/wasmcloud/keyvalue-redis docker tag to v0.30.0 by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4552
* build(nix): update OCI image bases by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4533
* chore(deps): Updates to latest OCI dependencies by @thomastaylor312 in https://github.com/wasmCloud/wasmCloud/pull/4553
* chore(deps): bump softprops/action-gh-release from 2.2.2 to 2.3.2 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4548
* chore(deps): bump wasm-encoder from 0.229.0 to 0.232.0 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4514
* chore(deps): bump tower-http from 0.6.4 to 0.6.6 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4539
* chore(deps): bump github/codeql-action from 3.28.18 to 3.29.0 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4551
* chore(deps): bump docker/setup-buildx-action from 3.10.0 to 3.11.0 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4560
* chore(deps): bump renovatebot/github-action from 42.0.4 to 42.0.6 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4561
* build(nix): update dependencies by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4544
* build(nix): update dependencies by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4567
* build(nix): update OCI image bases by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4566
* chore(charts): bump wasmcloud-host by @ricochet in https://github.com/wasmCloud/wasmCloud/pull/4571
* chore(charts): bump host and wadm by @ricochet in https://github.com/wasmCloud/wasmCloud/pull/4569
* chore(deps): bump taiki-e/install-action from 2.52.6 to 2.53.2 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4574
* chore(deps): bump acifani/setup-tinygo from 2.0.0 to 2.0.1 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4537
* chore(deps): bump hyper-util from 0.1.13 to 0.1.14 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4565
* chore(deps): bump uuid from 1.16.0 to 1.17.0 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4564
* chore(deps): bump taiki-e/cache-cargo-install-action from 2.1.1 to 2.1.2 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4572
* chore(deps): bump EmbarkStudios/cargo-deny-action from 2.0.11 to 2.0.12 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4578
* chore(deps): bump docker/setup-buildx-action from 3.11.0 to 3.11.1 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4573
* refactor(wash): remove duplicate constant for wadm.pid filename by @f4z3r in https://github.com/wasmCloud/wasmCloud/pull/4580
* chore: update reviewers for OCI base image updates by @vados-cosmonic in https://github.com/wasmCloud/wasmCloud/pull/4581
* chore(runtime): Expose wasmtime linker by @lxfontes in https://github.com/wasmCloud/wasmCloud/pull/4588
* chore(deps): bump renovatebot/github-action from 42.0.6 to 43.0.0 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4585
* chore(deps): bump marocchino/sticky-pull-request-comment from 2.9.2 to 2.9.3 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4584
* chore(deps): bump rustversion from 1.0.20 to 1.0.21 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4543
* chore(deps): bump clap_complete from 4.5.50 to 4.5.54 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4582
* chore(deps): bump clap from 4.5.39 to 4.5.40 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4583
* chore(deps): bump taiki-e/install-action from 2.53.2 to 2.54.0 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4589
* chore: Add new maintainers to file by @thomastaylor312 in https://github.com/wasmCloud/wasmCloud/pull/4594
* chore(deps): bump renovatebot/github-action from 43.0.0 to 43.0.1 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4590
* chore(deps): bump serde_with from 3.12.0 to 3.13.0 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4591
* build(nix): update OCI image bases by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4575
* build(nix): update dependencies by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4576
* chore(deps): bump Swatinem/rust-cache from 2.7.8 to 2.8.0 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4597
* test(wasmcloud): disable builtin_http_path_routing by @brooksmtownsend in https://github.com/wasmCloud/wasmCloud/pull/4599
* build(nix): update dependencies by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4605
* chore(deps): bump github/codeql-action from 3.29.0 to 3.29.2 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4612
* chore(deps): bump taiki-e/cache-cargo-install-action from 2.1.2 to 2.2.0 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4613
* chore(deps): bump taiki-e/install-action from 2.54.0 to 2.55.3 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4614
* build(nix): update dependencies by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4609
* chore(deps): update ghcr.io/wasmcloud/http-server docker tag to v0.27.0 by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4610
* chore(deps): bump renovatebot/github-action from 43.0.1 to 43.0.2 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4615
* chore(deps): bump reqwest from 0.12.15 to 0.12.21 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4611
* build(nix): update OCI image bases by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4604
* chore(deps): bump async-compression from 0.4.23 to 0.4.25 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4598
* chore(deps): bump taiki-e/install-action from 2.53.0 to 2.56.8 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4634
* chore(deps): bump mlugg/setup-zig from 2.0.1 to 2.0.4 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4630
* chore(deps): bump DeterminateSystems/nix-installer-action from 17 to 18 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4626
* chore: update wit-bindgen in rust examples by @brooksmtownsend in https://github.com/wasmCloud/wasmCloud/pull/4635
* build(nix): update OCI image bases by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4619
* build(nix): update OCI image bases by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4653
* chore(deps): bump taiki-e/install-action from 2.56.8 to 2.56.17 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4656
* chore(deps): bump serde_json from 1.0.140 to 1.0.141 in /tests/components/rust by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4655
* chore(deps): bump DeterminateSystems/nix-installer-action from 18 to 19 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4650
* chore(deps): bump DeterminateSystems/nix-installer-action from 17 to 19 in /.github/actions/install-nix by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4651
* chore(deps): bump docker/setup-buildx-action from 3.10.0 to 3.11.1 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4629
* chore(deps): bump renovatebot/github-action from 43.0.2 to 43.0.3 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4648
* chore(deps): bump marocchino/sticky-pull-request-comment from 2.9.3 to 2.9.4 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4654
* chore(deps): bump rand from 0.9.1 to 0.9.2 in /tests/components/rust by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4658
* chore(deps): bump taiki-e/cache-cargo-install-action from 2.2.0 to 2.3.0 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4660
* chore(deps): bump github/codeql-action from 3.29.2 to 3.29.3 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4661
* chore(deps): bump renovatebot/github-action from 43.0.3 to 43.0.4 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4662
* chore(deps): bump mlugg/setup-zig from 2.0.4 to 2.0.5 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4663
* chore(deps): bump taiki-e/install-action from 2.56.17 to 2.56.21 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4659
* chore(deps): bump anstyle from 1.0.10 to 1.0.11 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4617
* build(nix): update dependencies by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4620
* chore(deps): bump taiki-e/install-action from 2.56.21 to 2.57.2 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4678
* chore(deps): bump renovatebot/github-action from 43.0.4 to 43.0.5 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4672
* build(nix): update OCI image bases by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4664
* chore(deps): bump rand from 0.9.1 to 0.9.2 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4667
* build(nix): update dependencies by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4670
* chore(deps): bump wat from 1.232.0 to 1.236.0 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4676
* chore(CONTRIBUTING): update to suggest wasmcloud/contrib by @brooksmtownsend in https://github.com/wasmCloud/wasmCloud/pull/4680
* chore(deps): bump webpki-roots from 1.0.0 to 1.0.2 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4683
* chore(deps): bump taiki-e/install-action from 2.57.2 to 2.57.4 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4685
* chore(deps): bump github/codeql-action from 3.29.3 to 3.29.5 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4677
* build(nix): update dependencies by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4686
* build(nix): update OCI image bases by @wasmcloud-automation-app[bot] in https://github.com/wasmCloud/wasmCloud/pull/4696
* chore(deps): bump renovatebot/github-action from 43.0.5 to 43.0.7 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4713
* chore(deps): bump taiki-e/install-action from 2.57.4 to 2.58.9 by @dependabot[bot] in https://github.com/wasmCloud/wasmCloud/pull/4714

## New Contributors
* @bragern made their first contribution in https://github.com/wasmCloud/wasmCloud/pull/4464
* @f4z3r made their first contribution in https://github.com/wasmCloud/wasmCloud/pull/4425
* @miguelraz made their first contribution in https://github.com/wasmCloud/wasmCloud/pull/4535
* @Bilaltariq98 made their first contribution in https://github.com/wasmCloud/wasmCloud/pull/4623
* @if0ne made their first contribution in https://github.com/wasmCloud/wasmCloud/pull/4646

**Full Changelog**: https://github.com/wasmCloud/wasmCloud/compare/v1.8.0...v1.9.0