# Nuclei - v3.6.0

**Release Name**: v3.6.0
**Published**: 2025-12-04T20:40:33Z
**Repository**: https://github.com/projectdiscovery/nuclei

---

# What's Changed

## ✨ New Features
- Write resume file specified by flag by @circleous ([#6616](https://github.com/projectdiscovery/nuclei/pull/6616))
- Javascript Multi-Port Support by @pussycat0x ([#6501](https://github.com/projectdiscovery/nuclei/pull/6501))
- Direct fuzzing using target URL for OpenAPI/Swagger by @roiswd ([#6542](https://github.com/projectdiscovery/nuclei/pull/6542))
- Bump DSL with .NET deserialization helpers by @Ice3man543 ([#6625](https://github.com/projectdiscovery/nuclei/pull/6625))
- Implement persistent metadata cache in loader by @dwisiswant0 ([#6630](https://github.com/projectdiscovery/nuclei/pull/6630))
- Check for undefined params for lazy evaluation in variables by @dwisiswant0 ([#6618](https://github.com/projectdiscovery/nuclei/pull/6618))

## 🐛 Fixed
- Configure `tmpDir` for SDK by @AuditeMarlow ([#6596](https://github.com/projectdiscovery/nuclei/pull/6596))
- Skip DNS lookups on Interactsh domains by @dwisiswant0 ([#6614](https://github.com/projectdiscovery/nuclei/pull/6614))
- Restore parallel processing in file protocol by @dwisiswant0 ([#6493](https://github.com/projectdiscovery/nuclei/pull/6493))

## ⚙️ Changed / Improvements
- Enable `BenchmarkRunEnumeration/Default` benchmark by @dwisiswant0 ([#6603](https://github.com/projectdiscovery/nuclei/pull/6603))
- Cache Go-rod browser in CI by @dwisiswant0 ([#6640](https://github.com/projectdiscovery/nuclei/pull/6640))
- Apply free-disk-space check on tests by @dwisiswant0 ([#6642](https://github.com/projectdiscovery/nuclei/pull/6642))
- Disable stale workflow for enhancements by @dogancanbakir ([#6637](https://github.com/projectdiscovery/nuclei/pull/6637))
- Omit unnecessary reassignment by @ledigang ([#6622](https://github.com/projectdiscovery/nuclei/pull/6622))

## 🧹 Maintenance / Dependencies
- Bump the modules group with 6 updates by @dependabot[bot] ([#6615](https://github.com/projectdiscovery/nuclei/pull/6615))
- Bump actions/checkout from 5 to 6 in workflows by @dependabot[bot] ([#6628](https://github.com/projectdiscovery/nuclei/pull/6628))
- Bump PD modules & update `httputil` calls by @dependabot[bot] ([#6629](https://github.com/projectdiscovery/nuclei/pull/6629))
- Bump the modules group with 11 updates by @dependabot[bot] ([#6646](https://github.com/projectdiscovery/nuclei/pull/6646))
- Bump golang.org/x/crypto from 0.43.0 to 0.45.0 by @dependabot[bot] ([#6621](https://github.com/projectdiscovery/nuclei/pull/6621))
- Bump github.com/projectdiscovery/fastdialer@v0.4.16 by @dwisiswant0 ([#6624](https://github.com/projectdiscovery/nuclei/pull/6624))

## 🌱 New Contributors
- @AuditeMarlow ([#6596](https://github.com/projectdiscovery/nuclei/pull/6596))
- @roiswd ([#6542](https://github.com/projectdiscovery/nuclei/pull/6542))
- @ledigang ([#6622](https://github.com/projectdiscovery/nuclei/pull/6622))

**Full Changelog:** [v3.5.1 → v3.6.0](https://github.com/projectdiscovery/nuclei/compare/v3.5.1...v3.6.0)
