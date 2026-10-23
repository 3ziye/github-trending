<p align="center">
  <a href="https://getartcraft.com/">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="docs/brand/artcraft-logo-white.svg">
      <img alt="ArtCraft" src="docs/brand/artcraft-logo.svg" width="200">
    </picture>
  </a>
</p>


<p align="center">
  <img src="assets/app-icon/hicolor/256x256/apps/ai.storyteller.designcraft.png" width="128" height="128" alt="DesignCraft icon: an engraved cat in a polka-dot scarf on a green tile">
</p>

<h1 align="center">DesignCraft</h1>

<p align="center">
  <b>Page layout and publishing; an open-source, modern desktop publishing and page layout studio, built in pure Rust.</b>
</p>

<p align="center">
  A fast, open-source desktop publishing and page layout workflow. It runs natively on macOS,
  Windows and Linux, and in the browser via WebAssembly.<br>
  <i>By the ArtCraft team.</i>
</p>

<p align="center">
  <img alt="Written in Rust" src="https://img.shields.io/badge/written%20in-Rust-4d7a0a?style=flat-square&logo=rust&logoColor=white">
  <img alt="Runs on macOS, Windows, Linux and the web" src="https://img.shields.io/badge/runs%20on-macOS%20%C2%B7%20Windows%20%C2%B7%20Linux%20%C2%B7%20Web-7bb51c?style=flat-square">
  <img alt="License: MIT OR Apache-2.0" src="https://img.shields.io/badge/license-MIT%20%2F%20Apache--2.0-4d7a0a?style=flat-square">
  <img alt="Agent-drivable over MCP" src="https://img.shields.io/badge/agents-MCP-7bb51c?style=flat-square">
  <br>
  <a href="https://sonarcloud.io/project/overview?id=storytold_designcraft"><img alt="Scanned by SonarCloud" src="https://img.shields.io/badge/Scanned_by-SonarCloud-4b9fd5?style=flat-square&logo=sonarqubecloud&logoColor=white"></a>
  <a href="https://coderabbit.ai"><img alt="Reviewed by CodeRabbit" src="https://img.shields.io/coderabbit/prs/github/storytold/designcraft?style=flat-square&label=Reviewed%20by%20CodeRabbit&logo=coderabbit"></a>
</p>

<p align="center">
  <a href="https://discord.gg/artcraft"><img alt="Join the ArtCraft community on Discord" src="https://img.shields.io/badge/Join%20us%20on%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" height="40"></a>
</p>

<p align="center">
  <a href="https://getartcraft.com/apps/designcraft"><b>DesignCraft on getartcraft.com</b></a> ·
  <a href="https://getartcraft.com/">ArtCraft</a> ·
  <a href="https://getartcraft.com/apps">All Crafting Apps</a>
</p>

<br>

<p align="center">
  <img src="docs/images/ui-spread.png" alt="DesignCraft showing a magazine spread: a threaded three-column story is selected with its in/out ports and thread line, the Control panel shows its position in picas and the Properties panel its text frame options" width="100%">
  <br><sub><b>Quarterly, Spring Issue</b>: threaded three-column body text, a wrapped pull quote and parent-page folios, all set by DesignCraft's own paragraph composer.</sub>
</p>

> [!NOTE]
> **ArtCraft is a community of artists from all walks of life.** Digital, generative, music,
> games &mdash; if you make things, you're one of us. **[Come say hi on Discord](https://discord.gg/artcraft).**

<p align="center">
  <a href="#the-sample-magazine">The sample magazine</a> ·
  <a href="#why-designcraft">Why DesignCraft</a> ·
  <a href="#quick-start">Quick start</a> ·
  <a href="#web">Web</a> ·
  <a href="#architecture">Architecture</a> ·
  <a href="#downloads">Downloads</a> ·
  <a href="#the-crafting-apps">The Crafting Apps</a> ·
  <a href="#license-and-credits">License and credits</a>
</p>

## The sample magazine

Every page below was laid out by DesignCraft from code (`crates/engine/src/sample.rs`) and exported
by its own renderer. Try it yourself with `File → New → Sample Document`, or start the app with
`--sample`.

<table>
<tr>
<td width="50%" valign="top"><img src="docs/images/page-cover.png" alt="Magazine cover for The Spring Issue, No. 01: a dusk landscape of layered purple hills under a large pale sun, with the white serif headline The Quiet Art of Layout and an italic deck below" width="100%"><p align="center"><sub><b>Cover.</b> A full-bleed graphic frame, display type and an italic deck.</sub></p></td>
<td width="50%" valign="top"><img src="docs/images/page-2.png" alt="Feature opener titled Notes on the Grid, with an orange FEATURE · DESIGN kicker over a rule, an italic deck, a wide landscape picture with a small caption, and two columns of justified body text above a QUARTERLY folio" width="100%"><p align="center"><sub><b>Styles.</b> Kicker rule, headline, deck, caption and justified two-column body.</sub></p></td>
</tr>
<tr>
<td width="50%" valign="top"><img src="docs/images/page-3.png" alt="Three-column page of justified, hyphenated body text that wraps around a shaded pull quote reading The best layouts disappear. What remains is the story., with a gradient rule and SPRING ISSUE folio at the foot" width="100%"><p align="center"><sub><b>Threading, columns and text wrap.</b> One story flows through three columns and around the pull quote.</sub></p></td>
<t