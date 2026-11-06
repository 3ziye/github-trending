<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/brand/fire/header-dark.webp">
    <img alt="blaze" src="docs/brand/fire/header-light.webp" width="344" height="184">
  </picture>
</p>

<h3 align="center">Rebuild Rust in milliseconds.</h3>

<p align="center">Type <code>blaze</code> wherever you'd type <code>cargo</code>.<br>Blazingly fast Rust, literally.</p>

<p align="center">
  <a href="#install">Install</a> ·
  <a href="#try-it">Try it</a> ·
  <a href="#how-fast">How fast</a> ·
  <a href="#how-it-works">How it works</a> ·
  <a href="#learn-more">Docs</a>
</p>

## Install

```sh
curl -fsSL https://ix.dev/blaze | sh
```

For macOS on Apple silicon and Linux, with or without Rust installed: blaze builds with its own
Rust, whatever rustup or the project pins, and the installer downloads it once (about 125 to
160 MB; none when rustup already has that same nightly; v2's blaze cannot fetch it yet:
[toolchain.md](docs/toolchain.md)). Rather use crates.io or Nix?
[Other ways to install](docs/install.md).

That installs **stable**: a release that passed the heavy tests (real projects on macOS and
Linux: cargo, zed, servo, bun, NVIDIA Dynamo, fff, fframes, flox and OpenAI's Codex CLI each
build, build again after an edit faster than with cargo, and pass their tests). **Canary** is the
newest release, out as soon as it is built and promoted to stable unchanged once it passes them ([release.md](docs/release.md)):

```sh
curl -fsSL https://ix.dev/blaze | sh -s -- --channel canary
```

## Try it

In any Rust project:

```text
blaze run     # like cargo run
blaze test    # like cargo test
blaze build   # like cargo build
```

The first build loads your project and compiles every crate of it, with no cargo build and no
rustc. Then change a function and build again: blaze's daemon, still running, builds only what
the edit changed. blaze answers `build`, `check`, `run`, `test` and `bench`; other cargo
commands are not blaze's yet.

## How fast

These numbers are blaze v1's; v2 has not been measured yet.

- Edits rebuild <!-- benchheadline:start -->**10× faster** on macOS arm64, **24× faster** on Linux aarch64 and **11× faster** on Linux x86-64<!-- benchheadline:end --> than with `cargo build`, on average over real projects.
- **About 20 ms** from saving a file to a running program using the new code, with
  [live edits](docs/usage.md#change-a-running-program).

<!-- benchpick:start -->
| Edit one function, then build (Linux x86-64) | `cargo build` | `blaze build` |
|---|---:|---:|
| ripgrep | 508 ms | **56 ms** (9.1× faster) |
| nushell | 1.25 s | **236 ms** (5.3× faster) |
| helix | 2.15 s | **116 ms** (19× faster) |
| bun (1.25M lines of Rust) | 9.11 s | **451 ms** (20× faster) |
<!-- benchpick:end -->

Every project, platform, chart, and the memory and disk it takes: [benchmarks](docs/benchmarks.md).

### Over time

<!-- benchtrend:start -->
How blaze's own numbers move from run to run, each platform on its own benchmark machine: the instructions each merge to main retires, how long an edit takes and how soon a live edit runs, from [the history](docs/benchmarks/history) ([how it is kept](docs/benchmarks.md#history-and-regressions)). Every workflow that adds to the history draws these again and commits them with it.

<picture><source media="(prefers-color-scheme: dark)" srcset="docs/benchmarks/charts/trend-macos-arm64-live-dark.svg"><img alt="From saving an edit to the program running it, macOS arm64: 11 runs from Oct 21 to Oct 30, the first to the latest: bevy 83 ms to 3.79 s; egui 15 ms to 219 ms; life 22 ms to 34 ms (Oct 26); probe 7.7 ms to 14 ms" src="docs/benchmarks/charts/trend-macos-arm64-live-light.svg" width="760"></picture>

Not drawn until there are two runs on one machine: macOS arm64 instructions per merge (none yet), macOS arm64 edit times (one run), Linux aarch64 instructions per merge (none yet), Linux aarch64 edit times (one run), Linux x86-64 instructions per merge (none yet), Linux x86-64 edit times (one run), Windows x86-64 live-edit latency (one run).
<!-- benchtrend:end -->

## How it works

blaze's daemon keeps your project compiled in memory, with no cargo or rustc under it. After an
edit it compiles only the functions you changed and links the program again with its own linker.
[More](docs/v2/plan.md).

## Good to know

- **macOS on Apple silicon and Linux.** Windows has no installer, and v2 has not been run there
  ([v1 on Windows](docs/platforms.md#windows-x86-64-msvc)).
- **blaze is its own toolchain.** It builds every project with its own Rust, `blaze-2026-10-27`
  (today the nightly of that date), whatever the project pins; stable code and
  `#![feature(...)]` code build. Your toolchain and CI stay the final word
  ([why](docs/toolchain.md)).
- **It trades memory for speed:** a few GB for a small project.
- **It's young.** Keep `cargo check` or your CI as the final word, and
  [tell us](https://github.com/indexable-inc/blaze/issues) when something