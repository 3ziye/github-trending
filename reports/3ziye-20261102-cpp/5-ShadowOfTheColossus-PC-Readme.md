# Shadow of the Colossus — PC native port · v0.70

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
| **0.70** | **Area changes no longer drop to near zero FPS** (worst frame 534 ms → 58–75 ms, no forced loading screens; 1–6 frames are still lost per change), **fix for a rare crash in the game's allocator after a load** (`0x49800`), **DLSS no longer shakes** in PS4 Pro mode at 30 FPS, **the HUD stays still with frame generation** on FSR 1, a cheaper LOD feedback, new draw thread diagnostics. **Install the game on an SSD.** |
| **0.60.6-C3** | Fix for the C2 stamina bar with DLSS (wide screens, and 16:9 outside PS4 Pro mode); the 30 FPS cap holds in PS4 Pro mode too. |
| **0.60.6-C2** | **Widescreen health and stamina bars fixed** (21:9 / 32:9, #301), **controller vibration toggle** (launcher and in-game menu, #292), **more FPS at the Shrine** (Lucas-blip-png's barrier change), **frame generation without the interface** (no shaking text, experimental), **DLSS Ultra Performance**. |
| **0.60.6-C1** | **Community release.** tabnul's **page allocator fix** (an hour in Maximum + PS4 Pro without a crash, far less colour garbage after loads), **Maximum textures in PS4 Pro mode** (experimental), **NVIDIA DLSS** for RTX 20 and newer (tabnul; here also in PS4 Pro mode and at 4K), **grass** distance/height/detail live in the in-game menu (tabnul), the **US release CUSA08034** (NathanMBR), fixes for weak CPUs and GTX 10xx (JihedMrouki), Oussama268's readback and bind work (new "More FPS" option), **F7: 30 → 60 → unlimited**, a launcher **Debug** page (debug menu on F6 / Start+Select, skip the logos). |
| **0.60.6** | **No more rainbow garbage on textures and far fewer "closed out of nowhere" crashes** (the cause: speculative GPU readbacks written over memory the game had reused, after loading a save or a new area), **no more black dots on sandy ground**, **in-game menu cleaned up** (FPS, upscaler and sharpening now change at once; Bloodborne leftovers removed), **hard disk read-ahead** (fewer stalls in new areas on HDDs), textures refreshed on every load, a readable session event log (`user/events.log`). |
| **0.60.5** | **Texture quality selector: Off / High / Maximum** (#235: sharp again), **memory leak fixed** (~60 MB/min, long-session stutter), **+3% average and +12% minimum FPS** (descriptor binds reused), **loading after a GPU driver update: 106 s → 7 s**, possible fix for **white characters on AMD GCN** (RX 470–590, Vega), **4-thread CPUs** no longer stuck loading, a hang watchdog, short hitches no longer flash a black loading screen, code review fixes. |
| **0.60.4** | **No more cyan blocks on stone or blinking flowers** with high quality textures (the 0.60.3 crash protection switched the texture detail every second or two; now with hysteresis). |
| **0.60.3** | **The game can be finished from start to end** (played from the last colossus through the ending and credits): fix for the high quality textures crash in wide views (#186), fix for the crash on the load after the credits, +2.7% FPS at the Shrine. |
| **0.60.2** | **Quick settings in the in-game menu** (60 FPS, frame generation, high quality textures, far shadows, volume: apply at once and are kept), **the mouse works in the menu**, **animated loading screen while the shaders are prepared** at start. |
| **0.60.1** | **In-game menu** (Insert / F1 / L3+R3: FPS, GPU and VRAM, fullscreen, resolution, sharpening, mouse camera, effects), **Bloodborne leftovers removed** (~11,700 lines), the game exe has the SotC icon. |
| **0.60** | **Textures on GTX 10xx**, no title-screen hang, **starts on low-memory PCs**, **60 FPS through the game's own Performance mode** (right physics), **each copy has its own `user` folder**, +6% FPS at the Shrine, FSR 3 without black tiles on RX 7000. |
| **0.59.1** | **Far