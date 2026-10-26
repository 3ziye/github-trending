# DriveClub Recomp

**DriveClub for PS4 (version 1.28), running natively on Windows.**

<img width="1920" height="1080" alt="s009 20" src="https://github.com/user-attachments/assets/4c0fe155-eae9-4c78-aa24-4a5b154e2b9f" />

The source code is in this repository and the build is on the [Releases](../../releases) page.

## Join our Discord community: https://discord.gg/62b8jceumR

## Planned for the next major release
- **DLSS/FSR Frame Generation, DLSS up to 4X, FSR up to 2X**
- **DLSS Neural Rendering (Standard and Optimised model support)**
- **Further performance and stability improvements**

## New in 0.3.0
- **DLSS and FSR upscaling.** Pick the Output size and a mode from Quality to Ultra Performance: the game renders smaller and DLSS (GeForce RTX) or FSR 3.1 (any card) brings the picture to the output, with a Sharpness slider. Shadows no longer flicker while upscaling, and it works in car selection and the pre-race flyovers.
- **HDR10 output** on HDR displays, with a brightness control (Page Up / Page Down in the game).
- **Steering wheels, rewritten.** Force feedback from a physics model of the front tyres or a software model, live tuning in the FFB Tuner, pedals on their own USB device, Fanatec style wheels that show up as two controllers, a handbrake on its own USB or on a button, a Driving tab with assists, and a field of view you can change while playing (F5 / F6).
- **Faster.** A two-thread draw path is on by default, with far less processor work per draw. Cars load faster in car selection and menus no longer hitch on missing game files.

## New in 0.2.0: DLSS and FSR anti-aliasing
The game's own anti-aliasing is replaced by a modern one, chosen in the launcher:
- **NVIDIA DLAA** (GeForce RTX) for the sharpest, steadiest picture: thin lines, wires, fences and foliage stay clean.
- **AMD FSR 3.1** on any graphics card, with no special hardware and nothing extra to install.

Both use the game's own camera motion. In the game the overlay shows what is active, **F9** switches the new anti-aliasing off and on to compare, and **F10** switches between FSR and DLSS on RTX cards.

**Upscaling** (launcher, next to Anti-aliasing): the game draws at a lower resolution and DLSS or FSR rebuilds the picture at the full output size, after the game's own effects, so it stays sharp. At 5120x1440 on an RTX 4070 Ti the average went from 48 FPS (DLAA) to 80 (DLSS Quality), 88 (Balanced) and 104 (Performance); FSR 3.1 Quality gave 103 (DLSS's transformer model costs about 3 ms a frame there, for a cleaner picture). It works with every output and widescreen size; the render size follows from it. **Sharpness** sharpens the finished picture (AMD's RCAS, also after DLSS, which no longer sharpens by itself).

## How to play
1. Download the latest `driveclub-recomp-<version>-win64.zip` from the [Releases](../../releases) page and extract it anywhere you can write to (not `Program Files`).
2. Have **your own** game dumps ready:
   - the **version 1.28 update** folder (it contains `eboot.bin`)
   - the **base game** folder (it contains `game000.dat`)
3. Double-click `DriveClub.exe`, press **Browse** next to each folder, check the settings and press **Play**.

Nothing to install. Your own files are never modified or copied, and the folders you chose are remembered.

Logs are in the `logs` folder.

## Highlights
- The game's own x86-64 code runs directly on your CPU, with no CPU emulation. The PS4 system libraries are reimplemented and the GPU commands are translated to Vulkan, similar to Wine and DXVK
- Playable from the menus through races, photo mode and saves
- About 60 FPS at 4K in the heaviest scenes on our test PC (RTX 5070 Ti, Ryzen 7 5800X3D), higher in lighter ones, with an unlocked frame rate option in the launcher that keeps the game at its normal speed
- Runs on NVIDIA, AMD and Intel graphics through Vulkan, with Resizable BAR used automatically where the driver allows it
- Keyboard racing layout and any gamepad (Xbox, PlayStation, Switch Pro, 8BitDo)
- Steering wheels with force feedback from the car's tyre physics, pedals with clutch, an H-pattern shifter and a USB handbrake
- DLC content (add-on cars, bikes, tours and livery decals) can be unlocked from the launcher, built from your own game files. Cars you earn by playing still unlock through normal progression
- A launcher window that resizes from every edge and corner and stays sharp at any display scale
- A `mods` folder for loose-file mods: files in it replace the game's own files of the same path

## Controls
Any gamepad works. Keyboard, mouse and gamepad can be used at the same time.

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

F5 and F6 narrow and wid