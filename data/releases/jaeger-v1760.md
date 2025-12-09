# Jaeger - v1.76.0

**Release Name**: Release v1.76.0 / v2.13.0
**Published**: 2025-12-03T16:31:24Z
**Repository**: https://github.com/jaegertracing/jaeger

---

### Backend Changes

#### 🐞 Bug fixes, Minor Improvements

* Fix: register basicauth extension in component factory ([@xenonnn4w](https://github.com/xenonnn4w) in [#7668](https://github.com/jaegertracing/jaeger/pull/7668))

#### 👷 CI Improvements

* Make error message better ([@yurishkuro](https://github.com/yurishkuro) in [#7675](https://github.com/jaegertracing/jaeger/pull/7675))
* Clean go cache after installing gotip as suggested. ([@Kavish-12345](https://github.com/Kavish-12345) in [#7666](https://github.com/jaegertracing/jaeger/pull/7666))
* Fix: build test tools with stable go, not gotip ([@Kavish-12345](https://github.com/Kavish-12345) in [#7665](https://github.com/jaegertracing/jaeger/pull/7665))

### 📊 UI Changes

#### 🐞 Bug fixes, Minor Improvements

* Add support for custom ui configuration in development mode ([@Copilot](https://github.com/apps/copilot-swe-agent) in [#3194](https://github.com/jaegertracing/jaeger-ui/pull/3194))
* Remove duplicate antd dependencies ([@yurishkuro](https://github.com/yurishkuro) in [#3193](https://github.com/jaegertracing/jaeger-ui/pull/3193))
* Fix css class typo in sidepanel details div ([@Copilot](https://github.com/apps/copilot-swe-agent) in [#3190](https://github.com/jaegertracing/jaeger-ui/pull/3190))
* Reduce search form field margins for better viewport fit ([@Copilot](https://github.com/apps/copilot-swe-agent) in [#3189](https://github.com/jaegertracing/jaeger-ui/pull/3189))
* Migrate deepdependencies/header and qualitymetrics/header from nameselector to searchableselect ([@Copilot](https://github.com/apps/copilot-swe-agent) in [#3185](https://github.com/jaegertracing/jaeger-ui/pull/3185))
* Reorder checkbox before color by dropdown in tracestatisticsheader ([@Copilot](https://github.com/apps/copilot-swe-agent) in [#3184](https://github.com/jaegertracing/jaeger-ui/pull/3184))
* Feat: add fuzzy search to searchableselect ([@Copilot](https://github.com/apps/copilot-swe-agent) in [#3182](https://github.com/jaegertracing/jaeger-ui/pull/3182))
* Fix highlighting of the current tab in the main nav bar ([@SimonADW](https://github.com/SimonADW) in [#3183](https://github.com/jaegertracing/jaeger-ui/pull/3183))

#### 🚧 Experimental Features

* Sync themes with antd ([@yurishkuro](https://github.com/yurishkuro) in [#3196](https://github.com/jaegertracing/jaeger-ui/pull/3196))
* Add dark theme selector ([@yurishkuro](https://github.com/yurishkuro) in [#3192](https://github.com/jaegertracing/jaeger-ui/pull/3192))

#### 👷 CI Improvements

* Add copyright year linter to npm lint command ([@Copilot](https://github.com/apps/copilot-swe-agent) in [#3197](https://github.com/jaegertracing/jaeger-ui/pull/3197))
* Rename theme variables to match industry practice ([@yurishkuro](https://github.com/yurishkuro) in [#3174](https://github.com/jaegertracing/jaeger-ui/pull/3174))
* Tweak codecov config ([@yurishkuro](https://github.com/yurishkuro) in [#3169](https://github.com/jaegertracing/jaeger-ui/pull/3169))

#### ⚙️ Refactoring

* Apply theme vars to common/emphasizednode ([@yurishkuro](https://github.com/yurishkuro) in [#3191](https://github.com/jaegertracing/jaeger-ui/pull/3191))
* Fix ddg minimap border ([@yurishkuro](https://github.com/yurishkuro) in [#3188](https://github.com/jaegertracing/jaeger-ui/pull/3188))
* Use token vars in common/utils.css ([@yurishkuro](https://github.com/yurishkuro) in [#3187](https://github.com/jaegertracing/jaeger-ui/pull/3187))
* Apply theme vars to some shared components ([@yurishkuro](https://github.com/yurishkuro) in [#3181](https://github.com/jaegertracing/jaeger-ui/pull/3181))
* Apply theme vars to search page ([@yurishkuro](https://github.com/yurishkuro) in [#3180](https://github.com/jaegertracing/jaeger-ui/pull/3180))
* Use theme vars in errormessage & loadingindicator ([@yurishkuro](https://github.com/yurishkuro) in [#3177](https://github.com/jaegertracing/jaeger-ui/pull/3177))
* Use theme vars in main page and topnav ([@yurishkuro](https://github.com/yurishkuro) in [#3176](https://github.com/jaegertracing/jaeger-ui/pull/3176))
* Convert last remaining js files to typescript (excluding tests) ([@yurishkuro](https://github.com/yurishkuro) in [#3173](https://github.com/jaegertracing/jaeger-ui/pull/3173))
* Convert some easy files to typescript ([@yurishkuro](https://github.com/yurishkuro) in [#3167](https://github.com/jaegertracing/jaeger-ui/pull/3167))


