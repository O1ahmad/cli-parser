# Volcano - v1.13.0

**Release Name**: v1.13.0
**Published**: 2025-09-29T11:40:54Z
**Repository**: https://github.com/volcano-sh/volcano

---

## What's New
Welcome to the v1.13.0 release of Volcano! 🚀 🎉 📣
In this release, we have brought a series of significant enhancements that have been long-awaited by community users: 

- **AI Training and Inference Enhancements** 
  - [Support LeaderWorkerSet for Large Model Inference Scenarios](#support-leaderworkerset-for-large-model-inference-scenarios)
  - [Introduce Cron VolcanoJob](#introduce-cron-volcanojob)
  - [Support Label-based HyperNode Auto Discovery](#support-label-based-hypernode-auto-discovery)
  - [Add Native Ray Framework Support](#add-native-ray-framework-support)
  - [Introduce HCCL Plugin Support](#introduce-hccl-plugin-support)


- **Resource Management and Scheduling Enhancements**
  - [Introduce ResourceStrategyFit Plugin](#introduce-resourcestrategyfit-plugin)
    - [Independent Scoring Strategy by Resource Type](#independent-scoring-strategy-by-resource-type)
    - [Scarce Resource Avoidance (SRA)](#scarce-resource-avoidance-sra)
  - [Enhance NodeGroup Functionality](#enhance-nodegroup-functionality)

- **Colocation Enhancements**
  - [Decouple Colocation from OS](#decouple-colocation-from-os)
  - [Support Custom OverSubscription Resource Names](#support-custom-oversubscription-resource-names)

## Support LeaderWorkerSet for Large Model Inference Scenarios

[LeaderWorkerSet (LWS)](https://github.com/kubernetes-sigs/lws) is an API for deploying a group of Pods on Kubernetes. It is primarily used to address multi-host inference in AI/ML inference workloads, especially scenarios that require sharding large language models (LLMs) and running them across multiple devices on multiple nodes.

Since its open-source release, Volcano has actively integrated with upstream and downstream ecosystems, building a comprehensive community ecosystem for batch computing such as AI and big data. In the [v0.7](https://github.com/kubernetes-sigs/lws/releases/tag/v0.7.0) release of LWS, it natively integrated Volcano's AI scheduling capabilities. When used with the new version of Volcano, LWS automatically creates PodGroups, which are then scheduled and managed by Volcano, thereby implementing advanced capabilities like Gang scheduling for large model inference scenarios.

Looking ahead, Volcano will continue to expand its ecosystem integration capabilities, providing robust scheduling and resource management support for more projects dedicated to enabling distributed inference on Kubernetes.

Usage documentation: [LeaderWorkerSet With Gang](https://github.com/kubernetes-sigs/lws/tree/main/docs/examples/sample/gang-scheduling).

Related PRs: https://github.com/kubernetes-sigs/lws/pull/496, https://github.com/kubernetes-sigs/lws/pull/498, @[JesseStutler](https://github.com/JesseStutler)

## Introduce Cron VolcanoJob

This release introduces support for Cron Volcano Jobs. Users can now periodically create and run Volcano Jobs based on a predefined schedule, similar to native Kubernetes CronJobs, to achieve periodic execution of batch computing tasks like AI and big data. Detailed features are as follows:

- **Scheduled Execution**: Define the execution cycle of jobs using standard Cron expressions (`spec.schedule`).
- **Timezone Support**: Set the timezone in `spec.timeZone` to ensure jobs execute at the expected local time.
- **Concurrency Policy**: Control concurrent behavior via `spec.concurrencyPolicy`:
  - `AllowConcurrent`: Allows concurrent execution of multiple jobs (default).
  - `ForbidConcurrent`: Skips the current scheduled execution if the previous job has not completed.
  - `ReplaceConcurrent`: Terminates the previous job if it is still running and starts a new one.
- **History Management**: Configure the number of successful (`successfulJobsHistoryLimit`) and failed (`failedJobsHistoryLimit`) job history records to retain; old jobs are automatically cleaned up.
- **Missed Schedule Handling**: The `startingDeadlineSeconds` field allows tolerating scheduling delays within a certain timeframe; timeouts are considered missed executions.
- **Status Tracking**: The CronJob status (`status`) tracks currently active jobs, the last scheduled time, and the last successful completion time for easier monitoring and management.

Related PRs: https://github.com/volcano-sh/apis/pull/192, https://github.com/volcano-sh/volcano/pull/4560, @[GoingCharlie](https://github.com/volcano-sh/volcano/commits?author=GoingCharlie), @[hwdef](https://github.com/hwdef), @[Monokaix](https://github.com/volcano-sh/volcano/commits?author=Monokaix)

Usage example: [Cron Volcano Job Example](https://github.com/volcano-sh/volcano/blob/master/example/cronjob/cronjob.yaml).

## Support Label-based HyperNode Auto Discovery

Volcano officially launched network topology-aware scheduling capability in v1.12 and pioneered the UFM auto-discovery mechanism based on InfiniBand (IB) networks. However, for hardware clusters that do not support IB networks or use other network architectures (such as Ethernet), manually maintaining the network topology remains cumbersome.

To address this issue, the new version introduces a Label-based HyperNode auto-discovery mechanism. This feature provides users with a universal and flexible way to describe network topology, transforming complex topology management tasks into simple node label management.

This mechanism allows users to define the correspondence between topology levels and node labels in the volcano-controller-configmap. The Volcano controller periodically scans all nodes in the cluster and automatically performs the following tasks based on their labels:

- **Automatic Topology Construction**: Automatically builds multi-layer HyperNode topology structures from top to bottom (e.g., rack -> switch -> node) based on a set of labels on the nodes.
- **Dynamic Maintenance**: When node labels change, or nodes are added or removed, the controller automatically updates the members and structure of the HyperNodes, ensuring the topology information remains consistent with the cluster state.
- **Support for Multiple Topology Types**: Allows users to define multiple independent network topologies simultaneously to adapt to different hardware clusters (e.g., GPU clusters, NPU clusters) or different network partitions.

Configuration example:

```yaml
# volcano-controller-configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: volcano-controller-configmap
  namespace: volcano-system
data:
  volcano-controller.conf: |
    networkTopologyDiscovery:
      - source: label
        enabled: true
        interval: 10m # Discovery interval
        config:
          networkTopologyTypes:
            # Define a topology type named topology-A
            topology-A:
              # Define topology levels, ordered from top to bottom
              - nodeLabel: "volcano.sh/hypercluster" # Top-level HyperNode
              - nodeLabel: "volcano.sh/hypernode"   # Middle-level HyperNode
              - nodeLabel: "kubernetes.io/hostname" # Bottom-level physical node
```

This feature is enabled by adding the label source to the Volcano controller's ConfigMap. The above configuration defines a three-layer topology structure named `topology-A`:

- Top Level (Tier 2): Defined by the `volcano.sh/hypercluster` label.
- Middle Level (Tier 1): Defined by the `volcano.sh/hypernode` label.
- Bottom Level: Physical nodes, identified by the Kubernetes built-in `kubernetes.io/hostname` label.

When a node is labeled as follows, it will be automatically recognized and classified into the topology path `cluster-s4 -> node-group-s0`:

```yaml
# Labels for node node-0
labels:
  kubernetes.io/hostname: node-0
  volcano.sh/hypernode: node-group-s0
  volcano.sh/hypercluster: cluster-s4
```

The label-based network topology auto-discovery feature offers excellent generality and flexibility. It is not dependent on specific network hardware (like IB), making it suitable for various heterogeneous clusters, and allows users to flexibly define hierarchical structures of any depth through labels. It automates complex topology maintenance tasks into simple node label management, significantly reducing operational costs and the risk of errors. Furthermore, this mechanism dynamically adapts to changes in cluster nodes and labels, maintaining the accuracy of topology information in real-time without manual intervention.

Related PR: https://github.com/volcano-sh/volcano/pull/4629, @[zhaoqi612](https://github.com/zhaoqi612)

Usage documentation: [HyperNode Auto Discovery](https://github.com/volcano-sh/volcano/blob/master/docs/user-guide/how_to_use_hypernode_auto_discovery.md).

## Add Native Ray Framework Support

[Ray](https://docs.ray.io/) is an open-source unified distributed computing framework whose core goal is to simplify parallel computing from single machines to large-scale clusters, especially suitable for scaling Python and AI applications. To manage and run Ray on Kubernetes, the community provides KubeRay—an operator specifically designed for Kubernetes. It acts as a bridge between Kubernetes and the Ray framework, greatly simplifying the deployment and management of Ray clusters and jobs.

Historically, running Ray workloads on Kubernetes primarily relied on the KubeRay Operator. KubeRay integrated Volcano in its [v0.4.0 release (released in 2022)](https://docs.ray.io/en/master/cluster/kubernetes/k8s-ecosystem/volcano.html) for scheduling and resource management of Ray Clusters, addressing issues like resource deadlocks in distributed training scenarios. With this new version of Volcano, users can now directly create and manage Ray clusters and submit computational tasks through native Volcano Jobs. This provides Ray users with an alternative usage scheme, allowing them to more directly utilize Volcano's capabilities such as Gang Scheduling, queue management and fair scheduling, and job lifecycle management for running Ray workloads.

Related PR: https://github.com/volcano-sh/volcano/pull/4581, @[Wonki4](https://github.com/Wonki4)

Design documentation: [Ray Framework Plugin Design Doc](https://github.com/volcano-sh/volcano/blob/master/docs/design/distributed-framework-plugins.md).

Usage documentation: [Ray Plugin User Guide](https://github.com/volcano-sh/volcano/blob/master/docs/user-guide/how_to_use_ray_plugin.md).

## Introduce HCCL Plugin Support

The new version adds an HCCL Rank plugin (`hcclrank`) to Volcano Jobs, used for automatically assigning HCCL Ranks to Pods in distributed tasks. This includes:

-   New implementation of the `hcclrank` plugin for Volcano Jobs, supporting automatic calculation and injection of HCCL Rank into Pod annotations based on task type (master/worker) and index.
-   The plugin supports custom master/worker task names, allowing users to specify the master/worker roles in distributed tasks.

This feature enhances Volcano's native support for HCCL communication scenarios, such as Huawei Ascend, facilitating automatic management and assignment of Ranks in AI training tasks.

Related PR: https://github.com/volcano-sh/volcano/pull/4524, @[kingeasternsun](https://github.com/kingeasternsun)

## Enhance NodeGroup Functionality

In hierarchical queue structures, repeatedly configuring the same node group affinity (`nodeGroupAffinity`) for each sub-queue as its parent queue leads to configuration redundancy and difficult maintenance.
To solve this problem, the Nodegroup plugin adds support for inheriting affinity within hierarchical queues. Once enabled, the scheduler resolves the effective affinity for a queue according to the following rules:

1.  **Prioritize Self-Configuration**: If the queue has defined `spec.affinity`, it uses this configuration directly.
2.  **Upward Inheritance**: If the queue has not defined `spec.affinity`, it searches upward through its parents and inherits the affinity configuration defined by the nearest ancestor queue.
3.  **Override Capability**: A child queue can override the inherited configuration by defining its own `spec.affinity`, ensuring flexibility.

This feature allows administrators to set unified node group affinity at a parent queue (e.g., department level), and all child queues (e.g., team level) will automatically inherit this setting, simplifying management.

For queues without NodeAffinity configuration, the "strict" parameter in the plugin controls scheduling behavior. When `strict` is set to `true` (the default value), tasks in these queues cannot be scheduled to any nodes. When `strict` is set to `false`, these tasks are allowed to be scheduled to regular nodes that do not have the `volcano.sh/nodegroup-name` label.

In the nodegroup plugin parameters of the scheduler configuration file, setting `enableHierarchy: true` enables hierarchical queue mode, and setting `strict: false` configures non-strict mode. Example configuration is as follows:

```yaml
actions: "allocate, backfill, preempt, reclaim"
tiers:
- plugins:
  - name: nodegroup
    arguments:
      enableHierarchy: true # Enable hierarchical support
      strict: false # Set to non-strict mode, allowing tasks in the queue to be scheduled to nodes without the "volcano.sh/nodegroup-name" label
```

Related PRs: https://github.com/volcano-sh/volcano/pull/4455, @[JesseStutler](https://github.com/JesseStutler), @[wuyueandrew](https://github.com/wuyueandrew)

NodeGroup design documentation: [NodeGroup Design.](https://github.com/volcano-sh/volcano/blob/master/docs/design/node-group.md)

NodeGroup usage documentation: [NodeGroup User Guide.](https://github.com/volcano-sh/volcano/blob/master/docs/user-guide/how_to_use_nodegroup_plugin.md)

## Introduce ResourceStrategyFit Plugin

In the native Kubernetes `noderesources` fit strategy, only a single aggregated (`MostAllocated`) or dispersed (`LeastAllocated`) strategy can be applied to all resources. This has limitations in complex heterogeneous computing environments (like AI/ML clusters). To meet differentiated scheduling requirements, Volcano introduces the enhanced `ResourceStrategyFit` plugin.
This plugin now integrates two core features: Independent scoring strategies by resource type and Scarce Resource Avoidance (SRA).

### Independent Scoring Strategy by Resource Type

This feature allows users to specify `MostAllocated` (binpack) or `LeastAllocated` (spread) strategies for different resources (e.g., cpu, memory, nvidia.com/gpu) independently, and assign different weights to them. The scheduler calculates the node score meticulously based on the independent configuration for each resource.

To simplify the management of resources within the same family (e.g., different model GPUs from the same vendor), this feature also supports suffix wildcard (`*`) matching for resource names.

-   **Syntax Rules**: Only suffix wildcards are supported, e.g., `nvidia.com/gpu/*`. Patterns like `*` or `vendor.*/gpu` are considered invalid.
-   **Matching Priority**: Uses the "longest prefix match" principle. Exact matches have the highest priority; when no exact match exists, the wildcard pattern with the longest prefix is selected.

Configuration Example: The following configuration sets a high-priority binpack strategy for a specific V100 GPU model, a generic binpack strategy for all other NVIDIA GPUs, and a spread strategy for CPU resources. Pod-level resource scoring strategy configuration is also supported.

```yaml
actions: "enqueue, allocate, backfill, reclaim, preempt"
tiers:
- plugins:
  - name: resource-strategy-fit
    arguments:
      resourceStrategyFitWeight: 10
      resources:
        # Exact match, highest priority
        nvidia.com/gpu-v100:
          type: MostAllocated
          weight: 3
        # Wildcard match, applies to all other NVIDIA GPUs
        nvidia.com/gpu/*:
          type: MostAllocated
          weight: 2
        # Exact match for CPU resource
        cpu:
          type: LeastAllocated
          weight: 1
```

### Scarce Resource Avoidance (SRA)

SRA is a "soft" strategy designed to improve the overall utilization of expensive or scarce resources (like GPUs). It influences node scoring to guide ordinary tasks that do not require specific scarce resources (e.g., CPU-only tasks) to avoid nodes containing those resources where possible. This helps "reserve" scarce resource nodes for tasks that truly need them, thereby reducing resource contention and task waiting time.

Mechanism:

1.  Users define a set of "scarce resources" (e.g., `nvidia.com/gpu`) in the configuration.
2.  When scheduling a Pod that does *not* request any of the defined scarce resources, the SRA policy takes effect.
3.  The scheduler reduces the score of nodes that possess these scarce resources. The more types of scarce resources a node has, the lower its score.
4.  For Pods that *do* request scarce resources, the SRA policy does not negatively impact their scheduling decisions.

Configuration Example: The following configuration defines `nvidia.com/gpu` as a scarce resource. When scheduling a CPU-only task, nodes with GPUs will have their scores reduced, making the task more likely to be scheduled onto nodes without GPUs.

```yaml
actions: "enqueue, allocate, backfill, reclaim, preempt"
tiers:
- plugins:
  - name: resource-strategy-fit
    arguments:
      # ... binpack/spread strategy configuration for resourceStrategyFit ...
      resources:
        nvidia.com/gpu:
          type: MostAllocated
          weight: 2
        cpu:
          type: LeastAllocated
          weight: 1
      # SRA policy configuration
      sra:
        enable: true
        resources: "nvidia.com/gpu" # Define scarce resource list, comma-separated
        weight: 10 # Weight of the SRA policy in the total score
        resourceWeight:
          nvidia.com/gpu: 1 # Define nvidia.com/gpu as a scarce resource and its weight
```

By combining the binpack/spread strategies of ResourceStrategyFit with the avoidance strategy of SRA, users can achieve more refined and efficient scheduling of heterogeneous resources.

Related PRs: https://github.com/volcano-sh/volcano/pull/4391, https://github.com/volcano-sh/volcano/pull/4454, https://github.com/volcano-sh/volcano/pull/4512, @[LY-today](https://github.com/LY-today), @[XbaoWu](https://github.com/XbaoWu), @[ditingdapeng](https://github.com/ditingdapeng), @[kingeasternsun](https://github.com/kingeasternsun)

Design documentation: [ResourceStrategyFit Design](https://github.com/volcano-sh/volcano/blob/master/docs/design/resource-strategy-fit-scheduling.md)
Usage documentation: [ResourceStrategyFit User Guide](https://github.com/volcano-sh/volcano/blob/master/docs/user-guide/how_to_use_resource_strategy_fit_plugin.md)

## Decouple Colocation from OS

Volcano's co-location capability consists of two parts: application-level and kernel-level. Application-level co-location provides unified scheduling for online and offline workloads, dynamic resource overcommitment, node pressure eviction, etc. Kernel-level co-location involves QoS guarantees for resources like CPU, Memory, and Network at the kernel level, which typically requires support from a specific OS (like OpenEuler). In the new version, Volcano decouples the co-location capability from the OS. For users using an OS that does not support kernel-level co-location, they can choose to use Volcano's application-level co-location capabilities to achieve unified scheduling of online and offline tasks, dynamic resource overcommitment, and high-priority task guarantees.

Specific usage: When installing the Volcano agent, specify the `--supported-features` parameter:

```shell
helm install volcano . --create-namespace -n volcano-system --set custom.colocation_enable=true --set "custom.agent_supported_features=OverSubscription\,Eviction\,Resources"
```

Related PRs: https://github.com/volcano-sh/volcano/pull/4409, https://github.com/volcano-sh/volcano/pull/4630, @[ShuhanYan](https://github.com/ShuhanYan), @[Monokaix](https://github.com/Monokaix)

Colocation documentation: https://volcano.sh/en/docs/colocation/

## Support Custom OverSubscription Resource Names

The Volcano co-location Agent adds parameters `--extend-resource-cpu-name` and `--extend-resource-memory-name`, allowing users to customize the names of overcommitted resources. This supports custom naming for CPU and memory resources (defaults are `kubernetes.io/batch-cpu` and `kubernetes.io/batch-memory` respectively), enhancing flexibility in setting overcommitted resource names.

Specific usage: When installing Volcano, specify the `--extend-resource-cpu-name` and `--extend-resource-memory-name` parameters:

```shell
helm install volcano . --create-namespace -n volcano-system --set custom.colocation_enable=true --set custom.agent_extend_resource_cpu_name=example.com/cpu --set custom.agent_extend_resource_memory_name=example.com/memory
```

Related PRs: https://github.com/volcano-sh/volcano/pull/4413, https://github.com/volcano-sh/volcano/pull/4630, @[ShuhanYan](https://github.com/ShuhanYan), @[Monokaix](https://github.com/Monokaix)

Colocation documentation: https://volcano.sh/en/docs/colocation/

## Add Kubernetes 1.33 Support

The Volcano version keeps pace with the Kubernetes community releases. v1.13 supports the latest Kubernetes v1.33 release, ensuring functionality and reliability through comprehensive UT and E2E test cases.

For participating in Volcano's adaptation work for new Kubernetes versions, refer to: [adapt-k8s-todo](https://github.com/volcano-sh/volcano/blob/v1.13.0/docs/design/adapt-k8s-todo.md).

Related PR: https://github.com/volcano-sh/volcano/pull/4430, @[mahdikhashan](https://github.com/mahdikhashan)

## Overall Changes
* Support topology aware in the preempt action by @bibibox in https://github.com/volcano-sh/volcano/pull/4279
* Move InitCycleState from openSession to OpenSession by @ElectricFish7 in https://github.com/volcano-sh/volcano/pull/4378
* fix: Node resource topology awareness, stop scheduling and notReady by @LY-today in https://github.com/volcano-sh/volcano/pull/4373
* Support the allocation callback function provided by the extender. by @zhifei92 in https://github.com/volcano-sh/volcano/pull/4377
* Delete secrets permission for volcano agent by @JesseStutler in https://github.com/volcano-sh/volcano/pull/4389
* [Automation Enhancement] Update cherry-pick shell and add cherry-pick guide doc by @JesseStutler in https://github.com/volcano-sh/volcano/pull/4366
* [Automation Enhancement]: Add bump version script; Make version release more automated by @JesseStutler in https://github.com/volcano-sh/volcano/pull/4372
* fix incorrect scheduler log by @archlitchi in https://github.com/volcano-sh/volcano/pull/4419
* fix: rolling restart admission webhooks after helm upgrade by @junzebao in https://github.com/volcano-sh/volcano/pull/4396
* Only refresh podgroup to running when pods are scheduled by @JesseStutler in https://github.com/volcano-sh/volcano/pull/4384
* Fix panic while `vcctl queue list` after podgroups' queue was deleted by @halcyon-r in https://github.com/volcano-sh/volcano/pull/4428
* When some scalar resources are 0 in deserved, hierarychical queues validation can not pass by @JesseStutler in https://github.com/volcano-sh/volcano/pull/4347
* Move kube-scheduler related metrics initilization to server.go to avoid panic by @JesseStutler in https://github.com/volcano-sh/volcano/pull/4422
* fix: add ResourceStrategyFit plugin by @LY-today in https://github.com/volcano-sh/volcano/pull/4391
* [feature] upgrade k8s to v1.33.2 by @mahdikhashan in https://github.com/volcano-sh/volcano/pull/4430
* Update volcano author copyright header by @JesseStutler in https://github.com/volcano-sh/volcano/pull/4379
* Add support for skipping handler registration and QoS manager initialization based on configuration in Volcano Agent by @ShuhanYan in https://github.com/volcano-sh/volcano/pull/4409
* [doc] Jobflow parameter overrides by @mahdikhashan in https://github.com/volcano-sh/volcano/pull/4411
* Support for configurable extended resource names in volcano agent by @ShuhanYan in https://github.com/volcano-sh/volcano/pull/4413
* Fix:  Sync Jobflow status with vcjob Status Terminated by @dongjiang1989 in https://github.com/volcano-sh/volcano/pull/4443
* Correct step order to enable caching in E2E workflows by @GautamBytes in https://github.com/volcano-sh/volcano/pull/4464
* fix enable node device score plugin by @coldzerofear in https://github.com/volcano-sh/volcano/pull/4340
* Fix the issue where SelectBestNode returns nil when plugin scores are… by @guoqinwill in https://github.com/volcano-sh/volcano/pull/4445
* [Cherry-pick master] Check queue spec to ensure the rationality of resource size by @XbaoWu in https://github.com/volcano-sh/volcano/pull/4470
* fix: Volcano scheduler panic when scheduling Pods with delayed binding PVCs by @ouyangshengjia in https://github.com/volcano-sh/volcano/pull/4484
* fix node count reconcile by @Monokaix in https://github.com/volcano-sh/volcano/pull/4473
* Fix incorrect definition of `ReleaseNameEnvKey` by @ouyangshengjia in https://github.com/volcano-sh/volcano/pull/4486
* Add missing capacity metrics in hierarchical queues by @JesseStutler in https://github.com/volcano-sh/volcano/pull/4487
* Support configuring resources managed by the extender by @zhifei92 in https://github.com/volcano-sh/volcano/pull/4482
* Set root capability only when user not set it by @houyuting in https://github.com/volcano-sh/volcano/pull/4354
* Bump github.com/onsi/gomega from 1.35.1 to 1.38.0 by @dependabot[bot] in https://github.com/volcano-sh/volcano/pull/4495
* inherit non-existent scalar resources from the parent queue by @lhlxc in https://github.com/volcano-sh/volcano/pull/4504
* Fix volume binding e2e testing by @JesseStutler in https://github.com/volcano-sh/volcano/pull/4483
* fix #4499: scheduler panic caused by pod using gpu-number scheduled by volcano with old version (e.g v1.7) by @linuxfhy in https://github.com/volcano-sh/volcano/pull/4500
* test: add e2e test cases for hypernode by @Xu-Wentao in https://github.com/volcano-sh/volcano/pull/3983
* fix#4497: hypernode update bug by @cyf-2002 in https://github.com/volcano-sh/volcano/pull/4498
* Integrate with leaderworkerset: Volcano controller doesn't need to create podgroup for statefulset if statefulset pods have associated podgroup by @JesseStutler in https://github.com/volcano-sh/volcano/pull/4478
* fix: update podGroup when statefulSet update by @Poor12 in https://github.com/volcano-sh/volcano/pull/4517
* fix: deepcopy podgroup before update by @Poor12 in https://github.com/volcano-sh/volcano/pull/4526
* Fix dra flaky test: use `exec env` instead logs by @JesseStutler in https://github.com/volcano-sh/volcano/pull/4531
* ✨  add hcclrank job plugin by @kingeasternsun in https://github.com/volcano-sh/volcano/pull/4524
* add kingeasternsun as  reviewer by @kingeasternsun in https://github.com/volcano-sh/volcano/pull/4561
* Fix panic in job controller's killPods action by @neo502721 in https://github.com/volcano-sh/volcano/pull/4569
* Add permissions for managing namespaces in admission rules by @suyiiyii in https://github.com/volcano-sh/volcano/pull/4590
* Revert "fix: Node resource topology awareness, stop scheduling and notReady" by @dafu-wu in https://github.com/volcano-sh/volcano/pull/4575
* Minor docs changes  by @hajnalmt in https://github.com/volcano-sh/volcano/pull/4587
* Fix queue not counting volcano.sh/vgpu-memory and volcano.sh/vgpu-number properly by @archlitchi in https://github.com/volcano-sh/volcano/pull/4520
* feat: support wildcard syntax in resource-strategy-fit plugin by @ditingdapeng in https://github.com/volcano-sh/volcano/pull/4512
* use node.futureidle instead when pod has nominatedNodeName by @Monokaix in https://github.com/volcano-sh/volcano/pull/4588
* network topology aware hard mode support hypernode binpack by @kingeasternsun in https://github.com/volcano-sh/volcano/pull/4345
* Sync kube-scheduler: Improve CSILimits plugin accuracy by using VolumeAttachments by @guoqinwill in https://github.com/volcano-sh/volcano/pull/4608
* 🐛  fix mpi job plugin panic when mpi job only has master task by @kingeasternsun in https://github.com/volcano-sh/volcano/pull/4610
* Fix an issue in vc-scheduler about vgpu device memory allocated by @archlitchi in https://github.com/volcano-sh/volcano/pull/4615
* feat: add detail msg for pg event by @Poor12 in https://github.com/volcano-sh/volcano/pull/4544
* Cleanup: update MAINTAINERS.md with latest content location by @kevin-wangzefeng in https://github.com/volcano-sh/volcano/pull/4622
* Expose more helm config for agent by @Monokaix in https://github.com/volcano-sh/volcano/pull/4630
* Add hierarchical queue support for nodegroup plugin by @JesseStutler in https://github.com/volcano-sh/volcano/pull/4455
* fix: address remaining review comments from PR #4457 for ResourceStrategyFit plugin by @ditingdapeng in https://github.com/volcano-sh/volcano/pull/4635
* fix: fix ResourceStrategyFit plugin by @LY-today in https://github.com/volcano-sh/volcano/pull/4457
* feat: add cron volcano job by @GoingCharlie in https://github.com/volcano-sh/volcano/pull/4560
* feat: add ray plugin for job by @Wonki4 in https://github.com/volcano-sh/volcano/pull/4581
* Add sra policy for ResourceStrategyFit Plugin by @XbaoWu in https://github.com/volcano-sh/volcano/pull/4454
* Support identifying network topology from node labels and converted i… by @zhaoqi612 in https://github.com/volcano-sh/volcano/pull/4629
* Enhance README formatting with note callouts by @huntersman in https://github.com/volcano-sh/volcano/pull/4623
* Free up disk space by @Monokaix in https://github.com/volcano-sh/volcano/pull/4642
* fix: report all scalar metrics for each queue by @hajnalmt in https://github.com/volcano-sh/volcano/pull/4599
* Support configuring network-topology via pod annotations by @zhifei92 in https://github.com/volcano-sh/volcano/pull/4583
* Fix panic on volcano-vgpu when allocating multiple containers in a pod by @archlitchi in https://github.com/volcano-sh/volcano/pull/4633
* feat(resource-strategy-fit): add per-Pod scoring strategy by @kingeasternsun in https://github.com/volcano-sh/volcano/pull/4641
* Fix bump version script by @JesseStutler in https://github.com/volcano-sh/volcano/pull/4519
* Add nodegroup nonstrict mode by @JesseStutler in https://github.com/volcano-sh/volcano/pull/4652
* add nodegroup nonstrict to fit 0nodes queue by @wuyueandrew in https://github.com/volcano-sh/volcano/pull/4602
* Revise the user documentation for hypernode auto discovery by @zhaoqi612 in https://github.com/volcano-sh/volcano/pull/4654
* Automated: Bump version to v1.13.0 by @JesseStutler in https://github.com/volcano-sh/volcano/pull/4655

## New Contributors
* @ElectricFish7 made their first contribution in https://github.com/volcano-sh/volcano/pull/4378
* @zhifei92 made their first contribution in https://github.com/volcano-sh/volcano/pull/4377
* @junzebao made their first contribution in https://github.com/volcano-sh/volcano/pull/4396
* @ShuhanYan made their first contribution in https://github.com/volcano-sh/volcano/pull/4409
* @GautamBytes made their first contribution in https://github.com/volcano-sh/volcano/pull/4464
* @coldzerofear made their first contribution in https://github.com/volcano-sh/volcano/pull/4340
* @houyuting made their first contribution in https://github.com/volcano-sh/volcano/pull/4354
* @lhlxc made their first contribution in https://github.com/volcano-sh/volcano/pull/4504
* @cyf-2002 made their first contribution in https://github.com/volcano-sh/volcano/pull/4498
* @neo502721 made their first contribution in https://github.com/volcano-sh/volcano/pull/4569
* @suyiiyii made their first contribution in https://github.com/volcano-sh/volcano/pull/4590
* @dafu-wu made their first contribution in https://github.com/volcano-sh/volcano/pull/4575
* @ditingdapeng made their first contribution in https://github.com/volcano-sh/volcano/pull/4512
* @GoingCharlie made their first contribution in https://github.com/volcano-sh/volcano/pull/4560
* @Wonki4 made their first contribution in https://github.com/volcano-sh/volcano/pull/4581
* @zhaoqi612 made their first contribution in https://github.com/volcano-sh/volcano/pull/4629
* @huntersman made their first contribution in https://github.com/volcano-sh/volcano/pull/4623

**Full Changelog**: https://github.com/volcano-sh/volcano/compare/v1.12.2...v1.13.0