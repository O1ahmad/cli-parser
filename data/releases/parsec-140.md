# Parsec - 1.4.0

**Release Name**: 1.4.0
**Published**: 2024-09-01T21:02:52Z
**Repository**: https://github.com/parallaxsecond/parsec

---

# Main features delivered

- TPM security fix
- New CI set up to track dependency mismatches
- Minor fixes

For a more comprehensive view of the release see the changelog below.

# Changelog
## [1.4.0](https://github.com/parallaxsecond/parsec/tree/1.4.0) (2024-03-28)

[Full Changelog](https://github.com/parallaxsecond/parsec/compare/1.4.0-rc2...1.4.0)

## [1.4.0-rc2](https://github.com/parallaxsecond/parsec/tree/1.4.0-rc2) (2024-03-28)

[Full Changelog](https://github.com/parallaxsecond/parsec/compare/1.4.0-rc1...1.4.0-rc2)

**Merged pull requests:**

- tpm/tests: Ignore test\_root\_key\_check case [\#755](https://github.com/parallaxsecond/parsec/pull/755) ([tgonzalezorlandoarm](https://github.com/tgonzalezorlandoarm))

## [1.4.0-rc1](https://github.com/parallaxsecond/parsec/tree/1.4.0-rc1) (2024-03-18)

[Full Changelog](https://github.com/parallaxsecond/parsec/compare/1.3.0...1.4.0-rc1)

**Implemented enhancements:**

- Set up build to track dependency mismatches [\#360](https://github.com/parallaxsecond/parsec/issues/360)

**Fixed bugs:**

- e2e\_tests/stress.rs: Add a workaround for spurious test failures [\#739](https://github.com/parallaxsecond/parsec/pull/739) ([tgonzalezorlandoarm](https://github.com/tgonzalezorlandoarm))

**Security fixes:**

- TPM Provider: Check root key's name [\#751](https://github.com/parallaxsecond/parsec/pull/751) ([tgonzalezorlandoarm](https://github.com/tgonzalezorlandoarm))

**Closed issues:**

- parsec-cli-tests.sh error: The CSR does not contain the serialNumber field of the Distinguished Name [\#742](https://github.com/parallaxsecond/parsec/issues/742)
- Migrate away from using users crate [\#678](https://github.com/parallaxsecond/parsec/issues/678)
- Parsec Quickstart - Docker: Pull access denied for parallaxsecond/parsec-quickstart, repository does not exist [\#666](https://github.com/parallaxsecond/parsec/issues/666)
- Vulnerability in SQLite [\#648](https://github.com/parallaxsecond/parsec/issues/648)

**Merged pull requests:**

- dependency\_cross\_matcher: Fix typo \(missing comma\) [\#754](https://github.com/parallaxsecond/parsec/pull/754) ([tgonzalezorlandoarm](https://github.com/tgonzalezorlandoarm))
- structopt: Migrate to clap [\#753](https://github.com/parallaxsecond/parsec/pull/753) ([tgonzalezorlandoarm](https://github.com/tgonzalezorlandoarm))
- Cargo.toml: Bump tss-esapi to 7.5.0 [\#750](https://github.com/parallaxsecond/parsec/pull/750) ([tgonzalezorlandoarm](https://github.com/tgonzalezorlandoarm))
- nightly/audit: Temporary ignore RUSTSEC-2024-0006 [\#748](https://github.com/parallaxsecond/parsec/pull/748) ([tgonzalezorlandoarm](https://github.com/tgonzalezorlandoarm))
- Use infallible conversion into instead of try\_into [\#747](https://github.com/parallaxsecond/parsec/pull/747) ([gowthamsk-arm](https://github.com/gowthamsk-arm))
- .cargo/config.toml: remove [\#746](https://github.com/parallaxsecond/parsec/pull/746) ([billatarm](https://github.com/billatarm))
- Dependency mismatcher Comparison option [\#745](https://github.com/parallaxsecond/parsec/pull/745) ([tgonzalezorlandoarm](https://github.com/tgonzalezorlandoarm))
- dependency\_cross\_matcher job: Move to PR runs and minor refactoring [\#743](https://github.com/parallaxsecond/parsec/pull/743) ([tgonzalezorlandoarm](https://github.com/tgonzalezorlandoarm))
- Cargo.lock: Update rustix and bitflags dependencies to latest version [\#741](https://github.com/parallaxsecond/parsec/pull/741) ([tgonzalezorlandoarm](https://github.com/tgonzalezorlandoarm))
- cargo-check: Run with both stable and MSRV Compilers [\#737](https://github.com/parallaxsecond/parsec/pull/737) ([tgonzalezorlandoarm](https://github.com/tgonzalezorlandoarm))
- ci.yml: Trigger docker image creation only on workflow\_dispatch [\#736](https://github.com/parallaxsecond/parsec/pull/736) ([tgonzalezorlandoarm](https://github.com/tgonzalezorlandoarm))
- ci.yml,deny.toml: Setup license testing [\#735](https://github.com/parallaxsecond/parsec/pull/735) ([tgonzalezorlandoarm](https://github.com/tgonzalezorlandoarm))
- Cargo.toml: Specify rust-version=1.66.0 [\#733](https://github.com/parallaxsecond/parsec/pull/733) ([tgonzalezorlandoarm](https://github.com/tgonzalezorlandoarm))
- Track and test dependencies' 'next' branch [\#732](https://github.com/parallaxsecond/parsec/pull/732) ([tgonzalezorlandoarm](https://github.com/tgonzalezorlandoarm))
- Add dependency cross matching [\#731](https://github.com/parallaxsecond/parsec/pull/731) ([tgonzalezorlandoarm](https://github.com/tgonzalezorlandoarm))
- e2e\_tests/mangled\_ping: Fix socket path [\#728](https://github.com/parallaxsecond/parsec/pull/728) ([tgonzalezorlandoarm](https://github.com/tgonzalezorlandoarm))
- ci/coverage: Fix cargo-tarpaulin to its locked version [\#727](https://github.com/parallaxsecond/parsec/pull/727) ([tgonzalezorlandoarm](https://github.com/tgonzalezorlandoarm))