# Service Mesh Interface (SMI) - v0.6.0

**Release Name**: v0.6.0
**Published**: 2021-01-20T11:31:42Z
**Repository**: https://github.com/servicemeshinterface/smi-spec

---

This release encompasses much cleanup and new additions to the SMI specification. This version of the SMI specification is implemented in the go sdk [here](https://github.com/servicemeshinterface/smi-sdk-go/releases/tag/v0.5.0).

## Notable Changes ##
### Traffic Specs ###
- Updated to v1alpha4
- TCPRoute and UDPRoute were updated and added.
- Can be used with Traffic Access v1alpha3

### Traffic Access ###
- Updated to v1alpha3
- Port list was removed from the top level Traffic Target spec and into TCPRoute
- A constraint was added stating you must have at least one source, one destination, and one rule in order to have a valid Traffic Target object
- Can be used with Traffic Specs v1alpha4

### Traffic Metrics ###
- Remains v1alpha1
- Spelling and documentation fixes

### Traffic Split ###
- Updated to v1alpha4
- Spelling and documentation fixes
- Can be used with Traffic Specs v1alpha4

## Community

Thank you to everyone who participated in this release. We had several new community members and contributors this round. We really appreciate your input! Special shoutout to @patricekrakow @nojnhuh 🎉 

We also got new maintainers on the spec. @mhausenblas @Pothulapati ! 🎉 

We'd also like to extend a big welcome to the [Argo](https://argoproj.github.io/argo-rollouts/getting-started/smi/) to the SMI community of implementors. 🎉 

## Changelog
- chore(*): prepare spec for v0.6.0 release c03465859d0f86582e09af7c6b58e41be203a613 (Michelle Noorali)
- ref(TrafficTarget): update requirements for TrafficTarget 2e52af44c788a5265f6617e4578d3cd1ee0435a5 (Michelle Noorali)
- docs: add Argo Rollouts as part of SMI ecosystem a143e4300e9ad845acf96dc5d30e6d22ef8206ad (Jesse Suen)
- Update setup-node GH action 70f301a00e2e80bb1d4040b4566b0289812eddcb (Stefan Prodan)
- update service mesh hub -> gloo-mesh 279821520070ce156f5492e0a27a7abb2c945dee (Scott Weiss)
- Add Tarun Pothulapati as maintainer e3b3c9958485a246864b5b1cb1fa3054e4d2018d (Michelle Noorali)
- Add Michael Hausenblas as maintainer 6004c3045942a5cf9ddbd91fb493984115cd47b4 (Michelle Noorali)
- Rename maesh to traefik mesh in readme 8378df7c6479569ce4f2a5ecd2178e9f74efbd59 (kevinpollet)
- Align the structure of the 4 APIs 5ea7e93b29d4580ea615d0508d28a6ae0094a19a (Patrice Krakow)
- Just fix a small typo f53ef1304d17d6c6e88defe77c47441fc18b55e4 (Patrice Krakow)
- fix wrong service name mentioned in example 11516673742d20436b5756766fbe9712c6392f2b (Thorsten Hans)
- fix percentages mentioned in description for TrafficSplit 0e72fd0fba9d462cdb1d5b4806fb6871245440f9 (Thorsten Hans)
- Fix formatting c8bc04ba6bd99bdc002f9c614cbbbc2a1e7a773d (stefanprodan)
- Add TCP/UDP routes to access/v1alpha3 Replace 'destination.port' with TCP/UDPRoute 'matches.ports' 8008055c7f469a8acd5cf38fe78f24ebc93d8559 (stefanprodan)
- Add TCP/UDP port matching to specs/v1alpha4 894612ad68207376bececa477ee4312f0cda4d22 (stefanprodan)
- Adding Open Service Mesh a03f306ba5194238e44ef2df7e4993638f6aa44e (Bridget Kromhout)