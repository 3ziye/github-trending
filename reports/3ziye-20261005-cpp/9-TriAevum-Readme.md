# TriAevum

A native PC AOT recompilation of *The Legend of Zelda: Ocarina of Time 3D*,
with a modern NRI/Vulkan renderer, single-screen UI and customizable graphics.

## Credit Where It Belongs

Before the shaders, settings and excessive grass: **TriAevum would not exist in
its current form without [TopScreen](https://gamebanana.com/mods/695893),
developed by rlgcarrot**. Its single-screen experience is reimplemented here for
our runtime, but the vision, care and tremendous work behind it deserve a
special thank-you. Please consider [buying rlgcarrot a coffee](https://ko-fi.com/rlgcarrot)
to support that fantastic work.

Just as essential are **Azahar, Ship of Harkinian, libultraship, NVIDIA NRI**,
and the SDL controller-mapping community. And, of course, **Nintendo and
Grezzo**, who created the original game. [Full credits and licenses](THIRD_PARTY_NOTICES.md).

> **alpha.3 and alpha.3b are BROKEN and withdrawn. Do not use these builds.**
> Downloads have been removed pending further verification. Back up existing
> saves/settings. [Release status and earlier releases](https://github.com/coccofresco/TriAevum/releases).

## About

TriAevum is an AOT recomp in the same general spirit as the Xbox 360 recomp
projects. I just ended up spending most of my time on the renderer instead of,
you know, actually playing the game. The goal is to push the visuals further
without completely losing the original look.

**Development of this project is entirely AI-assisted, under human direction.**
That describes the TriAevum-specific work, not the mature donor projects and
libraries it builds on: Azahar, Ship of Harkinian, NRI and others. Aside from
those foundations, you could fairly call this concentrated AI slop.
Apparently, even AI slop can still consume several months of your life.

## Install

Requires Windows or Linux x64, a Vulkan-capable GPU with current drivers, and your own
supported decrypted ROM. Forge accepts `.3ds` and `.cci` and checks the contents,
not just the filename.

It should work with any personal EUR or USA ROM dump, provided it is decrypted
and in `.cci` or `.3ds` format.
See [ROM compatibility details](docs/TRIAEVUM_CONTENT_FAMILY_IMPORT.md).

### Windows

1. Download the **Windows-x64 ZIP**, not GitHub's source-code archive, and
   extract it into a writable folder.
2. Run `TriAevumForge.exe` and select your decrypted ROM.
3. When setup finishes, choose **Launch game**. Afterwards, use `TriAevum.exe`.

### Linux and Steam Deck

The alpha.3/alpha.3b AppImages are withdrawn; the instructions below describe
the intended packaging, not a currently recommended download.

1. Download the **Linux-x86_64.AppImage** and make it executable in your file
   manager, or with `chmod +x TriAevum-*.AppImage`.
2. Open the AppImage and select your decrypted ROM in Forge.
3. Choose **Launch game** when preparation finishes.

On Steam Deck, prepare in Desktop Mode, then add the same AppImage as a non-Steam
game. Use Steam Input's Gamepad layout without Proton. Physical Steam Deck and
Gaming Mode testing have not yet been performed. `--forge` reopens preparation;
`--appimage-extract-and-run` is available on systems without FUSE.

No compiler or SDK is needed. Forge downloads the official TopScreen texture
package during setup; an Internet connection is required unless that package
is [provided locally](docs/TRIAEVUM_TOPSCREEN_INSTALLATION.md). No ROM or original
game assets are included. Forge also prepares the bundled shaders for your GPU
automatically; shaders encountered later are cached while playing.
Back up your saves, settings and prepared data: `data/` beside the Windows
application, or `$XDG_DATA_HOME/TriAevum` (normally `~/.local/share/TriAevum`)
on Linux. Old Flatpak data remains in `~/.var/app/io.github.coccofresco.TriAevum/`
and is not migrated automatically.

## Graphics and controls

- Cel/toon shading and outlines.
- Ambient occlusion, plus optional reflections, shadows and anti-aliasing.
- Real widescreen framing and configurable field of view.
- **60/90 FPS visual interpolation** of the original 30 Hz game state.
  Game logic and gameplay speed remain unchanged; this is not 60/90 Hz physics.
- Azahar-compatible custom textures and texture dumping.
- Reimplemented **TopScreen** single-screen HUD and menus.
- Configurable gameplay free camera, keyboard/mouse and controller inputs.
- Named settings profiles, audio and save states.
- Procedural grass. A lot of grass. Possibly too much grass.

Press **F1** for settings. **F2** temporarily disables the main added graphics
effects, then restores them without losing your configuration. Most of the
presentation is configurable, so if my artistic decisions offend you
personally, you can probably undo them. Effects can be expensive; adjust them
to suit your GPU.

## Testing and contributing

This is an **experimental alpha**, not a fully tested port. Gameplay testing
currently covers the early parts of the game. The USA adapter has been checked
through insta