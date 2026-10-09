<p align="center">
  <a href="https://getartcraft.com/">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="docs/brand/artcraft-logo-white.svg">
      <img alt="ArtCraft" src="docs/brand/artcraft-logo.svg" width="200">
    </picture>
  </a>
</p>


<h1 align="center">EffectCraft</h1>

<p align="center">
  <b>Motion graphics and visual effects; an open-source, clean-room reimplementation of Adobe After Effects, rebuilt in pure Rust.</b>
</p>

<p align="center">
  A free, open-source compositor in the spirit of After Effects: compositions, layers,
  keyframes, 306 effects, layer styles, expressions, 3D cameras and lights, and a render queue, native on macOS,
  Windows and Linux, and in the browser. Young, moving fast, and already usable.
</p>

<p align="center">
  <img alt="Status: young and moving fast" src="https://img.shields.io/badge/status-young%20and%20moving%20fast-e0368f?style=flat-square">
  <img alt="Written in Rust" src="https://img.shields.io/badge/rust-1.95%2B-b0206c?style=flat-square&logo=rust&logoColor=white">
  <img alt="License: MIT OR Apache-2.0" src="https://img.shields.io/badge/license-MIT%20%2F%20Apache--2.0-555?style=flat-square">
</p>

<p align="center">
  <a href="https://discord.gg/artcraft"><img alt="Join the ArtCraft community on Discord" src="https://img.shields.io/badge/Join%20us%20on%20Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" height="40"></a>
</p>

<p align="center">
  <a href="https://getartcraft.com/apps/effectcraft"><b>EffectCraft on getartcraft.com</b></a> ·
  <a href="https://getartcraft.com/">ArtCraft</a> ·
  <a href="https://getartcraft.com/apps">All Crafting Apps</a>
</p>

<br>

<p align="center">
  <img src="docs/images/effectcraft-hero.png" alt="EffectCraft's main window: the animated demo composition in the Composition panel, the Project panel, a Timeline with text, shape and solid layers, and the Properties panel showing the selected text layer's transform, font and paragraph settings" width="100%">
</p>

> [!NOTE]
> **ArtCraft is a community of artists from all walks of life.** Digital, generative, music,
> games &mdash; if you make things, you're one of us. **[Come say hi on Discord](https://discord.gg/artcraft).**

<p align="center">
  <a href="#what-effectcraft-is">What it is</a> ·
  <a href="#animate">Animate</a> ·
  <a href="#effects">Effects</a> ·
  <a href="#3d">3D</a> ·
  <a href="#export">Export</a> ·
  <a href="#built-for-agents">Agents</a> ·
  <a href="#get-started">Get started</a> ·
  <a href="#where-it-stands">Status</a> ·
  <a href="#how-its-made">How it's made</a> ·
  <a href="#downloads">Downloads</a> ·
  <a href="#the-crafting-apps">The Crafting Apps</a> ·
  <a href="#license-and-credits">License</a>
</p>

## What EffectCraft is

EffectCraft is for animated titles, motion graphics and compositing work: the kind of thing
people reach for After Effects to do. You build a composition out of layers (solids, shapes,
text, footage, other compositions), animate their properties with keyframes, stack effects on
them and render the result.

The aim is to feel familiar to anyone who has used After Effects, with the same panels (Project,
Composition, Timeline, Effect Controls, Effects & Presets) and the same keyframe behaviour, and
then to go further in a few places where it matters to us:

- **Lottie import and export built in**, so animations can go straight to the web and apps
  without a plugin.
- **A project file you can read.** Projects are versioned JSON (`.ecproj`), so they diff cleanly
  in version control.
- **Everything is scriptable.** Every menu item, timeline drag and property edit goes through one
  command registry, so the same actions are reachable from a command line, a JSON control
  channel and an MCP server for agents.
- **No FFmpeg.** Video and audio decoding and encoding are pure Rust: FilmCraft's codecs and
  EffectCraft's own VP9, AV1, HEVC and Opus encoders.

## Animate

The panels, menus and shortcuts follow After Effects, so your muscle memory carries over:
Project, Composition, Timeline, Effect Controls, Properties, Effects & Presets, Character,
Paragraph, Align, Info, Preview, Audio and the Render Queue, docked the way you expect. Drag
footage, comps and effects between them: onto the comp viewer, where they land under the pointer,
or into the Timeline, between layers and at the time you point to.

- **Layers of every kind:** solids, shapes, text, footage, nested compositions, nulls,
  adjustment layers, cameras and lights; parenting, track mattes, all 38 blend modes, motion blur.
- **Keyframes that behave the same:** linear, Bezier, hold, auto and continuous Bezier, roving
  keys, Easy Ease (F9), Keyframe Velocity and Interpolation dialogs, copy and paste at the current
  time, and a **Graph Editor** with value and speed graphs and draggable handles.
- **Time:** time remapping, time stretch, time-reverse, freeze frame, work area, markers, exact
  frame-accurate timing at every frame rat