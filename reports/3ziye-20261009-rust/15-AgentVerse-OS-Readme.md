<p align="center">
  <img src="assets/shots/banner.webp" alt="AgentVerse OS — One system. Many worlds." width="100%">
</p>

<p align="center">
  <a href="#quick-start"><img alt="Ubuntu 22.04+" src="https://img.shields.io/badge/Ubuntu-22.04%2B-E95420?logo=ubuntu&logoColor=white"></a>
  <a href="cloudd/"><img alt="Rust" src="https://img.shields.io/badge/core-Rust-DEA584?logo=rust&logoColor=black"></a>
  <a href="desktop/"><img alt="Svelte 5" src="https://img.shields.io/badge/desktop-Svelte%205-FF3E00?logo=svelte&logoColor=white"></a>
  <a href="store/"><img alt="945 apps" src="https://img.shields.io/badge/store-945%20apps-5B8CFF"></a>
  <a href="LICENSE"><img alt="Apache-2.0" src="https://img.shields.io/badge/license-Apache--2.0-blue"></a>
  <img alt="status" src="https://img.shields.io/badge/status-alpha%200.2-7A5CFF">
</p>

**AgentVerse OS** is a personal cloud operating system for a developer and their AI agents: your own cloud running on a single server,
used from any device through the browser. It is built as a cross-platform vibe coding flow: the same desktop, workspaces and agents
open on a laptop, a tablet or a phone, the workspace and its agents stay on the server, and the work continues where you left it.
One command installs it on a clean Ubuntu; everything after that happens in the browser: a windowed desktop, isolated workspaces with
VS Code and agents (Claude Code, Codex, Gemini CLI, pi), a store of 945 self-hosted apps, backups and updates. Nothing is exposed to the internet:
access goes through Tailscale with real certificates, no root CAs to install on your devices.

> The project is in alpha and lives on a single test box. It works as a personal server for one person; there are no user accounts or
> permissions yet. See [Status](#status) for what is done and what is not.

## What it looks like

<p align="center">
  <img src="assets/shots/desktop-dark.webp" alt="Desktop: Store, the alpha project card with its workspace and capabilities, monitor and news widgets" width="100%">
</p>
<p align="center"><sub>Desktop on a computer: the Store catalog, a project card with its workspace and capabilities, widgets. Monolith theme, glass surfaces.</sub></p>

<table>
  <tr>
    <td width="50%" valign="top">
      <img src="assets/shots/desktop-light.webp" alt="Light theme: Projects window and Settings with theme presets">
      <p align="center"><sub>Light theme: projects and appearance settings. Seven presets, including OLED and high contrast.</sub></p>
    </td>
    <td width="50%" valign="top">
      <img src="assets/shots/tablet-dark.webp" alt="Tablet: icons, widgets and the Store window">
      <p align="center"><sub>Tablet: the same windows and widgets, portrait wallpaper.</sub></p>
    </td>
  </tr>
</table>

<p align="center">
  <img src="assets/shots/phone.webp" alt="Phone: home screen with apps and projects, the Store window" width="70%">
</p>
<p align="center"><sub>Phone: a home screen instead of a desktop, full-screen windows, PWA. One Desktop adapts to the device.</sub></p>

<p align="center">
  <img src="assets/shots/agents-code.webp" alt="The Agents app: Code view with session cards for Claude Code, Codex, Gemini CLI and pi, a permission request waiting in the middle card, the inspector on the right" width="100%">
</p>
<p align="center"><sub>The Agents app on a wide screen: Code view with session cards for Claude Code, Codex, Gemini CLI and pi, a permission request waiting for a decision, the inspector. Demo data.</sub></p>

## What it does

- **Projects and workspaces.** Every project gets its own network, its own gate and an isolated Incus container with Docker inside.
  Inside: VS Code in the browser, a terminal and agents; Claude Code and Codex log in with your subscriptions. Stop/start keeps the
  instance, resources are changed from the project card.
- **Agents.** A separate app for working with coding agents from any device: Claude Code, Codex, Gemini CLI and pi run inside the
  project's workspace, the conversation lives on the server and continues on the phone where the laptop left off. Tool calls and
  permission prompts, a terminal, the files and git of the workspace, model menus (including the models of the project's LLM gate),
  routines on a schedule, a ledger of spend, search and export of conversations, MCP servers and skills, diagrams and formulas in
  replies, and a simple chat straight to a model without a container. Conversations survive a restart of the daemon in the workspace.
- **A Store of 945 apps.** The Runtipi, Coolify and Umbrel catalogs merged into one, with source badges. Guided install, login
  credentials right in the card, logs, automatic repair of data-directory permissions, links between apps (e.g. n8n → LiteLLM),
  per-app snapshots and rollback.
- **Capabilities instead of addresses.** A project asks for `storage.s3`, `llm` or `notify`; the core connects the project's gate to
  the provider's network and drops environment variables into the workspace. Sw