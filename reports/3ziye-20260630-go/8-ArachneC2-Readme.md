# Arachne C2

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/3c009f8e-1bc2-4620-854b-a5c53e108893" />



A decentralized Command & Control framework built on **libp2p** (the peer-to-peer networking
stack behind IPFS). No servers, no domains, no IPs to block — just cryptographic identities
communicating over the global p2p network.

Inspired by [Sliver](https://github.com/BishopFox/sliver), but redesigned for decentralized
infrastructure.

## Key Idea

Instead of running a C2 server on a VPS that can be taken down, Arachne uses **GossipSub
(PubSub)** and **DHT peer discovery** over the IPFS peer-to-peer network. Your implant
fleet and operator are all equal peers in the network — no central point of failure.

## Features

- Self-contained single binary — no source tree needed to generate implants
- Beacon-mode implants that maintain presence via PubSub topics
- DHT-based peer discovery — no hardcoded server IPs
- Encrypted and signed messages (Ed25519 + NaCl box)
- Interactive operator console (list, select, exec, ls, ps, cd, pwd, download, upload)
- Interactive shell over direct libp2p stream (PTY on Linux/macOS, hidden ConPTY on Windows)
- Port forwarding through implant via direct libp2p stream
- Cross-platform implants (Linux, macOS, Windows)
- Protocol Buffers message format with per-message signature verification
- Opaque protocol identifiers (short proto package names, Z-series message types, short wire IDs)
- Per-implant command topics — commands reach only the intended implant
- Built-in hole punching and NAT traversal
- Automatic Go installation if missing (generates implants anywhere)
- Garble-based obfuscation (`--obfuscate` — strips names, literals, paths)
- Cover traffic to mask beacon timing signatures
- Persistent implant identity (embedded keypair per build)
- Quiet mode (`--quiet` — daemonize on Linux/macOS, hide console on Windows)
- Automatic implant disconnect detection and alerting
- Stream keepalive prevents relay circuit idle timeout
- WebSocket + TCP transport (UDP/multicast-free for sandbox compatibility)
- VM detection (`--antivm` — 65+ detection techniques with VMAware-compatible scoring, no CGO required)

## Project Structure

```
arachne-c2/
├── build.sh                # Build script (auto-installs Go if missing)
├── bin/                    # Compiled binaries
├── cmd/
│   └── arachne/            # Single entry point (serve + generate)
├── docs/                   # Design documentation
├── implant/                # Implant agent code
│   └── core/               # Agent runtime, command handlers, shell, portfwd
├── pkg/
│   ├── config/             # Shared config types
│   ├── cryptography/       # Ed25519 + NaCl key management
│   └── transport/          # libp2p node, messenger, PubSub helpers
├── protobuf/               # Protocol Buffers definitions
│   ├── apb/                # C2 protocol messages (opaque type names: Z1, Z2, ...)
│   ├── cpb/                # Common types (Process, Response, Request)
│   └── rpb/                # RPC service definitions (service S, methods M0-M13)
└── server/                 # Operator node (the "server")
    └── core/               # Operator logic, implant tracking, CLI, generate
```

## Build

The operator binary is self-contained — embed the implant source at build time, then it builds implants anywhere:

```bash
./build.sh       # auto-installs Go if missing, embeds source, cross-compiles for all platforms
```

Binaries are written to `bin/` as `arachne-{os}-{arch}` (or `*.exe` for Windows). The built binary can be copied to any machine with Go installed (or no Go — it auto-installs). No source tree needed.

## Quick Start

### 1. Run the operator

```bash
./bin/arachne
```

On first run, generates a keypair at `~/.arachne/operator.key` and exports the public
key to `~/.arachne/operator.pub`.

### 2. Build an implant

From the operator console (`generate`) or standalone:

```bash
./bin/arachne generate --os linux --arch amd64 --output ./myimplant --upx
```

Flags: `--os` (linux, darwin, windows), `--arch` (amd64, arm64), `--output`, `--pubkey`, `--upx` (default true), `--obfuscate`, `--quiet`, `--antivm`.

Use `--obfuscate` to strip function names, package paths, and literal strings via [garble](https://github.com/burrowers/garble) (auto-installed if missing). Combine with `--upx` for maximum hardening.

Use `--antivm` to compile in VM detection. The implant runs 65+ detection techniques (CPUID signatures, MAC prefixes, DMI/SMBIOS, PCI vendor IDs, process enumeration, registry keys, container detection) with a [VMAware](https://github.com/kernelwernel/VMAware)-compatible accumulated scoring system. Exits cleanly if the score exceeds 50%. Pure Go — no CGO, no cross-compilers needed.

Each build generates a unique embedded keypair — the implant keeps the same PeerID across restarts.

### 3. Deploy and run the implant

Copy `./myimplant` to the target machine and run:

```bash
./myimplant
```

