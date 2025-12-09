# NATS - v2.12.3-RC.2

**Release Name**: Release v2.12.3-RC.2
**Published**: 2025-12-05T13:24:47Z
**Repository**: https://github.com/nats-io/nats-server

---

## Changelog

Refer to the [2.12 Upgrade Guide](https://docs.nats.io/release-notes/whats_new/whats_new_212) for backwards compatibility notes with 2.11.x.

### Go Version

- 1.25.5 (#7604)

### Dependencies

- github.com/klauspost/compress v1.18.2 (#7604)
- github.com/antithesishq/antithesis-sdk-go v0.5.0-default-no-op (#7604)

### Added

General

- Added WebSocket-specific ping interval configuration with `ping_internal` in the `websocket` block (#7614)

### Fixed

JetStream

- The meta layer will now only respond to peer remove requests after quorum has been reached (#7581)
- Invalid subject filters containing non-terminating full wildcard no longer produce unexpected matches (#7585)
- A data race when creating a stream in clustered mode has been fixed (#7586)
- Raft will no longer allow multiple membership changes to take place concurrently (#7565, #7609)
- A panic when processing snapshots with missing nodes or assignments has been fixed (#7588)
- When purging whole message blocks, the subject tracking and scheduled messages are now updated correctly (#7593)
- Raft will no longer count responses from peer-removed nodes towards quorum (#7589)
- The filestore will no longer unexpectedly lose writes when `AsyncFlush` is enabled after a process pause (#7594)
- The filestore now will process message removal on disk before updating accounting, which improves error handling (#7595, #7601)
- Raft quorum counting has been refactored so the implicit leader ack is now only counted if still a part of the membership (#7600)
- Raft now writes the peer state immediately when handling a peer-remove to ensure the removed peers cannot unexpectedly reappear after a restart (#7602)
- The `DiscardNewPerSubject` retention policy is now enforced by the leader before proposing rather than by individual replicas, reducing the potential for stream desync (#7607)
- Raft will no longer allow peer-removing the one remaining peer (#7610)

MQTT

- Fixed a panic that could occur when reloading config if the user did not have permission to access retained messages (#7596)
- Fixed account mapping for JetStream API requests when traversing non-JetStream-enabled servers (#7598)
- QoS0 messages are now mapped correctly across account imports/exports with subject mappings (#7605)
- Loading retained messages no longer fails after restarting due to last sequence checks (#7616)


### Complete Changes
 
https://github.com/nats-io/nats-server/compare/v2.12.3-RC.1...v2.12.3-RC.2