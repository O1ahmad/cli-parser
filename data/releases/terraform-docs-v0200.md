# Terraform-docs - v0.20.0

**Release Name**: v0.20.0
**Published**: 2025-04-04T21:18:17Z
**Repository**: https://github.com/terraform-docs/terraform-docs

---

## Notable Updates

Add preliminary support OpenTofu, thanks to @jamesgeddes! We are now able to extract header and footer from `.tofu` files and generally make `.tofu` file a known filetype to terraform-docs.

> [!NOTE]  
> With this release, we are still not able to read and parse all the `.tofu` files to extract all the other information, such as inputs, outputs, providers, etc. 

## Changelog

### Features
* bb09818 add support for .tofu files

### Dependency updates
* 006ff31 chore(deps): bump golang.org/x/crypto from 0.27.0 to 0.31.0
* e470746 chore(deps): bump golang.org/x/net from 0.29.0 to 0.33.0
* adb8099 chore(deps): bump golang.org/x/net from 0.33.0 to 0.36.0
* 73ee296 chore(deps): bump library/alpine from 3.20.3 to 3.21.3
* 06ca95c chore(deps): bump library/alpine in /scripts/release
* 616bff0 chore(deps): bump library/golang from 1.23.1-alpine to 1.23.4-alpine

### Chores
* a22bdbe Fix typo in insert-output-to-file.md
* cf462c5 Release version v0.20.0
* 8c170f2 Update typo in pre-commit-hooks.md
* 983e98a chore: bump golang to 1.24.2
* 55d8916 chore: bump version to v0.20.0-alpha
* 93c1839 chore: update staticcheck to 2025.1.1

## Docker images

- `docker pull quay.io/terraform-docs/terraform-docs:latest`
- `docker pull quay.io/terraform-docs/terraform-docs:0.20.0`

## Contributors

Very special thanks to the contributors.

- @davejagoda
- @triangle-man
- @jamesgeddes 
- @khos2ow
- @sylim2357
- @pascal-hofmann
- @dependabot%5Bbot%5D
- @terraform-docs-bot

