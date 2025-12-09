# Koordinator - v1.7.0

**Release Name**: v1.7.0
**Published**: 2025-10-23T13:45:01Z
**Repository**: https://github.com/koordinator-sh/koordinator

---

## What's Changed
* koordlet: support init container for CPUSetAllocator by @zwzhang0107 in https://github.com/koordinator-sh/koordinator/pull/2349
* fix(scheduler/api): register missing NodeResourcesFitPlusArgs in v1 c… by @ditingdapeng in https://github.com/koordinator-sh/koordinator/pull/2353
* scheduler: optimize nodeNUMAResource performance by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2356
* scheduler: fix numaNodeResource not reserve cpu by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2355
* koordlet: skip reconcile containers in runtime hooks for kata pods by @zwzhang0107 in https://github.com/koordinator-sh/koordinator/pull/2357
* scheduler: inplace update quota when quota parent change by @shaloulcy in https://github.com/koordinator-sh/koordinator/pull/2351
* scheduler: update quota tree when quota spec changed by @shaloulcy in https://github.com/koordinator-sh/koordinator/pull/2358
* chore: refactor ReservationOwnerMatcher func by @googs1025 in https://github.com/koordinator-sh/koordinator/pull/2359
* scheduler: pre-calculate reservation info for perf by @saintube in https://github.com/koordinator-sh/koordinator/pull/2366
* koordlet: BECPUSuppress supports cpuSuppressMinPercent by @saintube in https://github.com/koordinator-sh/koordinator/pull/2369
* scheduler: make Activate invokable by handle by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2372
* chore: move SetReservationUnschedulable func to util package by @googs1025 in https://github.com/koordinator-sh/koordinator/pull/2362
* feature(GCmetrics): support GCHistogramVec for util package by @googs1025 in https://github.com/koordinator-sh/koordinator/pull/2382
* feat(koordlet): Add pod evict metrics by kill containers by @dongjiang1989 in https://github.com/koordinator-sh/koordinator/pull/2388
* fix(koordlet):BlkIOReconcile plugin not using WaitForCacheSync method correctly to synchronize by @googs1025 in https://github.com/koordinator-sh/koordinator/pull/2386
* scheduler: add log for diagnosize by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2397
* scheduler: add elasticquota ForgetPod, enable lazyreservationrestore for preferred topologyspread by @saintube in https://github.com/koordinator-sh/koordinator/pull/2394
* chore: update actions runner image  to Ubuntu 22.04 by @dongjiang1989 in https://github.com/koordinator-sh/koordinator/pull/2396
* apis: add default Pending phase when creating reservation by @googs1025 in https://github.com/koordinator-sh/koordinator/pull/2390
* scheduler: add metrics for elastic quota and refact UpdateQuota by @shaloulcy in https://github.com/koordinator-sh/koordinator/pull/2392
* scheduler: reduce loadaware lock overhead, improve reservation args by @saintube in https://github.com/koordinator-sh/koordinator/pull/2399
* scheduler: add ReservationStatusPhase metrics for reservation feature by @googs1025 in https://github.com/koordinator-sh/koordinator/pull/2368
* chore: fix wrong reservation phase in unit test by @googs1025 in https://github.com/koordinator-sh/koordinator/pull/2403
* webhook: add error info when failed to check sub and parent group quo… by @lijunxin559 in https://github.com/koordinator-sh/koordinator/pull/2406
* scheduler: support DispenseWithLRNDeviceAllocation by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2410
* koordlet: add resctrl qos collector by @Rouzip in https://github.com/koordinator-sh/koordinator/pull/2005
* scheduler: add OmitNodeLabelsForReservation, expose GetQuotaInformer by @saintube in https://github.com/koordinator-sh/koordinator/pull/2412
* koord-descheduler: add nil check for podMetric in NodeFit of loadaware plugin by @ClanEver in https://github.com/koordinator-sh/koordinator/pull/2405
* scheduler: fix reservation cache leak when terminated and deleted by @saintube in https://github.com/koordinator-sh/koordinator/pull/2416
* scheduler: Add gcDurationSeconds field to ReservationArgs by @googs1025 in https://github.com/koordinator-sh/koordinator/pull/2402
* webhook: check quota that only allow max >= used for specific resources by @zheng-weihao in https://github.com/koordinator-sh/koordinator/pull/2409
* scheduler: change quota info to rw lock by @shaloulcy in https://github.com/koordinator-sh/koordinator/pull/2421
* scheduler: rename leastRequestedScore func by @googs1025 in https://github.com/koordinator-sh/koordinator/pull/2422
* scheduler: optimize secondary device well planned by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2425
* scheduler: avoid string concatenation and podLister in loadaware func… by @lijunxin559 in https://github.com/koordinator-sh/koordinator/pull/2424
* scheduler: optimize filterNodeDevice by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2428
* scheduler: correct secondaryDeviceNotWellPlanned metric by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2431
* scheduler: remove Duplicate goroutines and remove Deprecated poll func by @googs1025 in https://github.com/koordinator-sh/koordinator/pull/2429
* chore: update EnableRuntimeQuota param description by @cntigers in https://github.com/koordinator-sh/koordinator/pull/2434
* scheduler: fix shared gpu binpack bug by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2436
* descheduler: return the unmatched cases first by @googs1025 in https://github.com/koordinator-sh/koordinator/pull/2435
* chore(statesInformer):  remove useless code and use generateQueryDuration() func in collectMetric() func by @googs1025 in https://github.com/koordinator-sh/koordinator/pull/2439
* scheduler: support multi-scheduler by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2441
* scheduler: fix CheckParentQuota bug when multiquotatree by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2442
* e2e: disable LoadAware Filter to fix flaky test by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2448
* scheduler: abstract nextPod and gang inplements it by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2417
* chore: qos manager removes repeat goroutine by @googs1025 in https://github.com/koordinator-sh/koordinator/pull/2437
* scheduler: add QuotaHookPlugin for extensible resource limiting in ElasticQuota plugin by @TaoYang526 in https://github.com/koordinator-sh/koordinator/pull/2415
* scheduler: add ElasticQuota arg to control preemption of default quota (#2413) by @LennonChin in https://github.com/koordinator-sh/koordinator/pull/2449
* scheduler: fix calFreeWithPreemptible modify nodeDevice by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2453
* scheduler: allow to disable Controllers by @saintube in https://github.com/koordinator-sh/koordinator/pull/2452
* scheduler: gpuSharedPod doesn't fit secondaryDeviceWellPlanned by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2454
* chore: refactor ValidateNodeNUMAResourceArgs func and add miss NUMAScoringStrategy validate by @googs1025 in https://github.com/koordinator-sh/koordinator/pull/2426
* chore: rename validateEstimatedResourceThresholds -> validateEstimatedScalingFactors by @googs1025 in https://github.com/koordinator-sh/koordinator/pull/2427
* scheduler: fix noisy monitor timeout for unhandled dequeue pod by @saintube in https://github.com/koordinator-sh/koordinator/pull/2458
* scheduler: change elastic quota Reserve/Unreserve lock by @shaloulcy in https://github.com/koordinator-sh/koordinator/pull/2456
* all: enhance colocation profile by @saintube in https://github.com/koordinator-sh/koordinator/pull/2445
* koordlet: support extension controllers by @shaloulcy in https://github.com/koordinator-sh/koordinator/pull/2459
* scheduler: run pod-update hooks for elastic-quota regardless of whether used resources have changed by @TaoYang526 in https://github.com/koordinator-sh/koordinator/pull/2461
* scheduler: add FG validatingPodDeviceResource and EnableSyncGPUShared… by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2466
* scheduler: Add hook plugins logic in ReplaceQuotas and OnQuotaUpdate methods of ElasticQuota plugin. by @TaoYang526 in https://github.com/koordinator-sh/koordinator/pull/2465
* scheduler: make loadaware debuggable by @saintube in https://github.com/koordinator-sh/koordinator/pull/2468
* scheduler: fix data race issues in GroupQuotaManager#IsQuotaUpdated and MockHookPlugin by @TaoYang526 in https://github.com/koordinator-sh/koordinator/pull/2469
* manager: reconcile colocation-profile if enabled by @saintube in https://github.com/koordinator-sh/koordinator/pull/2472
* proposal: heterogeneous GPU device reporting by @ZhuZhezz in https://github.com/koordinator-sh/koordinator/pull/2423
* scheduler: fine-grained device scheduling support Huawei Ascend NPU (full card) by @zqzten in https://github.com/koordinator-sh/koordinator/pull/2467
* koord-descheduler: support node selector for each descheduler profile by @songtao98 in https://github.com/koordinator-sh/koordinator/pull/2168
* koord-descheduler: fix descheduler object limiter with multiple profiles by @songtao98 in https://github.com/koordinator-sh/koordinator/pull/2200
* scheduler: fix quota webhook panic by @shaloulcy in https://github.com/koordinator-sh/koordinator/pull/2473
* scheduler: fix runtime not updated when no pending pods in quota by @qinfustu in https://github.com/koordinator-sh/koordinator/pull/2471
* scheduler: fix PreBind Patch for pods with same name but different uid by @saintube in https://github.com/koordinator-sh/koordinator/pull/2476
* scheduler: reject schedulerName unmatched binding by @saintube in https://github.com/koordinator-sh/koordinator/pull/2478
* koordlet: fix avg not being collected in AggregatedUsage by @ClanEver in https://github.com/koordinator-sh/koordinator/pull/2479
* chore: fix wrong event type by @googs1025 in https://github.com/koordinator-sh/koordinator/pull/2444
* scheduler: fix nodeName filter fail by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2482
* koordlet: fix resctrl metric releated flags's comment. by @dabaooline in https://github.com/koordinator-sh/koordinator/pull/2483
* scheduler: revise PreBind safe Patch by @saintube in https://github.com/koordinator-sh/koordinator/pull/2485
* scheduler: indicates X-th member pod failed when gangScheduling by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2486
* scheduler: support leave allocate logic to kubelet by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2487
* fix: GetLocalStorageInfo maybe hang by @dabaooline in https://github.com/koordinator-sh/koordinator/pull/2484
* scheduler: revise event handlers for updating scheduler name by @saintube in https://github.com/koordinator-sh/koordinator/pull/2488
* scheduler: put Coscheduling postFilter logic in afterPostFilter by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2490
* all: fix switching schedulers by @saintube in https://github.com/koordinator-sh/koordinator/pull/2493
* scheduler: set PodGroup's OccupiedBy field  correctly by @googs1025 in https://github.com/koordinator-sh/koordinator/pull/2494
* scheduler: fix pod not update in nextpod by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2495
* scheduler: use RWMutex instead of Mutex by @googs1025 in https://github.com/koordinator-sh/koordinator/pull/2497
* descheduler: fix podFitsAnyNodeWithThreshold when node not fit pod by @dabaooline in https://github.com/koordinator-sh/koordinator/pull/2492
* scheduler: fine-grained device scheduling support Huawei Ascend vNPU by @zqzten in https://github.com/koordinator-sh/koordinator/pull/2496
* scheduler: introduce gpu minors annotation to device plugin adapter by @zqzten in https://github.com/koordinator-sh/koordinator/pull/2504
* manager: colocationprofile support appending label suffix by @saintube in https://github.com/koordinator-sh/koordinator/pull/2503
* chores: update community meeting information by @songtao98 in https://github.com/koordinator-sh/koordinator/pull/2505
* manager: fix typo for colocationprofile by @saintube in https://github.com/koordinator-sh/koordinator/pull/2506
* scheduler: add koordinator.sh/gpu-memory to default device share scoring strategy resources by @zqzten in https://github.com/koordinator-sh/koordinator/pull/2507
* scheduler: revise preEnqueue RepresentativePod by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2509
* scheduler: mark gangGroupScheduling with startTime and fix pod status by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2512
* koordlet: remove qos module by @Rouzip in https://github.com/koordinator-sh/koordinator/pull/2440
* koordlet(statesinformer): sort podsMetricInfo and hostAppMetricInfo by name for consistent output by @googs1025 in https://github.com/koordinator-sh/koordinator/pull/2510
* scheduler: fix unhandled timeout in SchedulerMonitor by @saintube in https://github.com/koordinator-sh/koordinator/pull/2518
* manager: Optimize ConfigMap update event handling by reordering checks by @googs1025 in https://github.com/koordinator-sh/koordinator/pull/2511
* koord-descheduler: use RWMutex instead of use Mutex by @googs1025 in https://github.com/koordinator-sh/koordinator/pull/2514
* Update descheduler approvers by @songtao98 in https://github.com/koordinator-sh/koordinator/pull/2520
* scheduler: add pre-allocation api, revise reservation interfaces by @saintube in https://github.com/koordinator-sh/koordinator/pull/2513
* koordlet: adding cpu.max.burst comments by @bobsongplus in https://github.com/koordinator-sh/koordinator/pull/2524
* colocationprofile: support namespace selector for ClusterColocationProfile in controller by @googs1025 in https://github.com/koordinator-sh/koordinator/pull/2522
* webhook: add more info when deleting quota failed by @googs1025 in https://github.com/koordinator-sh/koordinator/pull/2519
* scheduler: add loadaware plugins Aggregated Args Validate by @googs1025 in https://github.com/koordinator-sh/koordinator/pull/2527
* proposal: network topology aware scheduling by @yccharles in https://github.com/koordinator-sh/koordinator/pull/2474
* scheduler: fix flaky test by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2532
* scheduler: loadaware support force estimated duration and other improvements by @zheng-weihao in https://github.com/koordinator-sh/koordinator/pull/2531
* remove inactive approve to smooth review process by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2534
* koordlet: fix Histogram maxValue error by @cntigers in https://github.com/koordinator-sh/koordinator/pull/2540
* scheduler: add ElasticQuota arg to control MinQuotaScale by @qinfustu in https://github.com/koordinator-sh/koordinator/pull/2542
* scheduler: only requeue gang when gangWorth and by activate by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2537
* koord-manager: support enhanced validation for pod by @TaoYang526 in https://github.com/koordinator-sh/koordinator/pull/2462
* scheduler: fix missing Unreserve when ResizePod=true by @saintube in https://github.com/koordinator-sh/koordinator/pull/2544
* scheduler: fix the noderesourcefitplus plugin does not implement the LocalStorageCapacityIsolation FeatureGate by @qinfustu in https://github.com/koordinator-sh/koordinator/pull/2536
* scheduler: fix panic on reserve pod scheduling failure by @saintube in https://github.com/koordinator-sh/koordinator/pull/2549
* scheduler: fix after deleting an ElasticQuota, its associated metrics can still be queried by @qinfustu in https://github.com/koordinator-sh/koordinator/pull/2516
* scheduler: add ReservationResourceAllocated metrics in reservation controller by @googs1025 in https://github.com/koordinator-sh/koordinator/pull/2533
* cmd: refactor SecureServing.Serve return in scheduler and descheduler by @googs1025 in https://github.com/koordinator-sh/koordinator/pull/2551
* scheduler: move DevicePluginAdaption to correct feature gates by @zqzten in https://github.com/koordinator-sh/koordinator/pull/2554
* scheduler: handle cache.DeletedFinalStateUnknown event in quota controller handler by @googs1025 in https://github.com/koordinator-sh/koordinator/pull/2543
* scheduler: loadaware fix cache for pod conditions changed by @zheng-weihao in https://github.com/koordinator-sh/koordinator/pull/2555
* scheduler: plugin register forgetpod by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2556
* qosmanager: add IsPodInactive to check if pod is not in Pending/Running phase and unit test by @googs1025 in https://github.com/koordinator-sh/koordinator/pull/2550
* koordlet: support heterogeneous GPU device reporting by @ZhuZhezz in https://github.com/koordinator-sh/koordinator/pull/2501
* koordlet: fix generateQueryDuration calculation by @zwzhang0107 in https://github.com/koordinator-sh/koordinator/pull/2567
* koordlet: fix collectMetric() panic when nodeSLO is nil by @googs1025 in https://github.com/koordinator-sh/koordinator/pull/2573
* scheduler: Reservation skips fitsNode to deduplicate with NodeResourceFit by @saintube in https://github.com/koordinator-sh/koordinator/pull/2576
* scheduler: clean expired ReservationAllocated for pods when reservation deleted by @saintube in https://github.com/koordinator-sh/koordinator/pull/2575
* scheduler: support pre-allocation filter by @saintube in https://github.com/koordinator-sh/koordinator/pull/2571
* scheduler: during scheduling, it must consider whether hami-core is installed on the nodes by @qinfustu in https://github.com/koordinator-sh/koordinator/pull/2577
* fix: podGroup not add to queue when pg not fount in PodGroupControlle… by @yccharles in https://github.com/koordinator-sh/koordinator/pull/2580
* chore: fix typo for RegisterTypeNodeMetadata by @qingyuanz in https://github.com/koordinator-sh/koordinator/pull/2584
* webhook: fix elasticquota validation error for min > max by @zheng-weihao in https://github.com/koordinator-sh/koordinator/pull/2586
* koordlet: support enhanced group identity for gpu by @saintube in https://github.com/koordinator-sh/koordinator/pull/2583
* scheduler: preprocess unmatch reservation's allocated by @saintube in https://github.com/koordinator-sh/koordinator/pull/2589
* manager: support batch resource limit of nodeCapacity by @lijunxin559 in https://github.com/koordinator-sh/koordinator/pull/2588
* apis: adapt to both v1alpha1&v1alpha2 noderesourcetopology by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2593
* scheduler: collect schedule pod result in metrics by @zheng-weihao in https://github.com/koordinator-sh/koordinator/pull/2585
* scheduler: add pre-allocation nominator by @saintube in https://github.com/koordinator-sh/koordinator/pull/2592
* koordlet: fix typo and add memory-ratio resource for buildXPUDevice() by @ZhuZhezz in https://github.com/koordinator-sh/koordinator/pull/2599
* scheduler: don't invoke SnapshotSharedLister in parallizer by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2600
* scheduler: add questionedObjectKet and topologyKeyToExplain by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2601
* apis: add scheduleExplanation CRD by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2602
* scheduler: improve load aware perf by resources cache and vectorization by @zheng-weihao in https://github.com/koordinator-sh/koordinator/pull/2582
* koordlet: fix koordlet panic randomly,caused by node info not ready by @yyrdl in https://github.com/koordinator-sh/koordinator/pull/2597
* scheduler: loadaware support dominantResourceWeight by @zheng-weihao in https://github.com/koordinator-sh/koordinator/pull/2603
* koordlet: fix path for sched_idle_saver_wmark by @saintube in https://github.com/koordinator-sh/koordinator/pull/2611
* scheduler: takeover nominatingInfo when waitingPod rejected by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2613
* koordlet: avoid create multi nri connection by @yyrdl in https://github.com/koordinator-sh/koordinator/pull/2617
* scheduler: make customized workflow by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2618
* koordlet: fix typo and update xpu condition/partition by @ZhuZhezz in https://github.com/koordinator-sh/koordinator/pull/2619
* scheduler: add diagnosis api by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2607
* scheduler: fine-grained device scheduling support Cambricon dynamic sMLU by @zqzten in https://github.com/koordinator-sh/koordinator/pull/2624
* scheduler: remove unused apis/util by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2627
* scheduler: don't invoke SnapshotSharedLister in parallizer by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2625
* scheduler: support ignore nominatedPods of same job by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2628
* scheduler: distinguish preemption failure&success in nominatingInfo by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2629
* koordlet: add mainline kernel support for IsCoreSchedSupported() by @hwenwur in https://github.com/koordinator-sh/koordinator/pull/2621
* scheduler: fix deviceShare UT by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2631
* scheduler: support customize preemption diagnosis by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2632
* all: provides vGPU allocation and utilization metrics by @qinfustu in https://github.com/koordinator-sh/koordinator/pull/2578
* scheduler: support job-level preemption by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2622
* koordlet: fix correct the default value of RuntimeHooksNRIPluginName by @qinfustu in https://github.com/koordinator-sh/koordinator/pull/2635
* scheduler: fill scheduleDiagnosis when pod or gang by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2634
* koordlet: fix resctrl cachable updates and core sched UTs by @saintube in https://github.com/koordinator-sh/koordinator/pull/2637
* koordlet: fix partition in buildXPUDeviceAnnotations() by @ZhuZhezz in https://github.com/koordinator-sh/koordinator/pull/2636
* scheduler: revise custom workflow and some helpers by @saintube in https://github.com/koordinator-sh/koordinator/pull/2640
* koordlet: Set HostToContainer propagation for kubelet dir by @hkttty2009 in https://github.com/koordinator-sh/koordinator/pull/2641
* scheduler: enhance framework extender for multi-scheduler by @saintube in https://github.com/koordinator-sh/koordinator/pull/2642
* koord-device-daemon: report device infos (xpu/npu/mlu) by @ZhuZhezz in https://github.com/koordinator-sh/koordinator/pull/2623
* device-daemon: add release by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2644
* scheduler: add scheduling hint by @saintube in https://github.com/koordinator-sh/koordinator/pull/2645
* scheduler: tweak sort device by preferred pcie by @zqzten in https://github.com/koordinator-sh/koordinator/pull/2646
* scheduler: support network topology aware coscheduling by @zqzten in https://github.com/koordinator-sh/koordinator/pull/2638
* scheduler: fix nominated reservation during preemption by @saintube in https://github.com/koordinator-sh/koordinator/pull/2647
* scheduler: tweak dp adapter node lock by @zqzten in https://github.com/koordinator-sh/koordinator/pull/2648
* koordlet: exclude device NUMANode by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2650
* scheduler: fix panic for reservation handler by @saintube in https://github.com/koordinator-sh/koordinator/pull/2652
* chore: revise go.mod by @saintube in https://github.com/koordinator-sh/koordinator/pull/2654
* scheduler: support allocated by desinated resource by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2653
* scheduler: pre-bind with gang info by @saintube in https://github.com/koordinator-sh/koordinator/pull/2655
* scheduler: add scheduling hint plugin by @saintube in https://github.com/koordinator-sh/koordinator/pull/2657
* koordlet: support batch pod eviction triggered by node usage by @lijunxin559 in https://github.com/koordinator-sh/koordinator/pull/2610
* koordlet: fix SysHasGenericInitiator path by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2656
* chore: revise go.mod by @saintube in https://github.com/koordinator-sh/koordinator/pull/2658
* koordlet: read rdma minor from ibdev and add rdma health status by @ZhuZhezz in https://github.com/koordinator-sh/koordinator/pull/2659
* scheduler: improve ut for network-topology aware scheduling by @ZiMengSheng in https://github.com/koordinator-sh/koordinator/pull/2661
* scheduler: coscheduling tweak and fix by @zqzten in https://github.com/koordinator-sh/koordinator/pull/2660

## New Contributors
* @ditingdapeng made their first contribution in https://github.com/koordinator-sh/koordinator/pull/2353
* @Rouzip made their first contribution in https://github.com/koordinator-sh/koordinator/pull/2005
* @ClanEver made their first contribution in https://github.com/koordinator-sh/koordinator/pull/2405
* @zheng-weihao made their first contribution in https://github.com/koordinator-sh/koordinator/pull/2409
* @cntigers made their first contribution in https://github.com/koordinator-sh/koordinator/pull/2434
* @LennonChin made their first contribution in https://github.com/koordinator-sh/koordinator/pull/2449
* @ZhuZhezz made their first contribution in https://github.com/koordinator-sh/koordinator/pull/2423
* @dabaooline made their first contribution in https://github.com/koordinator-sh/koordinator/pull/2483
* @bobsongplus made their first contribution in https://github.com/koordinator-sh/koordinator/pull/2524
* @yccharles made their first contribution in https://github.com/koordinator-sh/koordinator/pull/2474
* @qingyuanz made their first contribution in https://github.com/koordinator-sh/koordinator/pull/2584
* @yyrdl made their first contribution in https://github.com/koordinator-sh/koordinator/pull/2597
* @hwenwur made their first contribution in https://github.com/koordinator-sh/koordinator/pull/2621
* @hkttty2009 made their first contribution in https://github.com/koordinator-sh/koordinator/pull/2641

**Full Changelog**: https://github.com/koordinator-sh/koordinator/compare/v1.6.0...v1.7.0