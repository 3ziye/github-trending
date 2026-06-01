# Paper Mario ReCut

![Paper Mario ReCut title logo](assets/title_logo.png)
### <img width="1285" height="994" alt="Pic1" src="https://github.com/user-attachments/assets/47b4af91-d8b3-4905-a525-ad5b05453eb8" />
Paper Mario ReCut is a native Windows PC recompilation project for *Paper Mario* on Nintendo 64. It is built around the N64 recompilation toolchain, RT64 rendering, local legal ROM setup, live texture replacement, and the bundled Paper Atlas Tool for editing dumped texture pieces.

This repository does not include ROM files, extracted ROM assets, save files, or generated ROM-derived recomp output. On first run, the app asks for your legally dumped Paper Mario (U) ROM, validates it, and installs a local copy into that user's own `user` folder.

**Claims:** There seems to be a lot of speculation about what this project is and how it came to be.

This started as a hobby project made for fun, with the help of AI, to get N64Recomp to work more smoothly with the Paper Mario decomp. As many people who have tried generating the necessary files for N64Recomp know, the process can be tedious and, for many, not worth the time. I know a lot of people give up before getting very far.

My workflow also uses AI integration for formatting and optimization as a final pass before changes are pushed to the GitHub repo. Unfortunately, even though it is supposed to avoid pushing anything in my workspace that could involve potentially illegal content, it treated the generated TOML file as safe to push. I glanced over it and missed the issue, which was not intentional. That has since been fixed.

This is just a fun project for me. I am not trying to claim that I was first, take credit from anyone else, or do anything that could hurt the scene. I apologize for anything that made it seem that way.

I have a lot of respect for HarbourMasters, and I would not mind or care if their version becomes the top-rated and most-played version while mine stays in the shadows. I do this for fun and preservation, which I believe is the real purpose behind projects like this.

I am new to this, and I am sorry for the mistakes I've made.

In the meantime I've been working on some of the stuff that doesn't work in the current release and I'm sure those who choose to play will be surprised and happy about what's been acheived. Update Soon!!

## Features

- PRESS F1 TO ACCESS THE MENU (Might change to ESC not sure yet lol)
- First-run legal ROM setup with local validation.
- Windowed RT64 renderer integration.
- Graphics options menu with live-applying renderer settings.
- Live Texture Replacement toggle via F2.
- One-shot texture dumping with an in-window percentage and dump count.
- Continuous Dump mode for capturing newly created textures while the game keeps running.
- Paper Atlas Tool sidecar built for easy texture replacement and editing.
- Controller and keyboard configuration windows are present and still being expanded.

NOTE: The current Gamepad Implementaion will auto bind controls to known SDL controllers and the rebind system is currently in the works.

## Current Status

This is still an early working build. The game boots and the tooling is actively being shaped around Paper Mario as development continues.

Save states are implemented as an early runtime snapshot system. Slot saves and loads are queued onto Paper Mario's main game-loop boundary and store slots in `user/states/`. Treat them as testable while the runtime continues to mature. 

### Known issues:
1. Widescreen is currently broken, but it is still exposed for testing. Expect visual problems if you enable it. The normal 4:3 path is the intended play path for now.
2. Using Save States in it's current implementation will break the game. Avoid For Now.

## Runtime Folders

Local runtime data lives under:

```text
user/
```

Important subfolders:

```text
user/pm.n64.us.z64
user/states/
user/textures/dumps/
user/textures/replacements/
user/AtlasEditing/
```

Do not commit or distribute ROMs, save files, generated ROM output, local dumps, local replacements, or `user` folders.

## Paper Atlas Tool
<img width="1296" height="1058" alt="image" src="https://github.com/user-attachments/assets/fb50c23f-0cfe-470d-a20a-65d06c213a23" />

Paper Atlas Tool is included as a means for simple texture replacement and as it evolves will change the way Paper Mario will be experienced making texture modding very simple.
I originally was working on this tool for texture replacement for any N64 texture set but have repurposed it just for this and still has a lot of work to be done.

```text
tools/PaperAtlasTool/
```

Windows builds publish `PaperAtlasTool.exe` beside `PaperMarioReCut.exe`. You can open it from Graphics > Paper Atlas Tool or from the Texture Replacement window. If the expected dump or replacement folders are missing, the game and Atlas tool explain how to create them.

## Building

This source tree expects generated Paper Mario recomp output at:

```text
generated/paper_mario_