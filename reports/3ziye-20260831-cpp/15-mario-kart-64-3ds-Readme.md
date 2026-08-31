# Mario Kart 64 for Nintendo 3DS

<img width="1672" height="941" alt="Mario Kart 64 running on Nintendo 3DS" src="https://github.com/user-attachments/assets/6b367030-2f4d-4c5d-b295-7d6d7f7d2ceb" />

Native Nintendo 3DS port of Mario Kart 64, based on
[SpaghettiKart](https://github.com/HarbourMasters/SpaghettiKart). It is designed
specifically for the 3DS family, with a dual-screen interface and hardware-aware
rendering, audio, and memory profiles.

> [!WARNING]
> This is an experimental fan port. Save your work before launching it and
> report crashes or rendering issues with a diagnostic dump whenever possible.

No ROM, ROM fragment, save file, or extracted Nintendo game data is distributed
with this project. You must provide your own legally obtained USA Mario Kart 64
ROM.

Made with help from Codex.

## Community

Join the Discord for project updates, support, bug reports, suggestions, and
other Nintendo 3DS homebrew projects:

https://discord.gg/SMW49UMkw

## Features

- Native 400x240 gameplay and an optional 800x240 high-density top-screen mode.
- Selectable Low (0.50x), Medium (0.75x), and High (1.00x) internal resolution.
- Bilinear, Blur, and lightweight CRT display filters.
- Wide 5:3 and Original 4:3 display modes.
- Dual-screen interface, bottom-screen race HUD, and touch menu navigation.
- Hardware-aware Old 3DS and New 3DS resource, HUD, audio, and presentation
  profiles.
- Direct-to-NDSP audio buffers, with synthesis overlapped on an auxiliary CPU
  core when the hardware makes one safely available.
- A compact PICA200 vertex stream, bounded texture storage, and selective
  cache coherency for lower CPU, memory, and upload overhead.
- Original 30 Hz game simulation on every model, with an optional adaptive
  midpoint presentation path on New 3DS systems in 400-pixel mode.
- On-device ROM validation and resource extraction.
- Diagnostic dumps created on demand with `SELECT`.

Multiplayer is planned but is not currently available.

## Performance

Mario Kart 64 retains its original 30 Hz game simulation. On New Nintendo 3DS
systems using the 400-pixel top-screen mode, the port may render an additional
matrix-interpolated midpoint frame when recent frame, GPU, audio, and resource
activity leave enough headroom. It automatically falls back to the required
30 Hz keyframes under pressure.

The midpoint path is adaptive; it is not a promise of a fixed or sustained
60 FPS mode. The 800-pixel quality mode presents keyframes only.

The Screen menu can render the game at half, three-quarter, or full internal
resolution and scale it to the complete top screen. Bilinear uses a single GPU
presentation pass, Blur uses four lightweight samples, and CRT combines
bilinear scaling with a small procedural scanline and shadow-mask pattern.
High resolution with Bilinear selected keeps the original direct presentation
path and does not allocate the intermediate target.

The renderer flushes exact Fast3D vertex and texture ranges and requests a
broader linear-memory coherency pass only on frames that actually submit
Citro2D interface data. Vertex colors use a GPU-native byte format, reducing
the fixed Fast3D vertex allocation and per-frame vertex traffic by 25% without
changing the intended color precision. Audio synthesis writes directly into a
reserved NDSP wave buffer instead of producing and copying an intermediate
block. These changes reduce contention and memory traffic on both hardware
profiles; sustained performance still requires physical-hardware measurement.

## Installation

Download either the CIA for installation with FBI or the full 3DSX application
for the Homebrew Launcher from the
[latest release](https://github.com/EstebanPdN/mario-kart-64-3ds/releases/latest).

Create this folder on your SD card:

```text
sd:/3ds/MK64/
```

Place your USA Mario Kart 64 ROM in that folder and name it either:

```text
mk64.z64
```

or:

```text
Mario Kart 64.z64
```

The ROM must use the `.z64` byte order. ROMs in another byte order can be
converted with the [Hack64 ROM Swapper](https://hack64.net/tools/swapper.php).

### Automatic extraction

Launch the port with the ROM in place. The 3DS validates it and creates:

```text
sd:/3ds/MK64/mk64.o2r
```

The first extraction can take a long time, so keep the console charged. You can
close the lid while extraction continues. Press `START` to cancel, remove the
incomplete output, and exit safely. Later launches reuse the completed archive.

### Desktop extraction

For a faster setup, use
[SpaghettiKart](https://github.com/HarbourMasters/SpaghettiKart) on a computer
to create `mk64.o2r`, then copy it to `sd:/3ds/MK64/` alongside your ROM:

```text
sd:/3ds/MK64/mk64.z64
sd:/3ds/MK64/mk64.o2r
```

## Controls

| Nintendo 3DS | Function |
| --- | --- |
| Circle Pad | Control Stick |
| A / B | A / B |
| R | Hop / Drift |
| L | Use item / Open Options from Game Select |
| X | Camera distance |
| Y | Cycle top-screen HUD during races |
| ZL / ZR | C-buttons |
| C-Stick | Turbo