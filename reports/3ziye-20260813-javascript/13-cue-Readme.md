<div align="center">

# cue

**An open-source AI copilot that floats over your screen — sees what you see, hears your meetings, and stays hidden from screen shares.**

A free, self-hosted alternative to Cluely. Bring your own AI key (OpenAI · Anthropic · Google Gemini · OpenAI-compatible endpoints).

<img src="docs/tutorial.png" width="620" alt="cue first-run tutorial" />

</div>

---

> [!IMPORTANT]
> **Please read this first.** cue tries to stay out of screen recordings/shares, but this is **best-effort, not guaranteed** — on macOS 15.4+ Apple can let modern capture tools see it anyway, on Windows 10 builds older than 2004 it degrades to a black box instead of true exclusion, and a phone camera always can. Using a hidden assistant during a **proctored exam, job interview, or recorded meeting** may break that platform's rules and, in some places, consent laws. cue is built for legitimate uses — your own notes, studying, accessibility, and practice. **You are responsible for how you use it.**

---

## What it does

cue floats a small glass panel on top of everything. It takes **three separate inputs** — your **screen**, your **microphone**, and your **meeting audio** (what the other person says) — and uses an AI model to help you in real time.

| Feature | How to trigger | What it uses |
|---|---|---|
| **Assist** | `⌘` `↵` (macOS) or `Ctrl` `Enter` (Windows), configurable | your screen + recent conversation |
| **What should I say?** | button | meeting audio + your mic |
| **Follow-up questions** | button | the whole conversation |
| **Recap** | button | the whole conversation |
| **Ask anything** | type + `↵` | your screen + conversation |
| **Solve a coding problem** | `⌘` `H` (macOS) or `Ctrl` `H` (Windows) | your screen only |
| **Smart** toggle | pill in the box | switches to a smarter (slower) model |

It's a copilot for **live meetings** ("what do I say to that?") and **coding problems** (screenshot → full solution), and it's designed to be **invisible in screen shares** so it stays your private assistant.

### Platform support

|  | macOS | Windows 11 / 10 2004+ |
|---|---|---|
| Screen + coding help | ✅ | ✅ |
| Your mic (the **You** channel) | ✅ | ✅ |
| Meeting audio (the **Them** channel) | ✅ macOS 14.4+ | ✅ |
| Hidden from screen shares | ⚠️ best-effort, weaker on macOS 15.4+ | ✅ `WDA_EXCLUDEFROMCAPTURE` |
| Permissions to grant | Microphone **and** Screen Recording | Microphone only |

> [!NOTE]
> **Meeting audio needs macOS 14.4+.** Capturing the *other* person — what powers **What should I say?**, **Follow-up questions**, and **Recap** — uses system-audio loopback. On Windows that works out of the box. On macOS it relies on ScreenCaptureKit, which cue enables through Chromium's `MacLoopbackAudioForScreenShare` and `MacSckSystemAudioLoopbackOverride` switches; on older macOS the *Them* channel stays silent while your screen and the **You** channel keep working.

---

## Install

Option A is the easiest on both platforms. Use Option B if you'd rather run from source.

### Option A — Download the app (easiest)

Go to the [**Releases**](../../releases) page, then choose your platform:

- **Windows 10/11 (x64):** download **`cue-win-x64.exe`**, run it, and launch cue from the Start menu. The installer is unsigned, so Windows SmartScreen may show an **Unknown publisher** warning.
- **macOS (Apple silicon):** download **`cue-…-arm64-mac.zip`**, unzip it, drag **`cue.app`** into **Applications**, and open it.

### Option B — Run from source (macOS or Windows)

You need [Node.js](https://nodejs.org) 22.12+ installed (required by dev dependencies). No Xcode and no Visual Studio build tools required — cue deliberately avoids native modules.

```bash
git clone https://github.com/Blueturboguy07/cue.git
cd cue
npm install
npm start
```

That's the whole setup on Windows. There's no permission dance — grant the mic when Windows asks and you're done.

To build a standalone app:
```bash
npm run pack        # unpacked app in dist/ (either OS)
npm run pack:win    # unpacked Windows app -> dist/win-unpacked/cue.exe
npm run dist:mac    # macOS zip            -> dist/
npm run dist:win    # Windows installer    -> dist/cue-win-x64.exe
```
> **macOS note:** the packaged app is **ad-hoc signed** unless a Developer ID certificate is configured. macOS ties permission grants to the exact build, so **rebuilding resets the mic/screen permissions** — you'll grant them again. For everyday use, build once and keep it. Windows has no equivalent problem.
To build a packaged app:
```bash
npm run dist:mac    # macOS build
npm run dist:win    # Windows build
npm run dist:linux  # Linux x64 AppImage
```

Packaged builds include a pinned `whisper.cpp` runtime. When running from source, prepare the matching runtime once:

```bash
npm run prepare:whisper
```

Windows x64 and Linux x64/arm64 use checksum-verified binaries from the pinned upstream release. macOS x64/arm64 builds `whisper-server` from the same pinned source tag and requ