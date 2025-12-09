# Sermant - v2.3.0

**Release Name**: Release v2.3.0
**Published**: 2025-06-30T12:52:32Z
**Repository**: https://github.com/sermant-io/Sermant

---

## ⭐ Feature

- Support xds security. Issue #1789
- Add an independent xDS plugin. Issue #1776
- Support servlet5.x,6.x for tag transmission. Issue #1791
- Support okhttp3.x,4.x for tag transmission. Issue #1791
- Support feign11.x for tag transmission. Issue #1737
- Support dubbo3.x for rateLimiting/circuitBreaker. Issue #1746

## 📈 Improvements

- Improve the performance while select Nacos as configuration center. Issue #1769
- Support ignore the classes loaded by specific ClassLoaders in bytecode enhancement. Issue #1772
- Service-meta configuration item in the message gray configuration can effect dynamically. Issue #1785

## 🐞 Fixes

- Fix classes can not be loaded correctly when ContextClassLoader does not exist. Issue #1732
- Fix the support for Okhttp2 v2.2.0 in xDS flow control. Issue #1742
- Fix retry time is incorrect with HttpUrlConnection in xDS flow control. Issue #1742
- Fix the support for millisecond-level time in xDS flow control. Issue #1742
- Fix some retry conditions are inconsistent with Istio in xDS flow control. Issue #1742
- Fix the support for RocketMq retry-topic SQL filtering messages in message gray plugin. Issue #1748
- Fix the routing metric collection flag is not set in xds router. Issue #1754
- Add synchronization to fixed SQL92 expression build error problem. Issue #1786
- Fix the gray flag cannot be matched when consumerGroupTag contains uppercase characters. Issue #1782
- Update netty handler version. #1763
- Resolve CVE of dependencies #1797

## 🙇 Thank you

This release thanks the following contributors for their pull requests:

@chengyouling
@daizhenyu
@hanbingleixue
@lilai23
@provenceee
@SunJiFengPlus