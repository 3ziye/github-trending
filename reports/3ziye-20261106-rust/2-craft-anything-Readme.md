<p align="center">
  <a href="https://getartcraft.com/">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="docs/brand/artcraft-logo-white.svg">
      <img alt="ArtCraft" src="docs/brand/artcraft-logo.svg" width="200">
    </picture>
  </a>
</p>

<p align="center">
  <img src="assets/app-icon/hicolor/256x256/apps/ai.storyteller.craft-anything.png" width="128" height="128" alt="Craft Anything icon: an engraved raven on a blue tile">
</p>

<h1 align="center">Craft Anything</h1>

<p align="center">
  <b>English</b> · <a href="README.ja.md">日本語</a> · <a href="README.zh.md">简体中文</a> · <a href="README.ko.md">한국어</a>
</p>

<p align="center">
  <b>See how any website, app or game works, then have AI build your own version; an open-source, clean-room engine in pure Rust.</b><br>
  Point it at a target, say what you want, and it studies the original with real inspection tools,<br>
  has a coding agent build a new project, checks the result against the original and refines it.
</p>

<p align="center">
  <img alt="100% Rust" src="https://img.shields.io/badge/100%25-Rust-b7410e?style=flat-square&logo=rust">
  <img alt="macOS · Windows · Linux · FreeBSD · Web" src="https://img.shields.io/badge/macOS%20%C2%B7%20Windows%20%C2%B7%20Linux%20%C2%B7%20FreeBSD%20%C2%B7%20Web-native-2d81ff?style=flat-square">
  <img alt="License: MIT OR Apache-2.0" src="https://img.shields.io/badge/license-MIT%20%2F%20Apache--2.0-3a3a3a?style=flat-square">
  <img alt="Status: early alpha" src="https://img.shields.io/badge/status-early%20alpha-d69e2e?style=flat-square">
</p>

<p align="center">
  <a href="https://discord.gg/artcraft"><img alt="Join the ArtCraft community on Discord" src="https://img.shields.io/badge/Join%20us%20on%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" height="40"></a>
</p>

<p align="center">
  <a href="#downloads"><b>Download Craft Anything</b></a> ·
  <a href="https://getartcraft.com/">ArtCraft</a> ·
  <a href="https://getartcraft.com/apps">All Crafting Apps</a>
</p>

<br>

<p align="center">
  <img src="docs/images/project-website.png" alt="A website project in Craft Anything: the check lists what doesn't match yet and how alike each page is, the builder says its version is ready, an approval card asks before running a command, and the plan shows two of four steps done" width="100%">
  <br>
  <sub>A website project: each check says how alike the build is, you approve anything outside the rules, and the plan shows what's left.</sub>
</p>

> [!NOTE]
> **ArtCraft is a community of artists from all walks of life.** Painters, photographers,
> filmmakers, illustrators, designers, animators, hobbyists, and people who picked up a pencil
> last week. If you make things, you're one of us. **[Come say hi on Discord](https://discord.gg/artcraft).**

<p align="center">
  <a href="#how-it-works">How it works</a> ·
  <a href="#two-ways-to-use-it">Two ways to use it</a> ·
  <a href="#ai">AI</a> ·
  <a href="#built-for-agents">Agents</a> ·
  <a href="#under-the-hood">Under the hood</a> ·
  <a href="#get-started">Get started</a> ·
  <a href="#status">Status</a> ·
  <a href="#downloads">Downloads</a> ·
  <a href="https://discord.gg/artcraft">Discord</a>
</p>

<br>

<table>
  <tr>
    <td width="25%" valign="top">
      <h3>🔍 Study anything</h3>
      Websites, desktop apps, phone apps, games and files: real inspection tools find out how they're built and what they do, with the evidence behind every answer.
    </td>
    <td width="25%" valign="top">
      <h3>🛠️ Build your own</h3>
      Say what you want ("Recreate this website", "Recreate this game's gameplay in Rust") and a coding agent builds a new project in the stack you ask for.
    </td>
    <td width="25%" valign="top">
      <h3>✅ Checked, not guessed</h3>
      Every build is compared with the original (pages at three screen widths, a game's own self-test, an app's runs) and refined until it's close.
    </td>
    <td width="25%" valign="top">
      <h3>🤖 Agent-ready</h3>
      320 tools, each one a CLI command and an MCP tool, so any agent can drive the same engine the app uses. No AI is needed to inspect.
    </td>
  </tr>
</table>

<br>

## How it works

Point Craft Anything at a target, say what you want, and press Start. It works in four steps,
asking you in plain words when a decision is yours:

1. **Study:** inspect the original: its pages at every width, its code, its files, how it runs.
2. **Build:** a coding agent builds a new project, in the language, framework or engine your
   request names (or a sensible default).
3. **Check:** compare the build with the original and list what doesn't match yet.
4. **Ready:** open, play or preview the result, or ask for changes and it refines it.

<table>
  <tr>
    <td width="50%" valign="top">
      <img src="docs/images/make.png" alt="The Make screen: pick a website, an app or a game to recreate, type the address, choose Clean room or Deep, say what you want and press Start" width="10