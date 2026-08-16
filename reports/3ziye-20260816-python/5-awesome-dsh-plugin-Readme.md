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

> 💡 Prefer chat? [dsh-find-plugin](https://github.com/awesome-dsh-plugin/dsh-find-plugin#readme) lets your agent find plugins for you (`dsh plugin --profile web add dsh-find-plugin`).

> [!WARNING]
> Installing a plugin runs third-party code on your machine with your own permissions — it can read your files, use your credentials, and reach the network. Tool approvals don't sandbox plugin code. Being on this list is not a security review: check the source before you install, and try unfamiliar plugins somewhere that doesn't hold your keys. See the full disclaimer at the bottom of this page.

## Contents

- [Plugins](#plugins)
  - [UI Enhancements](#ui-enhancements)
  - [Themes & Appearance](#themes--appearance)
  - [Models & Providers](#models--providers)
  - [Sessions & Messages](#sessions--messages)
  - [Memory](#memory)
  - [Tools & Capabilities](#tools--capabilities)
  - [Skills](#skills)
  - [Workflow & Automation](#workflow--automation)
  - [Notifications & Integrations](#notifications--integrations)
  - [Development & Runtime](#development--runtime)
  - [Plugin Markets & Managers](#plugin-markets--managers)
  - [Just for Fun](#just-for-fun)
- [Badge](#badge)
- [Disclaimer](#disclaimer)

## Plugins

### UI Enhancements
- [Limitinfinitude/DSH-Right-Sidebar](https://github.com/Limitinfinitude/DSH-Right-Sidebar) - DSH Web right-side output dock that collects session artifacts, previews user-facing files, and preserves tab state per session.
- [No-PRM/dsh-explorer](https://github.com/No-PRM/dsh-explorer) - Git-first file-tree sidebar for the DSH web GUI: VS Code-style indent guides, M/A/U/D/R git decorations, HEAD-vs-worktree diff preview, media preview, and drag-to-reference (files/folders/selected code with line numbers) — pure plugin.
- [xiaweiliang060035/dsh-opencode-go-usage](https://github.com/xiaweiliang060035/dsh-opencode-go-usage) - Floating widget showing real-time OpenCode Go subscription usage (rolling/weekly/monthly) for every API key, with rate-limit alerts and automatic key-pool discovery.
- [wx-yss/dsh-message-rail](https://github.com/wx-yss/dsh-message-rail) - Codex-style left-side message navigation rail for the Web UI: one tick per user message, hover previews, and click-to-jump across the whole history.
- [Ricketts-Guo/dsh-shortcuts](https://github.com/Ricketts-Guo/dsh-shortcuts) - Fully customizable keyboard shortcuts for the Web UI: 34 pre-registered features (sessions, views, clipboard, models, silent permission cycling, settings), one-click recording to bind your own, and a shortcut cheatsheet with built-in diagnostics.
- [YEYEYEYESHIFU/dsh-session-hotkeys](https://github.com/YEYEYEYESHIFU/dsh-session-hotkeys) - Session hotkeys for the Web UI: Alt+1-9 positional switching, pin-slot tri-state, a sidebar highlight nav mode, new/rename/archive session shortcuts, and a rebindable panel with arrow-key navigation.
- [magian1127/deepseek-harness-zh_pro](https://github.com/magian1127/deepseek-harness-zh_pro) - Chinese UI enhancement for the DSH web client: completes the Chinese locale, keeps the session stats line fully visible on one row, and adds an Enhancements settings section with configurable chat width.
- [NewDaNew/dsh-voice-input](https://github.com/NewDaNew/dsh-voice-input) - Voice input for the web UI: a mic button in the composer that transcribes speech into the draft via the Web Speech API, with an optional auto-send toggle.
- [Nothree-code/voco-input-sh](https://github.com/Nothree-code/voco-input-sh) - Voice input for the Web UI: a mic button that drives local VocoType offline speech recognition and auto-inserts recognized text into the composer (auto-deploy, dedupe, continuous dictati