# SonShell - an effort to "ssh into my Sony camera"

A Linux-only helper built on Sony’s official **Camera Remote SDK**. It connects to supported Sony bodies (the full SDK model list is recognised) over Wi-Fi or Ethernet, mirrors new captures straight to your workstation, and drops you into an interactive shell for remote control.

The shell can download files automatically, trigger the shutter, tweak exposure settings, start live view, run post-download hooks, and keep retrying if the camera drops offline. Everything runs from a single terminal window.

---

## Demo

https://github.com/user-attachments/assets/6146ff3b-d51c-412b-8684-bdde5c418d4d

---

## Quick Start

### Requirements
- Linux (developed on Ubuntu 24.04) with a C++17 toolchain (`gcc`, `g++`, `cmake`, `make`).
- Sony Camera Remote SDK v2.00.00 (download it from Sony and extract it somewhere convenient).
- Python 3 for the small header-generation scripts.
- `pkg-config` (or `pkgconf`) so CMake can locate GTK when linking Sony’s OpenCV bundle (omit when configuring with `-DSONSHELL_HEADLESS=ON`).
- Runtime deps: libedit, ncurses, libudev, libxml2, OpenCV 4.8 (bundled inside Sony’s SDK).

On Ubuntu/Debian you can grab the basics with:
```bash
sudo apt install autoconf libtool libudev-dev gcc g++ make cmake unzip libxml2-dev libedit-dev python3 pkg-config
```

### Build in a hurry
1. Download and extract the Sony Camera Remote SDK v2.00.00, then configure CMake while pointing `SONY_SDK_DIR` at the folder that contains `app/`:
   ```bash
   cmake -S . -B build -DSONY_SDK_DIR="$HOME/SonySDK/CrSDK_v2.00.00_20250805a_Linux64PC"
   ```
2. Compile and copy the required Sony/OpenCV shared libraries next to the binary:
   ```bash
   cmake --build build --config Release
   ```
3. Run it (start with enumeration and let SonShell pick the download folder):
   ```bash
   ./build/sonshell --dir "$PWD/photos" --keepalive 3000
   ```

### Headless builds

If you are compiling on a machine without a GUI stack, pass `-DSONSHELL_HEADLESS=ON` to the CMake configure step. This skips the OpenCV/GTK dependencies and disables the live-view `monitor` command. The binary prints a reminder at startup and any `monitor` invocation warns that the build is headless.

The build copies `libCr_*`, the adapter modules, and Sony’s OpenCV libs into `build/`. Run the binary from inside `build/` (or keep the copied `.so` files alongside it) so live view keeps working.

---

## Command-Line Options

| Option | Description |
| --- | --- |
| `--dir <path>` | Directory where downloads are stored. If omitted, files land in the working directory; providing an explicit folder is strongly recommended for sync features. |
| `--ip <addr>` | Connect directly to a camera at the given IPv4 address (e.g. `192.168.1.1`). Skipped when enumerating automatically. |
| `--mac <hex:mac>` | Optional MAC address for direct-IP connects (`aa:bb:cc:dd:ee:ff`). Used to seed the SDK’s Ethernet object. |
| `--model <name>` | Optional camera model hint for direct-IP connects (e.g. `a7r5`, `fx3`, `zve1`). Enumeration ignores this flag and always picks the first discovered device. |
| `--user <name>` | Username for cameras with Access Auth enabled. |
| `--pass <password>` | Password for Access Auth. Combine with `--user`. |
| `--cmd <path>` | Executable/script that SonShell calls for every file event (new downloads, syncs, rating changes, …). Arguments: `<path> <mode> <operation> [old] [new]`. Runs asynchronously; SonShell does not wait for completion. |
| `--keepalive <ms>` | Reconnection delay after failure or disconnect. `0` disables retry (SonShell exits on error). |
| `--verbose`, `-v` | Print detailed property-change logs and transfer progress from the SDK callbacks. |

If no `--ip` is provided SonShell enumerates available cameras and uses the first match. A fingerprint of the successful connection is cached under `~/.cache/sonshell/fp_enumerated.bin` so subsequent launches pair faster.

---

## Hook Events

When `--cmd` is provided SonShell calls the hook for every file-affecting event. The hook always receives:

```
<path> <mode> <operation> [old] [new]
```

- `path` – absolute path to the newest local copy of the file.
- `mode` – current camera operating mode resolved via the SDK. Examples:
  - `record/still/m` → still capture in manual mode.
  - `record/still/auto_plus` → still capture in Auto+ mode.
  - `record/movie/cine_ei/sq` → movie clip shot in Cine EI with S&Q enabled.
  - `playback` → events raised while browsing files on-body.
- `operation` – high-level action SonShell observed.
  - `new` – a freshly captured file copied to disk.
  - `sync` – a file mirrored during a manual/auto sync.
  - `rating` – the camera changed the star rating of a file (works wherever the SDK reports the update).
- `old` / `new` – optional values tied to the operation (for `rating` they are the previous and current star counts, for `new`/`sync` only the `new` value is populated with the original camera path).

The hook is