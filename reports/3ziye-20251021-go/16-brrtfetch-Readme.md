<h3 align="center"><img src="./docs/readme-md-brrtfetch-main-textlogo.png" alt="logo" height="100px"></h3>
<p align="center"><img src="./docs/readme-md-main.gif" height="400px"></p>
<p align="center"><i>Fastfetch config: https://github.com/xerolinux/xero-layan-git</i></p>

**Brrtfetch** is an animated system information fetcher written mainly in Go. Please keep in mind that it is still in it's very early stage of development. It displays the user specified **GIF rendered as animated ASCII art** alongside the system information from your favourite fetcher.

Think of it like a renderer that replaces the ASCII art for your fetcher with **animated** art. You only need to provide a .gif file.

Broken on MacOS. It does not display sysinfo. I do not own any Apple devices so apologies if this takes a while to fix.

In the next version I plan to use a new way of deciding what to put where in the terminal. It should be way more stable. No more color bugs, already confirmed hyfetch works(no workaround needed),the issue with illegal flags for the script binary on MacOS will also be resolved in the upcoming release. You can also expect a very cool new feature which I have not seen on any other animated fetchers when the new update is released.

---
 
## ✨ Features

* Render animated GIFs as **colorful ASCII art** directly in your terminal.
* Side-by-side system information via `fastfetch`, `neofetch`, or your fetcher of choice. I have only tested with `fastfetch`, `neofetch` and `hyfetch`. Hyfetch requires a small workaround and even then it's still a bit buggy with hyfetch. See examples below. 
* **True color (24-bit ANSI)** support with optional white monochrome mode via `-color=false`.
* **Multithreaded prerendering** for smooth playback.
* Configurable:

  * Width / height to render at
  * FPS to render at (impacts animation speed)
  * Brightness multiplier (controls density of ASCII mapping)
  * Vertical offset for aligning sysinfo height relative to  ASCII art
* Attempts to preserves **ANSI color codes** from sysinfo commands (broken for hyfetch and Windows CMD/Powershell. WSL does show color for the sysinfo. Only tested this with Ubuntu for WSL).
* If you can somehow render DOOM in GIF format you could technically use this to play DOOM in your fetcher. It would only be (re)rendered in brrtfetch, not actually run inside of it, at least for now ;)

---

## 📦 Installation

More comprehensive instructions for different distros and support for various package managers will be coming soon.

Debian/Ubuntu based steps only for the initial release, it should work on any linux system as long as you replace apt with your package manager for the dependencies. You can install it on Windows and Mac if you want. Just translate the steps to Windows. Will try to add Winget support later so i don't have to make an install script/instructions for Powershell. I will also attempt to add support for all major Linux package managers and Brew.


### Prerequisites

* A terminal that supports ANSI colors and escape sequences. Almost all modern terminals do.
* `Script` (Linux only) 

  Optional but highly recommended for sysinfo color support. Part of the **bsdutils** package. Comes by default on most systems. Check with "which script"
* `Unbuffer` (Linux only)

  Optional but recommended. Part of the `expect` package. Install with "apt install expect" or any other package manager. Brrtfetch will attempt to fallback on `unbuffer` if `script` is not available. 
* A fetch application with an option to omit the ASCII art.

  * [fastfetch](https://github.com/fastfetch-cli/fastfetch) (default)
  * [hyfetch](https://github.com/hykilpikonna/hyfetch)
  * Or any command you like, it can be specified with `-info "neofetch --off"` or even `-info "echo $USER"` or anything custom if you want.

  ```bash
  apt install fastfetch # only works on Debian 13+, see fastfetch docs for other version and distros
  apt install bsdutils expect
  ```

### Build from source

Additional prerequisite:
* Go 1.20+ (I used Go 1.23.3, will assume 1.20+ works)

  ```bash
  # Install Go (replace apt with your package manager like brew, yum, pacman etc)
  sudo apt install golang

  # Build
  git clone https://github.com/ferrebarrat/brrtfetch
  cd brrtfetch 
  go build -o ./bin/brrtfetch ./go/main.go && chmod +x ./bin/brrtfetch

  # Add to path
  sudo cp ./bin/brrtfetch /usr/local/bin/brrtfetch

  # Optional - Save gifs from repo before cleanup
  mkdir -p /home/$USER/Pictures/brrtfetch/gifs
  cp -r ./gifs/* /home/$USER/Pictures/brrtfetch/gifs

  # Cleanup
  cd .. && rm -rf brrtfetch
  ```

---

## 🎮 Usage

  ```bash
  brrtfetch [options] /path/to/file.gif
  ```

* **Ctrl-C** → attempts to exit the animation gracefully, clears and restores terminal, prints first frame with sysinfo and returns you to your prompt as if it was just a static fetcher.
* Animation loops endlessly until interrupted with **CTRL-C**.

<p><img src="./docs/readme-md-example-run.gif" height="300px"></p>

