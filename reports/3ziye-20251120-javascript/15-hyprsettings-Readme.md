# HyprSettings

HyprSettings: a configurator for `hyprland.conf` that very loyally reconstructs your configs exactly(almost*) as you wrote them, including comments. It presents everything in an organized UI that is also keyboard navigable. Themable, too!

Made with Python, web technologies via PyWebviewGTK, vanilla JS, and some JS libraries.

<!-- <img width="1915" height="1046" alt="image" src="https://github.com/user-attachments/assets/ec4d850b-244f-40bc-a92a-5dc7909618d3" /> -->
<img width="1915" height="1046" alt="image" src="https://github.com/user-attachments/assets/c7284cf1-c51a-4996-b60c-7ab1d9ae402c" />


Hyprsettings in Catppuccin, with the search bar and the color selector open. Cool ain't it?


> New Feature: Colors, Sliders, Search bar! 
> How about we get some color picker and a search bar? Yes! It's already there! (I'm sooo happy not gonna lie)

> Looking for Contributors 🙌  
> I'd love help with: autocomplete color selectors, gradient selectors, a floating sidebar for Hyprland documentation, and other minor improvements. Open a discussion or issue if you're interested!

> [!IMPORTANT]
> This is in alpha state.

You can fork this repo, make changes, and submit pull requests. Please also submit bugs, start discussions, etc. I'd love to hear from you!

## Features

- Faithful `hyprland.conf` configurator that reconstructs your config exactly as written
- Preserves comments and their positions
- Organized UI with logical tabs for easier navigation
- Keyboard navigable controls throughout the UI
- Multi file configs supported with `source` discovery, `~/` expansion, '$variable' support , and globbing
- Color Picker , gradient editor
- Dynamic resizing
- Theming support

## Table of Contents

- [HyprSettings](#hyprsettings)
  - [Features](#features)
  - [Installation](#installation)
    - [Quick Clone and Venv Setup](#quick-clone-and-venv-setup)
    - [NixOS Installation](#nixos-installation)
    - [Arch Linux (AUR Package)](#arch-linux-aur-package)
  - [Testing the UI](#testing-the-ui)
  - [Configuration and Theming](#configuration-and-theming)
  - [Organizing Comments into Tabs](#organizing-comments-into-tabs)
  - [Contributing](#contributing)
  - [A Personal Note](#a-personal-note)
    - [Notice on the use of AI](#notice-on-the-use-of-ai)

## Installation

### Quick Clone and Venv Setup

Run the following in a shell to clone, create a virtual environment, install Python dependencies, and start the UI.

```bash
git clone https://github.com/acropolis914/hyprsettings
cd hyprsettings
python -m venv .venv
. .venv/bin/activate
python -m pip install -U pip setuptools wheel
python -m pip install tomlkit rich pywebview
python src/ui.py
```

### NixOS Installation
(courtesy of @wiktormalyska)

For NixOS users, this repository includes full Nix packaging support with both flakes and traditional Nix.

See [NIX_INSTALLATION.md](NIX_INSTALLATION.md) for detailed installation instructions including:
- Installation with Nix flakes
- Traditional Nix installation
- Home Manager integration
- NixOS module usage

Quick start with flakes:
```bash
nix run github:acropolis914/hyprsettings
```

### Arch Linux (AUR Package)

**HyprSettings is now available on Arch / AUR!**  
Install it with your helper of choice (example uses `yay`):

```bash
yay -S hyprsettings-git
```

Yay 🎉

After installation you can:
- Launch it from your application launcher (rofi, wofi, walker, fuzzel, etc.) by searching for “HyprSettings”.
- Run from terminal: `hyprsettings`
- (Optional) Add a Hyprland keybind:
  ```
  bind = SUPER, I, Exec, hyprsettings
  ```

## Testing the UI

If you are developing locally instead of using the AUR package:

1. Clone the repo:

```bash
git clone https://github.com/acropolis914/hyprsettings
cd hyprsettings
```

2. Install required system packages (make a venv if you want):

```bash
sudo pacman -Syu python python-gobject gtk3 python-pywebview python-tomlkit python-rich
```

3. Run the UI:

```bash
python src/ui.py
```

> Make sure to replace `SUPER, I` with the key combination you want to use if you still bind manually.

## Configuration and Theming

Hyprsettings will create a configuration file at:

```
~/.config/hypr/hyprsettings.toml
```

Theming works perfectly out of the box. The defaults should be fine, but if you like tweaking, you can explore and modify the file. Be careful, though I do not have extensive safeguards and fallbacks right now.

## Organizing Comments into Tabs

> [!NOTE]
> Config keys are auto-sorted regardless of where they appear in your configuration files. The convention below only applies to comments and determines which tab they appear under in the UI.  
> With globbing and multi source parsing, all allowed `source =` formats are supported (absolute paths, `~/` expansion, and glob patterns like `/*`). All included files are scanned.

To make comments appear under the correct tab in Hyprsettings, use a three line comment block before the section it applies to in your configuration fil