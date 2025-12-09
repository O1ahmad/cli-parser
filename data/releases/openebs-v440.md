# OpenEBS - v4.4.0

**Release Name**: v4.4.0
**Published**: 2025-11-21T15:25:02Z
**Repository**: https://github.com/openebs/openebs

---

# OpenEBS 4.4.0 Release Notes

## Release Summary
OpenEBS version 4.4 introduces several functional fixes and new features focused on improving Data Security, User Experience, High availability (HA), replica rebuilds, and overall stability. The key highlights are LocalPV LVM snapshot restores . In addition, the release includes various usability and functional fixes for mayastor,  ZFS, LocalPV LVM and LocalPV Hostpath provisioners, along with documentation enhancements to help users and new contributors get started quickly.

## Replicated Storage (Mayastor)

### New Features and Enhancements

- DiskPool Expansion
It's now possible to expand a DiskPool's capacity by expanding the underlying storage device.
> _**NOTE**_: As a precondition you must create the DiskPool with sufficient metadata to accommodate/support future growth, please read more about this [here](https://openebs.io/docs/main/user-guides/replicated-storage-user-guide/replicated-pv-mayastor/advanced-operations/diskpool-expansion).
- Configurable ClusterSize
You can now configure the cluster size when creating a pool - larger cluster sizes may be beneficial when using very large storage devices.
>_**NOTE**_: As an initial limitation volumes may not be placed across pools with different cluster sizes
- Pool Cordon
Extend cordoning functionality to pools. This can be used to prevent new replicas from being created on a pool, and also as a way of migrating a volume replica out of it via scale-up/scale-down operations. 
- Orphaned Retain Snapshot Delete
Similar to volumes, when with snapshots retain move are deleted, the underlying storage is kept by the provisioner and must be deleted with provisioner specific commands.
We've added a plugin sub-command to delete these orphaned snapshots safely.
- Node Spread
Node spread topology may now be used
- Affinity Group ScaleDown
Affinity group volumes may now be scaled down to 1 replica, provided the anti-affinity across nodes is not violated.

### Bug Fixes and Improvements

- Update replica health as an atomic etcd transaction
- Exit io-engine with error if the gRPC port is busy
- Set PR_SET_IO_FLUSHER for io-engine to resolve potential deadlock
- Don't let 1 bad nexus lockup the entire nexus subsystem
- Clean up uuid from DISKS output uri
- Honor stsAffinity on backup restores via external tools
- Validate K8s secret in diskpool operator ahead of pool creation request
- Allow pool creation with zfs volume paths
- Added support for kubeconfig context switching (kubectl-mayastor plugin)
- Fixed creating pools on very-slow/very-large storage devices
- Use udev kernel monitor
- Fixed race condition where udev events were lost leading to connecting nvme devices
- Fixed HA enablement on the latest rhel and derivatives
- Fixed open permissions on call-home encryption dir
- Configurable ports of services with hostNetwork
- Add support for 1GiB hugepages
- etcd dependency updated to `12.0.14`
- Use normalized etcdUrl in default etcd-probe init containers 
- Use correct grpc port in metrics exporter
- Fix volume mkfs stuck on very large pools/volumes
- Fix agent-core panic when scheduling replicas
- Add default priority class to the daemon sets

### Release Notes
   - Refer to the [Mayastor v2.10.0 release](https://github.com/openebs/mayastor/releases/tag/v2.10.0) for detailed changes.

### Limitations
   - The Mayastor IO engine fully utilizes allocated CPU cores regardless of I/O load, running a poller at full speed.
   - A Mayastor DiskPool is limited to a single block device and cannot span multiple block devices.
   - The new at-rest encryption feature does not support rotating Data Encryption Keys(DEK).
   - Volume rebuilds are only performed on published volumes.

### Known Issues
- **IO-Engine Pod Restarts**  
   - Under heavy I/O and during constant scaling up/down of volume replicas, the io-engine pod may restart occasionally.
- **fsfreeze Operation Failure**  
   - If a pod-based workload is scheduled on a node that reboots and the pod lacks a controller (such as a Deployment or StatefulSet),  the volume unpublish operation might not be triggered. 
   - This leads the control plane to assume the volume is still published, causing the fsfreeze operation to fail during snapshot creation.
        - **Workaround** Recreate or reinstate the pod to ensure proper volume mounting.
- **Diskpool's backing device failure**
   - If the backend device that hosts a diskpool runs into a fault, or gets removed e.g cloud disk removal, the status of diskpool and hosted replicas isn't clearly updated to reflect the problem. 
   - As a result the resultant failures aren't gracefully handled and volume might remain Degraded for an extended period of time.
- **Extremely large pool undergoing dirty shutdown**
   - In case of a dirty shutdown of io-engine node hosting an extremely large pool e.g 10TiB or 20TiB.
   - The recovery of pool takes a while after the node comes online.

## LocalPV ZFS

### New Features and Enhancements
- Update Go runtime to 1.24.
  Bumps up go runtime and all dependents to their latest available releases 
- Allow users to configure CPU and memory requests/limits for all zfs-node and zfs-controller containers via values.yaml, improving resource management and deployment flexibility

### Bug Fixes and Improvements
- Removes encryption parameter handling from `buildCloneCreateArgs()` since clones automatically inherit encryption from the parent snapshot and the property cannot be set (it's read-only) 

### Continuous Integration and Maintenance
- Staging CI 
   Introduction of the staging CI, which enables creating a staging build for e2e testing before releasing, the artifacts are then copied over to production build hosts.

### Release Notes
   - Refer to the [ZFS v2.9.0 release](https://github.com/openebs/zfs-localpv/releases/tag/v2.9.0) for detailed changes.

## LocalPV LVM

### New Features and Enhancements

- Snapshot restore
   LocalPV-LVM snapshot had limited capabilities. Now we support restoring a snapshot to volume 
- ThinPool space reclamation
   LocalPV-LVM will cleanup the thinpool LV after deleting the last thin volume of the thinpool 
- Scheduler fixes and enhancements
    Record thinpool statistics in lvmnode CR. Fail fast CreateVolume request if thick PVC size cannot be accommodated by any VG.
    Considers thinpool free space while scheduling thin pvc in SpaceWeighted algorithm 
- Runtime improvements
   Updates Go runtime, k8s modules, golint packages etc by @jochenseeber in https://github.com/openebs/lvm-localpv/pull/416

### Continuous Integration and Maintenance
-  Staging CI
    Introduction of the staging CI, which enables creating a staging build for e2e testing before releasing, the artifacts are then copied over to production build hosts.

### Release Notes
   - Refer to the [LVM v1.8.0 release](https://github.com/openebs/lvm-localpv/releases/tag/v1.8.0) for detailed changes.

### Known Issues

- There's no unmap/reclaim for thin pool capacity.
  It is not tracked in the `lvmnode`, which may lead to unexpected behaviour when scheduling volumes.  
  Read more about this [here](https://github.com/openebs/lvm-localpv/issues/382)

## LocalPV Hostpath

### Release Notes
   - Refer to the [Hostpath v4.4.0 release](https://github.com/openebs/dynamic-localpv-provisioner/releases/tag/v4.4.0) for detailed changes.


## LocalPV RawFile

### New Features and Enhancements

- VolumeSnapshots based on the rawfile image
- Volume Restore from snapshot
- Volume Clone

### Release Notes

Make sure you follow the [install guide](https://github.com/openebs/rawfile-localpv/blob/v0.11.0/docs/install-guide.md#upgrade) when upgrading.  
Refer to the [Rawfile v0.12.0 release](https://github.com/openebs/rawfile-localpv/releases/tag/v0.12.0) for detailed changes.

## Known Issues
- **Controller Pod Restart on Single Node Setup**  
   After upgrading, single node setups may face issues where the ZFS-localpv/LVM-localpv controller pod does not enter the Running state due to changes in the controller manifest (now a Deployment) and missing affinity rules.
 
  _Workaround:_ Delete the old controller pod to allow the new pod to be scheduled correctly. This does not happen if upgrading from the previous release of ZFS-localpv/LVM-localpv.

# Upgrade and Backward Incompatibilities
   - Kubernetes Requirement: Kubernetes 1.23 or higher is recommended.
   - Engine Compatibility: Upgrades to OpenEBS 4.4.0 are supported only for the following engines:
     - Local PV Hostpath
     - Local PV LVM
     - Local PV ZFS
     - Mayastor (from earlier editions, 3.10.x or below)
     - Local PV Rawfile

