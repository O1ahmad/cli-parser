# IoTDB - v1.3.5

**Release Name**: Apache IoTDB 1.3.5
**Published**: 2025-09-11T08:47:31Z
**Repository**: https://github.com/apache/iotdb

---

## Improvements
- Storage Module: Optimize user password encryption by changing the algorithm to SHA-256
- ... 

## Bugs
- Fixed the array out-of-bounds exception in cross-Region aggregate query with align by device
- Fixed the error in aggregate queries with `order by time + align by device` for single or multiple devices spanning across Regions
- Fixed the "out of memory" error in query with large TEXT objects + align by device + order by time
- Fixed the issue where the last query with where time > X and time < X was not applied to partitioned table fetching, resulting in failure to hit PartitionCache
- Fixed the error in using change_point function + align by device when single device data spans multiple Regions
- Fixed the OOM (Out of Memory) issue caused by the asynchronous submission queue of pipeTransferFile
- Fixed the memory leak issue in pipe password detection
- For the pipe receiver and during Load, change the behavior of'clear schema cache' to 'update last cache'
- Optimize the loading speed of TsFile when there are a large number of measuring points and the mods file contains deletions of a large number of measuring points
- ...

**Full Changelog**: https://github.com/apache/iotdb/compare/v1.3.4-1...v1.3.5