# Terminal Control

Control, inspect, test, and capture real terminal applications for agents and TUI review.

[![crates.io](https://img.shields.io/crates/v/terminal-control.svg)](https://crates.io/crates/terminal-control)
[![CI](https://github.com/kitlangton/terminal-control/actions/workflows/ci.yml/badge.svg)](https://github.com/kitlangton/terminal-control/actions/workflows/ci.yml)

![OpenCode answering a playful terminal request](https://raw.githubusercontent.com/kitlangton/terminal-control/main/docs/screenshots/opencode-haikus.png)

Saved from one live OpenCode session using `start`, `send`, and `save`.

## Agent Quickstart

Terminal Control is built for agents first. Install the `termctrl` binary, install the skill, then ask your coding agent to operate terminal applications through a real pseudo-terminal instead of guessing from plain command output.

Requires Rust 1.93 or newer. Video export also requires `ffmpeg`.

```bash
cargo install terminal-control
termctrl --help
```

Install the current repository head instead of the latest crate release:

```bash
cargo install --locked --git https://github.com/kitlangton/terminal-control terminal-control
```

Install the agent skill from this repository:

```bash
npx skills add kitlangton/terminal-control --skill terminal-control
```

Then ask your agent for terminal work in ordinary language:

```text
Use terminal-control to open my TUI, press through the setup flow, and save a screenshot of the final screen.
```

```text
Start two terminal sessions: one running the dev server and one running the CLI. Drive the CLI until it connects, then show me both screens.
```

```text
Record yourself using the terminal app, mark the important moments, and export a short MP4 demo.
```

The skill teaches agents the safe workflow: start named sessions, wait for visible text, send exact input, inspect screens, save artifacts, record timelines, mark important moments, export videos, and stop sessions when finished.

## What It Gives Agents

- Real PTY control for TUIs, shells, curses apps, OpenTUI apps, and long-running CLIs.
- Named background sessions so an agent can keep multiple terminals alive and switch between them.
- Visible-screen reads through `show`, not brittle scraping of scrollback or logs.
- Exact keyboard and text input with `send`, including arrows, tabs, enter, escape, page keys, and `ctrl-a` through `ctrl-z`.
- Explicit waits for rendered text before interacting.
- Resizing to test responsive terminal layouts.
- Evidence capture as PNG, SVG, text, JSON, or ANSI when requested.
- Recording timelines with markers, edited MP4 export, and optional branded footers for demos and bug reports.
- Local-only owner-protected session sockets and explicit warnings around sensitive terminal artifacts.

## CLI Quickstart

Read a one-off terminal screen:

```bash
termctrl show --cols 100 --rows 32 -- my-terminal-app
```

Save evidence:

```bash
termctrl save --format png --format txt --out captures/home -- my-terminal-app
```

Drive a persistent TUI session:

```bash
termctrl start demo --host opentui --cols 112 --rows 34 -- opencode
termctrl wait demo "Ask anything" --timeout 20000
termctrl send demo --pace-ms 35 'text:Write a terminal haiku.' enter
termctrl show demo
termctrl stop demo
```

Record and export a video:

```bash
termctrl start demo --host opentui --record captures/demo.termctrl -- opencode
termctrl wait demo "Ask anything"
termctrl mark demo ready
termctrl send demo --pace-ms 35 'text:Write a short terminal haiku. End with DONE.' enter
termctrl wait demo "DONE" --timeout 60000
termctrl mark demo after-answer
termctrl stop demo
termctrl video captures/demo.termctrl --edit captures/demo.json --out captures/demo.mp4
```

The sections below explain each workflow in more detail.

## Install The CLI

Requires Rust 1.93 or newer. Video export also requires `ffmpeg`.

```bash
cargo install terminal-control
termctrl --help
```

Install the current repository head instead of the latest crate release:

```bash
cargo install --locked --git https://github.com/kitlangton/terminal-control terminal-control
```

## Show A Terminal Screen

Run a program in a PTY and print its visible terminal state:

```bash
termctrl show --cols 100 --rows 32 -- my-terminal-app
```

Show is the routine observation command: it prints visible text to standard output and creates no files. Request a different stdout-readable representation explicitly:

```bash
termctrl show --format json -- my-terminal-app
termctrl show --format svg -- my-terminal-app
```

Wait for an application to mount, then interact before reading its screen:

```bash
termctrl show --cols 100 --rows 32 --wait-for "Commands" \
  -s ctrl-p text:model enter -- my-terminal-app
```

OpenTUI applications such as OpenCode require the opt-in host handshake:

```bash
termctrl show --host opentui --cols 112 --rows 34 \
  --wait-for "/connect" -- opencode
```

## Save Evidence

Write only the artifact formats you request:

```bash
te