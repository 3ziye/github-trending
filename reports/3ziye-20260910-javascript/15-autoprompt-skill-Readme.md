<p align="center">
  <img src="assets/banner.svg" alt="Autoprompt Skill: pink clouds and flying geese" width="1000"/>
</p>

<p align="center">Autoprompt is a coding-agent workflow that cuts failures by 45% by reviewing, fixing, and rechecking its work.</p>

<p align="center">
  <a href="#benchmarks"><img src="https://img.shields.io/badge/Terminal--Bench%202.1-%2B14.61%20points-965477?style=flat-square&labelColor=302335" alt="Terminal-Bench 2.1: plus 14.61 points"/></a>
  <a href="https://github.com/Spielewoy/autoprompt-skill/releases/latest"><img src="https://img.shields.io/github/v/release/Spielewoy/autoprompt-skill?style=flat-square&label=version&color=965477&labelColor=302335" alt="Latest release"/></a>
  <a href="#install"><img src="https://img.shields.io/badge/support-11%20supported%20providers-965477?style=flat-square&labelColor=302335" alt="Eleven supported providers"/></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-965477?style=flat-square&labelColor=302335" alt="License MIT"/></a>
</p>

<p align="center">
  <a href="README.md"><b>English</b></a> |
  <a href="docs/translations/zh.md">中文</a> |
  <a href="docs/translations/ko.md">한국어</a> |
  <a href="docs/translations/es.md">Español</a> |
  <a href="docs/translations/ar.md">العربية</a>
</p>

## Contents

[Install](#install) · [Benchmarks](#benchmarks) · [Invocation](#anatomy-of-an-invocation) · [Run controls](#run-controls) · [Workflow](#how-it-works) · [Agents](#the-agents) · [Examples](#examples) · [FAQ](#faq) · [License](#license)

## Install

Use the CLI below, or download an installer from [GitHub Releases](https://github.com/Spielewoy/autoprompt-skill/releases/latest).

### 1. Install the CLI

```bash
npm install -g https://github.com/Spielewoy/autoprompt-skill/releases/download/v2.0.0/autoprompt-skill-2.0.0.tgz
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
- [Python 3.11+](https://www.python.org/downloads/) available as `python3` or `python`, with [PyYAML](https://pypi.org/project/PyYAML/)
- [Bash 4.3+](https://www.gnu.org/software/bash/) on macOS or Linux
- [Git](https://git-scm.com/downloads) only for the GitHub checkout method

### Support

| Status | Coding agent | Tested version | Key |
|---|---|---|---|
| Working | [Claude Code](https://code.claude.com/docs/en/setup) | 2.1.263 | `claude` |
| Working | [Codex](https://github.com/openai/codex) | 0.148.0 | `codex` |
| Working | [OpenCode](https://opencode.ai/docs/agents) | 1.18.29 | `opencode` |
| Working | [Kilo Code](https://kilo.ai/docs/customize/custom-subagents) | 7.5.15 | `kilo` |
| Working | [VS Code](https://code.visualstudio.com/docs/agents/subagents) | 1.136.1 | `vscode` |
| Working | [Prime Agent](https://github.com/PrimeIntellect-ai/prime-agent) | 0.7.2 | `prime` |
| Working | [Oh My Pi](https://omp.sh/) | 18.1.14 | `omp` |
| Working | [DeepSeek Harness](https://deepseek.com/harness/en/) | 0.1.2-rc.1 | `deepseek` |
| Working | [Reasonix](https://reasonix.io/docs/) | 1.30.0 | `reasonix` |
| Working | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | 0.21.1 | `hermes` |
| Working | [Grok Build](https://docs.x.ai/build/overview) | 1.0.13 | `grok` |

These versions passed Linux runs. Model and platform availability varies by provider.

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

These are **version 1 benchmarks**. Version 2 benchmarks will follow.

<p align="center">
  <img src="assets/terminal-bench-2.1-leaderboard.svg" width="1000" alt="Terminal-Bench 2.1 leaderboard with 18 Artificial Analysis reference scores and measured DeepSeek V4 Flash 0731 scores with and without Autoprompt."/>
</p>

<details>
<summary><strong>Measured OpenCode comparison</strong></summary>

<p align="center">
  <img src="assets/terminal-bench-2.1.svg" width="900" alt="OpenCode 1.18.7 on Terminal-Bench 2.1: OpenCode solved 60 of 89 tasks and OpenCode with Autoprompt solved 73 of 89 tasks."/>
</p>

| Track | Solved | Score | Failed |
|---|---:|--