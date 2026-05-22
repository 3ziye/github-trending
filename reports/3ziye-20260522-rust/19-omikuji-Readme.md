# <img src="crates/omikuji/qml/icons/app.png" width="40" align="left"/>   omikuji

A Qt/QML based games/apps launcher for Linux. Built 'cause I couldn't bear having 3 different launchers for just games.

Manages wine/proton runners, wineprefixes, DXVK/VKD3D, and game launching. Imports from Steam, installs Epic, GOG and Waifu machine slots games directly. 
Backend is Rust, frontend is Qt/QML via [cxx-qt](https://github.com/KDAB/cxx-qt).

## Screenshots

| Library                                          | Edit Game                                                 |
|:---|:---|
| <img src="docs/screenshots/main_library.png"/>   | <img src="docs/screenshots/edit_page.png"/>               |
| Epic Games Store                                 | Epic Install Dialog                                       |
| <img src="docs/screenshots/epic_games_store.png"/> | <img src="docs/screenshots/epic_games_store_download.png"/> |
| Gacha Store                                      | Gacha Install Dialog                                      |
| <img src="docs/screenshots/gacha_store.png"/>    | <img src="docs/screenshots/gacha_store_download.png"/>    |
| Interface Settings                               | Components Settings                                       |
| <img src="docs/screenshots/settings_page_interface.png"/> | <img src="docs/screenshots/settings_page_componenets.png"/> |
| Console Mode (Aurora background)                 | Console Mode (Sakura background)   
| <img src="docs/screenshots/console_mode_1.png"/> | <img src="docs/screenshots/console_mode_2.png"/> |



## What it does

- **Game library** one TOML per game, shareable, git-friendly.
- **Wine / Proton**: auto-detects Steam-installed Proton, has its own fetcher in the settings.
- **Translation layers**: DXVK, VKD3D, DXVK-NVAPI. Auto-fetched from upstream releases.
- **Stores**: import from Steam (locally), install Epic games (via legendary), GOG (via gogdl), HoYoverse / Kuro / Gryphline gachas (direct CDN + delta patch handlers).
- **Wrapping chain**: gamescope, mangohud, gamemode, taskset, custom prefixes.
- **Wine tools**: winecfg, winetricks, regedit, cmd, winefile, run-exe, kill-wineserver.
- **Art fetch**: SteamGridDB for banners, covers, icons.
- **Playtime**: tracked per-game, persisted on exit. Steam playtime via your own Web API key.
- **CLI**: `omikuji run <slug_or_id>` launches games headlessly. Used for `.desktop` shortcuts.

## Status

Usable. Daily-driven by me. Still needs some UI polish and decisions that i'm too saturated to take yet.

QML side held up with tape and prays🙏

Not implemented/WIP/Planning to add: 
- i18n/qsTr (ehahahshhaha)
- Amazon Games
- make gacha stuff optional (not automatically fetched on startup)
- more CLI commands which i cant be bothered with yet
- Genuinely fix some UI stuff (e.g, settings page edit/add games tabs. I dont like them there ngl)
- Components tab in the settings page is a bit ass and im not sure i like the green texts/balls

## Building

Requires Rust (2024 edition), Qt 6.7+, plus `pkgconf` and `cmake`. Or skip all this and grab the AUR build below.

```sh
git clone https://github.com/reakjra/omikuji.git
cd omikuji
cargo build --release
```
> (let me know if after 8 hours rust finished compiling 👍👍👍)

Run it straight from the build dir:
```sh
./target/release/omikuji
```

Or go with the AUR:

```sh
yay -S omikuji-git
```


You can also install/build it with Nix:

<details>
<summary><b>Click to expand Nix related stuff</b></summary>

> For any issues related to the flake, mention @claymorwan in your issue.

If you're on NixOS and using flakes, add the flake to your inputs:
```nix
# flake.nix
{
	
	inputs = {
		nixpkgs.url = "nixpkgs/nixos-unstable";
		
		omikuji = {
			url = "github:reakjra/omikuji";
			inputs.nixpkgs.follows = "nixpkgs";
		};
	};
}
```

Then install the app:
```nix
{ inputs, pkgs, ... }:

{
  # Using the home-manager module (recommended)
  programs.omikuji.enable = true;

	# Or NixOS side installation
	environment.systemPackages = [
		inputs.omikuji.packages.${pkgs.stdenv.hostPlatform.system}.default
	];

	# Or home-manager side installation
	home.packages = [
		inputs.omikuji.packages.${pkgs.stdenv.hostPlatform.system}.default
	];
}
```

If you don't want to compile the full package, there's a cachix binary cache from where you can pull the precompiled package:
```nix
{
  nix.settings = {
    substituters = [
      "https://omikuji.cachix.org"
    ];
      
    trusted-substituters = [
      "https://omikuji.cachix.org"
    ];

    trusted-public-keys = [
      "omikuji.cachix.org-1:dS6sbpMxarHWIIk3y0R7KXz3eVHUg1lo/y3gMbv4JhM="
    ];

  };
}
```
And restart the nix daemon to apply them, then you can install the package
> More info about substituter [here](https://wiki.nixos.org/wiki/Binary_Cache#Using_a_binary_cache)

To run it without installing:
```sh
nix run github:reakjra/omikuji
# Add #omikuji-unwrapped to run the unwrapped package
```

Building the package itself:
```sh
nix bu