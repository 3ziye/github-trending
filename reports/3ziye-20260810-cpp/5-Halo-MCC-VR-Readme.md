<img width="1280" height="640" alt="heromxall" src="https://github.com/user-attachments/assets/6682b4bc-15d3-476f-b6f5-f6de82d1c0cd" />
### REACH/3/ODST Now Playable in VR 
### First-person vehicles are here — in all three games.

> # ⚠️ Before you drive: you have to set up your own seats
>
> Every seat ships with a starting camera position, but that is a **starting
> point, not a finished setting**. Everyone's height, play space and headset sit
> differently, so a seat that looks right for me will be too low, too far
> forward or too far back for you. **This is normal and it is a one-time job per
> seat.**
>
> 1. Get into the seat you want to fix — driver, passenger, gunner or turret.
> 2. Press **F1** and open the **Vehicles** category.
> 3. Move **Seat forward (m)**, **Seat height (m)** and **Seat left / right (m)**
>    until it feels right.
> 4. Get out. It saves itself.
>
> While you're **in a seat**, those sliders move **that seat only** — a
> vehicle's driver, its passengers and its gunner each remember their own spot,
> in each game. Do the ones you actually use and ignore the rest.
>
> While you're **on foot**, the same sliders set the shared starting point every
> seat you haven't adjusted follows. That one moves all three games at once, so
> use it for a quick overall height nudge. If you push it somewhere bad, a
> **Reset the universal trim** button appears under the sliders.

## 🆕 What's new in 0.3.3

1. **First-person vehicles in ODST and Reach** — the Halo 3 vehicle mode from
   0.3.2 now covers all three games. Sit in the seat instead of floating behind
   the vehicle, with your hands on the wheel, your own body hidden, and every
   seat placed: drivers, passengers, gunners and turrets.
2. **Turrets hold still and shoot where you're pointing** — mounted turrets in
   Halo 3 and ODST used to twitch up and down chasing the crosshair. They sit
   still now, and the reticle rides the gun barrel, so what you see is where the
   shot goes.
3. **Passenger guns shoot down the sight line** — riding shotgun in a Warthog,
   your shots now leave the line you're actually aiming down at every range,
   instead of only lining up at one distance.
4. **The brightness slider works in ODST and Reach** — `game_brightness` used to
   move Halo 3 only. One slider now moves all three games.
5. **No more loading a level twice** — the mod no longer touches a game while
   its level is still loading, which is what used to bounce you back to the main
   menu on the first load.
6. **Faster into VR** — ODST reaches stereo about two seconds sooner, and the
   startup scan every game does is roughly 7× faster.
7. **Your seat settings can't be wiped any more** — an unrecognised vehicle used
   to write over the shared setting that all three games fall back on. Each
   vehicle now keeps its own line, and there's a one-click reset if the shared
   one ever looks wrong.

## 🚧 What I'm working on RN
| Feature                                            | Status         |
| -------------------------------------------------- | -------------- |
| Xbox App / Game Pass Support                       | ✅ Added in 0.3.1 |
| ALVR / Virtual Desktop / Meta Link Support         | ✅ Fixed in 0.3.1 |
| Cutscene 3d Theater Mode                           | ✅ Added in 0.3.1 |
| Complete F1 Menu UI Restructure and Reorganization | ✅ Added in 0.3.1 |
| Reach: black-world fix on sniper                   | ✅ Fixed in 0.3.1 |
| Halo 3 first-person vehicles                       | ✅ Added in 0.3.2 |
| ODST first-person vehicles                         | ✅ Added in 0.3.3 |
| Reach first-person vehicles                        | ✅ Added in 0.3.3 |
| Turret aim + brightness in ODST/Reach              | ✅ Fixed in 0.3.3 |
| Halo 4                                             | 🟡 Up next |
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
> **Let me know in the [issues](https://github.co