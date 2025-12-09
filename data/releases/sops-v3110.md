# SOPS - v3.11.0

**Release Name**: v3.11.0
**Published**: 2025-09-28T18:28:49Z
**Repository**: https://github.com/getsops/sops

---

## Installation

To install `sops`, download one of the pre-built binaries provided for your platform from the artifacts attached to this release.

For instance, if you are using Linux on an AMD64 architecture:

```shell
# Download the binary
curl -LO https://github.com/getsops/sops/releases/download/v3.11.0/sops-v3.11.0.linux.amd64

# Move the binary in to your PATH
mv sops-v3.11.0.linux.amd64 /usr/local/bin/sops

# Make the binary executable
chmod +x /usr/local/bin/sops
```

### Verify checksums file signature

The checksums file provided within the artifacts attached to this release is signed using [Cosign](https://docs.sigstore.dev/cosign/overview/) with GitHub OIDC. To validate the signature of this file, run the following commands:

```shell
# Download the checksums file, certificate and signature
curl -LO https://github.com/getsops/sops/releases/download/v3.11.0/sops-v3.11.0.checksums.txt
curl -LO https://github.com/getsops/sops/releases/download/v3.11.0/sops-v3.11.0.checksums.pem
curl -LO https://github.com/getsops/sops/releases/download/v3.11.0/sops-v3.11.0.checksums.sig

# Verify the checksums file
cosign verify-blob sops-v3.11.0.checksums.txt \
  --certificate sops-v3.11.0.checksums.pem \
  --signature sops-v3.11.0.checksums.sig \
  --certificate-identity-regexp=https://github.com/getsops \
  --certificate-oidc-issuer=https://token.actions.githubusercontent.com
```

### Verify binary integrity

To verify the integrity of the downloaded binary, you can utilize the checksums file after having validated its signature:

```shell
# Verify the binary using the checksums file
sha256sum -c sops-v3.11.0.checksums.txt --ignore-missing
```

### Verify artifact provenance

The [SLSA provenance](https://slsa.dev/provenance/v0.2) of the binaries, packages, and SBOMs can be found within the artifacts associated with this release. It is presented through an [in-toto](https://in-toto.io/) link metadata file named `sops-v3.11.0.intoto.jsonl`. To verify the provenance of an artifact, you can utilize the [`slsa-verifier`](https://github.com/slsa-framework/slsa-verifier#artifacts) tool:

```shell
# Download the metadata file
curl -LO  https://github.com/getsops/sops/releases/download/v3.11.0/sops-v3.11.0.intoto.jsonl

# Verify the provenance of the artifact
slsa-verifier verify-artifact <artifact> \
  --provenance-path sops-v3.11.0.intoto.jsonl \
  --source-uri github.com/getsops/sops \
  --source-tag v3.11.0
```

## Container Images

The `sops` binaries are also available as container images, based on Debian (slim) and Alpine Linux. The Debian-based container images include any dependencies which may be required to make use of certain key services, such as GnuPG, AWS KMS, Azure Key Vault, and Google Cloud KMS. The Alpine-based container images are smaller in size, but do not include these dependencies.

These container images are available for the following architectures: `linux/amd64` and `linux/arm64`.

### GitHub Container Registry

- `ghcr.io/getsops/sops:v3.11.0`
- `ghcr.io/getsops/sops:v3.11.0-alpine`

### Quay.io

- `quay.io/getsops/sops:v3.11.0`
- `quay.io/getsops/sops:v3.11.0-alpine`

### Verify container image signature

The container images are signed using [Cosign](https://docs.sigstore.dev/cosign/overview/) with GitHub OIDC. To validate the signature of an image, run the following command:

```shell
cosign verify ghcr.io/getsops/sops:v3.11.0 \
  --certificate-identity-regexp=https://github.com/getsops \
  --certificate-oidc-issuer=https://token.actions.githubusercontent.com \
  -o text
```

### Verify container image provenance

The container images include [SLSA provenance](https://slsa.dev/provenance/v0.2) attestations. For more information around the verification of this, please refer to the [`slsa-verifier` documentation](https://github.com/slsa-framework/slsa-verifier#containers).

## Software Bill of Materials

The Software Bill of Materials (SBOM) for each binary is accessible within the artifacts enclosed with this release. It is presented as an [SPDX](https://spdx.dev/) JSON file, formatted as `<binary>.spdx.sbom.json`.

## What's Changed
* build(deps): Bump the go group with 4 updates by @dependabot[bot] in https://github.com/getsops/sops/pull/1845
* build(deps): Bump the go group with 5 updates by @dependabot[bot] in https://github.com/getsops/sops/pull/1850
* build(deps): Bump the ci group with 4 updates by @dependabot[bot] in https://github.com/getsops/sops/pull/1849
* build(deps): Bump the go group with 8 updates by @dependabot[bot] in https://github.com/getsops/sops/pull/1854
* build(deps): Bump tempfile from 3.19.1 to 3.20.0 in /functional-tests in the rust group by @dependabot[bot] in https://github.com/getsops/sops/pull/1853
* build(deps): Bump actions/setup-go from 5.4.0 to 5.5.0 in the ci group by @dependabot[bot] in https://github.com/getsops/sops/pull/1852
* use bullet points for structure by @md42 in https://github.com/getsops/sops/pull/1844
* Introduce EncryptContext and DecryptContext for AWS, Azure, GCP, PGP and HashiCorp Vault by @matheuscscp in https://github.com/getsops/sops/pull/1848
* build(deps): Bump the go group with 5 updates by @dependabot[bot] in https://github.com/getsops/sops/pull/1856
* build(deps): Bump the ci group with 2 updates by @dependabot[bot] in https://github.com/getsops/sops/pull/1857
* Allow injecting custom HTTP client for AWS, Azure, GCP and HashiCorp Vault by @matheuscscp in https://github.com/getsops/sops/pull/1838
* Update authors in main.go by @jvehent in https://github.com/getsops/sops/pull/1860
* build(deps): Bump the go group with 7 updates by @dependabot[bot] in https://github.com/getsops/sops/pull/1861
* Remove unmatched '`' from README.rst by @wasv in https://github.com/getsops/sops/pull/1863
* build(deps): Bump the go group with 4 updates by @dependabot[bot] in https://github.com/getsops/sops/pull/1867
* build(deps): Bump alpine from 3.21 to 3.22 in /.release in the docker group by @dependabot[bot] in https://github.com/getsops/sops/pull/1866
* build(deps): Bump the go group with 12 updates by @dependabot[bot] in https://github.com/getsops/sops/pull/1870
* build(deps): Bump github/codeql-action from 3.28.18 to 3.28.19 in the ci group by @dependabot[bot] in https://github.com/getsops/sops/pull/1869
* build(deps): Bump github.com/cloudflare/circl from 1.6.0 to 1.6.1 by @dependabot[bot] in https://github.com/getsops/sops/pull/1871
* build(deps): Bump the go group with 12 updates by @dependabot[bot] in https://github.com/getsops/sops/pull/1872
* build(deps): Bump the ci group across 1 directory with 3 updates by @dependabot[bot] in https://github.com/getsops/sops/pull/1874
* build(deps): Bump the go group with 8 updates by @dependabot[bot] in https://github.com/getsops/sops/pull/1878
* build(deps): Bump the ci group with 2 updates by @dependabot[bot] in https://github.com/getsops/sops/pull/1879
* build(deps): Bump github.com/go-viper/mapstructure/v2 from 2.2.1 to 2.3.0 by @dependabot[bot] in https://github.com/getsops/sops/pull/1882
* Fix Typo in README.rst by @inverted-tree in https://github.com/getsops/sops/pull/1881
* build(deps): Bump the go group with 4 updates by @dependabot[bot] in https://github.com/getsops/sops/pull/1884
* build(deps): Bump the ci group with 2 updates by @dependabot[bot] in https://github.com/getsops/sops/pull/1883
* Correct Windows path to store keys.txt by @EshemMimi in https://github.com/getsops/sops/pull/1885
* build(deps): Bump the go group with 3 updates by @dependabot[bot] in https://github.com/getsops/sops/pull/1888
* build(deps): Bump the ci group with 2 updates by @dependabot[bot] in https://github.com/getsops/sops/pull/1889
* build(deps): Bump the go group with 6 updates by @dependabot[bot] in https://github.com/getsops/sops/pull/1893
* Add "--value-file" option to "sops set [...]" by @bjornfor in https://github.com/getsops/sops/pull/1876
* Document XDG_CONFIG_HOME support on mac by @fredericrous in https://github.com/getsops/sops/pull/1897
* Fix Shamir threshold encoding for INI and ENV files by @felixfontein in https://github.com/getsops/sops/pull/1899
* build(deps): Bump the go group with 12 updates by @dependabot[bot] in https://github.com/getsops/sops/pull/1908
* build(deps): Bump serde_json from 1.0.140 to 1.0.142 in /functional-tests in the rust group by @dependabot[bot] in https://github.com/getsops/sops/pull/1907
* build(deps): Bump the ci group with 3 updates by @dependabot[bot] in https://github.com/getsops/sops/pull/1905
* Fix docs: mention all stores instead of just YAML, JSON, and BINARY by @felixfontein in https://github.com/getsops/sops/pull/1895
* Ensure temporary file for editing is only read-writable by owner by @felixfontein in https://github.com/getsops/sops/pull/1903
* Add `--value-stdin` option to `sops set` by @felixfontein in https://github.com/getsops/sops/pull/1894
* Collect age identity loading errors and only report if decryption failed by @felixfontein in https://github.com/getsops/sops/pull/1898
* add completion script. Resolves #1868 by @longxiucai in https://github.com/getsops/sops/pull/1892
* Resolves #1864. Adds Native List as an option for configuring keys.  by @lucqui in https://github.com/getsops/sops/pull/1880
* Fix example.yaml file by @felixfontein in https://github.com/getsops/sops/pull/1909
* build(deps): Bump the go group with 15 updates by @dependabot[bot] in https://github.com/getsops/sops/pull/1912
* build(deps): Bump the ci group with 4 updates by @dependabot[bot] in https://github.com/getsops/sops/pull/1911
* build(deps): Bump the go group with 9 updates by @dependabot[bot] in https://github.com/getsops/sops/pull/1917
* build(deps): Bump the ci group with 4 updates by @dependabot[bot] in https://github.com/getsops/sops/pull/1916
* build(deps): Bump github.com/go-viper/mapstructure/v2 from 2.3.0 to 2.4.0 by @dependabot[bot] in https://github.com/getsops/sops/pull/1920
* build(deps): Bump the go group with 14 updates by @dependabot[bot] in https://github.com/getsops/sops/pull/1923
* build(deps): Bump the rust group in /functional-tests with 2 updates by @dependabot[bot] in https://github.com/getsops/sops/pull/1921
* build(deps): Bump github/codeql-action from 3.29.9 to 3.29.11 in the ci group by @dependabot[bot] in https://github.com/getsops/sops/pull/1922
* Docs: remove paragraph on GPG/PGP keyservers by @felixfontein in https://github.com/getsops/sops/pull/1928
* Allow to configure --enable-local-keyservice and --keyservice through env variables by @felixfontein in https://github.com/getsops/sops/pull/1930
* build(deps): Bump the ci group with 2 updates by @dependabot[bot] in https://github.com/getsops/sops/pull/1937
* fix: correct destination validation logic to detect all conflicts by @bruce-szalwinski-he in https://github.com/getsops/sops/pull/1936
* Switch from deprecated gopkg.in/yaml.v3 to go.yaml.in/yaml/v3 by @sylr in https://github.com/getsops/sops/pull/1934
* INI: fix converting integers to strings; improve float and time.Time formatting by @felixfontein in https://github.com/getsops/sops/pull/1929
* feat(azkv): Skipping key-version will get latest key by @daogilvie in https://github.com/getsops/sops/pull/1919
* Fix keyservice client for unix domain sockets by @matheuscscp in https://github.com/getsops/sops/pull/1910
* README: fix argument order by @felixfontein in https://github.com/getsops/sops/pull/1940
* Allow non-complex non-string values in dotenv and exec-env by @billy4479 in https://github.com/getsops/sops/pull/1933
* Fix mention of macOS XDG_CONFIG_HOME fallback by @felixfontein in https://github.com/getsops/sops/pull/1944
* Improve age identity loading by @felixfontein in https://github.com/getsops/sops/pull/1931
* build(deps): Bump the rust group in /functional-tests with 4 updates by @dependabot[bot] in https://github.com/getsops/sops/pull/1948
* build(deps): Bump the ci group with 2 updates by @dependabot[bot] in https://github.com/getsops/sops/pull/1949
* build(deps): Bump the rust group in /functional-tests with 2 updates by @dependabot[bot] in https://github.com/getsops/sops/pull/1954
* build(deps): Bump anchore/sbom-action from 0.20.5 to 0.20.6 in the ci group by @dependabot[bot] in https://github.com/getsops/sops/pull/1955
* Start documenting the configuration file format by @felixfontein in https://github.com/getsops/sops/pull/1946
* CI: Build with Go 1.24 and 1.25, release with 1.25 by @felixfontein in https://github.com/getsops/sops/pull/1945
* build(deps): Bump the go group across 1 directory with 21 updates by @dependabot[bot] in https://github.com/getsops/sops/pull/1956
* When encrypting, load the config only once by @felixfontein in https://github.com/getsops/sops/pull/1939
* build(deps): Bump the go group across 1 directory with 10 updates by @dependabot[bot] in https://github.com/getsops/sops/pull/1958
* Ignore encryption selection options for binary store (and warn when they are used) by @felixfontein in https://github.com/getsops/sops/pull/1927
* AZKV: Also allow to omit version for AZKV keys specified in key groups by @felixfontein in https://github.com/getsops/sops/pull/1947
* Complex values in dotenv, and exec-env: do not print sensitive value in error message by @felixfontein in https://github.com/getsops/sops/pull/1959
* Release 3.11.0 by @felixfontein in https://github.com/getsops/sops/pull/1960

## New Contributors
* @md42 made their first contribution in https://github.com/getsops/sops/pull/1844
* @wasv made their first contribution in https://github.com/getsops/sops/pull/1863
* @inverted-tree made their first contribution in https://github.com/getsops/sops/pull/1881
* @EshemMimi made their first contribution in https://github.com/getsops/sops/pull/1885
* @bjornfor made their first contribution in https://github.com/getsops/sops/pull/1876
* @fredericrous made their first contribution in https://github.com/getsops/sops/pull/1897
* @longxiucai made their first contribution in https://github.com/getsops/sops/pull/1892
* @lucqui made their first contribution in https://github.com/getsops/sops/pull/1880
* @bruce-szalwinski-he made their first contribution in https://github.com/getsops/sops/pull/1936
* @sylr made their first contribution in https://github.com/getsops/sops/pull/1934
* @daogilvie made their first contribution in https://github.com/getsops/sops/pull/1919
* @billy4479 made their first contribution in https://github.com/getsops/sops/pull/1933

**Full Changelog**: https://github.com/getsops/sops/compare/v3.10.2...v3.11.0

