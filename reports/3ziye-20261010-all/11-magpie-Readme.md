<div align="center">

<a href="https://usemagpie.ai"><img src="site/public/img/icon-256.png" width="112" alt="magpie"></a>

# magpie

### Every agent's model. One place.

**Claude Code on Kimi. Codex on DeepSeek. Gemini CLI on GLM. OpenCode on your ChatGPT plan.**<br>
Switch any of them from the menu bar. One local gateway serves them all,<br>
and when a quota runs out, it quietly moves on to the next account.

[![Release](https://img.shields.io/github/v/release/yetone/magpie-releases?label=release&color=111111)](https://github.com/yetone/magpie-releases/releases/latest) [![Stars](https://img.shields.io/github/stars/yetone/magpie?style=flat&color=111111)](https://github.com/yetone/magpie/stargazers) [![Discord](https://img.shields.io/badge/Discord-join-5865F2?logo=discord&logoColor=white)](https://discord.gg/vGSnD3ZKQF) [![License](https://img.shields.io/badge/license-MIT-111111)](LICENSE)<br>
![macOS](https://img.shields.io/badge/macOS-000000?logo=apple&logoColor=white) ![Windows](https://img.shields.io/badge/Windows-0078D4?logo=windows&logoColor=white) ![Linux](https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black) ![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white) ![Termux](https://img.shields.io/badge/Termux-000000?logo=android&logoColor=white)

**[Download](https://usemagpie.ai)** &nbsp;·&nbsp; **[Docs](https://usemagpie.ai/docs/start)** &nbsp;·&nbsp; **[Reference](docs/reference.md)** &nbsp;·&nbsp; **[Plugins](https://github.com/magpie-community/plugins)** &nbsp;·&nbsp; **[Discord](https://discord.gg/vGSnD3ZKQF)** &nbsp;·&nbsp; **English** · [简体中文](README.zh-CN.md)

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="site/public/img/agents-dark.png">
  <img src="site/public/img/agents-light.png" width="900" alt="magpie's Agents page: Claude Code on Kimi K3, Codex on DeepSeek V4 Pro, Gemini CLI on GLM-5.3, each picked from one list">
</picture>

</div>

<br>

## Is magpie for you?

Each agent keeps its model in its own file, in its own format, with its own keys and base URLs. A subscription you pay for works in one agent and nowhere else. magpie puts all of that behind one app and one local gateway:

- **Pick any model for any agent** from one list. magpie edits the one key that matters in the agent's own config.
- **Use one provider everywhere**: an API key, a local model, or the Claude, ChatGPT, Copilot, Gemini or Grok plan you're signed in to.
- **Keep going when a quota runs out**: a routing group moves to the next account or model, and the agent never sees the error.

It's for you if you use more than one agent, more than one provider, or more than one account. If you use one agent on its vendor's own plan and that's enough, you don't need it.

Runs on macOS, Windows and Linux (menu bar app, window, TUI, web UI and CLI), in Docker, and on Termux.

## Quick start

**1 · Install.** Download the app from **[usemagpie.ai](https://usemagpie.ai)**, or run:

```sh
curl -fsSL https://usemagpie.ai/install.sh | sh
```

<sub>Mac builds are signed and notarised, and every build updates itself. Behind a firewall, use `--proxy` or `--mirror`. Or `go install github.com/yetone/magpie@latest`, or the [Docker image](https://usemagpie.ai/docs/docker).</sub>

**2 · Add a provider.** Open magpie and go to **Providers → Add provider**. Pick a preset and paste a key, or sign in with a subscription.

**3 · Pick a model** for each agent on the **Agents** page. Start a new session and it's on the new model.

Or do it all from the terminal:

```sh
magpie provider add deepseek sk-…              # a preset needs only the key
magpie claude deepseek/deepseek-v4-pro          # Claude Code on DeepSeek
magpie codex moonshot/kimi-k2.5                 # Codex on Kimi
magpie group add "Opus anywhere" models=claude/claude-opus-5-5,copilot/claude-opus-5.5 routing=smart
magpie claude group/opus-anywhere               # fails over between subscriptions
magpie save work && magpie use work             # profiles
magpie quota                                    # what's left on every plan
magpie tui                                      # the whole thing, in a terminal
```

## Supported agents

<table>
<tr><td>

Claude Code · Claude Desktop · Codex · Gemini CLI · Antigravity CLI · OpenCode · OpenChamber · MiMo Code · Pi · oh-my-pi · Aside · OmO · Goose · Cursor CLI · Cursor Private Inference · Zed · VS Code Chat · VS Code Insiders · VSCodium Chat · JetBrains Air · Copilot (JetBrains) · Copilot CLI · Crush · DeepSeek Harness · Reasonix Studio · Command Code · fx · Devin · Hermes Agent · Mister Morph · Kimi Code · Qwen Code · Muse Code · Empryo · MiniMax Code · Droid · Cline · Qoder · Qoder CN · Grok Build · ZCode · WorkBuddy · CodeBuddy Code · Pencil · T3 Code · OpenHanako · AtomCode · Snow CLI · Alma · Cindy

</td></tr>
</table>

magpie shows only the agents installed on your machine; setup notes for some of them are in the [reference](docs/reference.md#notes-on-some-agents). An