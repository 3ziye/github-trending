# Quake 4 The Awakening Release

Src folder - The alpha release contained the PDB file and helped us recreate the Quake 4 The Awakening Engine. 
The game code however didn't come with a PDB file so the game code included is only for the retail game.
YOU CAN RUN THE GAME WITHOUT THE SOURCE CODE RECREATION TO RUN THE EXPANSION PACK.

You will need a copy of the retail game(you can buy it on steam).

## Building the reconstructed engine and game DLL

The build is centralized in `src/CMakeLists.txt`; it does not consume external
CSV source lists. From the repository root, run:

```powershell
Set-Location src
cmake --preset windows-x86-debug
cmake --build --preset windows-x86-debug --target q4_runtime
```

Come join us on discord!
https://discord.gg/y2hp2S8c9Y

I came across this at a very sad point in my life, it was on a hard-drive on a vintage computer I bought
off Amazon. Litterally this essentially saved my life, I was going through a divorce and just happened
to come across something like this was insane.

Props to the team that made it and hopefully the community can make something awesome with it!
 
Check out the rest of my projects:
https://github.com/jmarshall23

If you want to get ahold of me for work(I'm 16 year veteran of the game industry, just got laid off due to the AI surge), 
specifically I do graphics engineering, port work, low level platform work, technical director work, complex gameplay code,
etc. I've worked on over 20 games or so, my e-mail address is justinmarshall20@gmail.com
