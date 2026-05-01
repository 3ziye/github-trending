# thClaws 🦞

> **Open-source Agent Harness Platform** — a native AI agent workspace that codes, automates, remembers, and coordinates. Runs on your own machine. Sovereign by design.

thClaws is a **native-Rust AI agent workspace** that runs locally on your machine. Not just coding — it edits code, automates workflows, searches your knowledge bases, and coordinates teams of agents, all in one binary. You tell it what you want in natural language; it reads your files, runs commands, uses tools, and talks back to you while it works.

[![License: MIT OR Apache-2.0](https://img.shields.io/badge/license-MIT%20OR%20Apache--2.0-blue.svg)](#license)
[![Platform: macOS · Windows · Linux](https://img.shields.io/badge/platform-macOS%20·%20Windows%20·%20Linux-lightgrey.svg)](#installation)
[![Built with Rust](https://img.shields.io/badge/built%20with-Rust-orange.svg)](https://www.rust-lang.org/)

---

## See it work

Three tabs, one binary — captured from a live thClaws session looking at its own source.

<table>
  <tr>
    <td width="33%" align="center">
      <a href="docs/img/screen-files.webp"><img src="docs/img/screen-files.webp" alt="thClaws Files tab — landing-page source open in the editor with file tree" /></a><br/>
      <strong>Files</strong><br/>
      <sub>preview · edit · browse — codemirror + tiptap</sub>
    </td>
    <td width="33%" align="center">
      <a href="docs/img/screen-terminal.webp"><img src="docs/img/screen-terminal.webp" alt="thClaws Terminal tab — REPL session with ASCII banner" /></a><br/>
      <strong>Terminal</strong><br/>
      <sub>raw REPL · slash commands · ANSI tool output</sub>
    </td>
    <td width="33%" align="center">
      <a href="docs/img/screen-chat.webp"><img src="docs/img/screen-chat.webp" alt="thClaws Chat tab — conversational interface answering a product question" /></a><br/>
      <strong>Chat</strong><br/>
      <sub>conversational · markdown render · tool indicators</sub>
    </td>
  </tr>
</table>

---

## Three interfaces, one binary

- **Desktop GUI** (`thclaws`) — a native window with Terminal, Chat, Files, and optional Team tabs.
- **CLI REPL** (`thclaws --cli`) — an interactive terminal prompt for SSH, headless servers, or when you want zero GUI overhead.
- **Non-interactive mode** (`thclaws -p "prompt"`) — runs a single turn and exits. Handy for scripts, CI pipelines, and shell one-liners.

---

## What makes it different

- **Multi-provider.** Anthropic, OpenAI, Gemini, Alibaba DashScope, OpenRouter, Ollama (local and Anthropic-compatible), Agentic Press, plus a generic **OpenAI-compatible** slot (`oai/*`) for LiteLLM / Portkey / Helicone / vLLM / internal proxies — auto-detected by model name prefix. Switch mid-session with `/model` or swap the whole provider with `/provider`.

- **Any knowledge worker, not just engineers.** Chat tab for researchers, PMs, ops, legal, marketing, finance — natural-language prompts, file access, knowledge-base lookup, drafting. Terminal tab for engineers who want the raw REPL. Same engine, same sessions, same config — different preferred surface.

- **Open standards, not a walled garden.** Built on the conventions the agent-tooling industry is converging on, not bespoke formats you have to learn only for us. [Model Context Protocol](https://modelcontextprotocol.io/) for tool servers. [`AGENTS.md`](https://agents.md) for project instructions — the vendor-neutral standard adopted by Google, OpenAI, Factory, Sourcegraph, and Cursor. `SKILL.md` with YAML frontmatter for packaged workflows. Your configuration is portable between thClaws, other agents that speak the same standards, and whatever comes next.

- **Skills.** Reusable expert workflows packaged as a directory with `SKILL.md` plus optional scripts. The agent picks the right skill automatically when a request matches the `whenToUse` trigger, or you can invoke one explicitly as `/<skill-name>`. Install from a git URL or `.zip` archive with `/skill install`.

- **MCP servers.** Plug in tools built by third parties — GitHub, filesystems, databases, browsers, Slack, and more. Both stdio and HTTP Streamable transports, with OAuth 2.1 + PKCE for protected servers. Add one with `/mcp add` or ship a `.mcp.json` in your project.

- **Plugin system.** Skills + commands + agent definitions + MCP servers bundled under a single manifest, installable from git or `.zip`. One install, one uninstall, one version to pin — ideal for sharing a team's extensions.

- **Memory & project instructions.** Drop an `AGENTS.md` (or `CLAUDE.md`) in your repo — thClaws walks up from `cwd` and injects every match into the system prompt. A persistent memory store holds longer-lived facts the agent has learned about you, classified as `user` / `feedback` / `project` / `reference` and stored as markdown you can read, edit, or commit.

- **Knowledge bases (KMS).** Per-project and per-user wikis the agent can search and read on demand. Drop markdown pages under `.thclaws/kms/<name>/pages/`, give each a one-