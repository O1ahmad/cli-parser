# gRPC - v1.76.0

**Release Name**: Release v1.76.0
**Published**: 2025-10-20T17:34:57Z
**Repository**: https://github.com/grpc/grpc

---

This is release 1.76.0 ([genuine](https://github.com/grpc/grpc/blob/master/doc/g_stands_for.md)) of gRPC Core.

For gRPC documentation, see [grpc.io](https://grpc.io/). For previous releases, see [Releases](https://github.com/grpc/grpc/releases).

This release contains refinements, improvements, and bug fixes, with highlights listed below.


Core
---

-  Prioritize system CA over bundled CA. ([#40583](https://github.com/grpc/grpc/pull/40583))
-  [event_engine] Introduce a event_engine_poller_for_python experiment. ([#40243](https://github.com/grpc/grpc/pull/40243))
-  [metrics] add grpc.lb.backend_service label. ([#40486](https://github.com/grpc/grpc/pull/40486))

C#
---

-  [csharp tools] #39374 Grpc.Tools can't process file Suffix name with Upper character. ([#40072](https://github.com/grpc/grpc/pull/40072))

Python
---

-  [Python] gRPC AsyncIO: Improve CompletionQueue polling performance. ([#39993](https://github.com/grpc/grpc/pull/39993))

