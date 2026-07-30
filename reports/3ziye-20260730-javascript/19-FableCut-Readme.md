# FableCut

**A browser video editor that AI agents can drive.**

<a href="https://trendshift.io/repositories/77702?utm_source=trendshift-badge&amp;utm_medium=badge&amp;utm_campaign=badge-trendshift-77702" target="_blank" rel="noopener noreferrer"><img src="https://trendshift.io/api/badge/trendshift/repositories/77702/daily?language=JavaScript" alt="ronak-create%2FFableCut | Trendshift" width="250" height="55"/></a>

[![Hacker News — front page](https://img.shields.io/badge/Hacker%20News-front%20page-ff6600?logo=ycombinator&logoColor=white)](https://news.ycombinator.com/item?id=48845422)
[![DEV — Top 7 of the week](https://img.shields.io/badge/DEV-Top%207%20of%20the%20week-0A0A0A?logo=devdotto&logoColor=white)](https://dev.to/devteam/top-7-featured-dev-posts-of-the-week-815)
[![Official MCP registry](https://img.shields.io/badge/MCP%20registry-io.github.ronak--create%2Ffablecut-7b6cff?logo=modelcontextprotocol&logoColor=white)](https://registry.modelcontextprotocol.io/v0/servers?search=fablecut)
[![Mentioned in Awesome MCP Servers](https://awesome.re/mentioned-badge.svg)](https://github.com/punkpeye/awesome-mcp-servers)
[![Glama score](https://glama.ai/mcp/servers/ronak-create/FableCut/badges/score.svg)](https://glama.ai/mcp/servers/ronak-create/FableCut)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/ronak-create/FableCut)
[![Discord](https://img.shields.io/badge/Discord-join%20the%20community-5865F2?logo=discord&logoColor=white)](https://discord.gg/WBKScy52F)

<https://github.com/user-attachments/assets/2430b854-168b-4a9a-af2e-489e5efa7543>

FableCut is a Premiere-style non-linear video editor that runs entirely in your
browser — and exposes its whole timeline as one JSON document. Edit it by hand,
from the UI, or let an AI agent (Claude Code, Claude Desktop, or anything that
speaks MCP/REST) cut your video for you while you watch the timeline update
live.

Zero npm dependencies. One `node server.js`. That's it.

![FableCut editor](docs/screenshot.png)

## Why it's interesting

Most "AI video" tools hide the edit behind an API. FableCut flips that: the
**project file is the interface**. `project.json` describes media, clips,
tracks, effects, keyframes and transitions — any process that can write JSON
can edit video, and the open browser UI hot-reloads within ~150 ms via
server-sent events. A human and an agent can work on the same timeline at the
same time.

## Features

**Editing**

- 3 video tracks + 4 audio tracks, drag/trim/split/snap, undo/redo
- **Settings** (cog in the top bar) — optional prefs stored in this browser via
  `localStorage`. Enable **Link timeline and Project bin selection** so picking a
  timeline clip highlights its media in Project, and clicking a Project item
  selects every timeline clip that uses it (off by default).
- **Direct manipulation on the monitor** — click a clip or title on the preview to
  move, resize (corner handles), or rotate (top handle, Shift-snap) it directly
- **Timeline multi-select** — rubber-band marquee (drag on empty track area),
  <kbd>Ctrl/Cmd/Shift+click</kbd> to add/remove clips, <kbd>Ctrl+A</kbd> to
  select all, <kbd>Esc</kbd> to deselect. Drag any selected clip to move the
  whole group; <kbd>Delete</kbd> removes all selected; <kbd>S</kbd> splits all
  selected at the playhead. Inspector shows an "N clips selected" banner.
- Beat & cue markers (tap <kbd>⇧m</kbd> on the beat during playback) with edge snapping
- Press <kbd>Alt+t</kbd> to add an in/out transition based on the playhead position over the selected clip. The last used transition is remembered as the default. Drag the overlay triangle to adjust duration; <kbd>Delete</kbd> clears the focused transition.
- Real decoded audio waveforms on clips
- **Project bin folders** — tree view with expand/collapse; drag media or folders to nest; right-click the **Project** tab → New folder; drop files onto a folder to import into it
- **Audio Hold** — timeline toolbar toggle: while paused, loops **one frame** of
  audio at the playhead (useful when stepping frame-by-frame). Scrubbing or
  frame-step retargets the held slice; meters stay live. **Play** / **Pause**
  turns it off.
- Canvas aspect presets (16:9, 9:16 reels, 4:5, 1:1) + safe-area guides
- **Program Monitor zoom** — mouse-wheel over the preview zooms the composition
  toward the cursor (fit → up to **2 screen pixels per canvas pixel**). Magnified
  view uses **native scrollbars** so overflow stays reachable; middle-click or
  <kbd>Alt</kbd>+drag pans. The **Fit** button (shown while zoomed) resets to the
  fit-to-stage baseline
- Preview playback speed — shuttle the monitor through 1×/1.5×/2×/4× with **J**/**K**/**L**
  (from a stop <kbd>J</kbd>/<kbd>L</kbd> start playback; while playing <kbd>L</kbd> steps faster
  and <kbd>J</kbd> slower, <kbd>K</kbd> toggles play/pause and resets to 1×); affects the
  preview player only, never the export
- Resizable workspace: drag the divider between monitor and timeline (double-c