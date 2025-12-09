# Tinkerbell - v0.22.0

**Release Name**: v0.22.0
**Published**: 2025-12-01T18:24:07Z
**Repository**: https://github.com/tinkerbell/tinkerbell

---

<!-- Release notes generated using configuration in .github/release.yml at v0.22.0 -->

## What's Changed
### Smee
* dhcp: add support domain name option by @clwluvw in https://github.com/tinkerbell/tinkerbell/pull/376
* Properly handle DHCP headers and options that need to be IPs: by @jacobweinstock in https://github.com/tinkerbell/tinkerbell/pull/375
* Create the iPXE extra version in one place: by @jacobweinstock in https://github.com/tinkerbell/tinkerbell/pull/379
* dhcp: log reason from option 56 on unknown message types by @clwluvw in https://github.com/tinkerbell/tinkerbell/pull/382
* dhcp: allow dhcp to reply custom TFTPServerName and BootFileName by @clwluvw in https://github.com/tinkerbell/tinkerbell/pull/383
* Add TLS termination by @jacobweinstock in https://github.com/tinkerbell/tinkerbell/pull/358
* Allow overriding the source ISO/multi-arch ISO support: by @jacobweinstock in https://github.com/tinkerbell/tinkerbell/pull/396
### Tink Controller
* Add netmaskToPrefix template function by @rahulbabu95 in https://github.com/tinkerbell/tinkerbell/pull/411
* Fix comment example for formatPartition function by @magicaljellybeans in https://github.com/tinkerbell/tinkerbell/pull/418
### Tink Server
* Don't impede Workflows on Auto discovery errors: by @jacobweinstock in https://github.com/tinkerbell/tinkerbell/pull/410
### Helm Chart
* Add Global bind address by @jacobweinstock in https://github.com/tinkerbell/tinkerbell/pull/374
* Update helm chart optional versions: by @jacobweinstock in https://github.com/tinkerbell/tinkerbell/pull/388
* Require successful container image push: by @jacobweinstock in https://github.com/tinkerbell/tinkerbell/pull/389
* Helm: hookos hostnetwork should be configurable like tinkerbell by @jakerbeck in https://github.com/tinkerbell/tinkerbell/pull/390
* Helm: Add HOST_IP to tinkerbell pod environment variables from the Downward API ... by @jakerbeck in https://github.com/tinkerbell/tinkerbell/pull/394
* fix(helm): add missing namespace in ConfigMap by @mcanevet in https://github.com/tinkerbell/tinkerbell/pull/416
* chart (fix): add tolerations to deployment, hookos, and kubevip by @muse-sisay in https://github.com/tinkerbell/tinkerbell/pull/417
### Dependencies
* Bump github.com/gin-gonic/gin from 1.10.1 to 1.11.0 by @dependabot[bot] in https://github.com/tinkerbell/tinkerbell/pull/387
* Bump go.etcd.io/etcd/server/v3 from 3.6.4 to 3.6.5 by @dependabot[bot] in https://github.com/tinkerbell/tinkerbell/pull/385
* Bump github.com/nats-io/nats.go from 1.45.0 to 1.46.0 by @dependabot[bot] in https://github.com/tinkerbell/tinkerbell/pull/386
* Bump github.com/nats-io/nats.go from 1.46.0 to 1.46.1 by @dependabot[bot] in https://github.com/tinkerbell/tinkerbell/pull/392
* Bump google.golang.org/protobuf from 1.36.9 to 1.36.10 by @dependabot[bot] in https://github.com/tinkerbell/tinkerbell/pull/402
* Bump github.com/docker/docker from 28.4.0+incompatible to 28.5.0+incompatible by @dependabot[bot] in https://github.com/tinkerbell/tinkerbell/pull/406
* Bump planetscale/ghcommit-action from 0.2.17 to 0.2.18 by @dependabot[bot] in https://github.com/tinkerbell/tinkerbell/pull/400
* Bump github.com/go-playground/validator/v10 from 10.27.0 to 10.28.0 by @dependabot[bot] in https://github.com/tinkerbell/tinkerbell/pull/403
* Bump golang.org/x/sys from 0.36.0 to 0.37.0 by @dependabot[bot] in https://github.com/tinkerbell/tinkerbell/pull/401
* Bump golang.org/x/net from 0.44.0 to 0.45.0 by @dependabot[bot] in https://github.com/tinkerbell/tinkerbell/pull/405
* Bump google.golang.org/grpc from 1.75.1 to 1.76.0 by @dependabot[bot] in https://github.com/tinkerbell/tinkerbell/pull/407
* Upgrade dependencies; bmclib redfish fix: by @jacobweinstock in https://github.com/tinkerbell/tinkerbell/pull/409
* Bump github.com/quic-go/quic-go from 0.54.0 to 0.54.1 by @dependabot[bot] in https://github.com/tinkerbell/tinkerbell/pull/408
* Bump github.com/ccoveille/go-safecast from 1.6.1 to 1.7.0 by @dependabot[bot] in https://github.com/tinkerbell/tinkerbell/pull/412
* Bump github.com/avast/retry-go/v4 from 4.6.1 to 4.7.0 by @dependabot[bot] in https://github.com/tinkerbell/tinkerbell/pull/413
* Bump github.com/nats-io/nats.go from 1.46.1 to 1.47.0 by @dependabot[bot] in https://github.com/tinkerbell/tinkerbell/pull/414
* Bump github.com/jaypipes/ghw from 0.19.1 to 0.20.0 by @dependabot[bot] in https://github.com/tinkerbell/tinkerbell/pull/421
* Bump actions/download-artifact from 5 to 6 by @dependabot[bot] in https://github.com/tinkerbell/tinkerbell/pull/420
* Bump actions/upload-artifact from 4 to 5 by @dependabot[bot] in https://github.com/tinkerbell/tinkerbell/pull/419
* Remove github.com/opencontainers/runtime-spec: by @jacobweinstock in https://github.com/tinkerbell/tinkerbell/pull/432
* Deps update by @jacobweinstock in https://github.com/tinkerbell/tinkerbell/pull/433
* Bump golang.org/x/sys from 0.37.0 to 0.38.0 by @dependabot[bot] in https://github.com/tinkerbell/tinkerbell/pull/435
* Bump go.etcd.io/etcd/server/v3 from 3.6.5 to 3.6.6 by @dependabot[bot] in https://github.com/tinkerbell/tinkerbell/pull/439
* Bump golang.org/x/net from 0.46.0 to 0.47.0 by @dependabot[bot] in https://github.com/tinkerbell/tinkerbell/pull/436
* Bump github.com/opencontainers/selinux from 1.12.0 to 1.13.0 by @dependabot[bot] in https://github.com/tinkerbell/tinkerbell/pull/442
* Bump golang.org/x/crypto from 0.44.0 to 0.45.0 by @dependabot[bot] in https://github.com/tinkerbell/tinkerbell/pull/448
* Bump planetscale/ghcommit-action from 0.2.18 to 0.2.19 by @dependabot[bot] in https://github.com/tinkerbell/tinkerbell/pull/446
* Bump google.golang.org/grpc from 1.76.0 to 1.77.0 by @dependabot[bot] in https://github.com/tinkerbell/tinkerbell/pull/447
* Bump go.uber.org/zap from 1.27.0 to 1.27.1 by @dependabot[bot] in https://github.com/tinkerbell/tinkerbell/pull/451
* Bump actions/checkout from 5 to 6 by @dependabot[bot] in https://github.com/tinkerbell/tinkerbell/pull/450
### General
* Add String method to netip.Addr: by @jacobweinstock in https://github.com/tinkerbell/tinkerbell/pull/377
* Improve pointer handling for netip package: by @jacobweinstock in https://github.com/tinkerbell/tinkerbell/pull/378
* Update iPXE binaries by @github-actions[bot] in https://github.com/tinkerbell/tinkerbell/pull/380
* Add documentation on the release cadence: by @jacobweinstock in https://github.com/tinkerbell/tinkerbell/pull/381
* Update iPXE script, auto.ipxe, URI by @jacobweinstock in https://github.com/tinkerbell/tinkerbell/pull/384
* Enable Mergify in-place checks: by @jacobweinstock in https://github.com/tinkerbell/tinkerbell/pull/393
* Fix link by @jacobweinstock in https://github.com/tinkerbell/tinkerbell/pull/422
* Fix link: by @jacobweinstock in https://github.com/tinkerbell/tinkerbell/pull/423

## New Contributors
* @jakerbeck made their first contribution in https://github.com/tinkerbell/tinkerbell/pull/390
* @rahulbabu95 made their first contribution in https://github.com/tinkerbell/tinkerbell/pull/411
* @mcanevet made their first contribution in https://github.com/tinkerbell/tinkerbell/pull/416
* @magicaljellybeans made their first contribution in https://github.com/tinkerbell/tinkerbell/pull/418

**Full Changelog**: https://github.com/tinkerbell/tinkerbell/compare/v0.21.0...v0.22.0