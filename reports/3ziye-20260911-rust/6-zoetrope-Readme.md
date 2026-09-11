<p align="center">
  <img src="https://raw.githubusercontent.com/furkankly/zoetrope/main/assets/icon.svg" alt="" width="80">
</p>

<h1 align="center">zoetrope</h1>

<p align="center">
  <em>Watch a Claude Code or Codex session as a live flow graph, in your terminal or your browser.</em>
</p>

<p align="center">
  <a href="https://crates.io/crates/zoetrope"><img src="https://img.shields.io/crates/v/zoetrope.svg?style=flat&labelColor=121212&color=d7af00&logo=Rust&logoColor=white" alt="crates.io"></a>
  <a href="https://docs.rs/zoetrope"><img src="https://img.shields.io/docsrs/zoetrope?style=flat&labelColor=121212&color=d7af00&logo=docs.rs&logoColor=white" alt="docs.rs"></a>
  <a href="https://crates.io/crates/zoetrope"><img src="https://img.shields.io/crates/d/zoetrope.svg?style=flat&labelColor=121212&color=d7af00" alt="downloads"></a>
  <a href="https://github.com/furkankly/zoetrope/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/furkankly/zoetrope/ci.yml?branch=main&style=flat&labelColor=121212&color=d7af00&logo=GitHub%20Actions&logoColor=white" alt="build status"></a>
  <a href="https://crates.io/crates/zoetrope"><img src="https://img.shields.io/crates/msrv/zoetrope?style=flat&labelColor=121212&color=d7af00&label=MSRV" alt="minimum supported Rust version"></a>
</p>

<p align="center">
  <a href="https://zoetrope.furkankly.dev"><b>zoetrope.furkankly.dev</b></a> · the whole app in your browser, the same binary compiled to WASM
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/furkankly/zoetrope/main/assets/zoetrope.svg" alt="A session drawn as a flow graph: a main agent above the subagents it spawned, over a timeline of tool activity" width="620">
</p>

Claude Code and Codex write a transcript for every session. zoetrope reads it and draws
the session as a graph in your terminal: the main agent, the agents it spawns, and the
tools each one runs, updating live as it goes. Point it at a finished run and it replays,
paced by the session's own timestamps. Point it at a running one and it follows along.
It's read-only, and nothing leaves your machine.

Built on [ratatui](https://ratatui.rs) and [rataflow](https://github.com/furkankly/rataflow).

![zoetrope replaying a Claude Code session as a flow graph](https://raw.githubusercontent.com/furkankly/zoetrope/main/assets/zoetrope-demo.gif)

## Supported agents

| Agent | Sessions live in | Replay | Follow live | Browser |
| --- | --- | --- | --- | --- |
| [Claude Code](https://claude.com/claude-code) | `~/.claude/projects/` | ✓ | ✓ | ✓ sessions and subagents |
| [Codex](https://openai.com/codex/) CLI and desktop app | `~/.codex/sessions/` | ✓ | ✓ | ✓ sessions and subagents |

zoetrope reads a session from any of its files and tells the formats apart by
content, so `zoe <file>` works for either, and `zoe <id>` finds a session by id
across both.

![zoetrope replaying a Codex CLI session as a flow graph](https://raw.githubusercontent.com/furkankly/zoetrope/main/assets/zoetrope-codex.gif)

## Installation

**Homebrew** — macOS and Linux:

```bash
brew install furkankly/tap/zoetrope
```

**Cargo** — needs a Rust toolchain:

```bash
cargo install zoetrope
```

**Prebuilt binaries** — no toolchain needed. Every
[release](https://github.com/furkankly/zoetrope/releases) carries archives for
macOS (Apple Silicon and Intel), Linux (`musl`, arm64 and x86_64) and Windows
(x86_64). Unpack one and put `zoe` on your `PATH`.

Whichever route you take, the command is `zoe`. Or build from source:

```bash
git clone https://github.com/furkankly/zoetrope
cd zoetrope
cargo build --release
./target/release/zoe
```

No install at all: **[try it in your browser](https://zoetrope.furkankly.dev/app)**.
Drop a transcript on the page and get the same graph.

## In Herdr

[Herdr](https://herdr.dev) is a terminal multiplexer built for running coding
agents side by side. It knows which agent occupies a pane and the id of the
session running there, so the plugin in
[`herdr-plugin/`](https://github.com/furkankly/zoetrope/tree/main/herdr-plugin)
opens that exact session in `zoe`, without you naming a file or an id.

```bash
herdr integration install claude          # and/or codex, so Herdr learns session ids
herdr plugin install furkankly/zoetrope/herdr-plugin
herdr plugin action invoke setup-keys --plugin furkankly.zoetrope
```

Focus an agent pane and press `prefix+shift+z`. The graph opens over the pane,
follows the session live, and the same key closes it. There are placements for
a split and a tab as well, and the plugin's
[README](https://github.com/furkankly/zoetrope/blob/main/herdr-plugin/README.md)
covers both.

![the zoetrope plugin opening a Claude Code pane's session as a graph inside Herdr](https://raw.githubusercontent.com/furkankly/zoetrope/main/assets/zoetrope-herdr.gif)

## Usage

```bash
zoe                          # follow the current project's live session
zoe <dir>                    # follow another project's sessio