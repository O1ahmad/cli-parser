# CubeFS - v3.5.2

**Release Name**: Release v3.5.2 - 2025/07/31
**Published**: 2025-07-31T08:04:33Z
**Repository**: https://github.com/cubefs/cubefs

---

### **UPGRAGDE NOTICE**

If you are using a CubeFS version earlier than v3.5.0, please refer to the UPGRADE NOTICE in version v3.5.0 for detailed upgrade steps and upgrade to v3.5.0 first.
Upgrade nodes in this order: **master** → **metanode** → **datanode** → **objectnode** → **cli** → **client**.
Upgrade **lcnode** and deploy **flashnode** when needed.

Clients should use versions later than 3.2.0. Older versions need to be upgraded promptly; otherwise, there will be a risk of compromising stability.

### **Main Feature**
+ `master/lcnode`: Lifecycle adds filtering rule based on file size. (#3893, @Victor1319)
+ `master`: dp decommission support priority&concurrency control. (#3891, @shuqiang-zheng)
+ `master`: Add master replica abnormality alarm. (#3882, @zhumingze1108)
+ `master`: Add disk decommission success alarm. (#3886, @zhumingze1108)
+ `meta`: Support mp reload capability. (#3894, @leonrayang)
+ `meta`: Volume file size distribution statistics. (#3884, @M1eyu2018,  @zhumingze1108)
+ `client`: Implement client pre-reading function. (#3889, @yanbin027, @Victor1319)
+ `client`: Client delay monitoring statistics. (#3885, @M1eyu2018,  @aaronwu2010)
+ `data`: Bad disk detection and lost disk discovery. (#3878, @zhumingze1108)
+ `data`: Support asynchronous limitio restrictions. (#3881, @zhumingze1108)
+ `master/data/meta/cli`: dp and mp read-only reasons display. (#3880, @zhumingze1108)

### **Enhance**
+ `all`: Remove the part of the code that uses datanode as cache. (#3888, @Victor1319)
+ `master`: DataNode&Disk&dp Decommission logic optimization. (#3891, @shuqiang-zheng, @zhumingze1108)
+ `meta`: Optimize metanode memory usage. (#3892, @Victor1319)
+ `data`: Optimize datanode memory usage. (#3887, @aaronwu2010)
+ `data`: Optimize and repair the process of tinyDeleteRecord synchronization logic. (#3890, @Victor1319)
+ `cli`: cli datapartition check display optimization. (#3879, @zhumingze1108)

### **Bugfix**
* `master/data`: Repair process blocked by host0 replica. (@shuqiang-zheng)
* `master/raft`: Fixed the issue of dp no leader caused by failure to add raft members during decommission process. (@shuqiang-zheng)