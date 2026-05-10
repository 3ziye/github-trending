# Agent Sprite Forge

Languages: [English](./README.md) | [繁體中文](./README.zh-TW.md) | [简体中文](./README.zh-CN.md) | [日本語](./README.ja.md) | [한국어](./README.ko.md)

<p align="center">
  <img src="./src/banner.png" alt="Agent Sprite Forge banner" width="900" />
</p>

<p align="center">
  <strong>Codex skills for game-ready 2D sprites, layered maps, and engine-ready prototypes.</strong>
</p>

<p align="center">
  Ask in natural language. Codex plans the asset pipeline, renders with built-in image generation, then local processors clean, split, validate, and export assets for Godot, Unity, or raw 2D game workflows.
</p>

<p align="center">
  <a href="#showcase">Showcase</a> ·
  <a href="#included-skills">Skills</a> ·
  <a href="#install">Install</a> ·
  <a href="#suggested-prompts">Prompts</a> ·
  <a href="#star-history">Star History</a>
</p>

## What Makes It Different

Agent Sprite Forge is not just a folder of prompts. It is a Codex-first 2D game asset workflow where the agent decides the plan, image generation creates the raw visuals, and deterministic scripts turn those visuals into reusable game assets.

<table>
  <tr>
    <td width="25%">
      <strong>Sprite sheets</strong><br />
      Characters, monsters, props, attacks, spells, projectiles, impacts, idles, walks, and reference-guided variants.
    </td>
    <td width="25%">
      <strong>Layered maps</strong><br />
      Ground-only bases, dressed references, prop packs, transparent props, y-sort placement, collision, zones, and previews.
    </td>
    <td width="25%">
      <strong>Engine handoff</strong><br />
      Godot scenes, editable TileMap layers, separated props, encounter grass, collision bodies, exits, and debug players.
    </td>
    <td width="25%">
      <strong>Local cleanup</strong><br />
      Chroma-key removal, frame extraction, alignment, transparent PNG/GIF export, prop-pack slicing, and QA metadata.
    </td>
  </tr>
</table>

## Showcase

### Engine-Ready Prototypes

These examples were assembled with Codex using `agent-sprite-forge` workflows. They are meant to show the full loop: generated assets, structured scene data, and playable prototype wiring.

<table>
  <tr>
    <td align="center" width="50%">
      <img src="./src/summon-survivors-game-preview1.png" alt="Summon Survivors Unity WebGL gameplay" width="420" />
      <br />
      <strong>Summon Survivors — Unity WebGL</strong>
      <br />
      Generated map art, hero sheets, summons, evolutions, enemies, bosses, pickups, HUD, FX, level-up choices, and WebGL deployment.
      <br />
      <a href="https://summon-survivors.vercel.app/">Play build</a> · <a href="https://drive.google.com/file/d/1TL7qRX95przTToZILVQ1EFwEXm3flB6t/view?usp=sharing">Build conversation</a>
    </td>
    <td align="center" width="50%">
      <img src="./src/kingdomrush-forest-pass.png" alt="Forest Pass Defense Godot tower-defense map" width="420" />
      <br />
      <strong>Forest Pass Defense — Godot Tower Defense</strong>
      <br />
      A Godot 4 prototype with map, separated props, tower slots, towers, enemy sheets, boss/flying enemies, waves, HUD, build/upgrade/sell flow, projectiles, and targeting rules.
    </td>
  </tr>
  <tr>
    <td align="center" width="50%">
      <img src="./src/godot-editor.png" alt="Generate2DMap Godot editor scene" width="420" />
      <br />
      <strong>Editable RPG Map — Godot TileMap</strong>
      <br />
      Image-generated tileset and prop sheet wired into editable <code>TileMapLayer</code>, <code>Sprite2D</code> props, encounter grass <code>Area2D</code>, <code>StaticBody2D</code> collision, exits, metadata, and debug player/camera.
    </td>
    <td align="center" width="50%">
      <img src="./src/neon-breach.png" alt="Neon Breach cyberpunk side-scroller" width="420" />
      <br />
      <strong>Neon Breach — Cyberpunk Side-Scroller</strong>
      <br />
      A playable side-scroller prototype built around generated character, attack, map, and gameplay assets.
    </td>
  </tr>
  <tr>
    <td align="center" width="50%">
      <img src="./src/pokemonlike2.png" alt="Sengoku Era JavaScript RPG starter selection" width="420" />
      <br />
      <strong>Sengoku Era — JavaScript Pokémon-like</strong>
      <br />
      A browser-based RPG prototype with generated characters, starter selection, map flow, and battle UI.
      <br />
      <a href="https://sengoku-era.vercel.app/">Play build</a>
    </td>
    <td align="center" width="50%">
      <img src="./src/pokemonlike.png" alt="Sengoku Era JavaScript RPG battle scene" width="420" />
      <br />
      <strong>Starter selection and battle loop</strong>
      <br />
      A compact JavaScript game showcase built from sprite, monster, battle, and map assets generated through the skill workflow.
    </td>
  </tr>
</table>

<details>
<summary>More Godot tower-defense output</summary>

<table>
  <tr>
    <td align="center" width="40%">
      <img src="./src/kingdomrush-enemy-roster.png" alt="Forest Pass