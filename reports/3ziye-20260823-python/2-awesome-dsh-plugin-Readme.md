# Awesome DeepSeek Harness (DSH) Plugin [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![awesome · DSH plugin](https://awesome-dsh-plugin.com/badge.svg) ![plugin count](https://img.shields.io/endpoint?url=https%3A%2F%2Fawesome-dsh-plugin.com%2Fcount.json)

[![Awesome DSH Plugin](https://awesome-dsh-plugin.com/banner-en.png)](https://awesome-dsh-plugin.com)

English | [中文](README.zh.md)

> A curated list of plugins for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`).

DeepSeek Harness is DeepSeek's open-source agent harness — a runnable coding agent (Web and headless), built on a framework where everything is a plugin: models, tools, sandboxes, session storage, UI, even the agent loop itself. Plugins can extend the official coding agent, swap out its core parts, or assemble something entirely different.

This list collects community plugins that are installable via `dsh plugin add` (each declares a `dsh.bundle` manifest). [PRs welcome](#contributing).

> 🛒 **Recommended: [dsh-market](https://github.com/dsh-market/dsh-market#readme)** (optional) — the plugin market inside DeepSeek Harness, with every plugin on this list. Simple, friendly UI: one-click plugin install and upgrade, one-click theme switching:

```sh
dsh plugin --profile web add dshmarket
```

<a href="https://raw.githubusercontent.com/dsh-market/dsh-market/main/assets/demo-en.png"><img src="https://raw.githubusercontent.com/dsh-market/dsh-market/main/assets/demo-en.png" width="320" alt="dsh-market plugin browser inside DeepSeek Harness Settings: searchable plugin cards with one-click Install, category filters and a Themes tab"></a>

<sub><i>The plugin market inside Settings — click to enlarge.</i></sub>

> 💡 Prefer chat? [dsh-find-plugin](https://github.com/awesome-dsh-plugin/dsh-find-plugin#readme) lets your agent find plugins for you (`dsh plugin --profile web add dsh-find-plugin`).

> ℹ️ **On desktop clients.** This list is client-agnostic. A plugin is listed because it follows the official protocol — it declares a `dsh.bundle` manifest and installs with `dsh plugin add` — not because it adapts to any particular client.
>
> We're talking with `anywhere-labs/deepseek-harness-desktop` about working together again; we'll update this note as that progresses. Whatever comes of it, the listing rule stays as it is: adapting to any particular client is not a condition of being listed, and no plugin will be removed or demoted for not doing so.
>
> Clients worth a look: [dsh-desktop](https://github.com/dataelement/dsh-desktop) and [deepseek-harness-desktop](https://github.com/hairyf/deepseek-harness-desktop) — both ship dsh-market built in, so everything on this list is one click away. Any other good third-party client works too.

> [!WARNING]
> Installing a plugin runs third-party code on your machine with your own permissions — it can read your files, use your credentials, and reach the network. Tool approvals don't sandbox plugin code. Being on this list is not a security review: check the source before you install, and try unfamiliar plugins somewhere that doesn't hold your keys. See the full disclaimer at the bottom of this page.

<details>
<summary><b>What it takes to be listed here</b></summary>

An entry is added when the plugin installs with `dsh plugin add`, does what its one-line description says, sits in the right category, and is maintained. Every submission is checked against its own source before merging — if a description claims "46 tools", someone counts them.

That is the whole bar. **This list doesn't rank plugins or judge their quality, and we don't want to.** Plenty of good software will never appear here, and a slot here proves nothing beyond meeting those rules. They exist so that whatever you pick installs and behaves the way the line said it would.

A listing isn't permanent either: entries whose repos go away, stop being maintained, or turn out to be broken get removed. Full criteria and the review checklist: [how submissions are reviewed](contributing.md#how-submissions-are-reviewed--收录如何评审).

</details>

## Contents

<!-- BEGIN TOC -->
- [Plugins](#plugins)
  - [UI Enhancements](#ui-enhancements)
  - [Usage & Billing](#usage--billing)
  - [Themes & Appearance](#themes--appearance)
  - [Models & Providers](#models--providers)
  - [Identity & Communication](#identity--communication)
  - [Sessions & Messages](#sessions--messages)
  - [Memory](#memory)
  - [Tools & Capabilities](#tools--capabilities)
  - [Browser & Web](#browser--web)
  - [Vision & Multimodal](#vision--multimodal)
  - [Voice & Audio](#voice--audio)
  - [Docs & Rendering](#docs--rendering)
  - [Skills](#skills)
  - [Workflow & Automation](#workflow--automation)
  - [Git & Code Review](#git--code-review)
  - [Notifications & Integrations](#notifications--integrations)
  - [Development & Runtime](#development--runtime)
  - [Security & Permissions](#security--permissions)
  - [Remote & Mobile](#remote--mobile)
  - [Plugin M