# AWS CLI - 2.0.0dev0

**Release Name**: AWS CLI 2.0.0dev preview release
**Published**: 2018-11-26T06:25:44Z
**Repository**: https://github.com/aws/aws-cli

---

This is the first developer release of AWS CLI v2.0.0.

**The AWS CLI v2.0.0 is not recommended for production use and is offered as a developer release.**

Major features include:

* Improved auto-completion performance
* Add support for resource value auto completion, which can auto complete resources such as Amazon DynamoDB table names, AWS IAM user names, etc.
* Add support for wizards, which allows interactive prompting in order to create and configure AWS resources.
* Add high level `aws ddb` command which includes the `select` and `put` command
* Add `aws logs tail` command for viewing most recent logs in an Amazon CloudWatch Logs group
* Add support for automatically retrieving region via IMDS.
* Add `aws configure import` command to create profiles from credentials CSV generated in the web console.
* Add support for `--output yaml`.
* Add `aws configure list-profiles` command.

Removal of features and backwards incompatible changes:

* Remove support support for python2.6, python3.3, and python3.4.
* Default timestamp to iso8601.  Previously it would display whatever format was returned by the AWS service.
* Remove support for automatically retrieving remote values starting with `http` and `https`.