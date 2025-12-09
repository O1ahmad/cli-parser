# Akri - v0.13.8

**Release Name**: v0.13.8
**Published**: 2024-11-20T21:58:06Z
**Repository**: https://github.com/project-akri/akri

---

## Announcing Akri v0.13.8!
Akri v0.13.8 is a pre-release of Akri.

To find out more about Akri, check out our [documentation](https://docs.akri.sh/) and start
[contributing](https://docs.akri.sh/community/contributing) today!

## New Features
The v0.13.8 release contains the following changes:

**Fixes, features, and optimizations**
- feat: Refactor the agent (https://github.com/project-akri/akri/pull/684)
- fix: Add proto build flag to allow option proto fields (https://github.com/project-akri/akri/pull/698)
- opt: Refactor agent followup (https://github.com/project-akri/akri/pull/700)
- opt: Update to use rust 1.79 and apply clippy cleanups (https://github.com/project-akri/akri/pull/703)
- fix: Upgrade serde_yaml (https://github.com/project-akri/akri/pull/701)
- fix: Only add device ID to broker env vars suffix (https://github.com/project-akri/akri/pull/709)
- feat: Add duplicate envs without instance suffix (https://github.com/project-akri/akri/pull/710)
- fix: brokerJob specs to use imagePullPolicy and image tag from values.yaml (https://github.com/project-akri/akri/pull/715)
- fix: Add Helm pre-delete hook to remove configurations before Akri chart cleanup (https://github.com/project-akri/akri/pull/717)

View the [full change log](https://github.com/project-akri/akri/compare/v0.12.20...v.0.13.8)

## Breaking Changes
- Agent refactoring: this release comes with many new improvements to the Akri agent!
  - In order to prevent deletion of existing Instances on Configuration update, the agent now only looks for updates to the capacity and broker capacities.
  - Agent no longer needs access to the CRI socket for slot reconciliation.
  - Added a finalizer to ensure clean-up of resources.
- Update to the Instance CRD to better handle upgrades.

## Known Issues


## Validated With

| Distribution | Version |
|---|---|
| Kubernetes | v1.31.2 |
| Kubernetes | v1.30.6 |
| Kubernetes | v1.29.10 |
| K3s | v1.31.2+k3s1 |
| K3s | v1.30.6+k3s1 |
| K3s | v1.29.10+k3s1 |
| MicroK8s | 1.31/stable |
| MicroK8s | 1.30/stable |
| MicroK8s | 1.29/stable |

## What's next?
Check out our [roadmap](https://docs.akri.sh/community/roadmap) to see the features we are looking forward to!

## Thanks 👏
Thank you everyone in the community who helped Akri get to this release! Your interest and contributions help Akri
prosper.

**⭐ Contributors to v0.13.8 ⭐**
- @CeerDecy
- @melinda-mytra
- @diconico07
- @kate-goldenring
- @yujinkim-msft


(Please send us (`@Yu Jin Kim`) a direct message on
  [Slack](https://kubernetes.slack.com/messages/akri) if we left you out!)

## Installation
Akri is packaged as a Helm chart. Check out our [installation doc](https://docs.akri.sh/user-guide/getting-started) on
how to install Akri.

```
helm repo add akri-helm-charts https://project-akri.github.io/akri/
helm install akri akri-helm-charts/akri --version 0.13.8 \
    # additional configuration
```

## Release history
See [CHANGELOG.md](https://github.com/project-akri/akri/blob/v0.13.8/CHANGELOG.md) for more information on what changed
in this and previous releases.