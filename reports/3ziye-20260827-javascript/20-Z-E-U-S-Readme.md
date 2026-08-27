<p align="center">
  🇬🇧 <a href="README.md">English</a> &nbsp;|&nbsp;
  🇮🇷 <a href="README.fa.md">فارسی</a>
</p>

<div align="center">
 
# ⚡ ZEUS PANEL
[![Version](https://img.shields.io/badge/Version-v2.0.5-blue.svg?style=for-the-badge&logo=cloudflare)](https://github.com/zeus-panel/ZEUS-PANEL)
[![Platform](https://img.shields.io/badge/Platform-Cloudflare%20Workers-f38020.svg?style=for-the-badge&logo=cloudflare&logoColor=white)](https://workers.cloudflare.com/)
[![License](https://img.shields.io/badge/License-Proprietary%20(Non--Commercial)-red.svg?style=for-the-badge)](https://github.com/zeus-panel/ZEUS-PANEL/blob/main/LICENSE)
[![Telegram](https://img.shields.io/badge/Community-PANEL__ZEUS-2CA5E0.svg?style=for-the-badge&logo=telegram)](https://t.me/PANEL_ZEUS)
</div>

<table width="100%">
<tr>
<td width="50%" valign="middle" align="center">
<img src="https://raw.githubusercontent.com/panel-zeus/Z-E-U-S/refs/heads/main/photos/dark.png" width="100%" alt="Zeus Panel Dark Mode" style="border-radius: 12px;">
</td>
<td width="50%" valign="middle" align="center">
<img src="https://raw.githubusercontent.com/panel-zeus/Z-E-U-S/refs/heads/main/photos/1.png" width="100%" alt="Zeus Panel Screenshot 1" style="border-radius: 12px;">
</td>
</tr>
<tr>
<td width="50%" valign="middle" align="center">
<img src="https://raw.githubusercontent.com/panel-zeus/Z-E-U-S/refs/heads/main/photos/2.png" width="100%" alt="Zeus Panel Screenshot 2" style="border-radius: 12px;">
</td>
<td width="50%" valign="middle" align="center">
<img src="https://raw.githubusercontent.com/panel-zeus/Z-E-U-S/refs/heads/main/photos/3.png" width="100%" alt="Zeus Panel Screenshot 3" style="border-radius: 12px;">
</td>
</tr>
</table>
 
<table width="100%">
<tr>
<td width="50%" valign="middle" align="center">
<img src="https://raw.githubusercontent.com/panel-zeus/Z-E-U-S/refs/heads/main/photos/bot.png" width="100%" alt="Zeus Panel Status" style="border-radius: 12px;">
</td>
<td width="50%" valign="middle" align="center">
<img src="https://raw.githubusercontent.com/panel-zeus/Z-E-U-S/refs/heads/main/photos/status.png" width="100%" alt="Zeus Panel Dark Mode" style="border-radius: 12px;">
</td>
</tr>
</table>

<div align="center">

[⚡️ Key Features](#features) • [🚀 Deployment Guide](#-quick-deployment-guide) • [🔎 IP Scanner](#-clean-ip-scanner) • [🛡️ SOCKS5 Proxy](#️-build-your-own-socks5-proxy-zeus-relay) • [❤️ Donate](#-donate--support) • [⚖️ License & Copyright](#license-copyright) • [Credits](#credits-section)
</div>


> [!CAUTION]
> **Security Notice**
> If you believe this project does not comply with GitHub's Community Guidelines or Acceptable Use Policies, please let us know. We make every effort to ensure all our projects are secure and compliant with GitHub's policies.

---


## <a id="features"></a>⚡️ Features & Capabilities

**🚀 Core Protocols & Routing**
* 📡 Dual Protocol Support: Native, highly optimized support for both VLESS and Trojan protocols over WebSocket, allowing simultaneous multi-protocol config generation.
* 🌍 Multi-Location Routing (Up to 8 Proxies): Seamlessly assign up to 8 distinct proxies or geographic locations simultaneously to individual users.
* 🔀 Automated Proxy Fallback: Intelligent auto-replacement of failing upstream user proxies with healthy nodes dynamically fetched from dedicated VIP proxy repositories.
* 🌐 Dynamic IP Rotation: Automated rotation of Clean Cloudflare Edge IPs at custom, user-defined intervals (e.g., every 5 minutes).

**🛡 Advanced Anti-Filtering & DPI Bypass**
* 🧩 Advanced TLS Fragmentation: Built-in TLS Fragment support (length and interval) to bypass deep packet inspection (DPI).
* 🇮🇷 ISP-Specific Presets: One-click optimized fragmentation presets for specific network operators (MCI, Irancell, Rightel, TCI, and Gaming mode).
* 🎭 Patterniha (PattN/PattNG) Integration: Native support for advanced JSON fragmentation (fm), Custom Cipher Suites (cs), and TLS Masking (Custom SNI/Host) for ultimate stealth.
* 🕵️ ClientHello Fingerprint Simulator: Dynamically spoof browser fingerprints (Chrome, Safari, iOS, Android, Edge, Randomized, Unsafe) to evade censorship.

**👥 Advanced User Management & Billing**
* ⚖️ Strict Quota Enforcement: Set precise limits based on Traffic Volume (GB), Time Expiration (Days), Total Requests, and Concurrent Devices (IP Limit).
* ⏳ Start on First Connect: Option to delay the countdown of a user's subscription time until their very first successful connection.
* ♻️ Automated Quota Resets: Scheduled auto-reset capabilities for volume and request counters based on user-specific timeframes.
* 🛠 Bulk Operations: Comprehensive multi-select tools for batch user status toggling, deletion, and quota/time resets.

**🛑 Security & Content Control**
* 🚫 Smart Content Blocker: Integrated DNS-over-HTTPS (DoH) engine to actively intercept and block NSFW (Porn) content and advertisements per user.
* 🔐 Panel Auth Protection: Secure SHA-256 hashed panel password with built-in brute-force protection m