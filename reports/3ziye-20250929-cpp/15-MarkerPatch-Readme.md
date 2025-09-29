<p align="center">
  <img src="assets/MarkerPatch_Logo.png" style="max-width:70%">
</p>

<p align="center">
A patch that fixes various issues and limitations in the PC port of Dead Space 2.
</p>

## How to Install

> [!NOTE]  
> Compatible with all versions of Dead Space 2 (Steam, EA App).
>
> **Download**: [MarkerPatch.zip](https://github.com/Wemino/MarkerPatch/releases/latest/download/MarkerPatch.zip)  
> Extract the contents of the zip file into the game's folder, in the same directory as the `deadspace2.exe` file.

### Steam Deck/Linux Specific Instructions (Windows users can skip this)

> [!WARNING]
> To launch the game on Steam Deck or Linux, open the game's properties in Steam and include `WINEDLLOVERRIDES="dinput8=n,b" %command%` in the launch options.
>
> **Note**: DXVK limits the framerate to 60 FPS by default. To increase this limit, add the following to your launch options (example for 120 FPS):  
> `DXVK_FRAME_RATE=120 WINEDLLOVERRIDES="dinput8=n,b" %command%`

# Features

## Havok Physics Fix

Stabilizes physics behavior at high framerates to eliminate the annoying flying corpses and limbs. While physics issues begin above 30 FPS, they become noticeably problematic after 100 FPS, causing dead bodies and severed limbs to launch erratically across rooms.

## High-Core CPU Fix

Prevents the game from crashing on systems with more than 10 CPU cores. The game's CPU detection code collects information about each core into fixed-size arrays, but these arrays weren't sized to handle more than 10 cores. When more cores are detected, the code overflows these arrays, corrupting memory and causing crashes later during execution. The patch stops the CPU detection loop early to prevent this overflow.

## VSync Refresh Rate Fix

Corrects the VSync implementation to use the refresh rate selected in the game's settings instead of locking to 30 FPS. The original implementation ignores your chosen refresh rate and forces 30 FPS when VSync is enabled.

<div align="center">
  <table>
    <tr>
      <td width="50%"><img style="width:100%" src="assets/vsyncfix_off.png"></td>
      <td width="50%"><img style="width:100%" src="assets/vsyncfix_on.png"></td>
    </tr>
    <tr>
      <td align="center">Vanilla (Locked to 30 FPS)</td>
      <td align="center">MarkerPatch (Uses Selected Rate)</td>
    </tr>
  </table>
</div>

## Save System Fixes

### Difficulty Reward Tracking
Fixes the tracking of Zealot and Hardcore difficulty completions to properly unlock rewards. 

> **Important**: This fix requires starting a new save with the patch installed. You must keep the patch installed for the entire playthrough for the fix to remain effective.

### Suit ID Conflicts
Resolves item database conflicts where certain DLC suits incorrectly share IDs with other suits:
- **Zealot Suit** was conflicting with the Security Suit.
- **Hacker Suit** was conflicting with the Elite Advanced Suit.

These conflicts would cause one suit to overwrite the other in your inventory, making purchased items disappear.

### String Buffer Overflow Prevention
Prevents crashes that can rarely occur when the game enumerates save files. This happens in two scenarios: when checking for Dead Space 1 saves to grant the DLC bonus for owning the first game, and when listing your Dead Space 2 save files in the load menu. Though these crashes are uncommon, they can be frustrating when they do occur.

## Subtitle Font Scaling

Scales subtitle text appropriately for high resolutions. The game was designed with console limitations in mind and intentionally prevents subtitles from scaling beyond 720p resolution, making them tinier at 1080p and above. This fix removes that limitation and allows proper scaling.

For those who prefer different subtitle sizes, `FontScalingFactor` in `MarkerPatch.ini` allows fine-tuning the subtitle text size to personal preference.

<div align="center">
  <table>
    <tr>
      <td width="50%"><img style="width:100%" src="assets/scaling_off.png"></td>
      <td width="50%"><img style="width:100%" src="assets/scaling_on.png"></td>
    </tr>
    <tr>
      <td align="center">4K Vanilla</td>
      <td align="center">4K MarkerPatch</td>
    </tr>
  </table>
</div>

## Raw Mouse Input

Implements proper raw mouse input to fix sensitivity issues. This works similarly to the existing "Dead Space 2 Mouse Fix" mod with several improvements:
- Added support for zero-gravity areas. (the original mouse fix didn't work properly in zero-G)
- Sensitivity scaling now matches the in-game sensitivity settings more accurately.
- Does not interfere with controller inputs when switching between mouse and gamepad.

The fix decouples mouse sensitivity from the game's framerate, providing consistent aiming regardless of FPS.

## Input Device Filtering

Blocks all DirectInput devices except mouse and keyboard to prevent unwanted camera spinning from devices like racing wheels, flight sticks, and other peripherals. This also removes a slow XInput compatibility c