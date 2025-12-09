# KServe - v0.16.0

**Release Name**: v0.16.0
**Published**: 2025-11-03T02:40:28Z
**Repository**: https://github.com/kserve/kserve

---

## What's Changed
* chore: remove 'default' suffix compatibility by @sivanantha321 in https://github.com/kserve/kserve/pull/4178
* Upgrade Torch to v2.6.0 everywhere by @ashahba in https://github.com/kserve/kserve/pull/4450
* chore: drop pydantic v1 support by @sivanantha321 in https://github.com/kserve/kserve/pull/4353
* fix: Update TextIteratorStreamer to skip special tokens by @sivanantha321 in https://github.com/kserve/kserve/pull/4490
* Add Jooho to approvers in OWNERS file by @terrytangyuan in https://github.com/kserve/kserve/pull/4504
* Rename CRD file to reflect all KServe CRDs (Fixes #4396) by @WHITE-ICE-BOX in https://github.com/kserve/kserve/pull/4494
* Update kserve-resources helm chart to disable desired servingruntimes by @jmlaubach in https://github.com/kserve/kserve/pull/4485
* upgrade vllm to v0.9.0 and Torch to v2.7.0 by @ashahba in https://github.com/kserve/kserve/pull/4501
* Upgrade vLLM to v0.9.0.1 by @ashahba in https://github.com/kserve/kserve/pull/4507
* Initial segregation of the storage module from KServe SDK by @spolti in https://github.com/kserve/kserve/pull/4391
* Fix pss restricted warnings by @akagami-harsh in https://github.com/kserve/kserve/pull/4327
* Fix: do not update poetry dependency when install hf cpu deps by @yuzisun in https://github.com/kserve/kserve/pull/4516
* [Bug] Fixes error in trace logging by @gavrissh in https://github.com/kserve/kserve/pull/4514
* Stop and resume a model [Raw Deployment] by @hdefazio in https://github.com/kserve/kserve/pull/4455
* Resolve inference endpoint using runtime protocol when applicable by @israel-hdez in https://github.com/kserve/kserve/pull/4527
* fix(codegen): pins code-generator binaries version by @bartoszmajsak in https://github.com/kserve/kserve/pull/4533
* Allow to set custom timeouts for `InferenceGraph` router by @lifo9 in https://github.com/kserve/kserve/pull/4218
* feat: support remote storage URI injection for serving runtimes by @de0725 in https://github.com/kserve/kserve/pull/4492
* [API] Define LLMInferenceService and LLMInferenceServiceConfig types and CRDs by @pierDipi in https://github.com/kserve/kserve/pull/4522
* Stop and Resume a transformer by @hdefazio in https://github.com/kserve/kserve/pull/4534
* Allow OCI for multi-node/multi-gpu by @israel-hdez in https://github.com/kserve/kserve/pull/4441
* 4380 - Inference logging to blob storage by @cjohannsen-cloudera in https://github.com/kserve/kserve/pull/4473
* Fix outdated BentoML import in sample code (BentoService no longer available in v1.x) by @YehCC52 in https://github.com/kserve/kserve/pull/4540
* Auto-update annotation for isvc. by @andresllh in https://github.com/kserve/kserve/pull/4342
* Stop and resume an explainer by @hdefazio in https://github.com/kserve/kserve/pull/4546
* fix: unset clampMax and clampMin, since they are not for replicas by @houshengbo in https://github.com/kserve/kserve/pull/4556
* refactor: Enhance HTTPRoute readiness checks by @sivanantha321 in https://github.com/kserve/kserve/pull/4543
* Refactor KServe to use global context for PredictorConfig by @sivanantha321 in https://github.com/kserve/kserve/pull/4526
* feat: refactor storage initializer resources configuration by @takamai06 in https://github.com/kserve/kserve/pull/4411
* feat(envtest): simplifies CRD lookup by @bartoszmajsak in https://github.com/kserve/kserve/pull/4564
* llmisvc: Initial controller scaffold and helm chart by @sivanantha321 in https://github.com/kserve/kserve/pull/4557
* Add logic to merge specs for LLMInferenceService  by @VedantMahabaleshwarkar in https://github.com/kserve/kserve/pull/4563
* fix: Allow CA bundle path without config map by @fabiendupont in https://github.com/kserve/kserve/pull/4451
* docs: fixes invalid openshift subscription by @bartoszmajsak in https://github.com/kserve/kserve/pull/4572
* Add Code Coverage change report for PRs by @andyi2it in https://github.com/kserve/kserve/pull/4487
* feat: support secure access to prometheus in keda by @andyi2it in https://github.com/kserve/kserve/pull/4384
* feat: switch kserve from poetry to uv by @andyi2it in https://github.com/kserve/kserve/pull/4407
* chore(utils): simplifies code using generics by @bartoszmajsak in https://github.com/kserve/kserve/pull/4578
* Add AOT flashinfer build to huggingfaceserver dockerfile to precompil… by @AyushSawant18588 in https://github.com/kserve/kserve/pull/4567
* feat: improves collection helpers by @bartoszmajsak in https://github.com/kserve/kserve/pull/4579
* Add Missing config file for code coverage by @andyi2it in https://github.com/kserve/kserve/pull/4581
* Fix: Support multiple metrics in OpenTelemetryCollector for autoscaling by @houshengbo in https://github.com/kserve/kserve/pull/4591
* Upgrade vllm to v0.9.2 by @AyushSawant18588 in https://github.com/kserve/kserve/pull/4586
* Remove unused Strategy interface from sharding package by @houshengbo in https://github.com/kserve/kserve/pull/4590
* fix(test): uses local httptest server urls for downloader tests by @bartoszmajsak in https://github.com/kserve/kserve/pull/4601
* Fixed the issue of the same metrics across different deployments under different namespaces by @houshengbo in https://github.com/kserve/kserve/pull/4593
* feat: Add disable postprocessing option for raw logits by @sivanantha321 in https://github.com/kserve/kserve/pull/4566
* Stop and resume an inference graph by @hdefazio in https://github.com/kserve/kserve/pull/4588
* disallow `name` field in standard predictor by @HutakiHare in https://github.com/kserve/kserve/pull/4535
* fix: missing pytest-asyncio session scope marker in test_kserve_logger_cipn by @sivanantha321 in https://github.com/kserve/kserve/pull/4607
* update CRDs for LWS based multi node support by @VedantMahabaleshwarkar in https://github.com/kserve/kserve/pull/4596
* Add LLM InferenceService base configurations by @VedantMahabaleshwarkar in https://github.com/kserve/kserve/pull/4613
* fix: fixes misleading print for parallelism when $# > 2 (#784) by @bartoszmajsak in https://github.com/kserve/kserve/pull/4619
* Remove storage spec from LLMIsvc by @israel-hdez in https://github.com/kserve/kserve/pull/4622
* feat: speed up ci by @ls-2018 in https://github.com/kserve/kserve/pull/4600
* fix(deps): adds missing LLMInferenceService types for python imports by @bartoszmajsak in https://github.com/kserve/kserve/pull/4604
* Adding Llm-d scheduler reconcilier by @andresllh in https://github.com/kserve/kserve/pull/4614
* [Followup] Improve the stop/resume Inference Service tests and status by @hdefazio in https://github.com/kserve/kserve/pull/4636
* Added advanced config for ScaleUp and ScaleDown by @andyi2it in https://github.com/kserve/kserve/pull/4570
* add resource default for otel collector container limit in configmap by @andyi2it in https://github.com/kserve/kserve/pull/4633
* Protobuf version bump by @karolpustelnik in https://github.com/kserve/kserve/pull/4634
* Stop and resume an inference graph [Raw Deployment] by @hdefazio in https://github.com/kserve/kserve/pull/4637
* Fix typos: in the repo by @mwaykole in https://github.com/kserve/kserve/pull/4641
* llm-d workload reconciliation by @brettmthompson in https://github.com/kserve/kserve/pull/4616
* Llm d http route reconciler by @andresllh in https://github.com/kserve/kserve/pull/4617
* feat(webhook): introduces Validating Webhook for LLMInferenceServiceConfig by @VedantMahabaleshwarkar in https://github.com/kserve/kserve/pull/4630
* fix: Adds support for NVIDIA MIG GPU resource detection by @sivanantha321 in https://github.com/kserve/kserve/pull/4642
* feat(webhook): introduces Validating Webhook for LLMInferenceService by @VedantMahabaleshwarkar in https://github.com/kserve/kserve/pull/4631
* Add logic for LLMISVC controller by @VedantMahabaleshwarkar in https://github.com/kserve/kserve/pull/4632
* Fix quickstart link by @thesteve0 in https://github.com/kserve/kserve/pull/4654
* ci: skip workflows when only markdown files are changed by @Jooho in https://github.com/kserve/kserve/pull/4650
* refactor: 4602 - Refactor "RawDeployment" to "Standard" and "Serverless" to  "KNative" to clarify usage by @cjohannsen-cloudera in https://github.com/kserve/kserve/pull/4608
* fix: README links to KServe website updated by @dominikkawka in https://github.com/kserve/kserve/pull/4656
* fix: allow digests in runtimes' images by @tmvfb in https://github.com/kserve/kserve/pull/4653
* [llmisvc] Improve config merge and update well-known presets by @pierDipi in https://github.com/kserve/kserve/pull/4663
* [llmisvc] Support cluster-scoped objects in generic CRUD functions by @pierDipi in https://github.com/kserve/kserve/pull/4664
* fix: fix snyk scan sarif file upload by @sivanantha321 in https://github.com/kserve/kserve/pull/4660
* fix: defaults GITHUB_SHA for graph images by @bartoszmajsak in https://github.com/kserve/kserve/pull/4620
* Promote new KServe Storage module by @spolti in https://github.com/kserve/kserve/pull/4625
* fix: escape HTML characters in api comments to fix syntax errors in website docs by @sivanantha321 in https://github.com/kserve/kserve/pull/4662
* Implement the progressive rollout for raw deployment by @houshengbo in https://github.com/kserve/kserve/pull/4623
* fix: dry run update for keda autoscaling loop by @andyi2it in https://github.com/kserve/kserve/pull/4587
* Fix HF Token Vulnerability in Storage Initializer Container by @brettmthompson in https://github.com/kserve/kserve/pull/4677
* docs: update Kafka sample path after file relocation by @1lyvianis in https://github.com/kserve/kserve/pull/4680
* Last Deployment Status Should Reflect Deployment Status by @HotsauceLee in https://github.com/kserve/kserve/pull/4667
* Fix: Update ModelCopies.TotalCopies for all model states  by @hardik-menger in https://github.com/kserve/kserve/pull/4676
* Prepare for 0.16.0-rc0 release by @houshengbo in https://github.com/kserve/kserve/pull/4678
* fix: istio installation failures and update kserve to stable version  by @Ce11an in https://github.com/kserve/kserve/pull/4684
* chore(test-setup): replaces gatewayclass in-memory by @bartoszmajsak in https://github.com/kserve/kserve/pull/4605
* [llmisvc] Update workload and router reconciliation by @pierDipi in https://github.com/kserve/kserve/pull/4666
* ci: publish llmisvc container image by @yuzisun in https://github.com/kserve/kserve/pull/4686
* deprecate: remove EnableDirectPvcVolumeMount flag by @anurags25 in https://github.com/kserve/kserve/pull/4694
* Fix autoscaling tests duration and crashes by @andyi2it in https://github.com/kserve/kserve/pull/4688
* Avoid Pervasive Logging of SA Not Found Errors by Credential Builder by @brettmthompson in https://github.com/kserve/kserve/pull/4696
* fix: correct llmisvc Dockerfile reference in image publish workflow by @sivanantha321 in https://github.com/kserve/kserve/pull/4705
* llmisvc: fix RBAC, templating, and adds quick install script by @sivanantha321 in https://github.com/kserve/kserve/pull/4698
* Fixed the panic nil pointer issue componentExt being nil by @houshengbo in https://github.com/kserve/kserve/pull/4704
* fix: Add disk space cleanup step to Docker publish workflows by @sivanantha321 in https://github.com/kserve/kserve/pull/4717
* Add Star History section to README by @terrytangyuan in https://github.com/kserve/kserve/pull/4719
* docs: Mention CNCF in project README by @terrytangyuan in https://github.com/kserve/kserve/pull/4718
* Enabled the configuration options in Helm for opentelemetryCollector and autoscaler by @houshengbo in https://github.com/kserve/kserve/pull/4725
* Time Series Forecast API Endpoint by @jinan-zhou in https://github.com/kserve/kserve/pull/4615
* llmisvc dev & kustomize setup, add webhook config to helm chart  by @sivanantha321 in https://github.com/kserve/kserve/pull/4712
* Revise KServe overview and enhance features section by @terrytangyuan in https://github.com/kserve/kserve/pull/4721
* Fix incorrect entrypoint in llmisvc Dockerfile by @Jooho in https://github.com/kserve/kserve/pull/4730
* Configure HF Downloads to Lower Memory Usage by @brettmthompson in https://github.com/kserve/kserve/pull/4726
* Temporarily disable SSL to unblock e2e tests by @Jooho in https://github.com/kserve/kserve/pull/4731
* Use a wrapper struct to accept resource.Quantity and keep the original input by @houshengbo in https://github.com/kserve/kserve/pull/4699
* Support Multiple Storage URIs for InferenceServices by @anurags25 in https://github.com/kserve/kserve/pull/4702
* Fix: prepend the KO_DOCKER_REPOSITORY to the base docker build to allow local publishing of the controller by @cjohannsen-cloudera in https://github.com/kserve/kserve/pull/4736
* Add Cert Manager installation to llmisvc quick install script by @sivanantha321 in https://github.com/kserve/kserve/pull/4733
* Injecting CA Bundle Into Storage Initializer Container for S3 Storage on LLMISVC Reconciliation by @brettmthompson in https://github.com/kserve/kserve/pull/4728
* Add metadata propagation for Kueue configurations to both Deployment and LeaderWorkerSet workloads by @hdefazio in https://github.com/kserve/kserve/pull/4747
* Add Support for Configuring S3 Storage via Secret Data by @brettmthompson in https://github.com/kserve/kserve/pull/4727
* 4739 - Fix: blob storage for inference logging recognizes embedded spec by @cjohannsen-cloudera in https://github.com/kserve/kserve/pull/4740
* Add llmd e2e tests by @andresllh in https://github.com/kserve/kserve/pull/4729
* Prepare for 0.16.0-rc1 release by @houshengbo in https://github.com/kserve/kserve/pull/4732
* Update the kserve-storage module to the latest version by @spolti in https://github.com/kserve/kserve/pull/4754
* feature: 4553 - Support inference logging to GCS and Azure by @cjohannsen-cloudera in https://github.com/kserve/kserve/pull/4582
* fix(helm-chart): expose `uidModelcar` in the chart by @maciej-tatarski in https://github.com/kserve/kserve/pull/4689
* fix(ci): recreate root venv when cached symlink is broken by @Jooho in https://github.com/kserve/kserve/pull/4768
* fix: wrong kserve controller image url by @Jooho in https://github.com/kserve/kserve/pull/4773
* bump up istio version to 1.27.1 by @Jooho in https://github.com/kserve/kserve/pull/4775
* refactor: separate llmisvc manifests from default kustomization by @Jooho in https://github.com/kserve/kserve/pull/4763
* 4778 - Fix: apply metadata headers to inference logging response by @cjohannsen-cloudera in https://github.com/kserve/kserve/pull/4779
* Fix the issue of Invalid value for env[1].valueFrom by @houshengbo in https://github.com/kserve/kserve/pull/4765
* clean-up raw-controller tests by @spolti in https://github.com/kserve/kserve/pull/4781
* Add centralized installation scripts for KServe dependencies by @Jooho in https://github.com/kserve/kserve/pull/4774
* Add/Update llm sample including README.md by @Jooho in https://github.com/kserve/kserve/pull/4780
* Fix XGBoost .ubj and .json models with modelcar by @balazsprehoda in https://github.com/kserve/kserve/pull/4746
* Fixed the CA bundle env var logic by @houshengbo in https://github.com/kserve/kserve/pull/4777
* Prepare for 0.16.0 release by @houshengbo in https://github.com/kserve/kserve/pull/4786
* huggingfaceserver: fix mean_pooling device/dtype mismatch and add regression test by @JohnsonWang1015 in https://github.com/kserve/kserve/pull/4744
* Allow mapping predictions to instances in sequential inference graphs by @tmbochenski in https://github.com/kserve/kserve/pull/4738
* update kserve-storage pypi token by @yuzisun in https://github.com/kserve/kserve/pull/4788
* fix llmisvc-crd-minimal chart by @yuzisun in https://github.com/kserve/kserve/pull/4789

## New Contributors
* @WHITE-ICE-BOX made their first contribution in https://github.com/kserve/kserve/pull/4494
* @jmlaubach made their first contribution in https://github.com/kserve/kserve/pull/4485
* @akagami-harsh made their first contribution in https://github.com/kserve/kserve/pull/4327
* @lifo9 made their first contribution in https://github.com/kserve/kserve/pull/4218
* @de0725 made their first contribution in https://github.com/kserve/kserve/pull/4492
* @pierDipi made their first contribution in https://github.com/kserve/kserve/pull/4522
* @cjohannsen-cloudera made their first contribution in https://github.com/kserve/kserve/pull/4473
* @YehCC52 made their first contribution in https://github.com/kserve/kserve/pull/4540
* @takamai06 made their first contribution in https://github.com/kserve/kserve/pull/4411
* @VedantMahabaleshwarkar made their first contribution in https://github.com/kserve/kserve/pull/4563
* @fabiendupont made their first contribution in https://github.com/kserve/kserve/pull/4451
* @HutakiHare made their first contribution in https://github.com/kserve/kserve/pull/4535
* @ls-2018 made their first contribution in https://github.com/kserve/kserve/pull/4600
* @karolpustelnik made their first contribution in https://github.com/kserve/kserve/pull/4634
* @mwaykole made their first contribution in https://github.com/kserve/kserve/pull/4641
* @thesteve0 made their first contribution in https://github.com/kserve/kserve/pull/4654
* @dominikkawka made their first contribution in https://github.com/kserve/kserve/pull/4656
* @tmvfb made their first contribution in https://github.com/kserve/kserve/pull/4653
* @1lyvianis made their first contribution in https://github.com/kserve/kserve/pull/4680
* @hardik-menger made their first contribution in https://github.com/kserve/kserve/pull/4676
* @Ce11an made their first contribution in https://github.com/kserve/kserve/pull/4684
* @anurags25 made their first contribution in https://github.com/kserve/kserve/pull/4694
* @jinan-zhou made their first contribution in https://github.com/kserve/kserve/pull/4615
* @maciej-tatarski made their first contribution in https://github.com/kserve/kserve/pull/4689
* @balazsprehoda made their first contribution in https://github.com/kserve/kserve/pull/4746
* @JohnsonWang1015 made their first contribution in https://github.com/kserve/kserve/pull/4744

**Full Changelog**: https://github.com/kserve/kserve/compare/v0.15.2...v0.16.0