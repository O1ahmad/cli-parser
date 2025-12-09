# Lima - v2.0.2

**Release Name**: v2.0.2
**Published**: 2025-11-24T14:28:56Z
**Repository**: https://github.com/lima-vm/lima

---

## Changes

- vz:
  - Fix incompatibility with Fedora 43 (#4384)
- `limactl` CLI:
  - Make errors less scary (#4387)
- Misc:
  - Don't trim whitespace from boot commands (#4381, thanks to @jandubois)

Full changes: https://github.com/lima-vm/lima/milestone/65?closed=1
Thanks to @alexandear @jandubois @norio-nomura @pragneshbagary @unsuman

## Usage
```console
$ limactl create
$ limactl start
...
INFO[0029] READY. Run `lima` to open the shell.

$ lima uname
Linux
```

- - -
The binaries were built automatically on GitHub Actions.
The build log is available for 90 days: https://github.com/lima-vm/lima/actions/runs/19637186442

The sha256sum of the SHA256SUMS file itself is `34404225335c06f30ff7990bb15f28f1fa11588b2ccc0bedc9ff07465a229106` .
- - -
Release manager: @AkihiroSuda 
