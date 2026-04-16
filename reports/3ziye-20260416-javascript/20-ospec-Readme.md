<h1><a href="https://ospec.ai/" target="_blank" rel="noopener noreferrer">OSpec.ai</a></h1>

<p align="center">
  <a href="https://www.npmjs.com/package/@clawplays/ospec-cli"><img src="https://img.shields.io/npm/v/%40clawplays%2Fospec-cli?style=for-the-badge&logo=npm&label=npm" alt="npm"></a>
  <a href="https://www.npmjs.com/package/@clawplays/ospec-cli"><img src="https://img.shields.io/npm/dm/%40clawplays%2Fospec-cli?style=for-the-badge&logo=npm&label=downloads&cacheSeconds=300" alt="npm downloads"></a>
  <a href="https://github.com/clawplays/ospec/stargazers"><img src="https://img.shields.io/github/stars/clawplays/ospec?style=for-the-badge&logo=github" alt="GitHub stars"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/clawplays/ospec?style=for-the-badge&color=green" alt="License"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Node.js-18%2B-339933?style=flat-square&logo=node.js&logoColor=white" alt="Node.js 18+">
  <img src="https://img.shields.io/badge/npm-8%2B-CB3837?style=flat-square&logo=npm&logoColor=white" alt="npm 8+">
  <img src="https://img.shields.io/badge/language-TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript">
  <img src="https://img.shields.io/badge/workflow-3_steps-0F766E?style=flat-square" alt="3-step workflow">
</p>

<p align="center">
  <strong>English</strong> |
  <a href="docs/README.zh-CN.md">中文</a> |
  <a href="docs/README.ja.md">日本語</a> |
  <a href="docs/README.ar.md">العربية</a>
</p>

The official OSpec CLI package is `@clawplays/ospec-cli`, and the official command is `ospec`. OSpec supports spec-driven development (SDD) and document-driven development for AI coding agents and CLI workflows.

<p align="center">
  <a href="docs/prompt-guide.md">Prompt Guide</a> |
  <a href="docs/usage.md">Usage</a> |
  <a href="docs/project-overview.md">Overview</a> |
  <a href="docs/installation.md">Installation</a> |
  <a href="docs/external-plugins.md">External Plugins</a> |
  <a href="docs/plugin-release.md">Plugin Release</a> |
  <a href="https://github.com/clawplays/ospec/issues">Issues</a>
</p>

## Why OSpec?

AI coding assistants are powerful, but requirements that live only in chat history are hard to inspect, review, and close out cleanly. OSpec adds a lightweight workflow layer so the repository can hold the change context before code is written and after the work ships.

- Align before code — keep proposal, tasks, state, verification, and review visible in the repo
- Keep each requirement explicit — the default path moves one requirement through one active change
- Stay lightweight — keep the normal flow short with `init -> change -> verify/finalize`
- Use the assistants you already have — OSpec is built for Codex, Claude Code, and direct CLI workflows

## Install With npm

```bash
npm install -g @clawplays/ospec-cli
```

Official package: `@clawplays/ospec-cli`  
Command: `ospec`  
Verify install: `ospec --help`

## Quick Start

OSpec only takes 3 steps:

1. initialize OSpec in your project directory
2. create and advance one change for a requirement, document update, or bug fix
3. archive the accepted change after deployment and validation are complete

### 1. Initialize OSpec In Your Project Directory

Recommended prompt:

```text
OSpec, initialize this project.
```

Claude / Codex skill mode:

```text
/ospec initialize this project.
```

<details>
<summary>Command line</summary>

```bash
ospec init .
ospec init . --summary "Internal admin portal for operations"
ospec init . --summary "Internal admin portal for operations" --tech-stack node,react,postgres
ospec init . --architecture "Single web app with API and shared auth" --document-language en-US
```

CLI notes:

- `--summary`: project overview text written into the generated docs
- `--tech-stack`: comma-separated stack list such as `node,react,postgres`
- `--architecture`: short architecture description
- `--document-language`: generated doc language, choose from `en-US`, `zh-CN`, `ja-JP`, or `ar`
- AI-first language resolution order: explicit language request in the conversation -> current conversation language -> persisted project language in `.skillrc`
- CLI language resolution order: explicit `--document-language` -> persisted project language in `.skillrc` -> existing project docs / managed `for-ai/*` guidance / asset manifest -> fallback `en-US`
- OSpec persists the chosen project document language in `.skillrc` and reuses it for `for-ai` guidance, `ospec new`, and `ospec update`
- new projects initialized by `ospec init` default to the nested layout: root `.skillrc` and `README.md`, with OSpec-managed files under `.ospec/`
- plain init does not create optional knowledge maps such as `.ospec/knowledge/src/` or `.ospec/knowledge/tests/`; those appear only when a project already has legacy knowledge content to migrate or when future explicit knowledge-generation flows create them
- CLI commands still accept shorthand like `changes/active/<ch