# Personal Model: local-first AI memory for coding agents

<p align="center">
  <a href="https://github.com/Intuition-Lab/personal-model/releases/tag/v0.3.2">
    <img src="docs/assets/readme/demo-preview.gif" alt="Looping 10-second preview of the Personal Model viewer orbiting an evidence-linked model" width="100%">
  </a>
</p>
<p align="center">
  <sub>Auto-playing preview · <a href="https://github.com/Intuition-Lab/personal-model/releases/tag/v0.3.2">Full-quality demo and v0.3.2 release notes</a></sub>
</p>

<!-- mcp-name: io.github.Intuition-Lab/personal-model -->

![Build your HUMAN.md — local-first AI memory for Claude Code, Codex, and MCP](docs/assets/readme/human-md-hero.png)

Build your `HUMAN.md` — one evidence-linked Personal Model for Claude Code, Codex, Cursor Agent, and other trusted MCP clients.

Personal Model is an open-source, local-first long-term memory Runtime. It learns how you think and work from focused activity captured on your Mac after you grant macOS permission, then gives your AI tools inspectable context to continue work and make grounded decisions.

**Runs locally on your Mac. Private by default. Yours to inspect, correct, export, and delete.**

[![CI](https://github.com/Intuition-Lab/personal-model/actions/workflows/ci.yml/badge.svg)](https://github.com/Intuition-Lab/personal-model/actions/workflows/ci.yml) [![Release](https://img.shields.io/github/v/release/Intuition-Lab/personal-model)](https://github.com/Intuition-Lab/personal-model/releases) [![GitHub stars](https://img.shields.io/github/stars/Intuition-Lab/personal-model?style=flat&logo=github&label=Stars)](https://github.com/Intuition-Lab/personal-model) [![License: Apache-2.0](https://img.shields.io/badge/code-Apache--2.0-blue)](LICENSE) [![macOS 13+](https://img.shields.io/badge/macOS-13%2B-black)](#1-install-with-your-data) [![MCP](https://img.shields.io/badge/interface-MCP-0b7285)](MCP.md) [![Official MCP Registry](https://img.shields.io/badge/Official_MCP_Registry-Personal_Model-6f42c1)](https://registry.modelcontextprotocol.io/?q=personal-model)

[Install Personal Model](#1-install-with-your-data) · [Connect your AI tool](#works-with-claude-code-codex-cursor-agent-and-mcp-clients) · [Star Personal Model on GitHub](https://github.com/Intuition-Lab/personal-model)

![Illustration of a mature Personal Model with evidence-linked Points, Lines, Faces, Volumes, and a Root](docs/assets/readme/personal-model.png)

_Concept illustration of a mature Personal Model._

---

## Why Personal Model

Personal Model turns focused activity from the apps you use into a portable context layer, keeps it on your Mac, and makes it available to the trusted AI clients you choose.

- **One memory across agents.** Connect the same Personal Model to Claude Code,
  Codex, Cursor Agent, and other MCP-compatible clients.
- **Evidence, not hidden summaries.** Important claims retain source receipts;
  new evidence can strengthen, revise, or overturn an earlier inference.
- **User-owned by design.** Inspect, correct, export, or delete your model and
  data without depending on a hosted memory service.
- **More than chat history.** Personal Model learns from focused activity after you
  explicitly grant macOS permissions.

### Your Personal Model is your `HUMAN.md`

Personal Model connects activity into progressively deeper context:

| Layer | Meaning |
| --- | --- |
| **Point** | A sourced observation or event |
| **Line** | A relationship or change over time |
| **Face** | A pattern supported by related evidence |
| **Volume** | A higher-order structure across projects or areas of life |
| **Root** | The current integrated model of you |

The result is a living model of what matters now, how you tend to decide, and
where your attention is moving.

## Works with Claude Code, Codex, Cursor Agent, and MCP clients

| Client | Connection | Setup |
| --- | --- | --- |
| [Claude Code](docs/mcp-clients.md#claude-code) | Native Personal Model installer | `persome install claude-code` |
| [Codex CLI and IDE extension](docs/mcp-clients.md#codex-cli-and-ide-extension) | Native Personal Model installer | `persome install codex` |
| [Cursor Agent CLI](docs/mcp-clients.md#cursor-agent-cli) | Native Personal Model installer | `persome install cursor-agent` |
| [Claude Desktop](docs/mcp-clients.md#claude-desktop) | Managed stdio config | `persome install claude-desktop` |
| [opencode](docs/mcp-clients.md#opencode) | Managed local stdio config | `persome install opencode` |
| [Other compatible clients](docs/mcp-clients.md#generic-clients) | Generated MCP JSON | `persome install mcp-json --filename persome-mcp.json` |

The [MCP client guide](docs/mcp-clients.md) covers prerequisites, verification,
the permission boundary, transport details, HTTP fallback, and troubleshooting.

> Personal Model is an MCP server used by trusted MCP clients. Other MCP servers—such
> as Filesystem, GitHub, Slack, or Google Drive—are separate tools and are not
> Personal Model integrat