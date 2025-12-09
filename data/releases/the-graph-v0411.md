# The Graph - v0.41.1

**Release Name**: v0.41.1
**Published**: 2025-11-07T13:38:09Z
**Repository**: https://github.com/graphprotocol/graph-node

---

## v0.41.1

```
$ docker pull graphprotocol/graph-node:v0.41.1
```

### Bug Fix

**Indexing Status Endpoint**

Fixed a regression in v0.41.0 where the indexing status endpoint would return an empty list when querying all subgraphs without specific deployment filters. Reverted an unnecessary optimization that broke this common use case. (https://github.com/graphprotocol/graph-node/pull/6210)