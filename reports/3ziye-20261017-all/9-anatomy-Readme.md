<h1 align="center">Anatomy</h1>

<p align="center"><b>A Claude skill that explains an idea by building it as a real, working object.</b><br>Also runs in Antigravity, OpenCode, Codex and MiniMax Code.<br>Crafted, interactive isometric figures with many small precise parts, in SVG, WebGL and 3D.</p>

<p align="center">
  <a href="https://code.claude.com/docs/en/skills"><img src="https://img.shields.io/badge/Claude_Code-skill-1b1b19?style=flat-square&logo=claude&logoColor=white" alt="Claude Code skill"></a>
  <a href="https://agentskills.io"><img src="https://img.shields.io/badge/Agent_Skills-compatible-1b1b19?style=flat-square" alt="Agent Skills compatible"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-1b1b19?style=flat-square" alt="MIT license"></a>
  <a href="#requirements"><img src="https://img.shields.io/badge/node-%E2%89%A5%2020.10-1b1b19?style=flat-square&logo=nodedotjs&logoColor=white" alt="Node 20.10 or later"></a>
  <a href="#requirements"><img src="https://img.shields.io/badge/dependencies-0-1b1b19?style=flat-square" alt="No dependencies"></a>
  <a href="https://github.com/wheresryan22/anatomy/actions/workflows/ci.yml"><img src="https://github.com/wheresryan22/anatomy/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
</p>

<p align="center">
  <a href="https://skills.wheresryan.sh/anatomy"><img src="https://img.shields.io/badge/Website-skills.wheresryan.sh%2Fanatomy-1b1b19?style=for-the-badge" alt="Website: skills.wheresryan.sh/anatomy"></a>
  &nbsp;
  <a href="https://github.com/wheresryan22/anatomy/archive/refs/heads/main.zip"><img src="https://img.shields.io/badge/Download-ZIP-1b1b19?style=for-the-badge&logo=github&logoColor=white" alt="Download ZIP"></a>
  &nbsp;
  <a href="#install"><img src="https://img.shields.io/badge/Install-npx_skills_add-d7d7d0?style=for-the-badge&labelColor=1b1b19&logo=npm&logoColor=white" alt="Install with npx"></a>
</p>

<p align="center">
  <a href="#quick-start">Quick start</a> ·
  <a href="#gallery">Gallery</a> ·
  <a href="#what-it-makes">What it makes</a> ·
  <a href="#install">Install</a> ·
  <a href="#usage">Usage</a> ·
  <a href="#examples">Examples</a> ·
  <a href="#how-it-works">How it works</a> ·
  <a href="#limits">Limits</a>
</p>

<p align="center">
  <img src=".github/assets/raptor-engine-firing.webp" width="640" alt="An isometric drawing of a Raptor 2 rocket engine hanging in a test stand, firing: a red exhaust plume, drawn by a WebGL shader, pours onto the stand's base plate. The card reads Fig 1, Raptor 2 test stand, Pc 300 bar, 230 tf.">
</p>

<p align="center"><sub><code>examples/raptor-engine</code>, light theme, firing. The engine and stand are SVG; the plume is a WebGL shader in the same isometric camera.</sub></p>

---

Ask Claude for a figure that explains a technical idea, and Anatomy has it invent a physical thing whose working *is* the concept. A cache key that skips work when nothing changed becomes a pin-tumbler lock that only turns when every pin matches. One GPU context serving many canvases becomes a gantry plotter whose single print head visits 16 wells.

Then Claude builds that thing out of dozens of small, solid, shaded parts, puts it in a framed card with a title, a hint and a live readout, makes it move calmly under the pointer and the keyboard, and checks its own work by zooming in on every joint. Every number the figure shows comes from the same small model that moves its parts.

## Quick start

```sh
npx skills add wheresryan22/anatomy -g
```

The CLI asks which agents to set up (Claude Code, Antigravity, OpenCode, Codex, MiniMax Code). To skip the question, add `-a claude-code`, `-a antigravity`, `-a opencode`, `-a codex`, or `-a minimax-code`.

Then, in Claude Code:

```text
/anatomy explain how a token bucket rate limiter works, interactive
```

For Antigravity, OpenCode, Codex, or MiniMax Code, target that agent: `-a antigravity`, `-a opencode`, `-a codex`, or `-a minimax-code`. Antigravity, OpenCode and MiniMax Code take the same `/anatomy` command; in Codex, type `$anatomy`.

That's it. No API keys and nothing to `npm install`: the kit uses only Node's built-in modules.

## Gallery

<table>
  <tr>
    <td width="50%"><img src=".github/assets/raptor-engine-apart.webp" alt="The Raptor 2 engine taken apart in its test stand: its assemblies, pipes and harness hang apart from each other between the posts of the stand."></td>
    <td width="50%"><img src=".github/assets/ripple-tank.webp" alt="A school ripple tank on four tall legs, with a lamp on an arm above it. Two dippers on a vibrating bar make interfering waves, and their caustics are projected onto the paper screen under the tank."></td>
  </tr>
  <tr>
    <td><sub><b>raptor-engine</b>: hover to take it apart into 11 assemblies. An audit proves that no pipe passes through anything, at rest, apart and in every frame between.</sub></td>
    <td><sub><b>ripple-tank</b>: SVG apparatus over two WebGL layers (lamp light and caustics on the paper, ref