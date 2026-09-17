# scroll-craft

**An agent skill for building premium, scroll-driven websites, with a real design standard.**

Use it with Codex, Claude Code, or another coding agent that can read instructions,
edit files, run commands, and inspect a browser. The skill contains the design
workflow, references, engine, and verification tools. It also ships as a Claude
Code plugin for convenient installation.

Most AI website output fails in one of two directions. It is either well behaved and forgettable, or it is a flashy scroll animation with 2.1:1 body text, a headline that wraps to six lines on a phone, and the same six sections every other AI page has. scroll-craft is built to fail neither way: it treats **interaction** and **craft** as one job rather than two.

[![MIT](https://img.shields.io/badge/licence-MIT-blue.svg)](LICENSE)
[![Agent skill](https://img.shields.io/badge/agent-skill-3b82f6.svg)](plugins/nateherk-design/skills/scroll-craft/SKILL.md)
[![Claude Code plugin](https://img.shields.io/badge/Claude%20Code-plugin-d97757.svg)](https://code.claude.com/docs/en/plugins)

---

## New in 0.3.0: the approved ten-site standard

The skill now includes the process behind ten approved immersive websites:
AI Automation Society, PERKFORM, Glaido, Herkules Advisory, Serein, FORME,
Pelagic, NOEMA, OFFGRID, and Afterhours.

### See the worked examples in motion

A 50-second walkthrough of several approved sites, showing their layered heroes,
pointer response, and scroll transitions.

https://github.com/user-attachments/assets/d193073b-5af9-45de-93ae-95bf7c6934d5

- Plan independent depth planes, contact anchors, and opening/midpoint/exit states.
- Use authentic brand assets and verified product details before generating imagery.
- Choose photographic compositing or real 3D rendering to suit the subject.
- Give each site its own navigation, information order, useful controls, and ending.
- Art-direct phones separately and verify actual scroll frames, fallbacks, and packages.
- Honor explicit creative delegation without forcing a redundant interview.

Read the [worked examples and production workflow](plugins/nateherk-design/skills/scroll-craft/references/approved-collection.md)
and the [hero-depth guide](plugins/nateherk-design/skills/scroll-craft/references/hero-depth.md).
These examples describe design behavior; client assets and private form data are
not bundled. The existing engine and video compatibility fixes are preserved.

## Three builds, three completely different pages

Same skill, same engine, no shared skeleton. The differences below are not themes: they are different page grammars, different navigation models, different endings.

### [AI Automation Society](https://aiautomationsociety.ai) · an AI community
A dark editorial landing for a 450,000-member community. One stat carries the whole promise, a live product surface rises into the frame, and the proof stacks under it as you fall down the page.

![AI Automation Society, a dark editorial community landing](media/ais.webp)

### [Nate Herk](https://www.nateherk.com) · a creator portfolio
High-key and bright, the opposite of the first. A lit-glass hero with the numbers up front, a portrait held in the light, and two clear next steps instead of a wall of links.

![Nate Herk, a high-key lit-glass creator portfolio](media/nateherk.webp)

### PERKFORM · a protein coffee
A filmic one-shot that hard-cuts to two full-bleed inverted grounds mid-page. Loud, product-forward, and the only one of the three that raises its voice.

![PERKFORM, a filmic one-shot product page](media/perkform.webp)

---

## What it actually does

**Interaction, engagement, and being unrepeatable**

- **Scroll is the timeline.** Video scrubs frame by frame under the wheel, sections pin while their argument advances, rails pan sideways, headlines assemble line by line, the page ground shifts colour as you travel, and the pointer moves things that are not scrolling.
- **Eight mutually exclusive page grammars.** Filmic one-shot, chaptered editorial, live surface, continuous world, typographic poster, gallery, split stage, rhythmic cutlist. Each one *forbids* what the others require, so two builds cannot quietly converge.
- **A required signature move.** Every build invents one bespoke interaction that exists on that site alone. A recoloured spotlight does not count.
- **A fingerprint gate.** A new build must differ from every page you have already made on at least 4 of 6 dimensions: grammar, nav, hero, act shape, close, signature move. Fail it and you change the plan, not the record.

**Craft, and how the page actually feels**

- **A feeling curve before any act exists.** One line per act: the emotion, then what on screen causes it. Two adjacent acts with the same feeling means one is filler.
- **One engineered peak.** Peak-end rule, applied literally. The peak gets the asset budget, the silence in front of it, and the most scroll room. A page with three peaks has none.
- **A typography floor.** Two 