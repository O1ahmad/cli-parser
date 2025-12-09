# ContainerSSH - v0.5.2

**Release Name**: v0.5.2
**Published**: 2025-01-19T18:20:04Z
**Repository**: https://github.com/ContainerSSH/ContainerSSH

---

## What's Changed
* Bump github.com/gorilla/schema from 1.2.1 to 1.4.1 by @dependabot in https://github.com/ContainerSSH/ContainerSSH/pull/608
* Bump github.com/go-git/go-git/v5 from 5.1.0 to 5.13.0 by @dependabot in https://github.com/ContainerSSH/ContainerSSH/pull/625
* Bump github.com/oschwald/geoip2-golang from 1.9.0 to 1.11.0 by @dependabot in https://github.com/ContainerSSH/ContainerSSH/pull/628
* Bump golang.org/x/crypto from 0.23.0 to 0.32.0
* Move handshake success processing outside the callbacks (https://github.com/ContainerSSH/libcontainerssh/pull/671)
   Note: While this change was prompted by crypto/ssh 's CVE-2024-45337 , ContainerSSHs handling of public key authentication did not allow any additional access, this change was made to make the code and handling clearer in light of the published vulnerability.

* Deprecate libcontainerssh, all library code is now under the main ContainerSSH repository, `go.containerssh.io/libcontainerssh` should be changed to `go.containerssh.io/containerssh`

**Full Changelog**: https://github.com/ContainerSSH/ContainerSSH/compare/v0.5.1...v0.5.2