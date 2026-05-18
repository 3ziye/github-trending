# ByeByeVPN

Клиентский сканер детектируемости VPN / DPI / Reality / ТСПУ. Одна
статическая `byebyevpn.exe` под Windows (работает через Wine на Linux
и macOS), без прав администратора, без DLL-зависимостей.

```
 ____             ____           __     ______  _   _
| __ ) _   _  ___| __ ) _   _  __\ \   / /  _ \| \ | |
|  _ \| | | |/ _ \  _ \| | | |/ _ \ \ / /| |_) |  \| |
| |_) | |_| |  __/ |_) | |_| |  __/\ V / |  __/| |\  |
|____/ \__, |\___|____/ \__, |\___| \_/  |_|   |_| \_|
       |___/            |___/
   Full TSPU/DPI/VPN detectability scanner   v2.7.0
```

**Languages:** [English](#english) · [Русский](#русский) · [简体中文](README.zh-CN.md) · [فارسی](README.fa.md)

**Discussion / report issues:**
[ntc.party/t/byebyevpn/24325](https://ntc.party/t/byebyevpn/24325) ·
[GitHub Issues](https://github.com/pwnnex/ByeByeVPN/issues)

<a href="https://nowpayments.io/donation/byebyevpn" target="_blank" rel="noreferrer noopener">
    <img src="https://nowpayments.io/images/embeds/donation-button-black.svg" alt="Crypto donation button by NOWPayments">
</a>

---

## English

### Purpose

Given an IP or hostname, run the full Russian OCR методика (§5-10) plus
modern 2026 tunnel fingerprints against it from an external vantage
point. Output: a detection score, the identified stack, and what a
TSPU-class classifier would decide. No VPN connection to the target
is needed - the scanner looks at the destination as a third-party
observer, the way an ISP or DPI middlebox sees it.

### Prerequisites (read before scanning)

> **Disable any active VPN / Zapret / proxy on the host running the
> scanner before you start.** the scanner uses the host's TCP/IP and
> TLS stack to emit probes. if your host routes through a TUN /
> sing-box / Zapret / GoodbyeDPI / proxifier, the wire-level signature
> you measure on the target is **your local stack reflected**, not the
> target's. specifically:
>
> - latency anchors and RTT to anchors will be wrong, breaking SNITCH.
> - ClientHello bytes may be rewritten by Zapret-style fragmentors,
>   breaking JA4 calculation.
> - GeoIP queries will resolve YOUR exit IP, not the lookups you want.
> - the `local` mode (`byebyevpn local`) is the one place where active
>   VPN matters in reverse: there the goal IS to inspect your own
>   adapters, but you still want to scan a remote target with the VPN
>   off.
>
> turn the VPN/proxy off, run the scan, then re-enable. on Windows:
> kill the v2rayN/sing-box/Zapret process and confirm
> `Get-NetAdapter` shows no active TUN/WireGuard/Wintun/TAP-style
> interfaces.

### Pipeline

| # | Module                          | What it does                                                            |
|---|---------------------------------|-------------------------------------------------------------------------|
| 1  | DNS resolve                     | A + AAAA, IPv4 preferred                                                |
| 2  | GeoIP aggregation               | 5 HTTPS-only providers in parallel, ASN + flags                         |
| 3a | TCP port scan                   | Connect-scan 1-65535 (default) or 205 curated ports, 500 threads        |
| 3b | TCP stack fingerprint           | Handshake distribution + SIO_TCP_INFO peer window/MSS + closed-port behavior, no admin |
| 4  | UDP probes                      | WireGuard / AmneziaWG / Hysteria2 handshakes                            |
| 4b | AmneziaWG S1 deep-probe (v2.6.0)| Junk-prefix size sweep on :51820, recovers the configured S1 parameter  |
| 5  | Service fingerprint + CT        | SSH, HTTP, TLS + SNI consistency, SOCKS5, CONNECT, Shadowsocks, crt.sh, proxy-header leak |
| 5b | uTLS dual-probe + JA4 + JA4S    | Two ClientHellos per TLS port (byte-accurate Chrome 131 vs openssl-default), JA4 / JA4S extracted from raw CH/SH bytes, JA4S classified against a backend-stack table |
| 6  | J3 / TSPU active probing        | 8 probes per TLS port (Reality discriminator)                           |
| 7  | SNITCH + traceroute + SSTP      | RTT vs GeoIP (methodika §10.1), ICMP hop-count, Microsoft SSTP          |
| 8  | Verdict + TSPU emulation        | Score 0-100, stack identification, 3-tier TSPU ruling, hardening advice |

### UDP handshakes

v2.6.0 narrowed the UDP set to the modern signature-less tunnels.
the legacy OpenVPN / IKEv2 / L2TP / TUIC / plain-QUIC / DNS probes were
removed: those protocols carry fixed-port / fixed-header signatures any
DPI already catches, so probing for them cost scan time without adding
detection value for this niche.

| Port       | Protocol           | Payload                                               |
|------------|--------------------|-------------------------------------------------------|
| 51820      | WireGuard          | 148-byte MessageInitiation, randomized body           |
| 51820      | AmneziaWG Sx=8     | Delta-probe: vanilla WG rejected, Sx=8 prefix accepted |
| 55555      | AmneziaWG Sx=8     | 8-byte junk prefix + WG init                          |
| 5182