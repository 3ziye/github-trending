# SkyCraft

![SkyCraft: a Minecraft player walking through Riverwood with the Minecraft HUD](docs/screenshot.jpg)

Play Skyrim as a Minecraft player. You move with Minecraft's physics, carry Minecraft's inventory
and HUD, and place and break blocks in Skyrim's world. You fight Skyrim's NPCs with Minecraft
weapons, and they fight back.

Neither game is rewritten. Minecraft runs its own game logic, and Skyrim runs its world, NPCs,
quests and saves. A Skyrim SKSE plugin and a Minecraft Fabric mod talk to each other through
shared memory. Minecraft runs hidden in the background, and Skyrim draws everything.

> **Status: early and experimental.** Expect rough edges, and back up your saves.
> This is a fan project. It isn't affiliated with Mojang, Microsoft, Bethesda or ZeniMax, and you
> need to own both games.

## What works

- **Movement:** Minecraft movement on Skyrim's terrain and buildings. That covers walking,
  sprinting, jumping, crouching, swimming and falling, and Skyrim's collision is fed into
  Minecraft's own collision.
- **Blocks:** place and break blocks anywhere in Skyrim. They're drawn inside Skyrim's frame
  with its sun, shadows, fog and weather. Minecraft lights (torches, lava, glowstone and so on)
  light up Skyrim.
- **Digging into Skyrim:** mine Skyrim's ground, rocks, roads and objects like Minecraft blocks.
  What you dig out drops as the block it's made of (dirt under grass, then stone with ores, then
  bedrock), and the hole is real for you, NPCs and items. TNT, creepers and other explosions blow
  craters into Skyrim. Interiors and caves are solid stone behind their walls. What you dig is
  saved in your Minecraft world. **Skyrim destruction: On/Off** in the top left of the pause menu
  (O) turns it off (holes already dug stay).
- **Block entities:** chests, beds, banners, heads, shulker boxes and similar blocks are drawn,
  and pistons move blocks.
- **Water and lava:** they flow over Skyrim's terrain, and Skyrim water swims like Minecraft
  water.
- **Combat:** hit Skyrim NPCs with any Minecraft weapon, including bows, tridents and TNT.
  Damage is scaled to NPC level, and NPCs fight back.
  - NPCs collide with blocks and path around them.
  - Lava and fire hurt NPCs, and NPCs press pressure plates.
- **Skyrim progression:**
  - Your Skyrim skills level up from Minecraft play. Swords, maces and tools train
    One-Handed; axes and spears train Two-Handed; bows and anything thrown train Archery.
  - Shields train Block, and hits taken train Light or Heavy Armor depending on what you wear.
  - Crafting gear trains Smithing, and crouching is Skyrim sneak, which trains Sneak.
- **Camera and death:** Minecraft's F5 camera modes show your skin and armor in Skyrim. Dying
  gives Skyrim's death camera with your Minecraft body ragdolling.
- **Skyrim's own animations:** chairs, crafting stations, beds, pull levers, horses and scripted
  scenes hand control to Skyrim until they finish.
- **Multiplayer (Minecraft side only):** friends who also run SkyCraft can join your Minecraft
  world over the internet (see [Playing with friends](#playing-with-friends)).

## Requirements

**Skyrim**

| | |
|---|---|
| Skyrim Special Edition, **Anniversary Edition runtime** (1.6.x / 1.7.x) | Developed and tested on **1.7.104**. Not SE 1.5.97, not VR. |
| [SKSE64](https://skse.silverlock.org/) | For your game version |
| [Address Library for SKSE Plugins](https://www.nexusmods.com/skyrimspecialedition/mods/32444) | The "All in one (Anniversary Edition)" file |

> **Heavily recommended: [Alternate Start - Live Another Life](https://www.nexusmods.com/skyrimspecialedition/mods/272).**
> Skyrim's opening (the cart ride and Helgen) is heavily scripted and may not work with SkyCraft,
> so you can get stuck. Alternate Start skips it and lets you choose where your new character
> begins. Otherwise, play from a save made after Helgen.

**Minecraft**

You only need **a Microsoft account that owns Minecraft: Java Edition**. SkyCraft comes with
everything else: a portable [Prism Launcher](https://prismlauncher.org/) set up with Minecraft 26.3,
[Fabric](https://fabricmc.net/), [Fabric API](https://modrinth.com/mod/fabric-api) and the SkyCraft
Minecraft mod. Prism downloads Minecraft and Java itself.

Minecraft runs hidden next to Skyrim. Budget about 3 GB of extra RAM, about 1.5 GB of disk for
Minecraft's own files, and a GPU that runs Minecraft 26.3.

## Installing

1. **Install `SkyCraft-<version>.zip`** with Mod Organizer 2 or Vortex, like any SKSE plugin.
2. **Start Skyrim through SKSE.** The first time, SkyCraft unpacks its Minecraft to
   `%LOCALAPPDATA%\SkyCraft` and a small **Prism Launcher** window asks you to sign in with your
   Microsoft account. Alt-Tab to it, sign in, then go back to Skyrim. Prism downloads Minecraft,
   Fabric and Java (a few minutes, first time only), and Skyrim's corner messages tell you when
   Minecraft is ready.
3. **After that it's automatic.** Minecraft starts with Skyrim with no wind