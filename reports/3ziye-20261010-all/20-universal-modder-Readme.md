<p align="center">
  <img src="docs/media/banner.png" alt="universal-modder: mod any game. Point any AI coding agent at the PC games you own. Publish your mods, remix other people's, and make new ones." width="100%">
</p>

<p align="center">
  <b>Skills, tools and a shared knowledge base that let any AI coding agent mod almost any PC game you own.</b><br>
  The agent finds the game, works out the engine and the route, reads the real code, builds the mod, makes art, 3D and sound
  with <a href="https://fal.ai">fal</a>, tests it in the running game, cuts the video, and writes down what it learned for the next agent.
</p>

<p align="center">
  <a href="#install"><img alt="works with Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot and OpenCode" src="docs/media/badges/agents.png" height="26"></a>
  <a href="knowledge/INDEX.md"><img alt="knowledge base: field notes by agents, for agents" src="docs/media/badges/knowledge.png" height="26"></a>
  <a href="https://fal.ai"><img alt="assets: fal" src="docs/media/badges/fal.png" height="26"></a>
  <a href="LICENSE"><img alt="license: MIT" src="docs/media/badges/license.png" height="26"></a>
</p>

<p align="center">
  <img src="docs/media/mods-teaser.gif" alt="Six mods made by AI coding agents, with the universal-modder tile in the corner: Steve gliding an elytra through Los Santos, the Nether spreading over Los Santos, Minecraft mobs fighting the LSPD, the Halo Warthog in Minecraft, a World at War flamethrower in Minecraft, and World at War zombies in Minecraft. It ends on the universal-modder logo and &quot;mod any game.&quot;" width="560">
</p>

<p align="center"><b>Coming next: the mod hub.</b> Publish your mods, remix other people's, and make new ones.</p>

## Install

Pick your agent. Each gets the same skills (Agent Skills format), the fal MCP server, and the `um` CLI.

| Agent | Install |
|---|---|
| **Claude Code** | `/plugin marketplace add rehan-remade/universal-modder`<br>`/plugin install universal-modder@universal-modder` |
| **Codex** | `codex plugin marketplace add rehan-remade/universal-modder`<br>`codex plugin add universal-modder@universal-modder` |
| **Gemini CLI** | `gemini extensions install https://github.com/rehan-remade/universal-modder` |
| **VS Code / Copilot** | Enable `chat.plugins.enabled`, run **Chat: Install Plugin From Source**, and enter this repo's URL |
| **Cursor** | Cursor Marketplace, or clone (Cursor reads `AGENTS.md` and `.cursor/mcp.json`) |
| **OpenCode** | Clone and run `opencode` inside it (`opencode.json` adds the skills and the fal MCP server) |
| **Skills only**<br>(any agent) | `npx skills add https://github.com/rehan-remade/universal-modder` |
| **Anything else** | `git clone https://github.com/rehan-remade/universal-modder` and start your agent inside it |

Inside a clone, each agent finds the skills where it looks for them: `.agents/skills` (Codex, Gemini CLI,
Copilot, Cursor, OpenCode) and `.claude/skills` (Claude Code) are copies of `skills/`. Instructions are in
`AGENTS.md`, which `CLAUDE.md` and `GEMINI.md` point to. MCP config is in `.mcp.json`, `.codex/config.toml`,
`.cursor/mcp.json`, `.vscode/mcp.json` and `opencode.json` (which also points OpenCode at `skills/`).

**The `um` CLI.** Plugin installs and clones put it on PATH. Anywhere else:
```bash
uv tool install git+https://github.com/rehan-remade/universal-modder     # or: pipx install git+...
```
**For assets,** get a [fal API key](https://fal.ai/dashboard/keys). It powers both the fal MCP server and
`um fal` (for images without a key, `um comfy` uses a local ComfyUI server):
```bash
export FAL_KEY=...
```
You also need Git, Python 3.10+ and ffmpeg. `uv` is recommended. Blender is needed for 3D → sprite renders.
Windows games are driven natively or from WSL.

## Try it
> Mod Terraria: add a homing missile launcher and a tactical nuke that craters the world. Make the sprites with fal.

> Make a new civilization for Age of Empires II with a unique unit rendered from 3D.

> Put real Minecraft inside GTA V story mode. Minecraft's camera should follow GTA's, and its TNT should blow up GTA cars.

> Port the Warthog from my Halo install into Minecraft, with a gunner on the turret.

> What engine is `C:\Games\Foo`, and has anyone modded it before?

The agent starts with the **mod-any-game** skill and runs the same loop every time:
1. search the knowledge base;
2. recon, then pick a route;
3. set up a safe lab (saves backed up);
4. read the actual code;
5. build one working slice;
6. generate assets;
7. verify in the real game;
8. record;
9. package;
10. write a field note for the next agent.

## A knowledge base that AIs write for AIs
[`knowledge/`](knowledge/) holds **field notes**: how specific games were actually modded, decompiled and
reverse-engineered. Each note gives:
- the exact versions that worked;
- the route, and why;
- what the engine really does;
- how it was verified;
- the gotchas (symptom → cause → fix).

**Every agent that finishes a mod can o