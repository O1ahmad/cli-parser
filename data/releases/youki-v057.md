# youki - v0.5.7

**Release Name**: v0.5.7
**Published**: 2025-11-05T12:52:53Z
**Repository**: https://github.com/youki-dev/youki

---

<!-- Release notes generated using configuration in .github/release.yml at v0.5.7 -->

# Security Notice

This release addresses two CVEs. An update is recommended.

- [CVE-2025-62161](https://github.com/youki-dev/youki/security/advisories/GHSA-4g74-7cff-xcv8)
    container escape via "masked path" abuse due to mount race conditions
- [CVE-2025-62596](https://github.com/youki-dev/youki/security/advisories/GHSA-vf95-55w6-qmrf)
    The write-target validation for /proc AppArmor label writes (e.g., /proc/self/attr/apparmor/exec) was insufficient, and combined with path substitution during pathname resolution (via shared-mount races) could allow writes to unintended /proc files.

## What's Changed
### 💪 Improvements
* Drop cgroup v1 in github workflows by @utam0k in https://github.com/youki-dev/youki/pull/3284
### 🐛 Bug Fixes
* Waiting on systemd to add intermediate process to cgroup. by @CheatCodeSam in https://github.com/youki-dev/youki/pull/3262
### 🧪 Test improvements and Misc Fixes
* Update/runc 1.3.2 by @n4mlz in https://github.com/youki-dev/youki/pull/3274
### Other Changes
* (auto merged) chore(deps): bump flate2 from 1.1.4 to 1.1.5 in the patch group by @dependabot[bot] in https://github.com/youki-dev/youki/pull/3281
* Release for v0.5.7 by @github-actions[bot] in https://github.com/youki-dev/youki/pull/3282

## New Contributors
* @n4mlz made their first contribution in https://github.com/youki-dev/youki/pull/3274

**Full Changelog**: https://github.com/youki-dev/youki/compare/v0.5.6...v0.5.7