<div align="center">

<a href="https://rmux.io">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://rmux.io/rmux-header-dark.svg">
    <img src="https://rmux.io/rmux-header.svg" alt="RMUX" width="500">
  </picture>
</a>

**A modern Rust terminal multiplexer for local shells, long-running agents, typed automation, and browser-shared terminal sessions.**

English · [Français](README.fr.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md)

[![License: MIT OR Apache-2.0](https://img.shields.io/badge/license-MIT%20OR%20Apache--2.0-blue.svg)](LICENSE-MIT)
[![Release validation](https://github.com/Helvesec/rmux/actions/workflows/ci.yml/badge.svg)](https://github.com/Helvesec/rmux/actions/workflows/ci.yml)
[![rmux 0.5.0](https://img.shields.io/badge/rmux-0.5.0-informational.svg)](#install)
[![Platform: Linux | macOS | Windows](https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey.svg)](#platform-support)
[![Unsafe policy](https://img.shields.io/badge/unsafe-restricted-success.svg)](#verification)

<br />
<a href="https://rmux.io">
  <img src="https://rmux.io/rmux-terminal-demo.gif" width="500" alt="RMUX terminal session demo" />
</a>

</div>

> [!NOTE]
> RMUX now includes serverless, hybrid post-quantum end-to-end web multiplexing. [Learn more in the repository Web Share docs](docs/web-share.md).
>
> RMUX is still moving fast. If you have a feature request or want to report anything, please [file an issue](https://github.com/Helvesec/rmux/issues).

## RMUX
A modern, async typed Rust <strong>multiplexer engine</strong> with native support for 90+ tmux commands across macOS, Linux, and Windows, with no WSL needed.

It ships with a public Rust SDK for persistent AI workflows and beautiful Ratatui TUIs.

Use it as your daily driver, share sessions in a browser, or script it into a <strong>persistent agentic TUI tool</strong>.

## Demos

Short examples of what RMUX can be used for.

<table>
  <tr>
    <td align="center" width="25%"><a href="https://rmux.io/#demo-orchestration"><img src="https://rmux.io/demos/demo-orchestration.png" width="150" alt="Multi Agents Orchestration demo preview"></a><br><sub><a href="https://github.com/Helvesec/rmux-demos/tree/main/demo-orchestration"><strong>Multi Agents Orchestration</strong></a></sub><br><sub>≃ 514 lines</sub></td>
    <td align="center" width="25%"><a href="https://rmux.io/#demo-broadcast"><img src="https://rmux.io/demos/demo-broadcast.png" width="150" alt="Agent Broadcast Arena demo preview"></a><br><sub><a href="https://github.com/Helvesec/rmux-demos/tree/main/broadcast-demo"><strong>Agent Broadcast Arena</strong></a></sub><br><sub>≃ 2,171 lines</sub></td>
    <td align="center" width="25%"><a href="https://rmux.io/#demo-zellij"><img src="https://rmux.io/demos/demo-zellij.png" width="150" alt="Mini-Zellij demo preview"></a><br><sub><a href="https://github.com/Helvesec/rmux-demos/tree/main/mini-zellij"><strong>Mini-Zellij</strong></a></sub><br><sub>≃ 944 lines</sub></td>
    <td align="center" width="25%"><a href="https://rmux.io/#demo-playwright"><img src="https://rmux.io/demos/demo-playwright.png" width="150" alt="Terminal automation demo preview"></a><br><sub><a href="https://github.com/Helvesec/rmux-demos/tree/main/terminal-playwright-demo"><strong>Terminal Automation</strong></a></sub><br><sub>≃ 1,495 lines</sub></td>
  </tr>
</table>



## Web Multiplex (Web Share)

<p align="center">
<a href="https://rmux.io/docs/web-share/">
  <img src="https://rmux.io/web-share-browser.png" width="500" alt="RMUX web share" />
</a>
</p>

RMUX lets you do web multiplexing: share your RMUX pane or session on the web, create new panes, move dividers with the mouse, and use RMUX through a richer browser interface.


```sh
# Start a local Web Share over loopback
rmux web-share

# Share a named session
rmux new-session -d -s work
rmux web-share -t work

# Share beyond localhost
rmux web-share --tunnel-provider localhost-run
```

Use a tunnel provider, bring your own ingress, or host the static frontend on your own domain.

Useful entry points:

- [Repository Web Share overview](docs/web-share.md)
- [Web Share docs](https://rmux.io/docs/web-share/)
- [Security model](https://rmux.io/docs/web-share/#/security)
- [Tunnel providers](https://rmux.io/docs/web-share/#/tunnels)

## Install

<a id="install-linux"></a>
<details>
<summary><strong>Linux install</strong></summary>

#### Portable installer

```sh
curl -fsSL https://rmux.io/install.sh | sh
```

#### APT

```sh
sudo install -d -m 0755 /etc/apt/keyrings
curl -fsSL https://packages.rmux.io/debian/rmux.asc | sudo tee /etc/apt/keyrings/rmux.asc >/dev/null
echo "deb [signed-by=/etc/apt/keyrings/rmux.asc] https://packages.rmux.io/debian stable main" | sudo tee /etc/apt/sources.list.d/rmux.list >/dev/null
sudo apt update
sudo apt install rmux
```

#### DNF

```sh
sudo curl -fsSL https://packages.rmux.io/rpm/rmux.repo -o /etc/yum.repos.d/rmux.repo
sudo dnf install rmux
```

Direct download