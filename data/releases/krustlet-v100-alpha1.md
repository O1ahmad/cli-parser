# Krustlet - v1.0.0-alpha.1

**Release Name**: v1.0.0-alpha.1
**Published**: 2021-07-27T17:06:02Z
**Repository**: https://github.com/krustlet/krustlet

---

# v1.0.0-alpha.1

Krustlet v1.0.0 is the first alpha release of 1.0! This marks the the start of API and feature stability to Krustlet. For more information on our roadmap to 1.0, please read our recently released [blog post](https://deislabs.io/posts/towards-krustlet-v1-cncf/). These release notes contain all breaking changes and new features from 0.7 and will be released with the final 1.0 release as well (for those who go straight from 0.7 to the final 1.0).

## Backwards compatibility

As we move towards 1.0, backwards compatibility and API stability will now be respected. However, during the alpha-beta-RC period, there may be times where we will need to break the API. To be clear, here are the guarantees for each type of release:

- Alpha: No backwards compatibility or API guarantees. However, we do not intend to do any major breaking changes, but we reserve the right to should the need arise
- Beta: Similar to alpha, we will not likely be breaking anything. The one exception would be to solve any bugs, security issues, or missing features found during beta releases
- RC: Backwards compatibility and API stability guarantees will go into effect. Breaking changes will only be considered for showstopper bugs or security issues
- 1.0.0+: No breaking changes will be allowed nor anything that changes backwards compatibility. The major exception to this is for security issues where breaking changes can be allowed based on maintainer consensus. Any other breaking changes will be deferred to a future 2.0 release

## Notable Features/Changes

- `krator` has now been moved to its [own repo](https://github.com/krator-rs/krator) so it can continue to evolve as its own project! This also means that the `kubelet` crate now consumes `krator` directly from crates.io
- Krustlet now has support for device plugins
- Krustlet providers can now implement custom shutdown behavior
- The WASI provider now supports outgoing HTTP calls!
- CSI support now has testing and most outstanding TODOs have been addressed
- `oci-distribution` now supports DockerHub authentication
- Although not a feature, there are now Windows e2e tests so all supported OS versions are now tested
- The `kubelet` crate is now instrumented with the `tracing` crate
- `Provider` implementations can now implement an optional `shutdown` method for graceful shutdown behavior

## Breaking changes

**`krustlet-wasi` binary**

- Due to our migration to the `tracing` crate, the log output is significantly different than 0.7.0

**Rust API**

- The `Ref` type has been replaced with the new `VolumeRef` enum. Each variant wraps the logic of each supported volume type while still allowing access to the underlying type. Any `VolumeRef` can be `mount`ed or `unmount`ed. This should be a cleaner experience for anyone leveraging this part of the API
- `VolumeType` has been removed from the API as part of the `VolumeRef` work
- The `Provider::ProviderState` associated type now has 2 additional bounds required:

Before:

```rust
type ProviderState: 'static + Send + Sync;
```

After:

```rust
type ProviderState: 'static + Send + Sync + PluginSupport + DevicePluginSupport;
```

These new traits are used to require implementation of plugin registries and device plugin support. A minimal implementation (that does nothing) is below:

```rust
struct ProviderState;

impl PluginSupport for ProviderState {}

impl DevicePluginSupport for ProviderState {}
```

Please note that these traits are also now required for implementors of `GenericProvider`.
 
## Known Issues/Missing Features

- Kubernetes networking support. See the "Networking" section for more information
- Modifying a bare pod's image is not implemented. Nothing will error, but Krustlet will not restart the "container"
- TLS bootstrapping does not auto-renew certificates when they are close to expiry

### Networking

After many discussions, we have decided that CNI and 100% native Kubernetes network support will not be part of the 1.0 release. Networking implementations vary wildly between different Krustlet providers and it would be difficult and unwise to try and define a common abstraction at this time. For example, wasmCloud connects using a system called a “lattice” which can consist of an arbitrary graph of connected hosts. Whereas the CRI provider relies on the CNI spec implementations built in to many Kubernetes distros. Not only are we at a point where we need to understand how more complex networking should work, but the same discussions involve things like sidecars, service meshes, and so on. As a result, we decided to let you handle your own networking here, which you can do, while the community understands what's the best path forward with these more complex interactions. 

Our hope is that once we have several different networking examples from various providers, it will be easier to add in a common abstraction at this time. Waiting on that information would only introduce additional delay for releasing Krustlet as an otherwise stable and production-ready (though still bleeding edge) project.

## What's next?

Our next anticipated version is 1.0.0-alpha.2 after we finish the remaining tasks in the [1.0 milestone](https://github.com/deislabs/krustlet/milestone/6)

## Thanks

We want to express a huge thanks to all of those in the community who have helped the project evolve to this point. We appreciate your efforts in making this project a success.

### Contributors to 1.0

If we missed you, let us know!

- @VishnuJin
- @bacongobbler
- @cmhamakawa
- @ereslibre
- @fibonacci1729
- @flavio
- @gdesmott
- @itowlson
- @jdolitsky
- @kate-goldenring
- @kesselborn
- @kflansburg
- @lfrancke
- @radu-matei
- @siegfriedweber
- @soenkeliebau
- @thomastaylor312
- @tot0

## Installation

Download Krustlet 1.0.0-alpha.1:

- [checksum file](https://krustlet.blob.core.windows.net/releases/checksums-v1.0.0-alpha.1.txt)
- [Linux amd64](https://krustlet.blob.core.windows.net/releases/krustlet-v1.0.0-alpha.1-linux-amd64.tar.gz)
- [Linux aarch64](https://krustlet.blob.core.windows.net/releases/krustlet-v1.0.0-alpha.1-linux-aarch64.tar.gz)
- [MacOS amd64](https://krustlet.blob.core.windows.net/releases/krustlet-v1.0.0-alpha.1-macos-amd64.tar.gz)
- [Windows 64-bit](https://krustlet.blob.core.windows.net/releases/krustlet-v1.0.0-alpha.1-windows-amd64.tar.gz)

Check out our [installation docs](https://github.com/krustlet/krustlet/blob/main/docs/intro/install.md) for information on how to install Krustlet.
