# Airflow - 3.1.3

**Release Name**: Apache Airflow 3.1.3
**Published**: 2025-11-14T14:47:34Z
**Repository**: https://github.com/apache/airflow

---

📦 PyPI: https://pypi.org/project/apache-airflow/3.1.3/
📚 Docs: https://airflow.apache.org/docs/apache-airflow/3.1.3/
🛠 Release Notes: https://airflow.apache.org/docs/apache-airflow/3.1.3/release_notes.html
🐳 Docker Image: "docker pull apache/airflow:3.1.3"
🚏 Constraints: https://github.com/apache/airflow/tree/constraints-3.1.3

## Significant Changes

### Fix Connection & Variable access in API server contexts (plugins, log handlers)(#56583)


Previously, hooks used in API server contexts (plugins, middlewares, log handlers) would fail with an ``ImportError``
for ``SUPERVISOR_COMMS``, because ``SUPERVISOR_COMMS`` only exists in task runner child processes.

This has been fixed by implementing automatic context detection with three separate secrets backend chains:

**Context Detection:**

1. **Client contexts** (task runner in worker): Detected via ``SUPERVISOR_COMMS`` presence
2. **Server contexts** (API server, scheduler): Explicitly marked with ``_AIRFLOW_PROCESS_CONTEXT=server`` environment variable
3. **Fallback contexts** (supervisor, unknown contexts): Neither marker present, uses minimal safe chain

**Backend Chains:**

- **Client**: ``EnvironmentVariablesBackend`` → ``ExecutionAPISecretsBackend`` (routes to Execution API via SUPERVISOR_COMMS)
- **Server**: ``EnvironmentVariablesBackend`` → ``MetastoreBackend`` (direct database access)
- **Fallback**: ``EnvironmentVariablesBackend`` only (+ external backends from config like AWS Secrets Manager, Vault)

The fallback chain is crucial for supervisor processes (worker-side, before task runner starts) which need to access
external secrets for remote logging setup but should not use ``MetastoreBackend`` (to maintain worker isolation).

**Architecture Benefits:**

- Workers (supervisor + task runner) never use ``MetastoreBackend``, maintaining strict isolation
- External secrets backends (AWS Secrets Manager, Vault, etc.) work in all three contexts
- Supervisor falls back to Execution API client for connections not found in external backends
- API server and scheduler have direct database access for optimal performance

**Impact:**

- Hooks like ``GCSHook``, ``S3Hook`` now work correctly in log handlers and plugins
- No code changes required for existing plugins or hooks
- Workers remain isolated from direct database access (network-level DB blocking fully supported)
- External secrets work everywhere (workers, supervisor, API server)
- Robust handling of unknown contexts with safe minimal chain

See: `#56120 <https://github.com/apache/airflow/issues/56120>`__, `#56583 <https://github.com/apache/airflow/issues/56583>`__, `#51816 <https://github.com/apache/airflow/issues/51816>`__

### Remove insecure dag reports API endpoint that executed user code in API server (#56609)

  The ``/api/v2/dagReports`` endpoint has been removed because it loaded user DAG files directly in the API server process,
  violating Airflow's security architecture. This endpoint was not used in the UI and had no known consumers.
  Use the ``airflow dags report`` CLI command instead for DAG loading reports.

## Bug Fixes

- Fix HITL tasks not properly validating params (#57547) (#58144)
- Fix secrets being exposed in Jinja template rendering error messages (#57467) (#57962)
- UI: Fix slow loading on next run assets page (#58052) (#58064)
- Fix logout not working in airflow-core (#57990) (#58043)
- Fix slow loading on UI [(#57820) (#57856), (#57956) (#57973), (#57957) (#57972),(#57869) (#57882), (#57868) (#57918),(#57624) (#57757)]
- UI: Fix log download to include .txt file extension (#57991) (#58040)
- Fix scheduler using incorrect max_active_runs value from cached DAG (#57619) (#57959)
- Fix database migration failures when XCom contains NaN values (#57866) (#57893)
- Fix incorrect task context in trigger rule scenarios (#57884) (#57892)
- UI: Fix test connection not working (#57811) (#57852)
- Fix worker ``healthcheck`` timeout not respecting worker-timeout CLI option (#57731) (#57854)
- Fix provider hooks not loading when FAB provider is not installed (#57717) (#57830)
- Fix slow API responses for task instances list [(#57645) (#57794), (#57646) (#57664),(#57500) (#57735), (#57549) (#57738), (#57450) (#57736),(#57647) (#57732)]
- Fix task instance errors when tasks are triggered by trigger rules (#57474) (#57786)
- Fix type consistency for extra field in Asset, AssetAlias, and AssetEvent (#57352) (#57728)
- Fix upgrade failures when XCom contains NaN in string values (#57614)

## Miscellaneous

- UI: Add resize functionality to DAG run and task instance notes (#57897) (#58068)
- Add Taiwan translation for UI (#58121)
- UI: Shorten German translation of Asset in navigation (#57671) (#57690)
- Fix code formatting via ruff preview (#57641) (#57670)
- Remove remnants from unlimited parallelism in local executor (#57579) (#57644)

## Doc Only Changes

- Add learning from Airflow 3 migration guide (#57989) (#58083)
- Fix duplicate mention of 'DAGs' and 'tasks' in overview documentation (#57524) (#57793)
- Document asset event extra storage behavior (#57727) (#57734)