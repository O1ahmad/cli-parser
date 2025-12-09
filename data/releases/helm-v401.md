# Helm - v4.0.1

**Release Name**: Helm v4.0.1
**Published**: 2025-11-24T20:31:57Z
**Repository**: https://github.com/helm/helm

---

Helm v4.0.1 is a patch release. Users are encouraged to upgrade for the best experience. Users are encouraged to upgrade for the best experience.

The community keeps growing, and we'd love to see you there!

- Join the discussion in [Kubernetes Slack](https://kubernetes.slack.com):
  -  for questions and just to hang out
  -  for discussing PRs, code, and bugs
- Hang out at the Public Developer Call: Thursday, 9:30 Pacific via [Zoom](https://zoom.us/j/696660622)
- Test, debug, and contribute charts: [ArtifactHub/packages](https://artifacthub.io/packages/search?kind=0)

## Installation and Upgrading

Download Helm v4.0.1. The common platform binaries are here:

- [MacOS amd64](https://get.helm.sh/helm-v4.0.1-darwin-amd64.tar.gz) ([checksum](https://get.helm.sh/helm-v4.0.1-darwin-amd64.tar.gz.sha256sum) / a8d1ca46c3ff5484b2b635dfc25832add4f36fdd09cf2a36fb709829c05b4112)
- [MacOS arm64](https://get.helm.sh/helm-v4.0.1-darwin-arm64.tar.gz) ([checksum](https://get.helm.sh/helm-v4.0.1-darwin-arm64.tar.gz.sha256sum) / 8e0b9615cf72a62faaa0cfc0e22115f05bcddfd3d7ee58406ef97bc1ba563ae8)
- [Linux amd64](https://get.helm.sh/helm-v4.0.1-linux-amd64.tar.gz) ([checksum](https://get.helm.sh/helm-v4.0.1-linux-amd64.tar.gz.sha256sum) / e0365548f01ed52a58a1181ad310b604a3244f59257425bb1739499372bdff60)
- [Linux arm](https://get.helm.sh/helm-v4.0.1-linux-arm.tar.gz) ([checksum](https://get.helm.sh/helm-v4.0.1-linux-arm.tar.gz.sha256sum) / b946401f857de078c744990188f8f664ecb1c72cdafde1ed239020fa3bb2fc3c)
- [Linux arm64](https://get.helm.sh/helm-v4.0.1-linux-arm64.tar.gz) ([checksum](https://get.helm.sh/helm-v4.0.1-linux-arm64.tar.gz.sha256sum) / 959fa52d34e2e1f0154e3220ed5f22263c8593447647a43af07890bba4b004d1)
- [Linux i386](https://get.helm.sh/helm-v4.0.1-linux-386.tar.gz) ([checksum](https://get.helm.sh/helm-v4.0.1-linux-386.tar.gz.sha256sum) / 6a358de71c8dc2cf4a7946930ff9a70a7a3716531e64093a88182f64bdaea5a3)
- [Linux ppc64le](https://get.helm.sh/helm-v4.0.1-linux-ppc64le.tar.gz) ([checksum](https://get.helm.sh/helm-v4.0.1-linux-ppc64le.tar.gz.sha256sum) / 29ef01eed29b3ba676cf6db45dc90b50e07f2b5ec4b1ea40071326bff4922a4e)
- [Linux s390x](https://get.helm.sh/helm-v4.0.1-linux-s390x.tar.gz) ([checksum](https://get.helm.sh/helm-v4.0.1-linux-s390x.tar.gz.sha256sum) / ecf11996bd01a483eca01aa258a58f9e3b3d8e732cd5c84d6975d51ab2abf538)
- [Linux riscv64](https://get.helm.sh/helm-v4.0.1-linux-riscv64.tar.gz) ([checksum](https://get.helm.sh/helm-v4.0.1-linux-riscv64.tar.gz.sha256sum) / e9a1ce6aa004027ba0349982279b0ecab847ddc51b961b963e64eb800de3ec6c)
- [Windows amd64](https://get.helm.sh/helm-v4.0.1-windows-amd64.zip) ([checksum](https://get.helm.sh/helm-v4.0.1-windows-amd64.zip.sha256sum) / a976ee9f3016ae86d8948c0a6d3fc5ed7489cd264cffdbff4860bd97120bd256)
- [Windows arm64](https://get.helm.sh/helm-v4.0.1-windows-arm64.zip) ([checksum](https://get.helm.sh/helm-v4.0.1-windows-arm64.zip.sha256sum) / 5ecbcd8e50577a325e22d365cd4c4de2e2bd014d81f73b356dbd4f7e6c2427fb)

The [Quickstart Guide](https://helm.sh/docs/intro/quickstart/) will get you going from there. For **upgrade instructions** or detailed installation notes, check the [install guide](https://helm.sh/docs/intro/install/). You can also use a [script to install](https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3) on any system with `bash`.

## What's Next

- 3.19.3 and 4.0.2 are the next patch releases and will be on December 10, 2025
- 3.20.0 and 4.1.0 is the next minor releases and will be on January 21, 2026

## Changelog

- Copy adopted resource info 12500dd401faa7629f30ba5d5bff36287f3e94d3 (George Jenkins)
- fixup test 1cf3841142a333c6e4f6bf935075fdaff7beb2ba (George Jenkins)
- logs 32e2d08c45cf1f9fedb2462a780d9f475d373729 (George Jenkins)
- fix 4b6472ffb042a2c76c5323b9bfb1e8000cb3fd1e (George Jenkins)
- fix: Use server-side apply for object create during update 9dfe3b35ec7fb16b941c5904c8b8dee716cc225a (George Jenkins)
- Fix kube client logging 861adc2f4a14e96bc5c627a6c557d80461777735 (Matt Farina)
- update tests b2f78726956ba79c0dfde538fa604c6a8e709a75 (yxxhero)
- Refactor environment variable expansion in PrepareCommands and update tests 77f97a169efda4e2c50453b4da4cee1a7e98af74 (yxxhero)
- Fix syntax errors in the document a156195c35525cfaf404058b0f9aa61610e9e791 (Fish-pro)
- fix: correct LDFLAGS path for default Kubernetes version 2c0dcda29b56f1e65098a4a2acb3c384734721af (Benoit Tigeot)
