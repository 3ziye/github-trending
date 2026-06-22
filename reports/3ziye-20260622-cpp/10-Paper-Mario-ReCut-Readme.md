# Paper Mario ReCut

![Paper Mario ReCut title logo](assets/title_logo.png)
### <img width="1285" height="994" alt="Pic1" src="https://github.com/user-attachments/assets/47b4af91-d8b3-4905-a525-ad5b05453eb8" />
Paper Mario ReCut is a native Windows PC recompilation project for *Paper Mario* on Nintendo 64. It is built around the N64 recompilation toolchain, RT64 rendering, local legal ROM setup, live texture replacement, and the bundled Paper Atlas Tool for editing dumped texture pieces.

This repository does not include ROM files, extracted ROM assets, save files, generated TOML, or generated recomp output. Release builds follow the Zelda64Recomp-style model: the app is already built, and the launcher asks for your legally dumped Paper Mario (U) ROM, validates it by hash, and stores it locally under that user's own `user` folder. Players do not need CMake, WSL, Git, compilers, or dependency downloads to launch the game.

## Clarification

There seems to be a lot of speculation about what this project is and how it came to be.

This started as a hobby project made for fun with the help of AI to get N64Recomp to work smoothly with the Paper Mario decomp. As many people who have tried generating the necessary files for N64Recomp know, the process can be tedious and, for many, not worth the time. I know a lot of people give up before getting very far. This project has existed for me a lot longer than the repo as well. I only created it when I had something to work with.

My workflow also uses AI integration for formatting and optimization as a final pass before changes are pushed to the GitHub repo. Unfortunately, even though it is supposed to avoid pushing anything in my workspace that could involve potentially illegal content, it treated the generated TOML file as safe to push. I glanced over it and missed the issue, which was not intentional. That has since been fixed.

This is just a fun project for me. I am not trying to claim that I was first, take credit from anyone else, or do anything that could hurt the scene. I apologize for anything that made it seem that way.

I have a lot of respect for HarbourMasters, and I would not mind or care if their version becomes the top-rated and most-played version while mine stays in the shadows. I do this for fun and preservation, which I believe is the real purpose behind projects like this.

I am new to this scene, and I am sorry for the mistakes I've made.

**False Stuffs:** 
This project was not fully “vibe coded” either.

Paper Atlas was created long before this project existed. I repurposed it for this project, which I have already explained.

I also do not know where the claim is coming from that the ROM check does not work. The project uses hash verification and the supplied ROM for N64Recomp. I have tried every way I can think of to recreate that claim, but I have not been able to reproduce it unless a clone was modified to behave that way. This was built in the exact manner the N64ZeldaRecomp is minus the cool fancy launcher so if there are issues in that way then there are other concerns.

N64Recomp uses the ROM provided to it during the static recompilation process. The ROM is supplied by the user, used by the tool, and then moved to the user folder after it has already been provided for later use by N64Recomp. Based on what I have tested, I suspect that some people making this claim may not have been testing in a clean-room setup.

The so called game assets included are not in any way from the ROM or assets therof. No assets from the ROM are included in the release PERIOD. They simply need to share their HASH references so they know where they need to replace said textures.

We need to stop giving so much weight to people who appear to have personal vendettas against AI and are trying to sabotage anything useful that may come from it. I chose to release this because Battleship has already proven to be an amazing port, and the possibilities these tools create for preservation are more important than people’s egos.

In the meantime I've been working on some of the stuff that doesn't work in the current release and I'm sure those who choose to play will be surprised and happy about what's been achieved. Update Soon!!

## Features

- PRESS F1 TO ACCESS THE MENU (Might change to ESC not sure yet lol)
- First-run legal ROM setup with local validation.
- Native launcher with Select ROM and Start Game flow.
- Windowed RT64 renderer integration.
- Graphics options menu with live-applying renderer settings.
- Live Texture Replacement toggle via F2.
- One-shot texture dumping with an in-window percentage and dump count.
- Continuous Dump mode for capturing newly created textures while the game keeps running.
- Paper Atlas Tool sidecar built for easy texture replacement and editing.
- Controller and keyboard configuration windows are present and still being expanded.

NOTE: The current Gamepad Implementaion will auto bind controls to known SDL controllers and the re