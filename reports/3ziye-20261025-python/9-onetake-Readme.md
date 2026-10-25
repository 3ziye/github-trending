<p align="center">
  <img src="assets/logo/onetake-icon.svg" alt="onetake icon" width="120">
</p>

<h1 align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/logo/onetake-wordmark-on-cream.svg">
    <img src="assets/logo/onetake-wordmark.svg" alt="onetake" height="90">
  </picture>
</h1>

> **Motion films that never cut to the next slide.** A Claude Agent Skill that makes product launch films, teasers and feature demos where every beat grows out of the one before — one continuous take, not a stack of scenes.
> **一镜到底的连贯动效。** 做产品发布片、预告片、功能演示：每一个画面都从上一个画面里长出来，是一整条连续的镜头，而不是一张张轮流出场的"PPT"。

[![License: PolyForm Noncommercial](https://img.shields.io/badge/License-PolyForm%20Noncommercial%201.0.0-lightgrey.svg)](LICENSE)
[![Type](https://img.shields.io/badge/Type-Agent%20Skill-333.svg)](SKILL.md)
[![Cases](https://img.shields.io/badge/Cases-11%20films-orange.svg)](cases/)
[![Continuity](https://img.shields.io/badge/Continuity-measured%20per%20boundary-brightgreen.svg)](scripts/verify_promo.py)

**▶ See the films and get onetake Pro → [onetakemotion.com](https://onetakemotion.com)**
**▶ 看成片、获取 onetake Pro → [onetakemotion.com](https://onetakemotion.com)**
**▶ New films every week → [@paojiaofty](https://x.com/paojiaofty) on X**

![onetake launch](assets/hero.gif)

<sub>From onetake's own launch film. A prompt bar opens into the ad it asked for; the next prompt collapses into a line that shoots across the desk and opens into a festival screen. No cut. [Full film with sound →](cases/onetake-launch-30s/onetake-launch.mp4)</sub>

---

[English](#english) | [中文说明](#chinese)

---

<a name="english"></a>
## English

### The problem: motion that falls apart

Most motion videos an AI makes today — and most template tools — come out **loose**. Title card, fade, UI shot, fade,
feature card, fade, logo. Each shot can look fine and the whole still reads like a slideshow, because nothing
connects one beat to the next: scenes *replace* each other.

### What onetake does differently: every beat is carried

onetake treats the boundary between two beats as the thing to design. At every boundary, **something on screen
survives and visibly becomes the next beat**:

- the prompt bar **opens into** the app window; the window **reflows into** the phone;
- a bar **collapses into a line**, the line **shoots across** the desk and **becomes the first grid line** of the next film;
- a card **grows into** the page; a stage **opens from** the character; the camera **pushes through** a card until it *is* the next scene;
- at the end, the cast **folds into** the lockup — in the launch film, the block cursor **writes the name** in one stroke.

And **one camera holds it all together**. It never cuts: it follows the subject a beat ahead, whips to where the next
thing will land, floats like a hand-held operator and shakes when something hits — then holds dead still, because rests
are what make the moves land.

### Continuity is measured, not hoped for

Every film is checked by an oracle before a human watches it. `probe.py` records what is on screen in every frame, finds
each boundary, and asks what carried across it. A film whose beats replace each other fails.

| film | verdict | continuity (carry score) |
|---|---|---|
| an earlier launch film, v1 — perfect rhythm, still a slideshow | rejected | **0.00** |
| the same film, v2 | rejected | **0.40** |
| the same film, v3 — every beat grows out of the last | accepted | **0.75** |
| onetake launch film | accepted | **0.83** |

The same oracle fails uniform cadence (shots all the same length), no stillness, clipped audio, fast moves without
motion blur, and a subject that leaves the frame.

### What makes it look finished

- **Real UI, rebuilt.** The product's interface is rebuilt in HTML from screenshots and sits on the camera's plane, so the camera can fly into it at any zoom. No screen recording.
- **Measured moves.** ~38 moves (springs, entrances, carries, contact, sims, camera, fluid grounds), each a pure function of time with its speed curve measured — never a hand-rolled ease.
- **Real motion blur.** Every moving frame is several captures across an open 180° shutter, averaged in linear light. Fast moves smear instead of strobing.
- **Sound in one room.** Foley and synthesis placed from the film's own events, in one reverb, ducking the music under the hits.
- **Deterministic.** Seek to any time, get the same frame. Drafts at 1080p30, finals at 4K60.

### 🌟 Films made with it

Every case ships the finished film and a breakdown (concept, beat sheet, numbers, what was rejected and why). The
films' source code is not included.

<table>
  <tr><th colspan="3" align="left">Concept ad</th></tr>
  <tr>
    <td width="33%" align="center"><b>domino</b><br/><img src="assets/cases/domino.gif" width="100%"/><br/>
      <sub>One phone is one pixel: 12,346 phones fall and a picture resolves, 1 → 100×100, one take in 3D</sub><br/>
      <a href="cases/domino-25s/domino.mp4">▶ 