
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
- Full per-controller button mapping
- Volume, instant mute, and the music ducking toggle

Everything you change is saved to `Config.toml` on the spot and restored next launch.

**Real controller support.** 
Controllers are fed to the game as a GameCube controller.
The port does NOT pretend to be a Wii Remote or Classic Controller.
Mappings are positional (`south`, `east`, `west`, `north`) rather than Xbox-labelled, so the
same config makes sense on Xbox, PlayStation, Nintendo and generic SDL pads alike, and extra
inputs like paddles, touchpads and share buttons show up when the hardware reports them.
The official Wii U / Switch GameCube adapter (WUP-028) works too; as with Dolphin, on Windows the
adapter must be switched to the WinUSB driver once (Zadig).

## Requirements

- Windows 10 or 11, 64-bit
- GPU: GTX 1650 / RX 6400 / Arc A310 or higher
- CPU: Intel Core i5-8400 / AMD Ryzen 5 2600 (4c/6c, ~3.5GHz+) or higher
- About 20 GB of free disk space during installation (Final game size ~5 GB)
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
> Only take builds from this repository's
> [Releases](https://github.com/patchzyy/Wiicompiled/releases) page. If someone's sharing an
> installer through Discord or some random download site, don't touch it!!

## A note on related projects

WiiCompiled, Wheel Wizard, Retro rewind and other related projects are developed
**independently** and each has its **own** contribution rules and all have their own
rules. What applies here does not automatically apply there,
and vice versa. Check each project's own CONTRIBUTING and README files.

## Retro Rewind

[Retro Rewind](https://wiki.tockdom.com/wiki/Retro_Rewind), ZPL's Mario Kart Wii mod distribution,
can be built as its **own static profile**: instead of applying `Code.pul` as runtime patches,
the Kamek/Pulsar code is statically translated together with the base game into a separate native
executable.

Wheel Wizard drives this too.

## Building from source

Owning the game is still required even if you compile everything yourself.

You'll need: .NET 8 SDK, CMake, Ninja, and LLVM/Clang (the shipped build uses LLVM-MinGW targeting
`x86-64-v3`).

Build the translator:

```powershell
dotnet build translator/Translator.sln -c Release
```

The default test suite needs no binaries and no host C++ compiler, so you can hack on the
translator wi