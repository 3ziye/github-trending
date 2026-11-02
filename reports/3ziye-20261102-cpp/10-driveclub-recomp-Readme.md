# DriveClub Recomp

**DriveClub for PS4 (version 1.28), running natively on Windows and Linux.**

<img width="1920" height="1080" alt="s009 20" src="https://github.com/user-attachments/assets/4c0fe155-eae9-4c78-aa24-4a5b154e2b9f" />

The source code is in this repository and the build is on the [Releases](../../releases) page.

## Join our Discord community: https://discord.gg/62b8jceumR

## Planned for the next major release
- **DLSS/FSR Frame Generation, DLSS up to 4X, FSR up to 2X**
- **Public online lobby** (being tested on our Discord first)
- **Further performance and stability improvements**

## How to play
1. Download the latest `driveclub-recomp-<version>-win64.zip` from the [Releases](../../releases) page and extract it anywhere you can write to (not `Program Files`).
2. Have **your own** game dumps ready:
   - the **version 1.28 update** folder (it contains `eboot.bin`)
   - the **base game** folder (it contains `game000.dat`)
3. Double-click `DriveClub.exe`, press **Browse** next to each folder, check the settings and press **Play**.

Nothing to install. Your own files are never modified or copied, and the folders you chose are remembered.

Logs are in the `logs` folder.

### Linux (x86_64)
The AppImage is built by the [AppImage workflow](.github/workflows/appimage.yml), or locally with
`bash packaging/appimage/build-appimage.sh <version>` (see [BUILDING.md](BUILDING.md#linux-x86_64)).
It uses the same game dumps and keeps its settings, prepared image, saves and logs in a
`data/` folder beside the AppImage whenever that folder is writable (otherwise in
`~/.local/share/driveclub-recomp`). Running the AppImage opens the native Linux launcher, with
the same game folders, display, driving and patch settings as the Windows launcher. Press
PLAY there and the recomp prepares and starts; `--play` starts it headlessly with the saved
settings. Use DATA FOLDER > Change... in the launcher to select another folder or move the
existing data. Put `update/` and `base/` next to the AppImage, use `--setup UPDATE BASE` once,
or set `DRIVECLUB_UPDATE_DIR` and `DRIVECLUB_BASE_DIR`. The choice is stored in `data-path`
beside the AppImage; `DRIVECLUB_DATA_DIR` overrides it, and a `portable` marker selects `data/`
when no folder has been chosen.

## Highlights
- The game's own x86-64 code runs directly on your CPU, with no CPU emulation. The PS4 system libraries are reimplemented and the GPU commands are translated to Vulkan, similar to Wine and DXVK
- Playable from the menus through races, photo mode and saves, with trophies and multiplayer: private sessions with friends, and a public lobby that is being tested on our Discord
- About 60 FPS at 4K in the heaviest scenes on our test PC (RTX 5070 Ti, Ryzen 7 5800X3D), higher in lighter ones, with an unlocked frame rate option in the launcher that keeps the game at its normal speed
- Runs on NVIDIA, AMD and Intel graphics through Vulkan, with Resizable BAR used automatically where the driver allows it
- Keyboard racing layout and any gamepad (Xbox, PlayStation, Switch Pro, 8BitDo)
- Steering wheels with force feedback from the car's tyre physics, pedals with clutch, an H-pattern shifter and a USB handbrake
- DLC content (add-on cars, bikes, tours and livery decals) can be unlocked from the launcher, built from your own game files. Cars you earn by playing still unlock through normal progression
- A launcher window that resizes from every edge and corner and stays sharp at any display scale
- A `mods` folder for loose-file mods: files in it replace the game's own files of the same path

## Controls
Any gamepad works. Keyboard, mouse and gamepad can be used at the same time.

### Controller button prompts
Button prompt icons can be configured in the launcher under **Driving > Controller buttons** (or via `button_prompts`, `xbox_buttons`, and `playstation_buttons` in `driveclub.ini`):
- **Prompts**: `Auto` (automatically follows the controller in use, and shows key caps when you play with the keyboard), `PlayStation`, or `Xbox`.
- **Xbox buttons**: `Xbox One` (modern flat A/B/X/Y buttons with View icon) or `Xbox 360` (glossy gem buttons with Back pill).
- **PlayStation buttons**: `PS4` (the game's original symbols) or `PS5` (DualSense-style icons).

| Action | Keyboard |
|---|---|
| Accelerate | W |
| Brake / reverse | S |
| Steer | A / D |
| Handbrake | Space |
| Shift down / up | Q / E |
| Change camera | C |
| Touchpad left / right half | R / T (R is Reset to Track) |
| Accept | Enter / Z |
| Back | Backspace |
| Pause | Esc / P |
| D-pad | Arrow keys |
| Look around | I J K L or the mouse |

F2 shows how far the clutch, brake and throttle are pressed, as bars with their percentage in the bottom left corner (a pedal at full travel is drawn bright and outlined; without a wheel it shows the gamepad's triggers). The launcher's "Show pedal inputs" turns it on at startup. Page Up and Page Down make the picture brighter or darker (the launcher's Picture card has the same bright