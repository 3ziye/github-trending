# Three.js Game Skills

Self-contained Codex and Claude Code skills for building playable, polished Three.js browser games. Install the skills, then ask your agent to use `threejs-game-director`; the director routes gameplay, graphics, UI, asset generation, audio, debugging, and release verification without requiring users to choose every specialist skill manually.

The package includes the runtime materials agents need: `SKILL.md` files, references, checklists, prompt templates, helper scripts, and a Vite + TypeScript + Three.js scaffold bundled inside the relevant skill folders. Generated games ship with deterministic test hooks, a seeded RNG, and Playwright templates for smoke tests, visual-regression baselines, and bot playtests so agents can verify their own work end to end.

Created by [Majid Manzarpour](https://x.com/majidmanzarpour).

## Demos

| Game | Video | Play |
| --- | --- | --- |
| Neon Ridge Drift | [Watch on X](https://x.com/majidmanzarpour/status/2064565389036540327) | [ridgedrift.netlify.app](https://ridgedrift.netlify.app) |
| Championship Snooker Arena | [Watch on X](https://x.com/majidmanzarpour/status/2064673249129071096) | [snookerarena.netlify.app](https://snookerarena.netlify.app) |
| Starship Dogfight | [Watch on X](https://x.com/majidmanzarpour/status/2065065340510281888) | [starshipdogfight.netlify.app](https://starshipdogfight.netlify.app) |
| Tide Singer | [Watch on X](https://x.com/majidmanzarpour/status/2065570428723007555) | [tidesinger.netlify.app](https://tidesinger.netlify.app) |
| Ripcore | [Watch on X](https://x.com/majidmanzarpour/status/2066687620709544070) | [ripcore.netlify.app](https://ripcore.netlify.app) |

## Install

Install all skills for Codex:

```bash
npx skills add majidmanzarpour/threejs-game-skills --skill '*' -a codex -g -y
```

Install all skills for Claude Code:

```bash
npx skills add majidmanzarpour/threejs-game-skills --skill '*' -a claude-code -g -y
```

If your installed `skills` CLI does not support one of these targets, install from a cloned checkout instead: `./install.sh --codex` for Codex, `./install.sh --claude` for Claude Code, or `./install.sh --all` for both.

For local development from a cloned checkout:

```bash
./install.sh --codex
./install.sh --claude
./install.sh --all
```

The local installer copies `skills/` into the selected agent skills directory. It skips same-named skills unless you pass `--force`, and it never removes unrelated user skills unless `--prune-managed` is explicitly requested.

```bash
./install.sh --codex --force
```

## Use The Skills

After installing, open Codex or Claude Code in an empty project folder, or in an existing Three.js game you want to improve. Then prompt the agent with the outcome you want and name the director skill:

```text
Use threejs-game-director to build a premium futuristic tower defense game from scratch.
Automatically use the relevant gameplay, graphics, UI, asset generation, audio, debug,
and QA skills. Build a playable loop first, then iterate until it passes browser,
mobile, visual, UI, performance, and release checks.
```

Both runners share the same `SKILL.md` files and auto-discover the skills once installed; the prompt above works in either:

- **Claude Code** reads skills from `~/.claude/skills` and routes from each `SKILL.md` description. Invoke the director with `/threejs-game-director`, or just name it in a prompt — it loads the sibling skills itself.
- **Codex** reads skills from `~/.codex/skills`, with each skill's `agents/openai.yaml` supplying its display name and a default kickoff prompt. Name the director in your prompt and it pulls in the specialists the same way.

The agent should:

- Load `threejs-game-director` first for broad game work.
- Load sibling skills for gameplay systems, AAA graphics, UI, debug/profile, QA/release, 3D generation, image generation, and audio generation when the request calls for them.
- Use the bundled scaffold internally when starting from an empty folder.
- Create or update the game code in your project.
- Run builds, browser checks, screenshots, canvas-pixel checks, mobile viewport checks, and QA gates before claiming completion.
- Report the skill-loading ledger, reference ledger, asset/audio sourcing decisions, visual scorecard, and remaining risks for premium work.

Users generally should not need to run the scaffold or QA helper scripts directly. Those scripts are packaged so the skills can use them as part of the workflow.

## Optional API Keys

The core Three.js skills work without paid API keys. When keys are missing, the director should report the credential probe output, skip external generation, and fall back to procedural/local assets. Add keys only when you want the agent to generate external models, images, or audio.

Never commit API keys or put them in browser-side game code. These skills use provider APIs from local agent tooling, then save generated assets into your game project.

| Provider | Skill | Environment vari