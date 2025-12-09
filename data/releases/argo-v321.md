# Argo - v3.2.1

**Release Name**: v3.2.1
**Published**: 2025-11-30T12:32:58Z
**Repository**: https://github.com/argoproj/argo-cd

---

## Quick Start

### Non-HA:

```shell
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/v3.2.1/manifests/install.yaml
```

### HA:

```shell
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/v3.2.1/manifests/ha/install.yaml
```

## Release Signatures and Provenance

All Argo CD container images are signed by cosign.  A Provenance is generated for container images and CLI binaries which meet the SLSA Level 3 specifications. See the [documentation](https://argo-cd.readthedocs.io/en/stable/operator-manual/signed-release-assets) on how to verify.

## Release Notes Blog Post
For a detailed breakdown of the key changes and improvements in this release, check out the [official blog post](https://blog.argoproj.io/argo-cd-v3-0-release-candidate-a0b933f4e58f)

## Upgrading

If upgrading from a different minor version, be sure to read the [upgrading](https://argo-cd.readthedocs.io/en/stable/operator-manual/upgrading/overview/) documentation.

## Changelog
### Bug fixes
* 6dd5e7a6d2df398bd3503da61ecbd7f450c7f392: fix(ui): add null-safe handling for assignedWindows in status panel (cherry-pick #25128 for 3.2) (#25180) (@argo-cd-cherry-pick-bot[bot])
* dabdf39772581fabc4d758e10b71f8e258f6f737: fix(ui): overlapping UI elements and add resource units to tooltips (cherry-pick #24717 for 3.2) (#25225) (@choejwoo)
* cd8df1721cf1eeeae7449005384cadcc7c2ab377: fix: Allow the ISVC to be healthy when the Stopped Condition is False (cherry-pick #25312 for 3.2) (#25318) (@argo-cd-cherry-pick-bot[bot])
* 27c506530836fb77a8242cdb773ae796d7151b31: fix: revert #24197 (cherry-pick #25294 for 3.2) (#25314) (@argo-cd-cherry-pick-bot[bot])
* 29f869c82fc632893707cf53c84057190e23c2f3: fix: the concurrency issue with git detached processing in Repo Server (#25101) (cherry-pick #25127 for 3.2) (#25448) (@dudinea)
* 7bd02d7f02ba267b46a42aedbdb62cce3d62880c: fix:(ui) don't render ApplicationSelector unless the panel is showing (cherry-pick #25201 for 3.2) (#25208) (@argo-cd-cherry-pick-bot[bot])
### Documentation
* c11e67d4bfc97232e9c3b5f70dade40a0d8da493: docs: Document usage of ?. in notifications triggers and fix examples (#25352) (cherry-pick #25418 for 3.2) (#25421) (@argo-cd-cherry-pick-bot[bot])
* a0a18438ab2bc58f19b8396c579123396507a544: docs: Improve switch to annotation tracking docs, clarifying that a new Git commit may be needed to avoid orphan resources - (cherry-pick #25309 for 3.2) (#25338) (@reggie-k)
* 86c99943945e166d8f984e88c568d8de4d79b752: docs: update user content for deleting applications (cherry-pick #25124 for 3.2) (#25174) (@argo-cd-cherry-pick-bot[bot])
### Other work
* 1545390cd822edce2e5ce448a7f1c590d2230b0c: fix(cherry-pick): bump gitops-engine ssd regression (#25226) (@pjiang-dev)

**Full Changelog**: https://github.com/argoproj/argo-cd/compare/v3.2.0...v3.2.1

<a href="https://argoproj.github.io/cd/"><img src="https://raw.githubusercontent.com/argoproj/argo-site/master/content/pages/cd/gitops-cd.png" width="25%" ></a>

