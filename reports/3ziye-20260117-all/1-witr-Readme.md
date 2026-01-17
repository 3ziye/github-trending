<div align="center">

# witr

### Why is this running?

[![Go Version](https://img.shields.io/github/go-mod/go-version/pranshuparmar/witr?style=flat-square)](https://github.com/pranshuparmar/witr/blob/main/go.mod) [![Go Report Card](https://goreportcard.com/badge/github.com/pranshuparmar/witr?style=flat-square)](https://goreportcard.com/report/github.com/pranshuparmar/witr) [![Build Status](https://img.shields.io/github/actions/workflow/status/pranshuparmar/witr/pr-check.yml?branch=main&style=flat-square&label=build)](https://github.com/pranshuparmar/witr/actions/workflows/pr-check.yml) [![Platforms](https://img.shields.io/badge/platforms-linux%20%7C%20macos%20%7C%20windows%20%7C%20freebsd-blue?style=flat-square)](https://github.com/pranshuparmar/witr) [![Latest Release](https://img.shields.io/github/v/release/pranshuparmar/witr?label=Latest%20Release&style=flat-square)](https://github.com/pranshuparmar/witr/releases/latest) <br>
[![Homebrew](https://img.shields.io/homebrew/v/witr?style=flat-square)](https://formulae.brew.sh/formula/witr) [![Conda](https://img.shields.io/conda/vn/conda-forge/witr?style=flat-square)](https://anaconda.org/conda-forge/witr) [![AUR](https://img.shields.io/aur/version/witr-bin?style=flat-square)](https://aur.archlinux.org/packages/witr-bin) [![FreeBSD Port](https://repology.org/badge/version-for-repo/freebsd/witr.svg?style=flat-square)](https://www.freshports.org/sysutils/witr/) [![AOSC OS](https://repology.org/badge/version-for-repo/aosc/witr.svg?style=flat-square)](https://packages.aosc.io/packages/witr) [![GNU Guix package](https://repology.org/badge/version-for-repo/gnuguix/witr.svg?style=flat-square)](https://packages.guix.gnu.org/packages/witr/)

<img width="1232" height="693" alt="witr_banner" src="https://github.com/user-attachments/assets/e9c19ef0-1391-4a5f-a015-f4003d3697a9" />

</div>

---

<div align="center">

[**Purpose**](#1-purpose) • [**Installation**](#2-installation) • [**Goals**](#3-goals) • [**Core Concept**](#4-core-concept) • [**Supported Targets**](#5-supported-targets)
<br>
[**Output Behavior**](#6-output-behavior) • [**Flags**](#7-flags--options) • [**Examples**](#8-example-outputs) • [**Platforms**](#9-platform-support) • [**Success Criteria**](#10-success-criteria)

</div>

---

## 1. Purpose

**witr** exists to answer a single question:

> **Why is this running?**

When something is running on a system—whether it is a process, a service, or something bound to a port—there is always a cause. That cause is often indirect, non-obvious, or spread across multiple layers such as supervisors, containers, services, or shells.

Existing tools (`ps`, `top`, `lsof`, `ss`, `systemctl`, `docker ps`) expose state and metadata. They show _what_ is running, but leave the user to infer _why_ by manually correlating outputs across tools.

**witr** makes that causality explicit.

It explains **where a running thing came from**, **how it was started**, and **what chain of systems is responsible for it existing right now**, in a single, human-readable output.

---

## 2. Installation

witr is distributed as a single static binary for Linux, macOS, FreeBSD, and Windows.

witr is also independently packaged and maintained across multiple operating systems and ecosystems. An up-to-date overview of packaging status is available on [Repology](https://repology.org/project/witr/versions). Please note that community packages may lag GitHub releases due to independent review and validation.

> [!TIP]
> If you use a package manager (Homebrew, Conda, etc.), we recommend installing via that for easier updates. Otherwise, the install script is the fastest way to get started.

---

### 2.1 Script Installation

The easiest way to install **witr** is via the install script.

#### Unix (Linux, macOS & FreeBSD)

```bash
curl -fsSL https://raw.githubusercontent.com/pranshuparmar/witr/main/install.sh | bash
```

<details>
<summary>Script Details</summary>

The script will:
- Detect your operating system (`linux`, `darwin` or `freebsd`)
- Detect your CPU architecture (`amd64` or `arm64`)
- Download the latest released binary and man page
- Install it to `/usr/local/bin/witr`
- Install the man page to `/usr/local/share/man/man1/witr.1`
- Pass INSTALL_PREFIX to override default install path

</details>

#### Windows (PowerShell)

```powershell
irm https://raw.githubusercontent.com/pranshuparmar/witr/main/install.ps1 | iex
```

<details>
<summary>Script Details</summary>

The script will:
- Download the latest release (zip) and verify checksum.
- Extract `witr.exe` to `%LocalAppData%\witr\bin`.
- Add the bin directory to your User `PATH`.

</details>

---

### 2.2 Package Managers

<details>
<summary><strong>Homebrew (macOS & Linux)</strong></summary>
<br>

You can install **witr** using [Homebrew](https://brew.sh/) on macOS or Linux:

```bash
brew install witr
```

See the [Homebrew Formula page](https://formulae.brew.sh/formula/witr#default) for more details.
</details>

<details>
<summary><s