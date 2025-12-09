# Rook - v1.18.8

**Release Name**: v1.18.8
**Published**: 2025-12-02T18:40:27Z
**Repository**: https://github.com/rook/rook

---

# Improvements
Rook v1.18.8 is a patch release limited in scope and focusing on feature additions and bug fixes to the Ceph operator.

- core: Add support for ceph tentacle (#16501, @subhamkrai)
- helm: Include exporter options in CephCluster (#16745, @michaeltchapman)
- toolbox: Merge rook-config-override ConfigMap into ceph.conf (#16731, @mheler)
- csi: ControllerPlugin/NodePlugin resource settings were reversed (#16735, @swills)
- osd: Allow snaptrimp and snaptrip_wait PGs by the PDBs during node drains (#16713, @sp98)
- helm: Fix default pathType for HTTPRoute in the rook-ceph-cluster chart (#16724, @fancl20)
- pool: Retry if pool status is empty in the rados namespace controller (#16705, @parth-gr)
- namespace: Add retryOnConflict when updating status (#16661, @subhamkrai)