# Kairos - v3.5.10

**Release Name**: v3.5.10
**Published**: 2025-11-28T09:46:15Z
**Repository**: https://github.com/kairos-io/kairos

---

Bump init to 0.5.29
    
This brings a patched immucore in order to fix an issue when rsyncing
binded dirs from RO images into persistent state dirs, if the
destination is a symlink it would overwrite it, even if the destination
was newer.

This updates the rsync flags to use --update which will check the mtime
before overwriting those files

**Full Changelog**: https://github.com/kairos-io/kairos/compare/v3.5.9...v3.5.10