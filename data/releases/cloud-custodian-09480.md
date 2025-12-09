# Cloud Custodian - 0.9.48.0

**Release Name**: 0.9.48.0
**Published**: 2025-12-01T19:04:50Z
**Repository**: https://github.com/cloud-custodian/cloud-custodian

---

## What's Changed
# aws
 - aws - account - add 'ami-block-public-access' filter (#10377)
 - aws - add 'iam-access-key' resource (#10364)
 - aws - add custom replica filter to the secretsmanager resource (#10350)
 - aws - add delete action for subnet (#10296)
 - aws - artifact-domain - fix cross account filter (#10446)
 - aws - cache-cluster - implement the 'upgrade-available' filter (#10361)
 - aws - core - consolidated query parsing (#10388)
 - aws - ebs - add Server-Side Query Filtering  (#10393)
 - aws - firehose - delete action add support for suspended streams (#10397)
 - aws - fsx - delete-file-system support other fsx types (#10391)
 - aws - kafka - cross account filter (#10371)
 - aws - kafka - upgrade-available (#10360)
 - aws - kms - add 'last-rotation' filter (#10363)
 - aws - lambda event source mapping (#10293)
 - aws - r53 domain -  test data fix (#10403)
 - aws - route53 domain - add a detail spec
 - aws - schedule mode - strip version from eventbridge schedule target arn (#10407)
 - aws - secrets manager - Filter on attributes of current version  (#10434)
 - aws - service-quota - Add hard_limit support for service quota management (#10331)
 - aws - ssm-document - support everyone-only in cross-account filter (#10413)
 - aws - wafv2 set logging (#10412)
 - Add VPC Resolver Query Logging Filter (#10167)
 - Adding analytics-association filter for Connect instances (#10275)
 - Adding support for AWS VPC Lattice resources (#10341)
 - feat: add action for app elb (#10248)
 - fix(guardduty): use correct key for administrator account (#10376)
 - Fixing KeyError in Comprehend cross-account filter when resource has no policy (#10355)

# azure
 - azure - AKS / ACI Azure Container Host Enhancements (#10395)
 - azure - add 'elasticache-reserved' resource (#10369)
 - azure - add base Entra ID support and the entraid-user resource (#10357)
 - azure - azure.keyvault-key: fix policy filter due to incompatible sdk update (#10368)
 - azure - keyvault-key - add update action (#9905)
 - azure - update azure mgmt keyvault version (#10352)
 - azure - update azure mgmt security version (#10351)


# core
 - core - add GOVERNANCE.md to document project governance structure  (#10320)


# gcp
 - gcp - add certificatemanager certificate support (#10326)
 - gcp - fix broken secret manager documentation link (#10438)
 - gcp - update metric support for spanner resources (#10374)


# kubernetes
 - kubernetes - enhanced PatchAction with save/restore functionality and improved error handling (#10288)


# releng
 - releng - 2025/10 increment versions and update dependencies (#10383)
 - releng - :seedling:  bump github-actions group across 4 directories with 12 updates (#10410)
 - releng - azure - update azure-mgmt-sql to 3.x (#10421)
 - releng - ensure dependabot scans reusable workflows (#10408)
 - releng - fix ci installation cache check to avoid breakage (#10404)
 - releng - make awscc build script is quiet by default (#10405)
 - releng - update dependencies 2025/11 (#10417)


# tencentcloud:
 - tencentcloud: fix metrics service name, enforce batching limits, and annotate resources with metrics (#10337)


# tools
 - c7n_mailer - ensure template_folders are sorted to get same sha256sum each time (#10387)


# schema changes
- [`aws.elasticache-reserved`](https://cloudcustodian.io/docs/aws/resources/elasticache-reserved.html) added
- [`aws.iam-access-key`](https://cloudcustodian.io/docs/aws/resources/iam-access-key.html) added
- [`aws.lambda-event-source-mapping`](https://cloudcustodian.io/docs/aws/resources/lambda-event-source-mapping.html) added
- [`aws.vpc-lattice-service`](https://cloudcustodian.io/docs/aws/resources/vpc-lattice-service.html) added
- [`aws.vpc-lattice-service-network`](https://cloudcustodian.io/docs/aws/resources/vpc-lattice-service-network.html) added
- [`aws.vpc-lattice-target-group`](https://cloudcustodian.io/docs/aws/resources/vpc-lattice-target-group.html) added
- [`azure.entraid-user`](https://cloudcustodian.io/docs/azure/resources/entraid-user.html) added
- [`gcp.certmanager-certificate`](https://cloudcustodian.io/docs/gcp/resources/certmanager-certificate.html) added
- [`terraform._`](https://cloudcustodian.io/docs/terraform/resources/_.html) added
- `aws.account`
  - added filters: [`ami-block-public-access`](https://cloudcustodian.io/docs/aws/resources/account.html#aws-account-filters-ami-block-public-access)
- `aws.app-elb`
  - added actions: [`delete-listener`](https://cloudcustodian.io/docs/aws/resources/app-elb.html#aws-app-elb-actions-delete-listener)
- `aws.cache-cluster`
  - added filters: [`upgrade-available`](https://cloudcustodian.io/docs/aws/resources/cache-cluster.html#aws-cache-cluster-filters-upgrade-available)
- `aws.connect-instance`
  - added filters: [`analytics-association`](https://cloudcustodian.io/docs/aws/resources/connect-instance.html#aws-connect-instance-filters-analytics-association)
- `aws.kafka`
  - added filters: [`cross-account`](https://cloudcustodian.io/docs/aws/resources/kafka.html#aws-kafka-filters-cross-account), [`upgrade-available`](https://cloudcustodian.io/docs/aws/resources/kafka.html#aws-kafka-filters-upgrade-available)
- `aws.kms-key`
  - added filters: [`last-rotation`](https://cloudcustodian.io/docs/aws/resources/kms-key.html#aws-kms-key-filters-last-rotation)
- `aws.opswork-stack`
  - removed filters: `metrics`
- `aws.secrets-manager`
  - added filters: [`current-version`](https://cloudcustodian.io/docs/aws/resources/secrets-manager.html#aws-secrets-manager-filters-current-version), [`replica-attribute`](https://cloudcustodian.io/docs/aws/resources/secrets-manager.html#aws-secrets-manager-filters-replica-attribute)
- `aws.subnet`
  - added actions: [`delete`](https://cloudcustodian.io/docs/aws/resources/subnet.html#aws-subnet-actions-delete)
- `aws.vpc`
  - added filters: [`resolver-query-logging`](https://cloudcustodian.io/docs/aws/resources/vpc.html#aws-vpc-filters-resolver-query-logging)
- `aws.wafv2`
  - added actions: [`set-logging`](https://cloudcustodian.io/docs/aws/resources/wafv2.html#aws-wafv2-actions-set-logging)
- `azure.keyvault-key`
  - added actions: [`update`](https://cloudcustodian.io/docs/azure/resources/keyvault-key.html#azure-keyvault-key-actions-update)
- `gcp.spanner-backup`
  - removed filters: `metrics`
- `gcp.spanner-database-instance`
  - removed filters: `metrics`


## New Contributors
* @vit-corp made their first contribution in https://github.com/cloud-custodian/cloud-custodian/pull/10351
* @yuzegao made their first contribution in https://github.com/cloud-custodian/cloud-custodian/pull/10337
* @franzramadhan made their first contribution in https://github.com/cloud-custodian/cloud-custodian/pull/10326
* @umairmkhan made their first contribution in https://github.com/cloud-custodian/cloud-custodian/pull/10320
* @linguini-dev made their first contribution in https://github.com/cloud-custodian/cloud-custodian/pull/10296
* @toastdriven made their first contribution in https://github.com/cloud-custodian/cloud-custodian/pull/10369
* @licquia made their first contribution in https://github.com/cloud-custodian/cloud-custodian/pull/10357
* @andrewhibbert made their first contribution in https://github.com/cloud-custodian/cloud-custodian/pull/10387
* @SoyTecnopata made their first contribution in https://github.com/cloud-custodian/cloud-custodian/pull/10288
* @priscila-lugon made their first contribution in https://github.com/cloud-custodian/cloud-custodian/pull/10393
* @ejohn20 made their first contribution in https://github.com/cloud-custodian/cloud-custodian/pull/10395
* @KeisukeYamashita made their first contribution in https://github.com/cloud-custodian/cloud-custodian/pull/10438

**Full Changelog**: https://github.com/cloud-custodian/cloud-custodian/compare/0.9.47.0...0.9.48.0