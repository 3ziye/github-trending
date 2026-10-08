<div align="center">

<img src="docs/assets/logo.svg" width="76" alt="ReelMimic">

# ReelMimic

**Show it a video you love. Get a new video in the same style.**

[![License: MIT](https://img.shields.io/badge/license-MIT-7A6BFF)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude_Code-supported-E86BD2)](https://docs.anthropic.com/en/docs/claude-code)
[![Codex CLI](https://img.shields.io/badge/Codex_CLI-supported-FF9D5C)](https://github.com/openai/codex)
![Node 22.18+](https://img.shields.io/badge/node-22.18%2B-5B57F0)
![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-5B57F0)

**English** · [繁體中文](README.zh-TW.md) · [简体中文](README.zh-CN.md)

<table>
  <tr>
    <td align="center" width="33%"><img src="docs/assets/demo-sugar.gif" alt="Sugar Rush"></td>
    <td align="center" width="33%"><img src="docs/assets/demo-sunshine-boy.gif" alt="Sunshine Boy"></td>
    <td align="center" width="33%"><img src="docs/assets/demo-cat-bath.gif" alt="Bath Time"></td>
  </tr>
  <tr>
    <td align="center"><b>Sugar Rush</b><br><sub>music video · hand-painted · 58 s</sub></td>
    <td align="center"><b>Sunshine Boy</b><br><sub>music video · hand-painted · 63 s</sub></td>
    <td align="center"><b>Bath Time</b><br><sub>narrated comic · 30 s</sub></td>
  </tr>
</table>

<sub>Each one made with ReelMimic from a reference video and a one-line brief. Previews are silent, with the lyrics cropped out.</sub>

</div>

## What is this?

Ever watched a video and thought "I want one in that style, but completely my own"?

Just drop it into ReelMimic. A file, a phone recording or a YouTube link all work. Then tell it what you want to make.

First it takes the reference apart: editing rhythm, shot lengths, transitions, framing, colors and camera moves. Then
it puts together a plan for you to check. You can chat right next to it, change settings or add assets, and start
when you're happy.

Once production starts, the work is split across several AI agents. Different parts of the video are made at the same
time, and every shot is handed to a different agent to check. If something's wrong it goes back to be fixed, so it's
not a one-shot generate-and-done.

ReelMimic learns how the reference was made. It doesn't carry over the original footage, characters or assets.

The whole thing runs on your own computer, with your own Claude Code or Codex.

<p align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/home-en-dark.png">
  <img src="docs/assets/home-en-light.png" alt="ReelMimic home page" width="860">
</picture>
</p>

<p align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/flow-en-dark.png">
  <img src="docs/assets/flow-en-light.png" alt="How ReelMimic works" width="860">
</picture>
</p>

## What it does

- **Breaks down the reference.** Shot count, shot lengths, BPM, transitions, colors, framing and camera moves.
- **Shows you the plan first.** Storyboard, characters, assets and a few style frames. Chat about it until you like it, then approve.
- **Several AI agents share the work.** Up to 6 work on different parts of the video. Each finished shot goes to a new agent for review, so nobody grades their own work.
- **Fixes need proof.** Every fix comes with before and after screenshots, and the reviewer checks them.
- **You can see what it's doing.** What each agent is thinking, what it ran, which frames it looked at. The full log is there too.
- **Comment right on the video.** When it's done, scrub to any second and type a note. Send them all at once.
- **New styles are just Markdown.** One file per style, no code.
- **Three languages.** 繁體中文, English and 简体中文, switch in the top right.

## Good to know

- **2D only, seven drawing engines:** vector / motion graphics (built on
  [HyperFrames](https://github.com/heygen-com/hyperframes)), hand-painted watercolor (built on
  [painted-animation](https://github.com/tuzhechen2005/painted-animation)), crayon picture book, pixel art, paper
  cut-out stop-motion, whiteboard doodle, and anime cel. The newer five are young and have had less real-world use than
  the first two. When a reference doesn't match a known style, it uses the closest engine and writes up a proposal
  for a new style.
- **It takes a while.** A 30–60 second video usually takes 1–3.5 hours after you approve the plan, depending on the
  length and the look. Watercolor and crayon are the slowest, because every frame is painted with brushes.
- **It uses your AI plan.** All the work runs through your Claude Code or Codex account, so it counts toward that
  account's usage. If you hit a limit, the job pauses and can pick up where it stopped.
- **Tested mostly on Windows.** macOS and Linux should work, but they've had less testing. Issues are welcome.
- **No real people.** It makes animation, not live-action footage of real people.

## Roadmap

- More built-in characters and styles for each engine
- Save a newly discovered style from the web app, so