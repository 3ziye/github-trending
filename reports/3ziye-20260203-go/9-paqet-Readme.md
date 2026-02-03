# paqet - Transport over Raw Packet

[![Go Version](https://img.shields.io/badge/go-1.25+-blue.svg)](https://golang.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

`paqet` is a bidirectional Packet-level proxy built using raw sockets in Go. It forwards traffic from a local client to a remote server, which then connects to target services. By operating at the packet level, it completely bypasses the host operating system's TCP/IP stack and uses KCP for secure, reliable transport.

> **⚠️ Development Status Notice**
>
> This project is in **active development**. APIs, configuration formats, protocol specifications, and command-line interfaces may change without notice. Expect breaking changes between versions. Use with caution in production environments.

This project serves as an example of low-level network programming in Go, demonstrating concepts like:

- Raw packet crafting and injection with `gopacket`.
- Packet capture with `pcap`.
- Custom binary network protocols.
- The security implications of operating below the standard OS firewall.

## Use Cases and Motivation

`paqet` is designed for specific scenarios where standard VPN or SSH tunnels may be insufficient. Its primary use cases include bypassing firewalls that detect standard handshake protocols by using custom packet structures, network security research for penetration testing and data exfiltration, and evading kernel-level connection tracking for monitoring avoidance.

While `paqet` includes built-in encryption via KCP, it is more complex to configure than general-purpose VPN solutions.

## How It Works

`paqet` creates a transport channel using KCP over raw TCP packets, bypassing the OS's TCP/IP stack entirely. It captures packets using pcap and injects crafted TCP packets containing encrypted transport data, allowing it to bypass kernel-level connection tracking and evade firewalls.

```
[Your App] <------> [paqet Client] <===== Raw TCP Packet =====> [paqet Server] <------> [Target Server]
(e.g. curl)        (localhost:1080)        (Internet)          (Public IP:PORT)     (e.g. https://httpbin.org)
```

The system operates in three layers: raw TCP packet injection, encrypted transport (KCP), and application-level connection multiplexing.

KCP provides reliable, encrypted communication optimized for high-loss or unpredictable networks, using aggressive retransmission, forward error correction, and symmetric encryption with a shared secret key. It is especially well-suited for real-time applications and gaming where low latency are critical.

## Getting Started

### Prerequisites

- `libpcap` development libraries must be installed on both the client and server machines.
  - **Debian/Ubuntu:** `sudo apt-get install libpcap-dev`
  - **RHEL/CentOS/Fedora:** `sudo yum install libpcap-devel`
  - **macOS:** Comes pre-installed with Xcode Command Line Tools. Install with `xcode-select --install`
  - **Windows:** Install Npcap. Download from [npcap.com](https://npcap.com/).

### 1. Download a Release

Download the pre-compiled binary for your client and server operating systems from the project's **Releases page**.

You will also need the configuration files from the `example/` directory.

### 2. Configure the Connection

paqet uses a unified configuration approach with role-based settings. Copy and modify either:

- `example/client.yaml.example` - Client configuration example
- `example/server.yaml.example` - Server configuration example

You must correctly set the interfaces, IP addresses, MAC addresses, and ports.

> **⚠️ Important:**
>
> - **Role Configuration**: Role must be explicitly set as `role: "client"` or `role: "server"`
> - **Transport Security**: KCP requires identical keys on client/server.
> - **Configuration**: See "Critical Configuration Points" section below for detailed security requirements

#### Finding Your Network Details

You'll need to find your network interface name, local IP, and the MAC address of your network's gateway (router).

**On Linux:**

1.  **Find Interface and Local IP:** Run `ip a`. Look for your primary network card (e.g., `eth0`, `ens3`). Its IP address is listed under `inet`.
2.  **Find Gateway MAC:**
    - First, find your gateway's IP: `ip r | grep default`
    - Then, find its MAC address with `arp -n <gateway_ip>` (e.g., `arp -n 192.168.1.1`).

**On macOS:**

1.  **Find Interface and Local IP:** Run `ifconfig`. Look for your primary interface (e.g., `en0`). Its IP is listed under `inet`.
2.  **Find Gateway MAC:**
    - First, find your gateway's IP: `netstat -rn | grep default`
    - Then, find its MAC address with `arp -n <gateway_ip>` (e.g., `arp -n 192.168.1.1`).

**On Windows:**

1. **Find Interface and Local IP:** Run `ipconfig /all` and note your active network adapter (Ethernet or Wi-Fi), along with:
   - Its **IPv4 Address**
   - The **Gateway** IP
2. **Find Interface device GUID:** Windows requires the Npcap device GUID. In Pow