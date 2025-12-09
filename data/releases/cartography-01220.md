# Cartography - 0.122.0

**Release Name**: 0.122.0
**Published**: 2025-12-08T05:48:22Z
**Repository**: https://github.com/cartography-cncf/cartography

---

## What's Changed
* refactor: PagerDuty tests by @jychp in https://github.com/cartography-cncf/cartography/pull/2077
* fix(azure): #2078 factory_id bug by @achantavy in https://github.com/cartography-cncf/cartography/pull/2079
* fix: Reduce ECR layer batch size to avoid Neo4j OOM by @kunaals in https://github.com/cartography-cncf/cartography/pull/2080
* chore: bump python from `975a1e2` to `c299e10` by @dependabot[bot] in https://github.com/cartography-cncf/cartography/pull/2089
* feat: ontology for inactive users + fix github mapping + inactive rule by @jychp in https://github.com/cartography-cncf/cartography/pull/2076
* feat(ontology): add APIKey by @achantavy in https://github.com/cartography-cncf/cartography/pull/2091
* rules: shai hulud attack rule by @jychp in https://github.com/cartography-cncf/cartography/pull/2090
* feat(vuln mgmt): Extra indexes on fields for vulnerability management by @kunaals in https://github.com/cartography-cncf/cartography/pull/2083
* fix: make shai-hulud query only return vulnerable pkgs by @achantavy in https://github.com/cartography-cncf/cartography/pull/2093
* chore: bump the minor-and-patch group with 2 updates by @dependabot[bot] in https://github.com/cartography-cncf/cartography/pull/2087
* chore: bump actions/checkout from 5.0.1 to 6.0.0 by @dependabot[bot] in https://github.com/cartography-cncf/cartography/pull/2088
* feat(kubernetes): KubernetesContainer memory and CPU by @kunaals in https://github.com/cartography-cncf/cartography/pull/2095
* feat(ontology): add ComputeInstance and Container by @jychp in https://github.com/cartography-cncf/cartography/pull/2066
* fix(rules): add missing modules to rules.Module by @jychp in https://github.com/cartography-cncf/cartography/pull/2098
* chore: bump the minor-and-patch group with 4 updates by @dependabot[bot] in https://github.com/cartography-cncf/cartography/pull/2102
* feat: GCP policy_bindings and Permissions Relationship Evaluation Sync by @Daksh1603 in https://github.com/cartography-cncf/cartography/pull/2062
* feat: add google oauth tokens by @jychp in https://github.com/cartography-cncf/cartography/pull/2094
* feat (GCP): Use CAI api as fallback when IAM is disabled by @shyammukund in https://github.com/cartography-cncf/cartography/pull/2096
* fix(gcp): Pass creds GCP by @kunaals in https://github.com/cartography-cncf/cartography/pull/2106
* fix(aws): Add region field to AWS Identity Center and AWS Permission Set Nodes by @shyammukund in https://github.com/cartography-cncf/cartography/pull/2111
* feat(gcp): Fetch predefined IAM roles from quota project for CAI fallback by @kunaals in https://github.com/cartography-cncf/cartography/pull/2115
* fix (AWS): Set RoleHint to include region for PermissionSets/AWS Roles not in us-east-1 by @shyammukund in https://github.com/cartography-cncf/cartography/pull/2114


**Full Changelog**: https://github.com/cartography-cncf/cartography/compare/0.121.0...0.122.0