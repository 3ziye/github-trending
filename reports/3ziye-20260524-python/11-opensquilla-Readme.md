# OpenSquilla — Token-Efficient AI Agent

<p align="center">
  <img src="assets/opensquilla-long-logo.png" alt="OpenSquilla logo" width="500">
</p>

<p align="center">
  <b>Same budget, more capability, better results.</b><br>
  A microkernel AI agent for your CLI, Web UI, and chat channels.
</p>

<p align="center">
  <a href="https://github.com/opensquilla/opensquilla/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/opensquilla/opensquilla/ci.yml?style=for-the-badge" alt="CI"></a>
  <a href="https://opensquilla.ai/"><img src="https://img.shields.io/badge/website-opensquilla.ai-blue?style=for-the-badge" alt="Website"></a>
  <a href="https://github.com/opensquilla/opensquilla/releases"><img src="https://img.shields.io/github/v/release/opensquilla/opensquilla?include_prereleases&style=for-the-badge" alt="GitHub release"></a>
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.12%2B-blue?style=for-the-badge" alt="Python 3.12+"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache%202.0-blue?style=for-the-badge" alt="Apache 2.0 License"></a>
</p>

---

## Overview

OpenSquilla is a token-efficient, microkernel AI agent. A local model
router sends each turn to the cheapest model that can handle it, while
persistent memory, a layered sandbox, built-in web search, and
on-device embeddings round out a single shared turn loop.

Every entry point — Web UI, CLI, and chat channels — runs through that
same loop, so tool dispatch, retries, and decision logging behave
identically everywhere. A pluggable provider layer speaks to
OpenRouter, OpenAI, Anthropic, Ollama, DeepSeek, Gemini, Qwen/DashScope,
and 20+ other LLM providers with no change to your code or config
schema.

OpenSquilla 0.2.1 is the current release.

---

## Installation

OpenSquilla runs on Windows, macOS, and Linux. Pick the path that
matches your use case.

Windows portable and Quick terminal install give you a prebuilt
**release** — no Git required. The other two — Install from source
and Develop from source — build **from a Git checkout** (`git clone` +
Git LFS).

Release install commands use published GitHub release assets. The
Windows portable zip also has a `/releases/latest/download/` alias for
the current release. Python wheel installs use versioned wheel filenames
because installers validate the version embedded in the wheel filename.

| Path | Audience | When to use |
| --- | --- | --- |
| [Windows portable](#windows-portable-no-python) | Windows users | No Python toolchain; one-zip launch |
| [Quick terminal install](#quick-terminal-install) **(recommended)** | End users on any OS | Release wheel from a terminal |
| [Install from source](#install-from-source) | Users tracking `main` | Run from a checkout, not edit it |
| [Develop from source](#develop-from-source) | Contributors | Edit, test, or debug the source |

### Prerequisites

| Requirement | Windows portable | Quick terminal install | Install from source | Develop from source |
| --- | :---: | :---: | :---: | :---: |
| Python 3.12+ | bundled | via `uv` | via `uv` or system | via `uv` |
| Git + Git LFS | — | — | required | required |
| `uv` | — | installed if missing | recommended | required |

The default `recommended` profile installs **SquillaRouter** —
OpenSquilla's on-device model router — and its model assets;
`OPENSQUILLA_INSTALL_PROFILE=core` omits those dependencies. The
separate `--router disabled` onboarding flag keeps the dependencies
installed but turns the router off at runtime.

On Windows, SquillaRouter's bundled ONNX runtime also needs the Visual
C++ runtime. The Windows portable launcher and the from-source
PowerShell installer install it automatically via `winget`; the
**Quick terminal install** (`uv tool install`) path does not — if
startup logs a `DLL load failed` error, install it manually (see
[Troubleshooting](#troubleshooting)). OpenSquilla keeps running with
direct single-model routing until it is installed.

Install links: [Git](https://git-scm.com/downloads) ·
[Git LFS](https://git-lfs.com/) ·
[uv](https://docs.astral.sh/uv/getting-started/installation/).

### Windows portable (no Python)

The fastest path on Windows — the zip ships a bundled CPython runtime,
so no separate Python install is required.

1. Download the current portable zip:
   <https://github.com/opensquilla/opensquilla/releases/latest/download/OpenSquilla-windows-x64-portable.zip>
2. Extract it to a writable folder such as Downloads or Documents,
   then right-click `Start OpenSquilla.cmd` and choose **Run as
   administrator**.
3. Complete the first-run setup, then open <http://127.0.0.1:18791/control/>.

> [!NOTE]
> Preview builds are unsigned; administrator launch is the supported
> path. If SmartScreen appears, choose **More info** → **Run anyway**.
> If Smart App Control or enterprise policy blocks the unsigned app,
> use [Quick terminal install](#quick-terminal-install) instead.

<