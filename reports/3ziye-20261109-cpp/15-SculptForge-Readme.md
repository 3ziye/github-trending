<p align="center">
  <img src="website/img/bust-256.png" width="160" alt="SculptForge: a clay bust on an anvil">
</p>

<h1 align="center">SculptForge</h1>

<p align="center">
  <strong>The free, open-source sculpting app.</strong><br>
  Digital sculpting for VFX, animation and games on Linux, macOS and Windows, with free built-in AI:<br>
  an AI brush creator and image/text to 3D.
</p>

<p align="center">
  <a href="https://github.com/islandmed/SculptForge/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/islandmed/SculptForge/actions/workflows/ci.yml/badge.svg"></a>
  <a href="https://github.com/islandmed/SculptForge/releases/latest"><img alt="Latest release" src="https://img.shields.io/github/v/release/islandmed/SculptForge?color=f28c3c"></a>
  <a href="LICENSE"><img alt="License: GPL-3.0-or-later" src="https://img.shields.io/badge/license-GPL--3.0--or--later-blue"></a>
  <img alt="Platforms" src="https://img.shields.io/badge/platforms-Windows%20%7C%20macOS%20%7C%20Linux-555">
</p>

<p align="center">
  <a href="https://sculptforge.app/"><b>Website & demo videos</b></a> ·
  <a href="https://github.com/islandmed/SculptForge/releases/latest"><b>Download</b></a> ·
  <a href="https://sculptforge.app/guide/"><b>User guide</b></a> ·
  <a href="#features">Features</a> ·
  <a href="#building">Build from source</a> ·
  <a href="CONTRIBUTING.md">Contribute</a> ·
  <a href="https://discord.gg/gWrYkEmQhH">Discord</a> ·
  <a href="https://sculptforge.app/support.html">Membership</a>
</p>

<p align="center"><sub>
  If sculptforge.app is blocked on your network: <a href="https://github.com/islandmed/SculptForge/releases/latest">download from GitHub Releases</a>
  and read the <a href="docs/guide/index.md">user guide on GitHub</a>.
</sub></p>

<p align="center">
  <a href="https://sculptforge.app/#demos"><img src="docs/images/showcase.jpg" width="800" alt="A detailed lion head sculpted in SculptForge"></a>
</p>

SculptForge is a free, open-source, focused sculpting app with the brushes, symmetry and
navigation experienced sculptors already know. It costs nothing, has no subscription, runs natively on Linux as well as
Windows and macOS, and comes with source code you can change. It starts instantly, works offline,
and fits into game and animation pipelines: sculpt a character, generate its LODs, sculpt blend shapes, and
send it straight into Unreal Engine. **AI comes built in and free**: describe a brush and the AI brush creator
(Brush Lab) builds it, or turn a sketch, concept art or a description into a sculptable model. No account or key is needed. Prefer your own?
Plug in Claude, fal.ai or Meshy, or run models entirely on your own machine.

## Experienced sculptor?

Pick **Classic sculpting keys** at the first start and your hands know the way: familiar brushes, symmetry, Alt and
Shift modifiers, masking and face groups with Ctrl and Ctrl+Shift, Parts, subdivision levels, dynamic topology, quad
remeshing and a Gizmo. Bring models over as OBJ, FBX, glTF or USD, or through the Bridge (face groups, mask and vertex
paint come along).

> **Status: early release (v0.8).** The core sculpting, pipeline and AI features work and are tested on every
> commit. Version 0.8 adds dynamic topology (brushes add triangles where they need them),
> vector displacement brushes, Quad Remesh Guides and sculpt layers on every subdivision level; 0.7 added classic
> keys and gestures and a Blender bridge add-on; 0.6 halved the memory and made the view twice as
> fast on huge meshes (see the [changelog](CHANGELOG.md)).

## Features

**An interface experienced sculptors can find their way around**
- Task menus (File, Edit, Sculpt, Paint, Mesh, View, Render, Help) in the Forge Terminal look by default, or the
  Classic layout with alphabetical palettes in one click (Preferences > Interface > Look)
- Shelves around the canvas, palettes holding every tool, a Library (`,`) of thumbnails, the
  brush picker (`B`, type letters to pick), hold-Ctrl help on every button, a command palette (F3) and a script
  console (`` ` ``), and a fully customizable layout; preferences save themselves. See [docs/ui-design.md](docs/ui-design.md).
- A built-in **user guide** (Help > User Guide, Shift+F1) with search, also on the
  [website](https://sculptforge.app/guide/); hold Ctrl over any control and press F1 to open its
  chapter. Source: [docs/guide](docs/guide/index.md).

**Sculpting**
- Standard, Clay, Smooth, Move, Inflate, Crease, Flatten, Pinch, Sharp Crease, Clay Block, Tendril, Trim,
  Layer and Nudge brushes; X/Y/Z symmetry; tablet pressure; classic modifiers and navigation.
- Stroke types (dots, drag-rect, spray, lazy mouse) and brush alphas (built-in or any grayscale image).
- **Masking** (Ctrl to paint, invert, blur, sharpen, grow/shrink, mask by cavity or face group) that every brush
  respects.
- **Face Groups and visibility** with classic gestures: auto groups, Ctrl+Shift isolate / hide, rectangle hide, remove
  hidden.
- **Parts**: keep t