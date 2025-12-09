# Perses - v0.53.0-beta.3

**Release Name**: 0.53.0-beta.3 / 2025-11-21
**Published**: 2025-11-21T11:38:44Z
**Repository**: https://github.com/perses/perses

---

### Core & UI

- [FEATURE] Add notices to panel header (#3577)
- [FEATURE] Display default dashboards when query is empty (#3572)
- [ENHANCEMENT] Error handling for Search Bar and dynamic Search List (#3575)
- [BUGFIX] Fix embedding markdown panels in tables (#3588)
- [BUGFIX] Add bits/sec convertion to human-readable sizes, add bits units(#3441) (#3583)
- [BUGFIX] Fix navigation after creating a new ephemeral dashboard (#3584)
- [BUGFIX] CLI/PLUGIN: Avoid re-building dev server tasks to shut down correctly the start plugin command (#3579)
- [BUGFIX] Add back piechart removed by mistake (#3552)
- [BREAKINGCHANGE/BUGFIX] PanelEditor + VariableEditor: queries changes are not saved (#3590)
- [DOC] Fix deprecated list of supported data-sources (#3601)
- [DOC] Add a concept doc about the open-specification and being compatible with Perses (#3598)

### Plugins improvements

- [FEATURE] StatChart: Add Color Mode (perses/plugins#433)
- [ENHANCEMENT] ScatterChart: remove time label, reduce chart padding, reduce amount of y axis labels (perses/plugins#476)
- [ENHANCEMENT] ScatterChart: sync xAxis with time range provider (perses/plugins#477)
- [BUGFIX] For all plugins : allow __mf/js/async assets to use proxy (perses/plugins#419 & perses/plugins#467)
- [BUGFIX] HistoryChart: Show no data when query result is empty (perses/plugins#465 & perses/plugins#468)
- [BUGFIX] TimeSeriesTable: Show No data accordingly (perses/plugins#466)
- [BUGFIX] StatChart: Add showLegend option with auto/on/off modes (perses/plugins#471)
- [BREAKINGCHANGE] datasources: Removing queryHandlers (perses/plugins#472)

### Breaking Changes

- `MultiQueryEditor` component has a new mandatory method: `onQueryRun`. It will be called when the user click on the button "Run Query". It's useful if you want to execute a query only when this button is clicked and not on every `onChange` (current Perses behavior).

From :

```tsx

export function FooExplorer(): ReactElement {
  const {
    data: { queries = [] },
    setData,
  } = useExplorerManagerContext<FooExplorerQueryParams>();

  return (
    <Stack gap={2} sx={{ width: '100%' }}>
      <MultiQueryEditor
        queryTypes={['ProfileQuery']}
        queries={queries}
        onChange={(newQueries) => setData({ queries: queryDefinitions })}
      />
      <FooPanel queries={queries} />
    </Stack>
  );
}
```

To :

```tsx

export function FooExplorer(): ReactElement {
  const {
    data: { queries = [] },
    setData,
  } = useExplorerManagerContext<FooExplorerQueryParams>();

  const [queryDefinitions, setQueryDefinitions] = useState<QueryDefinition[]>(queries);

  return (
    <Stack gap={2} sx={{ width: '100%' }}>
      <MultiQueryEditor
        queryTypes={['ProfileQuery']}
        queries={queryDefinitions}
        onChange={(newQueries) => setQueryDefinitions(newQueries)}
        onQueryRun={() => setData({ queries: queryDefinitions })}
      />
      <FooPanel queries={queries} />
    </Stack>
  );
}
```


- `queryHandlers` from `OptionsEditorProps` have been removed. 

<details>
  <summary> Commits </summary>

## What's Changed
* [BUGFIX] Add back piechart removed by mistake by @Nexucis in https://github.com/perses/perses/pull/3552
* [Feature] Display default dashboards when query is empty (#3539) by @prakhar29jain in https://github.com/perses/perses/pull/3572
* [IGNORE] doc: update TimeRangeProvider example by @Gladorme in https://github.com/perses/perses/pull/3578
* [BUGFIX] avoid re building dev server tasks to shutdown correctly the start plugin command by @jgbernalp in https://github.com/perses/perses/pull/3579
* [BUGFIX] Fix navigation after creating a new ephemeral dashboard by @AntoineThebaud in https://github.com/perses/perses/pull/3584
* [BUGFIX] Add bits/sec convertation to human-readable sizes, add bits units(#3441) by @lomobot in https://github.com/perses/perses/pull/3583
* Bump github.com/olekukonko/tablewriter from 1.1.0 to 1.1.1 by @dependabot[bot] in https://github.com/perses/perses/pull/3555
* Bump github.com/perses/plugins/prometheus from 0.54.0 to 0.55.0 in /internal/cli/cmd/dac/build/testdata/go by @dependabot[bot] in https://github.com/perses/perses/pull/3561
* [IGNORE] bump go deps and cue version to v0.15.0 by @Nexucis in https://github.com/perses/perses/pull/3566
* [FEATURE] Add notices to panel header by @OrReuben in https://github.com/perses/perses/pull/3577
* [BUGFIX] Don't pass queryResults wo/ supportedQueryTypes  by @PeterYurkovich in https://github.com/perses/perses/pull/3588
* [ENHANCEMENT] Add Dynamic display for Search Bar (#3573) by @prakhar29jain in https://github.com/perses/perses/pull/3575
* [IGNORE]: adds zed editor folder to .gitignore by @ibakshay in https://github.com/perses/perses/pull/3591
* [BUGFIX] PanelEditor + VariableEditor: queries changes are not saved by @Gladorme in https://github.com/perses/perses/pull/3590
* [IGNORE] upgrade vulnerable dependencies by @jgbernalp in https://github.com/perses/perses/pull/3593
* Bump golangci/golangci-lint-action from 8.0.0 to 9.0.0 by @dependabot[bot] in https://github.com/perses/perses/pull/3554
* [IGNORE] add CODEOWNERS file by @Nexucis in https://github.com/perses/perses/pull/3594
* [IGNORE] TraceMetaData: add hasMoreResults field by @andreasgerstmayr in https://github.com/perses/perses/pull/3599
* [DOC] Add a concept doc about the open-specification and being compatible with Perses by @Nexucis in https://github.com/perses/perses/pull/3598
* [DOC] Fix outdated list of supported datasources by @AntoineThebaud in https://github.com/perses/perses/pull/3601
* [ignore] fix supported language list for the open spec by @Nexucis in https://github.com/perses/perses/pull/3603
* merge main to branch release/v0.53 by @Nexucis in https://github.com/perses/perses/pull/3604
* [DOC] Add concept doc for Dashboard by @ekoutrouki in https://github.com/perses/perses/pull/3602
* [ignore] update plugin version by @Nexucis in https://github.com/perses/perses/pull/3606
* Release v0.53.0-beta.3 by @Nexucis in https://github.com/perses/perses/pull/3605
</details>

**Full Changelog**: https://github.com/perses/perses/compare/v0.53.0-beta.2...v0.53.0-beta.3

