<p align="center">
  <img src="assets/banner.svg" alt="Autoprompt Skill with 45% fewer failures on agentic coding tasks" width="760"/>
</p>

<p align="center">Autoprompt is a coding-agent skill that cuts failures by 45% on agentic coding tasks.</p>

<p align="center">
  <a href="#benchmarks"><img src="https://img.shields.io/badge/Terminal--Bench%202.1-%2B14.61%20points-255C60?style=flat-square&labelColor=14101F" alt="Terminal-Bench 2.1: plus 14.61 points"/></a>
  <a href="https://github.com/Spielewoy/autoprompt-skill/releases/latest"><img src="https://img.shields.io/github/v/release/Spielewoy/autoprompt-skill?style=flat-square&label=version&color=255C60&labelColor=14101F" alt="Version 1.0.4"/></a>
  <a href="#install"><img src="https://img.shields.io/badge/support-9%20supported%20providers-255C60?style=flat-square&labelColor=14101F" alt="Nine supported providers"/></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-255C60?style=flat-square&labelColor=14101F" alt="License MIT"/></a>
</p>

<p align="center">
  <a href="README.md"><b>English</b></a> |
  <a href="https://github.com/Spielewoy/autoprompt-skill/blob/main/docs/translations/zh.md">中文</a> |
  <a href="https://github.com/Spielewoy/autoprompt-skill/blob/main/docs/translations/ko.md">한국어</a> |
  <a href="https://github.com/Spielewoy/autoprompt-skill/blob/main/docs/translations/es.md">Español</a> |
  <a href="https://github.com/Spielewoy/autoprompt-skill/blob/main/docs/translations/ar.md">العربية</a>
</p>

## Contents

[Install](#install) · [Benchmarks](#benchmarks) · [Invocation](#anatomy-of-an-invocation) · [Run controls](#run-controls) · [Workflow](#how-it-works) · [Agents](#the-agents) · [Examples](#examples) · [FAQ](#faq) · [License](#license)

## Install

Use the CLI below, or download an installer from [GitHub Releases](https://github.com/Spielewoy/autoprompt-skill/releases/tag/v1.0.4).

### 1. Install the CLI

```bash
npm install -g autoprompt-skill
```

### 2. Launch the installer

```bash
autoprompt
```

### 3. Install

Choose your coding agent, confirm its path, and install. `N` means enter another path.

For another CLI or IDE, choose `Custom coding agent` and use the [compatibility guide](docs/guides/custom-agent-compatibility.md).

<details>
<summary><strong>Install from source</strong></summary>

```bash
git clone https://github.com/Spielewoy/autoprompt-skill
cd autoprompt-skill
npm install -g .
autoprompt
```

</details>

### Requirements

- [Node.js 20+](https://nodejs.org/en/download)
- [Python 3.11+](https://www.python.org/downloads/) exposed as `python`, with [PyYAML](https://pypi.org/project/PyYAML/)
- [Bash 4.3+](https://www.gnu.org/software/bash/) on macOS or Linux
- [Git](https://git-scm.com/downloads) only for the GitHub checkout method

### Support

| Status | Coding agent | Audited requirement | Key |
|---|---|---|---|
| Working | [Claude Code](https://code.claude.com/docs/en/setup) | 2.1.219+; audited 2.1.233 | `claude` |
| Working | [Codex](https://github.com/openai/codex) | Subagent-capable build; audited 0.147.0 | `codex` |
| Working | [OpenCode](https://opencode.ai/docs/agents) | 1.18.7+; audited 1.18.18 | `opencode` |
| Working | [Kilo Code](https://kilo.ai/docs/customize/custom-subagents) | 7.4.22+; audited 7.4.22 | `kilo` |
| Working | [VS Code](https://code.visualstudio.com/docs/agents/subagents) | 1.133+; audited 1.133.0 with Copilot 0.61.0 | `vscode` |
| Working | [Prime Agent](https://github.com/PrimeIntellect-ai/prime-agent) | 0.7.2; audited 0.7.2; native package adapter | `prime` |
| Working | [Oh My Pi](https://omp.sh/) | 17.4.0+; adapter contract, install lifecycle, and native role payload verified for 17.4.0 | `omp` |
| Working | [DeepSeek Harness](https://deepseek.com/harness/en/) | 0.1.0-rc.7+; adapter contract, install lifecycle, and native role payload verified for 0.1.0-rc.7 | `deepseek` |
| Working | [Reasonix](https://reasonix.io/docs/) | 1.30.0+; adapter contract, install lifecycle, and native role payload verified for 1.30.0 | `reasonix` |

See [support and audit notes](docs/faq/which-coding-agents-are-supported.md).

### Check, update, or remove an installation

- Check every detected installation: `autoprompt doctor --strict`
- Check one provider: `autoprompt doctor PROVIDER --strict`
- Update or repair: `autoprompt`, then choose an installed provider
- Uninstall interactively: `autoprompt uninstall`
- Uninstall one provider: `autoprompt uninstall PROVIDER`
- Show every command: `autoprompt help`

Replace `PROVIDER` with a key from the support table, such as `claude`, `codex`, or `prime`.

## Benchmarks

<p align="center">
  <img src="assets/terminal-bench-2.1-leaderboard.svg" width="1000" alt="Terminal-Bench 2.1 leaderboard with 18 Artificial Analysis reference scores and measured DeepSeek V4 Flash 0731 scores with and without Autoprompt."/>
</p>

<details>
<summary><strong>Measured OpenCode comparison</strong></summary>

<p align="center">
  <img src="assets/terminal-bench-2