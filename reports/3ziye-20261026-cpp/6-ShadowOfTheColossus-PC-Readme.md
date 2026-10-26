# Shadow of the Colossus — PC native port · v0.60.6

[Releases](../../releases) · [Changelog](CHANGELOG.md)

> **No game or Sony files are included.** You need your own game dump and, for sound, two
> modules from your own console. This project is not affiliated with Sony Interactive
> Entertainment or Bluepoint Games.

---

**Status: the game can be finished from start to end** (v0.60.3: played through the last
colossus, the ending and the credits, with high quality textures, PS4 Pro mode and 60 FPS on).

A native Windows port of the PS4 **Shadow of the Colossus** (Bluepoint, 2018; CUSA08809, EU 1.01)
for **Windows 10/11**. The game's own x86-64 code runs directly on the PC's CPU and the PS4 GPU
is translated to Vulkan. It is not a full emulator: it is a loader with the system functions the
game needs, in the style of [bloodborne_pc](https://github.com/Supermedo/bloodborne_pc).

### What's new

| Version | Improvements and fixes |
|---|---|
| **0.60.6** | **No more rainbow garbage on textures and far fewer "closed out of nowhere" crashes** (the cause: speculative GPU readbacks written over memory the game had reused, after loading a save or a new area), **no more black dots on sandy ground**, **in-game menu cleaned up** (FPS, upscaler and sharpening now change at once; Bloodborne leftovers removed), **hard disk read-ahead** (fewer stalls in new areas on HDDs), textures refreshed on every load, a readable session event log (`user/events.log`). |
| **0.60.5** | **Texture quality selector: Off / High / Maximum** (#235: sharp again), **memory leak fixed** (~60 MB/min, long-session stutter), **+3% average and +12% minimum FPS** (descriptor binds reused), **loading after a GPU driver update: 106 s → 7 s**, possible fix for **white characters on AMD GCN** (RX 470–590, Vega), **4-thread CPUs** no longer stuck loading, a hang watchdog, short hitches no longer flash a black loading screen, code review fixes. |
| **0.60.4** | **No more cyan blocks on stone or blinking flowers** with high quality textures (the 0.60.3 crash protection switched the texture detail every second or two; now with hysteresis). |
| **0.60.3** | **The game can be finished from start to end** (played from the last colossus through the ending and credits): fix for the high quality textures crash in wide views (#186), fix for the crash on the load after the credits, +2.7% FPS at the Shrine. |
| **0.60.2** | **Quick settings in the in-game menu** (60 FPS, frame generation, high quality textures, far shadows, volume: apply at once and are kept), **the mouse works in the menu**, **animated loading screen while the shaders are prepared** at start. |
| **0.60.1** | **In-game menu** (Insert / F1 / L3+R3: FPS, GPU and VRAM, fullscreen, resolution, sharpening, mouse camera, effects), **Bloodborne leftovers removed** (~11,700 lines), the game exe has the SotC icon. |
| **0.60** | **Textures on GTX 10xx**, no title-screen hang, **starts on low-memory PCs**, **60 FPS through the game's own Performance mode** (right physics), **each copy has its own `user` folder**, +6% FPS at the Shrine, FSR 3 without black tiles on RX 7000. |
| **0.59.1** | **Far shadows no longer blink** (AMD and NVIDIA; new launcher option), **AMD stripes** on shadows and water fixed, Intel fixes, the log shows the GPU and driver. |
| **0.59** | **More FPS** (Oussama268's fork: draw thread, shaders translated in parallel; bridge 30 → 37–40 FPS), **fix for the ending and save-load crash** (still being tested: report in the issues), **F11 fullscreen**, **video memory use** and **volume** options, launcher **self-update**, ultrawide with PS4 Pro mode, fixes for 6 GB cards and Chinese Windows. |
| **0.58.1** | **High quality textures** (sharp leaves and rocks; the game had not streamed its high resolution versions since 0.0.13) and the **game window's own icon** (or the game's, or a picture of yours). |
| **0.58** | **Community release** (Lucas-blip-png, Gabriell-os, Oussama268, jownatan, xeodeo, nakaionyt/y7ngboy, tabnul): **fewer crashes** (out of video memory, game freezing, post-colossus crash in PS4 Pro mode), **+15% FPS** and less video memory, AMD fixes (RDNA3/4 black tiles), **21:9/32:9 widescreen**, **FPS 30/60/unlimited**, **Xbox button icons**, FSR 3 / DLSS-G frame generation (experimental), launcher in Spanish, Chinese, Korean and Russian. |
| **0.57** | **AMD cards:** fix for the green/pink fog and characters (AMD now uses the NVIDIA 32-lane path; diagnosis from issue #7, not yet tested on an AMD card). **New launcher option** to turn off direct memory access: ~10% more FPS, flatter distant water. |
| **0.56** | **Open-world water with waves:** lakes and rivers below the waterfalls are no longer flat as a mirror (a shader instruction, `S_WQM_B64`, was ignored). **The upper lake ripples and reflects far away** (direct memory access on by default, as in Pink-shadPS4). Distant trees without "colored garbage". |
| **0.0.13** | **No more crashes:** fixed the 0.0.12 crash in the intro