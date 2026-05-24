# /watch

**Give Claude the ability to watch any video.**

Claude Code:
```
/plugin marketplace add bradautomates/claude-video
/plugin install watch@claude-video
```

claude.ai (web): [download `watch.skill`](https://github.com/bradautomates/claude-video/releases/latest) and drop it into Settings → Capabilities → Skills.

Codex / generic skills:
```bash
git clone https://github.com/bradautomates/claude-video.git ~/.codex/skills/watch
```

Zero config to start — `yt-dlp` and `ffmpeg` install on first run via `brew` on macOS (Linux/Windows print exact commands). Captions cover most public videos for free. Whisper API key is only needed when a video has no captions.

---

Claude can read a webpage, run a script, browse a repo. What it can't do, out of the box, is *watch a video*. You paste a YouTube link and it has to either guess from the title or pull a transcript that's missing 90% of what's on screen.

With Claude Video `/watch` you can paste a URL or a local path, ask a question, and Claude downloads the video, extracts frames at an auto-scaled rate, pulls a timestamped transcript (free captions when available, Whisper API as fallback), and `Read`s every frame as an image. By the time it answers, it has *seen* the video and *heard* the audio.

```
/watch https://youtu.be/dQw4w9WgXcQ what happens at the 30 second mark?
```

## Why this exists

I built this because I'm constantly using video to keep up with content. If I see a YouTube video that's blowing up, I want to know how the creator structured the hook — what's on screen in the first 3 seconds, what they said, why it worked. That used to mean watching it myself with a notepad. Now I just paste the URL and ask.

The other half is summarization. Most YouTube videos don't deserve 20 minutes of my attention. I hand the URL to Claude, it pulls the transcript, and tells me what actually happened. If the visual matters, frames come along too. If it's a podcast or a talking head, transcript is enough.

Claude is great at reading and synthesizing — but until now, video was the one input I couldn't hand it. Pasting a YouTube link got you nothing useful. `/watch` closes that gap.

## What people actually use it for

**Analyze someone else's content.** `/watch https://youtu.be/<viral-video> what hook did they open with?` Claude looks at the first frames, reads the opening transcript, breaks down the structure. Same for ad creative, competitor launches, podcast intros, anything where the *how* matters as much as the *what*.

**Diagnose a bug from a video.** Someone sends you a screen recording of something broken. `/watch bug-repro.mov what's going wrong?` Claude watches the recording, finds the frame where the issue appears, describes what's on screen, often catches the cause without you ever opening the file.

**Summarize a video.** `/watch https://youtu.be/<long-thing> summarize this` does the obvious thing — pulls the structure, the key moments, what was actually said and shown. Faster than watching at 2x.

## How it works

1. **You paste a video and a question.** URL (anything yt-dlp supports — YouTube, Loom, TikTok, X, Instagram, plus a few hundred more) or a local path (`.mp4`, `.mov`, `.mkv`, `.webm`).
2. **`yt-dlp` downloads it.** For URLs, into a temp working directory. For local files, no download — just probed in place.
3. **`ffmpeg` extracts frames at an auto-scaled rate.** The frame budget is duration-aware: ≤30s gets ~30 frames, 30-60s gets ~40, 1-3min gets ~60, 3-10min gets ~80, longer gets 100 sparsely. Hard ceilings: 2 fps, 100 frames. JPEGs at 512px wide by default — bump with `--resolution 1024` if Claude needs to read on-screen text.
4. **The transcript comes from one of two places.** First try: `yt-dlp` pulls native captions (manual or auto-generated) from the source. Free, instant, accurate-ish. Fallback: extract a mono 16 kHz audio clip and ship it to Whisper — Groq's `whisper-large-v3` (preferred — cheaper and faster) or OpenAI's `whisper-1`.
5. **Frames + transcript are handed to Claude.** The script prints frame paths with `t=MM:SS` markers and the transcript with timestamps. Claude `Read`s each frame in parallel — JPEGs render directly as images in its context.
6. **Claude answers grounded in what's actually on screen and in the audio.** Not "based on the description" or "according to the title." It saw the frames. It heard the transcript. It answers the way someone who watched the video would.
7. **Cleanup.** The script prints a working directory at the end. If you're not asking follow-ups, Claude removes it.

## Frame budget — why it matters

Token cost is dominated by frames. Every frame is an image; image tokens add up fast. The script's auto-fps logic exists so you don't blow your context budget on a sparse scan of a 30-minute video that would have been better answered by a focused 30-second window.

| Duration | Default frame budget | What you get |
|----------|---------------------|--------------|
| ≤30 s | ~30 frames | Dense — 