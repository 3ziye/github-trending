<div align="center">

<a href="https://usemagpie.ai"><img src="site/public/img/icon-256.png" width="120" alt="magpie"></a>

# magpie

### Every agent's model. One place.

Claude Code on Kimi, Codex on DeepSeek, Gemini CLI on GLM, OpenCode on your ChatGPT plan.<br>
Switch them from the menu bar. One local gateway serves them all, and it moves to another account when a quota runs out.

[![Release](https://img.shields.io/github/v/release/yetone/magpie-releases?label=release&color=111111)](https://github.com/yetone/magpie-releases/releases/latest) [![Stars](https://img.shields.io/github/stars/yetone/magpie?style=flat&color=111111)](https://github.com/yetone/magpie/stargazers) [![Discord](https://img.shields.io/badge/Discord-join-5865F2?logo=discord&logoColor=white)](https://discord.gg/vGSnD3ZKQF) [![License](https://img.shields.io/badge/license-MIT-111111)](LICENSE)<br>
![macOS](https://img.shields.io/badge/macOS-000000?logo=apple&logoColor=white) ![Windows](https://img.shields.io/badge/Windows-0078D4?logo=windows&logoColor=white) ![Linux](https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black) ![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white) ![Termux](https://img.shields.io/badge/Termux-000000?logo=android&logoColor=white)

**[Download](https://usemagpie.ai)** · **[Docs](https://usemagpie.ai/docs/start)** · **[Reference](docs/reference.md)** · **[Discord](https://discord.gg/vGSnD3ZKQF)** · **English** · [简体中文](README.zh-CN.md)

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="site/public/img/agents-dark.png">
  <img src="site/public/img/agents-light.png" width="900" alt="magpie's Agents page: Claude Code on Kimi K3, Codex on DeepSeek V4 Pro, Gemini CLI on GLM-5.3, each picked from one list">
</picture>

</div>

<br>

## Why magpie

You probably use more than one coding agent. Each one keeps its model in its own file, in its own format, with its own keys and base URLs. Each one also has its own idea of which vendors it supports. A subscription you pay for works in one agent and nowhere else. When it runs out at 3 pm, you start editing config files.

magpie puts all of it in one place:

<table>
<tr>
<td width="33%" valign="top">

**🎛 One screen for every agent**<br>
Over 35 agents in one list. Click a model and pick another. magpie changes only that one key in the agent's own config file. Comments, ordering and formatting stay as they were.

</td>
<td width="33%" valign="top">

**🔌 One gateway for every API**<br>
`127.0.0.1:3425` speaks OpenAI Chat, OpenAI Responses, Anthropic Messages and Gemini. It translates between them, streaming, tool calls and reasoning included.

</td>
<td width="33%" valign="top">

**🔀 Routing that keeps going**<br>
Put several models from several providers in a routing group. When one hits a rate limit or runs out of quota, the next one answers. Your agent never sees the error.

</td>
</tr>
<tr>
<td valign="top">

**🔑 Subscriptions you can share**<br>
Your Claude, ChatGPT, Copilot, Gemini or Grok sign-in becomes a provider that every other agent can use. There is no key to copy.

</td>
<td valign="top">

**🧩 Plugins**<br>
OpenCode auth plugins and pi provider packages from npm run in magpie as they do in their own apps. Any plan a plugin signs in to works in every agent. A plugin can also be gateway middleware that reads and rewrites every request and reply.

</td>
<td valign="top">

**📊 Usage and cost tracking**<br>
See tokens, cache hits, cost at list price, balances and quota windows for every provider and account. You can also set a limit for each key.

</td>
</tr>
</table>

<br>

## Pick any model for any agent

Click a value and a filtered list opens. It holds every model of every provider you added, as `provider/model`. Pick one and the agent's config file is rewritten safely and atomically. Use **Profiles** to save the setup of every agent under one name ("Budget", "Focus") and switch them all at once.

magpie also lives in the **menu bar**. There is a tray panel on macOS, Windows and Linux, a full window, a **TUI** (`magpie tui`), a **web UI** (`magpie web`) and a plain **CLI**.

<table>
<tr>
<td width="50%">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="site/public/img/panel-dark.png">
  <img src="site/public/img/panel-light.png" alt="The menu bar panel">
</picture>
</td>
<td width="50%">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="site/public/img/picker-dark.png">
  <img src="site/public/img/picker-light.png" alt="The model picker">
</picture>
</td>
</tr>
</table>

## Add providers with one field

Pick a preset and paste a key. That's it. The model list comes from the vendor itself, with names and reasoning levels filled in from [models.dev](https://models.dev), so a model released this morning shows up on the next refresh. No model list is built into magpie.

**Presets include** Anthropic · OpenAI · Google Gemini · DeepSeek · Kimi · Zhipu GLM · MiniMax · StepFun · Qw