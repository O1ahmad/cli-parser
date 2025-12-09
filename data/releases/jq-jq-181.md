# jq - jq-1.8.1

**Release Name**: jq 1.8.1
**Published**: 2025-07-01T11:50:06Z
**Repository**: https://github.com/jqlang/jq

---

This is a patch release to fix security, performance, and build issues found in 1.8.0.
Full commit log can be found at <https://github.com/jqlang/jq/compare/jq-1.8.0...jq-1.8.1>.

## Security fixes

- CVE-2025-49014: Fix heap use after free in `f_strftime`, `f_strflocaltime`.
  @wader 499c91bca9d4d027833bc62787d1bb075c03680e
- GHSA-f946-j5j2-4w5m: Fix stack overflow in `node_min_byte_len` of oniguruma.
  @wader 5e159b34b179417e3e0404108190a2ac7d65611c

## CLI changes

- Fix assertion failure when syntax error happens at the end of the query. @itchyny #3350

## Changes to existing functions

- Fix portability of `strptime/1` especially for Windows. @itchyny #3342

## Language changes

- Revert the change of `reduce`/`foreach` state variable in 1.8.0 (#3205).
  This change was reverted due to serious performance regression. @itchyny #3349

## Documentation changes

- Add LICENSE notice of NetBSD's `strptime()` to COPYING. @itchyny #3344

## Build improvements

- Fix build on old Mac with old sed. @qianbinbin #3336
