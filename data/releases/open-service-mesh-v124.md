# Open Service Mesh - v1.2.4

**Release Name**: v1.2.4
**Published**: 2023-04-20T21:24:44Z
**Repository**: https://github.com/openservicemesh/osm

---

## Notable Changes

- Deprecate support for TLS v1.0 and TLS v1.1 for the Envoy proxy TLSMaxProtocolVersion option
- Reduce minimum TLS version from v1.3 to v1.2 for the osm controller, verifier, and health servers
- Support robust CRD conversion patching on upgrade to ensure reconciliation is controlled by the newer OSM version

## Deprecation Notes

## CRD Updates

No CRD changes between tags v1.2.3 and v1.2.4

## Changelog

* chore(release): bump version to v1.2.4 and update release notes (#5330) 82651008921837b2f21113e4604a807c3f68a97c (Jackie Elliott)
* build(deps): bump github.com/docker/docker (#5315) (#5323) e15600804f60722195d192c7c9ae6b5bb0503032 (Jackie Elliott)
* Update addEventHandler return values eda8335f6a91872b7e93686cbe850c1e85ba050f (jaellio)
* build(deps): bump helm.sh/helm/v3 from 3.10.3 to 3.11.1 (#5283) 2d9d8a90c9404136822570ffb7d87567ab0e6630 (dependabot[bot])
* [backport] build(deps): bump github.com/hashicorp/vault from 1.12.0 to 1.12.5 (#5305) 00248280d2c0a2923398a0d6a0e22120a79aa230 (Jackie Elliott)
* [backport] build(deps): bump github.com/containerd/containerd from 1.6.6 to 1.6.18 (#5286) (#5304) 60285f9fc0fb0870af8cc3d88fd795c93cacd1ae (Jackie Elliott)
* [backport] Add more robust CRD conversion patching (#5303) c55b7db880f6b400c8983e900e44938e1574fa19 (Jackie Elliott)
* fix(): remove support for incompatible tls versions for envoy TLSMaxProtocolVersion (#5298) 00fd7e30a57acb18d0000b73f16ec529f087586b (Whitney Griffith)
* fix(): reduce minimum tls version for osm controller, verifier, health (#5292) 1a9b0678322aa708144e0e63c1b62dd776648185 (Whitney Griffith)
