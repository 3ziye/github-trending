<h1 align="center">reanimate</h1>

<p align="center"><b>Reverse-engineer animations you like. Build your own on top.</b><br>A Claude Code skill that works from a live site, a screen recording, an mp4, a gif or a Lottie file.</p>

<p align="center">
  <a href="https://code.claude.com/docs/en/skills"><img src="https://img.shields.io/badge/Claude_Code-skill-171717?style=flat-square&logo=claude&logoColor=white" alt="Claude Code skill"></a>
  <a href="https://agentskills.io"><img src="https://img.shields.io/badge/Agent_Skills-compatible-171717?style=flat-square" alt="Agent Skills compatible"></a>
  <a href="#install"><img src="https://img.shields.io/badge/runs_on-Bun-171717?style=flat-square&logo=bun&logoColor=white" alt="Runs on Bun"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-171717?style=flat-square" alt="MIT license"></a>
</p>

<p align="center">
  <a href="https://reanimate.niazmorshed.dev/demo.mp4"><img src=".github/assets/demo.webp" width="760" alt="Moments from the demo video: /reanimate slides in; three browsers record widgets on stripe.com, resend.com and clerk.com; the copies are measured against them until the difference is gone; the 18 examples turn on a helix; the install command types itself in."></a>
</p>
<p align="center"><sub>A short demo. <a href="https://reanimate.niazmorshed.dev/demo.mp4">Watch the full video</a>.</sub></p>

A lot of good ideas start on someone else's site. Ask an agent to rebuild one from a link or a screenshot and it makes one pass, calls it done, and misses. It can't see the motion or tell how far off it is.

reanimate records the original, rebuilds it in your code, then records the copy the same way and compares the two. Each round shows what's still off, so the agent keeps going until the numbers match. You end up with a close starting point to make your own.

<p align="center">
  <img src=".github/assets/entrance.webp" width="760" alt="Two recordings of the same three cards fading in: stripe.com on top, the copy reanimate built below. The chat bubbles, the particle ring, the Visa card and the dotted globe appear at the same moments in both.">
</p>
<p align="center"><sub>Three cards from stripe.com. Top: the original. Bottom: the copy, filmed the same way.</sub></p>

## Install

```sh
npx skills add NiazMorshed2007/reanimate -g
```

The [skills CLI](https://skills.sh) asks which agents to set up; add `-a claude-code` to skip the question. Then, in Claude Code, say what you want, where it is and where it should go:

```text
/reanimate the hero entrance on https://example.com, into components/Hero.tsx
/reanimate this loader, 0:03 to 0:05 of ~/Downloads/loader.mov
/reanimate the card hover in this gif, match it exactly
/reanimate the logo marquee from https://example.com, with our logos and pause on hover
```

Needs [Bun](https://bun.sh) 1.1 or later, on macOS or Linux (Windows is untested). The first run installs a static ffmpeg into the skill's folder and Playwright's Chromium into Playwright's usual cache, about 250 MB together. No API keys. Other agents that read `SKILL.md` can install it too, but it has only been tested with Claude Code.

## How it works

1. **Record.** It films the reference in a headless browser at a fixed viewport and frame rate: a video, numbered frames, every CSS and Web Animations API animation it finds, and the position of chosen elements on every frame. For canvas and WebGL it also traces the GPU calls (shaders, uniforms, draw calls, the three.js scene) on a virtual clock that makes every capture identical.
2. **Spec.** One row per element per property: start, duration, from → to, easing, stagger. A row with a "?" means the frames haven't been read yet.
3. **Build.** It writes the animation with what your project already uses: CSS, Framer Motion, GSAP, three.js.
4. **Verify.** It films the copy the same way, compares timing, easing and pixels, and makes side-by-side sheets.
5. **Repeat.** It fixes the biggest difference and films again, usually 2 to 5 rounds. Whatever still doesn't match after 5 is listed in its report, with the reason.

<p align="center">
  <img src=".github/assets/hover.webp" width="520" alt="The card issuing card hovered on stripe.com and in the copy, side by side: the same pointer path makes the Visa card tilt the same way in both.">
</p>
<p align="center"><sub>The same pointer path on stripe.com and on the copy. The tilt settles within 0.4 px.</sub></p>

By default it matches the motion and leaves the look to you. Ask for more or less:

| Say | Level | Must match |
|---|---|---|
| "clone this animation" | Moves the same (default) | trigger, order, stagger, timing within 80 ms, easing family, distance |
| "match it exactly", "pixel-perfect" | Looks the same | all of the above, plus fonts, sizes, colours, spacing and assets; ≤ 2 % mean pixel mismatch |
| "clone X and add Y" | Yours on top | the cloned parts at one of the levels above; your additions kept separate |

## Examples

Six animation