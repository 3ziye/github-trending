<h4 align="right"><strong><a href="./README.md">English</a></strong> | <a href="./README_CN.md">简体中文</a></h4>

<p align="center">
  <a href="https://github.com/GaoSSR/best-claude-hud">
    <img src="assets/best-claude-hud-logo.png" alt="best-claude-hud" width="480">
  </a>
</p>

<h3 align="center"><nobr>Minimal Claude Code statusline HUD, powered by Rust</nobr></h3>

---

<p align="center">
  <img alt="Rust" src="https://img.shields.io/badge/Rust-CLI-orange" />
  <img alt="MacOS Linux Windows supported" src="https://img.shields.io/badge/MacOS%20%7C%20Linux%20%7C%20Windows-supported-brightgreen" />
  <img alt="Command: best-claude-hud" src="https://img.shields.io/badge/command-best--claude--hud-8A2BE2" />
  <img alt="License: Apache-2.0" src="https://img.shields.io/badge/license-Apache--2.0-blue" />
</p>

## best-claude-hud Overview

`best-claude-hud` is a high-performance Claude Code statusline tool written in Rust. It shows the status information you actually need while using Claude Code in a terminal: model and live reasoning effort, workspace, Git branch/status, context window usage, and optional usage/rate-limit metadata.

<p align="center">
  <img src="assets/best-claude-hud-preview.png" alt="best-claude-hud statusline preview" width="1200">
</p>

The default statusline focuses on:

- Claude model display with live reasoning effort when available
- Claude Code launch directory, stable across temporary working-directory changes
- Git branch, clean/dirty/conflict state, and ahead/behind counts
- context window usage from Claude Code's official statusLine data, with active-transcript fallback
- optional usage/rate-limit, cost, session, and output style segments

## Install

`best-claude-hud` is distributed through npm. The npm package uses prebuilt native binaries; users do not need Rust installed.

Install and configure Claude Code in one line:

```bash
npm install -g best-claude-hud@latest && best-claude-hud --setup
```

Restart Claude Code after setup. Existing sessions do not automatically reload `~/.claude/settings.json`.

Install only:

```bash
npm install -g best-claude-hud@latest
```

Using yarn or pnpm:

```bash
yarn global add best-claude-hud@latest
pnpm add -g best-claude-hud@latest
```

For users in China:

```bash
npm install -g best-claude-hud@latest --registry https://registry.npmmirror.com && best-claude-hud --setup
```

Update an existing installation:

```bash
npm install -g best-claude-hud@latest
```

Uninstall:

```bash
npm uninstall -g best-claude-hud
```

## Nix

`best-claude-hud` also ships a Nix flake for declarative and reproducible environments.

Run without installing globally:

```bash
nix run github:GaoSSR/best-claude-hud -- --help
```

Install into a Nix profile:

```bash
nix profile install github:GaoSSR/best-claude-hud
best-claude-hud --setup
```

For home-manager or another declarative setup, point Claude Code directly at the Nix store binary:

```nix
# In your flake inputs:
# best-claude-hud.url = "github:GaoSSR/best-claude-hud";

{ inputs, pkgs, ... }:

let
  hud = inputs.best-claude-hud.packages.${pkgs.system}.default;
in
{
  home.packages = [ hud ];

  home.file.".claude/settings.json".text = builtins.toJSON {
    statusLine = {
      type = "command";
      command = "${hud}/bin/best-claude-hud";
      padding = 0;
    };
  };
}
```

If you already manage `~/.claude/settings.json` with Nix, merge the `statusLine` block into your existing JSON instead of replacing the whole file.

Development shell:

```bash
nix develop
```

## Claude Code Configuration

`npm install -g best-claude-hud@latest` only installs the command. Claude Code will not show the HUD until `statusLine` is configured.

Recommended:

```bash
best-claude-hud --setup
```

The setup command writes a `statusLine` block to `~/.claude/settings.json` and preserves existing settings. It resolves the installed command to an absolute path when possible:

```json
{
  "statusLine": {
    "type": "command",
    "command": "/path/to/best-claude-hud",
    "padding": 0
  }
}
```

Manual configuration can also use `"command": "best-claude-hud"` if your Claude Code sessions inherit the same PATH as your shell. If `statusLine` already exists, `--setup` creates a timestamped backup next to `settings.json` before replacing it. Restart Claude Code after changing this file.

The npm package intentionally does not install a binary into `~/.claude`. It uses the global npm command and resolves the matching native binary from Kiri-style npm alias optional dependencies.

## Commands

```bash
best-claude-hud                    # open the interactive menu when run in a terminal
best-claude-hud --help             # print command help
best-claude-hud --version          # print version
best-claude-hud --setup            # configure Claude Code statusLine
best-claude-hud --config           # open the TUI configuration interface
best-claude-hud --theme minimal    # temporarily render with a built-in theme
best-claude-hud --patch <cli.j