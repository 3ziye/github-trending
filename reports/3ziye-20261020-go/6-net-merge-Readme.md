<p align="center">
  <img src="docs/icon.png" width="128" alt="net-merge icon">
</p>

<h1 align="center">net-merge</h1>

<p align="center">
  <strong>Use all your internet connections at the same time.</strong><br>
  Combine Wi-Fi, Ethernet and phone hotspots, so downloads, games and browsers get the speed of every connection added up.
</p>

<p align="center">
  <a href="https://github.com/rohit267/net-merge/releases/latest">Download</a> ·
  <a href="#install">Install</a> ·
  <a href="#add-a-second-connection">Add a second connection</a> ·
  <a href="#troubleshooting">Troubleshooting</a> ·
  <a href="docs/DEVELOPING.md">How it works</a>
</p>

<p align="center">
  <a href="https://github.com/rohit267/net-merge/actions/workflows/ci.yml"><img src="https://github.com/rohit267/net-merge/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://github.com/rohit267/net-merge/releases"><img src="https://img.shields.io/github/v/release/rohit267/net-merge" alt="Latest release"></a>
  <a href="https://github.com/rohit267/net-merge/releases"><img src="https://img.shields.io/github/downloads/rohit267/net-merge/total" alt="Downloads"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/rohit267/net-merge" alt="MIT license"></a>
  <img src="https://img.shields.io/badge/platforms-Windows%20%7C%20macOS%20%7C%20Linux-blue" alt="Windows, macOS and Linux">
  <a href="https://buymeacoffee.com/rohit267"><img src="https://img.shields.io/badge/Buy%20me%20a%20coffee-rohit267-FFDD00?logo=buymeacoffee&logoColor=black" alt="Buy me a coffee"></a>
  <a href="https://paypal.me/champdev"><img src="https://img.shields.io/badge/Donate-PayPal-00457C?logo=paypal&logoColor=white" alt="Donate with PayPal"></a>
</p>

<p align="center">
  <img src="docs/demo.gif" width="600" alt="Speed test on a Mac with Wi-Fi and an Android phone: the net-merge menu shows both connections carrying traffic, and the download reaches about 326 Mbit/s">
  <br>
  <sub>A Mac with Wi-Fi + an Android phone. The menu shows both connections working at once. <a href="docs/demo.mp4">Watch the full 45-second video.</a></sub>
</p>

net-merge uses all your network adapters together. It works on **Windows, macOS and Linux**. It is free.
There is no account, no server and no VPN.

A real test with Wi-Fi + an Android USB tether + an iPhone hotspot, 9 downloads at once:
**232-303 Mbit/s**. The fastest connection alone gave about 121 Mbit/s.

| Windows: hover the icon | Windows: the menu | macOS: the menu bar |
|---|---|---|
| ![Tooltip: Merging, speed of each adapter and the total](docs/tray-tooltip.png) | ![Menu: total, each adapter's speed and flows, IPv6 option, Pause merging, Quit](docs/tray-menu.png) | ![macOS menu: total 399 Mbit/s, en0 and feth0 each with their flows, Pause merging, Quit](docs/tray-menu-macos.png) |

## How it helps

net-merge gives every new connection to one of your links. When an app opens many connections, they
spread over all your links.

- **Good for:** Steam and game downloads, browsers, system updates, cloud uploads (Google Drive),
  download managers like IDM, torrents.
- **Not for:** one single connection. One connection always uses one link, so one big file from one
  connection does not get faster. Browsers can split a download into several connections; see the tip
  under [Use it](#use-it).
- **Works for every app**, TCP and UDP, IPv4 and IPv6. You do not set up a proxy.
- **Smart:** faster links get more connections. A link with no internet gets none until it works again.
- **Safe:** if net-merge crashes, your internet keeps working.
- **Light:** about 0.18 CPU cores per 100 Mbit/s.

## Install

**macOS and Linux**: paste this into a terminal.

```
curl -fsSL https://raw.githubusercontent.com/rohit267/net-merge/main/install.sh | sh
```

**Windows**: paste this into PowerShell.

```
irm https://raw.githubusercontent.com/rohit267/net-merge/main/install.ps1 | iex
```

That's it: net-merge is installed and its icon appears in the menu bar or tray. On Linux the script
uses your package manager (apt, dnf, zypper, apk or pacman) and on macOS Homebrew when you have it, so
net-merge updates with the rest of your system. To start it at sign-in, tick *Start at sign-in* in its menu.

<details>
<summary><strong>Rather type the commands yourself?</strong> One block per system, each ready to paste.</summary>
<br>

**Homebrew** (macOS):

```
brew install rohit267/tap/net-merge && sudo "$(brew --prefix)/bin/net-merge" install && net-merge tray
```

**macOS without Homebrew**:

```
curl -fsSL https://github.com/rohit267/net-merge/releases/latest/download/net-merge-macos-universal.tar.gz | tar -xz -C /tmp net-merge && sudo /tmp/net-merge install && net-merge tray
```

**Debian, Ubuntu, Linux Mint, Pop!_OS, Raspberry Pi OS** (apt):

```
curl -fsSL https://rohit267.github.io/net-merge/apt/key.gpg | sudo tee /usr/share/keyrings/net-merge.gpg >/dev/null
echo "deb [signed-by=/usr/share/keyrings/net-merge.gpg] https://rohit267.github.io/