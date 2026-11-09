# Shadow of the Colossus — PC native port · v0.72.2

[Releases](../../releases) · [Changelog](CHANGELOG.md)

> [!CAUTION]
> *⚠️*No game or Sony files are included.** You need your own game dump and, for sound, two
> modules from your own console. This project is not affiliated with Sony Interactive
> Entertainment or Bluepoint Games.

> [!CAUTION]
> ⚠️ **Install the game on an SSD, NVMe if you can.** Every new area streams hundreds of MB of
> textures and models from the game folder; on a hard disk the area changes stutter far more and
> can freeze for seconds. Put the game dump (and, ideally, the port's folder) on an SSD.

---

**Status: the game can be finished from start to end** (v0.60.3: played through the last
colossus, the ending and the credits, with high quality textures, PS4 Pro mode and 60 FPS on).

A native Windows port of the PS4 **Shadow of the Colossus** (Bluepoint, 2018; CUSA08809 EU 1.01 or
CUSA08034 US 1.00) for **Windows 10/11**. The game's own x86-64 code runs directly on the PC's CPU and the PS4 GPU
is translated to Vulkan. It is not a full emulator: it is a loader with the system functions the
game needs, in the style of [bloodborne_pc](https://github.com/Supermedo/bloodborne_pc).

### What's new

| Version | Improvements and fixes |
|---|---|
| **0.72.2** | **Ending fixed:** no stretched textures or flicker at the end of the game and no close between the ending and the intro (textures the game freed while drawing them keep their contents for 400 frames). **Smoother area changes:** High/Maximum textures back at mip 2, area-change memory releases without a full GPU wait, and with 24 GB of RAM or more new textures read by the GPU straight from the game's memory. **Large textures get memory of their own** (no more 1.8 GB held empty after an area change). **Updating clears the shader cache once.** Window title with the port version and the play time. |
| **0.72.1** | **Cards with less than 8 GB of video memory get a light profile automatically:** Maximum textures at mip 1 (without the 3 s bank linger, with the page pool safety switch), High at mip 2 as in 0.71, video memory use capped at Default, no staging reserve in video memory. 8 GB cards and up keep everything. **"Card memory" in the launcher's quick settings** (Play page): Automatic (by the card), Light or Full. |
| **0.72** | **Improvements the 0.71 page pool fix made safe, now on by default:** fast GPU readbacks (~25% more FPS at the Shrine), sharper textures (finer mips: High mip 1, Maximum mip 0, with measured mips) and Maximum keeping texture banks 3 s, the heap guard shortcuts. **New upscaler: AMD FSR 4.1** (official AMD FSR SDK 2.4, Vulkan; FSR 4.1 on Radeon RX 6000/7000/9000, FSR 3.1 on other cards; experimental). **Play modes keep the grass as on PS4.** Fewer stutters at area changes (staging reserve, texture copies with fewer page faults), the right video memory budget on integrated GPUs, launcher fixes. |---|---|
| **0.71** |🔧 Critical Fixes & Performance • No More Texture Mosaics & Crashes: Fixed a critical memory bug where the game's 64 KiB page pool freed pages twice, causing textures and the heap to conflict. Tested through every Time Attack colossus on Maximum settings with zero crashes and perfect textures.• Stutter Reduction: Smoother transitions between areas thanks to optimized staging buffers and a rebuilt shader cache.• Visual Cleaning: Native motion blur is now disabled by default to fix the "shadow trail" artifact in dark areas. Optimized DLSS with Preset E and a current-frame bias for sharper imagery. Includes HUD-less frame generation by default.• Experimental HDR10: Added a new experimental HDR10 output mode for the base SDR game.🎮 All-New Custom Launcher Redesigned with a Shadow of the Colossus aesthetic (night stone, golden typography, and reactive sword-light highlights) inspired by the bloodborne_pc launcher.• Play Modes: Quick presets for Normal, Pro, Extreme (60 FPS, max textures, extended grass/shadow distance, DLSS), and Custom.• First-Time Setup Guide: A thematic 5-step hardware wizard that benchmarks your PC (CPU, GPU, RAM, Storage) and picks your ideal play mode.• Advanced Save Manager: Import/export your progress via .zip or shadPS4, with manual and automatic backups upon game close or crash.• Quality of Life: Global settings search (Ctrl+F), an interactive controller button tester, multi-monitor selection, a one-click bug report tool, and a dedicated help section. |
| **0.70** | **Area changes no longer drop to near zero FPS** (worst frame 534 ms → 58–75 ms, no forced loading screens; 1–6 frames are still lost per change), **fix for a rare crash in the game's allocator after a load** (`0x49800`), **DLSS no longer shakes** in PS4 Pro mode at 30 FPS, **the HUD stays still with frame generation** on FSR 1, a cheaper LOD feedback, new draw thread diagnostics. **Install the game on an SSD.** |
| **0.60.6-C3** | Fix for the C2 stamina bar with DLSS (wide screens, and 16:9 outside PS4 Pro mode); the 3