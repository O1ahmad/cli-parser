# Pravega - v0.13.0

**Release Name**: Version 0.13.0
**Published**: 2023-09-18T10:16:11Z
**Repository**: https://github.com/pravega/pravega

---

This release contains significant enhancements and fixes over the previous major release line (0.12.x). This page provides an overview of most important ones. The major goal of this release was support for more storage types like GCP, Azure, stability improvements, integrity checks, CLI commands and various other fixes.

## Pravega Client
In this release, Pravega Client along with providing new API's for better user experience, also brings in some performance fixes.

Issue #2166: Improve logging for outstanding checkpoint (#6974) (#6994) (#6996)
Issue #6747 : Cache segment to host mapping (#6872)
Issue #6891: Fix the wrong ScaleType value in the ScalingPolicy.ScaleType enum. (#6892)
Issue #6853: Expose location details of a segment. (#6854)
Issue #3658: FlowId and Request Id in InvalidEventNumber Wirecommand (#6774)


## Pravega LTS
Major goal of this release has been support for more storage types, specifically support for Azure and GCP, along with other important fixes.

Issue #7002: LTS - Set default value of storage.readindex.block.size to 1 GB. (#7003) (#7006)
Issue #6934: LTS - Update ECS client to v3.4.5. (#6936)
Issue #6896: LTS - Refactor FlakyChunkStorage by moving to top level and using wrapper pattern. (#6897)
Issue #6849: LTS - Remove deprecated RollingStorage implementations from bindings project. (#6858)
Issue #6790: (LTS) Implement bindings for Azure Storage (#6791)
Issue #6787: LTS - Implementation of GCP binding for LTS (#6786)
Issue #6032: Update ECS Object Client SDK dependency to latest version (#6738)
Issue #6734: LTS - Make CHUNKED_STORAGE default in ServiceConfig and InProcPravegaCluster. (#6735)
Issue #6704: LTS - Set writer.rollover.size.bytes.max=134217728 as default (#6726)
Issue #6811: LTS - Always disable lazy commit functionality for all writes to all segments (#6841)


## Pravega Segment Store
This release of SS majorly focuses on adding various integrity checks, that help preserve the integrity of data in the ingestion pipeline if enabled.
Apart from that there are also stability improvements made, which were found during the development and testing cylce of this release.

Issue #5975: ZKSegmentContainerMonitor blocks ForkJoinPool threads when queuing Segment Container Starts (#6913 )
Issue #6811: LTS - Add data integrity checks. (#6820)
Issue #6804: Add integrity checks in Pravega (Tier 1) (#6805)
Issue #6878: Revert Bookkeeper 4.15 upgrade in master (#6879)
Issue #6772: Unnecessary segment container restarts due to Bookkeeper client re-creation mechanism (#6773)
Issue #6444: Duplicate DataFrames detected upon ledger rollover (#6741)
Issue #6759: OperationProcessor may be left stuck during shutdown if operationQueue is unexpectedly closed (#6758)


## Pravega CLI
The major goal of this release of CLI has been recovery commands. As we can see we have added various recovery commands that  can help recover a Pravega cluster in various fatal scenarios, like Table Segment Index recovery, Ability to Update LTS Snapshots and most importantly ability to restore/recover Pravega off data stored in LTS via CLI. Some of the existing commands have also been enhanced in this release.

Issue #7011: Pravega LTS based Recovery (#7012) (#7026)
Issue #6809: Add new delete ledgers command (#6815)
Issue #6497: Adding admin cli for viewing pending events (#6828)
Issue #6817 : Pravega-cli should pick up the default environment values from tls based configuration (#6818)
Issue #6800: Add a new admin CLI command to delete the reader group. (#6802)
Issue #6716: Add Query Capabilities to Admin CLI DurableLog Repair Command (#6767)
Issue #6712: Table Segment index recovery tool (#6753)
Issue #6825: Update LTS Snapshot CLI command (#6826)
Issue #6792: Removing operation versioning for table-segment recovering command (#6793)


## Pravega Controller

Issue #6999: Add default Retention Policy (#7013) (#7022)
Issue #6488: No retry from Controller on NoSuchSegment exception (#6783)
Issue #6874: Flaky test SecureStreamMetadataTasksTest.readerGroupsTest is failing (#6887)
Issue #6366: New metrics for Controller Event Processor Service (#6749)


## Pravega Documentation

Issue #6914: Update pods names in k8s doc (#6927)
Issue #6914: Update k8s getting started guide (#6920)
Issue #6910: Update quick start guide to 0.12.0 (#6917)
Issue #6901: Upload MkDocs and Javadocs snapshots to pravega.io (#6904)
Issue #6900: Update beta.pravega.io references to cncf.pravega.io (#6903)
Issue #6899: Update gradle-mkdocs-plugin to version 2.4.0 (#6902)
Issue #6862: Create document to recover container exhibiting Table Segment credits exhausted (#6886)
Issue #6829: Metadata Table Segment Attribute Index recovery document (#6831)
Issue #6782: Table Segment Index recovery doc (#6760)
Issue #6915: Move AWS and DC/OS deployment guides (#6719)
Issue #6916: Update manual installation guide (#6919)
Issue #5350: Documentation for Retention and Consumption Based Retention in Pravega (#6750)


## Security

Issue #6975:  Upgrading jackson-databind, micrometer and woodstox libraries (#6976) (#6979)
Issue #6898: Update dependencies (#6923)
Issue #6985: Upgrading commons-net, netty and jackson libraries (#6986)


## Misc
Issue #6911: DelayedProcessor warning too verbose (#6912)
Issue  #6850: Adding Java doc for fetchStreamInfo API (#6873)
Issue #6861: Refactor LargeEventTest in System Tests (#6868)
Issue #6845: Remove build warnings (#6856)
Issue #6864: Disable Mkdocs gradle plugin by default (#6865)
Issue #6851: Create a faster, unified hash function for BufferView (#6842)
Issue #6839: LTS - Resolve NullPointerException when loading Azure (#6840)
Issue #6836: Temporarily revert PR 6528 (#6837)
Issue #6748: Renaming getStreaminfo() and changing return type (#6812)
Issue #6810: Allow Log Level to be configurable (#6814)
Issue #6806: Regressions detected with Fault Injection testing in Bookkeeper 4.15 (#6807)
Issue #6803: Fix standalone log location prompt (#6788)
Issue #6801: Fixed spelling of bindings (#6798)
Issue #6796: update gRPC version to 1.47.0 (was 1.39.0) (#6794)
Issue #6732: Unexpected Pravega pod restarted in system tests (#6733)
Issue #6745: Handle Controller connectivity with ZK (#6746)