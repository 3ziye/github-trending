# VMkatz

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Build](https://github.com/nikaiw/VMkatz/actions/workflows/release.yml/badge.svg)](https://github.com/nikaiw/VMkatz/actions/workflows/release.yml)
[![Clippy](https://github.com/nikaiw/VMkatz/actions/workflows/clippy.yml/badge.svg)](https://github.com/nikaiw/VMkatz/actions/workflows/clippy.yml)
[![Platform](https://img.shields.io/badge/platform-linux%20|%20windows%20|%20macos%20|%20esxi-lightgrey)]()

## Too Big to Steal

You are three weeks into a red team engagement. Your traffic crawls through a VPN, then bounces across four SOCKS proxies chained through compromised jump boxes before it touches the target network. Every packet takes the scenic route.

After days of lateral movement you land on a NAS attached to the virtualization cluster and the directory listing hits different: rows upon rows of `.vmdk`, `.vmsn`, `.sav`. Hundreds of gigabytes of virtual machines - domain controllers, admin workstations, the crown jewels - sitting right there.

But your link wheezes at 200 KB/s. Pulling a single 100 GB disk image would take **six days**, and every hour of sustained exfil is another chance the SOC spots the anomaly, burns your tunnel, and the whole chain collapses.

Without VMkatz, the traditional workflow looks like this: exfiltrate the entire VM disk or memory snapshot, mount it locally, install a full Windows analysis stack, load the snapshot into a debugger or use mimikatz on a booted copy, and manually piece together credentials from each VM - one at a time. Multiply that by a dozen VMs on the cluster and you are looking at days of bandwidth, tooling, and post-processing.

VMkatz exists because you shouldn't have to exfiltrate what you can read in place. It extracts Windows secrets - NTLM hashes, DPAPI master keys, Kerberos tickets, cached domain credentials, LSA secrets, NTDS.dit - directly from VM memory snapshots and virtual disks, **on the NAS, the hypervisor, wherever the VM files are**.

A single static binary, ~2.5 MB. Drop it on the ESXi host, the Proxmox node, or the NAS. Point it at a `.vmsn`, `.vmdk`, or an entire VM folder. Walk away with credentials, not disk images.

## What It Extracts

### From memory snapshots (LSASS)
All 9 SSP credential providers that mimikatz implements:

| Provider | Data | Notes |
| --- | --- | --- |
| MSV1_0 | NT/LM hashes, SHA1 | Physical-scan fallback for paged entries |
| WDigest | Plaintext passwords | Linked-list walk + `.data` fallback |
| Kerberos | AES/RC4/DES keys, tickets (`.kirbi`/`.ccache`) | AVL tree walk, often paged in VM snapshots |
| TsPkg | Plaintext passwords | RDP sessions only |
| DPAPI | Master key cache (GUID + decrypted key) | SHA1 masterkey for offline DPAPI decrypt |
| SSP | Plaintext credentials | `SspCredentialList` in `msv1_0.dll` |
| LiveSSP | Plaintext credentials | Requires `livessp.dll` (rare post-Win8) |
| Credman | Stored credentials | Hash-table + single-list enumeration |
| CloudAP | Azure AD tokens | Typically empty for local-only logon |

### From virtual disks (offline)
- **SAM hashes**: Local account NT/LM hashes
- **LSA secrets**: Service account passwords, auto-logon credentials, machine account keys
- **Cached domain credentials**: DCC2 hashes (last N domain logons)
- **DPAPI master keys**: Hashcat-ready hashes from user master key files (`$DPAPImk$` — modes 15300/15900)
- **NTDS.dit**: Full Active Directory hash extraction from domain controller disks, natively from the ESE database - no impacket or external tools needed

## Supported Inputs

| Format | Extensions | Source | Status |
| --- | --- | --- | --- |
| VMware snapshots | `.vmsn` + `.vmem` | Workstation, ESXi | Tested |
| VirtualBox saved states | `.sav` | VirtualBox | Tested |
| QEMU/KVM ELF core dumps | `.elf` | `virsh dump`, `dump-guest-memory` | Untested |
| Hyper-V saved states | `.vmrs` | Hyper-V 2016+ (native parser) | Untested |
| Hyper-V memory dumps | `.bin`, `.raw` | Legacy saved states, raw dumps | Untested |
| VMware virtual disks | `.vmdk` (sparse + flat) | Workstation, ESXi | Tested |
| VirtualBox virtual disks | `.vdi` | VirtualBox | Tested |
| QEMU/KVM virtual disks | `.qcow2` | QEMU, Proxmox | Tested |
| Hyper-V virtual disks | `.vhdx`, `.vhd` | Hyper-V | Untested |
| VMFS-6 raw SCSI devices | `/dev/disks/...` | ESXi datastores (bypasses file locks) | Tested |
| LVM block devices | `/dev/...` | Proxmox LVM-thin, raw LVs | Tested |
| Raw registry hives | `SAM`, `SYSTEM`, `SECURITY` | Exported from disk or `reg save` | Tested |
| Raw NTDS.dit | `ntds.dit` + `SYSTEM` | Copied from domain controller | Tested |
| LSASS minidump | `.dmp` | `--dump lsass`, procdump, Task Manager | Tested |
| VM directories | any folder | Auto-discovers all processable files | Tested |

**Target OS**: Windows XP SP3 through Windows Server 2025 (x86 PAE + x64, auto-detected).

## Quick Start

```bash
# Build (default features: all hypervisors + disk + NTDS)
cargo build --release
