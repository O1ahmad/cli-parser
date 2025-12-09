# OpenTracing - v1.2.0

**Release Name**: Release 1.2.0
**Published**: 2020-07-01T21:28:36Z
**Repository**: https://github.com/opentracing/opentracing-go

---

* Use error.object per OpenTracing Semantic Conventions (#179) -- Rahman Syed
* Convert nil pointer log field value to string "nil" (#230) -- Cyril Tovena
* Add Go module support (#215) -- Zaba505
* Make SetTag helper types in ext public (#229) -- Blake Edwards
* Add log/fields helpers for keys from specification (#226) -- Dmitry Monakhov
* Improve noop impementation (#223) -- chanxuehong
* Add an extension to Tracer interface for custom go context creation (#220) -- Krzesimir Nowak
  * Restore the ability to reset the current span in context to nil (#231) -- Yuri Shkuro
* Fix typo in comments (#222) -- meteorlxy
* Improve documentation for log.Object() to emphasize the requirement to pass immutable arguments (#219) -- 疯狂的小企鹅
* [mock] Return ErrInvalidSpanContext if span context is not MockSpanContext (#216) -- Milad Irannejad
