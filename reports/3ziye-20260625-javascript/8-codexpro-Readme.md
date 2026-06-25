<p align="center">
  <img src="docs/favicon.svg" width="72" height="72" alt="CodexPro logo">
</p>

<h1 align="center">CodexPro</h1>

<p align="center">
  Use ChatGPT like your local coding agent for one token-protected workspace.
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/codexpro"><img alt="npm" src="https://img.shields.io/npm/v/codexpro?style=flat-square"></a>
  <a href="https://github.com/rebel0789/codexpro/actions"><img alt="CI" src="https://img.shields.io/github/actions/workflow/status/rebel0789/codexpro/ci.yml?branch=main&style=flat-square"></a>
  <a href="https://github.com/rebel0789/codexpro/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/github/license/rebel0789/codexpro?style=flat-square"></a>
  <a href="https://rebel0789.github.io/codexpro/"><img alt="Website" src="https://img.shields.io/badge/site-GitHub%20Pages-67e8f9?style=flat-square"></a>
</p>

<p align="center">
  <a href="https://rebel0789.github.io/codexpro/">Website</a>
  ·
  <a href="README_ZH.md">中文 README</a>
  ·
  <a href="https://rebel0789.github.io/codexpro/zh.html">中文网站</a>
  ·
  <a href="https://github.com/rebel0789/codexpro">Star on GitHub</a>
  ·
  <a href="https://www.npmjs.com/package/codexpro">npm</a>
  ·
  <a href="DOMAIN_SETUP.md">Stable URL guide</a>
  ·
  <a href="FAQ.md">FAQ</a>
  ·
  <a href="SECURITY.md">Security</a>
</p>

## Installation

CodexPro requires Node.js 20+ and a ChatGPT Plus or Pro account with Apps / Developer Mode access.

Install the CLI:

```bash
npm install -g codexpro
```

Then run setup inside the repo you want ChatGPT to work on:

```bash
cd /path/to/your/repo
codexpro setup
```

CodexPro copies the ChatGPT Server URL for you. In ChatGPT, open `Settings -> Apps -> Advanced settings -> Create app`, paste that URL, and choose `Authentication: No Authentication / None`.

After setup, daily use from the same repo is just:

```bash
codexpro start
```

CodexPro turns ChatGPT Developer Mode into a local coding agent for that folder. It gives ChatGPT bounded MCP tools for file reads, code search, exact edits, git inspection, safe verification commands, and explicit repo-backed context from `AGENTS.md`, `.ai-bridge`, git state, and selected source files.

CodexPro is not a rate-limit bypass, model proxy, hosted SaaS, or OS sandbox. It uses ChatGPT's official Developer Mode and MCP app path to connect your own ChatGPT session to your own local repo. ChatGPT and Codex remain separate product surfaces, each subject to its own plan limits, safety rules, and availability.

## Quick Choices

| Need | Use |
| --- | --- |
| Fast first setup | `npm install -g codexpro`, then `codexpro setup` |
| Daily start | `codexpro start` from the same repo |
| Stable ChatGPT URL | ngrok free dev domain or Cloudflare named tunnel |
| Smallest tool surface | default `CODEXPRO_TOOL_MODE=standard` |
| Full diagnostics | `codexpro start --tool-mode full` |
| No ChatGPT-triggered shell | `codexpro start --no-bash` |
| Compact chat transcript | default bash cards; use `--bash-transcript full` only when needed |
| Local Codex history lookup | opt in with `--codex-sessions metadata` or `read` |

## Product Boundary

| CodexPro is | CodexPro is not |
| --- | --- |
| A local MCP bridge for the workspace you choose | A hosted coding service |
| A way for ChatGPT Developer Mode to inspect, edit, verify, and hand off work | A model unlock, proxy, resale layer, or quota workaround |
| A repo-backed context system using explicit files such as `AGENTS.md` and `.ai-bridge` | Permanent ChatGPT memory across every chat |
| A developer tool with conservative defaults | An OS sandbox or substitute for repo/terminal judgment |

## Why CodexPro?

| ChatGPT gets | CodexPro provides |
| --- | --- |
| Repo context | `AGENTS.md`, `.ai-bridge`, git status, git diff, selected source files |
| Coding actions | `read`, `write`, `edit`, `search`, `show_changes` |
| Verification | safe `bash` for focused test, lint, build, and git commands |
| Handoff | `.ai-bridge/current-plan.md` for Codex, OpenCode, Pi, or a custom local agent |
| Fallback planning | `.ai-bridge/pro-context.md` for model surfaces that cannot call MCP tools |

If one workflow is unavailable and another product surface you already have access to is still available, CodexPro lets you keep working against the same local repo without modifying or evading either product's limits.

If your ChatGPT account exposes a stronger model in the web app, and that model/surface can call Developer Mode apps, CodexPro lets it work against your local repo through MCP. Some ChatGPT model surfaces may not be able to call connectors or MCP tools directly. CodexPro does not provide, proxy, resell, or unlock models; it gives compatible ChatGPT sessions local coding tools and repo context.

## CodexPro vs generic workspace bridges

The high-level shape can look similar because both use a local MCP bridge, a tunnel, and a workspace root. CodexPro is narrower and more opinionat