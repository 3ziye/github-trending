<p align="center">
  <img src="https://raw.githubusercontent.com/furkankly/zoetrope/main/assets/icon.svg" alt="" width="80">
</p>

<h1 align="center">zoetrope</h1>

<p align="center">
  <em>Watch a Claude Code session as a live flow graph, in your terminal or your browser.</em>
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

Claude Code writes a JSONL transcript for every session under `~/.claude/projects/`.
zoetrope reads it and draws the session as a graph in your terminal: the main agent, the subagents and
workflows it spawns, and the tools each one runs, updating live as it goes. Point it
at a finished run and it replays, paced by the session's own timestamps. Point it at a
running one and it follows along. It's read-only, and nothing leaves your machine.

Built on [ratatui](https://ratatui.rs) and [rataflow](https://github.com/furkankly/rataflow).

![zoetrope replaying a Claude Code session as a flow graph](https://raw.githubusercontent.com/furkankly/zoetrope/main/assets/zoetrope-demo.gif)

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

## Usage

```bash
zoe                          # follow the current project's live session
zoe <dir>                    # follow another project's session
zoe <file.jsonl>             # replay a recording from the start
zoe <file.jsonl> --follow    # open a recording at its live edge
zoe <file.jsonl> --speed N   # playback speed (default 8.0)
zoe inspect <file.jsonl>     # print the session tree and exit (no TUI)
```

Give it a file and it reads the whole transcript, then keeps watching for new lines.
Give it a directory, or no argument at all, and it finds the newest session in that
project and follows it live. Whichever way you start, the controls are the same:
scrub, follow, pause, jump back to live.

The same engine also runs [in the browser](https://zoetrope.furkankly.dev/app),
compiled to WebAssembly via [ratzilla](https://github.com/ratatui/ratzilla). Open a
session from disk, or drop a transcript on the page. It stays local there too.

## Features

**The graph**
- A node per agent: the main session, its subagents, and workflow groups with their
  children nested underneath
- Status, current tool, tool count and output tokens on every card
- Edges animate while an agent is working, and settle when it finishes
- Tool calls surface as chips beneath their agent (`⚒ bash ×5`, or `⚒ bash 0.5s`
  ticking during a single call), resolving to `✓` or `✗`
- A minimap showing where your viewport sits once the graph outgrows the screen

**Time travel**
- One scrubbable timeline over both live and replayed sessions
- Indexed by event rather than wall-clock, so a busy minute gets room instead of
  collapsing into a sliver
- Scrub, pause, step between prompt eras, or snap back to the live edge
- Seek backwards and you see the session exactly as it stood at that moment. Agents
  un-finish, tool counts