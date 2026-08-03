### REACH/3/ODST Now Playable in VR 
### Halo 3 first-person vehicles are here. Reach and ODST first-person vehicles are up next.

## 🆕 What's new in 0.3.2

1. **Halo 3 first-person vehicles** — sit in the vehicle instead of floating
   behind it, with stable vehicle-relative hands, a hidden body, seat
   recentering, and comfort controls in `halomccvr.cfg`.
2. **Vehicle view follow** — optionally follow ground-vehicle yaw and pitch for
   a more connected ride; aircraft remain yaw-only.
3. **Halo 3 animated crosshair restored** — native authored reticle animation
   is back without sacrificing the tested capture cadence.
4. **Reach damage-bloom crosshair fix** — the crosshair stays visible when a
   damage reaction would otherwise push the captured art out of frame.

## 🚧 What I'm working on RN
| Feature                                            | Status         |
| -------------------------------------------------- | -------------- |
| Xbox App / Game Pass Support                       | ✅ Added in 0.3.1 |
| ALVR / Virtual Desktop / Meta Link Support         | ✅ Fixed in 0.3.1 |
| Cutscene 3d Theater Mode                           | ✅ Added in 0.3.1 |
| Complete F1 Menu UI Restructure and Reorganization | ✅ Added in 0.3.1 |
| Reach: black-world fix on sniper                   | ✅ Fixed in 0.3.1 |
| Halo 3 first-person vehicles                       | ✅ Added in 0.3.2 |
| Reach first-person vehicles                        | 🟡 Up next |
| ODST first-person vehicles                         | 🟡 Up next |
| SMAA T2X Support                                   | not possilbe atm |
| Gamepad support/Head-Aiming Mode                   | 🟡 In Progress |
| Scopes and weapon zoom fixes                       | 🟡 In Progress |
| Theater mode subtitles                              | 🟡 In Progress |

> **DO NOT ACCEPT FIXES FOR THIS MOD FROM OUTSIDE SOURCES. WE DON'T KNOW WHAT'S
> IN THEM.**
>
> [Quad-Views-Foveated](https://github.com/mbucchia/Quad-Views-Foveated) is
> **optional and no longer required** — try it only if you want a GPU
> performance boost.
>
> **Steam VR players: use the SteamVR Beta branch**, with SteamVR set as your
> default OpenXR runtime — that's what makes Virtual Desktop's VDXR mode work.
>
> **WINSTORE/XBOX APP: do not rename your game .exe to the Steam version.** The
> launcher now looks for the real Game Pass executable — if you renamed
> `MCCWinStore-Win64-Shipping.exe` in a previous update, rename it back.
>
> Compatibility across headsets may vary. If it doesn't work, try a different
> way to connect if you can. or leave an issue with your spec set up. I'll try to find a play tester with your headset.
>
> **Let me know in the [issues](https://github.com/pancreations/Halo-MCC-VR/issues)
> ** and someone or I can help you.
>
> **Please list your specs if you're having issues.** Saves me a bit of time

# Halo MCC VR

> **Hi, I'm [pancreations](https://www.instagram.com/pancreations/)** — a 3D
> animator. I really don't like AI art, but I also really want to play MCC in
> VR, so I'm taking one for the team. Follow me on Instagram if you like silly
> animations made by humans in Blender. 
>
>
A native OpenXR VR mod for Halo 3, Halo 3: ODST and Halo: Reach in Halo: The
Master Chief Collection — both the Steam edition and the Microsoft Store / Xbox
app (Game Pass) edition.

The current release is
[Halo 3 Vehicle Update — MCC VR Alpha 0.3.2](https://github.com/pancreations/Halo-MCC-VR/releases/tag/MCC_VR_ALPHA_0.3.2).
It adds **first-person Halo 3 vehicles** with vehicle-relative hands, body
hiding, seat recentering, optional view follow, and comfort tuning. It also
restores Halo 3's animated authored crosshair and fixes the Reach crosshair
disappearing during damage bloom. It is an alpha: use it at your own risk,
launch only without anti-cheat, and expect incomplete hardware and gameplay
coverage.

## What works

- Per-eye stereo and 6DOF head tracking.
- Motion-controller input, weapon aim, arm IK, snap/smooth turning, melee,
  grenades, and menu control.
- Native HUD, authored floating weapon crosshair, scopes, resolution scaling,
  comfort controls, and a shared F1 configuration menu.
- Halo 3 campaign behavior, including cutscenes, pause/resume, death/respawn,
  and mission transitions.
- Halo 3 first-person vehicles: a cockpit-style seat view, stable
  vehicle-relative hands, optional body hiding, seat recentering, and an
  optional ground-vehicle view-follow mode. New in 0.3.2.
- ODST stereo, controls, weapons/hands, native HUD, cutscenes, vibration,
  death/respawn recovery, and one tested drivable car.
- Halo: Reach stereo, controls, weapon aim, hands/gun, HUD, cutscenes and
  vibration, plus native vehicle controls and a fix for sniper-triggered black
  static-world geometry, both new in 0.3.1. Reach is new in 0.3.0 and is the
  earliest of the three titles.
- Both MCC editions from one download: S