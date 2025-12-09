# Serverless Workflow - v1.0.0

**Release Name**: v1.0.0
**Published**: 2025-01-27T18:14:26Z
**Repository**: https://github.com/serverlessworkflow/specification

---

## What's Changed
* Total refactor by @cdavernas in https://github.com/serverlessworkflow/specification/pull/847
* Add cache path to node CI and remove examples hydration pipeline by @ricardozanini in https://github.com/serverlessworkflow/specification/pull/861
* Fix switch 'then' to accept free strings by @ricardozanini in https://github.com/serverlessworkflow/specification/pull/863
* Remove YAML formatting tabs by @fjtirado in https://github.com/serverlessworkflow/specification/pull/870
* Fix bearer.token property by @matthias-pichler in https://github.com/serverlessworkflow/specification/pull/865
* Fix URI format in workflow schema for endpoint attribute by @ricardozanini in https://github.com/serverlessworkflow/specification/pull/879
* Fix workflow schema: change `const`, adding missing `object`; etc. by @matthias-pichler in https://github.com/serverlessworkflow/specification/pull/876
* Fix usage of endpoint in-call http tasks by @matthias-pichler in https://github.com/serverlessworkflow/specification/pull/877
* Remove reliance on key order in maps/objects by @matthias-pichler in https://github.com/serverlessworkflow/specification/pull/882
* Update maintainers by @JBBianchi in https://github.com/serverlessworkflow/specification/pull/888
* Rename output.from and output.to by @fjtirado in https://github.com/serverlessworkflow/specification/pull/892
* Fix error in export definition by @fjtirado in https://github.com/serverlessworkflow/specification/pull/896
* Make do an array by @matthias-pichler in https://github.com/serverlessworkflow/specification/pull/895
* Fix task `if` property doc by @cdavernas in https://github.com/serverlessworkflow/specification/pull/898
* Add titles to oneOf and repeating names by @fjtirado in https://github.com/serverlessworkflow/specification/pull/901
* Fix a few typo from DSL by @yzhao244 in https://github.com/serverlessworkflow/specification/pull/902
* Changes  the way authentication policies can be referenced by @cdavernas in https://github.com/serverlessworkflow/specification/pull/908
* Fixes the schema to allow `input.from`, `output.as` and `export.as` to be either a runtime expression string or object by @cdavernas in https://github.com/serverlessworkflow/specification/pull/907
* Adding title to switch by @fjtirado in https://github.com/serverlessworkflow/specification/pull/905
* Fix port schema by @matthias-pichler in https://github.com/serverlessworkflow/specification/pull/924
* Fix switch schema by @matthias-pichler in https://github.com/serverlessworkflow/specification/pull/922
* Add titles to tasks by @matthias-pichler in https://github.com/serverlessworkflow/specification/pull/919
* Fix `run` task documentation by @yzhao244 in https://github.com/serverlessworkflow/specification/pull/920
* Add Yuri Zhao and Francisco Javier Tirado Sarti as contributors by @cdavernas in https://github.com/serverlessworkflow/specification/pull/935
* Fix typo RunWokflow by @zolero in https://github.com/serverlessworkflow/specification/pull/925
* Fix CTK link by @cdavernas in https://github.com/serverlessworkflow/specification/pull/941
* Fix output examples from dsl reference and ctk feature by @yzhao244 in https://github.com/serverlessworkflow/specification/pull/936
* Allow runtime-expressions for formatted strings by @matthias-pichler in https://github.com/serverlessworkflow/specification/pull/938
* Adding missing titles for better pojo generation by @fjtirado in https://github.com/serverlessworkflow/specification/pull/944
* Restrict extra props by @matthias-pichler in https://github.com/serverlessworkflow/specification/pull/928
* Create SECURITY.md by @cdavernas in https://github.com/serverlessworkflow/specification/pull/947
* Fix README.md Badges by @cdavernas in https://github.com/serverlessworkflow/specification/pull/946
* Remove duplicate uri scheme from error types by @matthias-pichler in https://github.com/serverlessworkflow/specification/pull/957
* Specify task and workflow arguments by @matthias-pichler in https://github.com/serverlessworkflow/specification/pull/953
* Document limited uri-template support by @matthias-pichler in https://github.com/serverlessworkflow/specification/pull/955
* Allow query parameters in call http by @matthias-pichler in https://github.com/serverlessworkflow/specification/pull/956
* Specify runtime argument by @matthias-pichler in https://github.com/serverlessworkflow/specification/pull/952
* Fixed inconsistencies between `listen` and `emit` by @JBBianchi in https://github.com/serverlessworkflow/specification/pull/963
* Add a new `arguments` property to the `script` process by @cdavernas in https://github.com/serverlessworkflow/specification/pull/960
* Document Data Flow and expression context more clearly by @matthias-pichler in https://github.com/serverlessworkflow/specification/pull/958
* Add priority of constituencies by @matthias-pichler in https://github.com/serverlessworkflow/specification/pull/948
* Add `reference` property to the `TaskDescriptor` object by @cdavernas in https://github.com/serverlessworkflow/specification/pull/965
* Added titles and descriptions to the DSL JSON Schema by @JBBianchi in https://github.com/serverlessworkflow/specification/pull/968
* Fix custom function documentation by @cdavernas in https://github.com/serverlessworkflow/specification/pull/969
* Consolidate `endpoint` and `externalResource` definitions by @JBBianchi in https://github.com/serverlessworkflow/specification/pull/975
* Extract datetime descriptor by @matthias-pichler in https://github.com/serverlessworkflow/specification/pull/974
* Fixed `call`, `raise` and `try` features by @cdavernas in https://github.com/serverlessworkflow/specification/pull/984
* Refactor OAuth2 and add OIDC authentication policy by @cdavernas in https://github.com/serverlessworkflow/specification/pull/973
* Change CI to always kick validation by @ricardozanini in https://github.com/serverlessworkflow/specification/pull/986
* Document the difference between an event-driven schedule and a startup listen task by @cdavernas in https://github.com/serverlessworkflow/specification/pull/987
* Add use cases and examples by @cdavernas in https://github.com/serverlessworkflow/specification/pull/988
* Add a new `metadata` property to the workflow document and to tasks by @cdavernas in https://github.com/serverlessworkflow/specification/pull/996
* Document schema validation order by @matthias-pichler in https://github.com/serverlessworkflow/specification/pull/982
* Fixed `DigestAuthenticationProperties` title in schema by @JBBianchi in https://github.com/serverlessworkflow/specification/pull/1000
* Added new reusable components and fixed unreferenceable errors and retries by @cdavernas in https://github.com/serverlessworkflow/specification/pull/1002
* Add a new property used to determine whether or not to await the execution of a process  by @cdavernas in https://github.com/serverlessworkflow/specification/pull/995
* Document context of `task.if` by @matthias-pichler in https://github.com/serverlessworkflow/specification/pull/1005
* Added unevaluatedProperties false to oauth2AuthenticationProperties by @JBBianchi in https://github.com/serverlessworkflow/specification/pull/1008
* Updated schema version to 1.0.0 by @JBBianchi in https://github.com/serverlessworkflow/specification/pull/1010
* Fix #983 - Add CTK workflow features to CI/CD validation by @ricardozanini in https://github.com/serverlessworkflow/specification/pull/1014
* Fix schema id by @cdavernas in https://github.com/serverlessworkflow/specification/pull/1016
* Fix Uri-Template by @matthias-pichler in https://github.com/serverlessworkflow/specification/pull/1018
* Add a new `catalogs` property to workflow resources by @cdavernas in https://github.com/serverlessworkflow/specification/pull/1022
* Adding more titles to schema by @fjtirado in https://github.com/serverlessworkflow/specification/pull/1025
* Adding usage of content-type header in one of http examples by @fjtirado in https://github.com/serverlessworkflow/specification/pull/1027
* Change task context to workflow context by @fjtirado in https://github.com/serverlessworkflow/specification/pull/1028
* Fixed example file name by @JBBianchi in https://github.com/serverlessworkflow/specification/pull/1033
* Adjust authentication link by @mcruzdev in https://github.com/serverlessworkflow/specification/pull/1034
* Add filter error by @fjtirado in https://github.com/serverlessworkflow/specification/pull/1035
* Aligning examples errors with spec by @fjtirado in https://github.com/serverlessworkflow/specification/pull/1038
* Set behaviour clarification by @fjtirado in https://github.com/serverlessworkflow/specification/pull/1041
* Replace standard issue templates by form-based ones by @cdavernas in https://github.com/serverlessworkflow/specification/pull/1043
* Add a new `return` property to the `run` task by @cdavernas in https://github.com/serverlessworkflow/specification/pull/1052
* Add a new `$authorization` runtime expression argument by @cdavernas in https://github.com/serverlessworkflow/specification/pull/1048
* Renamed the OpenAPI `arguments` property to `parameters`  in the `dsl-reference.md` file by @cdavernas in https://github.com/serverlessworkflow/specification/pull/1046
* Document the output of a task that defines an non-awaited process by @cdavernas in https://github.com/serverlessworkflow/specification/pull/1050
* Refactor the `AsyncAPI` call by @cdavernas in https://github.com/serverlessworkflow/specification/pull/1053
* Add a new `to` property to the `emit` task by @cdavernas in https://github.com/serverlessworkflow/specification/pull/1047
* Add a new `lifetime` property to the `container` process by @cdavernas in https://github.com/serverlessworkflow/specification/pull/1049
* Add warnings about using the `$secrets` runtime expression by @cdavernas in https://github.com/serverlessworkflow/specification/pull/1058
* Add a new `redirect` property to both `http`and `openapi` calls by @cdavernas in https://github.com/serverlessworkflow/specification/pull/1057
* Restrict script language versions by @cdavernas in https://github.com/serverlessworkflow/specification/pull/1063
* Add warnings about flow directives being able to only target tasks defined in the same scope by @cdavernas in https://github.com/serverlessworkflow/specification/pull/1060
* Document the output of `fork` tasks in competing and non-competing scenarii by @cdavernas in https://github.com/serverlessworkflow/specification/pull/1059
* Recommend container naming convention for runtime implementations by @JBBianchi in https://github.com/serverlessworkflow/specification/pull/1061
* Add support for dynamic container names via runtime expressions by @JBBianchi in https://github.com/serverlessworkflow/specification/pull/1062
* Added a new `until` property to `any` event consumption strategies by @cdavernas in https://github.com/serverlessworkflow/specification/pull/997
* Add PHP and Rust SDKs to the SDK section in the README.md by @cdavernas in https://github.com/serverlessworkflow/specification/pull/1064
* Aling Listen to specification with example by @fjtirado in https://github.com/serverlessworkflow/specification/pull/1066
* Add data to EventProperties by @fjtirado in https://github.com/serverlessworkflow/specification/pull/1067
* Add streaming capabilities to both the `listen` task and to the `asyncapi` (subscribe operation) call  by @cdavernas in https://github.com/serverlessworkflow/specification/pull/1070
* Until option if any is empty by @fjtirado in https://github.com/serverlessworkflow/specification/pull/1072
* Add documentation about workflow and task lifecycle events by @cdavernas in https://github.com/serverlessworkflow/specification/pull/1054
* Remove the `cc` property from the `emit` task by @cdavernas in https://github.com/serverlessworkflow/specification/pull/1074

## New Contributors
* @matthias-pichler made their first contribution in https://github.com/serverlessworkflow/specification/pull/865
* @zolero made their first contribution in https://github.com/serverlessworkflow/specification/pull/925
* @mcruzdev made their first contribution in https://github.com/serverlessworkflow/specification/pull/1034

**Full Changelog**: https://github.com/serverlessworkflow/specification/compare/v0.9.0...v1.0.0