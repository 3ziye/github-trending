# TailVNC

A Windows remote desktop persistence tool built on top of Tailscale's WireGuard-encrypted mesh network. TailVNC embeds a fully self-contained VNC server and Tailscale node into a single binary, enabling secure remote desktop access over Tailscale/Headscale without exposing any ports to the public internet. Designed for both legitimate infrastructure administration and red team persistence operations.

Inspired by [SockTail](https://github.com/Yeeb1/SockTail).

## Features

- **Tailscale/Headscale Integration** - Leverages `tsnet` to embed a WireGuard peer directly into the binary; supports both official Tailscale coordination and self-hosted Headscale control planes
- **Windows Session 0 Isolation Bypass** - When running as SYSTEM, automatically spawns an agent process in the active user session via `CreateProcessAsUser` and proxies VNC traffic through IPC, circumventing Vista+ session isolation
- **Dynamic Desktop Tracking** - Follows the user across desktop transitions including the default desktop, Winlogon (login screen), UAC secure desktop, and lock screen via `OpenInputDesktop`/`SetThreadDesktop`
- **Ctrl+Alt+Del Injection** - Sends the Secure Attention Sequence from Session 0 via `sas.dll!SendSAS`
- **Bidirectional Clipboard Sync** - Latin-1 clipboard synchronization between VNC client and target host
- **Build-Time Configuration Embedding** - Auth key, VNC password, listen port, and control URL are injected at compile time via LDFLAGS; the resulting binary requires no configuration files at runtime
- **Auth Key Obfuscation** - Tailscale auth key is XOR-obfuscated at build time to prevent plaintext credential exposure in the binary

## Architecture

```
┌──────────────────────────────────────────────┐
│          TailVNC Service (Session 0)         │
│                                              │
│  tsnet.Server ───► Tailscale/Headscale Net   │
│       │                                      │
│  VNC Listener :5900 (Tailscale interface)    │
│       │                                      │
│  ┌────▼───────────────────────────────────┐  │
│  │ Session Manager                        │  │
│  │  - Polls active console session (2s)   │  │
│  │  - Spawns agent via CreateProcessAsUser│  │
│  │  - Auto-restarts on session change     │  │
│  │    or agent crash                      │  │
│  └────┬───────────────────────────────────┘  │
│       │ TCP Proxy (bidirectional)            │
└───────┼──────────────────────────────────────┘
        ▼
┌────────────────────────────────────────┐
│   VNC Agent (User Session, Desktop)    │
│   127.0.0.1:15900                      │
│   - GDI+ screen capture (~30fps)       │
│   - SendInput keyboard/mouse injection │
│   - Clipboard monitoring               │
└────────────────────────────────────────┘
```

## Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Go 1.25+ |
| Network Transport | [Tailscale tsnet](https://pkg.go.dev/tailscale.com/tsnet) — embedded WireGuard peer |
| VNC Protocol | RFB 3.008 (custom implementation, Raw encoding) |
| Screen Capture | Windows GDI+ (`CreateDIBSection`, `BitBlt`) |
| Input Injection | Windows `SendInput` API |
| Session Management | `WTSQueryUserToken` + `CreateProcessAsUser` |
| Desktop Switching | `OpenInputDesktop` + `SetThreadDesktop` |
| SAS Injection | `sas.dll!SendSAS` |
| Authentication | VNC DES challenge-response (per RFB spec) |
| Key Obfuscation | XOR + hex encoding |
| System Calls | `golang.org/x/sys` (Windows syscall wrappers) |
| Binary Compression | UPX (optional) |
| Build System | GNU Make + Go LDFLAGS injection |

## Building

### Prerequisites

- **Go** >= 1.25.3
- **GNU Make**
- **UPX** (optional, for binary size reduction)
- **Tailscale Auth Key** — generate from the Tailscale admin console; reusable + ephemeral keys are recommended for operational use

### Build Parameters

| Parameter | Required | Default | Description |
|-----------|----------|---------|-------------|
| `AUTH_KEY` | Yes | — | Tailscale auth key; automatically XOR-obfuscated and embedded at compile time |
| `LISTEN_PORT` | No | `5900` | VNC listen port on the Tailscale interface |
| `AUTH_PASS` | No | Empty (no auth) | VNC connection password (DES challenge-response) |
| `CONTROL_URL` | No | Empty (official Tailscale) | Headscale control plane URL |
| `CONFIG_DIR` | No | `C:\Windows\Temp\.cache` | Persistent tsnet state directory (WireGuard keys, node identity) |

### Compilation

```bash
# Minimal build — only auth key required
make build-vnc AUTH_KEY=tskey-auth-kBEXAMPLEKEY

# Full build with all parameters
# [CONTROL_URL] — optional, only required when using a self-hosted Headscale control plane
# [CONFIG_DIR]  — optional, overrides the default tsnet state directory (C:\Windows\Temp\.cache)
make build-vnc \
  AUTH_KEY=tskey-auth-kBEXAMPLEKEY \
  LISTEN_PORT=5900 \
  AUTH_PASS=VNCPassword \
  [CONTROL_URL=https://headscale.example.com] \
  [CONFIG_DIR='C:\Windows\Temp\.cache']
```

Build artifacts are w