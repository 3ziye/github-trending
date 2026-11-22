# gputaskman

**An `htop` for what's inside your GPU, not just how full it is.**

Windows with NVIDIA/AMD telemetry and Intel WDDM activity, plus Linux and WSL support (NVIDIA
everywhere, AMD and Intel on native Linux; see
[Linux and WSL](#linux-and-wsl)) and macOS on Apple Silicon (see [macOS](#macos-apple-silicon)). A terminal UI
that connects per-process GPU memory and engine activity with loaded runtimes, model files, and
LLM buffer breakdowns.

Task Manager says "15 GB used." This tries to answer: *by what? Model weights? KV cache?
Your browser? The desktop compositor? And why is so much GPU memory in system RAM?*

**Scope: local GPU workloads, not cloud services.** Decision models, vision, speech, LLM inference,
training/fine-tuning (including Unsloth), graphics, and video all belong here. Visibility varies:
process memory and engine activity are measured; identifying individual models and their work
requires supporting evidence. A PyTorch/CUDA DLL alone cannot identify a model or prove training,
and a mapped file does not prove that model is resident on the GPU or being exercised.
CPU-only, NPU-only, and cloud workloads are out of scope.

![Live GPU overview with an LLM's weights, KV cache, and compute buffer breakdown](docs/screenshots/overview.png)

> Early, experimental software. Device and process counters are measurements; classifications
> and GGUF-derived breakdowns are estimates. This does not dump VRAM or enumerate a game's textures.

## Install from PyPI

[gputaskman is on PyPI](https://pypi.org/project/gputaskman/). No repository clone is needed:

```powershell
uv tool install gputaskman
gputaskman
```

Or, with [pipx](https://pipx.pypa.io/):

```powershell
pipx install gputaskman
gputaskman
```

Works on Windows, Linux/WSL, and macOS with Python 3.11+ and the supported GPU/driver
configuration described below. Both installers keep the app in an isolated environment.
The shorter `gtm` command is also available. Upgrade with `uv tool upgrade gputaskman`
or `pipx upgrade gputaskman`; `gputaskman --version` shows what you have, and the TUI shows it
under the GPU panel. Each [release](https://github.com/shanselman/gputaskman/releases) lists what
changed. For Windows without Python, use the portable download below.

## Portable Windows download

The [Releases page](https://github.com/shanselman/gputaskman/releases) is where tagged builds
publish two portable ZIPs: `gputaskman-VERSION-windows-x64.zip` for Intel/AMD Windows PCs, and
`gputaskman-VERSION-windows-arm64.zip` for native Windows ARM64. These are separate native builds,
not a universal executable.

Extract the **entire ZIP**, keeping `_internal` beside `gputaskman.exe`. Open Windows Terminal
or PowerShell in the extracted folder:

```powershell
.\gputaskman.exe
.\gputaskman.exe --once
.\gputaskman.exe --json
```

No Python, uv, CUDA Toolkit, model download, or installation is needed. A supported GPU with a
current Windows WDDM driver is required. Builds are currently **unsigned**; code signing
and an installer are not part of this initial distribution. Each ZIP includes licenses and a
`.zip.sha256` companion file is published for integrity checks.

## Clone and run

Use **64-bit Windows 10/11** with a current WDDM driver and a terminal
(Windows Terminal is recommended). Live workload checks have included an RTX 4080 SUPER and an
RTX Spark N1X on Windows ARM64. CUDA workloads are supported on ARM64 with a compatible NVIDIA
driver and ARM64 CUDA runtime.

AMD live check: Radeon 860M Graphics on Windows 11 Enterprise build 26300, AMD driver 32.0.22050.1003.
During desktop/browser activity, WDDM reported per-process VRAM and AMD ADL reported GPU utilization,
clocks, and ASIC power; temperature, memory activity, and PCIe readings were unavailable. Vulkan/ROCm
workloads were not tested on this machine.

Intel and Qualcomm adapters on Windows can use WDDM's per-process memory and engine counters. When those
counters are available, device GPU activity is the busiest WDDM engine after combining its process counters.
An Intel or Qualcomm adapter reporting at most 512 MiB of dedicated memory and more shared system memory is
treated as integrated: per-process local usage is shown as Shared RAM, not VRAM, while device dedicated and
shared counters remain separate. This is a DXGI-capacity heuristic. Qualcomm GPU activity uses the WDDM
adapter counter; temperature, power, clocks, and memory activity are not currently available on Windows.
Arc B580 behavior is covered by mocked counters but has not been validated on Intel hardware.
When a Windows telemetry provider does not supply a version, gputaskman reads the selected adapter's
`DriverVersion` from its exact PnP device's driver registry key. If that value is unavailable, the
driver remains unknown.

Install [Git for Windows](https://git-scm.com/downloads/win) and
[uv](https://docs.astral.sh/uv/getting-started/installation/) if needed. With WinGet:

```powershell
winget install --id Git.Git --exact
w