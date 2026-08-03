# The Simpsons Game — Recompiled 🍩

A fan-made **static recompilation** of *The Simpsons Game* (Xbox 360, 2007) to a native
executable — the original game code, translated ahead-of-time from Xenon PowerPC to your CPU,
running against a Xenia-derived GPU/kernel emulation layer.

> **You must own the game.** This repository contains **no game assets, no ISO, and no
> copyrighted content**. The included launcher installs the game from *your own* legally-owned
> Xbox 360 ISO and even generates its artwork from *your* copy's cutscene files. See
> [Legal & disclaimers](#legal--disclaimers) below.

## Download & Play

The easiest way to play — no build tools required:

1. Grab the latest release for your OS from the
   [Releases page](https://github.com/YesterMester/TheSimpsonsGameRecomp/releases).
2. Extract the zip anywhere.
3. **Linux/Steam Deck:** run `Play.sh` at the top of the extracted folder.
   **Windows:** run `simpsons-launcher.exe` at the top of the extracted folder — it's a
   standalone app, no Python install required.
4. In the launcher's **Install** tab, point it at your own Simpsons Game Xbox 360 ISO. It
   extracts and installs the game data for you.
5. Hit **Play**.

The launcher checks for and installs new releases itself (About tab → Check for updates), so
you don't need to manually re-download after the first time.

> **Steam Deck players:** read the pop-in-patch warning in the launcher's Patches tab before
> touching the "Instant character pop-in" toggle — it's known to hang the GPU on Steam Deck's
> hardware, on both SteamOS and Windows. See [Known issues](#known-issues).

## Status

| Platform | State |
|---|---|
| Linux / Steam Deck | ✅ Playable (menus, saves, videos, gameplay) |
| Windows | ✅ Builds & boots to gameplay (clang + D3D12) — first bring-up, expect rough edges. So far only actually tested on a Steam Deck's Windows dual-boot partition (Van Gogh APU); not yet verified on a general desktop PC / discrete GPU. |
| Android | 🗺 Planned |

Input: controller required for now — experimental keyboard/mouse emulation can be enabled in
the launcher (Settings → Input).

## Requirements

- **Your own legally-owned Xbox 360 copy of The Simpsons Game**, as an ISO you supply yourself.
  Primarily tested against the USA release (title ID `45410809`); the EUR release has also been
  confirmed to boot and play, though it's had less overall testing.
- **~5 GB free disk space** for the extracted game data (movies, audio, levels — roughly 4 GB
  once extracted), on top of the launcher/engine download itself.
- A GPU with reasonably current Vulkan (Linux) or D3D12 (Windows) driver support. Integrated/APU
  graphics (Steam Deck included) work, see the pop-in patch caveat below for the one known
  exception.
- A controller is currently required for gameplay (see above).

## Known issues

- **Missing characters ("eternal pop-in") — largely fixed by default.** The game marks the
  vertex streams of streamed meshes "invalid" while they load, and additionally leaves the
  *optional* blend-shape streams of many finished character meshes permanently marked invalid.
  The engine used to throw away any draw touching an invalid stream, which is why characters
  could stay invisible indefinitely. It now tells the two cases apart: meshes whose only
  "invalid" streams are those absent optional ones (which their shaders provably never read)
  are drawn normally, by default, on every platform (`gpu_allow_null_optional_streams`).
  Entities genuinely mid-stream still appear a moment later — that's real loading. If you still
  see long-lasting invisible characters, grab the log and open an issue; the old Level-1
  camera-into-wall workaround should no longer be necessary.
- **"Instant character pop-in" patch is dangerous on Steam Deck's GPU.** On top of the default
  fix above, the community's full fix (`gpu_allow_invalid_fetch_constants`, launcher Patches
  tab) also runs the game's stale-descriptor streaming "priming" draws — but on Steam Deck's
  AMD APU it has crashed on level loads, on **both** Linux/Vulkan (RADV) *and* Windows/D3D12:
  on Windows it triggers a kernel **BSOD** (`PAGE_FAULT_IN_NONPAGED_AREA`, bugcheck `0x50`) in
  the AMD driver. The same crash on two independent driver stacks points at the Van Gogh APU
  itself. Those priming draws now run with rasterization disabled entirely (they only exist to
  feed the game's vertex-readback streaming), which is expected to remove the crash trigger,
  but this hasn't been re-verified on Deck hardware yet. **Leave it off on Steam Deck** unless
  you're specifically testing it.
- **Windows saves moved to the right place.** Saves and the shader cache used to be written to
  your **Documents** folder, which is wrong for Windows and breaks badly when Documents is
  redirected into OneDrive. They now live in `%LOCALAPPDATA%\simpsons` (the local app data
  folder). If you already had saves in Documents, the engine moves them across automatically
  the first time you