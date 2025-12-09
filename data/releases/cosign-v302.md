# Cosign - v3.0.2

**Release Name**: v3.0.2
**Published**: 2025-10-10T19:09:58Z
**Repository**: https://github.com/sigstore/cosign

---

# v3.0.2

v3.0.2 is a functionally equivalent release to v3.0.0 and v3.0.1, with a fix for CI to publish signed releases in the new bundle format.

* Note that the `--bundle` flag specifying an output file to write the Sigstore bundle (which contains all relevant verification material) has moved from optional to required in v3.

## Changes

* choose different signature filename for KMS-signed release signatures (#4448)
* Update rekor-tiles version path (#4450)