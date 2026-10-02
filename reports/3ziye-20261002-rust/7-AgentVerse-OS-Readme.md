<p align="center">
  <img src="assets/shots/banner.webp" alt="AgentVerse OS — One system. Many worlds." width="100%">
</p>

<p align="center">
  <a href="#quick-start"><img alt="Ubuntu 22.04+" src="https://img.shields.io/badge/Ubuntu-22.04%2B-E95420?logo=ubuntu&logoColor=white"></a>
  <a href="cloudd/"><img alt="Rust" src="https://img.shields.io/badge/core-Rust-DEA584?logo=rust&logoColor=black"></a>
  <a href="desktop/"><img alt="Svelte 5" src="https://img.shields.io/badge/desktop-Svelte%205-FF3E00?logo=svelte&logoColor=white"></a>
  <a href="store/"><img alt="944 apps" src="https://img.shields.io/badge/store-944%20apps-5B8CFF"></a>
  <a href="LICENSE"><img alt="Apache-2.0" src="https://img.shields.io/badge/license-Apache--2.0-blue"></a>
  <img alt="status" src="https://img.shields.io/badge/status-alpha%200.2-7A5CFF">
</p>

**AgentVerse OS** is a personal cloud operating system for a developer and their AI agents: your own cloud running on a single server,
used from any device through the browser. It is built as a cross-platform vibe coding flow: the same desktop, workspaces and agents
open on a laptop, a tablet or a phone, the workspace and its agents stay on the server, and the work continues where you left it.
One command installs it on a clean Ubuntu; everything after that happens in the browser: a windowed desktop, isolated workspaces with
VS Code and agents (Claude Code, Codex), a store of 944 self-hosted apps, backups and updates. Nothing is exposed to the internet:
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

## What it does

- **Projects and workspaces.** Every project gets its own network, its own gate and an isolated Incus container with Docker inside.
  Inside: VS Code in the browser, a terminal and agents; Claude Code and Codex log in with your subscriptions. Stop/start keeps the
  instance, resources are changed from the project card.
- **A Store of 944 apps.** The Runtipi, Coolify and Umbrel catalogs merged into one, with source badges. Guided install, login
  credentials right in the card, logs, automatic repair of data-directory permissions, links between apps (e.g. n8n → LiteLLM),
  per-app snapshots and rollback.
- **Capabilities instead of addresses.** A project asks for `storage.s3`, `llm` or `notify`; the core connects the project's gate to
  the provider's network and drops environment variables into the workspace. Swapping Garage for another S3 does not touch the project.
- **Browser only.** The first-run wizard joins Tailscale via a link or QR code, checks DNS and the certificate, creates the first project.
  System and app updates come from the Updates window: a package with automatic rollback if the new version does not come up.
- **Backups.** Scheduled ZFS snapshots and a restic repository taken from a snapshot; roll back a single app in two clicks. Off by default.
- **A desktop like a desktop OS.** Windows, taskbar, start menu, widgets (monitor, clock, news, weather, projects), Files over app data
  and workspace homes, Passwords & Access, themes and wallpapers, boot screen, offline overlay, screensaver. The UI speaks English,
  Russian, Ukrainian and Spanish; the language follows the browser or is set once for all devices.
- **Two assistants already in the catalog.** Hermes Agent with a web panel, and Pipecat Voice, a voice assistant in the browser with local
  speech recognition and synthesis. Voice control of the system itself is on the roadmap.

## Architecture

```mermaid
flowchart LR
  subgraph devices["Your devices