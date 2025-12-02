# 🫂 CliWaifuTamagotchi

Preview:
![Result](screenshots/result.gif)
---
###### You can turn the avatar to **husbando** in `~/.config/cliwaifutamagotchi/settings.json`!
![Husbando](screenshots/husbando-preview.jpg)


![Repo size](https://img.shields.io/github/repo-size/HenryLoM/CliWaifuTamagotchi?color=lightgrey)
![Commits](https://img.shields.io/github/commit-activity/t/HenryLoM/CliWaifuTamagotchi/main?color=blue)
![Last commit](https://img.shields.io/github/last-commit/HenryLoM/CliWaifuTamagotchi?color=informational)
![License](https://img.shields.io/github/license/HenryLoM/CliWaifuTamagotchi?color=orange)

## 📑 Table of Contents
- [✨ Overview](#-overview)
- [🎬 Launching Process](#-launching-process)
- [🎨 Customization](#-customization)
- [📂 Project Structure](#-project-structure)
- [⚙️ Core Scripts](#-core-scripts)
    - [main.go](#maingo)
    - [utils/app-utils.go](#utilsapp-utilsgo)
    - [utils/commands-utils.go](#utilscommands-utilsgo)
    - [utils/happiness-utils.go](#utilshappiness-utilsgo)
    - [utils/palette-handler.go](#utilspalette-handlergo)
    - [utils/settings-handler.go](#utilssettings-handlergo)
    - [utils/encouragements-handler.go](#utilsencouragements-handlergo)
    - [utils/gifts-handler.go](#utilsgifts-handlergo)
- [📜 Notes & Error handling](#-notes--error-handling)
- [🛐 Special thanks](#-special-thanks)

---

## ✨ Overview
CliWaifuTamagotchi is a **terminal-based tamagotchi** that:

- Renders **ASCII expressions and clothes**.
- Provides a small set of **interactions**: Encourage, Dress Up, Background Mode, Quit.
- Uses a **persistent color palette** stored in `~/.config/cliwaifutamagotchi/palette.json`.
- Uses **persistent detail settings** stored in `~/.config/cliwaifutamagotchi/settings.json`.
- Customize some of the functions editing **`words-of-encouragement.txt` and `gifts.json`** in the same directory.
- Has minimal UI built using **`tview` and `tcell`**.
- Has **Vim-style navigation**: Use `h`, `j`, `k`, `l` keys for intuitive navigation and selection (Must be enabled in **settings.json**).

No tons of loops - only one function that repeats itself every 5 seconds. Everything handles and updates according to it.

---

## 🎬 Launching Process

<details>
  <summary><b>Brew</b> (macOS)</summary>

  1. **Install**

  ```bash
  brew install HenryLoM/CliWaifuTamagotchi/cliwt
  ```

  2. **Run**

  ```bash
  cliwt
  ```

  ---

</details>

<details>
  <summary><b>AUR</b> (Arch)</summary>

  1. **Install**

  ```bash
  yay -S cliwt
  ```
  or
  ```bash
  paru -S cliwt
  ```

  2. **Run**

  ```bash
  cliwt
  ```

  ---

</details>

<details>
  <summary><b>Git</b> (Source code)</summary>

  1. **Clone repository**

  ```bash
  git clone https://github.com/HenryLoM/CliWaifuTamagotchi.git
  cd CliWaifuTamagotchi
  ```

  2. **Build app yourself, then run**

  ```bash
  go build -o cliwt
  ./cliwt
  ```

  - **Or run directly for development**

  ```bash
  go run main.go
  ```

  ---

</details>

> **💡 Notes**
>
> * First run creates `~/.config/cliwaifutamagotchi/` directory and `palette.json`, `settings.json` files in it on its own if missing.
> * On macOS, ensure your terminal supports **true color** for best rendering.

---

## 🎨 Customization

1. **Palette**<br>
JSON file is in `~/.config/cliwaifutamagotchi/` ; Named `palette.json`<br>
JSON file's structure:
```
{
  "background": "#1e1e2e",
  "foreground": "#cdd6f4",
  "border": "#cba6f7",
  "accent": "#eba0ac",
  "title": "#b4befe"
}
```
> Note: default palette is Catppuchin (Mocha).

2. **Settings**<br>
JSON file is in `~/.config/cliwaifutamagotchi/` ; Named `settings.json`<br>
JSON file's structure:
```
{
  "name": "Waifu",
  "defaultMessage": "...",
  "vimNavigation": false,
  "avatarType": "waifu",
  "keys": {
    "encourage": "l",
    "dressup": "2",
    "backgroundMode": "b",
    "quit": "q"
  }
}
```
> Note: try to avoid key overrides when using `"vimNavigation": true`.

3. **Words of encouragement**<br>
TXT file is in `~/.config/cliwaifutamagotchi/` ; Named `words-of-encouragement.txt`<br>
> Note: It's extensible!

4. **Gifts**<br>
JSON file is in `~/.config/cliwaifutamagotchi/` ; Named `gifts.json`<br>
> Note: It's extensible!

---

## 📂 Project Structure

```
CliWaifuTamagotchi/
│
├── README.md
├── LICENSE
├── .gitignore
├── go.mod
├── go.sum
├── main.go                             # Main file that launches the project
│
├── screenshots/
│   ├── result.gif
│   ├── reactions.jpg
│   └── husbando-preview.jpg
│
└── utils/
    │
    ├── ascii-arts/
    │   │
    │   ├── waifu/                      # Arts for waifu avatar
    │   │   ├── clothes/...             # ASCII bodies
    │   │   └── expressions/...         # ASCII heads
    │   │
    │   └── husbando/...                # Arts for husbando avatar
    │       ├── clothes/...             # ASCII bodies
    │       └── expressions/...         # ASCII heads
    │
    ├── assets/
    │   └── words-of-encouragement.txt  # List of lines for Encouragement function
    │
    ├── 