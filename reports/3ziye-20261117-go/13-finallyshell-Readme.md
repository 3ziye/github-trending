<h1 align="center">
  <img src="resources/icon.png" width="64" height="64" alt="" align="center">&nbsp;Finallyshell
</h1>

<p align="center">
  An SSH client with FinalShell's layout and vertical session tabs, written in Go.
</p>

<p align="center">
  <a href="https://github.com/TooonyChen/finallyshell/releases/latest"><img src="https://img.shields.io/github/v/release/TooonyChen/finallyshell?label=release" alt="Latest release"></a>
  <a href="https://github.com/TooonyChen/finallyshell/actions/workflows/ci.yml"><img src="https://github.com/TooonyChen/finallyshell/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <img src="https://img.shields.io/badge/platform-macOS%20%7C%20Windows%20%7C%20Linux-lightgrey" alt="macOS, Windows, Linux">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-PolyForm%20Noncommercial-blue" alt="License"></a>
  <br>
  <a href="https://awesomemygo.dev/apps/finallyshell"><img src="https://awesomemygo.dev/badge.svg" alt="Listed on Awesome MyGo"></a>
  <br>
  <a href="https://trendshift.io/repositories/343771?utm_source=trendshift-badge&amp;utm_medium=badge&amp;utm_campaign=badge-trendshift-343771" target="_blank" rel="noopener noreferrer"><img src="https://trendshift.io/api/badge/trendshift/repositories/343771/daily?language=Go" alt="TooonyChen%2Ffinallyshell | Trendshift" width="250" height="55"/></a>
</p>

<p align="center">
  <b>English</b> · <a href="README.zh-CN.md">简体中文</a>
  <br>
  <a href="#install">Install</a> · <a href="#features">Features</a> · <a href="#keyboard-shortcuts">Shortcuts</a> · <a href="docs/en/features.md">Full documentation</a>
</p>

<p align="center">
  <img src="docs/screenshots/main-en.png" alt="Finallyshell's main window: server monitor, session list, terminal and file panel">
</p>

If you have used FinalShell, you already know your way around: server stats at the top left, sessions under them, the terminal on the right and the remote files below it. Finallyshell keeps that layout and puts the session tabs in a vertical list you can scroll and drag to reorder.

It is a native app written in Go with the [MyGo](https://github.com/egoist/mygo) UI toolkit, so there's no Java runtime to install. The terminal is libghostty-vt, the terminal engine of [Ghostty](https://ghostty.org). Passwords go to the system's keychain, never to a file.

> [!IMPORTANT]
> The project's only official places are this repository and its site, [tooonychen.github.io/finallyshell](https://tooonychen.github.io/finallyshell/), and [Releases](https://github.com/TooonyChen/finallyshell/releases) here is the only official download. Any other site that offers downloads under the Finallyshell name is not affiliated with this project.

## Install

Download the latest build from [Releases](https://github.com/TooonyChen/finallyshell/releases/latest):

| System | File |
|---|---|
| macOS (Apple silicon) | `finallyshell-<version>-arm64.dmg` |
| macOS (Intel) | `finallyshell-<version>-amd64.dmg` |
| Windows (x64) | `finallyshell-setup-<version>-amd64.exe`, or the portable `.zip` |
| Debian, Ubuntu (x64) | `finallyshell_<version>_amd64.deb` |
| Other Linux (x64) | `finallyshell-<version>-linux-amd64.tar.gz`; `sh install.sh` installs it in `~/.local` |
| Debian, Ubuntu (ARM64) | `finallyshell_<version>_arm64.deb` |
| Other Linux (ARM64) | `finallyshell-<version>-linux-arm64.tar.gz`; `sh install.sh` installs it in `~/.local` |

To try what's on main before it's released, every merge also publishes a preview build on the [Releases](https://github.com/TooonyChen/finallyshell/releases) page, marked Pre-release. Installed apps don't update to previews; download them by hand.

The macOS app isn't notarized by Apple yet, so macOS blocks it the first time you open it. After dragging it to Applications, run:

```bash
xattr -dr com.apple.quarantine /Applications/Finallyshell.app
```

or open System Settings › Privacy & Security and click "Open Anyway". Windows SmartScreen may warn about the unsigned installer: click "More info", then "Run anyway".

On Linux, the tray icon needs `libayatana-appindicator3`, and remembering passwords needs a Secret Service keyring (GNOME Keyring, KWallet, KeePassXC). Without them the app still works; it just keeps passwords in memory.

After that, Finallyshell updates itself, except the `.deb`, which you update by installing the new one. Versions up to 0.2.0 can't: install a newer release by hand once.

## Features

### Connections

Open the connection manager with <kbd>Cmd</kbd>+<kbd>O</kbd> on macOS or <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>O</kbd> elsewhere. Hosts live in a tree of folders, as in FinalShell: drag them between folders, search by name, address, user or notes, duplicate a host, or delete it to a "Show deleted" list from which it can be restored.

The same tree stays in the main window too: the panel under the server stats switches between your sessions and Connections, where a double click opens a session and a green dot marks the hosts you have open