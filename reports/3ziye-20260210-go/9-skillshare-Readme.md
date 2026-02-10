<p align="center" style="margin-bottom: 0;">
  <img src=".github/assets/logo.png" alt="skillshare" width="280">
</p>

<h1 align="center" style="margin-top: 0.5rem; margin-bottom: 0.5rem;">skillshare</h1>

<p align="center">
  <a href="https://skillshare.runkids.cc"><img src="https://img.shields.io/badge/Website-skillshare.runkids.cc-blue?logo=docusaurus" alt="Website"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="go.mod"><img src="https://img.shields.io/github/go-mod/go-version/runkids/skillshare" alt="Go Version"></a>
  <a href="https://github.com/runkids/skillshare/releases"><img src="https://img.shields.io/github/v/release/runkids/skillshare" alt="Release"></a>
  <img src="https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-blue" alt="Platform">
  <a href="https://goreportcard.com/report/github.com/runkids/skillshare"><img src="https://goreportcard.com/badge/github.com/runkids/skillshare" alt="Go Report Card"></a>
  <a href="https://deepwiki.com/runkids/skillshare"><img src="https://deepwiki.com/badge.svg" alt="Ask DeepWiki"></a>
</p>

<p align="center">
  <a href="https://github.com/runkids/skillshare/stargazers"><img src="https://img.shields.io/github/stars/runkids/skillshare?style=social" alt="Star on GitHub"></a>
</p>

<p align="center">
  <strong>One source of truth for AI CLI skills. Sync everywhere with one command — from personal to organization-wide.</strong><br>
  Claude Code, OpenClaw, OpenCode & 40+ more.
</p>

<p align="center">
  <img src=".github/assets/demo.gif" alt="skillshare demo" width="960">
</p>

<p align="center">
  <a href="https://skillshare.runkids.cc">Website</a> •
  <a href="#installation">Install</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="#cli-and-ui-preview">Screenshots</a> •
  <a href="#common-workflows">Commands</a> •
  <a href="#web-dashboard">Web UI</a> •
  <a href="#project-skills-per-repo">Project Skills</a> •
  <a href="#organization-skills-tracked-repo">Organization Skills</a> •
  <a href="https://skillshare.runkids.cc/docs">Docs</a>
</p>

> [!NOTE]
> **Recent Updates**
> | Version | Highlights |
> |---------|------------|
> | [0.11.0](https://github.com/runkids/skillshare/releases/tag/v0.11.0) | Security Audit, Operation Log, Trash, Update Preview — full audit trail + safety net |
> | [0.10.0](https://github.com/runkids/skillshare/releases/tag/v0.10.0) | Web Dashboard — visual skill management via `skillshare ui` |
> | [0.9.0](https://github.com/runkids/skillshare/releases/tag/v0.9.0) | Project-level skills — scope skills to a single repo, share via git |

## Why skillshare

Stop managing skills tool-by-tool.
`skillshare` gives you one shared skill source and pushes it everywhere your AI agents work.

- **One command, everywhere**: Sync to Claude Code, Codex, Cursor, OpenCode, and more with `skillshare sync`.
- **Safe by default**: Non-destructive merge mode keeps CLI-local skills intact while sharing team skills.
- **True bidirectional flow**: Pull skills back from targets with `collect` so improvements never get trapped in one tool.
- **Cross-machine ready**: Git-native `push`/`pull` keeps all your devices aligned.
- **Team + project friendly**: Use global skills for personal workflows and `.skillshare/` for repo-scoped collaboration.
- **Privacy-first**: No central registry, no telemetry, no install tracking. Your skill setup stays entirely local.
- **Built-in security audit**: Scan skills for prompt injection, data exfiltration, and other threats before they reach your AI agent.
- **Visual control panel**: Open `skillshare ui` for browsing, install, target management, and sync status in one place.

## Comparison

skillshare uses a **declarative** approach: define your targets once in `config.yaml`, then `sync` handles everything — no prompts, no repeated selections.

| | Imperative (install-per-command) | Declarative (skillshare) |
|---|---|---|
| **Config** | No config; prompts every run | `config.yaml` — set once |
| **Agent selection** | Interactive prompt each time | Defined in config |
| **Install method** | Choose per operation | `sync_mode` in config |
| **Source of truth** | Skills copied independently | Single source → symlinks |
| **Remove one agent's skill** | May break other agents' symlinks | Only that target's symlink removed |
| **New machine setup** | Re-run every install manually | `git clone` config + `sync` |
| **Project-scoped skills** | Global lock file only | `init -p` for per-repo skills |
| **Cross-machine sync** | Manual | Built-in `push` / `pull` |
| **Bidirectional** | Install only | `collect` pulls changes back |
| **Security audit** | None | Built-in `audit` + auto-scan on install |
| **Web dashboard** | None | `skillshare ui` |
| **Runtime dependency** | Node.js + npm | None (single Go binary) |

> [!TIP]
> Coming from another tool? See the [Migration Guide](https://skillshare.runkids.cc/docs/guides/migration) and [det