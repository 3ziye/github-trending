**📢 Important news about development:** https://github.com/pwnnex/ByeByeVPN/issues/9

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
   Full TSPU/DPI/VPN detectability scanner   v2.5.9
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
| 2  | GeoIP aggregation               | 9 providers (3 EU / 3 RU / 3 global) in parallel, ASN + flags           |
| 3a | TCP port scan                   | Connect-scan 1-65535 (default) or 205 curated ports, 500 threads        |
| 3b | TCP stack fingerprint (v2.5.9)  | Handshake distribution + SIO_TCP_INFO peer window/MSS + closed-port behavior, no admin |
| 4  | UDP probes                      | Real handshakes: DNS, IKE, OpenVPN, QUIC, WG, Tailscale, L2TP, Hysteria2, TUIC, AmneziaWG |
| 5  | Service fingerprint + CT        | SSH, HTTP, TLS + SNI consistency, SOCKS5, CONNECT, Shadowsocks, crt.sh, proxy-header leak |
| 5b | uTLS dual-probe + JA4 (v2.5.9)  | Two TLS handshakes per TLS port (chrome-flavored ctx vs openssl-default), JA4 / JA4S extracted from raw CH/SH bytes |
| 6  | J3 / TSPU active probing        | 8 probes per TLS port (Reality discriminator)                           |
| 7  | SNITCH + traceroute + SSTP      | RTT vs GeoIP (methodika §10.1), ICMP hop-count, Microsoft SSTP          |
| 8  | Verdict + TSPU emulation        | Score 0-100, stack identification, 3-tier TSPU ruling, hardening advice |

### UDP handshakes

| Port       | Protocol           | Payload                                               |
|------------|--------------------|-------------------------------------------------------|
| 53         | DNS                | A query for `example.com` (txn id randomized)         |
| 500, 4500  | IKEv2              | ISAKMP SA_INIT header                                 |
| 1194       | OpenVPN            | HARD_RESET_CLIENT_V2                                  |
| 443        | QUIC v1            | 1200-byte Initial (random DCID)                       |
| 51820      | WireGuard          | 148-byte MessageInitiation                            |
| 41641      | Tailscale          | WG-style handshake                                    |
| 1701       | L2TP               | SCCRQ with mandatory AVPs, random tunnel-id           |
| 36712      |