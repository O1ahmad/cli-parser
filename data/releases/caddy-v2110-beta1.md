# Caddy - v2.11.0-beta.1

**Release Name**: v2.11.0-beta.1
**Published**: 2025-12-04T20:48:19Z
**Repository**: https://github.com/caddyserver/caddy

---

Welcome to the beta version of 2.11. This is the first release made by our [new, automated release process](https://github.com/caddyserver/caddy/pull/7383) developed by @Mohammed90 that was carried out and approved entirely by our maintainer team (together with @francislavoie) without intervention from @mholt, the original Caddy author. This represents a significant step forward in [project autonomy and growth](https://caddy.community/t/next-steps-for-the-caddy-project-maintainership/33076), ensuring that the project's stability and longevity is not reliant upon a single person.

This first beta release was primarily to test our new workflow, so there's still a couple things left to do before the stable release.

Featured here are numerous, mostly minor, bug fixes and enhancements, mostly affecting edge cases or niche corners of the software; for example, proxying H2C or HTTP/3, obscure Caddyfile scenarios, and named socket activation.

Some notable changes:

- SIGUSR1 can be used to reload configuration only if it was loaded from a file using the CLI, and not changed by the API since then.
- We replaced "lumberjack", our logging library, with a fork "timberjack" that supports the oft-requested time-rolling ability.
- Caddy can now bind listeners with named socket activation.

Before the final release, we expect ECH key rotation to be enabled as well as a few other patches/features

Thank you to our sponsors and contributors for all that you do!

## Changelog
* 5473eb95d8e94505b8c06955bd200f37179c54a2  encode: fix response corruption when handle_errors is used (#7235)
* 13a4ec7597f8e9ebe105b0ee89102ba521f21173 basicauth: Implement argon2id (#7186)
* 6d90c7707dac3026c1b28fba615b1962d2cd45e1 build(deps): bump github.com/slackhq/nebula from 1.9.5 to 1.9.7 (#7315)
* eead249382ac14c29d82ec75f30df7638e879567 build(deps): bump golang.org/x/crypto from 0.43.0 to 0.45.0 (#7355)
* 2d0f3f887bc1f70c52fc183ebcc6225f7f91c041 build(deps): bump the actions-deps group with 5 updates (#7237)
* afbdcec08bbd7471b9b5e5ed209881dfcc51bd6c build(deps): bump the actions-deps group with 8 updates (#7284)
* cd1c203777e89a64c8426c049727c58fbebc1276 build(deps): bump the all-updates group across 1 directory with 2 updates (#7307)
* 39357d3e5cb6124e8af651460cc8ab6975c637b8 build(deps): bump the all-updates group with 17 updates (#7236)
* 786d5378771d068440b7ddd8c310851bb7b9afe0 build(deps): bump the all-updates group with 3 updates (#7376)
* 07d2aaf22ef8225575b9557640806bc895067905 build(deps): bump the all-updates group with 4 updates (#7333)
* 0ba8786b35eaec5ec53f8562bec9587e6b1e6a8b caddyfile: Allow `block` to do nothing if nothing passed to `import` (#7206)
* 92c8bc73228aad9eb0b396fdb687c024124d8dbd caddyfile: fix nested quotes formatted incorrectly by fmt (#7045)
* 6d73d85c1fd3d20acaaadc0fb69e3f562d92f685 caddyfile: prevent adding trailing space on line before env variable (#7215)
* d7185fd002a2c57d20a98d3e94442da7b259b3ad caddyhttp: Add `trusted_proxies_unix` for trusting unix socket `X-Forwarded-*` headers (#7265)
* de6b78009b840eb395c33b8d65c5d32746df38b6 caddyhttp: Add server options `keepalive_idle` and `keepalive_count` (#7298)
* e0a8f9541d155b7385b78d2b8bbe2fad53bb6295 caddyhttp: Normalize (lowercase) {label.N} placeholders
* 5e2953670ed7eecbc34146b5d12cca7dd85ac580 caddyhttp: add replacer placeholders for escaped values (#7181)
* 8285eba8426e3c75ed81d6a8c5cd6ec685430d47 caddyhttp: allow customizing the Server header (#7338)
* bc0e1841305b2cc82aeaf9953e527d9819a88c83 caddyhttp: omit unnecessary reassignment (#7276)
* 3553cfb6adb2954a53d559c1841c8072b9921e61 caddyhttp: remove redundant middleware next copy (#7217)
* 1ce2a13ad10eab5693b425056c571621f5d860e9 caddyhttp: wrap accepted connection to suppress tls.ConnectionState (#7247)
* d9cc24f3df663e1bab58dc08ac12bf818c9f6852 caddypki: Disable internal auto-CA when auto_https is disabled (fix #7211) (#7238)
* 1e82f9652ec561cc0c84bec501976045aa01a310 caddypki: check intermediate lifetime to actual root cert lifetime (#7272)
* 38848f7f2525777edd0241ad3118f070e045d771 caddytls: Allow disabling distributed solving (except http-01)
* ddec1838b39a1b61432db4e78f2e752f27c3c769 caddytls: correct documentation of `LeafFolderLoader` (#7327)
* f5c3094050566d8d4fcf9f3ecf7d26f9c3241c65 cmd: prevent commas in header values from being split (#7268)
* 65e0ddc22137bbbaa68c842ae0b98d0548504545 core: Reloading with `SIGUSR1` if config never changed via admin (#7258)
* b3f2db233b5a71df6680b43d025bdb62ee2a999c core: custom slog handlers for modules (log contextual data) (#7346)
* b2ab419922e0dabc2956611531f73a6169ecc46f core: use reflect.TypeFor to check for encoding/json.RawMessage (#7274)
* 806fef85bedfc3fe178560afe6212c8ae90d3ebe encode: add graphql-response header to list (#7214)
* 2cb426776c091febccc6b9a6669f1c5a745648a4 encode: modernize, replace HasSuffix+TrimSuffix with CutSuffix (#7357)
* b462615439bf354dd1cb6780fb564b6a6c4a352c fileserver: set Content-Length for precompressed files (#7251)
* 0c8798fce36b0915ff39288bff7eddfad2a1673f go.mod: update quic-go to v0.54.1 (#7273)
* 3c003deec67ed1ca0127f4b303c64760a9a7b19d httpcaddyfile: Add missing DNS challenge check for `acme_dns` (#7270)
* 2f1d270968e050105e3f6814b1ef7e7660ed41ba httpcaddyfile: Map default_bind to BindHost in globalACMEDefaults (#7278)
* a7885aabec375db38ac6c221c7c709dc83122535 intercept: use already buffered response if possible when intercepting (#7028)
* 156ce99d3a46be8cefe8502b2c30b757e4deb79f listeners: Add support for named socket activation (#7243)
* 39ace450deb23a8ebb4f41ff4d8cfe2800d68118 logging: Adjustments to BufferedLog to keep logs in the correct order (#7257)
* 012b4b3d40dae32502503c9d6bc6333acb135cb3 logging: Buffer the logs before config is loaded (#7245)
* 10ac7da037828c5179ad7d04309fc8912f2fe0d5 logging: Switch from `lumberjack` to `timberjack`, add time-rolling options (#7244)
* f5f25d845a814a600102614cc8836af5ebe1487b logging: fix multiple regexp filters on same field (fixes #7049) (#7061)
* 595aab8bc0d98c510c044a2a6b8e7053aaf4e8fb metrics: resolve per-host inifinite cardinality (#7306)
* 57587ed18e3908931b4f7bfd73078c47082fb742 refactor: use reflect.TypeFor (#7313)
* 2ec28bca43e5269511f8d9c1656244dd84acdad9 reverse_proxy: use http1 for outbound tls requests with placeholder that are likely websockets (#7296)
* a6da1acdc86199a7f99fa2347d5f91cd59ff90d8 reverse_proxy: use interfaces to modify the behaviors of the transports (#7353)
* 67a9e0657e60df8c78510065e8977d86ee17d01c reverseproxy: Fix retries for requests with bodies (#7360)
* 7fb39ec1e56751c82950fa8a35a189ea39dfa005 reverseproxy: Use http1.1 upgrade for websocket for extended connect of http2 and http3 (#7305)
* 8aca108d2c9d9e9ff3a39ff00684ea58df1338f6 reverseproxy: do not disable keepalive if proxy protocol is used (#7300)
* abe0acabb61b0151f58c7b750d3963dbbffe7270 reverseproxy: set default values for keepalive if only some of them are set (#7318)
* 1e21b660c42485cb47287b595900446093d3df2b reverseproxy: use http.Protocols to handle h2c requests (#6990)
* b54e870b26a23a98d81967c80d9e875f3a9e3c1d tracing: switch to autoexport for OpenTelemetry span exporter (#7317)

## What's Changed
* caddyhttp: add replacer placeholders for escaped values by @Qusic in https://github.com/caddyserver/caddy/pull/7181
* AI assistance disclosure by @mholt in https://github.com/caddyserver/caddy/pull/7212
* caddyfile: Prevent trailing space on line before env variable - Fixes #6881 by @arpansaha13 in https://github.com/caddyserver/caddy/pull/7215
* add: encode header Content-Type graphql-response by @aro-lew in https://github.com/caddyserver/caddy/pull/7214
* caddyhttp: Removing redundant middleware next copy by @maxcelant in https://github.com/caddyserver/caddy/pull/7217
* build(deps): bump the all-updates group with 17 updates by @dependabot[bot] in https://github.com/caddyserver/caddy/pull/7236
* build(deps): bump the actions-deps group with 5 updates by @dependabot[bot] in https://github.com/caddyserver/caddy/pull/7237
* encode: fix response corruption when handle_errors is used by @Siomachkin in https://github.com/caddyserver/caddy/pull/7235
* Fix PKI creation when auto_https is disabled (#7211) by @Siomachkin in https://github.com/caddyserver/caddy/pull/7238
* logging: Buffer the logs before config is loaded by @francislavoie in https://github.com/caddyserver/caddy/pull/7245
* fileserver: set Content-Length for precompressed files by @WeidiDeng in https://github.com/caddyserver/caddy/pull/7251
* refactor: use WaitGroup.Go to simplify code by @mickychang9 in https://github.com/caddyserver/caddy/pull/7253
* caddyfile: Allow `block` to do nothing if nothing passed to `import` by @BeeJay28 in https://github.com/caddyserver/caddy/pull/7206
* logging: Adjustments to BufferedLog to keep logs in the correct order by @francislavoie in https://github.com/caddyserver/caddy/pull/7257
* caddyhttp: Prevent commas in header values from being split in CLI commands by @gilbsgilbs in https://github.com/caddyserver/caddy/pull/7268
* update quic-go to v0.54.1 by @marten-seemann in https://github.com/caddyserver/caddy/pull/7273
* chore: ugh, lint fix... by @mohammed90 in https://github.com/caddyserver/caddy/pull/7275
* caddypki: check intermediate lifetime to actual root cert lifetime by @u5surf in https://github.com/caddyserver/caddy/pull/7272
* refactor: omit unnecessary reassignment by @asttool in https://github.com/caddyserver/caddy/pull/7276
* core: use reflect.TypeFor to check for encoding/json.RawMessage by @WeidiDeng in https://github.com/caddyserver/caddy/pull/7274
* core: Reloading with `SIGUSR1` if config never changed via admin by @francislavoie in https://github.com/caddyserver/caddy/pull/7258
* build(deps): bump the actions-deps group with 8 updates by @dependabot[bot] in https://github.com/caddyserver/caddy/pull/7284
* httpcaddyfile: Add missing DNS challenge check for `acme_dns` by @rightaditya in https://github.com/caddyserver/caddy/pull/7270
* httpcaddyfile: Map default_bind to BindHost in globalACMEDefaults by @Monviech in https://github.com/caddyserver/caddy/pull/7278
* Argon2id Support for Basic Auth by @GreyXor in https://github.com/caddyserver/caddy/pull/7186
* update quic-go to v0.55.0 by @marten-seemann in https://github.com/caddyserver/caddy/pull/7288
* reverse_proxy: use http1 for outbound tls requests with placeholder t… by @WeidiDeng in https://github.com/caddyserver/caddy/pull/7296
* caddyhttp: Add server options `keepalive_idle` and `keepalive_count` by @joshuamcbeth in https://github.com/caddyserver/caddy/pull/7298
* chore: fix some comments by @wyrapeseed in https://github.com/caddyserver/caddy/pull/7303
* logging: Switch from `lumberjack` to `timberjack`, add time-rolling options by @aeris in https://github.com/caddyserver/caddy/pull/7244
* reverseproxy: Use http1.1 upgrade for websocket for extended connect of http2 and http3. by @tonyb486 in https://github.com/caddyserver/caddy/pull/7305
* caddyhttp: Add `trusted_proxies_unix` for trusting unix socket `X-Forwarded-*` headers by @cseufert in https://github.com/caddyserver/caddy/pull/7265
* caddyhttp: wrap accepted connection to suppress tls.ConnectionState by @WeidiDeng in https://github.com/caddyserver/caddy/pull/7247
* logging: fix multiple regexp filters on same field (fixes #7049) by @s2010 in https://github.com/caddyserver/caddy/pull/7061
* intercept: use already buffered response if possible when intercepting by @WeidiDeng in https://github.com/caddyserver/caddy/pull/7028
* listeners: Add support for named socket activation by @Siomachkin in https://github.com/caddyserver/caddy/pull/7243
* reverseproxy: do not disable keepalive if proxy protocol is used by @WeidiDeng in https://github.com/caddyserver/caddy/pull/7300
* metrics: resolve per-host inifinite cardinality by @mohammed90 in https://github.com/caddyserver/caddy/pull/7306
* reverseproxy: use http.Protocols to handle h2c requests by @WeidiDeng in https://github.com/caddyserver/caddy/pull/6990
* refactor: use reflect.TypeFor by @wyrapeseed in https://github.com/caddyserver/caddy/pull/7313
* build(deps): bump the all-updates group across 1 directory with 2 updates by @dependabot[bot] in https://github.com/caddyserver/caddy/pull/7307
* build(deps): bump github.com/slackhq/nebula from 1.9.5 to 1.9.7 by @dependabot[bot] in https://github.com/caddyserver/caddy/pull/7315
* feat: switch to autoexport for OpenTelemetry span exporter by @PKeidel in https://github.com/caddyserver/caddy/pull/7317
* reverse_proxy: set default values for keepalive if only some of them are set by @WeidiDeng in https://github.com/caddyserver/caddy/pull/7318
* fix quote within quotes  formatted incorrectly by fmt by @keystroke3 in https://github.com/caddyserver/caddy/pull/7045
* caddytls: correct documentation of `LeafFolderLoader` by @mohammed90 in https://github.com/caddyserver/caddy/pull/7327
* fix golangci-lint error G602 in caddyhttp by @cdenicola in https://github.com/caddyserver/caddy/pull/7334
* feat: allow customizing the Server header by @dunglas in https://github.com/caddyserver/caddy/pull/7338
* update quic-go to v0.56.0, enable qlog for HTTP/3 by @marten-seemann in https://github.com/caddyserver/caddy/pull/7345
* build(deps): bump the all-updates group with 4 updates by @dependabot[bot] in https://github.com/caddyserver/caddy/pull/7333
* feat: custom slog handlers for modules (log contextual data) by @dunglas in https://github.com/caddyserver/caddy/pull/7346
* ci: implement new release flow by @mohammed90 in https://github.com/caddyserver/caddy/pull/7341
* reverse_proxy: use interfaces to modify the behaviors of the transports by @WeidiDeng in https://github.com/caddyserver/caddy/pull/7353
* build(deps): bump golang.org/x/crypto from 0.43.0 to 0.45.0 by @dependabot[bot] in https://github.com/caddyserver/caddy/pull/7355
* update quic-go to v0.57.0 by @marten-seemann in https://github.com/caddyserver/caddy/pull/7359
* refactor: replace HasSuffix+TrimSuffix with CutSuffix by @ledigang in https://github.com/caddyserver/caddy/pull/7357
* Fix retries for requests with bodies by @chebyrash in https://github.com/caddyserver/caddy/pull/7360
* build(deps): bump the all-updates group with 3 updates by @dependabot[bot] in https://github.com/caddyserver/caddy/pull/7376
* ci: escape backticks in changelogs embedded in JS by @mohammed90 in https://github.com/caddyserver/caddy/pull/7382

## New Contributors
* @Qusic made their first contribution in https://github.com/caddyserver/caddy/pull/7181
* @arpansaha13 made their first contribution in https://github.com/caddyserver/caddy/pull/7215
* @aro-lew made their first contribution in https://github.com/caddyserver/caddy/pull/7214
* @maxcelant made their first contribution in https://github.com/caddyserver/caddy/pull/7217
* @Siomachkin made their first contribution in https://github.com/caddyserver/caddy/pull/7235
* @mickychang9 made their first contribution in https://github.com/caddyserver/caddy/pull/7253
* @asttool made their first contribution in https://github.com/caddyserver/caddy/pull/7276
* @rightaditya made their first contribution in https://github.com/caddyserver/caddy/pull/7270
* @Monviech made their first contribution in https://github.com/caddyserver/caddy/pull/7278
* @wyrapeseed made their first contribution in https://github.com/caddyserver/caddy/pull/7303
* @aeris made their first contribution in https://github.com/caddyserver/caddy/pull/7244
* @tonyb486 made their first contribution in https://github.com/caddyserver/caddy/pull/7305
* @cseufert made their first contribution in https://github.com/caddyserver/caddy/pull/7265
* @s2010 made their first contribution in https://github.com/caddyserver/caddy/pull/7061
* @PKeidel made their first contribution in https://github.com/caddyserver/caddy/pull/7317
* @cdenicola made their first contribution in https://github.com/caddyserver/caddy/pull/7334
* @ledigang made their first contribution in https://github.com/caddyserver/caddy/pull/7357
* @chebyrash made their first contribution in https://github.com/caddyserver/caddy/pull/7360

**Full Changelog**: https://github.com/caddyserver/caddy/compare/v2.10.2...v2.11.0-beta.1