# OpenPuck
Opensource firmware for NRF52840 Pro Micro that copycats the Steam Controller 2 Puck and allows emulation of Xbox, Switch, and PS3/4/5 controllers and also includes an independant lizard mode (which can work on UAC prompts/task manager/etc). The Switch and PS3 modes have been verified to work on real consoles and Switch, PS4/5 modes have gyro (and touchpad where available) hooked in. Back 4 buttons are mappable for all emulated modes.

> [!WARNING]
> Every part of this project _HEAVILY_ used LLMs*

# The Steam Controller 2
Released in 2026, the Steam Controller 2 represents the peak (IMO) of controller design. Trackpads, gyro, 4 back buttons, all with the flexibility of Steam Input brings the amazing flexiblity of the Steam Deck's controls to gaming PCs in general.

The "puck" is what the controller uses for wireless communication with the host device. It can handle 4 controllers paired to it at the same time and can run at a very low latency with all 4 connected. While the controller has a bluetooth mode too it has over twice the latency so the puck is truly where it's at.

# The Problem
There are two fundamental problems with the controller:

1. The puck is not (yet) available for purchase separately from the controller so if you want a replacement or a second one (a single controller can pair to two) you're out of luck. Given Valve's track record I predict it'll never be available to buy as a separate accessory.

2. Steam Input isn't just a nicety, it's a requirement. This means that the controller is basically useless unless you have Steam running (outside of certain contexts that I personally consider niche). If, for example, you have gamepass and want to play FH6 through Gamepass you're gonna be in for a bad time and you'll probalby need specialized software running on your computer in order to make the controller work with it.

# What this project does
**Video Intro**

[![OpenPuck Intro](https://img.youtube.com/vi/gSaqO9oqq9s/0.jpg)](https://www.youtube.com/watch?v=gSaqO9oqq9s)

OpenPuck uses a [Pro Micro NRF52840](https://www.amazon.com/dp/B0GSZ7FD6T) ($8 on Amazon, possibly cheaper elsewhere) which uses a radio similar to the one being used by the controller and the puck. Once the arduino sketch is uploaded it emulates the puck over USB to Steam by default and allows pairing the controller normally (almost, the lizard mode for when Steam is off might not be 1:1). Latency [has been measured to be within 1ms of the official puck](https://www.reddit.com/r/SteamController/comments/1u754ze/complete_latency_testing_of_openpuck_project/).

At any point you can hold all 4 back buttons and press X to switch over to ***Xbox mode** which maps all canonical inputs to their expected counterparts (plus L4 -> LB, L5 -> L3, etc which are configurable). In this mode the right trackpad acts as a mouse but at present this only works in Android and SteamOS.

Similarly you can hold all 4 back buttons and press Y to switch (teehee) over to a **Switch mode**. This emulates a pro controller full with gyro and haptics. There's other modes as well:

| Button combo (configurable) | Mode | Comment |
|---|---|---|
| back-4 + A | Steam | Steam Controller Mode |
| back-4 + B | Lizard | Lizard mode, even if Steam is open |
| back-4 + X | Xbox | Xbox 360 Controller |
| back-4 + Y | Switch Pro | Switch Controller + Gyro + Haptics |
| WebUSB panel → mode 4 | Hori Pad | Switch mode with no gyro or haptics |
| WebUSB panel → mode 5 | DualSense + Gyro + Trackpad | PC only |
| WebUSB panel → mode 6 | DS4/HIDGYRO + Gyro + Trackpad | PC only |
| WebUSB panel → mode 9 | PS3 DualShock 3 / Sixaxis | Enumerates on a real PS3 (+ gyro/haptics) |

I'm also adding various QOL items as I go as well. For example having to hold the Steam button for like 6 seconds feels like an eternity. If Steam is open you can do Steam + Y for a shutdown. I'm adding Steam + Y for 2 seconds as a shutdown chort in ALL modes now.

Note: to use the Switch mode on a real Switch you'll need to [enable the pro controller wired communication option](https://www.nintendo.com/en-gb/Support/Troubleshooting/How-to-Enable-Disable-Pro-Controller-Wired-Communication-1516284.html).

### A note on the Lizard mode:
The Lizard mode behaves similarly to how the controller behaves when Steam is closed, but this will work even when Steam is open. This has a few advantages
the biggest one being that you can use inputs when a high privilege application is in the foreground (like the Task Manager, when using Steam if you wanna be able to do that Steam must be run as admin).

Additionally it has some shortcuts that might be useful: Steam + L5/R5 will do volume control, RB is Alt so you can RB + Select to move through windows, LB is Ctrl 
and Steam + L4 ls Ctrl + Alt + Delete.

# How to install/use it
You will need to flash OpenPuck.ino onto a compatible microcontroller. The easiest way to do this is to grab a uf2 file from the GitHub releases and drag and drop it onto the folder 