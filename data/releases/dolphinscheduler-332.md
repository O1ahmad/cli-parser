# DolphinScheduler - 3.3.2

**Release Name**: 
**Published**: 2025-10-26T08:49:29Z
**Repository**: https://github.com/apache/dolphinscheduler

---

## Improvement

<details><summary>Click to expand</summary>

- [Improvement-17447] Remove unused task definition doc (#17448) @SbloodyS
- [Improvement-17445] Fix dolphindb doc location error (#17444) @SbloodyS
- [Chore] Optimize pom, make dolphinscheduler-spi provided (#17500) @ruanwenjun
- [Improvement-17485][Master] Change batchTriggerAcquisitionMaxCount default value equals to threadCount (#17483) @ruanwenjun
- [Doc-17490] Deployment doc improvement (#17491) @SbloodyS
- [Improvement-17467][Master] Support set a separate dataSource for quartz (#17468) @ruanwenjun
- [Improvement-17506][dao] Add index on column workflow_definition_code for table t_ds_schedules to reduce time cost when access db (#17513) @unigof
- [Chore] Prevent NPE when handling zk connection events (#17526) @Mrhs121
- [Improvement-17480][Storage] Separate the local storage implementation from hdfs storage plugin (#17547) @ruanwenjun

</details>

## Bugfix

<details><summary>Click to expand</summary>

- [Fix-17473] [Task Plugin] Fix Aliyun SS task final state (#17475) @EricGao888
- [Fix-17469]Fix threadLocal will not clean if exception occur in LoginHandlerInterceptor  (#17474) @njnu-seafish
- [Fix-17436][Workflow]Task timeout kill throw exception (#17437) @njnu-seafish
- [Fix-17370] Fix worker server start failed when using hdfs storage type (#17496) @SbloodyS
- [Fix-17453] Fix TASK_ONLY strategy cannot work (#17461) @ruanwenjun
- [Fix-17477] Fix workflow can be deleted which contains failover instance (#17478) @ruanwenjun
- [Fix-17406]Fix Parameter passing feature is unavailable in SQL Task (#17456) @Zzih96
- [Fix-17413][DataSource][Hive&Spark]Principal field is not displayed and not used correctly in kerberos env (#17493) @njnu-seafish
- [Fix-17370][FOLLOWUP] Fix worker server start failed when using hdfs storage type (#17524) @Mrhs121
- [Fix-17520][TaskExecutor] fix not clear task exec path when set development.state=false in common.properties (#17523) @LourierL
- [Fix-17548] [Api] Sub WorkFlow Set Schedule Failed (#17549) @shangeyao
- [Fix-17555] [Master] TaskDispatchableEvent might block when the queue exist hight priority delay event (#17556) @ruanwenjun
- [Fix-17495] [Kubernetes] Fix configuration file mounting path issue (#17517) @cn-hew
- [Fix-17575][Workflow] Add a check for duplicate task names when saving or updating a workflow. (#17576) @njnu-seafish
- [Fix-17579][Workflow] fix view variable error after setting startup parameters for workflow instance (#17583) @Mrhs121

</details>

## Document

<details><summary>Click to expand</summary>

- [Chore] Fix doc deadlink error (#17466) @SbloodyS
- [Chore] fix k8s e2e (#17553) @Gallardot
- [Chore] Change version to 3.3.2 (#17602) @ruanwenjun

</details>

## Chore

<details><summary>Click to expand</summary>

- [Chore] Hotfix ci error (#17463) @SbloodyS
- [Chore] Fix zk repo (#17471) @Gallardot
- [Chore][CI] Fix flaky ci (#17479) @SbloodyS
- [Chore] Try to fix ci dead link check 429 (#17509) @SbloodyS
- [Chore] Hotfix CI error (#17545) @SbloodyS
- [Chore] Remove unused zt-zip lib (#17525) @ruanwenjun

</details>