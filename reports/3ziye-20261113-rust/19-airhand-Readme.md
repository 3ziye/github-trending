<p align="center"><img src="assets/icon.svg" width="96" alt="Airhand"></p>

<h1 align="center">Airhand</h1>

<p align="center"><b>High-performance, low-latency remote desktop</b><br>QUIC transport · hardware encoding and decoding · up to 120 fps<br>Windows · macOS · Linux · Android · browser</p>

<p align="center"><b>English</b> · <a href="README.zh-CN.md">简体中文</a></p>

---

Airhand is a **high-performance, low-latency** remote desktop: the screen is encoded on the GPU (AV1 / HEVC / H.264) at up to 120 fps and sent over QUIC; when the network slows down it skips to the latest frame instead of letting lag pile up; and the mouse pointer is drawn locally, so it moves without delay.

The same program is both the **host** (the device being controlled) and the **controller** (the device you control it from). The two sides meet through a **relay server** that you deploy yourself. It's small, and Docker Compose deploys it with one command. Enter the other side's 6-digit **control code** to connect.

> [!NOTE]
> **Work in progress (0.2.3).** Since protocol v9, client ⇄ server and host ⇄ controller each support a range of versions, new features are negotiated with capability bits and unknown messages are skipped, so later versions can be mixed; versions before v9 are incompatible, which is detected and reported (see [Protocol versions](docs/development.md#protocol-versions)).

## Performance

Every stage from capture to display is built for low latency:

- **Hardware encoding and decoding**: the host encodes on the GPU (NVENC / Quick Sync / AMF, VideoToolbox, MediaCodec) in low-latency mode without B-frames; the controller decodes on the GPU (WebCodecs / MediaCodec). Measured with a 4K screen streamed at 1080p, hardware AV1 encoding takes about 7 ms per frame (RTX graphics card)
- **The best format**: AV1 > HEVC > H.264, automatically picking the most efficient format both sides support; scaling and color conversion use SIMD, and all buffers are reused
- **No lag build-up**: the host limits the bytes in flight (≈ bitrate × (RTT + 50 ms)) and skips to the latest frame on a slow network; the bitrate follows the measured queueing delay and bandwidth on every acknowledgement, backing off within a few hundred milliseconds and recovering gradually
- **Direct path**: besides the relay, the two ends punch a direct path through their NATs (on the same LAN, or whenever the NAT isn't symmetric), so video and audio stop detouring through the server; the lower-latency path is picked automatically, and if the direct path breaks the session falls back to the relay without dropping
- **QUIC + BBR**: BBR congestion control is steadier than Cubic on lossy networks such as Wi-Fi or long-distance links; control messages, audio and video are queued separately, so mouse input and pings never wait behind a large frame; the relay only forwards bytes and never parses the video
- **Decode and show**: the decoder runs in low-latency mode, and each frame is drawn to a desynchronized canvas as soon as it's decoded, without waiting for vsync
- **Local pointer**: the remote cursor's shape is mirrored locally, and moving it happens locally
- **Low bandwidth**: no frames are sent while the screen is still, so an idle desktop uses almost nothing; sessions that aren't on screen drop to 5 fps

See [How it works → Video](docs/architecture.md#video) for details.

## Features

- **Windows system service**: the lock screen, the sign-in screen and UAC prompts can be seen and controlled, and the computer can be reached after boot, before anyone signs in
- **Fixed control codes**: they survive restarts, upgrades and even server restarts until you change them yourself
- **Console**: browser-style tabs to control several computers at once, plus a multi-screen overview to watch them all. Computers you've connected to are saved and reconnect with one click; if one is offline, it connects as soon as it comes back
- **Web console**: the controller can also run in Docker and be used from a browser, with nothing to install on the computer you control from
- **Android**: control computers and phones from a phone as a trackpad or touchscreen, or share your own screen to get help (you approve each connection by default); watch on a TV with the remote
- **Audio**: the host's system audio plays on the controller (Opus + adaptive jitter buffer), with optional A/V sync for watching videos
- **Handy tools**: two-way clipboard sync, typing the clipboard as keystrokes, system shortcuts (Win, Alt+Tab, Ctrl+Shift+Esc…), multiple monitors, keyboard lock in fullscreen, quality presets
- **Secure by default**: sessions are end-to-end encrypted, so the relay server can't see the screen or keystrokes; the first connection needs the pairing code from the other computer's tray (it never goes through the server), and its identity is recognized afterwards; TLS 1.3 with certificate pinning, brute-force protection for control codes; the host always sees who is connected and can disconnect 