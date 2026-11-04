# RTX Remix for Minecraft

Play Minecraft Java Edition 1.21.1 with real-time path tracing on a GeForce RTX
GPU, powered by NVIDIA RTX Remix.

## What To Expect

This is a beta. It was built as a technology showcase, but we love Minecraft
and want it to succeed as a rendering mod. We tuned it against one showcase
world, built for this project by [BlockWorks](https://www.blockworks.uk/) (see
[Showcase World And Art Pack](#showcase-world-and-art-pack)), and the places
that world visits are where it looks and runs best. We have worked hard to fix
as many issues as we could, but it ships with
[known issues](https://github.com/NVIDIAGameWorks/rtx-remix-minecraft/issues),
and there are certainly bugs yet to be discovered.

Three areas have had less attention than the rest:

- **Other mods.** It has had limited testing alongside other mods, and a
  renderer that takes over the scene the way this one does is likely to
  conflict with anything that changes rendering or the chunk pipeline.
- **A full playthrough.** Blocks, mobs, dimensions, and situations the showcase
  never reaches have had less care, and some will look wrong or run slowly.
- **Other versions.** It targets Minecraft 1.21.1 only, chosen because that is
  where the modding community is today. Ports to newer versions are something
  we hope the community takes on.

We hope the community helps fill it out. If something breaks,
[report it](docs/PLAYING.md#reporting-a-bug); if you can fix it, see
[Contributing](#contributing).

## Download

Download the release archive from the
[Releases page](https://github.com/NVIDIAGameWorks/rtx-remix-minecraft/releases/latest).

## Install in three steps

1. Extract the release archive.
2. Double-click `install.bat` and follow the menu.
3. Launch the **NVIDIA RTX Remix for Minecraft** profile from your launcher.

The step-by-step version, with launcher advice and troubleshooting, is in
[Playing](docs/PLAYING.md).

## Requirements

- Windows 10 or 11, x64 or ARM64.
- Minecraft Java Edition 1.21.1, on a Microsoft account that owns the game.
- A GeForce RTX 30-series or newer GPU with NVIDIA driver 616.92 or newer.
- About 5 GB of free disk space while installing; about 3 GB stays in use.
- An internet connection while the installer runs.
- 16 GB of system memory is recommended.

Java 21, Fabric, and the RTX Remix runtime are installed for you.

Building and running from source has its own
[prerequisites](docs/GETTING_STARTED.md#prerequisites), including Prism
Launcher, signed in to a Microsoft account that owns Minecraft: Java Edition.

## Crash Reports And Privacy

The mod collects no data of its own. The RTX Remix runtime it carries can send
basic session information and crash reports to NVIDIA. Its First Use Guide asks
about both, with both on by default, and the Permissions tab of the RTX Remix
Graphics Settings menu changes them at any time.
[Crash Reports And Privacy](docs/PLAYING.md#crash-reports-and-privacy) lists
what is sent.

## What it does

**Every block, mob, and item is lit by a path tracer.** Light bounces off walls,
through glass, and out of torches the way it does in a film renderer, so shadows,
reflections, and the colour a nearby block casts on its neighbours are all
computed rather than painted in.

**The look follows the game.** Time of day, weather, and being underwater each
bring their own lighting, and a map author can attach a look to a place in the
world. Nothing needs switching on.

**A new block.** The Copper Beacon is a directional lamp you can place or
carry, and its beam is a real light that picks out walls, rain, and anything
standing in it.

**Camera flythroughs.** Record a path by walking it, then replay it, for a video
or for an exact before-and-after comparison.

**A settings screen in the game.** Distances, framerate, sky, lighting,
exposure, and materials, all in Options, with no config files to edit, and a
button into Remix's own Graphics Settings for the quality tier.

## Showcase World And Art Pack

Two optional extras go with the mod. The developer launcher in
[`tools/`](tools/README.md) downloads both the first time it runs and launches
into the world with the pack on.

- **The showcase world**, the map the renderer was tuned against, was built for
  this project by BlockWorks: [website](https://www.blockworks.uk/),
  [YouTube](https://www.youtube.com/@BlockWorksYT),
  [X](https://x.com/BlockWorksYT), and
  [Instagram](https://www.instagram.com/blockworks/).
- **The RTX art pack**, a texture resource pack, was created by an art team at
  NVIDIA. Its normal and specular maps follow the
  [LabPBR standard](https://shaderlabs.org/wiki/LabPBR_Material_Standard), so
  other renderers and shader packs that read LabPBR may be able to use it too,
  but it has only been tested with this mod. Its `_sss` subsurface maps are
  this mod's own addition, described in
  [Resource Packs](docs/RESOURCE_PACKS.md).

## Start Here

| You want to | Read |
|---|---|
| Play with path tracing | [Playi