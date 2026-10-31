# MacNativeGames

<p align="center"><b>A technical exploration: can a Nintendo Switch game's NVN graphics be ported to Metal?</b><br>
Tested with your own copies of Tears of the Kingdom and Breath of the Wild on Mac, iPhone and iPad. Not an emulator: the game's own ARM64 code runs directly on Apple chips.</p>

[English](#english) | [中文](#chinese)

# English

## Legal

**You must own the game.** Use this project only with games that you bought, and with keys and system files dumped from your own Nintendo Switch. This is an independent, non-commercial project. It is not affiliated with, endorsed by, or sponsored by Nintendo. The Legend of Zelda and Nintendo Switch are trademarks of Nintendo.

The repository contains no game content and distributes none: no game program, art, text, audio, shaders or keys. Everything the game needs is made on your own computer from your own files when you build the app. The app you build contains the game, so it is for your own use only; do not share it. What the repository does hold is the information needed to make the port work: the patch code, the addresses and hashes used to check your files, and the [shared shader list](docs/shader-list.md), which names shaders and bind states but contains no shader code.

Apple, Mac, iPhone, iPad, Apple Vision Pro and Metal are trademarks of Apple Inc.; this project is not affiliated with Apple. Other game titles and trademarks named here belong to their respective owners.

Whether dumping games, keys and system files is legal depends on where you live; check and follow your local laws.

Issues and pull requests that contain or ask for game files, keys or firmware will be deleted.

## About

**This project is a technical exploration, mainly feasibility experiments and analysis.** The Nintendo Switch is an ARM system (an ARM64 CPU in NVIDIA's Tegra X1), and Apple chips are ARM64 as well, so we want to test whether its games can, technically, be ported to Apple chips. It started from one question: can the NVN graphics a Switch game was written for be rebuilt faithfully on Apple's Metal, and can the game's own ARM64 code run directly on Apple chips without an emulator? Tears of the Kingdom and Breath of the Wild are the test cases, because they push the graphics API hard. The repository records the experiments, measurements and findings along the way; it is a study of the technique, not a game distribution. **It does not encourage piracy:** use only your own game data, dumped from a game you bought and from your own Switch, never game files, keys or firmware downloaded from the internet or obtained from anyone else.

How it works: bring your game file (XCI or NSP) and your `prod.keys`; one script builds a Mac app or an unsigned iPhone/iPad IPA. The game's own ARM64 code runs directly on Apple chips (rewritten where the operating system requires it), the Switch system services are answered by a small host, and the game's NVN graphics are rebuilt on Metal. The iOS build requires iOS/iPadOS 26 and iPhone 14 or newer; version 1.4.3 has been played on an iPhone 14 and an iPad, see [iPhone and iPad](docs/install.md#iphone-and-ipad). Details are in [How it works](docs/how-it-works.md).

| Game | Version | Platform | Status | Folder |
|---|---|---|---|---|
| The Legend of Zelda: Tears of the Kingdom | 1.0.0, 1.2.1, 1.4.3 (1.1.2 builds too) | Mac, iPhone, iPad; Apple Vision Pro (windowed, early) | Supported | [`games/totk`](docs/install.md) ([Vision Pro](docs/install.md#apple-vision-pro)) |
| The Legend of Zelda: Breath of the Wild | 1.6.0, 1.9.0 | Mac; 1.6.0 also on the iPhone | Supported | [`games/totk`](docs/install.md#breath-of-the-wild) (shared runtime), list in `games/botw` |
| Super Smash Bros. Ultimate | 13.0.2, 13.0.5 | Mac | Community port | [`games/ssbu`](games/ssbu/README.md) |
| Super Mario Odyssey | 1.3.0, 1.4.1 | Mac | Community port, early | [`games/odyssey`](games/odyssey/README.md) |
| Bayonetta 3 | 1.2.0 | Mac | Community port, work in progress | [`games/by3`](games/by3/README.md) |
| Super Mario Bros. Wonder | 1.0.0, 1.2.1 | Mac | Community port, early | [`games/wonder`](games/wonder/README.md) |
| Ori and the Blind Forest: Definitive Edition | 1.0.1 | Mac | Community port | [`games/ori`](games/ori/README.md) |
| Super Mario Party Jamboree | 2.3.0 | Mac | Community port, experimental | [`games/jamboree`](games/jamboree/README.md) |
| Mario vs. Donkey Kong | 1.0.1 | Mac | Community port, early | [`games/mvdk`](games/mvdk/README.md) |
| Metroid Dread | 1.0.0 | Mac | Community port, early | [`games/dread`](games/dread/README.md) |
| Unicorn Overlord (Asian release) | 1.05 | Mac | Community port, early; DLC optional | [`games/unicorn`](games/unicorn/README.md) |
| The Legend of Zelda: Echoes of Wisdom | 1.1.0 | Mac | Community port, early | [`games/eow`](games/eow/README.md) |
| Animal Crossing: New Horizons | 1.2.1; 3.0.1 (experimental) | Mac | Community port | [`games/acnh`](games/acnh/README.md) |
| Octopath Traveler 0 | 1.0.3, 1.