# Headlamp - headlamp-plugin-0.13.0

**Release Name**: headlamp-plugin 0.13.0
**Published**: 2025-11-27T21:17:28Z
**Repository**: https://github.com/kubernetes-sigs/headlamp

---

New release of the headlamp-plugin tool for plugin authors.

## ⬆️ Upgrade

Upgrade your plugin to latest version by running:

<br>

```shell
npx @kinvolk/headlamp-plugin upgrade .
```

## ✨ Enhancements:

- Creating a new plugin and installing dependencies is up to 4.2x times faster
- New and expanded guides for [plugin architecture](https://headlamp.dev/docs/latest/development/architecture#plugins) and [development](https://headlamp.dev/docs/latest/development/plugins/getting-started), including how to publish and ship plugins
- [i18n](https://headlamp.dev/docs/latest/development/plugins/i18n) support so plugins can be translated and localized
- Add example plugins: [ui-panels](https://github.com/kubernetes-sigs/headlamp/tree/main/plugins/examples/ui-panels), [resource-charts](https://github.com/kubernetes-sigs/headlamp/tree/main/plugins/examples/resource-charts), [custom-theme](https://github.com/kubernetes-sigs/headlamp/tree/main/plugins/examples/custom-theme), and [projects](https://github.com/kubernetes-sigs/headlamp/tree/main/plugins/examples/projects)
- Improve TypeScript support so more things are typed correctly, and on-hover documentation is shown
- Document plugin install locations, UI signifiers in Plugin Settings, and labels that differentiated shipped, UI-installed, and dev-mode plugins
- Remove many unused dependencies, for faster installs and fewer updates
- Add --noinstall option to `headlamp-plugin create` command
- Add concept of "shipped", "user plugins" and "dev plugins"

### For Plugin Developers: Find Plugin Folder in the UI

To make it easier for plugin developers to find where on the local file system plugins are there is an open plugin folder button. In Plugin Settings select the plugin being developed, and then click the open folder icon to open the plugin path with the Desktop file Finder.

<img width="942" height="434" alt="Shows the UI for finding the plugin folder and the open folder where the plugin is" src="https://github.com/user-attachments/assets/e7fe6c1e-ef30-47e1-b66d-f319fe3e6b47" />

## 🐞 Bug fixes

- Fix storybook, so "npm run storybook" works again
- Upgrade dependencies to match latest Headlamp release
- Fix `create` command to install with npm ci
- Fix support for env vars REACT_APP_ NODE_ENV
- Fix npm start to log where files are copied, which helps people understand where plugins are copied
- Fix polyfils for node modules process and path
- Fix lib k8s import paths in storybook
- Fix `npm run build` command to copy css and svg files
- Fix storybook theme logo and fonts to match Headlamp
- Fix storybook to include base mocks and css

## 🛠️ headlamp-plugin development

Items about the development of the headlamp-plugin package.

- Add tests to check storybook is working inside headlamp-plugin
- Add copy-package-lock script to create template/package-lock.json to pin dependencies and make headlamp-plugin installs faster

## ⚠️ Type Checking

Because of the improvements to type checking there may be a number of TypeScript issues found when ugprading.

You may find similar issues have been fixed in the [example plugins](https://github.com/kubernetes-sigs/headlamp/tree/main/plugins/examples), or in [other plugins](https://github.com/headlamp-k8s/plugins/pulls).

## 🐛 Reporting issues

Please [submit an issue](https://github.com/kubernetes-sigs/headlamp/issues) if you have any ideas, questions or feedback on Headlamp plugin development. Or come to the [Kubernetes slack headlamp](https://kubernetes.slack.com/?redir=%2Fmessages%2Fheadlamp) channel for a chat.
