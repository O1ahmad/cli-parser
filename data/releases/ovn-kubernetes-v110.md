# OVN-Kubernetes - v1.1.0

**Release Name**: OVN-Kubernetes v1.1.0
**Published**: 2025-08-12T05:22:25Z
**Repository**: https://github.com/ovn-kubernetes/ovn-kubernetes

---

# v1.1.0

📢 We are happy to announce the release of OVN-Kubernetes v1.1.0 🎉 🎊 🎆 🎇💥
This version of OVN-Kubernetes uses:
☸️ Kubernetes v1.33.3
🎖️ Libovsdb v0.8.1
🔁 OVN ovn-25.03.1-42.fc42.x86_64
🔄 OVS openvswitch-3.4.1-1.fc42.x86_64

## Summary of important changes for this release

This release includes many exciting features that end-users can leverage:

🌐 **UserDefinedNetworks** offer flexible network configurations for users, going beyond the traditional single default network model for all pods within a Kubernetes cluster. This feature addresses the diverse and advanced networking requirements of various applications and use cases. It allows the end users to create isolated networks on a cluster to which they can attach their workloads to. See our [user-guide](https://ovn-kubernetes.io/features/user-defined-networks/user-defined-networks/) for more details.

🌐 **NetworkQoS** superceeds `EgressQoS` feature that was released in 1.0 release. This is an alpha versioned API feature that allows users to leverage DSCP markings to ensure Quality of Service for workloads attached to different networks on your cluster. See our [user-guide](https://ovn-kubernetes.io/features/network-qos-guide/) for more details.

🌐 **RouteAdvertisements** feature leverages the FRR-K8s CNCF project to allow users to advertise their networks (cluster default network and cluster user defined networks) via BGP to the external world outside the cluster. This let's external clients reach the workloads directly using the podIPs that are advertised to outside. If you want to have an unSNATed experience try out this feature. See our [user-guide](TBD) for more details.

🔀 Interconnect mode of deployment makes OVN-Kubernetes more scalable, performant and secure. Support for this mode of deployment was added as part of 1.0.0 release, however it was not the default. Now, from 1.1 release, we are making this the default deployment mode of OVN-Kubernetes.

Please reach out to us on CNCF Slack channel ovn-kubernetes and provide feedback based on your experience of using this release so that we can keep improving this project!

## New Contributors 💖 💖 

* @shaneutt made their first contribution in https://github.com/ovn-kubernetes/ovn-kubernetes/pull/4588
* @ormergi made their first contribution in https://github.com/ovn-kubernetes/ovn-kubernetes/pull/4585
* @RamLavi made their first contribution in https://github.com/ovn-kubernetes/ovn-kubernetes/pull/4725
* @fossabot made their first contribution in https://github.com/ovn-kubernetes/ovn-kubernetes/pull/4836
* @poroh made their first contribution in https://github.com/ovn-kubernetes/ovn-kubernetes/pull/4870
* @FSchumacher made their first contribution in https://github.com/ovn-kubernetes/ovn-kubernetes/pull/4945
* @yboaron made their first contribution in https://github.com/ovn-kubernetes/ovn-kubernetes/pull/4955
* @TOMOFUMI-KONDO made their first contribution in https://github.com/ovn-kubernetes/ovn-kubernetes/pull/5132
* @almusil made their first contribution in https://github.com/ovn-kubernetes/ovn-kubernetes/pull/5164
* @thisisobate made their first contribution in https://github.com/ovn-kubernetes/ovn-kubernetes/pull/5180
* @aztecher made their first contribution in https://github.com/ovn-kubernetes/ovn-kubernetes/pull/5136
* @anuragthehatter made their first contribution in https://github.com/ovn-kubernetes/ovn-kubernetes/pull/5248
* @jitseklomp made their first contribution in https://github.com/ovn-kubernetes/ovn-kubernetes/pull/5281
* @hedgieinsocks made their first contribution in https://github.com/ovn-kubernetes/ovn-kubernetes/pull/5312
* @PGhiorzo made their first contribution in https://github.com/ovn-kubernetes/ovn-kubernetes/pull/5323
* @GeorgianaTurcsanyi made their first contribution in https://github.com/ovn-kubernetes/ovn-kubernetes/pull/5333
* @booxter made their first contribution in https://github.com/ovn-kubernetes/ovn-kubernetes/pull/5382
* @tsebastiani made their first contribution in https://github.com/ovn-kubernetes/ovn-kubernetes/pull/5442
* @asood-rh made their first contribution in https://github.com/ovn-kubernetes/ovn-kubernetes/pull/5319

Special welcome to our new set of contributors into the community 💖 💖 

## Contributors  💖 

Many thanks to all of our contributors who helped make this release happen 😄👏 !! We truly couldn't have done this without all your contributions. Contributors info taken based on [this data](https://github.com/ovn-kubernetes/ovn-kubernetes/graphs/contributors?from=6%2F14%2F2024&to=8%2F12%2F2025&type=c).

@tssurya @jcaamano @qinqon @trozet @npinaeva @martinkennelly @maiqueb @dceara @kyrtapz @ormergi @flavio-fernandes @RamLavi @ricky-rav @crnithya @pperiyasamy @oshoval @JacobTanenbaum @danwinship @cathy-zhou @pliurh @arghosh93 @aserdean @jotak @booxter @jluhrsen @arkadeepsen @yboaron @oribon @dave-tucker @girishmg @numansiddique @zeeke @SchSeba @poroh @aztecher @abhat @hareeshpc 

Also special thanks to everyone who reported issues and opened tickets against the project. That helps OVN-Kubernetes get better!

**Full Changelog**: https://github.com/ovn-kubernetes/ovn-kubernetes/compare/v1.0.0...v1.1.0