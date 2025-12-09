# Buildpacks - v0.39.0

**Release Name**: pack v0.39.0
**Published**: 2025-11-27T15:48:18Z
**Repository**: https://github.com/buildpacks/pack

---

## Prerequisites

- A container runtime such as [Docker](https://www.docker.com/get-started) or [podman](https://podman.io/getting-started/) must be available to execute builds.

## Install

For instructions on installing `pack`, see our [installation docs](https://buildpacks.io/docs/tools/pack/cli/install/).

## Run

Run the command `pack`.

You should see the following output

```text
CLI for building apps using Cloud Native Buildpacks

Usage:
  pack [command]

Available Commands:
  build                 Generate app image from source code
  builder               Interact with builders
  buildpack             Interact with buildpacks
  extension             Interact with extensions
  config                Interact with your local pack config file
  inspect               Show information about a built app image
  stack                 (deprecated) Interact with stacks
  rebase                Rebase app image with latest run image
  sbom                  Interact with SBoM
  completion            Outputs completion script location
  report                Display useful information for reporting an issue
  version               Show current 'pack' version
  help                  Help about any command

Flags:
      --force-color   Force color output
  -h, --help          Help for 'pack'
      --no-color      Disable color output
  -q, --quiet         Show less output
      --timestamps    Enable timestamps in output
  -v, --verbose       Show more output
      --version       Show current 'pack' version

Use "pack [command] --help" for more information about a command.
```

## Info

Builders created with this release of the pack CLI contain [lifecycle v0.20.19](https://github.com/buildpack/lifecycle/releases/tag/v0.20.19) by default.

## Changelog

### Features

* Updating lifecycle version to v0.20.19 (#2481 by @jjbustamante)
* Use Docker API version negotiation instead of hardcoded version (#2474 by @jjbustamante)
* When fetching lifecycle image, use a platform-specific digest (#2467 by @natalieparellano)
* fix: update lifecycle API validation for experimental flag solve issue #2414 (#2432 by @vky5)
* Update imgutil to improve containerd storage driver performance (#2427 by @jabrown85)
* Fix #2405: Add template parameter to GitHub issue URL (#2407 by @jjbustamante)
* Added the first tag argument (#2394 by @dgannon991)

## Contributors

We'd like to acknowledge that this release wouldn't be as good without the help of the following amazing contributors:

@dependabot[bot], @dgannon991, @jabrown85, @jjbustamante, @natalieparellano, @vky5
