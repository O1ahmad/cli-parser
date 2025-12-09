# Tremor - v0.13.0-rc.33

**Release Name**: Release v0.13.0-rc.33
**Published**: 2024-10-23T19:53:07Z
**Repository**: https://github.com/tremor-rs/tremor-runtime

---

### New features
* update apache-avro to version 0.17 adding support for nano resolution timestamp logical types in schemas
* Added `graphite-plaintext` tremor codec to support the graphite plaintext line protocol

### Fixes
* gbq connector naming is now `gbq_writer` as it is documented
* fix gbq connector url missing `/`
* fix GELF message-id from auto-increment to random-id in postprocessor/gelf_chunking.rs