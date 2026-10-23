<p align="center">
  <a href="https://getartcraft.com/">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/storytold/vectorcraft/main/docs/brand/artcraft-logo-white.png">
      <img alt="ArtCraft" src="https://raw.githubusercontent.com/storytold/vectorcraft/main/docs/brand/artcraft-logo.png" width="200">
    </picture>
  </a>
</p>

<p align="center">
  <img src="assets/app-icon/hicolor/256x256/apps/ai.storyteller.figcraft.png" width="128" height="128" alt="FigCraft icon: an engraved chameleon on a mint-green tile">
</p>

<h1 align="center">FigCraft</h1>

<p align="center">
  <b>Interface design and prototyping: open source, collaborative and built in pure Rust.</b><br>
  Frames, auto layout, components and variants, vector networks, styles, variables and prototypes,<br>
  in a native app that opens instantly and works offline. Open source, and yours.
</p>

<p align="center">
  <img alt="100% Rust" src="https://img.shields.io/badge/100%25-Rust-b7410e?style=flat-square&logo=rust">
  <img alt="macOS · Windows · Linux · FreeBSD · Web" src="https://img.shields.io/badge/macOS%20%C2%B7%20Windows%20%C2%B7%20Linux%20%C2%B7%20FreeBSD%20%C2%B7%20Web-native-0EA5C6?style=flat-square">
  <img alt="License: MIT OR Apache-2.0" src="https://img.shields.io/badge/license-MIT%20%2F%20Apache--2.0-3a3a3a?style=flat-square">
  <img alt="Status: early alpha" src="https://img.shields.io/badge/status-early%20alpha-d69e2e?style=flat-square">
  <br>
  <a href="https://sonarcloud.io/project/overview?id=storytold_figcraft"><img alt="Scanned by SonarCloud" src="https://img.shields.io/badge/Scanned_by-SonarCloud-4b9fd5?style=flat-square&logo=sonarqubecloud&logoColor=white"></a>
  <a href="https://coderabbit.ai"><img alt="Reviewed by CodeRabbit" src="https://img.shields.io/coderabbit/prs/github/storytold/figcraft?style=flat-square&label=Reviewed%20by%20CodeRabbit&logo=coderabbit"></a>
</p>

<p align="center">
  <a href="https://discord.gg/artcraft"><img alt="Join the ArtCraft community on Discord" src="https://img.shields.io/badge/Join%20us%20on%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" height="40"></a>
</p>

<p align="center">
  <a href="https://getartcraft.com/apps/figcraft"><b>FigCraft on getartcraft.com</b></a> ·
  <a href="https://getartcraft.com/">ArtCraft</a> ·
  <a href="https://getartcraft.com/apps">All Crafting Apps</a>
</p>

<br>

<p align="center">
  <img src="docs/images/shot-1-hero.png" alt="FigCraft in its dark theme editing the Ridgeline hiking app: three phone screens (Home in light mode, a trail detail page and Home in dark mode) on the canvas, the Featured trail card instance selected, the layers panel showing the screen's auto layout tree, and the Design panel showing the instance's Fill and Hug auto layout sizing, its Theme variable mode and a fill bound to the surface colour variable" width="100%">
  <br><sub><b>Ridgeline</b>: auto layout screens built from components, with Light and Dark modes from one set of colour variables · <code>examples/ridgeline-app.figcraft</code></sub>
</p>

<br>

> [!NOTE]
> **ArtCraft is a community of artists from all walks of life.** Designers, illustrators, developers,
> musicians, game makers &mdash; if you make things, you're one of us. **[Come say hi on Discord](https://discord.gg/artcraft).**

<p align="center">
  <a href="#a-look-around">A look around</a> ·
  <a href="#made-in-figcraft">Made in FigCraft</a> ·
  <a href="#features">Features</a> ·
  <a href="#built-for-agents">Agents</a> ·
  <a href="#under-the-hood">Under the hood</a> ·
  <a href="#get-started">Get started</a> ·
  <a href="#the-crafting-apps">Crafting Apps</a> ·
  <a href="https://discord.gg/artcraft">Discord</a>
</p>

<br>

<table>
  <tr>
    <td width="25%" valign="top">
      <h3>🎛️ Familiar by design</h3>
      The toolbar, layers panel, Design panel, menus and shortcuts sit right where your hands expect them.
    </td>
    <td width="25%" valign="top">
      <h3>⚡ Native and fast</h3>
      A Rust engine with a persistent document model: edits touch only what changed, so creating a node in a 20,000-node file takes a fraction of a millisecond. No Electron, no web view.
    </td>
    <td width="25%" valign="top">
      <h3>🔌 Offline and private</h3>
      Your files are plain <code>.figcraft</code> archives on your own disk. No account, no telemetry, and nothing leaves your computer unless you share a file (<a href="#privacy-and-online-sharing">what sharing sends where</a>). SVG, PNG, JPG, WebP and PDF in and out; <code>.fig</code> files open (best effort), and so do designs exported as the public REST API file JSON, with their prototypes and variables.
    </td>
    <td width="25%" valign="top">
      <h3>🤖 Agent-ready</h3>
      Every menu item, tool and drag is a command, so the same engine runs from the UI, the CLI, a JSON control channel or an MCP server.
    </td>
  </tr>
</table>

<br>

## A look around

<table>
<tr>
<td widt