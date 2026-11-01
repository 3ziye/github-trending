# earshot

**Ears for coding agents.**

<!-- launch video -->
[**Watch the 22 s launch film**](https://github.com/Leonxlnx/earshot/releases/tag/v0.1.0) - every sound in it was made
in code by `earshot forge`; no recordings, no music track.

![Frames from the launch film](docs/media/launch_frames.png)

AI coding agents can now write the code that renders a film, a product demo or a game. They still cannot hear what
they made. They cannot tell a premium key press from a cheap one, notice that a hit lands 80 ms after the cut, or
hear that the music swells in the wrong place.

earshot turns sound into evidence an agent can reason about: what a file sounds like in words, how well it fits a
description, the best moment inside a long recording, whether it is a real recording or code-synthesized, a
second-by-second listening transcript of a whole film, an annotated picture of it, and a scorecard against
professional launch films. It runs locally on CPU, as a CLI, a Python API and an MCP server.

With ears, an agent can also **make its own sounds in code** and improve them by listening (`earshot forge`), and
**translate a recording into code** it can vary (`earshot fit`). Both below.

**New in 0.4: the sound of a music-led launch film.** 51 new sounds made in code for the soft, short, mid-register
style those films use: rounded UI pops, wood and plastic knocks, short cut hits and sub hits with a kick, gated
glockenspiel / celesta / marimba notes and chime runs, water drops, camera shutters, reverse cymbals, a thump-whoosh,
short dark risers, bright swishes, burst glitches and mid dings (the bank now holds 252). A new `launch` kit preset
mixes every effect against the music bed instead of at a fixed level, says where each one sits against the cut (taps
lead it, whoosh peaks land after it) and how close a run may go. And `earshot fit` was re-made against professional
sound effects and measured on held-out clips ([below](#earshot-fit-audio-to-code)).

**New in 0.3: sound for code-made films.** A bank of sound effects stored as code that render by id in seconds,
with no models and no network: `earshot sfx` aims a whoosh, hit, click or note at a moment in the picture, and
`earshot kit` renders a whole film's effects with measured sync points ([below](#sound-for-films-bank-sfx-kits)).

```
$ earshot describe enter.ogg
  0.56 s short transient (attack 3 ms, decays in 190 ms). Sounds most like: a single mechanical keyboard key press
  (z +5.4), a soft key release click (z +3.6) ... [clear reading]. peak -0.1 dBFS, brightness 1.5 kHz ...

$ earshot match key.ogg "a deep thocky mechanical keyboard press" --alts "a clicky blue switch keyboard" "a mouse click"
  -> strong (z +3.7; would rank #2 among 322 vocabulary descriptions) ...

$ earshot find keys.ogg "a single mechanical key press" --top 4
  0:03.94-0:04.19 (0.24 s stroke, z +4.1 strong); 0:10.60-0:10.86 ...

$ earshot critique film.mp4
  VERDICT: close - 21 of 23 scored metrics in range ... FIX FIRST: 1. [major] nothing reaches body level until 0:01.01 ...
```

## What it does

| command | what an agent gets |
|---|---|
| `describe FILE` | what it sounds like: calibrated tags (z) with the closest alternative readings, AudioSet labels, measurements |
| `match FILE QUERY [--alts ...]` | how well a description fits: cosine, z among the vocabulary, a verdict (strong / plausible / weak / no match) with held-out evidence |
| `rank QUERY PATHS...` | many candidate files sorted by a description (pick the best download) |
| `find FILE QUERY` | the best moments inside a long recording, as sample trims (start / end seconds) |
| `compare FILE --refs DIR` / `ab A B` | nearest reference recordings and typicality; A/B two sounds or two trims, the differences in words |
| `realness FILE...` | real recording / pro-produced vs code-synthesized, with evidence and per-window scores |
| `timeline FILE [--video V] [--cues C]` | the listening transcript: events (time, level, tag), sections, loudness, beat grid, sync of sound to picture cuts and cue frames |
| `sheet FILE -o out.png` | an annotated PNG (video frames, sections, labelled events, spectrogram, waveform, loudness, sync markers) for agents that read images |
| `critique FILE [--video V]` | a launch-video scorecard against a profile of 7 professional launch films, with timestamped fixes |
| `profile REFS... -o p.json` | build your own reference profile from films you admire |
| `measure FILE` | objective measurements only (no models): LUFS, true peak, LRA, envelope, spectrum, tempo / key |
| `forge RECIPE --refset CAT` | make a sound in code and improve it by listening (see below) |
| `fit FILE -o recipe.py` | translate a recording into a forge recipe module that re-renders it, with knobs and morphs (see below) |
| `sfx render ID -o x.wav` | a sound from the shipped bank of 252, aimed at the picture (`--dur`, `--apex`, `--pitch`) and audited; `sfx list`, `sfx check` (no models) |
| `kit init / render / check` | a film's sound kit: on