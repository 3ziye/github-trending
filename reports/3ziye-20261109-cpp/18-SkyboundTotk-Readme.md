# SkyboundTOTK

SkyboundTOTK is an experimental native static recompilation project for *The Legend of Zelda: Tears of the Kingdom*, **base game version 1.0.0**. It targets Windows x64 and Linux x86_64. It is not affiliated with Nintendo. Expect graphical problems and incomplete compatibility; a successful build does not guarantee a complete playthrough.

The project's AArch64 game code is translated ahead of time into C and compiled locally into a native executable. A runtime implements the services the game expects, and the renderer translates its graphics work and shaders for WebGPU. This is a game-specific port, not a general-purpose Switch emulator. Some graphics translation still happens at runtime.

## Game files and distribution

You must supply your own legally obtained, already-extracted, **unmodified 1.0.0 base-game ExeFS and RomFS**. No game files, generated game code, keys, firmware or saves are included in this source project. The build does not extract NSP or XCI files. Version 1.2.1 also builds from its own ExeFS and the RomFS with the update applied (PR #19, contributed and tested by keno80: the build picks the hooks by the main module's build id); everything else in this README was tested on 1.0.0, and other updates are not supported by the game-specific hooks.

Keep your game files, generated code, executable package and saves private. The `game/`, `build/` and `dist/` directories are Git-ignored, but check what you are publishing rather than relying on ignore rules alone. The generated standalone package contains copyrighted game-derived data and must not be shared or committed.

## Build on Windows

### Requirements

- Windows 10/11 x64 and a GPU and driver supported by wgpu-native. Allow **at least 45 GB free in addition to the original game dump** for intermediate files and the separate packaged RomFS; the build is CPU- and memory-intensive. It runs as many compiles at once as fit in 80% of your RAM at 3.5 GB each (three on a 16 GB PC); set `RX_JOBS=<n>` to choose.
- Python 3.10 or newer on PATH, with `lz4` installed: `python -m pip install lz4`.
- Visual Studio 2022 Build Tools with the MSVC C++ tools and Windows SDK. Use an **x64 Native Tools Command Prompt** so the compiler can find the Windows headers and libraries.
- Clang, clang++ and lld. The build previously used emsdk 6.0.9: install it separately and set `EMSDK` to its directory (the lookup defaults to `C:\emsdk`), or put these LLVM tools on PATH. The build script does not download compilers or Python packages.

### Prepare and build

1. Put the extracted files in the project's `game` folder. The paths must look like this, not `game/exefs/exefs/main` or `game/romfs/romfs/Event`:

   ```text
   SkyboundTOTK/
     build.bat
     game/
       exefs/
         main
         main.npdm
         rtld
         sdk
         ...
       romfs/
         ActorSystem/
         Event/
         ...
   ```

2. Open an **x64 Native Tools Command Prompt**, change to the SkyboundTOTK directory and run `build.bat`. The launcher pauses at the end so you can read any errors.
3. The script checks the `main` and `sdk` module build IDs and a few RomFS directories, lifts the game code, compiles the native executable and copies the runtime and RomFS into `dist/SkyboundTOTK/`. The checks do **not** verify the entire RomFS or guarantee that a dump is complete.
4. Open `dist/SkyboundTOTK/SkyboundTOTK.exe` to run it. No command-line arguments are needed. Keep `image.bin`, `image.json`, `romfs/`, `wgpu_native.dll` and `SDL2.dll` alongside the executable. The standalone folder can be moved as a unit and does not need the original `game/` folder to launch.

The first lift and compile can take a long time. The builder reuses a completed lift only when its recorded game and lifter inputs match. If the lift was interrupted or those inputs change, move the existing `build/` directory aside before retrying. The script refuses to overwrite a nonempty `dist/SkyboundTOTK/`: move the existing package aside before a new build. Copy its `user/` folder into the new package if you want to retain its saves and settings. Do not delete your only save backup.

The package normally creates its own `user/` directory beside the executable; it does not automatically use the saves from another installation. Native renderer pipeline cache data is kept in `rxcache/` beside the executable. The executable also accepts an image path and `--romfs` / `--user` overrides for advanced use, but they are not needed for normal launching.

### Build and launch troubleshooting

- **Python or `lz4` missing:** install them for the Python on PATH, then reopen the tools prompt. Run `python -m pip install lz4` with that same Python.
- **Compiler, headers or libraries missing:** open the x64 Native Tools prompt and check that the C++ tools, Windows SDK, Clang, clang++ and lld are installed and discoverable. Set `EMSDK` if the LLVM tools are in a non-default emsdk directory.
- **Wrong module or missing R