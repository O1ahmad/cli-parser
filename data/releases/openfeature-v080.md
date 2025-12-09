# OpenFeature - v0.8.0

**Release Name**: v0.8.0
**Published**: 2024-03-11T16:11:41Z
**Repository**: https://github.com/open-feature/spec

---

## What's Changed

This spec release contains some minor enhancements for `dynamic-context` (server) SDK implementations, and significant changes and enhancements for `static-context` (client) SDK implementations. It also contains the first draft of the OFREP (OpenFeature Remote Evaluation Protocol).

* feat: internal provider state, new client events by @toddbaert in https://github.com/open-feature/spec/pull/241
* feat: emit events on context change (client-only) by @Billlynch in https://github.com/open-feature/spec/pull/200
* feat: introduce OFREP to appendix section by @Kavindu-Dodan in https://github.com/open-feature/spec/pull/246
* feat: NOT_READY after provider shutdown by @toddbaert in https://github.com/open-feature/spec/pull/216
* feat: add domain as an openfeature concept by @beeme1mr in https://github.com/open-feature/spec/pull/229
* feat: context propagation by @lukas-reining in https://github.com/open-feature/spec/pull/227

* fix: broken link, outdated link by @toddbaert in https://github.com/open-feature/spec/pull/208
* fix: add stale state to provider state diagram by @federicobond in https://github.com/open-feature/spec/pull/212
* fix: correct `event details` type, include `provider name` by @toddbaert in https://github.com/open-feature/spec/pull/210
* fix: add dynamic-context condition to 4.1.4 by @toddbaert in https://github.com/open-feature/spec/pull/217
* fix: invalid links detected by Docusaurus by @beeme1mr in https://github.com/open-feature/spec/pull/222
* fix: language-neutral verbiage for set-and-wait by @toddbaert in https://github.com/open-feature/spec/pull/242
* fix: minor corrections around FATAL state by @toddbaert in https://github.com/open-feature/spec/pull/247
* fix: add missing Provider Event Details 'error code' field by @federicobond in https://github.com/open-feature/spec/pull/249
* fix: Include hook hints in evaluation options type. by @kinyoklion in https://github.com/open-feature/spec/pull/250

* chore: clarify eval details funcs/structs by @toddbaert in https://github.com/open-feature/spec/pull/209
* chore: move 1.1.8 content to 1.1.2.4 by @toddbaert in https://github.com/open-feature/spec/pull/225
* chore: add repo stats by @toddbaert in https://github.com/open-feature/spec/pull/226
* chore: improve Renovate config by @beeme1mr in https://github.com/open-feature/spec/pull/231
* chore: Clarify resolution detail reason. by @kinyoklion in https://github.com/open-feature/spec/pull/239
* chore: clarify event/domain scoping, lifecycle by @toddbaert in https://github.com/open-feature/spec/pull/248

* docs: add language-specific initialize naming by @maxveldink in https://github.com/open-feature/spec/pull/244
* docs: improve spec readme by @beeme1mr in https://github.com/open-feature/spec/pull/232

## New Contributors
* @federicobond made their first contribution in https://github.com/open-feature/spec/pull/212
* @Billlynch made their first contribution in https://github.com/open-feature/spec/pull/200
* @lukas-reining made their first contribution in https://github.com/open-feature/spec/pull/227
* @maxveldink made their first contribution in https://github.com/open-feature/spec/pull/244

**Full Changelog**: https://github.com/open-feature/spec/compare/v0.7.0...v0.8.0