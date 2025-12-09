# Kubeflow - v1.10.0

**Release Name**: v1.10.0
**Published**: 2025-03-25T21:59:50Z
**Repository**: https://github.com/kubeflow/kubeflow

---

This release was cut for [Kubeflow Platform](https://www.kubeflow.org/docs/started/introduction/#what-is-kubeflow-platform) version [__1.10.0__](https://www.kubeflow.org/docs/releases/kubeflow-1.10/).

__NOTE:__ the following release notes are __only__ for the components in the `kubeflow/kubeflow` repo.

## Significant Changes

* feat: update notebook server images by @thesuperzapper in https://github.com/kubeflow/kubeflow/pull/7687
* chore: migrate docker images to ghcr by @ederign and @thesuperzapper in https://github.com/kubeflow/kubeflow/pull/7706

## Features

* feat(crud-web-apps): Add Prometheus metrics by @rgildein in https://github.com/kubeflow/kubeflow/pull/7634
* feat(central-dashboard): Add Prometheus metrics with prom-client by @rgildein in https://github.com/kubeflow/kubeflow/pull/7639
* feat: use rootless base image for nb-controller and pod-default by @thesuperzapper in https://github.com/kubeflow/kubeflow/pull/7686
* feat: update gaudi notebooks to version 1.19.2 by @tkatila in https://github.com/kubeflow/kubeflow/pull/7680

## Fixes

* fix: running code-server notebook behind proxy by @thesuperzapper in https://github.com/kubeflow/kubeflow/pull/7658
* fix: add container securityContext to profile-controller and kfam by @biswassri in https://github.com/kubeflow/kubeflow/pull/7669

## Code Health

* chore: update node in crud-web-apps from 12 to 16 by @tariq-hasan in https://github.com/kubeflow/kubeflow/pull/7637
* fix: stop using gcr.io registry for kube-rbac-proxy by @kimwnasptd in https://github.com/kubeflow/kubeflow/pull/7678
* Remove unused files by @thesuperzapper in https://github.com/kubeflow/kubeflow/pull/7643
* Improve README and GitHub issue templates by @thesuperzapper in https://github.com/kubeflow/kubeflow/pull/7642

## New Contributors
* @rgildein made their first contribution in https://github.com/kubeflow/kubeflow/pull/7634
* @tariq-hasan made their first contribution in https://github.com/kubeflow/kubeflow/pull/7637

**Full Changelog**: https://github.com/kubeflow/kubeflow/compare/v1.9.2...v1.10.0