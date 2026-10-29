# Animate — procedural animation in any style, for Claude Code

A Claude Code skill that makes short animated videos entirely in code: one `<canvas>`, drawn and scored procedurally, deterministic frame by frame, rendered to MP4 with a headless browser and ffmpeg. Explainers, histories, little stories — in one of the built-in styles, or in a new look matched from your own references.

![the built-in styles](docs/styles.png)

*The built-in styles, each a frame from its demo piece: cut paper, crosshatch ink, riso print, sketchbook, math, pixel, isometric — and the eighth slot: any other look, made from your references.*

## How it works

The skill walks you through a few questions, then makes you approve three cheap things before it spends time animating:

| step | what you see | you decide |
|---|---|---|
| 0. Intake | a handful of questions (subject, formats, voice, the look, hero, your music, your product) and the style gallery | answers, a style, or your references |
| 1. Story check | the format it picked and a numbered beat table, facts web-checked | approve / change beats |
| 2. Look check | 2–4 full-size style frames (for a new look: side-by-side comparisons with your references) | thumbs up per frame |
| 3. Storyboard | every beat as a key frame, with sound and the transition into the next | thumbs up/down by panel number |
| 4. Build | — (animate the approved panels, render, review) | — |
| 5. Delivery | the video plus measured checks: cuts on the beat grid, story arc loudness, hero anchoring, the loudest moment after the silence, narration pace | notes → a revision run |

## Styles

A style is a plug-in: the story grammar, timing, sound, renderer and tools stay the same; the style supplies the drawing kit. A piece picks one in its `piece.json` (`"style": "riso"`).

| style | the look |
|---|---|
| cut paper | torn paper, drop shadows, crayon, patterns, characters with faces |
| crosshatch | sketchy ink that boils on 2s, hatch and pencil shading, warm paper and navy "inside the machine" worlds |
| riso | a three-ink risograph print: halftone screens at their own angles, overprints, misregistration |
| sketchbook | graphite and one accent colour on a sketchbook page, hand lettering |
| math | a manim-style math explainer: black stage, axes and graphs, colour-coded variables, smooth easing |
| pixel | low-resolution eras: drawn at the true resolution, upscaled nearest-neighbour, a bitmap font |
| isometric | precise isometric line art: constant hairlines, white faces hiding what's behind, rounded slabs, one dark accent; light or dark ground |

**Your own look:** give the skill references (a video, stills, a web page) and it follows a procedure — measure the palette, line weight, texture, motion and cut rhythm; draw 1–2 matched frames next to your references (`tools/compare.mjs`); ask for your thumbs up; save it as `styles/<name>/` in your project so every later piece can use it. Reference media stays on your machine.

Each style folder has a `STYLE.md` (its rules, palette, motion habits and a frame checklist), a `kit.js`, a `sample.png` and a small `demo/` piece.

## What's baked in

- **A story grammar** (`grammar/`) — 8 short-form formats (a history is a chronology joined by shape morphs; a mission cuts on the beat; …), the rules every piece follows (one constant, colour means one thing, silence before the payoff and loudest on it, the end is the start changed), and a checklist for what any single frame needs.
- **A kit** (`kit/`) — seeded randomness and a line that boils on 2s; cameras; a renderer with shape-morph transitions (the old world closes in on one object, it morphs into the next world's counterpart, the new world opens out of it) that draws through the style's hooks; a storyboard; a synthesizer and a loudness stage for phone playback.
- **Tools** (`tools/`) — build (assembles one self-contained `index.html` from the piece, the kit and the style), test tiles, stills, storyboard, export (frames → WAV + stems → MP4), review (contact sheets and the measured checks, including text that's cut off or overlapping, and loudness), compare (reference vs frame), a reference measurer, gallery, and a frame-hash check that a kit change left a piece pixel-identical.
- **Craft rules** (`craft.md`) — everything learned building these pieces, from "the sustained pad sets a section's loudness, not the plucks" to "cameras put a world point on a screen point".
- **A voice-over** — it writes the script, gets one take per line from the ElevenLabs connector (or your recording), hears when every word is spoken (locally, with faster-whisper) and times the picture to the words; re-takes re-time the picture automatically.
- **Your own music** — give it a track and it maps the beats (tempo, bars, the big hits, the drops), cuts on the song's beats and puts the payoff on its loudest hit; or it composes a score in code.
- **Your real product** — it screenshots your site (or takes your logo files) and animates the real scr