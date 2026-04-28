# gopacket

A complete Go implementation of [Impacket](https://github.com/fortra/impacket) - 63 tools and 24 library packages for Windows network protocol interaction, Active Directory enumeration, and attack execution. Built as a native Go framework so you can compile once and run anywhere without Python dependencies.

> **Beta Release - Highly Experimental.** gopacket is under active development. Core tools have been tested against Active Directory lab environments, but edge cases and protocol quirks are expected. If something isn't working, please test the same operation with Impacket side-by-side and include both outputs in your bug report. This helps us quickly identify whether it's a gopacket-specific issue or a shared protocol limitation.

## Installation

```bash
git clone https://github.com/mandiant/gopacket
cd gopacket

# Default: Linux/macOS build + install to /usr/local/bin
./install.sh

# Run with no flags and it prompts you through the choices interactively.
# Or pick a target directly:
./install.sh --target portable   # static Linux binaries in ./dist/portable/
./install.sh --target windows    # Windows .exe cross-compiles in ./dist/windows/
./install.sh --target all        # build every target in one run

# Build without installing (native only)
./install.sh --build-only

# Or build with make
make build
```

The default (`--target native`) build needs Go 1.24.13+, GCC, and libpcap
development headers (`apt install build-essential libpcap-dev` on
Debian/Ubuntu/Kali, `yum install gcc libpcap-devel` on RHEL/CentOS, or
`brew install libpcap` on macOS). The `portable` and `windows` targets only
need the Go toolchain; `sniff` and `split` become stubs in those builds
because they require libpcap. See [Platform Support](#platform-support) for
the full matrix.

### Platform Support

gopacket builds on Linux, macOS, and Windows. The set of working tools and
available proxying paths depends on the build flags:

| Build                                  | Tools available                        | Proxying                                            |
|----------------------------------------|----------------------------------------|-----------------------------------------------------|
| Linux / macOS with cgo (default)       | All 63                                 | proxychains (LD_PRELOAD) and/or `-proxy` SOCKS5     |
| Linux with `CGO_ENABLED=0`             | 61 (`sniff`, `split` become stubs)     | `-proxy` only (proxychains needs the libc hook)     |
| Windows (`GOOS=windows CGO_ENABLED=0`) | 60 (`sniff`, `split`, `sniffer` stubs) | `-proxy` only (no `LD_PRELOAD` on Windows)          |

`sniff` and `split` depend on libpcap via cgo; `sniffer` depends on Unix raw
sockets. When a tool can't be built for the target, gopacket substitutes a
stub that prints a clear message and exits 1, so `go build ./...` always
succeeds and the install layout is consistent across platforms.

To uninstall:
```bash
./install.sh --uninstall
```

## Proxy Support

gopacket supports two independent proxying paths. They can also be chained.

### proxychains (LD_PRELOAD)

All gopacket tools work through proxychains. Go binaries normally bypass proxychains because Go's runtime handles DNS and networking internally, skipping the `LD_PRELOAD` hooks that proxychains relies on. gopacket works around this by linking against the system C library for network operations, allowing proxychains to intercept connections normally.

```bash
proxychains gopacket-secretsdump 'domain/user:password@target'
proxychains gopacket-smbclient -k -no-pass 'domain/user@dc.domain.local'
```

### Internal SOCKS5 proxy (`-proxy`)

Every tool accepts `-proxy` to route outbound TCP through a SOCKS5 server without relying on `LD_PRELOAD`. Accepted schemes: `socks5` and `socks5h`. When `-proxy` is unset, the `ALL_PROXY` / `all_proxy` environment variables are consulted as a fallback.

```bash
gopacket-secretsdump -proxy socks5h://127.0.0.1:1080 'domain/user:password@target'
ALL_PROXY=socks5h://127.0.0.1:1080 gopacket-smbclient 'domain/user:password@target'
```

UDP-dependent features are **disabled** under `-proxy` rather than silently leaking packets (SOCKS5 UDP ASSOCIATE is rarely supported by proxies, and bypassing the proxy for UDP would reveal the operator's real source IP). Affected features and their workarounds are documented in [KNOWN_ISSUES.md](KNOWN_ISSUES.md).

**Chaining:** `-proxy` is compatible with proxychains. The TCP connection to the SOCKS5 proxy itself still goes through libc `connect()`, so `proxychains → gopacket → -proxy → target` works for nested routing scenarios.

## Documentation

See the [Library Developer Guide](https://github.com/mandiant/gopacket/wiki) for full API documentation, code examples, and architecture overview for building custom tools on top of gopacket's 24 protocol packages.

## Tools (63)

### Remote Execution
| Tool | Description |
|------|-------------|
| **psexec** | Remote command execution via SMB service creati