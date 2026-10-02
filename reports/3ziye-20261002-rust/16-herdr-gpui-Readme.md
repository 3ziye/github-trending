<p align="center">
  <img src="assets/icons/herdr-ui-icon-badge.png" alt="Herdr ram on a simple ivory tile with a red notification badge showing 1" width="176" height="176">
</p>

<h1 align="center">Herdr GPUI</h1>

<p align="center">
  <a href="https://github.com/penso/herdr-gpui/actions/workflows/ci.yml"><img src="https://github.com/penso/herdr-gpui/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
</p>

<p align="center">
  <a href="https://github.com/penso/herdr-gpui/releases">Releases</a> ·
  <a href="docs/updating.md">App updates</a> ·
  <a href="crates/herdr-gpui/README.md">GUI scope &amp; configuration</a> ·
  <a href="crates/herdr-gpui/PERFORMANCE.md">Performance report</a> ·
  <a href="AGENTS.md">Contributing</a>
</p>

A native Rust/GPUI client for a [Herdr](https://herdr.dev/) daemon you installed
yourself. It paints the daemon's terminal cells, split panes included, without
running another terminal emulator or wrapping the TUI.

> **Unaffiliated project.** Not affiliated with, endorsed by, or supported by
> Herdr or [herdr.dev](https://herdr.dev/).

## Install

### macOS with Homebrew

Requires [Homebrew](https://brew.sh/) and macOS 15 Sequoia or newer, on Apple
Silicon or Intel. The cask installs the signed, notarized universal app.

```sh
brew install penso/tap/herdr-gpui
open -a Herdr
```

`brew install` resolves casks directly, so `--cask` is not required. To update it
later, or to install by its short name, tap once first:

```sh
brew tap penso/tap
brew install herdr-gpui
```

The cask is published from the [tap](https://github.com/penso/homebrew-tap) by the
release workflow. A cask install updates itself through Homebrew: the in-app
updater detects that Homebrew owns the bundle and runs `brew upgrade --cask
herdr-gpui` for you, so Homebrew's records stay correct. If its metadata is stale,
the updater runs `brew update` and retries once. The update panel shows progress
throughout. macOS `.dmg`, experimental Linux packages, and experimental Windows `.zip`s
are also published on [Releases](https://github.com/penso/herdr-gpui/releases).

### Linux packages

Each release publishes x86_64 and ARM64 builds as a `.deb`, an `.rpm`, an Arch
Linux package, and a plain tarball, all containing the same executable. They need
glibc 2.39 or newer (Ubuntu 24.04, Debian 13, Fedora 40, current Arch, or later).
Download the file for your architecture from
[Releases](https://github.com/penso/herdr-gpui/releases), then:

```sh
sudo apt install ./Herdr-VERSION-x86_64-unknown-linux-gnu.deb      # Debian, Ubuntu
sudo dnf install ./Herdr-VERSION-x86_64-unknown-linux-gnu.rpm      # Fedora
sudo pacman -U Herdr-VERSION-x86_64-unknown-linux-gnu.pkg.tar.zst  # Arch Linux
```

The package manager pulls in the runtime libraries, including the Vulkan loader;
a Vulkan driver for your GPU must also be present. Packages are not in any
distribution repository, so they never update themselves: install each new
release the same way. Before a release, CI installs each package on Ubuntu 24.04,
Debian 13 and Fedora 42, and the x86_64 Arch package on Arch Linux, then checks that
the executable finds every library. The ARM64 Arch package targets Arch Linux ARM
and is not install-tested.

On NixOS, or anywhere with Nix, build from source with the repository's flake:

```sh
nix run github:penso/herdr-gpui
# or add it to a configuration: inputs.herdr-gpui.url = "github:penso/herdr-gpui";
# then environment.systemPackages = [ inputs.herdr-gpui.packages.${system}.default ];
```

The flake builds with the toolchain pinned in `rust-toolchain.toml` on x86_64 and
ARM64 Linux. Like the packages, it never updates itself.

### From source

Install Rust/rustup and, on macOS, the Xcode command-line tools. The repository
pins Rust 1.96.1 and GPUI 0.3.6 (the `gpui-pre` snapshot crate); the Rust version
is declared in `rust-toolchain.toml` and mirrored in `mise.toml`, so `mise install`
also provisions it.

```sh
git clone https://github.com/penso/herdr-gpui.git
cd herdr-gpui
just run
```

`just run` uses the optimized release build with the QA menu enabled;
`just run-debug` is notably slower with a dense terminal on screen.
On macOS both build a local bundle identified as `so.pen.herdr-gpui.dev`, so
it never shares a Dock tile or icon cache with an installed release.
Without `just`: `cargo run --locked --release -p herdr-gpui --features qa-menu`.

Install the Herdr daemon separately. The app starts an already-installed local
`herdr server` when the target session is absent, but never installs or upgrades
a daemon. Explicitly confirming session deletion stops that named session first;
closing or removing the GUI leaves daemon sessions and shared Herdr
configuration intact.

### Linux Builds

On Ubuntu 24.04 (x86_64 or ARM64), run `bash scripts/install-linux-deps.sh`
before building. This installs GPUI's X11/Wayland/font development dependencies
and `libasound2-dev` for Rodio/CPAL native audio. CI and release builds use the
same script. Linux binaries 