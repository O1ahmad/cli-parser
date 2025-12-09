# KubeStellar - v0.29.0

**Release Name**: v0.29.0
**Published**: 2025-11-06T22:10:15Z
**Repository**: https://github.com/kubestellar/kubestellar

---

## What's Changed since 0.28.0

* 📖 Update documentation for Kubernetes cluster setup by @Arpit529Srivastava in https://github.com/kubestellar/kubestellar/pull/2982
* 📖  Improve website doc wrt autogen, dual view by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/2983
* 🐛bug: fix controller-runtime logging warnings in transport unit tests by @antedotee in https://github.com/kubestellar/kubestellar/pull/2984
* 🌱 other/misc: add log for better understanding of docker context error! by @Rupam-It in https://github.com/kubestellar/kubestellar/pull/2974
* ✨ Fix GitHub Actions script injection vulnerabilities to resolve CLOMonitor security failures by @antedotee in https://github.com/kubestellar/kubestellar/pull/2998
* 🐛Fix race condition where PRs merge before all tests complete by @antedotee in https://github.com/kubestellar/kubestellar/pull/2986
* ✨  Add GitHub workflow that checks action hashes by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/2987
* ✨  Improve action hash script and bump two actions by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/2988
* ✨ restricted permissions for GITHUB_TOKEN to minimum permissions to prevent security risks by @antedotee in https://github.com/kubestellar/kubestellar/pull/3005
* ✨  Bump azure/setup-kubectl from 4.0.0 to 4.0.1 by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3014
* 🐛 fix: avoid panic in type conversion by @rishi-jat in https://github.com/kubestellar/kubestellar/pull/3007
* 🌱  Bump rojopolis/spellcheck-github-actions from 0.50.0 to 0.51.0 by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3015
* ✨Token permission security fix for CLOMonitor and openssf by @antedotee in https://github.com/kubestellar/kubestellar/pull/3010
* ✨  Various improvements mainly wrt GitHub Actions workflows by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3016
* 📖  improve user guide and add observability page  by @rishi-jat in https://github.com/kubestellar/kubestellar/pull/2992
* 🌱  Don't test on issue template or other workflow changes by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3039
* 📖  Update the PR and Issue templates by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3038
* ✨ Document histogram bucket boundaries in Grafana panels by @antedotee in https://github.com/kubestellar/kubestellar/pull/2996
* 🐛  Add quoting in .github/ISSUE_TEMPLATE/feature_request.yaml by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3041
* 🐛  Fix syntax for path exclusion by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3043
* 📖  Note branch name restriction and fork repair by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3050
* ✨feat: add docs preview enforcement workflow and PR template  by @rishi-jat in https://github.com/kubestellar/kubestellar/pull/3006
* 📖  Move docs/README.md content into website area by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3055
* 📖  An example of concurrent work by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3060
* 📖 docs: define env vars earlier in Getting Started guide (fixes #2646) by @rishi-jat in https://github.com/kubestellar/kubestellar/pull/3059
* 📖  Move CONTRIBUTING content into contributing-inc by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3054
* 📖 add smooth transitions for elements and theme toggle button by @Arpit529Srivastava in https://github.com/kubestellar/kubestellar/pull/3062
* 🌱kubeflex version updated by @Rupam-It in https://github.com/kubestellar/kubestellar/pull/3064
* 📖 clarify CSR wait instructions in Getting Started guide by @rishi-jat in https://github.com/kubestellar/kubestellar/pull/3053
* 🌱  Bump anchore/sbom-action/download-syft to 0.20.2, generalize yq version check by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3089
* 🐛 Split ambiguous cr-validation test into two focused cases by @rishi-jat in https://github.com/kubestellar/kubestellar/pull/3091
* 🌱  Add diagnostic to PR title failure by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3099
* ✨️ split WDS PCH into two parts by @Rupam-It in https://github.com/kubestellar/kubestellar/pull/3031
* 📖 Fix the broken link for Galaxy repository in galaxy.md file by @greninja517 in https://github.com/kubestellar/kubestellar/pull/3102
* 🌱  Bump com/actions/first-interaction to version 2.0.0 by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3097
* 🌱  Remove duplicate workflow by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3100
* 🌱  Rename and tweak PR title checking workflow by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3103
* 🐛 Fix the Warning message from kubeflex to display actual kubeflex version by @greninja517 in https://github.com/kubestellar/kubestellar/pull/3107
* 🌱using kubectl wait for cp to be ready in import-cp-context.sh file by @Rupam-It in https://github.com/kubestellar/kubestellar/pull/3082
* 📖 revise WEC registration based on feedback from #2997  by @rishi-jat in https://github.com/kubestellar/kubestellar/pull/3051
* 📖  Cross-link the two readmes by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3120
* 📖 CNCF Slack Update: Update all Slack URLs to point to new CNCF Slack Channel across the repo and docs by @greninja517 in https://github.com/kubestellar/kubestellar/pull/3127
* 📖 finalize observability page with protocol and port clarifications by @rishi-jat in https://github.com/kubestellar/kubestellar/pull/3057
* 🐛 remove variable double definition in WDS CP (fixes #3124) by @flushthemoney in https://github.com/kubestellar/kubestellar/pull/3126
* 🌱more refined logic for kind cluster creation with ssl-passthrough by @Rupam-It in https://github.com/kubestellar/kubestellar/pull/3080
* 📖  Add the Contributor Ladder to website by @KPRoche in https://github.com/kubestellar/kubestellar/pull/3123
* 📖 improve WDS page based on feedback from #3023 by @Tob-iee in https://github.com/kubestellar/kubestellar/pull/3092
* 🌱refine logic to make sure k3s service start and nginx ingress controler pod to be created  by @Rupam-It in https://github.com/kubestellar/kubestellar/pull/3084
* 📖  Fix up WDS doc page by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3128
* 🌱clean kubectl command in ocm-local-up-for-ingress.sh file by @Rupam-It in https://github.com/kubestellar/kubestellar/pull/3083
* ✨ Bump golang.org/x/oauth2 from 0.23.0 to 0.27.0 by @dependabot[bot] in https://github.com/kubestellar/kubestellar/pull/3096
* 🌱migrate complex bash script to init container in argocd setup file by @Rupam-It in https://github.com/kubestellar/kubestellar/pull/3105
* 📖  Add elementary style guide to website contribution section by @KPRoche in https://github.com/kubestellar/kubestellar/pull/3129
* 📖 Fix multiple broken links in docs discovered via crawler by @greninja517 in https://github.com/kubestellar/kubestellar/pull/3134
* 🐛  Make doc preview check not crash by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3138
* 🌱 Refactor: Improve the wait logic for CSR approval of WECs in demo-env file by @greninja517 in https://github.com/kubestellar/kubestellar/pull/3135
* 📖 Update get-started documentation by @abhishek-8081 in https://github.com/kubestellar/kubestellar/pull/3141
* 🐛 add shellcheck to setup-shell.sh by @AritraDey-Dev in https://github.com/kubestellar/kubestellar/pull/3040
* 📖 Style Guide: fixing initial typos by @KPRoche in https://github.com/kubestellar/kubestellar/pull/3150
* ✨  Add hack to reverse PR-to-files map and pretty print by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3143
* 🌱  Bump anchore/sbom-action/download-syft to v0.20.4 by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3156
* ✨ split ITS PCHs into status and clusteradmin by @rishi-jat in https://github.com/kubestellar/kubestellar/pull/3121
* 🐛 Undo bugs introduced in split of ITS PCH into two by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3163
* 🐛 Expand list of website source files by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3165
* 📖  Put one-shot tracking work in release process by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3164
* ✨ dependency policy fix of CLOMonitor by @antedotee in https://github.com/kubestellar/kubestellar/pull/3077
* 🐛 Fix bash typo by @eeshaanSA in https://github.com/kubestellar/kubestellar/pull/3159
* 🐛fix(pch): finalize ITS PCH sync, CRD wait, and busybox migration (follow-up to #3121) by @rishi-jat in https://github.com/kubestellar/kubestellar/pull/3168
* 📖 update generative AI paragraph in initial style guide by @KPRoche in https://github.com/kubestellar/kubestellar/pull/3162
* 📖 Add GitHub slash commands section to contributing guide by @krrish-sehgal in https://github.com/kubestellar/kubestellar/pull/3181
* 🌱better syntax and readibility for controlers in PCH by @Rupam-It in https://github.com/kubestellar/kubestellar/pull/3191
* 🌱 Bump stuff to pick up security fixes by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3201
* 🐛 Fix #3192: Use per-WDS ITSName and correct Helm quoting to resolve transport-controller ambiguity by @rishi-jat in https://github.com/kubestellar/kubestellar/pull/3194
* 🌱 Bump kubestellar/ocm-status-addon to 0.2.0-rc16 by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3202
* ✨ Update self-references in preparation for 0.29.0-alpha.1 by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3206
* 🐛fix(docs): restore PostCreateHook wait commands for install-status-addon and its-hub-init by @rishi-jat in https://github.com/kubestellar/kubestellar/pull/3169
* 📖 Start release notes for 0.29.0 by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3207
* 🌱 Bump dependencies in hack/build-clusteradm-image.sh by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3208
* 🐛 Getting started icon rendering at two places, one was unnecessary by @antedotee in https://github.com/kubestellar/kubestellar/pull/3205
* 🐛refactor(install-status-addon): replace shell-based CRD wait with dedicated initContainers by @rishi-jat in https://github.com/kubestellar/kubestellar/pull/3197
* 📖 Start drafting roadmap by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3199
* 🌱  Bump docker/login-action, set actions/github-script by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3225
* ✨ Update contributing-inc.md by @clubanderson in https://github.com/kubestellar/kubestellar/pull/3234
* 🌱 Refactor: Enhance K3d cluster creation wait to use kubectl wait instead of sleep for more reliability by @greninja517 in https://github.com/kubestellar/kubestellar/pull/3175
* added carriage return to 2 spots in doc to help with readability by @clubanderson in https://github.com/kubestellar/kubestellar/pull/3238
* 📖docs: document issue archive in CONTRIBUTING.md by @shivansh-source in https://github.com/kubestellar/kubestellar/pull/3231
* 📖 added release note to readme.md by @shivansh-source in https://github.com/kubestellar/kubestellar/pull/3232
* ✨ Add .gitattributes to normalize line endings and ignore generated files in diffs by @shivansh-source in https://github.com/kubestellar/kubestellar/pull/3241
* 🌱 Bump anchore/sbom-action/download-syft to 0.20.5 by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3248
* 🌱 Bump actions/first-interactions from 2 to 3.0.0 by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3249
* 📖 docs: Update .gitignore to block compiled binaries by @shivansh-source in https://github.com/kubestellar/kubestellar/pull/3251
* ✨ feat: add static analysis workflow for OpenSSF by @katara-Jayprakash in https://github.com/kubestellar/kubestellar/pull/3263
* 📖  Expand a11y section in docs style guide by @eeshaanSA in https://github.com/kubestellar/kubestellar/pull/3220
* 🌱 Bump goreleaser/goreleaser-action from 6.3.0 to 6.4.0 by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3266
* 🌱 Bump actions/checkout to 5.0.0 by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3265
* ✨ Increase in SEO and performance score on lighthouse for docs website by @antedotee in https://github.com/kubestellar/kubestellar/pull/3204
* 🐛 bug: golangci-lint workflow: remove deprecated --fast flag by @katara-Jayprakash in https://github.com/kubestellar/kubestellar/pull/3268
* 🌱 Bump .../google.golang.org/grpc/otelgrpc to 0.49.0 by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3270
* 🌱 Improved error handling in hack/gha-reversemap.sh by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3271
* 📖added explanation of authorization for downsync by @antedotee in https://github.com/kubestellar/kubestellar/pull/3209
* ✨  Add LatencyCollector controller to collect end-to-end metrics across clusters by @asmit27rai in https://github.com/kubestellar/kubestellar/pull/3008
* ✨Added stale workflow by @antedotee in https://github.com/kubestellar/kubestellar/pull/3272
* 📖 Update the ginkgo e2e test list to include the missing 'create-only' test cases by @waltforme in https://github.com/kubestellar/kubestellar/pull/3274
* ✨ Allow embedding for grafana by @asmit27rai in https://github.com/kubestellar/kubestellar/pull/3285
* ✨ KubeStellar Latency Controller by @asmit27rai in https://github.com/kubestellar/kubestellar/pull/3277
* ✨ Add prowjob to test the kubestellar-demo-env script by @greninja517 in https://github.com/kubestellar/kubestellar/pull/3203
* 🌱 Refactor `ValidateNumDeploymentReplicas` in ginkgo e2e test by @waltforme in https://github.com/kubestellar/kubestellar/pull/3276
* 🌱 Bump setup helm to 431 by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3291
* ✨Change static analysis schedule by @antedotee in https://github.com/kubestellar/kubestellar/pull/3273
* 🐛 Delete CustomTransform object before each ginkgo node by @waltforme in https://github.com/kubestellar/kubestellar/pull/3304
* 🌱 Bump actions stale, setup-python, setup-go, github-script by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3305
* 📖  Change headings to use colons and  headline case in example-scenarios.md by @KPRoche in https://github.com/kubestellar/kubestellar/pull/3282
* 🐛 fix(e2e): improve bash job wait logic by @rishi-jat in https://github.com/kubestellar/kubestellar/pull/3101
* 🐛fix(ci): sanitize and validate testFlags input for OSPS-BR-01.01 compliance by @rishi-jat in https://github.com/kubestellar/kubestellar/pull/3318
* 🐛fix: add doc link to preview check failure message by @rishi-jat in https://github.com/kubestellar/kubestellar/pull/3319
* ✨ Upgrade ArgoCD core-chart dependency to v8.3.5 by @francostellari in https://github.com/kubestellar/kubestellar/pull/3312
* 🐛 Add safeguard for kubeflex-system ns creation by @francostellari in https://github.com/kubestellar/kubestellar/pull/3315
* 📖  Updating readme for KS benchmarking exps by @dumb0002 in https://github.com/kubestellar/kubestellar/pull/3328
* 📖Fix CONTRIBUTING.md and contributing-inc.md dual-source structure by @rishi-jat in https://github.com/kubestellar/kubestellar/pull/3321
* ✨  Scale Infra for KS Performance Test by @dumb0002 in https://github.com/kubestellar/kubestellar/pull/2666
* ✨ Change some unit tests into Go fuzz tests  by @katara-Jayprakash in https://github.com/kubestellar/kubestellar/pull/3327
* 🌱 Remove unused DeprecatedAddToFlags function by @shubhanshu-02 in https://github.com/kubestellar/kubestellar/pull/3306
* ✨ Update to use kubeflex release 0.9.1 by @katara-Jayprakash in https://github.com/kubestellar/kubestellar/pull/3309
* ✨added deepwiki badge in the readme by @antedotee in https://github.com/kubestellar/kubestellar/pull/3358
* 📖fixed the docs to add `relates to` in PR signoff by @antedotee in https://github.com/kubestellar/kubestellar/pull/3353
* 📖  Remove stop applying PCHes too early from roadmap by @gaurab-khanal in https://github.com/kubestellar/kubestellar/pull/3376
* 🌱 Bump five actions to latest by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3388
* 🌱 Simplify wait-for-placements-crd-created init container by @francostellari in https://github.com/kubestellar/kubestellar/pull/3407
* 🌱 Simplify wait-for-managedclustersetbindings-crd-created initContainer by @francostellari in https://github.com/kubestellar/kubestellar/pull/3409
* ✨ enable waitForPostCreateHooks for ITSes by @AritraDey-Dev in https://github.com/kubestellar/kubestellar/pull/3148
* 🐛fixed the build error by @antedotee in https://github.com/kubestellar/kubestellar/pull/3340
* 📖removed unncessary references by @antedotee in https://github.com/kubestellar/kubestellar/pull/3341
* 📖fixed the link issue by @antedotee in https://github.com/kubestellar/kubestellar/pull/3342
* 📖fixed the highlighting link error by @antedotee in https://github.com/kubestellar/kubestellar/pull/3348
* 📖 fixed link to inline image by @antedotee in https://github.com/kubestellar/kubestellar/pull/3349
* ✨added hacktober-fest-label by @antedotee in https://github.com/kubestellar/kubestellar/pull/3367
* ✨ Speed up Helm chart deployment by removing unnecessary initContainer  [NEW] by @francostellari in https://github.com/kubestellar/kubestellar/pull/3416
* ✨ Added the content for removing outdated (draft branch) versions after rendering section by @antedotee in https://github.com/kubestellar/kubestellar/pull/3360
* 🌱 Remove redundant code by @ngvanthanggit in https://github.com/kubestellar/kubestellar/pull/3419
* ✨ Cleanup hub-init PCH by @francostellari in https://github.com/kubestellar/kubestellar/pull/3425
* ✨ Cleanup kubestellar controller PCH by @francostellari in https://github.com/kubestellar/kubestellar/pull/3426
* 📖 Brush up documentation of website rendering by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3427
* ✨Cleanup install-status-addon PCH by @francostellari in https://github.com/kubestellar/kubestellar/pull/3424
* ✨ Make E2E CI job list namespaces in ITS1 by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3429
* ✨ Improve resource handling in kubectl-rbac-flatten by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3435
* ✨added scroll to top feature by @antedotee in https://github.com/kubestellar/kubestellar/pull/3385
* ✨ Add filtering by subject and verb, to rbac flattener by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3438
* 🌱 feat(e2e): Dump redacted Secret YAMLs for debuggability by @shivansh-gohem in https://github.com/kubestellar/kubestellar/pull/3361
* 🌱 Bump anchore/sbom-action/download-syft from 0.20.6 to 0.20.9 by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3445
* 🌱 Bump actions/upload-artifact from 4.6.2 to 5.0.0 by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3446
* 🌱 test(e2e): Always dump kubeflex-controller-manager logs by @shivansh-gohem in https://github.com/kubestellar/kubestellar/pull/3447
* 🌱 Bump rojopolis/spellcheck-github-actions from 0.52.0 to 0.53.0 by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3448
* 🐛 Fix version check when only bounded range is desired by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3449
* ✨ Make transport-controller mount WDS secret directly by @francostellari in https://github.com/kubestellar/kubestellar/pull/3428
* 📖 Self-reference updates in prep for 0.29.0-rc.1 by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3455
* ✨ Update self-references for release 0.29.0 by @MikeSpreitzer in https://github.com/kubestellar/kubestellar/pull/3463

## New Contributors
* @Arpit529Srivastava made their first contribution in https://github.com/kubestellar/kubestellar/pull/2982
* @rishi-jat made their first contribution in https://github.com/kubestellar/kubestellar/pull/3007
* @greninja517 made their first contribution in https://github.com/kubestellar/kubestellar/pull/3102
* @flushthemoney made their first contribution in https://github.com/kubestellar/kubestellar/pull/3126
* @Tob-iee made their first contribution in https://github.com/kubestellar/kubestellar/pull/3092
* @abhishek-8081 made their first contribution in https://github.com/kubestellar/kubestellar/pull/3141
* @AritraDey-Dev made their first contribution in https://github.com/kubestellar/kubestellar/pull/3040
* @eeshaanSA made their first contribution in https://github.com/kubestellar/kubestellar/pull/3159
* @krrish-sehgal made their first contribution in https://github.com/kubestellar/kubestellar/pull/3181
* @shivansh-source made their first contribution in https://github.com/kubestellar/kubestellar/pull/3231
* @katara-Jayprakash made their first contribution in https://github.com/kubestellar/kubestellar/pull/3263
* @asmit27rai made their first contribution in https://github.com/kubestellar/kubestellar/pull/3008
* @shubhanshu-02 made their first contribution in https://github.com/kubestellar/kubestellar/pull/3306
* @gaurab-khanal made their first contribution in https://github.com/kubestellar/kubestellar/pull/3376
* @ngvanthanggit made their first contribution in https://github.com/kubestellar/kubestellar/pull/3419
* @shivansh-gohem made their first contribution in https://github.com/kubestellar/kubestellar/pull/3361

**Full Changelog**: https://github.com/kubestellar/kubestellar/compare/v0.28.0...v0.29.0