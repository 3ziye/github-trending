# riddle — the diary of Tom Riddle, for the reMarkable Paper Pro

Write on the page with your pen. After a pause, the diary **drinks your ink** —
your words fade into the paper — the page thinks for a moment, and an answer
writes itself back in a flowing hand, stroke by stroke, then fades away.

No screen glow, no keyboard, no chat UI. Just ink appearing on paper.

_This is the diary from [the demo](https://x.com/MaximeRivest)._

### 🪄 New to this? Start here

You need a **reMarkable Paper Pro** in developer mode with a launcher installed.
If that sounds like a lot, it isn't — **[remagic](https://github.com/maximerivest/remagic)**
walks you through turning on developer mode and sets up everything with one
command. Come back here, drop riddle in, and start writing to Tom.

Already have xovi + AppLoad? Install from the [remagic](https://github.com/maximerivest/remagic)
catalog, [grab the prebuilt bundle](#install-the-prebuilt-bundle), or
[build from source](#building).

### Install with remagic (easiest)

```sh
remagic install riddle     # checksum-verified download → AppLoad
remagic config riddle      # settings form in your browser (+ QR for phone)
```

Then in **AppLoad**: tap **Reload**, then **The Diary**. Write, and rest your
pen. (Or install it from the **Store** app right on the tablet.)

### Install the prebuilt bundle

1. Grab `riddle-<version>.zip` from the [latest release](https://github.com/MaximeRivest/riddle/releases/latest)
   and unzip it into a folder: `unzip riddle-*.zip -d riddle`
2. Copy the folder to your tablet:
   `scp -O -r riddle root@10.11.99.1:/home/root/xovi/exthome/appload/`
3. Add an API key: `cp oracle.env.example oracle.env` in that folder and put your `RIDDLE_OPENAI_KEY` in it (any OpenAI-compatible key). Or skip it to use [pi](#option-b--pi-the-power-path).
4. In **AppLoad**: tap **Reload**, then **The Diary**. Write, and rest your pen.

> ⚠️ **This modifies your device.** The prebuilt bundle and the catalog build
> run in **takeover mode**: tapping The Diary stops the whole reMarkable UI
> and takes the screen. Leave with a **5-finger tap** — xochitl restarts
> automatically. It runs as root and drives the e-ink engine directly. It has
> only been tested on a **reMarkable Paper Pro** (ferrari, aarch64,
> OS 3.26–3.27). It may not work on other models or OS versions, and you use
> it entirely at your own risk. Not affiliated with reMarkable AS. Keep SSH
> access working before you install anything — if anything ever wedges:
> `ssh root@10.11.99.1 'systemctl start xochitl'`.

## How it works

```
 pen (raw evdev, full 4096-level pressure, hardware event rate)
   │ strokes
   ▼
 riddle ── idle 2.8s → commit page → PNG ──► oracle (resident LLM process,
   │                                          streams reply sentence-by-sentence)
   ▼ strokes (Dancing Script → skeletonized to single-pixel pen paths)
 display backend
   ├── qtfb        — windowed, inside xochitl (build-from-source flavour)
   └── quill       — full takeover: xochitl stopped, vendor e-ink engine
                     driven directly for instant ink (lowest latency there
                     is; what the prebuilt bundle runs)
```

- **`riddle/`** — the app (Rust). Pen input, ink surface, handwriting
  synthesis (rasterize → Zhang-Suen thinning → stroke tracing → animated
  replay), the oracle process manager, and both display backends.
- **`quill/`** — the takeover display host (C/C++). An
  [epfb-re](https://github.com/asivery/epfb-re)-style QImage-constructor
  interposition shim over the vendor `libqsgepaper.so` waveform engine,
  exposed as a small C ABI (`quill_init` / `quill_buffer` / `quill_swap`)
  that riddle links against with `--features takeover`. Also carries a small
  family of demos (`scribble`, a pen-to-glass latency test, plus map, image,
  and GIF renderers).

## Gestures

| Do this | And |
|---------|-----|
| Write, then rest the pen | The diary drinks your ink and Tom replies |
| Write *"show me what I wrote about…"* | The remembered page **rises through the paper**: the date, your own handwriting rewriting itself stroke by stroke, Tom's old reply — all in faded ink. Touch the pen anywhere and today's page returns |
| Write *"what do you remember?"* | Tom answers with a handwritten list of remembered moments |
| Flip the marker | Erase |
| Draw a large **?** | Summon the built-in guide |
| Tap five fingers at once | Leave the diary *(takeover mode)* |
| Power button | The page turns to *"The diary sleeps."*, then the tablet suspends; press again to wake exactly where you were *(takeover mode)* |

In the windowed (qtfb) flavour, xochitl keeps the touchscreen and the power
button: close the diary from AppLoad instead.

## The diary remembers

Every finished page is kept — your actual pen strokes, a transcription, and
Tom's reply — so the diary can do three things:

- **Follow the conversation.** Recent pages ride along with each request, so
  Tom remembers what you wrote yesterday (both backend