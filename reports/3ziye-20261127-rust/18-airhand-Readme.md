<p align="center"><img src="assets/icon.svg" width="96" alt="Airhand"></p>

<h1 align="center">Airhand</h1>

<p align="center"><b>High-performance, low-latency remote desktop</b><br>QUIC transport · hardware encoding and decoding · up to 120 fps<br>Windows · macOS · Linux · Android · iOS · browser</p>

<p align="center"><b>English</b> · <a href="README.zh-CN.md">简体中文</a></p>

---

Airhand is a **high-performance, low-latency** remote desktop: the screen is encoded on the GPU (AV1 / HEVC / H.264) at up to 120 fps and sent over QUIC; when the network slows down it skips to the latest frame instead of letting lag pile up; and the mouse pointer is drawn locally, so it moves without delay.

The same program is both the **host** (the device being controlled) and the **controller** (the device you control it from). The two sides meet through a **relay server** that you deploy yourself. It's small, and Docker Compose deploys it with one command. Enter the other side's 6-digit **control code** to connect.

> [!NOTE]
> **Work in progress (0.4.0).** Build the relay, clients and web service from the same v10 revision; earlier builds cannot be mixed. Video uses one QUIC stream per frame. [Protocol versions](docs/development.md#protocol-versions)

## Performance

Every stage from capture to display is built for low latency:

- **Hardware encoding and decoding**: the host encodes on the GPU (NVENC / Quick Sync / AMF, VideoToolbox, MediaCodec) in low-latency mode without B-frames; the controller decodes on the GPU (WebCodecs / MediaCodec). Measured with a 4K screen streamed at 1080p, hardware AV1 encoding takes about 7 ms per frame (RTX graphics card)
- **The best format**: AV1 > HEVC > H.264, automatically picking the most efficient format both sides support; scaling and color conversion use SIMD, and all buffers are reused
- **No lag build-up**: the host limits the bytes in flight (≈ bitrate × (RTT + 50 ms)) and skips to the latest frame on a slow network; the bitrate follows the measured queueing delay and bandwidth on every acknowledgement, backing off within a few hundred milliseconds and recovering gradually
- **Direct path**: besides the relay, the two ends punch a direct path through their NATs (on the same LAN, or whenever the NAT isn't symmetric), so video and audio stop detouring through the server; the lower-latency path is picked automatically, and if the direct path breaks the session falls back to the relay without dropping
- **QUIC + BBR**: BBR congestion control is steadier than Cubic on lossy networks such as Wi-Fi or long-distance links; control messages, audio and video are queued separately, so mouse input and pings never wait behind a large frame; the relay only forwards bytes and never parses the video
- **Loss doesn't stall the picture**: each frame travels on its own QUIC stream, so a lost packet only holds up that frame. A frame that keeps not arriving is abandoned (no more retransmitting stale data) and the encoder continues from a long-term reference frame the controller already has (reference invalidation) instead of sending a large keyframe (Windows H.264, NVIDIA AV1; other encoders send a keyframe)
- **Decode and show**: the decoder runs in low-latency mode, and each frame is drawn to a desynchronized canvas as soon as it's decoded, without waiting for vsync
- **Local pointer**: the remote cursor's shape is mirrored locally, and moving it happens locally
- **Low bandwidth**: no frames are sent while the screen is still, so an idle desktop uses almost nothing; sessions that aren't on screen drop to 5 fps

See [How it works → Video](docs/architecture.md#video) for details.

## Features

- **Windows system service**: the lock screen, the sign-in screen and UAC prompts can be seen and controlled, and the computer can be reached after boot, before anyone signs in
- **Works with the monitor off** (Windows): when the host's monitor is switched off (or there's none), a virtual display fills in automatically; while a controller is connected the screen doesn't turn off and the computer doesn't sleep. On a Mac the same goes for a closed laptop lid (on a power adapter) or a Mac mini with no display
- **Smooth on a Mac's Wi-Fi** (macOS): AirDrop's Wi-Fi peer-to-peer link (AWDL) keeps borrowing a Mac's wireless card, which makes remote control over Wi-Fi stutter now and then. The controller says so when it happens, and an option in the menu pauses AWDL while a remote session runs on Wi-Fi (as host or controller) and resumes it afterwards
- **Privacy mode** (Windows, macOS): with one click the remote computer's monitors all go blank and its keyboard and mouse stop working, so only you can see and control it; it ends by itself after you disconnect, with the remote screen locked first
- **Fixed control codes**: they survive restarts, upgrades and even server restarts until you change them yourself
- **Console**: browser-style tabs to control several computers at once, plus a multi-screen overview to watch the