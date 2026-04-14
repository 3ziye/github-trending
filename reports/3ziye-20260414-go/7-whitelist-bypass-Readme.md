# Whitelist Bypass

Tunnels internet traffic through video calling platforms (VK Call, Yandex Telemost) to bypass government whitelist censorship.

## Setup

Step-by-step setup guide (in Russian): [docs/SETUP.md](docs/SETUP.md)

## How it works

Two tunnel modes are available: **DC** (DataChannel) and **Pion Video** (VP8 data encoding).

### DC mode

Browser-based. JavaScript hooks intercept RTCPeerConnection on the call page, create a DataChannel alongside the call's built-in channels, and use it as a bidirectional data pipe.

- **VK Call** - Negotiated DataChannel id:2 (alongside VK's animoji channel id:1). Data flows through VK's SFU
- **Telemost** - Non-negotiated DataChannel labeled "sharing" (matching real screen sharing traffic), with SDP renegotiation via signaling WebSocket. SFU architecture

```
Joiner (censored, Android)                Creator (free internet, desktop)

All apps
  |
VpnService (captures all traffic)
  |
tun2socks (IP -> TCP)
  |
SOCKS5 proxy (Go, :1080)
  |
WebSocket (:9000)
  |
WebView (call page)                       Electron (call page)
  |                                         |
DataChannel  <----- SFU ----->   DataChannel
                                            |
                                        WebSocket (:9000)
                                            |
                                        Go relay
                                            |
                                        Internet
```

### Pion Video mode

Go-based. Pion (Go WebRTC library) connects directly to the platform's TURN/SFU servers, bypassing the browser's WebRTC stack entirely. Data is encoded inside VP8 video frames.

- **VK Call** - Single PeerConnection, data flows through VK's SFU
- **Telemost** - Dual PeerConnection (pub/sub), SFU architecture

The JS hook replaces `RTCPeerConnection` with a `MockPeerConnection` that forwards all SDP/ICE operations to the local Pion server via WebSocket. Pion creates the real PeerConnection with the platform's TURN servers.

**VP8 data encoding:**
- Data frames: `[0xFF marker][4B length][payload]` - sent as VP8 video samples
- Keepalive frames: valid VP8 interframes (17 bytes) at 25fps, keyframe every 60th frame. Keeps the video track alive so the SFU/TURN does not disconnect
- The `0xFF` marker byte distinguishes data from real VP8 (keyframe first byte has bit0=0, interframe has bit0=1, so `0xFF` never appears naturally)
- On the receiving side, RTP packets are reassembled into full frames. First byte `0xFF` = extract data, otherwise = keepalive, ignore

**Multiplexing protocol** over the VP8 tunnel: `[4B frame length][4B connID][1B msgType][payload]`
- Message types: Connect, ConnectOK, ConnectErr, Data, Close, UDP, UDPReply
- Multiple TCP/UDP connections are multiplexed into a single VP8 video stream

```
Joiner (censored, Android)                Creator (free internet, desktop)

All apps
  |
VpnService (captures all traffic)
  |
tun2socks (IP -> TCP)
  |
SOCKS5 proxy (Go, :1080)
  |
VP8 data tunnel (Pion)                    VP8 data tunnel (Pion)
  |                                         |
MockPC (WebView)                          MockPC (Electron)
  |                                         |
Pion WebRTC  <------ SFU ------>  Pion WebRTC
                                            |
                                        Relay bridge
                                            |
                                        Internet
```

Traffic goes through the platform's SFU servers which are whitelisted. To the network firewall it looks like a normal video call.

## Components

- `hooks/` - JavaScript hooks for DC, Video, and Headless modes (VK and Telemost)
- `relay/` - Go relay: SOCKS5 proxy, WebSocket server, VP8 video tunnel, headless joiner, connection multiplexing
- `headless/vk/` - Headless VK creator: creates calls via API, Pion DataChannel tunnel, no browser
- `headless/telemost/` - Headless Telemost creator: same approach for Yandex Telemost
- `android-app/` - Android joiner app (WebView/headless + VpnService + Go relay)
- `creator-app/` - Electron desktop creator app

## Download

Prebuilt binaries are available on [GitHub Releases](../../releases).

### Creator side (free internet, desktop)

Download and run the Electron app from [GitHub Releases](../../releases). It bundles the Go relay automatically.

1. Open the app
2. Select tunnel mode (DC or Pion Video)
3. Click "VK" or "Telemost"
4. Log in, **create a new call** from the app
5. Copy the join link, send it to the joiner

**Important:** The call must be created from within the Creator app. Joining an existing call from the app will not work - the JS hooks must be present from the moment the call starts.

### Joiner side (censored, Android)

1. Download and install `whitelist-bypass.apk` from [GitHub Releases](../../releases)
2. Select tunnel mode (DC or Pion Video)
3. Paste the call link and tap GO
4. The app joins the call, establishes the tunnel, starts VPN
5. All devic