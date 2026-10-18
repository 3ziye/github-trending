<p align="center">
  <img src="docs/media/banner.png" alt="universal-modder: mod any game. Point any AI coding agent at the PC games you own. Publish your mods, remix other people's, and make new ones." width="100%">
</p>

<p align="center">
  <b>Skills, tools and a shared knowledge base that let any AI coding agent mod almost any PC game you own.</b><br>
  The agent finds the game, works out the engine and the route, reads the real code, builds the mod, makes art, 3D and sound
  with <a href="https://fal.ai">fal</a>, tests it in the running game, cuts the video, and writes down what it learned for the next agent.
</p>

<p align="center">
  <a href="https://discord.com/invite/sEZWaf7vV"><img alt="community: join us on discord" src="docs/media/badges/discord.png" height="26"></a>
  <a href="#install"><img alt="works with Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot and OpenCode" src="docs/media/badges/agents.png" height="26"></a>
  <a href="knowledge/INDEX.md"><img alt="knowledge base: field notes by agents, for agents" src="docs/media/badges/knowledge.png" height="26"></a>
  <a href="https://fal.ai"><img alt="assets: fal" src="docs/media/badges/fal.png" height="26"></a>
  <a href="LICENSE"><img alt="license: MIT" src="docs/media/badges/license.png" height="26"></a>
</p>

<p align="center">
  <img src="docs/media/mods-teaser.gif" alt="Six mods made by AI coding agents, with the universal-modder tile in the corner: Steve gliding an elytra through Los Santos, the Nether spreading over Los Santos, Minecraft mobs fighting the LSPD, the Halo Warthog in Minecraft, a World at War flamethrower in Minecraft, and World at War zombies in Minecraft. It ends on the universal-modder logo and &quot;mod any game.&quot;" width="560">
</p>

<p align="center"><b>Coming next: the mod hub at <a href="https://universalmodder.com">universalmodder.com</a>.</b> Publish your mods, remix other people's, and make new ones.<br>
  Share what you make, get help, and follow along:</p>
<p align="center">
  <a href="https://discord.com/invite/sEZWaf7vV"><picture><source media="(prefers-color-scheme: dark)" srcset="docs/media/discord-dark.svg"><img src="docs/media/discord-light.svg" height="32" alt="join the discord"></picture></a>
</p>

## Install

Pick your agent. Each gets the same skills (Agent Skills format), the fal MCP server, and the `um` CLI.

| Agent | Install |
|---|---|
| **Claude Code** | `/plugin marketplace add rehan-remade/universal-modder`<br>`/plugin install universal-modder@universal-modder` |
| **Codex** | `codex plugin marketplace add rehan-remade/universal-modder`<br>`codex plugin add universal-modder@universal-modder` |
| **Gemini CLI** | `gemini extensions install https://github.com/rehan-remade/universal-modder` |
| **VS Code / Copilot** | Enable `chat.plugins.enabled`, run **Chat: Install Plugin From Source**, and enter this repo's URL |
| **Cursor** | Cursor Marketplace, or clone (Cursor reads `AGENTS.md` and `.cursor/mcp.json`) |
| **OpenCode** | Clone and run `opencode` inside it (`opencode.json` adds the skills and the fal MCP server)<br>or, on OpenCode 2, `opencode plugin add 'github:rehan-remade/universal-modder#main::path:plugins/opencode'` (the `um` tool and fal MCP; add the skills with **Skills only**) |
| **Skills only**<br>(any agent) | `npx skills add https://github.com/rehan-remade/universal-modder` |
| **Anything else** | `git clone https://github.com/rehan-remade/universal-modder` and start your agent inside it |

Inside a clone, each agent finds the skills where it looks for them: `.agents/skills` (Codex, Gemini CLI,
Copilot, Cursor, OpenCode) and `.claude/skills` (Claude Code) are copies of `skills/`. Instructions are in
`AGENTS.md`, which `CLAUDE.md` and `GEMINI.md` point to. MCP config is in `.mcp.json`, `.codex/config.toml`,
`.cursor/mcp.json`, `.vscode/mcp.json` and `opencode.json` (which also points OpenCode at `skills/`).

Without a clone, OpenCode 2 installs the plugin in `plugins/opencode/` with `opencode plugin add`: one
`um_run` tool that passes its arguments straight to the CLI and runs `um` from PATH (see below), plus the
fal MCP server when `FAL_KEY` is set and none is configured. A clone doesn't need it. See
`plugins/opencode/README.md`.

**The `um` CLI.** The Claude Code plugin puts it on PATH (its SessionStart hook), and so does a clone opened in
Claude Code (`.claude/settings.json`); in a clone with another agent, `export PATH="$PWD/bin:$PATH"`. Other
agents' plugin installs (Codex, Cursor, Gemini CLI, OpenCode) don't, so install it once:
```bash
uv tool install git+https://github.com/rehan-remade/universal-modder     # or: pipx install git+...
```
**For assets,** get a [fal API key](https://fal.ai/dashboard/keys). It powers both the fal MCP server and
`um fal`. Rather than exporting it from a shell profile or a `.env`, store it once with `um fal key set`: on
Linux it goes into the desktop keyring (libsecret's `secret-tool`), elsewhere into an owner-only
`~/.secrets/fal-key