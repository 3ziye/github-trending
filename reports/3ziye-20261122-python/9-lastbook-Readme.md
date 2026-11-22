# Lastbook

Lastbook is an offline survival library for Mac, Windows and Linux. It puts manuals, videos, encyclopedias, an offline map and
short practical guides on one computer. After setup, it works offline. The desktop sidebar opens Videos, Map and Chat.
Chat answers questions using the library, including the offline encyclopedias when they are present, and links to its sources.

Website: <https://lastbook.org>. Contact: hello@lastbook.org.

> Lastbook’s original code and documentation are licensed under the [MIT License](LICENSE).
> Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) to get started.

## Release status

| Platform | Version | Status |
|---|---|---|
| macOS (Apple Silicon, macOS 14 or later) | 1.1.15 | Live on lastbook.org, signed and notarized |
| Windows (64-bit, Windows 10 or later) | 1.1.15 | Live on lastbook.org, Authenticode signed |
| Linux (Ubuntu 24.04 or 26.04 LTS, x86_64) | 1.1.15 | Ubuntu packages; installation instructions below |

## iPad (development preview, source only)

A native iPad app (Videos, Map and Chat, offline, with optional on-device AI) is in [`mobile/ipad/`](mobile/ipad/).
- It is source for contributors to build and sign themselves.
- There is no App Store, TestFlight or downloadable iPad build.
- See [mobile/ipad/README.md](mobile/ipad/README.md) for what works, the current limitations and how to build it.

## Install on Linux

The Linux packages target **Ubuntu 24.04 LTS and Ubuntu 26.04 LTS on Intel/AMD x86_64 computers**, one package for each. Download
[Lastbook for Ubuntu 24.04](https://downloads.lastbook.org/Lastbook_1.1.15_amd64.deb) (or [for Ubuntu 26.04](https://downloads.lastbook.org/Lastbook_1.1.15_ubuntu26.04_amd64.deb)), then install it with apt so Ubuntu resolves its dependencies.

```bash
sudo apt install ./Lastbook_1.1.15_amd64.deb                  # Ubuntu 24.04
sudo apt install ./Lastbook_1.1.15_ubuntu26.04_amd64.deb      # Ubuntu 26.04
```

Open Lastbook from the application menu. First-run setup downloads your chosen library, state map and optional local AI.
The app uses Ubuntu's GTK, WebKitGTK and media codecs. Its own files install under `/opt/lastbook`, and your library and
settings stay in your home folder. Removing the package leaves those downloaded files and settings in place.

The Linux release was tested on Ubuntu 24.04.5 in WSL2, including installation, setup, video playback, maps, address search,
PDF reading, offline AI with citations, shutdown and uninstall. AI tests used the CPU. Native Linux GPU performance and
other Linux distributions have not been validated for this release.

## What it does

- **Guides first.** Short, curated guides for urgent needs (`content/topics/`), each pointing to real pages in the library
  with page numbers, plus what curators looked for and did not find (`content/gaps.json`).
- **The full library.** Manuals and PDFs (with a whole-PDF view), videos, and offline encyclopedias (ZIM files), with
  keyword search everywhere and meaning-based search on Windows.
- **Offline map.** A base map of the world and the US, plus a detailed map for the state selected during setup: local streets,
  buildings, terrain, crops, and water, help and resource points. Addresses in that state can be found offline. The person
  picks the state; Lastbook never detects location.
- **Optional local AI.** Ask questions in plain words and get answers that cite library pages, from a model that runs on
  the computer itself (see "The local AI" below). Without it, Chat still finds the right pages.
- **Saved video moments.** Keep several named positions in a video and open them from the player or Saved. Names and
  positions stay on this device; the video and its captions are unchanged.
- **One-download setup.** On first run, setup defaults to Small and selects local AI when the computer can run it.
  The person can choose Small, Medium or All, selects a state map, and starts the checked downloads. A library already on the
  computer (a folder or a pack zip) can be used instead of downloading.
- **Check for updates, only when asked.** About has a Check for updates button (and the Mac menu has Lastbook > Check for
  Updates…). It only says whether a newer version is on the website; nothing is downloaded or installed.

## Privacy and network use

- **No listening port.** The desktop app opens no network port. The window and the engine talk through an in-memory bridge
  (`app/bridge.py`): WKURLSchemeHandler on macOS (`app/shell_macos.py`), WebView2 `WebResourceRequested` on Windows
  (`app/shell_windows.py`), and WebKitGTK `URISchemeRequest` on Linux (`app/shell_linux.py`). The local AI runner speaks JSON lines on standard input and output and opens no socket either.
- **Two uses of the network, both started by the person.** (1) Setup's downloader (`engine/setup/`), when the person
  starts or resumes a download. (2) The update check (`engine/update.py`, `web/update.js`), when the person presses
  the button. Both go th