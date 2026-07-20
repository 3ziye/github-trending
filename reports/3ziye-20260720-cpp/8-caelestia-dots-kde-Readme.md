<div align="center">

# C A E L E S T I A <img src="assets/caelestia.svg" width="35" align="top">

### A KDE adaptation of the celestial aesthetic

![Arch Linux](https://img.shields.io/badge/Arch_Linux-1793d1?logo=arch-linux&logoColor=white&style=for-the-badge)
![Fedora](https://img.shields.io/badge/Fedora-51A2DA?logo=fedora&logoColor=white&style=for-the-badge)
![KDE Plasma](https://img.shields.io/badge/KDE_Plasma-1D99F3?logo=kde&logoColor=white&style=for-the-badge)
![Quickshell](https://img.shields.io/badge/Quickshell-FF6B6B?style=for-the-badge)
![License: GPLv3](https://img.shields.io/badge/License-GPLv3-blue?style=for-the-badge&color=86dbce)

<br/>
<img width="400" height="230" alt="logo" src="https://github.com/user-attachments/assets/5662c83d-7181-4846-9fb8-79d0363c8c4f" />

<br/>
<br/>

> *“Ad astra per aspera.”*

</div>

---

<div align="center">
    <h2>✦ What is this? ✦</h2>
</div>

> [!NOTE]  
> This is a **community KDE port** of the beautiful [Caelestia Hyprland dotfiles](https://github.com/caelestia-dots/caelestia), meticulously adapted by **[ladybug-me](https://github.com/ladybug-me)** to bring the heavens to **KDE Plasma**.

<details> 
  <summary><b>What this is / isn't</b></summary>
  <br/>

  - **Technically:** A curated collection of KDE Plasma configuration files, custom widgets, and idempotent installation scripts.
  - **Visually:** The ethereal caelestia aesthetic seamlessly ported to KDE Plasma utilizing cutting-edge Quickshell widgets.
  - **NOT:** A direct replacement for the original Hyprland dotfiles (which remain superior for dedicated minimal window managers).
  - **NOT:** A fully unattended system setup script (installs packages and configs, but no low-level system drivers or core tuning).
  
</details>

<details> 
  <summary><b>Why KDE instead of Hyprland?</b></summary>
  <br/>

  - KDE Plasma offers broader compatibility with existing tools, hardware, and ecosystems.
  - Provides a familiar, highly robust desktop environment.
  - Integrates strongly with the Arch Linux community and the AUR.
  - Proves that heavy DEs can still achieve an ultra-customized, highly aesthetic ricing spirit.
  
</details>

<details> 
  <summary><b>Key Features</b></summary>
  <br/>

  - **Works on Real KDE Setups:** Built and tested on current Plasma versions across Arch-based distros and Fedora.
  - **Fast to Install, Safe to Re-run:** Idempotent scripts let you retry installation without wrecking your existing setup.
  - **Clean Rollback:** Dedicated uninstaller makes it easy to revert if you do not like the result.
  - **Consistent Theming:** Darkly + Kvantum + dynamic color extraction keep apps and shell visuals in sync.
  - **Deep KDE Integration:** Custom KWin bridge and Quickshell modules provide tight desktop-level behavior.
  - **Daily-Use Tools Included:** Screenshot, screen recording with audio, color picker, clipboard history, and emoji picker are ready out of the box.
  - **Simple Update Path:** Update from UI or command line without overwriting your shell settings.
  - **Optional Tiling Workflow:** Polonium support is available if you want dynamic tiling on Plasma.
  
</details>

<details> 
  <summary><b>Installation</b></summary>
  <br/>

  1. **Clone this repository:**
     ```bash
     git clone -b main --single-branch --depth 1 https://github.com/ladybug-me/caelestia-dots-kde ~/caelestia-dots-kde
     cd ~/caelestia-dots-kde
     ```
  2. **Run the installer:**
     ```bash
     bash ./setup.sh
     ```
  3. **Follow the interactive prompts:** You can safely retry or ignore errors as needed.
     
  > **Note:** The installer might occasionally prompt for your password multiple times due to sudo timeouts. This is a known quirk and will be optimized in future releases.
  
  **Requirements:**
  - Arch Linux or an Arch-based distro (EndeavourOS, CachyOS, Manjaro, etc.), or Fedora Linux.
  - KDE Plasma 6.0+

  **Tested on:**
  - CachyOS
  - Manjaro KDE
  - Fedora 44 KDE Edition
  
</details>

<details> 
  <summary><b>Updates</b></summary>
  <br/>
    
    NOTE: You must backup your ~/.config if you have made changes to the dot or shell files
  - Updating is simple now with integrated experience.
  - **Gui**: Open Shell settings -> Updates -> Select the update type (stable or bleeding edge) -> Install Updates
  - **Manual**: just run `bash update.sh` and select the branch from which you want to update. 
  - branches: main (stable) and dev (bleeding edge)
  - Shell settings are **not** changed during updates. 


</details>

<div align="center">
    <h2>✦ Visuals ✦</h2>
</div>



https://github.com/user-attachments/assets/9ad2e5f5-f80e-48c0-b65b-a4084bb363c6


| Caelestia on KDE Plasma Shell | Theming in Action |
|:---:|:---:|
| <img width="460" height="259" alt="shell" src="https://github.com/user-attachments/assets/14681aaf-77d9-4a65-af7d-8a4fc0b795cc" /> | <img width="460" height="259" alt="Rengoku" src="https://github.com/user-attachments/assets/d1b73dcb-82c9-465d-ba7e-da79ce263917" /