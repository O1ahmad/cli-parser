# KubeVirt - v1.7.0

**Release Name**: v1.7.0
**Published**: 2025-11-27T12:37:52Z
**Repository**: https://github.com/kubevirt/kubevirt

---

tag v1.7.0
Tagger: Luboslav Pivarc <lpivarc@redhat.com>

This release follows v1.6.3 and consists of 1181 changes, contributed by 71 people, leading to 2363 files changed, 105899 insertions(+), 65799 deletions(-).
v1.7.0 is a promotion of release candidate v1.7.0-rc.1 which was originally published 2025-11-24
The source code and selected binaries are available for download at: https://github.com/kubevirt/kubevirt/releases/tag/v1.7.0.

The primary release artifact of KubeVirt is the git tree. The release tag is
signed and can be verified using `git tag -v v1.7.0`.

Pre-built containers are published on Quay and can be viewed at: <https://quay.io/kubevirt/>.

Notable changes
---------------

- [PR #16199][kubevirt-bot] Don't use attachment pods marked for deletion for hotplug volume status updates.
- [PR #16168][kubevirt-bot] Migration is using dedicated certificate for mTLS.
- [PR #16198][kubevirt-bot] Bug fix: KubeVirt.spec.imagetag installation is working again
- [PR #16150][kubevirt-bot] fix: KSM is enabled in case of node pressure within 3 minutes
- [PR #16129][kubevirt-bot] Add RestartRequired when detaching CD-ROMs from a running VM
- [PR #16108][kubevirt-bot] Allow migration when host model changes after libvirt upgrade.
- [PR #16089][kubevirt-bot] A decentralized live migration failure is properly propagates between source and target
- [PR #16097][kubevirt-bot] Introduce a new subresource `/evacuate/cancel` and `virtctl evacuate-cancel` command to allow users to cancel the evacuation process for a VirtualMachineInstance (VMI). This clears the `evacuationNodeName` field in the VMI's status, stopping the automatic creation of migration resources and fully aborting the eviction cycle.
- [PR #16076][kubevirt-bot] NodeRestriction: Source of node update is now verified
- [PR #16033][noamasu] VMSnapshot: add SourceIndications status field to list snapshot indications with descriptions for clearer meaning.
- [PR #16041][kubevirt-bot] The KubevirtSeccompProfile feature is now in Beta
- [PR #16039][kubevirt-bot] Promote IBM Secure Execution Feature to Beta stage.
- [PR #16051][kubevirt-bot] Introduce pool.kubevirt.io/v1beta1
- [PR #16027][kubevirt-bot] VMPool: Add support for auto-healing startegy
- [PR #16011][kubevirt-bot] BugFix: The migration limit was not accurately being used with decentralized live migrations
- [PR #16026][fossedihelm] support v0.32.5 code generator
- [PR #16005][kubevirt-bot] promote ImageVolume FG to Beta
- [PR #15999][kubevirt-bot] VMpool: Add Scale-in strategy support with Proactive, opportunistic modes and statePreservation
- [PR #14973][Barakmor1] support live migration for ImageVolume with modified container disk images
- [PR #15939][dasionov] Beta: VideoConfig
- [PR #15887][fossedihelm] Alpha: Generalized Migration Priority in KubeVirt
- [PR #14575][zhencliu] Experimental support of Intel TDX
- [PR #15718][Vicente-Cheng] Bump k8s v1.33
- [PR #15123][Sreeja1725] VMpool: Add UpdateStrategy support with Proactive, Opportunistic modes and Selection policies
- [PR #15878][Sreeja1725] Add v1.6.0 perf and scale benchmarks data
- [PR #15936][kubevirt-bot] Updated common-instancetypes bundles to v1.5.1
- [PR #15008][fossedihelm] Fix possible nil pointer caused by migration during kv upgrade
- [PR #14845][alancaldelas] Experimental support for AMD SEV-SNP that is behind the `WorkloadEncruptionSEV` feature gate.
- [PR #15783][orelmisan] Specify correct label selection when creating a service via virtctl expose. The expose command on virtctl v1.7 and above will not work with older KubeVirt versions.
- [PR #15830][varunrsekar] Beta: PanicDevices
- [PR #15698][Acedus] It is now possible to configure discard_granularity for VM disks.
- [PR #15867][xpivarc] Bug fix: Thousands of migrations should not cause failures of active migrations
- [PR #15712][lyarwood] The `DefaultVirtHandler{QPS,Burst}` values are increased to ensure no bottleneck forms within `virt-handler`
- [PR #15788][mhenriks] Fix RestartRequired handling for hotplug volumes
- [PR #15539][tiraboschi] Add VirtualMachineInstanceEvictionRequested condition for eviction tracking
- [PR #14902][tiraboschi] The list of annotations and labels synced from VM.spec.template.metadata to VMI and then to virt-launcher pods can be extended
- [PR #15784][brianmcarey] Build KubeVirt with go v1.24.7
- [PR #15706][ksimon1] fix: prioritize expired cert removal over 50-cert limit in MergeCABundle
- [PR #15798][lyarwood] Support for the `ioThreads` VMI configurable is added to the `instancetype.kubevirt.io/v1beta1` API allowing `supplementalPoolThreadCount` to now be provided by an instance type.
- [PR #15615][alromeros] Object Graph: Include NADs and ServiceAccounts
- [PR #15398][lyarwood] Preferences can now express preferred and required architecture values for use within VirtualMachines
- [PR #15676][xpivarc] Bug fix, virt-launcher is properly reaped
- [PR #15690][lyarwood] Replicas of `virt-api` are now scaled depending on the number of nodes within the environment with the `kubevirt.io/schedulable=true` label.
- [PR #15692][awels] BugFix: Restoring naked PVCs from a VMSnapshot are now properly owned by the VM if the restore policy is set to VM
- [PR #15759][lyarwood] Only a single `Signaled Graceful Shutdown` event is now sent to avoid spamming the event recorder during long graceful shutdown attempts
- [PR #15400][lyarwood] The deprecated `instancetype.kubevirt.io/v1alpha{1,2}` API and CRDs have been removed
- [PR #15681][jean-edouard] Memory overcommit is now recalculated on migration.
- [PR #13111][brianmcarey] build: update to bazel v6.5.0 and rules_oci
- [PR #15406][Sreeja1725] Add VMpool finalizer to ensure proper cleanup
- [PR #15669][HarshithaMS005] Normalise iface status to ensure test stability of hotplug and hotunplug tests
- [PR #14772][ShellyKa13] ChangedBlockTracking: enable add/remove of qcow2 overlay if vm matches label selector
- [PR #15661][nirdothan] Support Istio versions 1.25 and above.
- [PR #15531][Yu-Jack] bump prometheus operator to 0.80.1
- [PR #15605][awels] BugFix: Able to cancel in flight decentralized live migrations properly
- [PR #15238][victortoso] Does Screenshot without the usage of VNC
- [PR #15504][sradco] Update metric kubevirt_vm_container_free_memory_bytes_based_on_rss and kubevirt_vm_container_free_memory_bytes_based_on_working_set_bytes names to kubevirt_vm_container_memory_request_margin_based_on_rss_bytes and kubevirt_vm_container_memory_request_margin_based_on_working_set_bytes so they will be clearer
- [PR #15503][Sreeja1725] Enhance VMPool unit tests to make use of fake client
- [PR #15422][lyarwood] The `DefaultVirtWebhookClient{QPS,Burst}` values are aligned with `DefaultVirtWebhookClient{QPS,Burst}` to help avoid saturating the webhook client with requests it is unable to serve during mass eviction events
- [PR #15651][dcarrier] Add WithUploadSource builder to libdv
- [PR #15642][akalenyu] BugFix: Windows VM with vTPM that was previously Storage Migrated cannot live migrate
- [PR #15181][avlitman] Add kubevirt_vm_labels metric which shows vm labels converted to Prometheus labels, and can be configured using config map with ignore and allow lists.
- [PR #15630][awels] Allow decentralized live migration on L3 networks
- [PR #15513][jean-edouard] Fixed priority escalation bug in migration controller
- [PR #15603][akalenyu] BugFix: Fix volume migration for VMs with long name
- [PR #15344][SkalaNetworks] Added VolumeOwnershipPolicy to decide how volumes are owned once they are restored.
- [PR #14976][dasionov] remove ppc64le architecture configuration support
- [PR #15509][alromeros] Bugfix: Exclude lost+found from export server
- [PR #15557][fossedihelm] Fix: grpc client in handler rest requests are properly closed
- [PR #15227][sradco] New VM alerts - VirtualMachineStuckInUnhealthyState, VirtualMachineStuckOnNode
- [PR #15478][0xFelix] virtctl: The --local-ssh flag and native ssh and scp clients are removed from virtctl. From now on the local ssh and scp clients on a host are always wrapped by virtctl ssh and scp.
- [PR #13500][brandboat] Fix incorrect metric name kubevirt_vmi_migration_disk_transfer_rate_bytes to kubevirt_vmi_migration_memory_transfer_rate_bytes
- [PR #15464][avlitman] Added virt-launcher to kubevirt_memory_delta_from_requested_bytes metric and cnv_abnormal metrics.
- [PR #15267][victortoso] Add `preserve session` option to VNC endpoint
- [PR #15357][dasionov] ensure default Firmware.Serial value on newly created vms
- [PR #15470][awels] BugFix: Unable to delete source VM on failed decentralized live migration
- [PR #15423][tiraboschi] Derive eviction-in-progress annotation from VMI eviction status
- [PR #15475][0xFelix] virtctl (portfoward|ssh|scp): Drop support for legacy dot syntax. In case the old dot syntax was used virtctl could ask for verification of the host key again. In some cases the known_hosts file might need to be updated manually.
- [PR #15170][dasionov] bugfix: ensure grace period metadata cache is synced in virt-launcher
- [PR #15397][ShellyKa13] bugfix: prevent VMSnapshotContent repeated update with the same error message
- [PR #15167][Sreeja1725] Add Command line flag to disable Node Labeller service
- [PR #15365][tiraboschi] Aligning descheduler opt-out annotation name
- [PR #14983][sradco] This PR adds the following alerts: GuestPeakVCPUQueueHighWarning, GuestPeakVCPUQueueHighCritical
- [PR #15096][lyarwood] The `foregroundDeleteVirtualMachine` has been deprecated and replaced with the domain-qualified `kubevirt.io/foregroundDeleteVirtualMachine`.
- [PR #15001][noamasu] bugfix: Enable vmsnapshot for paused VMs
- [PR #15093][Acedus] bugfix: volume hotplug pod is no longer evicted when associated VM can live migrate.
- [PR #14879][machadovilaca] Add GuestAgentInfo info metrics
- [PR #15305][Acedus] bugfix: snapshot and restore now works correctly for VMs after a storage volume migration
- [PR #15314][xpivarc] Common Names are now enforce for aggregated API
- [PR #15253][0xFelix] Bumped the bundled common-instancetypes to v1.4.0 which add new preferences.
- [PR #15182][akalenyu] BugFix: export fails when VMExport has dots in secret
- [PR #15061][lyarwood] Support for all `*_SHASUM` environment variables has been removed from the `virt-operator` component. Users should instead use the remaining `*_IMAGE` environment variables to request a specific image version using a tag, digest or both.
- [PR #15157][jean-edouard] virt-operator won't schedule on worker nodes
- [PR #15118][dankenigsberg] Drop an arbitrary limitation on VM's domain.firmaware.serial. Any string is passed verbatim to smbios. Illegal may be tweaked or ignored based on qemu/smbios version.
- [PR #15098][dominikholler] Update dependecy golang.org/x/oauth2 to v0.27.0
- [PR #15016][fossedihelm] Fix postcopy multifd compatibility during upgrade
- [PR #15100][dominikholler] Update dependecy golang.org/x/net to v0.38.0
- [PR #15099][akalenyu] BugFix: export fails when VMExport has dots in name
- [PR #14685][seanbanko] allows virtual machine instances with an instance type to specify memory fields that do not conflict with the instance type
- [PR #14888][akalenyu] Cleanup: libvmi: add consistently named cpu/mem setters
- [PR #15067][alromeros] Bugfix: Label upload PVCs to support CDI WebhookPvcRendering
- [PR #15037][jean-edouard] HostDisk: KubeVirt no longer performs chown/chmod to compensate for storage that doesn't support fsGroup
- [PR #15017][nekkunti] Added support for architecture-specific configuration of `s390x` (IBM Z) in KubeVirt cluster config.
- [PR #15022][awels] The synchronization controller migration network IP address is advertised by the KubeVirt CR
- [PR #15021][awels] Decentralized migration resource now shows the synchronization address
- [PR #14365][alaypatel07] Add support for DRA devices such as GPUs and HostDevices.
- [PR #14882][awels] Decentralized live migration is available to allow migration across namespaces and clusters
- [PR #14964][xpivarc] Beta: NodeRestriction
- [PR #14986][awels] Possible to trust additional CAs for verifying kubevirt infra structure components
- [PR #14875][nirdothan] Support seamless TCP migration with passt (alpha)

Contributors
------------
71 people contributed to this release:

71	fossedihelm <ffossemo@redhat.com>
63	Lee Yarwood <lyarwood@redhat.com>
57	Luboslav Pivarc <lpivarc@redhat.com>
57	Orel Misan <omisan@redhat.com>
56	Brian Carey <bcarey@redhat.com>
49	Alexander Wels <awels@redhat.com>
35	Jed Lejosne <jed@redhat.com>
23	Nir Dothan <ndothan@redhat.com>
17	Or Shoval <oshoval@redhat.com>
17	Shelly Kagan <skagan@redhat.com>
16	dsionov <dsionov@redhat.com>
15	Alex Kalenyuk <akalenyu@redhat.com>
15	Ananya Banerjee <anbanerj@redhat.com>
15	svarnam <svarnam@nvidia.com>
13	Felix Matouschek <fmatouschek@redhat.com>
13	bmordeha <bmordeha@redhat.com>
11	João Vilaça <machadovilaca@gmail.com>
11	dsanatar <dsanatar@redhat.com>
10	Andrej Krejcir <akrejcir@redhat.com>
10	Edward Haas <edwardh@redhat.com>
10	Noam Assouline <nassouli@redhat.com>
10	Victor Toso <victortoso@redhat.com>
10	Vladik Romanovsky <vromanso@redhat.com>
9	Adi Aloni <aaloni@redhat.com>
8	Michael Henriksen <mhenriks@redhat.com>
7	Arnon Gilboa <agilboa@redhat.com>
7	Daniel Hiller <dhiller@redhat.com>
7	Zhenchao Liu <zhencliu@redhat.com>
6	Alay Patel <alayp@nvidia.com>
6	Alvaro Romero <alromero@redhat.com>
6	Shirly Radco <sradco@redhat.com>
6	Vicente Cheng <vicente.cheng@suse.com>
6	YuJack <jk82421@gmail.com>
6	avlitman <alitman@redhat.com>
4	Michal Vavrinec <mvavrine@redhat.com>
4	Simone Tiraboschi <stirabos@redhat.com>
4	Sreeja1725 <svarnam@nvidia.com>
4	Yiming Jing <yimingjing@google.com>
3	Dan Kenigsberg <danken@redhat.com>
3	Igor Bezukh <ibezukh@redhat.com>
3	Skala Networks <contact@skala.network>
2	Ben Oukhanov <boukhanov@redhat.com>
2	Ivan Mikheykin <ivan.mikheykin@flant.com>
2	Jan Schintag <jan.schintag@de.ibm.com>
2	Karel Simon <ksimon@redhat.com>
2	Mohit Nagaraj <mohitnagaraj20@gmail.com>
2	Renovate Bot <renovate@hollyhome.ath.cx>
2	Sean Banko <sean.banko@gmail.com>
2	Yaroslav Borbat <yaroslav.752@gmail.com>
2	ajcaldelas <alan.caldelas@amd.com>
2	rkishner <rkishner@redhat.com>
1	Alan Caldelas <ajcaldelas@gmail.com>
1	Anand Nekkunti <anand.nekkunti@ibm.com>
1	Eng Zer Jun <engzerjun@gmail.com>
1	German Maglione <gmaglione@redhat.com>
1	Harshitha MS <harshitha.ms@ibm.com>
1	Itamar Holder <iholder@redhat.com>
1	Jed Lejosne <jean-edouard@users.noreply.github.com>
1	Kuan-Po Tseng <brandboat@gmail.com>
1	Or Mergi <ormergi@redhat.com>
1	Ram Lavi <ralavi@redhat.com>
1	Renuka Devi Rajendran <renuka.rajendran@suse.com>
1	Ryan Hallisey <rhallisey@nvidia.com>
1	Shanjiv A <shanjiv177@gmail.com>
1	Vamsi Krishna Siddu <vamsikrishna.siddu@ibm.com>
1	Varun Ramachandra Sekar <vsekar@nvidia.com>
1	alexandr.lushin <alexander.lushin@mail.ru>
1	dacarrie <dacarrie@cisco.com>
1	machadovilaca <machadovilaca@gmail.com>

Additional Resources
--------------------
- Mailing list: <https://groups.google.com/forum/#!forum/kubevirt-dev>
- Slack: <https://kubernetes.slack.com/messages/virtualization>
- An easy to use demo: <https://github.com/kubevirt/demo>
- [How to contribute][contributing]
- [License][license]

[contributing]: https://github.com/kubevirt/kubevirt/blob/main/CONTRIBUTING.md
[license]: https://github.com/kubevirt/kubevirt/blob/main/LICENSE
---
-----BEGIN PGP SIGNATURE-----

iHUEABEIAB0WIQQK4GMgftQ8MISyrdLHuzxv+aiWdAUCaSgk4gAKCRDHuzxv+aiW
dP9lAP9Z1OgwTVjOJX3kZRJxfKOdtoOLswauswPkG6239wgv9gD6Atsc+iN1pGgn
gu0fjfngYsc/KdbeaaxqeuC0ZOlYXpA=
=s19F
-----END PGP SIGNATURE-----



