
# WiiCompiled

A native PC port of Mario Kart Wii, made with static recompilation.

There's no emulator in the loop, no interpreter, no JIT, no PowerPC
anywhere at runtime.

> [!IMPORTANT]
> There is no Nintendo code, no assets and no game data anywhere in this project or its releases.
> You need your own legally dumped copy of the PAL version of the game. Setup only ships the
> toolchain, the translation runs on your machine against your disc image, and nothing ever gets
> uploaded.

[What is a github, I just want to play](https://github.com/TeamWheelWizard/WheelWizard/releases/latest)

---

## What it does

**Unlocked framerate with interpolation.** 
The original game is hard-locked to 60 fps. The runtime can generate interpolated frames in between, so on a
120/144 Hz monitor things genuinely look smoother.

> [!WARNING]
> Interpolation is experimental right now and will show artifacts in specific scenarios.

**Any aspect ratio you want.** 
Drag the window bigger, wider, whatever, the camera adjusts
live.

**Native rendering via aurora.** 
The graphics layer is built on
[aurora](https://github.com/encounter/aurora). Aurora is a source-level GameCube & Wii compatibility layer.

**High internal resolution.** 
Play at several times the console's resolution.

**Music ducking.** 
Start playing something else, Spotify, a YouTube video, and
the game automatically mutes its own music until the other audio stops. Optional, if you'd
rather it didn't. All audio that shows in your display media controls on your windows pc fall under this.

**An in-game settings bar.** 
Press **F10** while the game window has focus:
- Internal resolution
- FPS counter
- Controller assignment for all four ports
- Full per-controller button mapping, including the bumpers
- Dolphin-syntax input expressions and GCPadNew.ini import
- Controller vibration on/off
- Volume, instant mute, and the music ducking toggle

Everything you change is saved to `Config.toml` on the spot and restored next launch.

**Real controller support.** 
Controllers are fed to the game as a GameCube controller.
Mappings are positional (`south`, `east`, `west`, `north`) rather than Xbox-labelled, so the
same config makes sense on Xbox, PlayStation, Nintendo and generic SDL pads alike, and extra
inputs like paddles, touchpads and share buttons show up when the hardware reports them.

**Dolphin-compatible input expressions.** 
Each GameCube control can carry an expression in Dolphin's input syntax, with the same operators
and the same functions.
A Dolphin `GCPadNew.ini` can be imported directly from the F10 bar.

**Vibration toggle.** 
Force feedback can be turned off for every port at once.
The official Wii U / Switch GameCube adapter (WUP-028) works too; as with Dolphin, on Windows the
adapter must be switched to the WinUSB driver once (Zadig).

**Real Wii Remotes over Bluetooth.**
Pair a Wii Remote with Windows (Settings > Bluetooth > Add device, press 1+2 or SYNC, leave the
PIN empty)

Known limitations of the Wii Remote path:
- No IR pointer yet: menus are navigated with the D-pad and A (the game treats the remote as
  pointing away from the screen).
- Battery level is not reported to the game and the remote's speaker is not implemented.
- Only the Wii Remote's own accelerometer is calibrated; the Nunchuk's uses SDL's fixed zero point.
- The Classic Controller's L/R triggers reach the game as digital (full pull on click): SDL does not
  expose their analog travel.
- Turn the Wii Remote support off in that menu if you use a Mayflash DolphinBar, which already
  presents the remote as a regular gamepad.

## Requirements

- Windows 10 or 11, 64-bit
- GPU: GTX 1650 / RX 6400 / Arc A310 or higher
- CPU: Intel Core i5-8400 / AMD Ryzen 5 2600 (4c/6c, ~3.5GHz+) or higher
- About 20 GB of free disk space during installation (Final game size ~5 GB)
- macOS 14 (Sonoma) or later on Apple Silicon
- On macOS, Apple Xcode Command Line Tools (Setup opens Apple's installer when they are missing)
- A clean, unmodified **PAL `RMCP01`** disc image of Mario Kart Wii, dumped by you. ISO, GCM,
  GCZ, CISO, WBFS, WIA and RVZ are accepted.

> [!NOTE]
> GPU/CPU minimums are set by driver support and D3D12/Vulkan feature requirements, not by the game's actual demands.

Only the clean PAL revision will work. Anything else (other
regions, patched executables) is rejected outright.

> [!NOTE]
> Nobody here will tell you where to get the game. Dumping your own disc is on you, and links to
> game files won't be provided or tolerated.

## Installing

For an easy experience, use [Wheel Wizard](https://github.com/TeamWheelWizard/WheelWizard). Pick your clean PAL `RMCP01`
image under Settings, turn on **WiiCompiled (beta)**, and hit install from the Home page.
Wheel Wizard downloads the setup tool from this repo and walks you through install, updates and
launching. The backend itself is deliberately command-line only, Wheel Wizard is a wrapper around it.


> [!CAUTION]
> Only take builds from this 