<p align="center">
  <img src="docs/images/logo.png" alt="CTR Nitro-Fueled PC" width="360">
</p>

# CTR-NitroFueled-PC

**Crash Team Racing: Nitro-Fueled (PS4, CUSA13795 v1.21) running natively on Windows 10/11.**

This is a Windows fork of [SacredFire](https://github.com/T3CHNOLOG1C/SacredFire), the native
Linux port of the game by T3CHNOLOG1C. The game's own x86-64 code runs directly on the CPU, a
small runtime replaces the PS4 system libraries, and a renderer derived from shadPS4 translates
the PS4 GPU work to Vulkan. This fork adds the Windows layer (loader, memory, TLS, exceptions,
files, timers) from Supermedo's Windows port of bbport, plus the fixes SacredFire needed on top
of it: see [packaging/windows/README.md](packaging/windows/README.md).

> **No game files are included.** You need your own dump of the game and its 1.21 update.
> Both builds of the 1.21 update work: the one for firmware 5.05 (the reference) and the one for
> 6.72+ (since v0.2.1).
> Not affiliated with or endorsed by Sony Interactive Entertainment, Activision or Beenox.
> *Crash Team Racing*, *Nitro-Fueled* and *PlayStation* are trademarks of their owners, named
> here only to identify the game this software runs.

**Status on Windows: playable.** Menus, Adventure and Arcade, races, sound, cutscenes, Xbox/SDL
controllers and keyboard, saving, the community patches (60 FPS, no motion blur), restart from
the in-game menu, and the game's DLC from your own packages (optional). Internal resolution from
480p to native 4K, with AMD FSR 1 or temporal upscaling (AMD FSR 3.1, or NVIDIA DLSS on RTX
cards; experimental). Tested on
Windows 11 24H2 with an NVIDIA RTX 3070 and an Intel i5-9500: 110-130 FPS uncapped in races with
the 60 FPS patch (the FPS limit keeps it at 60 by default; up to 240). Shaders seen for the first
time cause short stalls; they are cached and load at start from the next session on, or compile
in the background with the experimental switch.

| Release | What it brought |
|---|---|
| [v0.4](https://github.com/GetLostIn/CTR-NitroFueled-PC/releases/tag/v0.4) | Redesigned launcher with a *Controls* tab (live controller test and rumble, players 1-4, gamepad buttons remapped by pressing them, stick dead zone; the keyboard page moves there); *Achievements*: trophies kept when unlocked, a launcher-style notice in the game (picture, name, grade, what it was for) and a tab with all 48 (picture, name, what to do, progress and dates); the in-game menu restyled in tabs, in Spanish or English; game languages per edition; AMD FSR 4 (experimental) in the *Upscaling* list; *Frame generation* (AMD FSR 3, experimental): an interpolated frame between each pair of game frames; *Aspect ratio* 16:9, 21:9 UltraWide or 32:9 Super UltraWide with centered HUD (by tcosi, in Settings > Display, not Patches); the European edition CUSA14876 (by martijnhe), ultrawide included; the game's 2x MSAA as a setting, off by default (fixes dotted sky lines); CPUs without MOVBE/BMI1/LZCNT (by MetaHeart); damaged dumps reported (by Naif Alqurashi); rare libwinpthread crashes fixed; FSR 3 no longer turns off without Resizable BAR |
| [v0.3](https://github.com/GetLostIn/CTR-NitroFueled-PC/releases/tag/v0.3) | Internal resolution 480p to native 4K (the game's own render scale; replaces the PS4 Pro switch); one *Upscaling* list: AMD FSR 1, AMD FSR 3.1 or NVIDIA DLSS (temporal, experimental) with DLSS quality modes, output and model (Transformer/CNN); game languages of this build (English, Latin American Spanish, French, Brazilian Portuguese); PS4 PKG Tool dumps (Image0 + Sc0); fullscreen switch in game fixed |
| [v0.2.1](https://github.com/GetLostIn/CTR-NitroFueled-PC/releases/tag/v0.2.1) | The 1.21 update built for firmware 6.72+ is accepted (patches found by signature); keyboard page in the launcher to rebind keys |
| [v0.2.0](https://github.com/GetLostIn/CTR-NitroFueled-PC/releases/tag/v0.2.0) | Launcher (`CTR-NitroFueled-PC.exe`): game setup with hard-link merge, settings, patches, save backups and imports, optional DLC; bundled Python; the project's icon |
| [v0.1.1](https://github.com/GetLostIn/CTR-NitroFueled-PC/releases/tag/v0.1.1) | First portable build: FPS limit up to 240, fullscreen switch, licenses in the package |

### Quick start (Windows)

**Easiest: the portable build.** Download `CTR-NitroFueled-PC-portable-windows.zip` from
[Releases](https://github.com/GetLostIn/CTR-NitroFueled-PC/releases), unzip it anywhere and open
**`CTR-NitroFueled-PC.exe`**, the launcher: choose your `CUSA13795` (base game) and
`CUSA13795-patch` (update 1.21) folders, press *Prepare the game* once (it merges them with hard
links, no extra disk space) and then *Play*. Python is bundled; you only need a Vulkan 1.3 GPU.

**Picture** (launcher: Settings > Display; in game: Insert):

- *Internal resolution*: the size the game draws its 3D scene at. 480p and 720p for modest PCs;
  1440p to 2160p output a 4K picture, which also smooths edges on a 1080p screen. Needs a restart
  (