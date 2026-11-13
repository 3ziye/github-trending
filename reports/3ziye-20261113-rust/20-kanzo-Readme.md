<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/img/kanzo-dark.jpg">
    <img alt="kanzo: a tiny kanban board for you and your coding agents" src="docs/img/kanzo-light.jpg">
  </picture>
</p>

<p align="center">
  <a href="https://github.com/emanuele-em/kanzo/actions/workflows/ci.yml"><img src="https://github.com/emanuele-em/kanzo/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://crates.io/crates/kanzo"><img src="https://img.shields.io/crates/v/kanzo" alt="crates.io"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-AGPL--3.0-blue" alt="AGPL-3.0"></a>
</p>

<p align="center">
  English | <a href="README.zh.md">简体中文</a>
</p>

Kanzo is a kanban board in your browser and an MCP server in one 4.7 MB program, so you and your coding agents work on the same tasks: on one computer, or on one board shared by all of them. No account, no server, no setup: run `kanzo` and it works.

You never edit a file. Everything is done in one of three places:

- **the board**, in your browser, for you;
- **MCP**, for your agents: they take tasks, move cards and comment;
- **the `kanzo` command**, for the terminal and scripts.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/img/board-dark.gif">
  <img alt="The Kanzo board: agents move cards while you watch, ⌘K finds a task in any project, a task is made to wait on another, two selected tasks are dragged together, a list groups the tasks by status, the sidebar folds, Laptop A shares the board and Laptop B joins it" src="docs/img/board-light.gif">
</picture>

## Install

> [!TIP]
> **Just ask your agent:** *"install Kanzo from github.com/emanuele-em/kanzo."*

```sh
curl -LsSf https://github.com/emanuele-em/kanzo/releases/latest/download/kanzo-installer.sh | sh
```

For macOS and Linux, including every Raspberry Pi. On Windows, in PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -c "irm https://github.com/emanuele-em/kanzo/releases/latest/download/kanzo-installer.ps1 | iex"
```

Both add Kanzo to your `PATH`, for terminals you open from then on. To use it in the one you installed from, run `source $HOME/.cargo/env` (`env.fish` in fish), or open a new one.

Or download the Windows zip from the [latest release](https://github.com/emanuele-em/kanzo/releases/latest) and put `kanzo.exe` in a folder named `bin` on your `PATH`, like `%USERPROFILE%\.cargo\bin`: the board updates itself only there.

Every release is signed by GitHub: check a download with `gh attestation verify <file> --repo emanuele-em/kanzo`. Or with Cargo:

```sh
cargo install kanzo
```

## Start

> [!TIP]
> **Just ask your agent:** *"start Kanzo and keep it running at login."*

```sh
kanzo
```

The board opens at http://localhost:4242. That's all the setup there is: the first run creates `~/kanzo`, and the whole board lives in it.

| Key | Does |
| --- | --- |
| `n` | New task |
| `/` or `⌘K` | Search every project |
| `f` | Filter the board; `↵` keeps the filter |
| `Tab` | Move to the description |
| `⌘↵` | Save and close |
| `Esc` | Keep what you typed in a description or tags; cancel other fields |

## Use the board

> [!TIP]
> **Just ask your agent:** *"mark kanzo#12 as human, and set its URL to github.com/acme/api/pull/482."*

- **Select tasks:** `⌘`-click them, or drag on empty board space, then move, tag or delete them together. Drag one and the rest follow.
- **List view:** the list icon shows the same tasks as rows to sort and group.
- **Human tasks:** mark a task Human and agents leave it to you. The person icon shows only those.
- **Images:** paste or drop one into a task or a comment.
- **Links:** give a task a URL, like its pull request, and open it from its card. Agents set it with `url`.
- **Files:** `[name](file:///path)` in a description or comment opens in your editor.
- **Task panel:** drag its left edge to resize it, or expand it to the whole window. Double-click the edge to reset it.
- **Sidebar:** the panel button beside search folds it to its icons. Drag a project to reorder the list, for everyone on a shared board.
- **App:** in Chrome or Edge, **Install app** at the bottom of the sidebar makes the board an app of its own. `⌘1`–`⌘8` pick a project, `⌘9` the last one, `⌘0` all of them. On macOS, `kanzo` then opens it instead of a tab, on the default port.
- **Updates:** when a new version is out, the sidebar offers it. One click installs it.

## Connect your agents

> [!TIP]
> **Just ask your agent:** *"add Kanzo as your MCP server,"* then restart it.

```sh
claude mcp add kanzo --scope user -- kanzo mcp   # Claude Code
codex mcp add kanzo -- kanzo mcp                 # Codex
```

Other MCP clients: run `kanzo mcp` (apps like Raycast need the full path, from `which kanzo`), or use the running board at `http://localhost:4242/mcp`.

Then ask: *"take the next task from kanzo and do it."* The agent:

- finds the project from the git remote of its repo; link more repos from the projec