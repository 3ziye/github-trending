# Whitelist Bypass

Tunnels internet traffic through video calling platforms (VK Call, Yandex Telemost) to bypass government whitelist censorship.

## How it works

Two tunnel modes are available: **DC** (DataChannel) and **Pion Video** (VP8 data encoding).

### DC mode

Browser-based. JavaScript hooks intercept RTCPeerConnection on the call page, create a DataChannel alongside the call's built-in channels, and use it as a bidirectional data pipe.

- **VK Call** - Negotiated DataChannel id:2 (alongside VK's animoji channel id:1). P2P via TURN relay
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
DataChannel  <--- TURN/SFU --->   DataChannel
                                            |
                                        WebSocket (:9000)
                                            |
                                        Go relay
                                            |
                                        Internet
```

### Pion Video mode

Go-based. Pion (Go WebRTC library) connects directly to the platform's TURN/SFU servers, bypassing the browser's WebRTC stack entirely. Data is encoded inside VP8 video frames.

- **VK Call** - Single PeerConnection, P2P via TURN relay
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
Pion WebRTC  <--- TURN/SFU --->   Pion WebRTC
                                            |
                                        Relay bridge
                                            |
                                        Internet
```

Traffic goes through the platform's TURN servers which are whitelisted. To the network firewall it looks like a normal video call.

## Components

- `hooks/` - JavaScript hooks injected into call pages
  - `joiner-vk.js`, `creator-vk.js` - VK Call DC hooks
  - `joiner-telemost.js`, `creator-telemost.js` - Telemost DC hooks
  - `pion-vk.js`, `pion-telemost.js` - Pion Video hooks (MockPeerConnection mode)
  - DC hooks intercept RTCPeerConnection, create tunnel DataChannel, bridge to local WebSocket
  - Pion hooks replace RTCPeerConnection with MockPC, forward SDP/ICE to Pion via WebSocket
  - Telemost hooks include fake media (camera/mic), message chunking (994B payload, 1000B total), and SDP renegotiation
- `relay/` - Go relay binary and gomobile library
  - `relay/mobile/` - DC mode: SOCKS5 proxy, WebSocket server, binary framing protocol
  - `relay/pion/` - Pion Video mode: VP8 data tunnel, relay bridge, SOCKS5 proxy
    - `common.go` - Shared types, WebSocket helper, ICE server parsing, AndroidNet
    - `vk.go` - VK Pion client (single PeerConnection, P2P)
    - `telemost.go` - Telemost Pion client (dual PeerConnection, pub/sub)
    - `vp8tunnel.go` - VP8 frame encoding/decoding, keepalive generation
    - `relay.go` - Relay bridge with connection multiplexing, SOCKS5 proxy, UDP ASSOCIATE
  - `relay/mobile/tun_android.go` - Android-only: tun2socks + fdsan fix (CGo)
  - `relay/mobile/tun_stub.go` - Desktop stub (no tun2socks needed)
- `android-app/` - Android joiner app
  - WebView loading call page with hook injection
  - VpnService capturing all device traffic
  - Tunnel mode selector (DC / Pion Video