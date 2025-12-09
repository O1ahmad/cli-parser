# The Update Framework (TUF) - v6.0.0

**Release Name**: v6.0.0
**Published**: 2025-03-11T10:41:57Z
**Repository**: https://github.com/theupdateframework/python-tuf

---

This release is not strictly speaking an API break from 5.1 but it does contain some
major internal changes that users should be aware of when upgrading.

### Changed

* ngclient: urllib3 is used as the HTTP library by default instead of requests (#2762,
  #2773, #2789)
  * This removes dependencies on `requests`, `idna`, `charset-normalizer` and `certifi`
  * The deprecated RequestsFetcher implementation is available but requires selecting
    the fetcher at Updater initialization and explicitly depending on requests
* ngclient: TLS certificate source was changed. Certificates now come from operating
  system certificate store instead of `certifi` (#2762)
* ngclient: The updater can now initialize from embedded initial root metadata every
  time. Users are recommended to provide the `bootstrap` argument to Updater (#2767)
* Test infrastructure has improved and should now be more usable externally, e.g. in
  distro test suites (#2749)

