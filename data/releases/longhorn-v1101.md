# Longhorn - v1.10.1

**Release Name**: Longhorn v1.10.1
**Published**: 2025-11-12T08:04:25Z
**Repository**: https://github.com/longhorn/longhorn

---

## Longhorn v1.10.1 Release Notes

Longhorn 1.10.1 introduces several improvements and bug fixes that are intended to improve system quality, resilience, stability and security.

We welcome feedback and contributions to help continuously improve Longhorn.

For terminology and context on Longhorn releases, see [Releases](https://github.com/longhorn/longhorn#releases).

> [!WARNING]
> ### HotFix
>
> The `longhorn-manager:v1.10.1` image is affected by a [regression issue](https://github.com/longhorn/longhorn/issues/12233) that can trigger a nil-pointer dereference under certain conditions, potentially causing unexpected crashes. To mitigate this issue, replace `longhorn-manager:v1.10.1` with the hotfixed image `longhorn-manager:v1.10.1-hotfix-1`.
>
>Follow these steps to apply the update:
>
>1. **Disable the upgrade version check**
>   - Helm users: Set `upgradeVersionCheck` to `false` in the `values.yaml` file.
>   - Manifest users: Remove the `--upgrade-version-check` flag from the deployment manifest.
>
>2. **Update the `longhorn-manager` image**
>   - Change the image tag from `v1.10.1` to `v1.10.1-hotfix-1` in the appropriate file:
>     - For Helm: Update `values.yaml`
>     - For manifests: Update the deployment manifest directly.
>
>3. **Proceed with the upgrade**
>   - Apply the changes using your standard Helm upgrade command or reapply the updated manifest.
>
> ### Upgrade
> 
> If your Longhorn cluster was initially deployed with a version earlier than v1.3.0, the Custom Resources (CRs) were created using the `v1beta1` APIs. While the upgrade from Longhorn v1.8 to v1.9 automatically migrates all CRs to the new `v1beta2` version, **a manual CR migration is strongly advised before upgrading from Longhorn `v1.9` to `v1.10`**.
> 
> Certain operations, such as an `etcd` or CRD restore, may leave behind `v1beta1` data. Manually migrating your CRs ensures that all Longhorn data is properly updated to the `v1beta2` API, preventing potential compatibility issues and unexpected behavior with the new Longhorn version.
> 
> Following the manual migration, **verify that `v1beta1` has been removed from the CRD stored versions** to ensure completion and a successful upgrade.
>
> For more details, see [Kubernetes official document for CRD storage version](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning/#upgrade-existing-objects-to-a-new-stored-version), and [Issue #11886](https://github.com/longhorn/longhorn/issues/11886).
> 
> #### Migration Requirement Before Longhorn v1.10 Upgrade
> 
> Before upgrading from Longhorn v1.9 to v1.10, perform the following manual CRD storage version migration.
> 
> > **Note**: If your Longhorn installation uses a namespace other than `longhorn-system`, replace `longhorn-system` with your custom namespace throughout the commands.
> 
> ```bash
> # Temporarily disable the CR validation webhook to allow updating read-only settings CRs.
> kubectl patch validatingwebhookconfiguration longhorn-webhook-validator \
>   --type=merge \
>   -p "$(kubectl get validatingwebhookconfiguration longhorn-webhook-validator -o json | \
>   jq '.webhooks[0].rules |= map(if .apiGroups == ["longhorn.io"] and .resources == ["settings"] then
>     .operations |= map(select(. != "UPDATE")) else . end)')"
>
> # Migrate CRDs that ever stored v1beta1 resources
> migration_time="$(date +%Y-%m-%dT%H:%M:%S)"
> crds=($(kubectl get crd -l app.kubernetes.io/name=longhorn -o json | jq -r '.items[] | select(.status.storedVersions | index("v1beta1")) | .metadata.name'))
> for crd in "${crds[@]}"; do
>   echo "Migrating ${crd} ..."
>   for name in $(kubectl -n longhorn-system get "$crd" -o jsonpath='{.items[*].metadata.name}'); do
>     # Attach additional annotations to trigger v1beta1 resource updating in the latest storage version.
>     kubectl patch "${crd}" "${name}" -n longhorn-system --type=merge -p='{"metadata":{"annotations":{"migration-time":"'"${migration_time}"'"}}}'
>  done
>  # Clean up the stored version in CRD status
>  kubectl patch crd "${crd}" --type=merge -p '{"status":{"storedVersions":["v1beta2"]}}' --subresource=status
> done
> 
> # Re-enable the CR validation webhook.
> kubectl patch validatingwebhookconfiguration longhorn-webhook-validator \
>   --type=merge \
>   -p "$(kubectl get validatingwebhookconfiguration longhorn-webhook-validator -o json | \
>   jq '.webhooks[0].rules |= map(if .apiGroups == ["longhorn.io"] and .resources == ["settings"] then
>     .operations |= (. + ["UPDATE"] | unique) else . end)')"
> ```
> 
> #### Migration Verification
> 
> After running the script, verify the CRD stored versions using this command:
> 
> ```bash
> kubectl get crd -l app.kubernetes.io/name=longhorn -o=jsonpath='{range .items[*]}{.metadata.name}{": "}{.status.storedVersions}{"\n"}{end}'
> ```
> 
> Crucially, all Longhorn CRDs MUST have only `"v1beta2"` listed in `storedVersions` (i.e., `"v1beta1"` must be completely absent) before proceeding to the v1.10 upgrade.
> 
> Example of successful output:
> 
> ```
> backingimagedatasources.longhorn.io: ["v1beta2"]
> backingimagemanagers.longhorn.io: ["v1beta2"]
> backingimages.longhorn.io: ["v1beta2"]
> backupbackingimages.longhorn.io: ["v1beta2"]
> backups.longhorn.io: ["v1beta2"]
> backuptargets.longhorn.io: ["v1beta2"]
> backupvolumes.longhorn.io: ["v1beta2"]
> engineimages.longhorn.io: ["v1beta2"]
> engines.longhorn.io: ["v1beta2"]
> instancemanagers.longhorn.io: ["v1beta2"]
> nodes.longhorn.io: ["v1beta2"]
> orphans.longhorn.io: ["v1beta2"]
> recurringjobs.longhorn.io: ["v1beta2"]
> replicas.longhorn.io: ["v1beta2"]
> settings.longhorn.io: ["v1beta2"]
> sharemanagers.longhorn.io: ["v1beta2"]
> snapshots.longhorn.io: ["v1beta2"]
> supportbundles.longhorn.io: ["v1beta2"]
> systembackups.longhorn.io: ["v1beta2"]
> systemrestores.longhorn.io: ["v1beta2"]
> volumeattachments.longhorn.io: ["v1beta2"]
> volumes.longhorn.io: ["v1beta2"]
> ```
> 
> With these steps completed, the Longhorn upgrade to v1.10 should now proceed without issues.
> 
> #### Troubleshooting CRD Upgrade Failures During Upgrade to Longhorn v1.10
> 
> If you did not apply the required pre-upgrade migration steps and the CRs are not fully migrated to `v1beta2`, the `longhorn-manager` Pods may fail to operate correctly. A common error message for this issue is:
> 
> ```
> Upgrade failed: cannot patch "backingimagedatasources.longhorn.io" with kind CustomResourceDefinition: CustomResourceDefinition.apiextensions.k8s.io "backingimagedatasources.longhorn.io" is invalid: status.storedVersions[0]: Invalid value: "v1beta1": missing from spec.versions; v1beta1 was previously a storage version, and must remain in spec.versions until a storage migration ensures no data remains persisted in v1beta1 and removes v1beta1 from status.storedVersions
> ```
> 
> To fix this issue, you must perform a **forced downgrade** back to the **exact Longhorn v1.9.x version** that was running before the failed upgrade attempt.
> 
> ##### Downgrade Procedure (kubectl Installation)
> 
> If Longhorn was installed using `kubectl`, you must patch the `current-longhorn-version` setting before downgrading. Replace `v1.9.x` with the original version before upgrade in the following commands.
> 
> ```bash
> # Attaching annotation to allow patching current-longhorn-version.
> kubectl patch settings.longhorn.io current-longhorn-version -n longhorn-system --type=merge -p='{"metadata":{"annotations":{"longhorn.io/update-setting-from-longhorn":""}}}'
> # Temporarily override current version to allow old version installation
> # Replace the value `"v1.9.x" to the original version before upgrade.
> kubectl patch settings.longhorn.io current-longhorn-version -n longhorn-system --type=merge -p='{"value":"v1.9.x"}'
> ```
> 
> After modifying `current-longhorn-version`, you can proceed to downgrade to the original Longhorn v1.9.x deployment.
> 
> ##### Downgrade Procedure (Helm Installation)
> 
> If Longhorn was installed using Helm, the downgrade is allowed by disabling the [`preUpgradeChecker.upgradeVersionCheck`](https://github.com/longhorn/longhorn/tree/v1.9.x/chart#other-settings) flag.
> 
> ##### Post-Downgrade
> 
> Once the downgrade is complete and the Longhorn system is stable on the v1.9.x version, you must immediately follow the steps outlined in the **Migration Requirement Before Longhorn v1.10 Upgrade**. This step is crucial to migrate all remaining `v1beta1` CRs to `v1beta2` before attempting the Longhorn v1.10 upgrade again.

## Important Fixes

This release includes several critical stability and performance improvements:

### Goroutine Leak in Instance Manager (V2 Data Engine)

Fixed a goroutine leak in the instance manager when using the V2 data engine. This issue could lead to increased memory usage and potential stability problems over time.

For more details, see [Issue #11962](https://github.com/longhorn/longhorn/issues/11962).

### V2 Volume Attachment Failure in Interrupt Mode

Fixed an issue where V2 volumes using interrupt mode with NVMe disks could fail to complete the attachment process, causing volumes to remain stuck in the attaching state indefinitely.

In Longhorn v1.10.0, interrupt mode supports only **AIO disks**. Interrupt mode for **NVMe disks** is supported starting in v1.10.1.

For more details, see [Issue #11816](https://github.com/longhorn/longhorn/issues/11816).

### UI Deployment Failure on IPv4-Only Nodes

Fixed a bug introduced in v1.10.0 where the Longhorn UI failed to deploy on nodes with only IPv4 enabled. The UI now correctly supports IPv4-only configurations without requiring IPv6.

For more details, see [Issue #11875](https://github.com/longhorn/longhorn/issues/11875).

### Share Manager Excessive Memory Usage

Fixed excessive memory consumption in the share manager for RWX (ReadWriteMany) volumes. The component now maintains stable memory usage under normal operation.

For more details, see [Issue #12043](https://github.com/longhorn/longhorn/issues/12043).

## Installation

>  [!IMPORTANT]
**Ensure that your cluster is running Kubernetes v1.25 or later before installing Longhorn v1.10.1.**

You can install Longhorn using a variety of tools, including Rancher, Kubectl, and Helm. For more information about installation methods and requirements, see [Quick Installation](https://longhorn.io/docs/1.10.0/deploy/install/) in the Longhorn documentation.

## Upgrade

>  [!IMPORTANT]
**Ensure that your cluster is running Kubernetes v1.25 or later before upgrading from Longhorn v1.9.x to v1.10.1.**

Longhorn only allows upgrades from supported versions. For more information about upgrade paths and procedures, see [Upgrade](https://longhorn.io/docs/1.10.0/deploy/upgrade/) in the Longhorn documentation.

## Post-Release Known Issues

For information about issues identified after this release, see [Release-Known-Issues](https://github.com/longhorn/longhorn/wiki/Release-Known-Issues).

## Resolved Issues

### Improvement

- [BACKPORT][v1.10.1][IMPROVEMENT] The `auto-delete-pod-when-volume-detached-unexpectedly` should only focus on the kubernetes builtin workload. [12125](https://github.com/longhorn/longhorn/issues/12125) - @derekbit @chriscchien
- [BACKPORT][v1.10.1][IMPROVEMENT] `CSIStorageCapacity` objects must show schedulable (allocatable) capacity [12036](https://github.com/longhorn/longhorn/issues/12036) - @chriscchien @bachmanity1
- [BACKPORT][v1.10.1][IMPROVEMENT] improve error logging for failed mounting during node publish volume [12033](https://github.com/longhorn/longhorn/issues/12033) - @COLDTURNIP @roger-ryao
- [BACKPORT][v1.10.1][IMPROVEMENT] Improve Helm Chart defaultSettings handling with automatic quoting and multi-type support [12020](https://github.com/longhorn/longhorn/issues/12020) - @derekbit @chriscchien
- [BACKPORT][v1.10.1][IMPROVEMENT] Avoid repeat engine restart when there are replica unavailable during migration [11945](https://github.com/longhorn/longhorn/issues/11945) - @yangchiu @shuo-wu
- [BACKPORT][v1.10.1][IMPROVEMENT] Adjust maximum of GuaranteedInstanceManagerCPU to a big value [11968](https://github.com/longhorn/longhorn/issues/11968) - @mantissahz
- [BACKPORT][v1.10.1][IMPROVEMENT] Add usage metrics for Longhorn installation variant [11795](https://github.com/longhorn/longhorn/issues/11795) - @derekbit

### Bug

- [BACKPORT][v1.10.1][BUG] Backup target metric is broken [12089](https://github.com/longhorn/longhorn/issues/12089) - @mantissahz @roger-ryao
- [BACKPORT][v1.10.1][BUG] Backing image download gets stuck after network disconnection [12094](https://github.com/longhorn/longhorn/issues/12094) - @COLDTURNIP @chriscchien
- [BACKPORT][v1.10.1][BUG] panic: runtime error: invalid memory address or nil pointer dereference [signal SIGSEGV: segmentation violation code=0x1 at longhorn-engine/pkg/controller/control.go:218 +0x2de [12088](https://github.com/longhorn/longhorn/issues/12088) - @roger-ryao
- [BACKPORT][v1.10.1][BUG] Unable to complete uninstallation due to the remaining backuptarget [11964](https://github.com/longhorn/longhorn/issues/11964) - @mantissahz @roger-ryao
- [BACKPORT][v1.10.1][BUG] share-manager excessive memory usage [12043](https://github.com/longhorn/longhorn/issues/12043) - @derekbit @chriscchien
- [BACKPORT][v1.10.1][BUG] NVME disk not found in v2 data engine (failed to find device for BDF) [12029](https://github.com/longhorn/longhorn/issues/12029) - @derekbit @roger-ryao
- [BACKPORT][v1.10.1][BUG] NPE error during recurring job execution [11926](https://github.com/longhorn/longhorn/issues/11926) - @yangchiu @shuo-wu
- [BACKPORT][v1.10.1][BUG] v2 volume creation failed on talos nodes [12026](https://github.com/longhorn/longhorn/issues/12026) - @c3y1huang @chriscchien
- [BACKPORT][v1.10.1][BUG] mounting error is not properly hanedled during CSI node publish volume [12008](https://github.com/longhorn/longhorn/issues/12008) - @COLDTURNIP
- [BACKPORT][v1.10.1][BUG] Adding multiple disks to the same node concurrently may occasionally fail [12018](https://github.com/longhorn/longhorn/issues/12018) - @davidcheng0922 @roger-ryao
- [BUG] upgrading from 1.9.1 to 1.10.0 fails due to old resources still being in v1beta1 [11886](https://github.com/longhorn/longhorn/issues/11886) - @COLDTURNIP @roger-ryao
- [BACKPORT][v1.10.1][BUG] DR volume gets stuck in `unknown` state if engine image is deleted from the attached node [11998](https://github.com/longhorn/longhorn/issues/11998) - @yangchiu @shuo-wu
- [BACKPORT][v1.10.1][BUG] Volume gets stuck in `attaching` state if engine image image is not deployed on one of nodes [11996](https://github.com/longhorn/longhorn/issues/11996) - @yangchiu @shuo-wu
- [BACKPORT][v1.10.1][BUG] Unable to re-add block-type disks by BDF after re-enable v2 data engine [12000](https://github.com/longhorn/longhorn/issues/12000) - @yangchiu @davidcheng0922
- [BACKPORT][v1.10.1][BUG] `test_system_backup_and_restore` test case failed on master-head [12005](https://github.com/longhorn/longhorn/issues/12005) - @derekbit @chriscchien
- [BACKPORT][v1.10.1][BUG] Fix SPDK v25.05 CVE issue [11970](https://github.com/longhorn/longhorn/issues/11970) - @derekbit @roger-ryao
- [BACKPORT][v1.10.1][BUG] V2 volume stuck in volume attachment (V2 interrupt mode) [11976](https://github.com/longhorn/longhorn/issues/11976) - @c3y1huang @chriscchien
- [BACKPORT][v1.10.1][BUG] RWX volume causes process uninterruptible sleep [11958](https://github.com/longhorn/longhorn/issues/11958) - @COLDTURNIP @chriscchien
- [BACKPORT][v1.10.1][BUG] longhorn-manager fails to start after upgrading from 1.9.2 to 1.10.0 [11865](https://github.com/longhorn/longhorn/issues/11865) - @derekbit @roger-ryao
- [BACKPORT][v1.10.1][BUG] Block disk deletion fails without error message [11954](https://github.com/longhorn/longhorn/issues/11954) - @davidcheng0922 @roger-ryao
- [BACKPORT][v1.10.1][BUG] Goroutine leak in instance-manager when using v2 data engine [11962](https://github.com/longhorn/longhorn/issues/11962) - @PhanLe1010 @chriscchien
- [BACKPORT][v1.10.1][BUG] invalid memory address or nil pointer dereference [11942](https://github.com/longhorn/longhorn/issues/11942) - @bachmanity1 @roger-ryao
- [BACKPORT][v1.10.1][BUG] csi-provisioner silently fails to create CSIStorageCapacity if dataEngine parameter is missing [11918](https://github.com/longhorn/longhorn/issues/11918) - @yangchiu @bachmanity1
- [BACKPORT][v1.10.1][BUG] longhorn-engine's UI panics [11901](https://github.com/longhorn/longhorn/issues/11901) - @derekbit @chriscchien
- [BACKPORT][v1.10.1][BUG] Volume is unable to upgrade if the number of active replicas is larger than `volumme.spec.numberOfReplicas` [11895](https://github.com/longhorn/longhorn/issues/11895) - @yangchiu @derekbit
- [BACKPORT][v1.10.1][BUG] UI fails to deploy when only IPv4 is enabled on nodes with v1.10.0 version [11875](https://github.com/longhorn/longhorn/issues/11875) - @yangchiu @c3y1huang
- [BACKPORT][v1.10.1][BUG] Unable to detach a v2 volume after labeling `disable-v2-data-engine=true` [11801](https://github.com/longhorn/longhorn/issues/11801) - @mantissahz

### Misc

- [BACKPORT][v1.10.1][REFACTOR] SAST checks for UI component [11992](https://github.com/longhorn/longhorn/issues/11992) - @chriscchien
- [HOTFIX] Create hotfixed image for longhorn-manager:v1.10.0 [11951](https://github.com/longhorn/longhorn/issues/11951) - @c3y1huang @roger-ryao

## Contributors

- @COLDTURNIP
- @PhanLe1010
- @bachmanity1
- @c3y1huang
- @chriscchien
- @davidcheng0922
- @derekbit
- @forbesguthrie
- @innobead
- @mantissahz
- @rebeccazzzz
- @roger-ryao
- @sushant-suse
- @shuo-wu
- @yangchiu