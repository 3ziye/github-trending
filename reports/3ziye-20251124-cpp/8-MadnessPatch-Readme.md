<p align="center">
  <img src="assets/MadnessPatch_Logo.png" width="575" />
</p>

<p align="center">
A patch that fixes various issues in the PC port of Alice: Madness Returns.
</p>

## How to Install

> [!NOTE]  
> Compatible with the Steam and EA App versions of Alice: Madness Returns.
>
> **Download**: [MadnessPatch.zip](https://github.com/Wemino/MadnessPatch/releases/latest/download/MadnessPatch.zip)  
> Extract the contents of the zip file into the game's `Win32` folder, which contains the `AliceMadnessReturns.exe` file.
>
> <img width="240" src="assets/install.png">
>
> Directory path for Steam:  
> `SteamLibrary\steamapps\common\Alice Madness Returns\Binaries\Win32`
>
> Directory path for EA App:  
> `EA\Alice Madness Returns\Game\Alice2\Binaries\Win32`

> [!WARNING]
If the game doesn’t start on Windows after installing the patch, try updating the latest Microsoft Visual C++ Redistributable (x86).  
You can download it here: https://aka.ms/vs/17/release/vc_redist.x86.exe

> [!TIP]  
> If you own the remastered version of *American McGee's Alice*, check out [VorpalFix](https://github.com/Wemino/VorpalFix)!

### Steam Deck/Linux Specific Instructions (Windows users can skip this)

> [!WARNING]
> To launch the game on Steam Deck or Linux, set the game’s compatibility tool to Proton Experimental in the Steam properties.

# Features

## Subtitle Font Scaling

Scales subtitles properly on high-resolution displays. The game was originally designed for consoles and limits subtitle size above 720p, making text harder to read on 1080p or higher. This fix removes that limit so subtitles scale correctly with your resolution.

If you want a different size, you can fine-tune it with `FontScalingFactor` in `MadnessPatch.ini`.

<div align="center">
  <table>
    <tr>
      <td width="50%"><img style="width:100%" src="assets/FontScaling_Off.jpg"></td>
      <td width="50%"><img style="width:100%" src="assets/FontScaling_On.jpg"></td>
    </tr>
    <tr>
      <td align="center">4K Vanilla</td>
      <td align="center">4K MadnessPatch</td>
    </tr>
  </table>
</div>

## High FPS Fixes

Fix multiple physics and gameplay issues that occur at high framerates by preventing hair and dress physics from becoming unstable and ensuring consistent hitbox size for projectiles like the Pepper Grinder.

## Crashes and Infinite Loading Fix

Prevents crashes and infinite loading screens caused by race conditions that occur more frequently at higher framerates during map transitions.

## Input Binding Fix

Fix issues where certain input mappings fail to respond correctly. This particularly affects the umbrella key and other special action bindings that may not register during the input initialization process.

## Force High Resolution Textures

The game normally loads blurry textures first and then sharpens them as you get closer, which was meant for consoles but looks distracting on PC. This patch forces the highest texture resolution from the start and improves texture streaming, so you don’t see textures popping into clarity as you move around. It also slightly reduces mipmap bias, improving texture sharpness at a distance.

<div align="center">
  <table>
    <tr>
      <td width="50%"><img style="width:100%" src="assets/ForceHighResTextures_Off.jpg"></td>
      <td width="50%"><img style="width:100%" src="assets/ForceHighResTextures_On.jpg"></td>
    </tr>
    <tr>
      <td align="center">Vanilla</td>
      <td align="center">Force High Res</td>
    </tr>
  </table>
</div>

> **Note**: May increase VRAM usage and impact performance on systems with limited graphics memory.

## Bink Video Color Space Fix

Switched the Bink video color profile from BT.601 to BT.709, which is the standard for HD video, so pre-rendered videos now show correct colors, especially deep reds and warm tones.

<div align="center">
  <table>
    <tr>
      <td width="50%"><img style="width:100%" src="assets/FixBinkVideoBT709_Off.jpg"></td>
      <td width="50%"><img style="width:100%" src="assets/FixBinkVideoBT709_On.jpg"></td>
    </tr>
    <tr>
      <td align="center">Vanilla (BT.601)</td>
      <td align="center">MadnessPatch (BT.709)</td>
    </tr>
  </table>
</div>

## Input Improvements

### Disable Mouse Acceleration

Stops the game from ramping up mouse speed when you start moving it.

### Disable Controller Acceleration

Turns off the same acceleration system for controllers. The game speeds up your look input as the stick starts moving, and this option removes that so the stick behaves more consistently.

Enable with `DisableControllerAcceleration = 1` in `MadnessPatch.ini`.

### Disable Mouse Smoothing

Turns off camera smoothing so the view responds instantly to your mouse movements.

Enable with `DisableMouseSmoothing = 1` in `MadnessPatch.ini`.

## Ultrawide FOV Fix

Removes pillarboxing and adjusts the FOV for ultrawide monitors.

<div align="center">
  <table>
    <tr>
      <td><img style="width:100%" src="assets/FixUltraWideScreenFOV_Off.