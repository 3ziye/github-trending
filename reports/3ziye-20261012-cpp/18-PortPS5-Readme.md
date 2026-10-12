<p align="center">
  <img src="assets/logo.png" alt="PortPS5 Logo" width="180" />
</p>

# PortPS5

[![CI](https://img.shields.io/github/actions/workflow/status/yuriolive/PortPS5/ci.yml?branch=main&label=CI&style=flat-square)](https://github.com/yuriolive/PortPS5/actions/workflows/ci.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/yuriolive/PortPS5/codeql.yml?branch=main&label=CodeQL&style=flat-square)](https://github.com/yuriolive/PortPS5/actions/workflows/codeql.yml)
[![CodeRabbit Pull Request Reviews](https://img.shields.io/coderabbit/prs/github/yuriolive/PortPS5?style=flat-square&utm_source=oss&utm_medium=github&utm_campaign=yuriolive%2FPortPS5&color=FF570A&link=https%3A%2F%2Fcoderabbit.ai&label=CodeRabbit+Reviews)](https://coderabbit.ai)
[![License: GPL-2.0](https://img.shields.io/badge/license-GPL--2.0--only-blue?style=flat-square)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html)
[![Platform: Windows](https://img.shields.io/badge/platform-Windows%2010%2F11-informational?style=flat-square&logo=windows)](https://github.com/yuriolive/PortPS5)
[![Language: C++23](https://img.shields.io/badge/language-C%2B%2B23-informational?style=flat-square&logo=cplusplus)](https://github.com/yuriolive/PortPS5)
[![Vulkan 1.3](https://img.shields.io/badge/Vulkan-1.3-red?style=flat-square&logo=vulkan)](https://www.vulkan.org/)
[![GitHub Sponsors](https://img.shields.io/github/sponsors/yuriolive?style=flat-square&logo=githubsponsors&color=ea4aaa)](https://github.com/sponsors/yuriolive)
[![libraries](https://yuriolive.github.io/PortPS5/badge-libraries.svg)](https://yuriolive.github.io/PortPS5/)
[![shaders](https://yuriolive.github.io/PortPS5/badge-shaders.svg)](https://yuriolive.github.io/PortPS5/)

Native Windows execution of decrypted PS5 game dumps.

PortPS5 converts **user-supplied, already-decrypted PS5 game dumps** into native Windows executables plus replacement system libraries. It executes the game's x86-64 code directly on the host CPU without emulation, relinks guest ELFs into PE images, implements PS5 system libraries (`.prx`), and translates the GPU workload to Vulkan.

PortPS5 is a GPL-2.0-only hard fork of [AnyPS5](https://github.com/boykopovar/AnyPS5) by boykopovar. Hard fork means an independent product direction, not isolation: improvements flow from upstream continuously, but each one is adopted selectively and adapted to fork policy — never taken as-is, and never depended on. Full upstream tracking is revisited only after Milestone 3 (see [PRD §5](docs/PRD.md)).

## Why a hard fork

Upstream optimizes for title-by-title progress, including game-specific mechanisms and environment switches for tuning and tracing. PortPS5 optimizes for a shippable, Windows-first product boundary instead: generic mechanisms only, enforced by CI; typed config instead of switches; return codes instead of throws; and a measured 1.0 bar (sections below). Upstream currently shows more public real-game evidence; the fork's arrives as results JSON from M2 onward.

## Product decisions

- **No title-specific code in `core/`.** Every title runs the same code. Per-title behaviour lives only in `config/games/<titleId>.toml` under `[workarounds]`, where the key names the mechanism (never the game) and is registered in [docs/workarounds.md](docs/workarounds.md). The `policy` step of the hosted `build_and_test` CI job enforces both directions.
- **No behaviour-changing environment variables.** The `APS5_*` switches are removed. Tracing, dumps and profiling survive only as a typed `[debug]` config section.
- **General mechanisms over game-specific fixes.** A fix that happens to help one title first (e.g. a uniform-fill or linear-copy IR pattern, GPU-side resource resolution, general block-generation write tracking) is adopted; a branch on a title ID, executable hash or shader hash is not. If a title cannot progress without a hack, work stops and the root cause goes into the subsystem spec's Open questions.
- **Honest errors.** Real POSIX/SCE conditions return codes. Only genuinely unsupported states abort, through the logging abort path. Nothing throws across the `APS5_VABI` boundary; every host function reachable from guest code is `APS5_VABI` (System V ABI).
- **Concurrency without global locks.** Guest synchronization uses in-place futex words on `WaitOnAddress`, not heap `std::` mutexes and no process-global lock on hot paths.
- **GPU work resolved on the GPU.** Indirect draws, buffer resolves at submit time, and write tracking run on GPU-side paths — never by reading records back on the CPU or satisfying a wait from an unexecuted label a capture depends on.
- **Verification splits by machine.** Hosted CI (`build_and_test` with its unit, recompiler-golden and `policy` steps, `driver-lavapipe` on Mesa lavapipe, python-quality — full job list in [spec/verification.md](docs/spec/verification.md)) has no GPU and never needs game data. GPU runs are local-only on a maintainer machine with their own dumps, and the