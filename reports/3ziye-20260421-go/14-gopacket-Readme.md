# gopacket

A complete Go implementation of [Impacket](https://github.com/fortra/impacket) - 63 tools and 24 library packages for Windows network protocol interaction, Active Directory enumeration, and attack execution. Built as a native Go framework so you can compile once and run anywhere without Python dependencies.

> **Beta Release - Highly Experimental.** gopacket is under active development. Core tools have been tested against Active Directory lab environments, but edge cases and protocol quirks are expected. If something isn't working, please test the same operation with Impacket side-by-side and include both outputs in your bug report. This helps us quickly identify whether it's a gopacket-specific issue or a shared protocol limitation.

## Installation

```bash
git clone https://github.com/mandiant/gopacket
cd gopacket

# Build and install all tools as gopacket-<toolname> on your PATH
./install.sh

# Or just build without installing
./install.sh --build-only

# Or build with make
make build
```

Requires Go 1.24.13+, GCC, and libpcap development headers
(install with `apt install build-essential libpcap-dev` on Debian/Ubuntu/Kali,
or `yum install gcc libpcap-devel` on RHEL/CentOS, or `brew install libpcap` on macOS).

The libpcap headers are only needed by the `sniff` and `split` tools - if
libpcap is missing, `install.sh` will skip those two and build the rest.

### Platform Support

Linux and macOS only. Native Windows builds (MSYS2/MINGW64, plain `go build`
on Windows) are **not supported** - `pkg/transport` uses libc's `connect()`
via cgo so that `LD_PRELOAD`-based proxies like proxychains can hook it,
which has no Windows equivalent. On Windows, use
[WSL](https://learn.microsoft.com/windows/wsl/install) and build from inside
the Linux environment.

To uninstall:
```bash
./install.sh --uninstall
```

## Proxychains Support

All gopacket tools work through proxychains. Go binaries normally bypass proxychains because Go's runtime handles DNS and networking internally, skipping the `LD_PRELOAD` hooks that proxychains relies on. gopacket works around this by linking against the system C library for network operations, allowing proxychains to intercept connections normally.

```bash
proxychains gopacket-secretsdump 'domain/user:password@target'
proxychains gopacket-smbclient -k -no-pass 'domain/user@dc.domain.local'
```

## Documentation

See the [Library Developer Guide](https://github.com/mandiant/gopacket/wiki) for full API documentation, code examples, and architecture overview for building custom tools on top of gopacket's 24 protocol packages.

## Tools (63)

### Remote Execution
| Tool | Description |
|------|-------------|
| **psexec** | Remote command execution via SMB service creation |
| **smbexec** | Remote command execution via SMB (stealthier than psexec) |
| **wmiexec** | Remote command execution via WMI |
| **dcomexec** | Remote command execution via DCOM |
| **atexec** | Remote command execution via Task Scheduler |

### Credential Dumping & DPAPI
| Tool | Description |
|------|-------------|
| **secretsdump** | SAM/LSA/NTDS.dit extraction and DCSync (remote + offline) |
| **dpapi** | DPAPI backup key extraction |
| **esentutl** | Offline ESE database parser (NTDS.dit) |
| **registry-read** | Offline Windows registry hive parser |

### Kerberos
| Tool | Description |
|------|-------------|
| **getTGT** | Request a TGT with password, hash, or AES key |
| **getST** | Request a service ticket with S4U2Self/S4U2Proxy |
| **GetUserSPNs** | Kerberoasting - find and request SPNs |
| **GetNPUsers** | AS-REP roasting - find accounts without pre-auth |
| **ticketer** | Golden/silver ticket forging |
| **ticketConverter** | Convert between ccache and kirbi formats |
| **describeTicket** | Parse and decrypt Kerberos tickets |
| **getPac** | Request and parse PAC information |
| **keylistattack** | KERB-KEY-LIST-REQ attack (RODC) |
| **raiseChild** | Child-to-parent domain escalation via golden ticket |

### Active Directory Enumeration
| Tool | Description |
|------|-------------|
| **GetADUsers** | Enumerate domain users via LDAP |
| **GetADComputers** | Enumerate domain computers via LDAP |
| **GetLAPSPassword** | Read LAPS passwords via LDAP |
| **findDelegation** | Find delegation configurations |
| **lookupsid** | SID brute-forcing via LSARPC |
| **samrdump** | Enumerate users via SAMR |
| **rpcdump** | Dump RPC endpoints via epmapper |
| **rpcmap** | Scan for accessible RPC interfaces |
| **net** | net user/group/computer enumeration via SAMR/LSARPC |
| **netview** | Enumerate sessions, shares, and logged-on users |
| **CheckLDAPStatus** | Check LDAP signing and channel binding requirements |
| **DumpNTLMInfo** | Dump NTLM authentication info from SMB negotiation |
| **getArch** | Detect remote OS architecture via RPC |
| **machine_role** | Detect machine role (DC, server, workstation) |

### Active Directory Attacks
| Tool | Description |
|------|-------------|
| **addcomputer** | Creat