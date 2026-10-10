<p align="center">
  <a href="https://getartcraft.com/">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="docs/brand/artcraft-logo-white.svg">
      <img alt="ArtCraft" src="docs/brand/artcraft-logo.svg" width="200">
    </picture>
  </a>
</p>


<h1 align="center">LightCraft</h1>

<h3 align="center">Your photos. Your pixels. Your machine.</h3>

<p align="center">
  <b>Photo library and raw development; an open-source, clean-room reimplementation of Adobe Lightroom, rebuilt in pure Rust.</b><br>
  Native on macOS, Windows and Linux. In the browser via WebAssembly. Drivable end to end by AI agents over MCP.
</p>

<p align="center">
  <img alt="Pure Rust" src="https://img.shields.io/badge/pure-Rust-f2a516?style=flat-square&logo=rust&logoColor=white">
  <img alt="macOS, Windows, Linux and Web" src="https://img.shields.io/badge/macOS%20%C2%B7%20Windows%20%C2%B7%20Linux%20%C2%B7%20Web-8a5800?style=flat-square">
  <img alt="MCP server included" src="https://img.shields.io/badge/MCP-ready-8a5800?style=flat-square">
  <img alt="License: MIT OR Apache-2.0" src="https://img.shields.io/badge/license-MIT%20OR%20Apache--2.0-8a5800?style=flat-square">
  <a href="ROADMAP.md"><img alt="Status: young and moving fast" src="https://img.shields.io/badge/status-young%20%26%20moving%20fast-f2a516?style=flat-square"></a>
</p>

<p align="center">
  <a href="https://discord.gg/artcraft"><img alt="Join the ArtCraft community on Discord" src="https://img.shields.io/badge/Join%20us%20on%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" height="40"></a>
</p>

<p align="center">
  <a href="https://getartcraft.com/apps/lightcraft"><b>LightCraft on getartcraft.com</b></a> ·
  <a href="https://getartcraft.com/">ArtCraft</a> ·
  <a href="https://getartcraft.com/apps">All Crafting Apps</a>
</p>

<br>

<p align="center">
  <img src="docs/images/hero-tetons.jpg" alt="LightCraft's Edit view with Ansel Adams' The Tetons and the Snake River in the loupe, the Light and Effects panels open on the right, and the four showcase photos in the filmstrip" width="100%">
  <br>
  <sub><i>Ansel Adams, "The Tetons and the Snake River" (1942). Public domain, U.S. National Archives. Developed in LightCraft.</i></sub>
</p>

> [!NOTE]
> **ArtCraft is a community of artists from all walks of life.** Digital, generative, music,
> games &mdash; if you make things, you're one of us. **[Come say hi on Discord](https://discord.gg/artcraft).**

<p align="center">
  <a href="#edit-like-you-mean-it">Editing</a> ·
  <a href="#color-grading-the-cinematic-way">Color grading</a> ·
  <a href="#before--after">Before &amp; after</a> ·
  <a href="#masking-that-goes-where-you-point">Masking</a> ·
  <a href="#presets-profiles--the-color-mixer">Presets</a> ·
  <a href="#organize-everything">Library</a> ·
  <a href="#built-for-agents">Agents &amp; MCP</a> ·
  <a href="#fast-native-private">Performance</a> ·
  <a href="#feature-status">Status</a> ·
  <a href="#quick-start">Quick start</a> ·
  <a href="ROADMAP.md">Roadmap</a> ·
  <a href="#downloads">Downloads</a> ·
  <a href="#the-crafting-apps">Crafting Apps</a>
</p>

<br>

## Edit like you mean it

LightCraft is a complete darkroom in a single native app. Every adjustment is **non-destructive**, so your originals
are never touched. Every slider renders through a **scene-referred, wide-gamut, 32-bit float pipeline**: highlights
roll off like film, shadows open up without halos, and colour stays clean from capture to export.

<table>
<tr>
<td width="50%" valign="top">

### ☀️ Light
**Exposure, Contrast, Highlights, Shadows, Whites, Blacks**, with edge-aware local tone mapping (a guided filter on
log-luminance). Pulling −100 Highlights recovers a blown sky without the grey halos you'd get from a naive curve.

### 🎨 Color
**White balance** by temperature and tint (Kelvin for raw, relative for JPEG) with presets, Auto and a
click-to-neutralise **eyedropper**. **Vibrance** that protects skin tones, **Saturation**, an 8-band **Color Mixer**
(hue / saturation / luminance) and 3-way **Color Grading** wheels with blending and balance. All of it is computed in
OkLCh, a modern perceptual colour space.

</td>
<td width="50%" valign="top">

### ✨ Effects
**Texture** for fine detail, **Clarity** for mid-tone punch, **Dehaze** (dark-channel prior with guided refinement;
push it negative to add atmosphere), post-crop **Vignette** with highlight priority, roundness and feather, and
resolution-independent film **Grain** with size and roughness.

### 📈 Tone Curve
Parametric region curve with movable splits **plus** point curves for RGB, Red, Green and Blue. Curves are monotone by
construction, so you never get an accidental tone inversion.

</td>
</tr>
</table>

<p align="center">
  <img src="docs/images/curve-tetons.jpg" alt="The Tone Curve open under the Light panel, with a gentle S-curve on the RGB point curve applied to The Tetons and the Snake River" width="100%">
  <br>
  <sub>A gentle S on the RGB point c