# Prometheus <!-- omit in toc -->

Hey and welcome, thanks for stopping by!
- [1. Usage](#1-usage)
  - [Download a Release](#download-a-release)
    - [Optional stuff](#optional-stuff)
    - [Patcher \& how it works](#patcher--how-it-works)
  - [Compilation](#compilation)
- [2. Game internals](#2-game-internals)
  - [Managers](#managers)
  - [ECS](#ecs)
  - [STU](#stu)
  - [DataFlow](#dataflow)
  - [Game Messages](#game-messages)
  - [Components](#components)
    - [STUPvPGameComponent 0x24](#stupvpgamecomponent-0x24)
    - [STUStatescriptComponent 0x23](#stustatescriptcomponent-0x23)
    - [Component 1](#component-1)
    - [MovementStateSystem](#movementstatesystem)
- [3. Broken stuff and why it's broken](#3-broken-stuff-and-why-its-broken)
- [4. Tips \& Tricks](#4-tips--tricks)
- [5. Contributions Welcome!](#5-contributions-welcome)
- [6. NOTE](#6-note)
- [7. Open Source libraries used](#7-open-source-libraries-used)
- [8. License and Contact](#8-license-and-contact)

# 1. Usage

If you havent already, download the 0.8 beta from [archive.org](https://archive.org/details/overwatch-beta-0-8-0-24919) and extract the files somewhere.
* ⚠️ Make sure that you don't download any malicious executable and verify that GameClientApp.exe is signed by Blizzard. The signature will get broken after applying the patcher.
* You can safely remove the BlizzardError directory.

## Download a Release

* Download a release.zip. Extract all files to the game directory.
* Rename prometheus.dll into inject.dll
* Execute patcher.exe. It will ask for an input GameClientApp.exe, select the one you have downloaded and verified.
  * The patcher will write a GameClientApp.patched.exe file into the same directory. The only thing this patched executable does is load inject.dll before running the game code itself.
* Congratulations, you're done :) Have a cookie 🍪

### Optional stuff

* Download the [MonaspaceXenon](https://monaspace.githubnext.com/) font and put the -regular.otf and -bold.otf in the directory of the game files.
* Download the [Font Awesome v6](https://fontawesome.com/v6/download) free desktop font files and put the .otf files into the game directory.
* Once first started, the library will create hashlibrary.json. You can add crc32 strings / elements to hash which will be displayed in various places where applicable. You can just add all the strings from the [overtools github repository](https://github.com/overtools/OWLib/tree/develop/TankLibHelper/DataPreHashChange). To do so add another root JSON element (an array) called "add" and put all your strings there.

### Patcher & how it works

The patcher itself just goes to TlsCallback_0 and patches some bytes so the executable loads inject.dll before anything else. inject.dll then restores the game to its original state, decrypts everything and hooks stuff. Afterwards it runs the game normally. This was achieved with just copying the bytes which lazy_importer created for the LoadLibrary function and then calling LoadLibrary with "inject.dll" as an argument.

## Compilation

* You need Visual Studio 2022. I have not tested it on any other platform
* Make sure to initialize the submodules / clone recursively
* Initialize the vcpkg repository with the ps1 file located at external/vcpkg/scripts/bootstrap.ps1
* Compile as Relaese/x64. No other configuration is tested  (some flags and settings are missing).

# 2. Game internals

## Managers
The first think Overwatch does is initialize all its "Managers". They handle things such as Dataflow, CASC, Window management, etc. This is the lowest level and not really interesting.

## ECS
Afterwards, all the Entity Admins get initialized. First the Lobby, then Game and finally Replay.

There is one Entity admin base class on which all others depend upon. The LobbyEntityAdmin includes some login and user information in the inherited class, though I have never really researched that.

The Game Enttiy Admin is the biggest one and contains amongst others:
* An uint that says "this is the local entity". This must reference the controller entity. Systems use Components 2F (local player component) and 20 (model reference component) out of that entity to display the local player on screen.
* A JAM virtual function table. This is used to send JAM messages contained in actions.
* A table of map callbacks. Systems can subscribe to map change events (for example if the map state changes from "Global Loading" to "World Loading")
* A virtual function table reference from the MirrorSystem, which systems can use to subscribe to pre and post component deserialization. When a server sends a component update it calls the callback functions that were registered.
* An Accessor which searches for an Entity with the PvPGameComponent and takes some information from that.
* An entityid referencing a static dataflow provider?
* A char indicating if this is the live game or not.

The replay entity admin is just a GameEntityAdmin with a few additional systems and the