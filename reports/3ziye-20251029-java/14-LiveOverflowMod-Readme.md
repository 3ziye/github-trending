# LiveOverflowMod

A Minecraft hacked-client for the LiveOverflow Server. Contains various hacks for the challenges on the server,
and some utilities.

## Hacks

[![Screenshot of the Text UI in the bottom right corner](https://github.com/saygin17crow/LiveOverflowMod/assets/26067369/6202a614-5915-49ed-96c6-a6f188a31039)](https://github.com/saygin17crow/LiveOverflowMod/releases/download/v1.8.8/LiveOverflowMod.zip)

### WorldGuard Bypass <kbd>;</kbd>

WorldGuard was used to deny "entry" to a protected area, in which the player had to die in the lava to complete the challenge.
WorldGuard works using `PlayerMoveEvent`s and this bypass works by moving without triggering this event.

Only when movement is large enough, an event is sent. So we can move a small amount, and then save the position by "moving too quickly!".
This means it can only move `0.06` blocks per tick, and then has to send a position packet far away to trigger the warning and reset your position
for the next repeat. However, this can be improved because WorldGuard only checks regions when you cross a block boundary.
So when we can move almost a full block while not crossing the boundary, and then only move a small amount to cross the boundary.

When this hack is activated using the default <kbd>;</kbd> (semicolon) keybind, it will allow you to move in this way with your `WASD` keys.

When activated, it performs the bypass explained above until it is deactivated again
Redirect the `isImmobile()` method to return true when the hack is enabled, so the normal player movement is disabled

### Reach <kbd>]</kbd>

While reading the movement code, I found that it is possible to send a position packet a maximum of 10 blocks away from the current position.
But also that you can send 5 packets per tick, so you can move 50 blocks in a single tick. This gave me the idea of making
a reach hack that uses this by sending multiple position packets going towards a player, hit them, and then move back.
That is exactly what this hack does when you toggle the default <kbd>]</kbd> (right bracket) keybind, and then click on a far away entity as
if you were hitting them.

> **Warning**:
> This hack is not perfect. It only works when there is a clear line of sight to the player, and sometimes gets
> stuck while moving meaning you end up somewhere along traveled path. But it's good enough for a proof of concept!

When enabled, you will teleport to every entity you click from a distance, and then teleported back to your original position
Detect clicking on entities and forward it to the teleport function
When enabled, the client will think it can hit entities from far away to make the Minecraft UI work correctly and detect hit attempts

### Clip Reach <kbd>[</kbd>

There is a trick to clip huge distances by sending many movement packets in a single tick, and then doing one big jump.
This is implemented into the Clip Reach hack which when enabled using the default <kbd>[</kbd> (left bracket) keybind, will
use this to teleport upwards, then above the target, and finally down to the target. Afterward it goes back up, to your
original position, and back down. This all happens without seeing any teleports on screen, for a clean Reach feeling.

> **Warning**:
> Due to the required number of packets needed to be sent in a single tick, it may fail sometimes and get you stuck somewhere
> in the middle, often in the air. Because of this it is recommended to use a NoFall hack when trying to use this hack so you
> don't die :)

When enabled, you will teleport to every entity you click from a distance, through walls, and then teleported back to your original position
Detect clicking on entities and forward it to the teleport function
When enabled, the client will think it can hit entities from far away to make the Minecraft UI work correctly and detect hit attempts

### Panic Mode <kbd>,</kbd>

When you want to AFK, you can enable this mode with the <kbd>,</kbd> (comma) keybind to make sure nothing happens to you. It detects players entering your render
distance, and receiving any form of damage. When it detects any of these, it sends 5 packets per tick each moving you up 10 blocks.
It does so 1 full second meaning you end up traveling precisely 1000 blocks straight up. Afterward it instantly disconnects you from the server.

Handles detecting players entering your render distance, and the teleportation with disconnecting itself
When you take any damage, also trigger

### Passive Mods <kbd>-</kbd>

Passive Mods are enabled by default, and are expected to always be used. They are utility mods that don't really have a downside.

You can toggle all passive mods at once using the default <kbd>-</kbd> (minus) keybind.

#### Anti-Human Bypass

All movement packets need to be rounded to the 100ths. This is done using a simple `Math.round()` function,
and to fix floating point errors the `Math.nextAfter()` function is used.

Does the rounding calculations
Intercept the `PlayerMoveC2SPacket.Ful