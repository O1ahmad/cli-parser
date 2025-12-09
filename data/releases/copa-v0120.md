# Copa - v0.12.0

**Release Name**: v0.12.0
**Published**: 2025-11-03T06:52:01Z
**Repository**: https://github.com/project-copacetic/copacetic

---

## Notable Changes
* 🧩 **Experimental [App-level Patching](https://project-copacetic.github.io/copacetic/website/next/app-level-patching):** Now supports Python and Node.js applications!  
* 🐳 **Docker Build Integration:** Use the new [`generate`](https://project-copacetic.github.io/copacetic/website/next/docker-build) command to patch images. This provides support for any Docker CLI flags.
* 📁 **Local Output for Multi-Platform Patching:** Added support for the `--oci-dir` flag to store patched artifacts locally when performing [multi-platform patching](https://project-copacetic.github.io/copacetic/website/next/multiplatform-patching).  
* 🛠️ **Enhanced End-of-Life (EOL) Checks:** Improved support through `--exit-on-eol` and `--eol-api-url` flags for customizable [EOL validation](https://project-copacetic.github.io/copacetic/website/next/faq#how-does-copa-check-for-eol-status).

## Changelog
* 5b7b435922b0f24e9ecd5f61fafd5ee404c36091 chore: cherry pick fixes for v0.12.0 and final release (#1366)
* 3efb1aac1e4fde9f777723f29b159e5e7a89c23f chore: cherry pick fixes for v0.12.0 rc3 (#1360)
* 134fbc15e29bad4f70cb6dbdf8bea42c2c86a1c5 chore: cherry pick fixes for v0.12.0 rc2 (#1355)

