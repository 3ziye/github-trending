# Forbric

English | [简体中文](README.zh-CN.md)

**One Minecraft instance that runs Fabric mods, Forge mods and NeoForge mods at the same time.**

Version 0.3.0 · Minecraft 26.2

## What it does

Minecraft mods come in three kinds, and normally you have to pick one. A mod is built for **Fabric**, or
for **Forge**, or for **NeoForge**, and it only works on the one it was built for. Put a Fabric mod into
a Forge game and nothing happens. So most people keep several separate setups, and whichever one they
start, most of their mods are sitting in the other ones.

Forbric is a fourth thing you install instead of those three. You put **every** mod into **one** folder —
Fabric, Forge and NeoForge mixed together, no sorting — and Forbric opens each file, works out what kind
it is, and loads it. All of them are running in the same world at the same time.

It also gives you one list of everything you have installed. The pause menu and the title screen get a
Forbric mods button, and from that list you can open a mod's own settings screen, whichever of the
three it belongs to (for Fabric mods, only when Mod Menu is installed too).

**You may have heard of Kilt or Sinytra Connector.** Those are mods you add to a normal loader, and they
re-create one side's features inside the other — a translator in the room. Forbric is the loader itself.
Fabric Loader and the loaders inside Forge and NeoForge never start; Forbric does their job — finding the
mods, starting them, running them in order — and tries to do it the way each mod's own loader would. Your
mods call the real Fabric API and the real Forge and NeoForge code; that part is not re-created. So this is
not three loaders running side by side: it is one new loader that puts all three kinds of mods, and the
real code they rely on, into one game.

But Forge and NeoForge both change Minecraft, often in the same spots, and one game can hold only one
version of each spot, so Forbric mostly keeps NeoForge's. Its own glue then keeps the other mods working:
it passes game events on to Forge mods, moves Fabric mods' changes to where the code now sits, and lets
mods from different loaders hand each other items, fluids and energy. That glue is translation too, and
it is not finished, which is one reason some mods still fail.

Connector is mature and Forbric is not, so if Connector already runs the mods you want, use Connector.
Forbric is for the cases it cannot reach.

## How to install

### Before you start

- **A launcher that starts versions from your `.minecraft/versions` folder.** Forbric has been tested
  with **PCL2** on Windows. HMCL reads the same files and should work, but has not been tested yet. The
  official Minecraft Launcher has not been tested either (see step 6). Prism Launcher and MultiMC keep
  their own instances and will not see Forbric.
- **Java.** If you can already play Minecraft, you have it. The installer finds the copy your launcher
  downloaded, even if you never installed Java yourself.
- **An internet connection**, and about 730 MB of free disk while it works (about 190 MB is kept
  afterwards).

You do **not** need to install Minecraft 26.2 first. If you do not have it, the installer downloads it.
You also do **not** need Fabric, Forge or NeoForge, and you do not need to find any other files: the
installer downloads and builds everything Forbric needs. Your mods still need their own prerequisites as
usual, for example Fabric API for most Fabric mods.

### Install

1. Open the [latest release](https://github.com/Ray-T-r/Minecraft-Forbric-mod-loader/releases/latest).

2. Download **two** files into the **same folder**:

   | You are on | Download |
   | --- | --- |
   | Windows | `forbric-kernel-installer-0.3.0.jar` **and** `Forbric-Installer.bat` |
   | macOS | `forbric-kernel-installer-0.3.0.jar` **and** `Forbric-Installer.command` |
   | Linux | `forbric-kernel-installer-0.3.0.jar` (run it with `java -jar`) |

3. **Double-click the `.bat` (Windows) or the `.command` (macOS).** It looks for Java, including the copy
   a launcher keeps in the usual Minecraft folder, and starts the installer with it. On some Windows PCs,
   double-clicking the jar itself only flashes a black window, because Windows was once told to open
   `.jar` files in a way that does not work; the script avoids that. If double-clicking the jar does open
   the installer window, that is fine too: it is the same installer.

   On macOS the first time, you may need to right-click the file and choose **Open**, then confirm. That
   is macOS being careful about downloads, not an error.

4. **A window opens.** The only field that matters is **Game directory** — the `.minecraft` folder your
   launcher uses. It starts out filled in with the usual place for your system:

   - Windows — `C:\Users\<your name>\AppData\Roaming\.minecraft`
   - macOS — `~/Library/Application Support/minecraft`
   - Linux — `~/.minecraft`

   If your launcher keeps `.minecraft` somewhere else (PCL2 and HMCL can keep