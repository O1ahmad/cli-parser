# Vault - v1.21.1

**Release Name**: v1.21.1
**Published**: 2025-11-19T17:36:49Z
**Repository**: https://github.com/hashicorp/vault

---

## 1.21.1
### November 20, 2025

SECURITY:

* auth/aws: fix an issue where a user may be able to bypass authentication to Vault due to incorrect caching of the AWS client
* ui: disable scarf analytics for ui builds

CHANGES:

* auth/kubernetes: Update plugin to [v0.23.1](https://github.com/hashicorp/vault-plugin-auth-kubernetes/releases/tag/v0.23.1)
* auth/saml: Update plugin to [v0.7.0](https://github.com/hashicorp/vault-plugin-auth-saml/releases/tag/v0.7.0)
* auth/saml: Update plugin to v0.7.1, which adds the environment variable VAULT_SAML_DENY_INTERNAL_URLS to allow prevention of idp_metadata_url, idp_sso_url, or acs_urls fields from containing URLs that resolve to internal IP addresses
* core: Bump Go version to 1.25.4
* secrets/azure: Update plugin to [v0.25.0+ent](https://github.com/hashicorp/vault-plugin-secrets-azure/releases/tag/v0.25.0+ent)
* secrets/pki: sign-verbatim endpoints no longer ignore basic constraints extension in CSRs, using them in generated certificates if isCA=false or returning an error if isCA=true

IMPROVEMENTS:

* Update github.com/dvsekhvalnov/jose2go to fix security vulnerability CVE-2025-63811.
* api: Added sudo-permissioned `sys/reporting/scan` endpoint which will output a set of files containing information about Vault state to the location specified by the `reporting_scan_directory` config item.
* auth/ldap: Require non-empty passwords on login command to prevent unauthenticated access to Vault.
* core/metrics: Reading and listing from a snapshot are now tracked via the `vault.route.read-snapshot.{mount_point}` and `vault.route.list-snapshot.{mount_point}` metrics.
* license utilization reporting (enterprise): Add metrics for the number of issued PKI certificates.
* policies: add warning about list comparison when using allowed_parameters or denied_parameters
* secret-sync: add parallelization support to sync and unsync operations for secret-key granularity associations
* secrets/pki: Include the certificate's AuthorityKeyID in response fields for API endpoints that issue, sign, or fetch certs.
* sys (enterprise): Add sys/billing/certificates API endpoint to retrieve the number of issued PKI certificates.
* ui/activity (enterprise): Add clarifying text to explain the "Initial Usage" column will only have timestamps for clients initially used after upgrading to version 1.21
* ui/activity (enterprise): Allow manual querying of client usage if there is a problem retrieving the license start time.
* ui/activity (enterprise): Reduce requests to the activity export API by only fetching new data when the dashboard initially loads or is manually refreshed.
* ui/activity (enterprise): Support filtering months dropdown by ISO timestamp or display value.
* ui/activity: Display total instead of new monthly clients for HCP managed clusters
* ui/pki: Adds support to configure `server_flag`, `client_flag`, `code_signing_flag`, and `email_protection_flag` parameters for creating/updating a role.

BUG FIXES:

* activity (enterprise): sys/internal/counters/activity outputs the correct mount type when called from a non root namespace
* auth/approle (enterprise): Role parameter `alias_metadata` now populates alias custom metadata field instead of alias metadata.
* auth/aws (enterprise): Role parameter `alias_metadata` now populates alias custom metadata field instead of alias metadata.
* auth/cert (enterprise): Role parameter `alias_metadata` now populates alias custom metadata field instead of alias metadata.
* auth/github (enterprise): Role parameter `alias_metadata` now populates alias custom metadata field instead of alias metadata.
* auth/ldap (enterprise): Role parameter `alias_metadata` now populates alias custom metadata field instead of alias metadata.
* auth/okta (enterprise): Role parameter `alias_metadata` now populates alias custom metadata field instead of alias metadata.
* auth/radius (enterprise): Role parameter `alias_metadata` now populates alias custom metadata field instead of alias metadata.
* auth/scep (enterprise): Role parameter `alias_metadata` now populates alias custom metadata field instead of alias metadata.
* auth/userpass (enterprise): Role parameter `alias_metadata` now populates alias custom metadata field instead of alias metadata.
* auth: fixed panic when supplying integer as a lease_id in renewal.
* core/rotation: avoid shifting timezones by ignoring cron.SpecSchedule
* core: interpret all new rotation manager rotation_schedules as UTC to avoid inadvertent use of tz-local
* secrets/azure: Ensure proper installation of the Azure enterprise secrets plugin.
* secrets/pki: Return error when issuing/signing certs whose NotAfter is before NotBefore or whose validity period isn't contained by the CA's.
* ui (enterprise): Fix KV v2 not displaying secrets in namespaces.
* ui (enterprise): Fixes login form so input renders correctly when token is a preferred login method for a namespace.
* ui/pki: Fixes certificate parsing of the `key_usage` extension so details accurately reflect certificate values.
* ui/pki: Fixes creating and updating a role so `basic_constraints_valid_for_non_ca` is correctly set.
* ui: Fix KV v2 metadata list request failing for policies without a trailing slash in the path.
* ui: Resolved a regression that prevented users with create and update permissions on KV v1 secrets from opening the edit view. The UI now correctly recognizes these capabilities and allows editing without requiring full read access.
* ui: Update LDAP accounts checked-in table to display hierarchical LDAP libraries
* ui: Update LDAP library count to reflect the total number of nodes instead of number of directories
