# external-secrets - v1.1.1

**Release Name**: v1.1.1
**Published**: 2025-12-05T12:13:20Z
**Repository**: https://github.com/external-secrets/external-secrets

---

Image: `ghcr.io/external-secrets/external-secrets:v1.1.1`
Image: `ghcr.io/external-secrets/external-secrets:v1.1.1-ubi`
Image: `ghcr.io/external-secrets/external-secrets:v1.1.1-ubi-boringssl`


<!-- Release notes generated using configuration in .github/release.yml at main -->

## What's Changed
### General
* chore(chart): release helm chart 1.1.0 by @Skarlso in https://github.com/external-secrets/external-secrets/pull/5619
* docs: improve spec.md by exporting generator types by @gusfcarvalho in https://github.com/external-secrets/external-secrets/pull/5624
* chore(deps): remove sprig fork by @Skarlso in https://github.com/external-secrets/external-secrets/pull/5626
* fix: report 404 secrets correctly in Gitlab provider by @alekc in https://github.com/external-secrets/external-secrets/pull/5104
* docs(secretserver): update documentation to include Platform compatibility by @DelineaSahilWankhede in https://github.com/external-secrets/external-secrets/pull/5546
* docs: add llm policy by @Skarlso in https://github.com/external-secrets/external-secrets/pull/5649
* fix: pass in the token to the build and publish container by @Skarlso in https://github.com/external-secrets/external-secrets/pull/5651
* test(secretserver): improve test coverage for SecretServer provider by @DelineaSahilWankhede in https://github.com/external-secrets/external-secrets/pull/5641
* fix: docs pipeline by @rkferreira in https://github.com/external-secrets/external-secrets/pull/5663
* fix: modify the url of the remote to include the token by @Skarlso in https://github.com/external-secrets/external-secrets/pull/5664
* feat(helm): add dynamic labelSelector if not define in topologySpread… by @fe80 in https://github.com/external-secrets/external-secrets/pull/5065
* feat: Support retry settings for Doppler provider by @maduonline in https://github.com/external-secrets/external-secrets/pull/5608
* feat(beyondtrust): enable pushing secrets in BeyondTrust provider by @btfhernandez in https://github.com/external-secrets/external-secrets/pull/5586
* fix: correctly merge map fields during templating by @Skarlso in https://github.com/external-secrets/external-secrets/pull/5671
* fix: use patch instead of update for finalizers addition and removal by @Skarlso in https://github.com/external-secrets/external-secrets/pull/5670
* feat(oracle): implement SecretExists by @anders-swanson in https://github.com/external-secrets/external-secrets/pull/5672
* fix(security): create provider for webhook & fake by @ShimonDarshan in https://github.com/external-secrets/external-secrets/pull/5628
* fix: set client transport to use GitHub Enterprise URL by @fred-gagnon in https://github.com/external-secrets/external-secrets/pull/5662
* feat(generator): Password generator can generate and expose multiple passwords by @Trojanekkk in https://github.com/external-secrets/external-secrets/pull/5669
* fix: run check diff on main by @Skarlso in https://github.com/external-secrets/external-secrets/pull/5681
* feat: `bitwardenServerSDKURL` is required for `bitwardensecretsmanager` by @budimanjojo in https://github.com/external-secrets/external-secrets/pull/5679
* fix: update the refreshInterval formatting _everywhere_ by @Skarlso in https://github.com/external-secrets/external-secrets/pull/5680
* clean: Update conjur-api-go; Disable credential storage by @szh in https://github.com/external-secrets/external-secrets/pull/5648
* fix: add live-reload to make docs.serve by @gusfcarvalho in https://github.com/external-secrets/external-secrets/pull/5676
* fix: remove cached artifacts after build by @gusfcarvalho in https://github.com/external-secrets/external-secrets/pull/5686
* fix(keepersecurity): properly handle fields key by @pepordev in https://github.com/external-secrets/external-secrets/pull/5674
### Dependencies
* chore(deps): bump golang from `d3f0cf7` to `d3f0cf7` by @dependabot[bot] in https://github.com/external-secrets/external-secrets/pull/5630
* chore(deps): bump golang from `7419f54` to `e174196` in /e2e by @dependabot[bot] in https://github.com/external-secrets/external-secrets/pull/5638
* chore(deps): bump zizmorcore/zizmor-action from 0.2.0 to 0.3.0 by @dependabot[bot] in https://github.com/external-secrets/external-secrets/pull/5637
* chore(deps): bump actions/setup-go from 6.0.0 to 6.1.0 by @dependabot[bot] in https://github.com/external-secrets/external-secrets/pull/5636
* chore(deps): bump anchore/sbom-action from 0.20.9 to 0.20.10 by @dependabot[bot] in https://github.com/external-secrets/external-secrets/pull/5635
* chore(deps): bump actions/create-github-app-token from 2.1.4 to 2.2.0 by @dependabot[bot] in https://github.com/external-secrets/external-secrets/pull/5634
* chore(deps): bump github/codeql-action from 4.31.3 to 4.31.4 by @dependabot[bot] in https://github.com/external-secrets/external-secrets/pull/5633
* chore(deps): bump aws-actions/configure-aws-credentials from f2964c7281262753f549b15ae39f1cbbb033b9e4 to 4a54c24244cf4f82abd7d44e7b2024258a8aa041 by @dependabot[bot] in https://github.com/external-secrets/external-secrets/pull/5632
* chore(deps): bump actions/checkout from 5.0.0 to 6.0.0 by @dependabot[bot] in https://github.com/external-secrets/external-secrets/pull/5631
* chore(deps): bump pymdown-extensions from 10.17.1 to 10.17.2 in /hack/api-docs by @dependabot[bot] in https://github.com/external-secrets/external-secrets/pull/5660
* chore(deps): bump softprops/action-gh-release from 2.4.2 to 2.5.0 by @dependabot[bot] in https://github.com/external-secrets/external-secrets/pull/5656
* chore(deps): bump actions/setup-python from 6.0.0 to 6.1.0 by @dependabot[bot] in https://github.com/external-secrets/external-secrets/pull/5657
* chore(deps): bump peter-evans/slash-command-dispatch from 4.0.0 to 5.0.0 by @dependabot[bot] in https://github.com/external-secrets/external-secrets/pull/5658
* chore(deps): bump hashicorp/setup-terraform from 4c5fdabea201636fa7ea13d8babd1ed828687f5d to 712b43959e9be7e82c34d18450fa5ec3237af3f1 by @dependabot[bot] in https://github.com/external-secrets/external-secrets/pull/5659

## New Contributors
* @fe80 made their first contribution in https://github.com/external-secrets/external-secrets/pull/5065
* @maduonline made their first contribution in https://github.com/external-secrets/external-secrets/pull/5608
* @fred-gagnon made their first contribution in https://github.com/external-secrets/external-secrets/pull/5662
* @Trojanekkk made their first contribution in https://github.com/external-secrets/external-secrets/pull/5669
* @budimanjojo made their first contribution in https://github.com/external-secrets/external-secrets/pull/5679

**Full Changelog**: https://github.com/external-secrets/external-secrets/compare/v1.1.0...v1.1.1