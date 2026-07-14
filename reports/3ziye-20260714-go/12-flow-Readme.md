<div align="center">

### flow

*A terminal dashboard for real-time network throughput.*

<img src="./assets/demo.gif" alt="flow demo" width="100%">

<h3 align="center">
  Featured on&nbsp;&nbsp;<a href="https://terminaltrove.com/flow"><img src="assets/terminal_trove_black_green.png" alt="Terminal Trove logo" width="140" valign="middle"></a>
</h3>

<p align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&pause=1200&color=00E0A4&center=true&vCenter=true&repeat=false&width=460&lines=Your+Internet+Stats%2C+TUIfied." alt="Typing SVG" />
  </a>
</p>

<p align="center">
  <i>Fast • Beautiful • Cross-Platform • Open Source</i>
</p>

</div>

<p align="center">
  <a href="https://github.com/programmersd21/flow/actions">
    <img src="https://img.shields.io/github/actions/workflow/status/programmersd21/flow/release.yml?style=for-the-badge&logo=githubactions&logoColor=white&label=Build&labelColor=111111&color=00c853" alt="Build">
  </a>
  <a href="https://github.com/programmersd21/flow/releases">
    <img src="https://img.shields.io/github/v/release/programmersd21/flow?style=for-the-badge&logo=github&logoColor=white&label=Release&labelColor=111111&color=ff6d00" alt="Release">
  </a>
  <a href="https://github.com/programmersd21/flow/releases">
    <img src="https://img.shields.io/github/downloads/programmersd21/flow/total?style=for-the-badge&logo=github&logoColor=white&label=Downloads&labelColor=111111&color=8e24aa" alt="Downloads">
  </a>
  <a href="https://github.com/programmersd21/flow/stargazers">
    <img src="https://img.shields.io/github/stars/programmersd21/flow?style=for-the-badge&logo=github&logoColor=white&label=Stars&labelColor=111111&color=fbc02d" alt="Stars">
  </a>
</p>

<p align="center">
  <a href="https://github.com/programmersd21/flow">
    <img src="https://img.shields.io/github/go-mod/go-version/programmersd21/flow?style=for-the-badge&logo=go&logoColor=white&label=Go&labelColor=111111&color=2196f3" alt="Go Version">
  </a>
  <a href="https://github.com/programmersd21/flow/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/programmersd21/flow?style=for-the-badge&label=License&labelColor=111111&color=43a047" alt="License">
  </a>
  <a href="https://github.com/programmersd21/homebrew-flow">
    <img src="https://img.shields.io/badge/Homebrew-brew%20install%20programmersd21%2Fflow%2Fflow?style=for-the-badge&logo=homebrew&logoColor=white&labelColor=111111&color=fbb040" alt="Homebrew">
  </a>
  <a href="https://aur.archlinux.org/packages/flow-network-monitor-bin">
    <img src="https://img.shields.io/aur/version/flow-network-monitor-bin?style=for-the-badge&logo=archlinux&logoColor=white&label=AUR&labelColor=111111&color=1793d1" alt="AUR Version">
  </a>
  <a href="https://aur.archlinux.org/packages/flow-network-monitor-bin">
    <img src="https://img.shields.io/aur/popularity/flow-network-monitor-bin?style=for-the-badge&logo=archlinux&logoColor=white&label=Popularity&labelColor=111111&color=1976d2" alt="AUR Popularity">
  </a>
</p>

## Contents

- [Install](#install)
- [Rationale](#rationale)
- [Philosophy](#philosophy)
- [Modes](#modes)
- [Features](#features)
- [Usage](#usage)
- [Configuration](#configuration)
- [Architecture](#architecture)
- [Development](#development)
- [Star History](#star-history)
- [License](#license)

## Install

### Arch Linux (AUR)

```sh
yay -S flow-network-monitor-bin
```

> 💝 Thanks to [@Dominiquini](https://github.com/Dominiquini) for helping bring Flow to the AUR!

### Homebrew:

```sh
brew install programmersd21/flow/flow
```

### Go:

```sh
go install github.com/programmersd21/flow/cmd/flow@latest
```

### From source:

```sh
git clone https://github.com/programmersd21/flow
cd flow
make install
```

Pre-built binaries for Linux, macOS, and Windows (amd64 and arm64) are available on the [releases page](https://github.com/programmersd21/flow/releases).

## Rationale

Most network monitors display CPU usage, per-process breakdowns, packet counts, and connection tables. flow displays throughput only.

| btop | flow |
|:---:|:---:|
| <img src="./assets/btop.png" alt="btop"> | <img src="./assets/flow.png" alt="flow"> |
| CPU, memory, disks, processes, network | throughput only |

Every feature decision is evaluated against a single question: does this help the user understand their network within one second. If not, it is not included.

The result is a small, deliberately scoped tool. There are no additional panels, no required configuration, and no unnecessary complexity in either the interface or the underlying implementation.

## Philosophy

```mermaid
flowchart LR
    Input["Network throughput"] --> Q{"Understood within<br/>one second?"}
    Q -->|Yes| Keep["Retain feature"]
    Q -->|No| Cut["Remove feature"]
    Keep --> Result["Calm, minimal interface"]
    Cut --> Result
```

Every feature is evaluated against one question: does this help a user understand 