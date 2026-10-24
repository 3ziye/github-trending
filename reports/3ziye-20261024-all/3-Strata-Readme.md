<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="apps/host/public/brand/strata-lockup-dark.svg">
    <img src="apps/host/public/brand/strata-lockup-light.svg" alt="Strata" width="380">
  </picture>
</p>

<p align="center"><b>English</b> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.de.md">Deutsch</a> · <a href="README.fr.md">Français</a> · <a href="README.es.md">Español</a> · <a href="README.pt-BR.md">Português</a></p>

<h3 align="center">Run a state-of-the-art model on your own gaming PC</h3>

<p align="center">Support for NVIDIA, AMD, Intel · Windows, Linux, Mac · free and open source</p>

<p align="center">
  <a href="https://github.com/Niko1221/Strata/releases"><img src="https://img.shields.io/github/v/release/Niko1221/Strata?include_prereleases&label=release" alt="Latest release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/Niko1221/Strata" alt="MIT license"></a>
  <a href="https://github.com/Niko1221/Strata/stargazers"><img src="https://img.shields.io/github/stars/Niko1221/Strata?style=flat" alt="GitHub stars"></a>
</p>

<p align="center"><a href="https://github.com/Niko1221/Strata/releases/download/v0.1.10/Pagoda.mp4"><img src="docs/media/pagoda-preview.webp" width="720" alt="A voxel pagoda garden that Strata's model wrote, running in the browser"></a><br>
<sub>A voxel pagoda garden, 1 shot prompt running on an RTX 5070 with Strata (IQ3_S, 128K context) ·
<a href="https://github.com/Niko1221/Strata/releases/download/v0.1.10/Pagoda.mp4">full video (49 s)</a></sub></p>

Strata runs **[Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)**, a 125-billion-parameter model that
normally needs a server, on a normal PC. It chats, writes code, reads pictures and works with your apps and coding
agents. Your chats and files stay on your PC.

**New here?** Check [what you need](#what-you-need), then [install the app](#option-a-the-strata-app).

- **Runs on a gaming PC.** 32 GB of RAM and graphics memory together is enough to start.
- **Works with your tools.** It speaks the OpenAI and Anthropic APIs, so Claude Code, Codex CLI, OpenCode and other agents connect to it.
- **Reads pictures.** They are on by default.
- **Free.** MIT license, no account, no cloud.
- **Private.** No telemetry. What Strata downloads, when it uses the internet and how it checks downloads is in [docs/SAFETY.md](docs/SAFETY.md).

Version 0.2.3 · engine 0.1.48

## What you need

**You need at least 32 GB of RAM and graphics memory (VRAM) together.** On a Mac or a Ryzen AI Max, that is the unified
memory. More memory gives a bigger model or a faster one.

- A 32 GB PC with a 12-16 GB card runs the Coder.
- 64 GB of RAM runs every size.

| Your computer | Details |
| --- | --- |
| **NVIDIA** GeForce RTX 20, 30, 40, 50 series (12 GB or more) | Install the app or the Terminal. |
| **AMD** Radeon RX 6800 and newer, Radeon AI PRO R9700 (12 GB or more) | [AMD cards](docs/AMD_HIP.md) |
| **Intel** Arc | [Intel Arc](docs/INTEL_ARC.md), [Intel engine](docs/INTEL.md) |
| **Apple Silicon Mac** (M1 or newer, macOS 15 or newer) | [Mac](docs/MAC.md) |
| **AMD Ryzen AI Max (Strix Halo)** and other unified-memory systems | [Strix Halo](docs/STRIX_HALO.md) |
| Older cards and processors | [Older GPUs](docs/OLDER_GPUS.md), [Older CPUs](docs/INSTALL.md#older-cpus-experimental) |

Also needed:

- about 80 GB of free disk (an SSD makes the first start much faster)
- Windows 10 / 11, Linux or macOS
- a current graphics driver

Two or three cards of the same make can share a model ([multi-GPU](docs/MULTI_GPU.md)). Strata never splits a model across
NVIDIA and AMD cards. Full list: [docs/INSTALL.md](docs/INSTALL.md#what-you-need).

## Install

Pick one option. They all start the same engine and use the same models.

### Option A: the Strata app

The easiest way. The app has the engine inside: install it, pick a model, chat. Download the file for your system and
graphics card from the [releases page](https://github.com/Niko1221/Strata/releases/latest). Not sure which one? See the
line under the table.

| System | Your graphics card | File to download |
| --- | --- | --- |
| **Windows 10 / 11** | NVIDIA RTX, driver 580 or newer | [`Strata-0.2.3-windows-cuda13.exe`](https://github.com/Niko1221/Strata/releases/latest/download/Strata-0.2.3-windows-cuda13.exe) |
| | NVIDIA, older card or driver older than 580 | [`Strata-0.2.3-windows-cuda12.exe`](https://github.com/Niko1221/Strata/releases/latest/download/Strata-0.2.3-windows-cuda12.exe) |
| | AMD Radeon RX 9000 series or Radeon AI PRO R9700 | [`Strata-0.2.3-windows-hip.exe`](https://github.com/Niko1221/Strata/releases/latest/download/Strata-0.2.3-windows-hip.exe) |
| | AMD Radeon RX 7000 series or Ryzen AI Max (Strix Halo) | [`Strata-0.2.3-windows-hip-rdna3.exe`](https://github.com/Niko1221/Strata/releases/latest/download/Strata-0.2.3-windows-hip-rdna3.exe) |
| **Linux** | NVIDIA RTX, driver 580 or