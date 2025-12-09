# OpenELB - v0.6.0

**Release Name**: OpenELB v0.6.0
**Published**: 2024-06-14T08:45:18Z
**Repository**: https://github.com/openelb/openelb

---

## What's Changed
* Add version info by @renyunkang in https://github.com/openelb/openelb/pull/298
* allow endpoint nodeName to be empty by @renyunkang in https://github.com/openelb/openelb/pull/301
* add CIDR range for NICs in layer2 by @chaunceyjiang in https://github.com/openelb/openelb/pull/303
* feat(bgp): add method to configure BGP policies by @amalthundiyil in https://github.com/openelb/openelb/pull/292
* chore(deploy): 🔧 Tolerate node-role.kubernetes.io/control-plane:NoSch… by @t106362512 in https://github.com/openelb/openelb/pull/313
* add validation for afisafi config when addpaths is set in bgppeer by @AnuragThePathak in https://github.com/openelb/openelb/pull/311
* docs: Fix adopters img link by @alecrajeev in https://github.com/openelb/openelb/pull/321
* chore: migrate from k8s.gcr.io to registry.k8s.io by @ahmedwaleedmalik in https://github.com/openelb/openelb/pull/326
* Add an http server for web ui by @AnuragThePathak in https://github.com/openelb/openelb/pull/290
* sync vip configmap by @renyunkang in https://github.com/openelb/openelb/pull/304
* Refactor openelb controller by @renyunkang in https://github.com/openelb/openelb/pull/332
* refactor openelb bgp speaker by @renyunkang in https://github.com/openelb/openelb/pull/335
* Cleanup useless code by @chaunceyjiang in https://github.com/openelb/openelb/pull/340
* refactor openelb vip speaker by @renyunkang in https://github.com/openelb/openelb/pull/338
* add controller ipam unit test by @renyunkang in https://github.com/openelb/openelb/pull/344
* Merge the changes of the refactor branch by @renyunkang in https://github.com/openelb/openelb/pull/347
* Add openelb e2e test by @renyunkang in https://github.com/openelb/openelb/pull/346
* chore: integrate e2e test into the workflow by @renyunkang in https://github.com/openelb/openelb/pull/350
* remove default eip webhook by @cherryFloris in https://github.com/openelb/openelb/pull/348
* fix: upgrade controller-gen by @renyunkang in https://github.com/openelb/openelb/pull/349
* allocate eip to specified namespace by @cherryFloris in https://github.com/openelb/openelb/pull/352
* Add PITS Global Data Recovery Services as an adopter by @pheianox in https://github.com/openelb/openelb/pull/356
* add test case by @cherryFloris in https://github.com/openelb/openelb/pull/357
* fix README typo by @alfajorcito in https://github.com/openelb/openelb/pull/327
* the port of the keepalived process is now configurable by @EmielBruijntjes in https://github.com/openelb/openelb/pull/355
* build(deps): bump k8s.io/client-go from 0.18.2 to 0.18.14 by @dependabot in https://github.com/openelb/openelb/pull/374
* Merge refactor-ospp to refactor by @renyunkang in https://github.com/openelb/openelb/pull/377
* Refactor Layer2 Speaker by @renyunkang in https://github.com/openelb/openelb/pull/380
* build(deps): bump google.golang.org/grpc from 1.31.0 to 1.56.3 by @dependabot in https://github.com/openelb/openelb/pull/376
* build(deps): bump golang.org/x/net from 0.0.0-20210525063256-abc453219eb5 to 0.17.0 by @dependabot in https://github.com/openelb/openelb/pull/375
* update dependant by @renyunkang in https://github.com/openelb/openelb/pull/386
* update dependant & Dockerfile by @renyunkang in https://github.com/openelb/openelb/pull/388
* build(deps): bump the go_modules group group with 3 updates by @dependabot in https://github.com/openelb/openelb/pull/387
* switch to golang:alpine as builder by @renyunkang in https://github.com/openelb/openelb/pull/389
* update charts && update file tree by @renyunkang in https://github.com/openelb/openelb/pull/394
* build(deps): bump google.golang.org/protobuf from 1.30.0 to 1.33.0 by @dependabot in https://github.com/openelb/openelb/pull/396
* Merge remote-tracking branch 'upstream/master' into refactor by @renyunkang in https://github.com/openelb/openelb/pull/395
* upgrade controller runtime dependencies by @renyunkang in https://github.com/openelb/openelb/pull/399
* refactor speaker by @renyunkang in https://github.com/openelb/openelb/pull/402
* remove docker dep by @renyunkang in https://github.com/openelb/openelb/pull/403
* build(deps): bump golang.org/x/net from 0.17.0 to 0.23.0 in the go_modules group across 1 directory by @dependabot in https://github.com/openelb/openelb/pull/407
* refactor vip by @renyunkang in https://github.com/openelb/openelb/pull/408
* merge refactor branch into master by @renyunkang in https://github.com/openelb/openelb/pull/409
* remove images build for linux/arm/v6 by @renyunkang in https://github.com/openelb/openelb/pull/411
* update docker images by @renyunkang in https://github.com/openelb/openelb/pull/412
* uniform log format by @renyunkang in https://github.com/openelb/openelb/pull/413
* optimize controller recycling ip by @renyunkang in https://github.com/openelb/openelb/pull/418
* chore: remove refs to deprecated io/ioutil by @testwill in https://github.com/openelb/openelb/pull/419
* keepalive speaker clear datas when stopped by @renyunkang in https://github.com/openelb/openelb/pull/420
* update charts & update changelog by @renyunkang in https://github.com/openelb/openelb/pull/422
* fix iprange cidr parsing results by @renyunkang in https://github.com/openelb/openelb/pull/424
* fix: ipam specify a different IP by @renyunkang in https://github.com/openelb/openelb/pull/427
* skip existing records when handling service by @renyunkang in https://github.com/openelb/openelb/pull/434
* update charts by @renyunkang in https://github.com/openelb/openelb/pull/435
* determine if the speaker is registered by @renyunkang in https://github.com/openelb/openelb/pull/431
* delete a single record instead of the entire instance by @renyunkang in https://github.com/openelb/openelb/pull/432
* update images tag by @renyunkang in https://github.com/openelb/openelb/pull/436

## New Contributors
* @t106362512 made their first contribution in https://github.com/openelb/openelb/pull/313
* @AnuragThePathak made their first contribution in https://github.com/openelb/openelb/pull/311
* @alecrajeev made their first contribution in https://github.com/openelb/openelb/pull/321
* @ahmedwaleedmalik made their first contribution in https://github.com/openelb/openelb/pull/326
* @cherryFloris made their first contribution in https://github.com/openelb/openelb/pull/348
* @pheianox made their first contribution in https://github.com/openelb/openelb/pull/356
* @alfajorcito made their first contribution in https://github.com/openelb/openelb/pull/327
* @EmielBruijntjes made their first contribution in https://github.com/openelb/openelb/pull/355
* @dependabot made their first contribution in https://github.com/openelb/openelb/pull/374
* @testwill made their first contribution in https://github.com/openelb/openelb/pull/419

**Full Changelog**: https://github.com/openelb/openelb/compare/v0.5.1...v0.6.0