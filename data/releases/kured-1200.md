# Kured - 1.20.0

**Release Name**: Kured 1.20.0
**Published**: 2025-08-30T16:30:08Z
**Repository**: https://github.com/kubereboot/kured

---

## What's Changed
* Update Kured to support kubernetes 1.34 by @evrardjp in https://github.com/kubereboot/kured/pull/1190
* add golangci lint by @7h3-3mp7y-m4n in https://github.com/kubereboot/kured/pull/1140
* chore: update release by @evrardjp in https://github.com/kubereboot/kured/pull/1192

## New Contributors
* @7h3-3mp7y-m4n made their first contribution in https://github.com/kubereboot/kured/pull/1140

**Full Changelog**: https://github.com/kubereboot/kured/compare/1.19.0...1.20.0

## Kubernetes Version Compatibility

The daemon image contains a 0.33.x k8s.io/{client-go,kubectl} for the purposes of maintaining the lock and draining worker nodes. Kubernetes aims to provide forwards & backwards compatibility of one minor version between client and server, so this should work on 1.32.x, 1.33.x and 1.34.x

## Important note about the manifest name

Going forward, we will use the name kured-<version>-combined.yaml instead of dockerhub, as we are not using dockerhub anymore. Please update your automation tools!

## Get involved

As an open source project, we are based on a community of volunteers. Help is always welcomed, at least so we don't feel alone caring about the reboot of your nodes :)

Don't hesitate to onboard by tackling issues labeled as "good-first-issue" in our repositories (or harder ones if you like the challenge!), reviewing patches, improving the documentation, maintaining the charts, or help producing releases...
There are plenty of places you can contribute, and all you need to get started is your motivation to be one of us :)
You can contact us on slack if you want.

Thanks a lot to everyone who contributed to kured since last release!