# GTA: Vice City Stories — Native PC port (PS2 static recompilation)

A native **Windows and Linux** port of **Grand Theft Auto: Vice City Stories** (PS2, USA, SLUS-21590), made by
recompiling the game's PS2 executable into C++. Both are built from the same source and run natively: Direct3D 11 on
Windows, Vulkan on Linux.

**This repository contains no game code or game data.** You need your own copy of the game as an `.iso`.
The build reads the executable from your disc, and the finished game reads everything else from it while it runs.

Status: in development. See [docs/PROGRESS.md](docs/PROGRESS.md) for what works, and [docs/LINUX.md](docs/LINUX.md)
for the Linux build in detail.

## Install on Windows: the launcher (easiest)

1. Download the newest `VCS-Recomp-<version>-windows.zip` from the [Releases](../../releases) page and extract it
   somewhere short and local, like `C:\Games\VCS` (not Program Files, not a OneDrive-synced folder such as Desktop or
   Documents: the build writes thousands of files).
2. Start **`VCSLauncher.exe`** in that folder. It walks you through four steps, one at a time, then shows a big
   **Play** button:
   - **Folder**: the game is built in `build\` next to the launcher, or in a folder you choose (another drive with
     more room, say): *Choose another folder* on this step.
   - **Disc**: it looks for your `.iso` in Downloads, Desktop, Documents and its own folder; otherwise choose it (or
     drag it onto the window, or copy your disc from a DVD drive). It checks that it is the USA release.
   - **Build tools**: the game is compiled on your PC with Microsoft's free C++ tools. If they are missing,
     *Install build tools* runs Microsoft's installer with the right options (about 6 GB; Windows asks for permission).
   - **Build**: recompiles the game from your disc and compiles it, with a progress bar - 20 to 60 minutes the first
     time, a few minutes after an update. Nothing is downloaded during the build: the release brings Python and the
     libraries.
   - **Play**.

The launcher also backs up and restores your saves, makes a desktop shortcut, checks for a new release (only when you
ask, or at start if you turn that on in *Settings*), and zips the logs into a report for bug reports. Windows may warn
that the launcher is from an unknown publisher (it isn't signed): *More info > Run anyway*. How it works:
[docs/LAUNCHER.md](docs/LAUNCHER.md). Everything it does is a script in `tools/` you can also run yourself (below).
If the *Pricedown* font (GTA's lettering, free for personal desktop use from Typodermic) is installed on your PC, the
launcher uses it for its title and Play button; its licence doesn't allow including it, so it isn't.

## Install on Linux: the launcher (easiest)

1. Download the newest `VCS-Recomp-<version>-x86_64.AppImage` from the [Releases](../../releases) page. It runs on
   any 64-bit desktop with glibc 2.35 or newer: Ubuntu 22.04, Debian 12, Linux Mint 21, Fedora, Arch and later, on
   X11 or Wayland. It needs a Vulkan driver (Mesa or NVIDIA's) and `python3`, which every desktop has.
2. Make it executable and start it: in the file manager, *Properties > Permissions > Allow executing as a program*, or
   `chmod +x VCS-Recomp-*.AppImage && ./VCS-Recomp-*.AppImage`. The first start puts the game's files (the source,
   the scripts, the libraries) in `~/.local/share/VCSRecomp/install`, where the game is built, then walks you through
   the same steps as on Windows:
   - **Folder**: where the game is built (another drive with more room: *Choose another folder*).
   - **Disc**: your `.iso` from Downloads, Desktop or Documents, chosen, or dropped onto the window.
   - **Build tools**: the compiler (clang 19 or newer) and the libraries the build needs, from your distribution.
     *Install packages* asks for your password and installs them; *Install in a terminal* shows the command instead.
     On Ubuntu 22.04 and Debian 12, whose clang is older, it adds LLVM's own repository ([apt.llvm.org](https://apt.llvm.org)) first.
   - **Build**, then **Play**.

The AppImage is the whole launcher: *Add a shortcut to the desktop* in *Settings* puts it in your applications menu
too. Updates replace the AppImage itself (*Settings > Check now*); the next start puts the new files in place and only
what changed is rebuilt. Without FUSE (some containers and minimal systems), start it with
`--appimage-extract-and-run`.

## Install by hand (Windows and Linux)

The release zip contains the full source: the steps below work in it too, and in a git clone.

### 1. Install the tools (once)

**Windows**
- **Python 3**: [python.org](https://www.python.org/downloads/). During setup, tick *Add python.exe to PATH*.
- **Git**: [git-scm.com](https://git-scm.com/download/win) (the default options are fine). The first build uses it
  to download the libraries the game needs (SDL3, FFmpeg, ...), so it also needs an internet connection.

That's all: there's no compiler to install. The 